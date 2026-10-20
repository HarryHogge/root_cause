# SWITCHIN_TRACE_EXPLANATION.md

Attachment 52355, text, 18 KB, added 2026-04-02 by Scott Hunter.

# Understanding the SwitchedIn Trace Tables

## Overview

The crash dump captures a circular buffer of the most recent 64 "switched-in" events before a system crash. These events represent two distinct types of system activity:
1. **FreeRTOS task context switches** - when the scheduler gives the CPU to a task
2. **ISR entry points** - when hardware interrupts preempt the current task

## What Gets Captured

### Task Switch-In Events (TCB Numbers < 1000)
When FreeRTOS performs a **context switch** and gives the CPU to a task, the trace records:
- **Timestamp**: `ReadCoreTimer()` value (100MHz, 10ns resolution)
- **TCB Number**: Task Control Block unique identifier (e.g., 13, 15, 8)

This happens via the FreeRTOS trace hook `TRACE_EVENT_TASK_SWITCHED_IN` which calls `log_trace_event()`.

### ISR Entry Events (TCB Numbers >= 1000)
When a hardware interrupt fires, the trace records:
- **Timestamp**: `ReadCoreTimer()` value at ISR entry
- **ISR Number + 1000**: To differentiate from task numbers (e.g., 1146 = ISR 146 = UART2 Rx, 1004 = ISR 4 = Timer1)

This happens via `isrIncrement()` which calls `log_isr_as_trace_event()` on every ISR entry.

## What Does NOT Get Captured

### 1. Task Switch-Out Events
The trace does **not** record when a task is switched out (loses the CPU). Once a task is switched in, it remains the "active task" until another switch-in event occurs.

### 2. ISR Exit/Return Events
When an ISR completes and returns, there is **no trace event recorded**. The CPU simply returns to whatever was running before (the active task), and that task continues executing without a new trace entry.

### 3. Task Resumption After ISR
If an ISR interrupts Task A and then returns to Task A, you will see:
- Task A switch-in event (TCB = A)
- ISR entry event (TCB = 1000 + ISR_NUM)
- *(No event for ISR return to Task A)*
- *(Task A continues running with no new trace entry)*

The next trace entry will be either:
- Another ISR that interrupts Task A
- A different task being switched in by FreeRTOS

### Important: Task-to-Task Preemption IS Captured
**This is different from task preemption by another task.** If a high-priority task preempts a low-priority task:
- Low Priority Task A switch-in event (TCB = A)
- High Priority Task B switch-in event (TCB = B) - **explicit FreeRTOS context switch**
- Low Priority Task A switch-in event (TCB = A) - **explicit switch back when B blocks/completes**

When FreeRTOS switches from one task to another task (not an ISR), **both the preemption and the resumption generate switch-in events**. This is because FreeRTOS explicitly calls `vTaskSwitchContext()` in both directions.

**Summary**:
- **ISR → Task**: No trace event (hardware return)
- **Task → Task**: Trace event (FreeRTOS context switch)

## Reading the Trace Tables

### Example Trace Sequence
```
switch in: switched-in ticks
switch in: 28) 3645764895 3645765475 3645766202 3645766969
switch in: 32) 3645771974 3645779959 3645787944 3645795932

switch in: switched-in TCBNum (ISRs are +1000)
switch in: 28)     1004       13       15        8
switch in: 32)     1146     1146     1146     1146
```

### Interpretation

**Index 28 (tick 3645764895, TCB 1004)**
- Timer1 ISR (ISR #4) fired
- Interrupted whatever was running before
- ISR likely made tasks ready for scheduling

**Index 29 (tick 3645765475, TCB 13) - 580 ticks (5.8μs) later**
- FreeRTOS **context switched to Task 13**
- Task 13 was made ready (possibly by Timer1 ISR)
- Task 13 begins executing

**Index 30 (tick 3645766202, TCB 15) - 727 ticks (7.3μs) later**
- FreeRTOS **context switched to Task 15**
- Task 13 is no longer running (but we don't see a "switch-out" event)
- Task 15 begins executing

**Index 31 (tick 3645766969, TCB 8) - 767 ticks (7.7μs) later**
- FreeRTOS **context switched to Task 8 (IDLE task)**
- All higher priority tasks finished their work
- IDLE task begins executing

**Index 32 (tick 3645771974, TCB 1146) - 5005 ticks (50μs) later**
- UART2 Rx ISR (ISR #146) fired
- **Task 8 (IDLE) is still the active task** but now interrupted
- ISR handles received character
- ISR returns to Task 8 *(no trace event)*
- Task 8 continues running

**Index 33-35 (TCB 1146, 1146, 1146) - ~80μs intervals**
- UART2 Rx ISR fires again... and again... and again
- Each character received triggers the ISR
- **Task 8 remains the active task** throughout
- Task 8 never gets CPU time to execute because ISRs arrive every 80μs
- Each ISR completes and returns to Task 8 between characters

## Key Concepts

### Active Task vs. Executing Task
- **Active Task**: The task that FreeRTOS has scheduled (last "switched-in" task number < 1000)
- **Executing Code**: Could be the active task OR an ISR that interrupted it

### ISR Burst Pattern
When you see repeating ISR numbers (e.g., 1146, 1146, 1146), this means:
1. The same interrupt is firing repeatedly
2. The "active task" (last non-ISR entry) remains unchanged
3. Each ISR completes and returns to the active task
4. The next character/event triggers another ISR before the task can make progress

This is **normal behavior** for high-speed data sources (UART at 125kbps = 80μs per character).

### Task Scheduling Opportunities
FreeRTOS can only reschedule tasks at specific times:
1. **Task yields explicitly** (`vTaskDelay()`, blocking on queue, etc.)
2. **ISR makes higher-priority task ready** and ISR exit triggers scheduler
3. **Tick interrupt** (Timer1) occurs, triggering scheduler

During continuous ISR bursts (like UART reception), tasks may be starved of CPU time even though they are "switched in" because they never get a chance to execute between ISR invocations.

## Timing Analysis

The timestamps use the MIPS CP0 Count register:
- **Clock Rate**: 100 MHz (CPU clock / 2 = 200MHz / 2)
- **Resolution**: 10 nanoseconds per tick
- **Wraparound**: Every ~43 seconds (2^32 / 100,000,000)

To calculate time between events:
```
Δt (microseconds) = (tick₂ - tick₁) / 100
```

### Typical Timings Observed
- **Task context switch overhead**: ~5-8 μs
- **UART character spacing** (125 kbps): **~79.85 μs** (7985 ticks ±2 ticks)
  - Very consistent - shows continuous serial data stream
  - Theoretical: 80 μs per character at 125 kbps with 8N1 framing
- **Timer1 tick period**: **Exactly 1.000 ms** (100,000 ticks ±4 ticks)
  - Highly consistent - provides reliable timing reference throughout trace
  - Timer1 ISR execution time: ~1.06 μs (measured from Index 10→11)
- **ISR execution time**: Difference between consecutive ISRs minus expected interval

## Limitations

1. **No execution duration**: Can't directly measure how long a task runs
2. **No ISR duration**: Can't directly measure ISR execution time (unless followed by another event)
3. **No switch-out reason**: Can't tell why FreeRTOS switched away from a task
4. **No ISR preemption visibility**: When ISR B follows ISR A, can't directly see if:
   - ISR A completed and returned to task, then ISR B fired, OR
   - ISR B (higher priority) preempted ISR A mid-execution
   - **Heuristic**: Check the time delta between entries:
     - Very short (few μs): ISR A likely preempted by ISR B (didn't have time to complete)
     - Longer (tens of μs or more): ISR A probably completed before ISR B fired
   - Example: 1.06 μs between ISRs strongly suggests preemption; 79 μs suggests completion
5. **Limited history**: Only last 64 events (typically 3-10 ms of history depending on activity)
6. **Missing events**: Very rapid events might be lost if trace buffer processing lags

## Use Cases

### Good For
- Identifying which task was running when crash occurred
- Detecting ISR starvation (task repeatedly interrupted)
- Measuring ISR arrival patterns and frequencies
- Understanding task scheduling sequence
- Correlating crashes with specific task or ISR activity

### Not Suitable For
- Measuring exact task execution time
- Determining task CPU utilization
- Identifying blocking/waiting time
- Detailed profiling (use dedicated profiling tools)

## Complete Example: Real Crash Dump Analysis

### Raw Trace Data from Crash Dump

```
switch in: switched-in ticks
switch in:  0) 2605515231 2605523219 2605531203 2605539190
switch in:  4) 2605547176 2605555161 2605563147 2605571133
switch in:  8) 2605579119 2605587104 2605594989 2605595095
switch in: 12) 2605595868 2605596836 2605597546 2605598335
switch in: 16) 2605603083 2605611063 2605619048 2605627832
switch in: 20) 2605635818 2605643803 2605651789 2605659773
switch in: 24) 2605667760 2605694990 2605695676 2605696407
switch in: 28) 2605700586 2605701478 2605708148 2605794994
switch in: 32) 2605795644 2605797189 2605798325 2605800248
switch in: 36) 2605810160 2605820446 2605894996 2605895638
switch in: 40) 2605897047 2605897820 2605898556 2605931819
switch in: 44) 2605974483 2605994983 2605995595 2605997808
switch in: 48) 2605998579 2606005097 2606025338 2606045576
switch in: 52) 2606094983 2606095595 2606097767 2606098547
switch in: 56) 2606159721 2606167671 2606175659 2606183645
switch in: 60) 2606191631 2606194983 2606195671 2606196406

switch in: switched-in TCBNum (ISRs are +1000)
switch in:  0)     1146     1146     1146     1146
switch in:  4)     1146     1146     1146     1146
switch in:  8)     1146     1146     1004     1146
switch in: 12)        5       13       15        8
switch in: 16)     1146     1146     1146     1146
switch in: 20)     1146     1146     1146     1146
switch in: 24)     1146     1004       13       28
switch in: 28)       15        8     1151     1004
switch in: 32)       13     1151       15        8
switch in: 36)     1151     1151     1004       13
switch in: 40)       15        8     1151     1151
switch in: 44)     1151     1004       13       15
switch in: 48)        8     1151     1151     1151
switch in: 52)     1004       13       15        8
switch in: 56)     1146     1146     1146     1146
switch in: 60)     1146     1004       13       23
```

### Supporting Reference Data

**Complete ISR Table (from crash dump):**
```
[09:26:49.663 43.663] ISR::  0,  Core Timer,       1,          1
[09:26:49.744 43.746] ISR::  4,      Timer1,   43744,      43744
[09:26:49.845 43.845] ISR:: 23,  External 4,       1,          1
[09:26:49.945 43.947] ISR::146,    UART2 Rx,  319896,     319896
[09:26:50.046 44.046] ISR::147,    UART2 Tx,    6496,       6496
[09:26:50.146 44.146] ISR::151,         CAN,   11706,      11706
[09:26:50.244 44.245] ISR::153,    Ethernet,     344,        344
[09:26:50.344 44.346] ISR::159,    UART3 Tx,      50,         50
[09:26:50.444 44.446] ISR::181,    UART5 Tx,     215,        215
[09:26:50.546 44.546] ISR::190,    UART6 Tx,     138,        138
```

**Mapping for trace (add 1000 to ISR number):**
- ISR 0 = Core Timer → 1000 in trace
- ISR 4 = Timer1 → 1004 in trace
- ISR 23 = External 4 → 1023 in trace
- ISR 146 = UART2 Rx → 1146 in trace
- ISR 147 = UART2 Tx → 1147 in trace
- ISR 151 = CAN → 1151 in trace
- ISR 153 = Ethernet → 1153 in trace
- ISR 159 = UART3 Tx → 1159 in trace
- ISR 181 = UART5 Tx → 1181 in trace
- ISR 190 = UART6 Tx → 1190 in trace

**Complete TCB-Name Table (from crash dump):**
```
TCB-Name:   1) taskFileStr SP:0x8003F980
TCB-Name:   2) OneHz SP:0x800405F8
TCB-Name:   3) User IO SP:0x80040DA8
TCB-Name:   4) StatusText SP:0x80041450
TCB-Name:   5) SYS_TMR Tas SP:0x80041AA8
TCB-Name:   6) DelayedInit SP:0x80042A20
TCB-Name:   7) Watchdog SP:0x80043138
TCB-Name:   8) IDLE SP:0x80043968
TCB-Name:   9) Tmr Svc SP:0x800442C8
TCB-Name:  10) NetworkSwit SP:0x80044D40
TCB-Name:  11) TCP/IP Stac SP:0x80046C58
TCB-Name:  12) FTP Server SP:0x80047C88
TCB-Name:  13) Can Task SP:0x80049378
TCB-Name:  14) taskDataLog SP:0x8004A420
TCB-Name:  15) SpareIO SP:0x8004ABE0
TCB-Name:  16) Udp:50011:l SP:0x80057B88
TCB-Name:  17) Udp:50200:c SP:0x8005B7A8
TCB-Name:  18) Udp:50100:m SP:0x8005CAC8
TCB-Name:  19) Udp:50005:m SP:0x8005F030
TCB-Name:  20) XComm Ser I SP:0x800600D0
TCB-Name:  21) XComm Ser O SP:0x80060AB8
TCB-Name:  22) Remote Air SP:0x80060FE0
TCB-Name:  23) XComm Misc SP:0x80061F58
TCB-Name:  24) XComm Fuel  SP:0x800626D8
TCB-Name:  25) XComm Geo/K SP:0x800630A8
TCB-Name:  26) XComm Ping SP:0x80063918
TCB-Name:  27) XComm Vtol SP:0x80064788
TCB-Name:  28) oem7_ser SP:0x80068210
TCB-Name:  29) AGNSS Rcvrs SP:0x80068CE0
TCB-Name:  30) GetFDR SP:0x80069F98
```

**Crash Context:**
```
current task: can
current func: system
func state: (24) system 204    <- Exception code 4 (AdEL)
```

### Detailed Analysis

**Indices 0-11: Continuous UART Reception (UART2 Rx ISR)**
```
Index 0-1:   ~79.88 μs  (1146 → 1146)  UART character spacing at 125kbps
Index 1-2:   ~79.84 μs  (1146 → 1146)  
Index 2-3:   ~79.87 μs  (1146 → 1146)
...continuous UART reception...
Index 8-9:   ~79.85 μs  (1146 → 1146)
Index 9-10:  ~78.85 μs  (1146 → 1004)  Timer1 fires
```
- Active task unknown (was running before trace history started)
- UART receiving data at 125kbps (80μs per character)
- No FreeRTOS scheduling - ISRs complete faster than scheduler can intervene
- Between consecutive ISR entries, the previous ISR has either:
  - Completed and returned to the active task, OR
  - Was preempted by a higher-priority interrupt (if priorities allow)

**Index 10: Timer1 Tick (ISR 1004)**
```
Timestamp: 2605594989
Delta:     78.85 μs from last UART ISR entry
```
- Periodic Timer1 interrupt fires
- Either interrupted the active task (if UART ISR completed), OR
- Preempted the UART ISR (if Timer1 has higher priority than UART2 Rx)
- Makes tasks ready for scheduling (typical tick behavior)

**Index 11: Return to UART Reception (ISR 1146)**
```
Timestamp: 2605595095
Delta:     1.06 μs from Timer1 ISR entry
```
- Timer1 completed in 1.06 μs (consistent with measured Timer1 execution time)
- Another UART character arrived immediately after Timer1 completed
- Shows UART data stream continues regardless of Timer1 interruption

**Indices 12-15: Task Scheduling Window**
```
Index 12:   879 ticks = 8.79 μs   (1146 → 5)   Switch to SYS_TMR Task
Index 13:   968 ticks = 9.68 μs   (5 → 13)     Switch to Can Task  
Index 14:   710 ticks = 7.10 μs   (13 → 15)    Switch to SpareIO
Index 15:   789 ticks = 7.89 μs   (15 → 8)     Switch to IDLE
```
- Timer1 ISR made tasks ready, triggering FreeRTOS scheduler
- Rapid task switches: SYS_TMR → Can → SpareIO → IDLE
- Each task likely ran briefly then yielded/blocked
- Total scheduling window: **33.46 μs** before next interrupt

**Indices 16-23: UART Burst Resumes**
```
Index 16-24: Eight UART ISRs (1146) with ~79-80 μs spacing
```
- IDLE task (8) is active but repeatedly interrupted
- UART reception continues at 125kbps
- IDLE never gets CPU time between ISR invocations

**Index 24: Timer1 Tick Again**
```
Index 24:   27,230 ticks = 272.3 μs from previous Timer1
Delta:      79 μs from last UART ISR (1146 → 1004)
```
- Another periodic Timer1 tick
- Note: Only **272 μs** between Timer1 ISRs (seems short for typical tick)

**Indices 25-27: Quick Task Switches**
```
Index 25:   686 ticks = 6.86 μs   (1004 → 13)   Can Task
Index 26:   731 ticks = 7.31 μs   (13 → 28)     oem7_ser (GPS serial)
Index 27:   892 ticks = 8.92 μs   (28 → 15)     SpareIO
Index 28:   892 ticks = 8.92 μs   (15 → 8)      IDLE
```
- Tasks scheduled: Can → oem7_ser → SpareIO → IDLE
- Total: **31.93 μs** of task switching

**Indices 29-63: Mixed ISR and Task Activity**
```
Index 29-51: Alternating between CAN ISR (1151) and tasks
             - CAN ISR fires frequently (processing CAN messages)
             - Timer1 ISRs trigger periodic rescheduling
             - Tasks 13, 15, 8 repeatedly scheduled

Index 56-60: Return to UART burst (four consecutive 1146 entries)
             - Back to continuous UART reception at 80μs intervals

Index 60-63: Final sequence before crash
   60:  (1146)     UART2 Rx ISR
   61:  (1004)     Timer1 ISR - 33.52 μs later
   62:  (13)       Can Task scheduled - 6.88 μs after Timer1
   63:  (23)       XComm Misc task - 7.35 μs after Can Task
```

### Key Observations

1. **Multiple ISR Sources**: UART2 Rx (1146) and CAN (1151) dominate the trace with Timer1 (1004) providing periodic scheduling points

2. **High Interrupt Frequency, Low CPU Utilization**: 
   - UART: 2,228,697 total interrupts (125kbps serial = ~12,500 interrupts/sec)
   - CAN: 195,042 total interrupts
   - IDLE task getting 47-611 μs of runtime between interrupts
   - System efficiently servicing I/O with minimal CPU overhead

3. **Normal Interrupt Activity**: 
   - IDLE task runs when no higher-priority tasks are ready (47-611 μs bursts observed)
   - IDLE interrupted by ISRs is expected behavior - it's the lowest priority task
   - Higher priority tasks (Can, SpareIO, etc.) get scheduled after Timer1 ticks
   - No evidence of task starvation - system responding to normal I/O load

4. **Crash Context**:
   - Last active task: **XComm Misc (TCB 23)**
   - Exception occurred: **system 204** = Exception code **4 (AdEL - Address Error Load)**
   - Current task shown as "can" in crash dump (tasks switched during exception handling)
   - Exception likely occurred very shortly after final trace entry

5. **Timing Summary**:
   - Total trace span: 681,175 ticks = **6.81 milliseconds**
   - UART character rate: ~80 μs/char = 125 kbps (correct)
   - Task switch overhead: 7-9 μs per switch
   - Typical scheduling window between ISR bursts: 30-35 μs

### Conclusions

This trace shows a system under **heavy interrupt load** with continuous UART reception and frequent CAN activity. Tasks are being scheduled appropriately by FreeRTOS when Timer1 ticks occur, but actual task execution time is minimal due to continuous ISR preemption. The crash occurred in XComm Misc task, likely during normal processing after being switched in by the scheduler.

---

*This trace mechanism provides valuable crash context but is not a replacement for detailed runtime profiling or performance analysis tools.*
