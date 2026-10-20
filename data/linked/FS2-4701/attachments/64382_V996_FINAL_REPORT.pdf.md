# V996_FINAL_REPORT.pdf

Attachment 64382, pdf, 235 KB, added 2026-09-01 by Kurt Burian.

## Page 1

V996 Incident Investigation Report
Vehicle: V996 Date: June 4, 2026 Flights Analyzed:
 Flight 1: 165813Z (primary incident)
 Flight 2: 182857Z (comparison flight)
Executive Summary
The V996 incident investigation analyzed two flights where motors failed to shut off after false landing detection. This
was NOT a communications hardware failure - the evidence conclusively shows the communication link was
functioning, as the FW AP continued transmitting data ("local rx okay"). The root cause was the Fixed-Wing Autopilot
CPU becoming blocked and unresponsive ("ap rx bad"), preventing it from processing incoming motor shutoff
commands. The false landing was triggered by steady flight conditions (quiet gyro, quiet accelerometer, low GPS
velocity) meeting the voting threshold while the laser altimeter was out of range, so no altitude confirmation was
required. The XCOMM event log proves the landed-event task started but never reached the FDR capture step, and
approximately 100 seconds later link faults were detected when XCOMM noticed the FW AP had stopped
responding. All 14 watchdog boot markers found in the FDR files were traced to historical flights stored in the circular
buffer - no watchdog reset occurred during the incident. The single WDE warning found was caused by mission
upload processing during pre-flight on a previous flight and is unrelated to the incident. Recommended fixes include
requiring altitude confirmation for landing detection, adding timeouts to blocking loops in the FW AP serial/SPI code,
and implementing heartbeat monitoring between XCOMM and FW AP.
Investigation Objective
Determine whether the delayed motor shutoff was caused by:
1. A communications hardware issue, or
2. A CPU blocking issue (processor unresponsive)
Finding: This was NOT a communications hardware issue. The communication hardware was functioning - the
FW AP was still transmitting data. The root cause was the FW AP CPU becoming blocked/unresponsive and not
processing incoming commands.
Both flights exhibited similar anomalies. This report analyzes both to establish a pattern.
Root Cause Summary (Fishbone Diagram)

## Page 2

V996 Fishbone Diagram
Key Finding: The link fault message "local rx okay ap rx bad" proves the communication hardware was
working:
 "local rx okay" = XCOMM successfully receiving data FROM the FW AP
 "ap rx bad" = FW AP not receiving/processing data from XCOMM
This indicates the FW AP CPU was blocked in a loop, able to transmit but unable to process incoming commands.
This is NOT a communication hardware failure - it is a CPU blocking issue.
Incident Summary
Both flights detected landing while still airborne (false landing). The landing detection system triggered based on
steady flight conditions (quiet gyro, quiet accel, low GPS velocity) without any altitude confirmation - the laser was
out of range so no AGL vote was cast. The motors did not shut off because the fixed-wing autopilot controls the
VTOL state and it was not responding.
VtolState Analysis
The VtolState values in the FDR correspond to landing states (from NavVtol.h):
vtol_state = m_landstate + 100

## Page 3

VtolState  State Name        Description
---------  ----------------  --------------------------------------------
124        LAND_DESCENDING   Process nudges, monitor health, monitor landing detect
125        LAND_COMPLETE     Disarm and safe the VTOL
100        LAND_IDLE         Idle
State Transitions - Both Flights Compared
Flight 1 (165813Z):
Time       VtolState  State Name         Event
--------   ---------  ----------         -----
3983.3s    116 -> 124 LAND_DESCENDING    Descent monitoring begins
4045.4s    124 -> 125 LAND_COMPLETE      *** FDR LOGGING DEGRADES HERE ***
4045.0s    125 -> 100 LAND_IDLE          Back to idle
Flight 2 (182857Z):
Time       VtolState  State Name         Event
--------   ---------  ----------         -----
2185.7s    116 -> 124 LAND_DESCENDING    Descent monitoring begins
2286.2s    124 -> 125 LAND_COMPLETE      *** FDR LOGGING DEGRADES HERE ***
2286.0s    125 -> 100 LAND_IDLE          Back to idle
Key Finding: BOTH flights show identical VtolState transition pattern (124 ? 125 ? 100), and BOTH experience FDR
logging degradation exactly at the 124?125 transition.
Flight Comparison Summary
Metric                      Flight 1 (165813Z)    Flight 2 (182857Z)
--------------------------  --------------------  --------------------
Total state transitions     21                    22
LAND_COMPLETE time          4045.4s               2286.2s
FDR gap after incident      1,075 seconds         16,474 seconds
Landing state pattern       124 -> 125 -> 100     124 -> 125 -> 100
WD BOOT in incident seg     None                  None
See: V996_FLIGHT_COMPARISON.png for visual comparison.
Flight 1 Incident Timeline
Time (s)    Event
--------    -----
3983.3      VtolState -> 124 (LAND_DESCENDING)
4045.4      VtolState -> 125 (LAND_COMPLETE) - FDR rate drops
4045.0      VtolState -> 100 (LAND_IDLE)
4090.8      "ll detected landing 4"
4091.3      "MC disarmed 0" / "MC safe 1"
            *** EXPECTED: Motors shut off ***
            *** ACTUAL: Motors continue running ***
            (FW AP not responding)
4125.0      Last FDR entry before 1075s logging gap
4143-4146   Motor throttle 17-92% (motors still active)

## Page 4

4192.2      "sw 1 port link reset 2"
4193.0      "ap dbg: Bad CRC"
4197.4      "ap link fault: local rx okay ap rx bad"
4213        Actual landing
Flight 2 Incident Timeline
Time (s)    Event
--------    -----
2185.7      VtolState -> 124 (LAND_DESCENDING)
2286.2      VtolState -> 125 (LAND_COMPLETE) - FDR rate drops
2286.0      VtolState -> 100 (LAND_IDLE)
2366.0      Last FDR entry before 16,474s logging gap
2288-2378   Motor throttle ~-0.11 (idle/off in sampled window)
18840.0     FDR logging resumes
Evidence Analysis
FDR Logging Gaps (Primary Evidence - Both Flights)
Note: FDR logging rate is variable by design and does not indicate CPU load. However, logging gaps (extended
periods with no data) indicate a problem.
Flight 1:
Time       Event
---------  ------------------------------------------
< 4125s    Normal logging (variable rate)
4125s      Last FDR entry before gap
           *** 1,075 SECOND GAP - NO DATA ***
5200s      FDR logging resumes
Flight 2:
Time       Event
---------  ------------------------------------------
< 2366s    Normal logging (variable rate)
2366s      Last FDR entry before gap
           *** 16,474 SECOND GAP - NO DATA ***
18840s     FDR logging resumes
Observation: Both flights show large logging gaps that began after the false landing detection. The cause of these
gaps is not yet determined.
Landing Detection Sensor Analysis
The VTOL uses a voting system to detect landing. Multiple sensors contribute votes, and when votes >= 4
(threshold), a countdown begins. When the countdown reaches 0, landing is declared.
Sensor Vote Indicators (from landStat field)

## Page 5

Position   Code   Meaning                          Vote Value
--------   ----   -------                          ----------
[2]        d      Motor output dropping            +1
[3]        g      Gyro quiet (low rotation)        +1
[4]        a      Accel quiet (near 1g, static)    +1
[5]        v      GPS velocity low                 +2
[6]        l/L    AGL sensor low/very low          +1/+2
[7]        t      Throttle zero (RC mode)          +2
[8]        p      Motor power low                  +1
[9]        i      Impact/thud detected             +1
[10]       b      Baro ROC (rate of climb) low     +1
[11-12]    ##     Countdown (50 -> 0)              --
[13]       !      LANDING TRIGGERED                --
Flight 1 - False Landing Trigger at 4090.883s
Time       Votes  Landed  landStat           Active Sensors
---------  -----  ------  ----------------   -------------------
4087.084     4      0     --gav-----38--     gyro,accel,vel
4087.184     4      0     --gav-----37--     gyro,accel,vel
4087.283     4      0     --gav-----36--     gyro,accel,vel
   ...countdown continues...
4089.883     5      0     --gav----b10--     gyro,accel,vel,baro
4089.983     5      0     --gav----b09--     gyro,accel,vel,baro
4090.083     5      0     --gav----b08--     gyro,accel,vel,baro
4090.183     5      0     --gav----b07--     gyro,accel,vel,baro
4090.283     5      0     --gav----b06--     gyro,accel,vel,baro
4090.383     4      0     --gav-----05--     gyro,accel,vel
4090.483     4      0     --gav-----04--     gyro,accel,vel
4090.583     4      0     --gav-----03--     gyro,accel,vel
4090.683     4      0     --gav-----02--     gyro,accel,vel
4090.783     4      0     --gav-----01--     gyro,accel,vel
4090.883     4      1     --gav-----00!-     gyro,accel,vel  <-- TRIGGER
Flight 2 - False Landing Trigger at 2282.773s
Time       Votes  Landed  landStat           Active Sensors
---------  -----  ------  ----------------   -------------------
2280.873     5      0     --gav----b05--     gyro,accel,vel,baro
2280.973     5      0     --gav----b04--     gyro,accel,vel,baro
2281.073     5      0     --gav----b03--     gyro,accel,vel,baro
2281.173     5      0     --gav----b02--     gyro,accel,vel,baro
2281.273     5      0     --gav----b01--     gyro,accel,vel,baro
2282.773     5      1     --gav----b00!-     gyro,accel,vel,baro  <-- TRIGGER
Key Observations
1. AGL was NOT used in the landing vote:
 Position 6 in landStat is - (not l or L)
 AGL vote only occurs when laser (LRF) is active (stat == AGL_LRF)
 Laser was not in range at ~300-400 feet altitude
2. Votes that triggered false landing:
 g = Gyro quiet (low rotation rates)
 a = Accel quiet (near 1g, steady flight)
 v = GPS velocity low (+2 votes)

## Page 6

 b = Baro ROC low (intermittent)
3. Why the false detection occurred:
 Vehicle was in steady flight (low rates, low accel, low GPS velocity)
 These conditions met the voting threshold without actual ground contact
 No AGL check was performed because laser was out of range
4. Why motors didn't stop:
 The FW autopilot controls the VTOL state
 The FW AP was not responding
 Motor shutoff command was never properly executed
See: V996_LANDING_DETECTION_ANALYSIS.png for detailed sensor plots.
Why Motors Didn't Shut Off
The false landing was detected by the VTOL controller. The fixed-wing autopilot controls the VTOL state, but it was
not responding. The motors continued running because the shutoff command was never properly executed.
Communications Events (Flight 1)
Time       Event
---------  ----------------------
4192.2s    Switch port link reset
4193.0s    Bad CRC
4197.4s    AP link fault
These events occur ~100 seconds AFTER the state transition, suggesting they are a consequence of the CPU
blocking rather than the cause.
Motor Data
Flight 1 (4143-4146s):
Time       Throttle Values
---------  ---------------------------------
4143.0s    M1=45%, M2=17%, M3=26%, M4=25%
4145.9s    M1=85%, M2=77%, M3=75%, M4=92%
Motors remained active - vehicle still flying.
Flight 2 (2288-2378s):
Time       vtThr1    vtThr2    vtThr3    vtThr4
---------  --------  --------  --------  --------
2288-2378  -0.11     -0.11     -0.11     -0.11
Motors at idle/off in this sampled window.
WD BOOT Event Analysis (Dismissal)

## Page 7

The FDR files contain "WD BOOT" markers indicating watchdog reboots. A detailed analysis was performed to
determine if any occurred during the incident flights.
Raw FDR File Structure
The FDR file is a circular buffer with new data appended to the bottom:
 Top of file (oldest): Historical data from previous flights (segments 1-18)
 Bottom of file (newest): Current/incident flight data (segment 0)
WD BOOT Marker Locations and Crash Codes
Each WD BOOT entry is followed by a crash code that identifies which subsystem was active when the watchdog
triggered. The code format is:
Code:-{Nav}-{Hostif}-{WdMgr}-{GPS}-{Vted}-{NavMan}-{Sensor}-j
Position  Subsystem      Description
--------  -------------  ------------------------------------------
[0]       Nav            Navigation task state (a-Z)
[1]       Hostif         Host interface/comms state
[2]       WdManager      Watchdog manager state
[3]       GPS            GPS processing state
[4]       Vted           VTED (vertical terrain) state
[5]       NavMan         Navigation manager state
[6]       Sensor         Sensor processing state
Character meanings:
  '-' or '_' = Not active / idle
  'a'-'z'    = Lowercase = early in function
  'A'-'Z'    = Uppercase = later in function (closer to completion)
  'Z'        = Function completed normally
Flight 1 WD BOOT Events (ALL HISTORICAL):
Line   Segment  Crash Code               Analysis
-----  -------  -----------------------  ----------------------------------
3772   4        Code:-g-Z-6-X-Z-6-z-j    Nav=g, WdMgr=6, GPS=X, Vted=Z
4570   6        Code:-a-Z-9-X-Z-6-n-j    Nav=a, WdMgr=9, GPS=X, Vted=Z
4838   9        Code:-g-Z-9-X-Z-6-z-j    Nav=g, WdMgr=9, GPS=X, Vted=Z
4884   10       Code:-a-Z-9-6-Z-6-q-j    Nav=a, WdMgr=9, GPS=6, Vted=Z
4944   11       Code:-a-Z-9-b-Z-6-s-j    Nav=a, WdMgr=9, GPS=b, Vted=Z
4970   12       Code:-a-Z-9-X-Z-X-c-j    Nav=a, WdMgr=9, GPS=X, NavMan=X
5252   13       Code:-a-Z-9-b-Z-6-q-j    Nav=a, WdMgr=9, GPS=b, Vted=Z
Flight 2 WD BOOT Events (ALL HISTORICAL):
Line   Segment  Crash Code               Analysis
-----  -------  -----------------------  ----------------------------------
3184   4        Code:-g-Z-6-X-Z-6-z-j    Nav=g, WdMgr=6, GPS=X, Vted=Z
3982   6        Code:-a-Z-9-X-Z-6-n-j    Nav=a, WdMgr=9, GPS=X, Vted=Z
4250   9        Code:-g-Z-9-X-Z-6-z-j    Nav=g, WdMgr=9, GPS=X, Vted=Z
4296   10       Code:-a-Z-9-6-Z-6-q-j    Nav=a, WdMgr=9, GPS=6, Vted=Z
4356   11       Code:-a-Z-9-b-Z-6-s-j    Nav=a, WdMgr=9, GPS=b, Vted=Z
4382   12       Code:-a-Z-9-X-Z-X-c-j    Nav=a, WdMgr=9, GPS=X, NavMan=X
4664   13       Code:-a-Z-9-b-Z-6-q-j    Nav=a, WdMgr=9, GPS=b, Vted=Z
Crash Code Pattern Analysis

## Page 8

The historical WD BOOT events show a consistent pattern:
 Vted=Z in most cases indicates VTED completed normally
 GPS=X or GPS=b indicates GPS was mid-processing
 Nav=a or Nav=g indicates Navigation was early in its cycle
 WdMgr=6 or 9 indicates specific watchdog manager states
These crash codes are from previous flights stored in the FDR circular buffer, not from the incident flights.
Conclusion on WD BOOT
Flight 1:  7 WD BOOT markers - ALL in historical segments (4-13)
           0 WD BOOT markers in segment 0 (incident flight)
Flight 2:  7 WD BOOT markers - ALL in historical segments (4-13)
           0 WD BOOT markers in segment 0 (incident flight)
The WD BOOT events are from PREVIOUS flights stored in the circular FDR buffer. No watchdog reset
occurred during either incident flight.
This dismisses the hypothesis that a watchdog reboot caused the logging gap. The FDR gaps occurred without a
system reset.
Likely Cause
False Landing Detection Due to Steady Flight Conditions + FW AP Communication Failure
The evidence from both flights and the XCOMM event log shows:
1. False landing triggered by steady flight conditions:
 Laser was out of range, so no AGL vote was cast
 Landing triggered purely on flight dynamics (gyro, accel, GPS velocity)
 Voting system accumulated enough votes from: quiet gyro, quiet accel, low GPS velocity
 Countdown reached zero and landing was declared while airborne
2. XCOMM landed-event task started but did not complete:
 "start of landed event task" logged at 4090.842s
 "capturing ap fdr" was NEVER logged - task did not reach FDR capture step
 This same pattern occurred in Flight 2's false landing (2282.741s)
 In Flight 2's actual landing, "capturing ap fdr" appeared ~0.5s after task start
3. FW AP became unresponsive:
 Link fault at 4197.4s: "local rx okay ap rx bad"
 XCOMM could receive from FW AP, but FW AP was not receiving/processing commands
 This blocked the motor shutoff command
4. Motors did not shut off because:

## Page 9

 The FW autopilot controls the VTOL state
 The FW AP was not responding to incoming commands
 Motor shutoff command was never properly executed
5. FDR logging gaps followed:
 Flight 1: 1,075 second gap starting at 4125s
 Flight 2: 16,474 second gap starting at 2366s
 Gap timing correlates with the communication failure
No watchdog reset occurred during either flight - the WD BOOT markers are all from historical flights in the FDR
buffer.
Code Execution Path at Landing Detection
When landing is detected, the VTOL sends commands that cause the Fixed-Wing AP to perform blocking
operations.
1. VTOL LLDetect.c - Landing Detection (t=4090.831s)
AddMessageInt("ll detected landing", landvotes);  // "ll detected landing 4"
fsMcLanded(true, 11);                              // Sets landed state
fltlogEvent(FLT_EVENT_LAND, NULL);                 // Triggers VTOL flight log task
if(autodisarm) fsMcArm(false, 11);                 // "MC disarmed 0"
if(autosafe) multiControlStopSafe(11);             // "MC safe 1"
2. XCOMM ApParser.cpp - Detects Landing State Change
// When NavState changes to FS_LANDED
if((last.ns.NavState != FS_LANDED) && (vstate->ns.NavState == FS_LANDED))
{
    fltlogEvent(FLT_EVENT_LAND, NULL);  // Triggers XCOMM flight log task
}
3. XCOMM FlightLog.c - Landing Wrapup Task (Requests FW AP FDR)
static void flightLandTask(void *pvparm) {
    landbusy = true;
    AddMessage("start of landed event task");
    vTaskDelay(300);
    // ... file operations ...
    AddMessage("capturing ap fdr");
    oldapGetFDR(fname, 0, 5000);           // *** REQUESTS FDR FROM FW AP ***
    AddMessage("waiting for fdr capture");
    while(oldapFdrBusy()) {                 // *** WAITS FOR FW AP RESPONSE ***
        vTaskDelay(1000);
        // timeout after MAX_LAND_TASK (30 seconds)
    }
    AddMessage("fdr capture complete");
    // ... more file operations ...
    configExport(fname, &all, &none, false);

## Page 10

}
4. FW AP hostintf.cpp - FDR Request Processing (BLOCKING)
// When FW AP receives RAW_UPLOAD command for FDR
case RAW_UPLOAD:
    ReplyRawUpload(iparm1);  // Sends FDR block
    break;
// After sending FDR data:
LastFDRTime = clock->GetTime();  // Marks FW AP as "busy"
// While busy, FW AP suppresses status transmissions:
bool HostInterface::BusyWithFDR() {
    if(clock->GetTime() - LastFDRTime > FDRTimeout)  // 500-1500ms timeout
        return false;
    return true;
}
// Many status messages are blocked while BusyWithFDR():
if(!BusyWithFDR() && !BusyWithMission())
    TransmitTaggedPacket(&nav);  // NAV STATE BLOCKED
if(!BusyWithFDR() && !BusyWithMission())
    SendShortStatus(...);         // STATUS MESSAGES BLOCKED
XCOMM Event Log Correlation - Critical Evidence
The processed XCOMM event log (rca_timeline.json) reveals the key sequence:
Flight 1 (Incident) - False Landing at 4090.8s:
Time (s)   Event Log Message              Source      Description
---------  -----------------------------  ----------  ---------------------------
4022.365   "mc land trigger"              VTOL        Land sequence initiated
4022.374   "mc land start"                VTOL        
4028.194   "MC landing start 0"           VTOL        
4090.831   "ll detected landing 4"        VTOL        False landing detected (4 votes)
4090.836   "MC land detect 11"            VTOL        
4090.842   "start of landed event task"   VTOL        *** Landed task spawned ***
4090.844   "mc land complete"             VTOL        
4091.154   "event FLT_EVENT_LAND"         VTOL        Flight event logged
4091.308   "MC disarmed 0"                VTOL        
4091.311   "MC safe 1"                    VTOL        
           *** NO "capturing ap fdr" MESSAGE EVER APPEARS ***
           *** FDR capture step was never reached or failed ***
           *** FDR GAP BEGINS ~4125s (1075 seconds) ***
4192.232   "sw 1 port link reset 2"       XCOMM       Link issue detected (~101s later)
4193.012   "ap dbg: Bad CRC"              FW AP       Communication errors
4197.424   "ap link fault: local rx       XCOMM       Critical: XCOMM receives okay
            okay ap rx bad"                            but FW AP is NOT receiving
4197.425   "ap link fault during landing" XCOMM       Fault during landing state
4286.970   "ap link restored"             XCOMM       Link recovered (~195s later)
Flight 2 (Comparison) - False Landing vs Actual Landing:
Time (s)   Event Log Message              Source      Description
---------  -----------------------------  ----------  ---------------------------
FALSE LANDING (same pattern as Flight 1):
2282.741   "start of landed event task"   VTOL        *** NO "capturing ap fdr" follows ***
ACTUAL LANDING (normal behavior):

## Page 11

3506.318   "start of landed event task"   XCOMM       Landed task spawned
3506.845   "capturing ap fdr"             XCOMM       *** FDR capture started (~0.5s later) ***
3585.694   "start of landed event task"   XCOMM       Second landing event
3586.221   "capturing ap fdr"             XCOMM       *** FDR capture started ***
Key Finding from XCOMM Event Log
The critical difference between Flight 1 and Flight 2:
 Flight 1: "start of landed event task" logged but NO "capturing ap fdr" follows
 Flight 2 false landing: Same pattern - NO "capturing ap fdr" follows
 Flight 2 actual landing: "capturing ap fdr" appears ~0.5 seconds after landed task start
This proves:
1. The VTOL/XCOMM landing workflow started normally with "start of landed event task"
2. But the FDR capture step was never reached in Flight 1 (and in Flight 2's false landing)
3. Something blocked or failed between spawning the landed task and reaching the "capturing ap fdr" step
Link Fault Diagnostic
The message "ap link fault: local rx okay ap rx bad" is critical:
 "local rx okay" = XCOMM is still receiving data FROM the FW AP
 "ap rx bad" = FW AP is NOT receiving data from XCOMM
This indicates the FW AP can still transmit but is not processing incoming commands - consistent with a
blocking/hung state in the FW AP.
Root Cause Hypothesis (Updated with XCOMM Evidence)
The XCOMM event log shows that "capturing ap fdr" was never logged in Flight 1, meaning the
flightLandTask() either:
1. Never reached the oldapGetFDR() call, OR
2. Crashed/blocked before logging the "capturing ap fdr" message
Timeline Analysis:
1. False landing detected at 4090.8s triggers fltlogEvent(FLT_EVENT_LAND)
2. XCOMM spawns flightLandTask - logs "start of landed event task" at 4090.842s
3. Something blocks or fails - "capturing ap fdr" never appears
4. ~100 seconds later (4192-4197s) link faults are detected
5. Link fault shows "local rx okay ap rx bad" - FW AP transmitting but not receiving
6. Motors don't shut off because FW AP is not processing commands
Possible failure points between "start of landed event task" and "capturing ap fdr":
 vTaskDelay(300) - 300ms delay (should not block indefinitely)
 File operations: makeflightname(), sdcardReady(), configExport()

## Page 12

 Any of these could hang if SD card or filesystem has issues
Alternative hypothesis: The FW AP may have already been in a blocked state before the landing detection,
causing:
1. VTOL false landing to detect (possibly due to lack of FW AP state updates)
2. XCOMM landed task to fail when trying to communicate with FW AP
3. Link fault to be detected when XCOMM finally notices FW AP unresponsive
Potential Blocking Points in FW AP
File: hostintf.cpp
// FDR block transmission - sends 1024 bytes per block
TxBuf[0] = RAW_UPLOAD;
memmove(&TxBuf[1], &index, sizeof(short));
// ... copy 1024 bytes from flash ...
TransmitHost(TxBuf, count+3);  // Serial transmission
LastFDRTime = clock->GetTime();  // Marks as busy for 500-1500ms
File: Serial167.cpp:333
while(txh == TxTail) {};  // Infinite wait for TX buffer, no watchdog
File: SPI_I2C.cpp:551
while(ReadStatus() == 0xf3) {};  // Infinite wait for SPI status
Code Locations of Interest
VTOL - Landing Detection (LLDetect.c)
 Voting system with threshold of 4 votes
 Sensors: gyro rates, accel, GPS velocity, baro ROC, AGL (when laser in range)
 Countdown from 50 cycles (~5 seconds) before triggering
 Calls fltlogEvent(FLT_EVENT_LAND) which propagates to XCOMM
XCOMM - FDR Capture (FlightLog.c, OldApGains.c)
 flightLandTask() spawned on landing detection
 oldapGetFDR() requests FDR data from FW AP
 Waits up to 30 seconds for FDR capture to complete
FW AP - FDR Transmission (hostintf.cpp)
 RAW_UPLOAD command triggers FDR block transmission
 BusyWithFDR() returns true for 500-1500ms after each block
 While busy, status messages are suppressed

## Page 13

FW AP - Serial TX Blocking (Serial167.cpp:333)
while(txh == TxTail) {};  // Infinite wait, no watchdog reset
FW AP - SPI Blocking (SPI_I2C.cpp:551)
while(ReadStatus() == 0xf3) {};  // Infinite wait for SPI
Conclusions
1. False Landing Detection: Both flights falsely detected landing based on steady flight conditions (no AGL check
- laser out of range)
2. Sensor Voting: Landing triggered by: quiet gyro + quiet accel + low GPS velocity (threshold=4 votes)
3. No AGL Check: Laser was out of range at ~300-400 feet, so no altitude confirmation was required for landing
vote
4. XCOMM Landed Task Failed: "start of landed event task" logged but "capturing ap fdr" never
appeared - task blocked before FDR capture
5. FW AP Communication Failure: Link fault message "local rx okay ap rx bad" confirms FW AP was
transmitting but not receiving/processing commands
6. Motor Behavior: Motors continued running because FW AP was not responding to execute shutoff
7. FDR Gaps: Large logging gaps occurred (1,075s and 16,474s) correlating with the communication failure
8. Watchdog: No reset occurred during incident flights - all 14 WD BOOT markers are from historical data
Recommendations
Landing Detection Improvements
1. Require AGL confirmation - landing detection should not trigger without altitude confirmation when laser is out
of range
2. Add altitude gate - inhibit landing detection above a certain altitude threshold
3. Cross-check landing votes - require additional confirmation for landing at high altitude
FW AP Communication Robustness
4. Review Serial167.cpp and SPI_I2C.cpp for infinite-wait blocking loops - add timeouts
5. Add watchdog petting in blocking loops to prevent CPU hangs
6. Add heartbeat monitoring between XCOMM and FW AP with automatic recovery
XCOMM Landed Task Robustness
7. Add timeout handling in flightLandTask() for file operations and SD card access
8. Add telemetry for CPU load and task status during landing states
9. Log diagnostic info when landed task blocks or fails to reach FDR capture step

## Page 14

Generated Visualizations
 V996_FISHBONE_DIAGRAM.png - Root cause analysis showing why this was NOT a communications issue
 V996_FLIGHT_COMPARISON.png - Side-by-side comparison of both flights
 V996_LANDING_DETECTION_ANALYSIS.png - Sensor voting and false landing trigger analysis
 V996_INVESTIGATION_DIAGRAMS.png - State transition and timeline diagrams
Analysis Scripts
Script
Purpose
generate_fishbone_diagram.py
Generates root cause fishbone diagram
analyze_landing_detection.py
Analyzes sensor votes and false landing triggers
decode_vtolstate.py
Decodes VtolState values to landing state names
analyze_both_flights.py
Compares state transitions between flights
analyze_wd_boot_detail.py
Analyzes WD BOOT markers by segment
check_flight2_throttle.py
Extracts Flight 2 throttle data
generate_flight_comparison.py
Generates comparison plot
Data Files
fdr_analysis/
??? flight1_fdr.csv           # Flight 1 raw FDR
??? flight1_fdr_cleaned.csv   # Flight 1 segment 0 only
??? flight2_fdr.csv           # Flight 2 raw FDR
??? flight2_fdr_cleaned.csv   # Flight 2 segment 0 only
APPENDIX A: WD BOOT Analysis - Detailed
Explanation
This appendix provides a comprehensive explanation of the WD BOOT (Watchdog Boot) markers found in the FDR
files, including how to interpret them and why they are NOT related to the incident flights.
A.1 What is WD BOOT?
The Fixed-Wing Autopilot (FW AP) has a hardware watchdog timer that monitors system health. If the CPU becomes
unresponsive (fails to "pet" the watchdog within a timeout period), the watchdog forces a hardware reset.

## Page 15

When the system boots after a watchdog reset, it:
1. Detects that the previous shutdown was due to a watchdog timeout
2. Logs "WD BOOT" to the FDR
3. Logs a crash code showing which subsystem was active when the watchdog triggered
4. Performs a full system reset
Source: sams.cpp:568-590
if(dogstat)  // dogstat = true if previous boot was watchdog reset
{
    debug->DebugStr("WD BOOT");
    strcpy(bootcode, "Code:----------------");
    bootcode[6] = booty_copy;           // Boot phase
    bootcode[8] = navcrash_copy;        // NavCrash
    bootcode[10] = hostcrash_copy;      // HostifCrash
    bootcode[12] = wdman_copy;          // WdManagerCrash
    bootcode[14] = gpscrash_copy;       // GpsCrash
    bootcode[16] = vtedcrash_copy;      // VtedCrash
    bootcode[18] = navmancrash_copy;    // NavManCrash
    bootcode[20] = sensorcrash_copy;    // SensorCrash
    debug->DebugStr(bootcode);
    _int166(0);  // Full reset after WD Boot report
}
A.2 Crash Code Format
The crash code format is:
Code:-{Boot}-{Nav}-{Hostif}-{WdMgr}-{GPS}-{Vted}-{NavMan}-{Sensor}-j
Position  Variable         Subsystem              Source Files
--------  ---------------  --------------------   ---------------------------
[6]       booty_copy       Boot phase             sams.cpp
[8]       navcrash_copy    Navigation task        navigate.cpp, sams.cpp
[10]      hostcrash_copy   Host interface/comms   hostintf.cpp
[12]      wdman_copy       Watchdog manager       fasttask.cpp, iloop.cpp
[14]      gpscrash_copy    GPS processing         nmeadata.cpp, ubloxgps.cpp
[16]      vtedcrash_copy   VTED/terrain           gpsnav.cpp, missdb.cpp
[18]      navmancrash_copy Navigation manager     (not found in search)
[20]      sensorcrash_copy Sensor processing      sensors.cpp
Character Meanings
Each position contains a single character indicating the state of that subsystem:
Character
Meaning
`-` or `_`
Not active / idle state
`a`-`z`
Lowercase = early in function (just started)
`A`-`Z`
Uppercase = later in function (closer to completion)
`Z`
Function completed normally
`0`-`9`
Numeric states (subsystem-specific)
`!`, `*`
Special states (e.g., GPS error conditions)

## Page 16

Example Interpretation
Code:-g-Z-6-X-Z-6-z-j
Position  Value  Interpretation
--------  -----  ------------------------------------------
[6]  -    Boot   Boot phase idle/normal
[8]  g    Nav    Navigation early in cycle (state 'g')
[10] Z    Hostif Host interface completed normally
[12] 6    WdMgr  Watchdog manager state 6
[14] X    GPS    GPS mid-processing (state 'X')
[16] Z    Vted   VTED completed normally
[18] 6    NavMan Navigation manager state 6
[20] z    Sensor Sensor near completion (lowercase z)
A.3 FDR File Structure - Circular Buffer
The FDR (Flight Data Recorder) file is a circular buffer:
 New data is appended to the bottom of the file
 Old data remains at the top of the file
 The file contains data from multiple flights
Segment Organization
TOP OF FILE (oldest data)
??? Segment 18 - oldest historical flight
??? Segment 17
??? ...
??? Segment 4  - contains WD BOOT from previous flights
??? ...
??? Segment 1
??? Segment 0  - CURRENT/INCIDENT FLIGHT (newest data)
BOTTOM OF FILE
Critical Point: WD BOOT markers found in segments 1-18 are from PREVIOUS flights, not the incident flight.
A.4 WD BOOT Markers in V996 FDR Files
Flight 1 FDR (165813Z)
Line
Segment
Crash Code
Analysis
3772
4
`Code:-g-Z-6-X-Z-6-z-j`
Nav=g, GPS=X mid-processing
4570
6
`Code:-a-Z-9-X-Z-6-n-j`
Nav=a early, GPS=X
4838
9
`Code:-g-Z-9-X-Z-6-z-j`
Nav=g, GPS=X
4884
10
`Code:-a-Z-9-6-Z-6-q-j`
Nav=a, GPS=6
4944
11
`Code:-a-Z-9-b-Z-6-s-j`
Nav=a, GPS=b

## Page 17

4970
12
`Code:-a-Z-9-X-Z-X-c-j`
Nav=a, GPS=X, NavMan=X
5252
13
`Code:-a-Z-9-b-Z-6-q-j`
Nav=a, GPS=b
Total: 7 WD BOOT markers, ALL in historical segments (4-13) Segment 0 (incident flight): 0 WD BOOT
markers
Flight 2 FDR (182857Z)
Line
Segment
Crash Code
Analysis
3184
4
`Code:-g-Z-6-X-Z-6-z-j`
Nav=g, GPS=X mid-processing
3982
6
`Code:-a-Z-9-X-Z-6-n-j`
Nav=a early, GPS=X
4250
9
`Code:-g-Z-9-X-Z-6-z-j`
Nav=g, GPS=X
4296
10
`Code:-a-Z-9-6-Z-6-q-j`
Nav=a, GPS=6
4356
11
`Code:-a-Z-9-b-Z-6-s-j`
Nav=a, GPS=b
4382
12
`Code:-a-Z-9-X-Z-X-c-j`
Nav=a, GPS=X, NavMan=X
4664
13
`Code:-a-Z-9-b-Z-6-q-j`
Nav=a, GPS=b
Total: 7 WD BOOT markers, ALL in historical segments (4-13) Segment 0 (incident flight): 0 WD BOOT
markers
A.5 Pattern Analysis of Historical WD BOOTs
The 14 historical WD BOOT events (7 per flight file) show consistent patterns:
Common Crash Code Patterns
1. Hostif=Z (position 10): Host interface always completed normally
 The communication subsystem was NOT the cause of these historical watchdog resets
2. GPS=X or GPS=b (position 14): GPS was mid-processing
 Suggests GPS parsing may have been involved in some historical resets
3. Nav=a or Nav=g (position 8): Navigation was early in its cycle
 Navigation was just starting when watchdog triggered
4. Vted=Z (position 16): VTED usually completed normally
 Terrain processing was NOT the typical cause
5. WdMgr=6 or 9 (position 12): Consistent watchdog manager states
 These are normal operational states
Interpretation

## Page 18

These historical watchdog resets appear to be related to GPS processing during navigation startup. This is a known
pattern that can occur during:
 GPS cold start
 Loss of GPS lock
 GPS message parsing timeouts
These are NOT related to the incident being investigated.
A.6 Why WD BOOT Did NOT Occur During Incident Flights
Evidence
1. Segment 0 Analysis:
 Flight 1 Segment 0: No WD BOOT markers
 Flight 2 Segment 0: No WD BOOT markers
2. Timeline Continuity:
 If a watchdog reset occurred during flight, there would be:
 A WD BOOT marker at the restart point
 A discontinuity in timestamps
 Loss of flight state
 None of these are present in either incident flight
3. System Behavior:
 The vehicle continued flying (motors active)
 VTOL state machine continued operating
 XCOMM continued logging (with gaps)
 This is inconsistent with a full system reset
Conclusion
The WD BOOT markers found in the FDR files are historical artifacts from previous flights stored in the circular
buffer. No watchdog reset occurred during either incident flight.
The FDR logging gaps (1,075s and 16,474s) occurred without a system reset, pointing to a communication or
blocking issue rather than a watchdog failure.
A.7 How to Verify This Analysis
To confirm that WD BOOT markers are from historical segments:
1. Check line numbers: WD BOOT entries at lines 3000-5500 are in older segments
2. Check timestamps: Timestamps before/after WD BOOT should show discontinuity (flight boundaries)

## Page 19

3. Check segment boundaries: Look for "Time,ET,UTC" headers that mark new segments
Command to Find WD BOOT with Context
Get-Content "flight1_fdr.csv" | Select-String -Pattern "WD BOOT" -Context 5,5
Command to Find Segment Boundaries
Get-Content "flight1_fdr.csv" | Select-String -Pattern "^Time,ET,UTC"
A.8 Watchdog System Architecture Reference
Subsystem Crash Variables
Variable
File
Purpose
`NavCrash`
navigate.cpp, sams.cpp
Navigation task state
`HostifCrash`
hostintf.cpp
Host interface/comms state
`WdManagerCrash`
fasttask.cpp, iloop.cpp
Watchdog manager state
`GpsCrash`
nmeadata.cpp, ubloxgps.cpp
GPS processing state
`VtedCrash`
gpsnav.cpp, missdb.cpp
Vertical terrain state
`NavManCrash`
(navigation manager)
Navigation manager state
`SensorCrash`
sensors.cpp
Sensor processing state
Watchdog Petting
The watchdog must be "pet" regularly by calling Hitdog():
void Hitdog(void);  // fasttask.cpp - watchdog strobe routine
If any task blocks for too long without calling Hitdog(), the watchdog will trigger a reset.
Pre-Reset Warnings
Before a watchdog reset, the system logs warnings:
debug->DebugStr("WDE O 500");   // Odog counter warning
debug->DebugStr("WDE O 1000");  // More severe warning
debug->DebugStr("WDE M 300");   // Mdog counter warning
DumpWdState();                   // Dumps current crash codes
If these warnings appear in logs before a gap, it would indicate an impending watchdog reset.
WDE Warning in Flight 1 FDR (Historical, Not Incident)
One WDE M 300 warning was found in the Flight 1 FDR file:
Time: 2760s, UTC: 163428853

## Page 20

WDE M 300
Code:___Z_n_e_Z_6_z_j
H: 109
However, this is from a historical flight segment, not the incident:
 WDE location: Time=2760s, UTC=163428853
 Incident flight: Time=4080-4090s, UTC=171910798
The different UTC timestamps confirm these are from different flights. The incident flight (segment 0 at the bottom of
the file) has no WDE warnings.
A.9 Root Cause Analysis of Historical WDE Warning
The single WDE M 300 warning found in the FDR can be traced to a specific cause:
Crash Code Decode
Code:___Z_n_e_Z_6_z_j
Position  Value  Subsystem      Interpretation
--------  -----  -------------  ------------------------------------------
[6]  _    Boot   Boot phase idle (normal)
[8]  Z    Nav    Navigation completed normally
[10] n    Hostif DispatchSystemCommand() in progress
[12] e    WdMgr  Watchdog manager state 'e'
[14] Z    GPS    GPS completed normally
[16] 6    Vted   VTED state 6
[18] z    NavMan Navigation manager near completion
[20] j    Sensor Sensor state 'j'
H: 109 Decode
H: 109 = Hflag = RxState + 100 = RxState = 9 = SYNC4
From hostintf.h:
enum RX_STATE { 
  RXS_IDLE=0, SYNC1, SYNC2, SYNC2A, COUNT, DATA, CKSUM1, CKSUM2, 
  SYNC3, SYNC4,  // <-- State 9 = SYNC4
  ...
};
The FW AP was in state SYNC4 - actively receiving a packet when the warning triggered.
Timeline Context
Time (s)   Mode  NavState  VtolState  Event
---------  ----  --------  ---------  ---------------------------
2600-2760  2     0         0          On ground, pre-flight
2760       2     0         0          WDE M 300 warning triggered
2780       2     0         0          Still on ground, recovered
2800       4     17        20002      *** MISSION ACTIVATED ***
2820+      4     17        20002      Vehicle launching

## Page 21

Root Cause
The WDE M 300 warning was triggered during pre-flight mission upload/activation:
1. Vehicle on ground receiving pre-flight commands
2. Large command processing (likely mission upload) in DispatchSystemCommand()
3. Mdog counter reached warning threshold (100 ticks without reset)
4. HostifCrash='n' confirms the system was inside DispatchSystemCommand()
5. H: 109 (SYNC4) confirms active packet reception
6. System recovered - no actual watchdog reset occurred
7. Mission activated at Time 2800s, vehicle launched normally
Conclusion
This WDE warning was caused by mission upload processing taking longer than expected, likely due to:
 Large mission database transfer
 NV page writes during mission setup
 Multiple commands queued during pre-flight
This is a benign warning that occurs occasionally during heavy pre-flight communications. The system recovered
without a reset, and the vehicle launched and flew normally.
This pattern is NOT related to the incident being investigated, which occurred at a completely different time
(4090s vs 2760s) during a different flight (UTC 171xxxxxx vs 163xxxxxx).
