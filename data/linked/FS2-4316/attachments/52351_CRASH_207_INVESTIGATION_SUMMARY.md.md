# CRASH_207_INVESTIGATION_SUMMARY.md

Attachment 52351, text, 10 KB, added 2026-04-02 by Scott Hunter.

# Crash 207 Investigation Summary

## Context

This summary captures the investigation into repeated `CRASH_FUNC = 207` crashes, focusing on the dominant crash site in `Serial.cpp` and the interpretation of what `207` means in this codebase.

Date: 2026-03-20

---

## What `207` Means in This Project

In this codebase:

- `CRASH_FUNC = 200 + _excep_code`
- `207` therefore means `_excep_code = 7`
- Exception code 7 is `EXCEP_DBE` = **Data Bus Error**

Practical meaning:

- A **data load/store bus transaction failed**
- This is typically **not** a simple misalignment fault
- Misalignment normally shows up as:
  - `204` = `AdEL` (Address Error Load)
  - `205` = `AdES` (Address Error Store)

Relevant code:
- [utils.c](utils.c#L1272-L1276)
- [utils.c](utils.c#L1380-L1387)

---

## Crash CSV Findings

File analyzed:
- [crash_data_unique.csv](crash_data_unique.csv)

Key observations:

- Total crash rows: **54**
- `trace(0) = func(0) system 207`: **53** rows
- `trace(0) = func(0) system 6`: **1** row

This means the dataset is overwhelmingly dominated by `207` crashes.

---

## Crash Address Hotspots from CSV

After normalizing the `crash addr` field for `trace(0) = func(0) system 207`, the dominant addresses were:

- `0x9d073b44` → 19 occurrences
- `0x9d073b40` → 18 occurrences
- `0x9d0737cc` → 6 occurrences
- `0x9d0b3a78` → 4 occurrences
- `0x9d0b3918` → 3 occurrences
- `0x9d0b3a80` → 2 occurrences
- `0x9d0c8fc0` / other isolated addresses → rare

---

## Correct-Build Address Resolution

Important finding: address resolution only made sense once the source and ELF were aligned to the correct build/git hash.

Using the correct build, the resolved addresses were:

- `0x9d073b40` → `_IntHandlerUartTransmit3` at [Serial.cpp](Serial.cpp#L1176)
- `0x9d073b44` → `_IntHandlerUartTransmit3` at [Serial.cpp](Serial.cpp#L1176)
- `0x9d0b3918` → `isrIncrement` at [ISR_count.cpp](ISR_count.cpp#L162)
- `0x9d0b3a78` → `DumpISRTable` at [ISR_count.cpp](ISR_count.cpp#L210)
- `0x9d0b3a80` → `DumpISRTable` at [ISR_count.cpp](ISR_count.cpp#L210)
- `0x9d0c8fc0` → `configFormatHtmlLine` at [ConfigManager.c](ConfigManager.c#L3605)

Interpretation:

- The dominant hotspot is clearly the UART3 TX ISR in [Serial.cpp](Serial.cpp#L1176)
- The `ISR_count` and `ConfigManager` hits appear to be secondary/rarer contexts, not the primary repeated signature

---

## Dominant Crash Site

Resolved dominant crash line:

- [Serial.cpp](Serial.cpp#L1176)

Source line of interest:

- `if(serial_control[SP_PORT].TxDone != 1)`

This is inside `_IntHandlerUartTransmit3()` with:

- `SP_PORT = 2`
- therefore accessing `serial_control[2].TxDone`

---

## Cross-Build Confirmation

The same investigation was repeated against a different repository/build at a different git hash using:

- external repo: `C:\Users\shunter\GIT\InWork\xcomm_AC864`
- ELF: `C:\Users\shunter\GIT\InWork\xcomm_AC864\XComm2.X\dist\PIC32MZ2048EF_SK_HARD_FLOAT\production\XComm2.X.production.elf`

Resolved result:

- `0x9d0737cc` → `_IntHandlerUartTransmit3` at `Serial.cpp:1207`

Source at that location in the updated build:

- `if(serial_control[SP_PORT].TxDone != 1)`

Interpretation:

- the absolute crash PC changed between builds
- the resolved source line did **not**
- this confirms the repeated `207` crash signature is tied to the same UART3 TX ISR read path across multiple builds

---

## Disassembly-Based Effective Address

Using the correct ELF and disassembly of `_IntHandlerUartTransmit3`:

- `0x9d073b40`: forms base pointer to `serial_control`
- `0x9d073b44`: `lbu v1,121(v0)`

Resolved symbol base:

- `serial_control` = `0x8001ac18`

Effective read address:

- `0x8001ac18 + 0x79 = 0x8001ac91`

Therefore, assuming line 1176 is the crash of interest, the faulting data read is most likely:

- **effective address = `0x8001ac91`**

This corresponds to the byte read for:

- `serial_control[2].TxDone`

---

## Interpretation of the Fault

Because the fault is occurring on a read from a fixed global SRAM address (`0x8001ac91`), the likely categories are:

1. **Hardware / bus / SRAM path problem**
   - SRAM access path issue
   - local power integrity issue
   - local signal integrity / board problem
   - MCU or board-specific defect

2. **System corruption leading to a failed bus access**
   - corrupted ISR context before entry
   - register corruption causing an invalid bus transaction sequence
   - wider memory/bus state corruption

3. **Much less likely: simple software alignment issue**
   - alignment faults should normally show up as `204`/`205`, not `207`

So the best description is:

- `207` here indicates a **bus-level data access failure**
- It does **not** directly imply a bad pointer in source code
- The source line is where the CPU noticed the failed read

### Why a Hardware Problem Can Repeat at the Same Instruction

This can still be a hardware or unit-specific problem even when the crash repeatedly points at the same source line.

Reasons:

- the UART3 TX ISR is a **very high-frequency code path**, so it repeatedly touches the same SRAM/global state
- a marginal bus/SRAM/power-integrity condition may only fail **rarely**, but over millions of accesses that rare event becomes observable
- the same instruction can act as the system's **canary touch point**: not necessarily the root cause, but the first frequent access to trip the weak resource
- seeing the same logical source line across multiple builds strengthens the idea that this is tied to the same hardware access pattern rather than one binary layout

---

## Fleet-Level Observation

A critical fact from the investigation:

- This behavior appears to be **specific to a single computer/unit**
- Many other systems are in the field with the **same software build** and do **not** show this failure pattern

This strongly shifts the working hypothesis toward:

- **unit-specific hardware issue**, or
- **unit-specific corruption state**, rather than a broad software defect in the released build

---

## Working Conclusion

Current best conclusion:

- The repeated `207` crashes are primarily associated with the UART3 TX ISR at [Serial.cpp](Serial.cpp#L1176)
- The failing data read is most likely at effective address **`0x8001ac91`** (`serial_control[2].TxDone`)
- The exception type indicates a **data bus error**, not a simple misalignment
- A second build at a different git hash also resolves the crash to the same `TxDone` check in `_IntHandlerUartTransmit3`, strengthening the case that this is the same logical hotspot across builds
- Because this is a fixed SRAM/global location and the issue is reportedly isolated to one unit, **hardware or unit-specific integrity problems are currently the leading hypothesis**

---

## Related Pattern: System 203

Brief differential only:

- `system 203` = `CRASH_FUNC 200+3` (`TLBS`, store-side TLB translation fault)
- `system 207` = `CRASH_FUNC 200+7` (`DBE`, data bus error)

Example:

- if a bad pointer **write** hits unmapped virtual space, expect `203`
- if a recurring **read** at UART3 `TxDone` fails at bus/data path, expect `207`

Full 203 guidance is maintained in [CRASH_DUMP_ANALYSIS_PATTERNS.md](CRASH_DUMP_ANALYSIS_PATTERNS.md) under "What `system 203` Means".

---

## Additional Logging Needed for Faster 207 Triage

Current gap in persisted crash data for `_general_exception_handler`:

- We persist `CRASH_FUNC` and `CRASH_ADDR(EPC)`
- We do **not** persist `BADVADDR` in the same crash page path
- We do **not** persist `NESTEDEPC` in the same crash page path
- We do **not** persist the raw exception code in diag slots in that handler path

Why this matters:

- Without persisted `BADVADDR`, we cannot conclusively tell from field logs whether DBE happened on the expected UART3 read address or on a different effective address
- This forces debugger-only confirmation and slows field triage

For this specific hotspot, the key one-line validation is:

- compare persisted `BADVADDR` against expected `serial_control[2].TxDone` address aliases
   - cached KSEG0: `0x8001A451`
   - uncached KSEG1 alias: `0xA001A451`
   - physical: `0x0001A451`

Interpretation rule:

- match: fault happened on the intended `TxDone` read path
- no match: address generation/context corruption remains in play

Recommended minimum persisted fields for future 207 captures:

- `diag0`: exception code (`_excep_code`)
- `diag1`: `BADVADDR`
- `diag2`: `NESTEDEPC`
- `diag5`: SP and `diag6`: RA (already captured)

Note: this section documents required telemetry; no code change is included in this report update.

---

## Recommended Next Steps

High-value next checks:

1. **A/B hardware swap test**
   - move this computer/unit vs a known-good one
   - determine whether failure follows hardware

2. **Stress around UART3 activity**
   - reproduce under high TX traffic
   - test with temperature / supply / vibration variation if possible

3. **Power and integrity checks**
   - inspect rails and board health during UART3 activity
   - look for unit-specific issues

4. **Memory/bus stress on the affected unit**
   - SRAM/bus stress testing if available

5. **Continue watching for address diversity**
   - if more crashes appear in unrelated fixed SRAM accesses, that further supports broader hardware/bus instability

---

## Related Investigation Files

- [CRASH_DUMP_ANALYSIS_PATTERNS.md](CRASH_DUMP_ANALYSIS_PATTERNS.md)
- [EXCEPTION_TEST_PLAN.md](EXCEPTION_TEST_PLAN.md)
- [crash_data_unique.csv](crash_data_unique.csv)
- [Serial.cpp](Serial.cpp#L1176)
