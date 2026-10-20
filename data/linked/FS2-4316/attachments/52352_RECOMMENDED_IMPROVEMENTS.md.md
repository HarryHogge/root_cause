# RECOMMENDED_IMPROVEMENTS.md

Attachment 52352, text, 4 KB, added 2026-04-02 by Scott Hunter.

# Recommended Improvements
## Crash Dump Telemetry Enhancements for Faster Field Triage

**Date:** 2026-04-02  
**Scope:** Exception/crash telemetry captured from `_general_exception_handler` and related crash-page persistence path.  
**Goal:** Increase root-cause confidence for `system 202/203/206/207` events without requiring debugger-only confirmation.

---

## Background

Current analysis guidance and investigation notes identify a recurring telemetry gap:

- We persist `CRASH_FUNC` and `CRASH_ADDR (EPC)`.
- We already capture `SP/RA` in `diag[5]/diag[6]`.
- In the same persisted path, we do not consistently persist all of:
  - raw exception code (`_excep_code`)
  - `BADVADDR`
  - `NESTEDEPC`

Impact:

- Lower confidence in distinguishing translation faults vs bus faults in field data.
- Slower triage for recurring `system 207` reports.
- Extra dependence on debugger access for confirmation.

---

## Recommended Minimum Persisted Fields

For `_general_exception_handler` crash records, persist at least:

- `diag0`: `_excep_code`
- `diag1`: `BADVADDR`
- `diag2`: `NESTEDEPC`
- `diag5`: `SP` (already captured)
- `diag6`: `RA` (already captured)

Keep existing:

- `CRASH_FUNC`
- `CRASH_ADDR` (EPC)

---

## Why These Fields Matter

### 1) `_excep_code` in `diag0`

- Disambiguates exception class directly in persisted logs.
- Prevents ambiguity when only `CRASH_FUNC` is available from field snapshots.

### 2) `BADVADDR` in `diag1`

- Required to classify faulting virtual address behavior.
- Enables robust instruction-fetch vs data-access triage when compared with EPC.
- Critical for validating expected fault address hotspots (for example, known UART `TxDone` paths).

### 3) `NESTEDEPC` in `diag2`

- Preserves additional control-flow context when nested exception state is relevant.
- Improves confidence in corruption-vs-routing interpretations.

### 4) `SP/RA` in `diag5/diag6`

- Already high-value and should remain unchanged.
- Supports stack integrity and call-site reconstruction workflows.

---

## Interpretation Rules Enabled by This Telemetry

With `EPC + BADVADDR + _excep_code + SP/RA` persisted:

- Differentiate instruction fetch vs data access in TLB-class faults (`BADVADDR ≈ EPC` vs `BADVADDR ≠ EPC`).
- Improve classification confidence for `system 202` and `system 203` without debugger attachment.
- Improve `system 206/207` triage by retaining both path/type and address context in field logs.

---

## Recommended Implementation Approach

1. In `_general_exception_handler`, ensure values are read before final crash persistence:
   - `_excep_code`
   - `_bad_virtual_addr`
   - `_excep_addr_nested`

2. Persist to diag slots consistently:
   - `CRASH_DIAG0(_excep_code)`
   - `CRASH_DIAG1(_bad_virtual_addr)`
   - `CRASH_DIAG2(_excep_addr_nested)`

3. Keep existing:
   - `CRASH_ADDR(_excep_addr)`
   - `CRASH_CAPTURE_SP_RA()`

4. Confirm no regression to existing TLB handler path conventions.

---

## Validation Plan

After implementation, validate with known scenarios:

- TLB refill instruction fetch (`system 6`) and data access variants.
- `system 202` and `system 203` paths through `_general_exception_handler`.
- At least one `system 207` reproduction or archived replay comparison.

For each run, verify persisted crash page contains:

- `CRASH_FUNC`
- `CRASH_ADDR`
- `diag0/diag1/diag2/diag5/diag6` populated and plausible

---

## Compatibility Notes

- This recommendation is additive telemetry; it should not alter exception routing behavior.
- Existing offline tools that ignore `diag2` should continue to work.
- Analysis scripts should be updated to consume `diag0/diag1/diag2` when present.

---

## Related Documents

- [CRASH_207_INVESTIGATION_SUMMARY.md](CRASH_207_INVESTIGATION_SUMMARY.md)
- [CRASH_DUMP_ANALYSIS_PATTERNS.md](CRASH_DUMP_ANALYSIS_PATTERNS.md)
- [EXCEPTION_TEST_PLAN.md](EXCEPTION_TEST_PLAN.md)
- [EXCEPTION_TESTING.md](EXCEPTION_TESTING.md)
