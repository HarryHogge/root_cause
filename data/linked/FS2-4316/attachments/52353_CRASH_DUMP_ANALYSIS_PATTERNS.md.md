# CRASH_DUMP_ANALYSIS_PATTERNS.md

Attachment 52353, text, 37 KB, added 2026-04-02 by Scott Hunter.

# Crash Dump Analysis Patterns
## Automated Analysis Reference for PIC32MZ Exception Dumps

**Purpose:** Document empirically validated patterns for automated crash dump analysis script.

**Date Created:** February 18, 2026  
**Last Updated:** March 24, 2026

---

## Overview

This document captures key patterns discovered through empirical testing that enable automated distinction between different crash scenarios. Validation status is tracked per test case below (validated vs implemented/pending).

For the current `CRASH_FUNC=207` case study and documented telemetry gaps in `_general_exception_handler`, see:
- [CRASH_207_INVESTIGATION_SUMMARY.md](CRASH_207_INVESTIGATION_SUMMARY.md) (section: **Additional Logging Needed for Faster 207 Triage**)

---

## Crash Dump Structure

**Standard Fields:**
- `CRASH_FUNC`: Exception handler identifier
- `CRASH_ADDR`: EPC (Exception Program Counter) - instruction that caused/was executing during exception
- `CRASH_DIAG[0]`: Exception code from CPU Cause register (for TLB handler)
- `CRASH_DIAG[1]`: BadVAddr - virtual address that caused exception (for TLB handler)
- `CRASH_DIAG[5]`: Stack Pointer (SP) at exception time
- `CRASH_DIAG[6]`: Return Address (RA) at exception time

---

## Exception Handler Identification

### Primary Pattern: CRASH_FUNC Value

```
CRASH_FUNC = 6   → _simple_tlb_refill_exception_handler (TLB refill)
CRASH_FUNC = 7   → _cache_err_exception_handler (cache error)
CRASH_FUNC = 200+N → _general_exception_handler (N = exception code)
```

**Examples:**
- `CRASH_FUNC = 6`: TLB Refill (most common for null/unmapped pointers)
- `CRASH_FUNC = 7`: Cache error (hardware issue)
- `CRASH_FUNC = 202`: TLBL via `_general_exception_handler` (TLB Load exception path)
- `CRASH_FUNC = 203`: TLB Store exception seen via `_general_exception_handler` (store-side TLB fault path)
- `CRASH_FUNC = 204`: AdEL - Address Error (Load) exception
- `CRASH_FUNC = 205`: AdES - Address Error (Store) exception
- `CRASH_FUNC = 206`: IBE - Instruction Bus Error (instruction fetch bus transaction failure; typically rare)
- `CRASH_FUNC = 207`: DBE - Data Bus Error (data load/store bus transaction failure; usually not simple misalignment)
- `CRASH_FUNC = 208`: Syscall exception
- `CRASH_FUNC = 209`: Breakpoint exception
- `CRASH_FUNC = 210`: Reserved Instruction exception
- `CRASH_FUNC = 212`: Arithmetic Overflow exception (if trap enabled)
- `CRASH_FUNC = 213`: Trap exception (divide/trap path; platform behavior may vary)

---

## CPU Exception Precedence (EMPIRICALLY VALIDATED)

**Critical Finding:** CPU checks faults in this exact order:

1. **TLB mapping** (HIGHEST PRIORITY - checked FIRST)
2. **Alignment** (checked second, if mapped)
3. **Physical memory validity** (checked third, if mapped and aligned)

**Implication:** An address that is BOTH unmapped AND misaligned will trigger **TLB Refill**, NOT **AdEL**.

**Example:**
- Address `0xFFFFFFFF` (unmapped AND misaligned):
  - Result: **TLB Refill** (`CRASH_FUNC = 6`)
  - NOT AdEL (`CRASH_FUNC = 204`)
  - CPU never reaches alignment check because TLB lookup fails first

### What `system 202` Means

`system 202` maps to:

- `CRASH_FUNC = 200 + 2`
- exception code `2` = `TLBL` (TLB Load exception)

Practical meaning:

- a **load-side** translation fault occurred (instruction fetch or data read)
- this is the same TLB-load class as many `CRASH_FUNC = 6` events, but reported through `_general_exception_handler`
- this is primarily a virtual-address translation/protection problem, not a bus-completion fault like `207`

How we typically get there:

- instruction fetch from unmapped virtual address
- data read via null/corrupted pointer into unmapped region
- load from mapping that is invalid for current TLB state

Why this can appear as `202` instead of `6`:

- `6` is the dedicated simple refill handler path used for many unmapped TLB cases
- `202` means `_general_exception_handler` captured `_excep_code=2` (TLBL)
- both indicate load-side TLB class, but from different handler routing

Triage note:

- if available, compare `BADVADDR` vs `EPC` to separate instruction-fetch TLBL from data-read TLBL
- if only `CRASH_FUNC=202` and one address are persisted, confidence is limited; persist `BADVADDR`, `_excep_code`, and `NESTEDEPC` for better automation

### What `system 203` Means

`system 203` maps to:

- `CRASH_FUNC = 200 + 3`
- exception code `3` = `TLBS` (TLB Store exception)

Practical meaning:

- a **store/write** touched a virtual address that failed TLB translation/protection checks
- this is a **store-side translation fault**, not primarily an alignment classification (`AdES=205`) and not a bus completion failure (`DBE=207`)

How we typically get there:

- write through a bad/corrupted pointer
- write to unmapped virtual address
- write to a mapping that exists but is invalid for store path under current TLB state

Why this can appear as `203` instead of `6`:

- `6` is the dedicated simple refill handler path used for many unmapped cases (often with `diag[0]=3` for TLBS)
- `203` means the fault was handled by `_general_exception_handler` with `_excep_code=3`
- so `203` is still TLB-store class, but through the general-exception route

Triage note:

- if only `CRASH_FUNC=203` and `CRASH_ADDR` are persisted, root-cause confidence is limited
- highest-value missing field is `BADVADDR` (faulting virtual address)
- next best is persisting raw `_excep_code` and `NESTEDEPC` in diag slots for this handler path

### What `system 204` Means

`system 204` maps to:

- `CRASH_FUNC = 200 + 4`
- exception code `4` = `AdEL` (Address Error (Load))

Practical meaning:

- invalid/unaligned **load** address class fault
- in this project, flash-region unaligned reads are a common source

### What `system 205` Means

`system 205` maps to:

- `CRASH_FUNC = 200 + 5`
- exception code `5` = `AdES` (Address Error (Store))

Practical meaning:

- invalid/unaligned **store** address class fault
- treat similarly to `204`, but on write path

### What `system 206` Means

`system 206` maps to:

- `CRASH_FUNC = 200 + 6`
- exception code `6` = `IBE` (Instruction Bus Error)

Practical meaning:

- an **instruction fetch** bus transaction failed
- this is different from translation faults (`6`/TLB refill path) and different from data-path bus faults (`207`/DBE)
- this class is expected to be **rare** in normal operation

How we typically get there:

- execute/jump into a region that is aligned and reachable but not a valid instruction source
- attempt instruction fetch beyond valid physical program space (for example, outside real flash backing)
- instruction-side bus/target availability issue during fetch

How to distinguish from nearby codes:

- `system 6` (TLB refill): translation/mapping failed first (higher-priority check)
- `system 204/205` (AdEL/AdES): alignment/address-error class
- `system 207` (DBE): bus failure on **data** load/store path, not instruction fetch

Triage note:

- resolve the reported crash address against the **matching ELF/map for that unit/build**
- if symbolized location is valid code but `206` repeats on one unit, prioritize hardware/path integrity checks (flash/bus/power) alongside software context
- persist/inspect `BADVADDR`, `_excep_code`, and `NESTEDEPC` to improve confidence when separating bus-path vs control-flow corruption scenarios

### What `system 207` Means

`system 207` maps to:

- `CRASH_FUNC = 200 + 7`
- exception code `7` = `DBE` (Data Bus Error)

Practical meaning:

- data load/store bus transaction failure
- usually not a simple alignment classification (`204/205`)

### What `system 208` Means

`system 208` maps to:

- `CRASH_FUNC = 200 + 8`
- exception code `8` = `Syscall`

Practical meaning:

- syscall instruction path executed
- expected in test/intentional syscall paths; suspicious in normal production flow

### What `system 209` Means

`system 209` maps to:

- `CRASH_FUNC = 200 + 9`
- exception code `9` = `Breakpoint`

Practical meaning:

- breakpoint instruction path executed
- often intentional in debug/test; in production can indicate unexpected control flow

### What `system 210` Means

`system 210` maps to:

- `CRASH_FUNC = 200 + 10`
- exception code `10` = `Reserved Instruction`

Practical meaning:

- invalid/unsupported instruction executed
- common suspects: code corruption, executing data as code, or wrong binary/CPU expectation

### What `system 212` Means

`system 212` maps to:

- `CRASH_FUNC = 200 + 12`
- exception code `12` = `Arithmetic Overflow`

Practical meaning:

- integer-overflow trap path fired (when enabled)
- platform/config dependent; may not reproduce on all MIPS setups

### What `system 213` Means

`system 213` maps to:

- `CRASH_FUNC = 200 + 13`
- exception code `13` = `Trap`

Practical meaning:

- CPU entered the trap-exception path (explicit `trap` instruction or trap-qualified arithmetic path)
- this is generally a **software/intentional exception class**, not a bus/translation/alignment fault class
- divide-by-zero-trigger assumptions can be platform/config dependent on MIPS; explicit trap instructions are more deterministic

How we typically get there:

- explicit trap/test instruction path
- arithmetic trap configuration enabled and triggered
- less commonly, corrupted execution reaching trap-encoded instruction

How to distinguish from nearby codes:

- vs `202/203/6`: not a TLB translation miss class
- vs `206/207`: not instruction/data bus completion failure class
- vs `204/205`: not alignment/address-error class

Triage note:

- resolve `CRASH_ADDR` to confirm whether the faulting PC is in expected test/assert/trap path
- if `213` appears in production (non-test) flows, inspect control-flow integrity, assertions, and unexpected execution path triggers

### What `system 224` Means

`system 224` maps to:

- `CRASH_FUNC = 200 + 24`
- exception code `24` = `Machine Check`

Practical meaning:

- severe machine-level fault path
- prioritize hardware/integrity triage (power, memory/cache/bus, board condition)

---

## TLB Refill Handler Patterns (CRASH_FUNC = 6)

### Key Challenge: Distinguishing Fault Types

Both **instruction fetch** faults and **data access** faults can trigger the same handler with the same exception code.

**Pattern:**
```
CRASH_FUNC = 6
CRASH_DIAG[0] = 2 (TLBL - TLB Load exception)
```

**Question:** Was this an instruction fetch or a data read?

### Solution: Compare BadVAddr with EPC

**Empirically Validated Pattern:**

```python
if CRASH_FUNC == 6:
    exception_code = CRASH_DIAG[0]
    bad_vaddr = CRASH_DIAG[1]
    epc = CRASH_ADDR
    
    if exception_code == 2:  # TLBL - TLB Load
        # Both instruction fetch and data read show code 2
        
        if abs(bad_vaddr - epc) <= 4:
            # BadVAddr ≈ EPC (within instruction size)
            fault_type = "Instruction fetch from unmapped address"
            scenario = "Bad function pointer / corrupted return address"
            
        else:
            # BadVAddr ≠ EPC (significantly different)
            fault_type = "Data read from unmapped address"
            scenario = "Null pointer dereference / corrupted data pointer"
            
    elif exception_code == 3:  # TLBS - TLB Store
        # Always data access (can't store to instruction stream)
        fault_type = "Data write to unmapped address"
        scenario = "Null pointer dereference on write / corrupted pointer"
```

**Test Coverage:**
- **Instruction fetch tests:** 6, 14-17, 0xF3, 0xF5 (BadVAddr ≈ EPC)
- **Data write test:** 0xF2 (BadVAddr ≠ EPC)
- **Data read test:** 19 (BadVAddr ≠ EPC)

---

## BadVAddr CPU Behavior (EMPIRICALLY VALIDATED)

**Critical Finding:** CPU clears **bit 0 (LSB) ONLY** in BadVAddr register.

### Pattern Validation

Tested across 5 different addresses:

| Test Address | Binary (last 4 bits) | BadVAddr Result | Bit 0 Status |
|--------------|---------------------|-----------------|--------------|
| 0xFFFFFFFF   | ...1111             | 0xFFFFFFFE      | Cleared      |
| 0xFFFFFFFD   | ...1101             | 0xFFFFFFFC      | Cleared      |
| 0xFFFFFFFB   | ...1011             | 0xFFFFFFFA      | Cleared      |
| 0x00000001   | ...0001             | 0x00000000      | Cleared      |
| 0x00000003   | ...0011             | 0x00000002      | Cleared      |

**Conclusion:**
- CPU clears **bit 0 only** (LSB)
- CPU does **NOT** perform full word alignment (clearing bits 0-1)
- Pattern is consistent across all tested addresses

**Analysis Implication:**
```python
# Do NOT assume full alignment
original_addr_estimate = bad_vaddr | 0x01  # Could be +0 or +1 from actual
# Cannot determine bits 2-3 from BadVAddr alone
```

---

## Hardware Unaligned Access Support

**CRITICAL FINDING:** PIC32MZ unaligned memory access support is **REGION-SPECIFIC**, not universal.

**Empirically Validated Behavior:**

### Flash Memory (0x9D, 0xBD) - NO Unaligned Support ❌
- **Test 18:** Read from 0x9D000001 → **CRASH_FUNC=204 (AdEL)** ✅
- Flash memory controller does NOT handle unaligned access
- AdEL/AdES are **COMMON** for unaligned flash access

### RAM Memory (0x80, 0xA0) - YES Unaligned Support ✅
- **Test 20:** Unaligned RAM read (manual cast) → **NO CRASH** ✅
- **Test 21:** Packed struct field in RAM → **NO CRASH** ✅
- RAM memory controller handles misalignment transparently
- AdEL/AdES are **RARE** for RAM access (indicates other issues)

**Test Code:**
```c
// Test 18: Flash unaligned read (CRASHED)
volatile int *flash_ptr = (volatile int *)0x9D000001;
volatile int dummy = *flash_ptr;  // AdEL exception!

// Test 20: RAM unaligned read (NO CRASH)
struct __attribute__((packed)) test_struct {
    unsigned char byte1;
    unsigned long unaligned;  // offset 1, not 4-byte aligned
};
static struct test_struct data = {0x42, 0xDEADBEEF};
volatile unsigned long *ram_ptr = (volatile unsigned long *)((char*)&data + 1);
volatile unsigned long val = *ram_ptr;  // Works fine in RAM

// Test 21: Compiler-aware packed struct (NO CRASH)
volatile unsigned long lvar = data.unaligned;  // Compiler handles it
```

**Packed Structures Implications:**
- Packed structures throughout codebase (export.h: CFuelCellStateEx, CXCommStat, etc.) are **SAFE**
- They're allocated in RAM where unaligned access is supported
- If const packed struct data exists in flash, unaligned field access will crash

**When AdEL/AdES WILL Occur:**
- **Flash region (0x9D/0xBD):** Unaligned pointer accessing const data or string literals
- **RAM region (0x80/0xA0):** Pointer corruption, invalid address, or DMA misconfiguration (rare)
- Instruction fetch from unaligned address (cannot be handled transparently)
- Some atomic operations may require alignment

**Analysis Priority:**
- **Flash AdEL/AdES:** Expected for unaligned pointers - check const data access
- **RAM AdEL/AdES:** Unusual - investigate pointer corruption or invalid addresses
- **TLB Refill** (`CRASH_FUNC = 6`) remains most common overall

---

## Automated Analysis Decision Tree

```
START
  |
  v
Read CRASH_FUNC
  |
  ├─ CRASH_FUNC = 6 ──> TLB Refill
  |   |
  |   ├─ Read CRASH_DIAG[0] (exception code)
  |   |   |
  |   |   ├─ Code 2 (TLBL) ──> TLB Load
  |   |   |   |
  |   |   |   ├─ Compare CRASH_DIAG[1] (BadVAddr) with CRASH_ADDR (EPC)
  |   |   |   |   |
  |   |   |   |   ├─ BadVAddr ≈ EPC ──> "Instruction fetch from unmapped"
  |   |   |   |   |                      - Bad function pointer
  |   |   |   |   |                      - Corrupted return address
  |   |   |   |   |                      - Jump to 0x00000000 or invalid addr
  |   |   |   |   |
  |   |   |   |   └─ BadVAddr ≠ EPC ──> "Data read from unmapped"
  |   |   |   |                          - Null pointer dereference (read)
  |   |   |   |                          - Reading from freed memory
  |   |   |   |                          - Corrupted data pointer
  |   |   |   |
  |   |   └─ Code 3 (TLBS) ──> TLB Store
  |   |       |
  |   |       └─> "Data write to unmapped"
  |   |           - Null pointer dereference (write)
  |   |           - Writing to freed memory
  |   |           - Buffer overflow into unmapped region
  |   |
  |   └─ Output: BadVAddr (CRASH_DIAG[1]), EPC (CRASH_ADDR), SP, RA
  |
  ├─ CRASH_FUNC = 7 ──> Cache Error
  |   └─> "Hardware error - cache subsystem"
  |       - Possible RAM failure
  |       - Signal integrity issue
  |       - Power supply problem
  |
    ├─ CRASH_FUNC = 200+N ──> General Exception (N = exception code)
    |   |
    |   ├─ N=4 (204) ──> AdEL - Address Error (Load)
  |   |   |
  |   |   └─> Check CRASH_ADDR (BadVAddr) memory region:
  |   |       |
  |   |       ├─ 0x9D000000-0x9DFFFFFF (Flash) ──> "Unaligned flash access"
  |   |       |   └─> COMMON - flash does NOT support unaligned access
  |   |       |       - Unaligned pointer to const data
  |   |       |       - Unaligned string literal access
  |   |       |       - Check packed structures in flash
  |   |       |
  |   |       ├─ 0x80000000-0x8007FFFF (RAM) ──> "Unusual RAM AdEL"
  |   |       |   └─> RARE - RAM supports unaligned access
  |   |       |       - Pointer corruption likely
  |   |       |       - Invalid address calculation
  |   |       |       - Check for buffer overruns
  |   |       |
  |   |       └─ Unaligned instruction fetch (BadVAddr ≈ EPC)
  |   |           └─> Jump to odd address
  |   |               - Corrupted function pointer
    |   |
    |   ├─ N=5 (205) ──> AdES - Address Error (Store)
  |   |   |
  |   |   └─> Check CRASH_ADDR (BadVAddr) memory region:
  |   |       |
  |   |       ├─ Flash region ──> "Unaligned flash write attempt"
  |   |       |   └─> COMMON - flash does NOT support unaligned access
  |   |       |
  |   |       └─ RAM region ──> "Unusual RAM AdES"
  |   |           └─> RARE - RAM supports unaligned access
  |   |               - Pointer corruption
  |   |               - Check atomic operations
  |   |
  |   ├─ N=6 (206) ──> IBE - Instruction Bus Error
  |   |   └─> "Instruction fetch from invalid physical memory" (VERY RARE)
  |   |       - Requires aligned, mapped, but physically invalid
  |   |       - Possible TLB misconfiguration
  |   |
  |   ├─ N=7 (207) ──> DBE - Data Bus Error
  |   |   └─> "Data access to invalid physical memory" (VERY RARE)
  |   |
  |   ├─ N=8 (208) ──> Syscall
  |   |   └─> "Intentional syscall instruction" (TEST ONLY)
  |   |
  |   ├─ N=9 (209) ──> Breakpoint
  |   |   └─> "Intentional breakpoint or corrupted code"
  |   |
  |   ├─ N=10 (210) ──> Reserved Instruction
  |   |   └─> "Invalid/corrupted instruction"
  |   |       - Executing from data region
  |   |       - Memory corruption in code space
  |   |       - Wrong CPU architecture binary
  |   |
  |   ├─ N=12 (212) ──> Arithmetic Overflow
  |   |   └─> "Integer overflow in ADD instruction" (if enabled)
  |   |
  |   └─ N=13 (213) ──> Trap
  |       └─> "Divide by zero or explicit trap"
  |
  └─ CRASH_FUNC = Other ──> Non-Exception Crash
      |
      ├─ 100-199 ──> Test/Debug Functions
      |   └─> Look up in breadcrumb mapping
      |
      └─ Other ──> Application-Specific Crash
          └─> Consult crash function mapping
```

---

## Breadcrumb Trail Pattern

**⚠️ TEST/DEBUG ONLY - NOT present in production crashes**

**Pattern:** In commanded/artificial test scenarios, CRASH_FUNC values form a breadcrumb trail showing execution path through test infrastructure.

**Example from Test 6:**
```
XCMISC_FUNC 106  →  SYS_FUNC 100  →  SYS_FUNC 6
    (entry)         (test runner)    (TLB handler)
```

**Decoding:**
- `XCMISC_FUNC 106` = `XCMISC_FUNC (100 + test_code)` = test code 6
- `SYS_FUNC 100` = `TriggerException()` function
- `SYS_FUNC 6` = `_simple_tlb_refill_exception_handler`

**For Test Analysis:**
- Start from most recent CRASH_FUNC (exception handler)
- Work backward through breadcrumbs to find test origin
- Test codes: 0-31 show as XCMISC 100+N
- Special tests: 0xF0-0xF5 show as XCMISC 0xF0-0xF5

**For Production Crashes:**
- No breadcrumb trail present
- CRASH_FUNC will be just the exception handler ID (6, 7, 200+N, etc.)
- Analysis must rely on CRASH_ADDR (EPC), CRASH_DIAG (BadVAddr, SP, RA), and context

---

## Sample: CRASH_FUNC 207 (DBE)

### Example Symptom

- Reported crash attribution: `if(serial_control[SP_PORT].TxDone != 1)` in `Serial.cpp` (UART3 TX ISR, `SP_PORT = 2`)
- This line is a data read from `serial_control[2].TxDone`

### What 207 Means Here

- `CRASH_FUNC = 207` means general handler with exception code 7 (`DBE`, data bus error)
- In practical terms: a data load/store bus transaction failed
- This is usually **not** a simple misalignment fault (`AdEL/AdES` would be `204/205`)

### Practical Interpretation for This Case

- If the fault points at the `TxDone` read, the source line is where the CPU noticed the failing access
- Common software-side cause: corrupted execution context (stack/register corruption) causing an invalid effective address for the load
- Less common cause: true hardware/bus issue while accessing SRAM/peripheral fabric
- Cross-build confirmation: a different git hash / ELF also resolved a separate `207` PC (`0x9d0737cc`) to the same `_IntHandlerUartTransmit3` `TxDone` check, so the repeated signature is tied to the same logical code path rather than one specific binary layout

### Triage Checklist

1. Verify `CRASH_ADDR` resolves near the UART3 TX ISR load instruction
2. Check `CRASH_DIAG[5]` (SP) for out-of-range or suspicious values
3. Check `CRASH_DIAG[6]` (RA):
    - valid flash range -> software path still plausible
    - outside code range -> strong corruption signal
4. Distinguish by handler code:
    - `204/205` -> alignment path
    - `6` -> TLB/unmapped path
    - `207` -> data bus/physical access path

### Automation Hint

```python
if crash_func == 207:
     classification = "DBE (data bus error)"
     likely_primary = "invalid effective address or bus transaction failure"
     likely_secondary = "context corruption before faulting load/store"
```

---

## Sample: CRASH_FUNC 202 (TLBL via General Handler)

### Example Symptom

- Crash log reports `CRASH_FUNC = 202` with a code address in flash (`~0x9Dxxxxxx`)
- Crash context suggests an attempted read/fetch through an invalid or unmapped virtual address

### What 202 Means Here

- `CRASH_FUNC = 202` means general handler with exception code 2 (`TLBL`, TLB Load exception)
- In practical terms: a load-side translation fault (instruction fetch or data read) reached `_general_exception_handler`
- This is a translation-class failure, not a bus-completion class like `207`

### Practical Interpretation for This Case

- If `BADVADDR` is near `EPC`, treat it as likely instruction-fetch TLBL
- If `BADVADDR` is far from `EPC`, treat it as likely data-read TLBL (null/corrupted pointer read)
- If telemetry is sparse (only `CRASH_FUNC` + one address), confidence drops quickly; preserve `BADVADDR` and `NESTEDEPC`

### Triage Checklist

1. Verify build-match and resolve the logged PC against the correct ELF/map
2. Compare `BADVADDR` with `EPC` (if available) to classify fetch vs data-read TLBL
3. Check `CRASH_DIAG[5]` (SP) and `CRASH_DIAG[6]` (RA) for control-flow corruption signals
4. Differentiate from related codes:
    - `6` = same TLB-load class, different handler routing
    - `203` = store-side TLB class
    - `207` = data bus failure, not translation miss

### Automation Hint

```python
if crash_func == 202:
    classification = "TLBL via general handler"
    likely_primary = "unmapped/invalid virtual address on load path"
    likely_secondary = "bad pointer or corrupted control flow"
```

---

## Sample: CRASH_FUNC 213 (Trap)

### Example Symptom

- Crash log reports `CRASH_FUNC = 213` with PC resolving to a trap-related code path
- Trigger may have been test command, assert-style trap, or trap-qualified arithmetic behavior

### What 213 Means Here

- `CRASH_FUNC = 213` means general handler with exception code 13 (`Trap`)
- In practical terms: CPU entered trap exception path
- This is generally software-intentional or control-flow-related, not a TLB/bus/alignment class fault

### Practical Interpretation for This Case

- In test/debug flows, `213` can be expected and useful for validation
- In production flows, `213` is usually suspicious and should trigger control-flow/assert-path review
- Divide-by-zero trap behavior can be implementation/config dependent on MIPS; explicit trap instructions are more reliable reproductions

### Triage Checklist

1. Resolve `CRASH_ADDR` and verify whether PC is in expected trap/assert/test path
2. Confirm whether unit was in commanded test mode or normal operation
3. Check `RA`/`SP` for control-flow integrity signs if trap location is unexpected
4. Differentiate from related codes:
    - `202/203/6` = TLB translation class
    - `206/207` = bus-failure class
    - `204/205` = alignment/address-error class

### Automation Hint

```python
if crash_func == 213:
    classification = "Trap exception"
    likely_primary = "intentional trap/assert/test path"
    likely_secondary = "unexpected control-flow into trap instruction"
```

---

## Common Crash Scenarios

### 1. Null Pointer Dereference (Most Common)

**Symptoms:**
```
CRASH_FUNC = 6
CRASH_DIAG[0] = 2 or 3 (TLBL/TLBS)
CRASH_DIAG[1] = 0x00000000 (or near-zero)
```

**Analysis:**
- Check CRASH_DIAG[6] (RA) to find calling function
- Check CRASH_DIAG[5] (SP) to verify stack integrity
- If BadVAddr ≈ EPC: function pointer was null
- If BadVAddr ≠ EPC: data pointer was null

### 2. Corrupted Stack/Return Address

**Pattern 1: Null Return**
```
CRASH_FUNC = 6
CRASH_DIAG[0] = 2 (TLBL)
CRASH_DIAG[1] = 0x00000000
BadVAddr ≈ EPC (both near zero)
```
→ Function returned to 0x00000000 (stack corruption)

**Pattern 2: Unmapped Return**
```
CRASH_FUNC = 6
CRASH_DIAG[0] = 2 (TLBL)
CRASH_DIAG[1] = 0xXXXXXXXE (bit 0 cleared)
BadVAddr ≈ EPC
```
→ Function returned to garbage address (stack overflow/corruption)

**Pattern 3: Unaligned Return (Rare)**
```
CRASH_FUNC = 204 (AdEL)
```
→ Function returned to odd address in mapped memory

### 3. Use After Free / Dangling Pointer

**Symptoms:**
```
CRASH_FUNC = 6
CRASH_DIAG[0] = 2 or 3
CRASH_DIAG[1] = mid-range address (freed heap memory)
BadVAddr ≠ EPC (significantly different)
```

**Analysis:**
- Check if BadVAddr is in heap range
- Review recent free() calls
- Check for pointer used after free

### 4. Hardware Errors

**Symptoms:**
```
CRASH_FUNC = 7 (cache error)
  OR
CRASH_FUNC = 224 (machine check)
```

**Analysis:**
- Not a software bug
- Check hardware: power supply, temperature, RAM
- Review signal integrity
- Check for intermittent failures

---

## Stack Pointer Analysis

**Valid SP Ranges:**
- Task stacks: Allocated by FreeRTOS, check task definitions
- ISR stack: Check `xISRStack` definition and `configISR_STACK_SIZE`

**SP Analysis:**
```python
sp = CRASH_DIAG[5]

# Check if SP is reasonable
if sp < 0x80000000 or sp > 0x80080000:
    print("WARNING: SP outside SRAM range - stack corruption likely")
    
# Check for stack overflow
# Compare SP with stack base addresses from linker map
```

**Red Flags:**
- SP outside SRAM range (0x80000000 - 0x80080000)
- SP very close to stack limit (potential overflow)
- SP misaligned (should be 8-byte aligned typically)

---

## Return Address Analysis

**Valid RA Ranges:**
- Flash: 0x9D000000 - 0x9D1FFFFF (program code)
- RAM: Could be valid for function pointers to RAM code

**RA Analysis:**
```python
ra = CRASH_DIAG[6]

# Check if RA points to valid code
if 0x9D000000 <= ra <= 0x9D1FFFFF:
    # Valid flash address
    # Use addr2line to find calling function
    print(f"addr2line -e firmware.elf 0x{ra:08X}")
else:
    print("WARNING: RA outside code range - stack corruption")
```

**Using addr2line:**
```bash
addr2line -e build/firmware.elf 0x9D012345
# Output: c:/Users/.../source_file.c:line_number
```

---

## Implementation Recommendations

### Python Script Structure

```python
class CrashDumpAnalyzer:
    def __init__(self, crash_func, crash_addr, diag):
        self.crash_func = crash_func
        self.crash_addr = crash_addr  # EPC
        self.diag = diag  # Array of diagnostic values
        
    def analyze(self):
        if self.crash_func == 6:
            return self.analyze_tlb_refill()
        elif self.crash_func == 7:
            return self.analyze_cache_error()
        elif 200 <= self.crash_func < 300:
            return self.analyze_general_exception()
        else:
            return self.analyze_other()
    
    def analyze_tlb_refill(self):
        exc_code = self.diag[0]
        bad_vaddr = self.diag[1]
        epc = self.crash_addr
        sp = self.diag[5]
        ra = self.diag[6]
        
        result = {
            'handler': 'TLB Refill',
            'exception_code': exc_code,
            'bad_vaddr': f"0x{bad_vaddr:08X}",
            'epc': f"0x{epc:08X}",
            'sp': f"0x{sp:08X}",
            'ra': f"0x{ra:08X}"
        }
        
        # Distinguish instruction fetch vs data access
        if abs(bad_vaddr - epc) <= 4:
            result['fault_type'] = "Instruction fetch"
            result['scenario'] = "Bad function pointer or corrupted RA"
        else:
            if exc_code == 2:
                result['fault_type'] = "Data read"
                result['scenario'] = "Null pointer dereference (read)"
            elif exc_code == 3:
                result['fault_type'] = "Data write"
                result['scenario'] = "Null pointer dereference (write)"
        
        return result
    
    def analyze_general_exception(self):
        exc_code = self.crash_func - 200
        
        if exc_code == 4:  # AdEL
            return self.analyze_adel()
        elif exc_code == 5:  # AdES
            return self.analyze_ades()
        # ... other exception codes
        
    def analyze_adel(self):
        """Address Error (Load) - REGION-SPECIFIC analysis"""
        epc = self.crash_addr  # In this project, CRASH_ADDR is EPC
        fault_addr = epc       # If BadVAddr is not separately persisted, use EPC as best available fault-location proxy
        
        result = {
            'handler': 'AdEL (Address Error (Load))',
            'fault_addr': f"0x{fault_addr:08X}"
        }
        
        # Check memory region
        is_flash = ((0x9D000000 <= fault_addr <= 0x9DFFFFFF) or 
                (0xBD000000 <= fault_addr <= 0xBDFFFFFF))
        is_ram = ((0x80000000 <= fault_addr <= 0x8007FFFF) or 
              (0xA0000000 <= fault_addr <= 0xA007FFFF))
        
        if is_flash:
            result['region'] = "Flash (0x9D/0xBD)"
            result['analysis'] = "Unaligned access in flash - NOT supported by hardware"
            result['likely_cause'] = "Unaligned pointer to const data or string literal"
            result['severity'] = "COMMON - expected for flash unaligned access"
        elif is_ram:
            result['region'] = "RAM (0x80/0xA0)"
            result['analysis'] = "AdEL in RAM is UNUSUAL - RAM supports unaligned access"
            result['likely_cause'] = "Pointer corruption or invalid address calculation"
            result['severity'] = "RARE - investigate pointer corruption"
        else:
            # Check if instruction fetch proximity (fault_addr ≈ EPC)
            if abs(fault_addr - epc) <= 4:
                result['fault_type'] = "Instruction fetch from unaligned address"
                result['likely_cause'] = "Jump to odd address"
            else:
                result['region'] = "Unknown/Unmapped"
                result['likely_cause'] = "Invalid address"
        
        return result
    
    def analyze_ades(self):
        """Address Error (Store) - REGION-SPECIFIC analysis"""
        bad_vaddr = self.crash_addr
        
        result = {
            'handler': 'AdES (Address Error (Store))',
            'bad_vaddr': f"0x{bad_vaddr:08X}"
        }
        
        # Check memory region (same logic as AdEL)
        is_flash = ((0x9D000000 <= bad_vaddr <= 0x9DFFFFFF) or 
                    (0xBD000000 <= bad_vaddr <= 0xBDFFFFFF))
        is_ram = ((0x80000000 <= bad_vaddr <= 0x8007FFFF) or 
                  (0xA0000000 <= bad_vaddr <= 0xA007FFFF))
        
        if is_flash:
            result['region'] = "Flash"
            result['analysis'] = "Unaligned write to flash - NOT supported"
            result['severity'] = "COMMON for flash writes"
        elif is_ram:
            result['region'] = "RAM"
            result['analysis'] = "AdES in RAM is UNUSUAL - RAM supports unaligned access"
            result['likely_cause'] = "Atomic operation or pointer corruption"
            result['severity'] = "RARE - investigate"
        
        return result
        
    def validate_sp(self, sp):
        # Check if SP is in valid SRAM range
        return 0x80000000 <= sp <= 0x80080000
    
    def validate_ra(self, ra):
        # Check if RA points to flash (code region)
        return 0x9D000000 <= ra <= 0x9D1FFFFF
### addr2line Integration

```python
import subprocess

def resolve_address(elf_file, address):
    """Use addr2line to resolve address to source file:line"""
    try:
        result = subprocess.run(
            ['addr2line', '-e', elf_file, f'0x{address:08X}'],
            capture_output=True,
            text=True
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Error: {e}"

# Usage
source_location = resolve_address('build/firmware.elf', crash_addr)
print(f"Crash location: {source_location}")
```

---

## Testing Validation

**Empirically validated (completed on hardware):**
- Test 6: Jump to `0xFFFFFFFF` → **CRASH_FUNC=6**, `CRASH_DIAG[0]=2`, `CRASH_DIAG[1]=0xFFFFFFFE`; confirms TLB check precedes alignment.
- Tests 14-17: Unaligned unmapped jump set (`0xFFFFFFFD`, `0xFFFFFFFB`, `0x00000001`, `0x00000003`) → confirms BadVAddr clears bit 0 consistently.
- Test 18: Unaligned flash read (`0x9D000001`) → **CRASH_FUNC=204 (AdEL)**.
- Test 19: Unmapped data read (`0xFFFF0000`) → **CRASH_FUNC=6 (TLB)** with BadVAddr ≠ EPC (data-access signature).
- Test 20: Unaligned RAM read (manual cast) → **no crash**.
- Test 21: Unaligned RAM read (compiler-aware packed field) → **no crash**.

**Implemented in firmware and command path, pending empirical run documentation:**
- Tests 28, 29, 30, 31 are implemented in `TriggerException()` and reachable via `GCS_CMD_EXCEPTION_TEST` (`test_ID <= 32`).
- Test 32 is implemented in `TriggerException()` and reachable via `GCS_CMD_EXCEPTION_TEST`.
- Special tests `0xF2`, `0xF3`, `0xF4`, `0xF5` are implemented and routed in `GcsInterface.c`.

**ID correction / planning note:**
- The uncached-flash jump test in current code is `test_ID 27` (`0xBD000000`), not `33`.

**Current high-confidence findings used by automation:**
- Unaligned memory behavior is region-specific: flash faults (`AdEL`), RAM access succeeds.
- TLB handler triage using BadVAddr vs EPC is reliable for distinguishing instruction fetch vs data access in validated cases.

---

## Future Enhancements

**Potential Additions:**
1. **Symbol Resolution:** Parse .elf symbol table to show function names
2. **Stack Unwinding:** Analyze stack contents to show call chain
3. **Pattern Database:** Build database of known crash patterns
4. **Automated Triage:** Categorize crashes by severity/likelihood
5. **Trend Analysis:** Track crash patterns over time
6. **Report Generation:** Generate human-readable crash reports

---

## Revision History

| Date | Version | Changes |
|------|---------|---------|
| 2026-02-18 | 1.0 | Initial document with empirically validated patterns |
| 2026-03-19 | 1.1 | Updated validation status by test, corrected uncached test ID (27 vs 33), added routability note for test 32 |
| 2026-03-23 | 1.2 | Added `system 203` interpretation/triage guidance and cross-reference to `CRASH_207_INVESTIGATION_SUMMARY.md` telemetry requirements section |
| 2026-03-24 | 1.3 | Added `system 206` interpretation/triage guidance with differential notes vs `6`/`204`/`205`/`207` |
| 2026-03-24 | 1.4 | Added `system 202` and `system 213` interpretation/triage guidance and aligned short examples list |
| 2026-03-24 | 1.5 | Added sample sections for `CRASH_FUNC 202` and `CRASH_FUNC 213` with triage checklists and automation hints |
| 2026-03-24 | 1.6 | Added compact `What system 2XX Means` entries for missing referenced codes (`204`,`205`,`207`,`208`,`209`,`210`,`212`,`224`) |

---

## References

- MIPS Architecture Documentation
- PIC32MZ Family Reference Manual: Section 50 (CPU)
- PIC32MZ Datasheet: Table 7-1 (Exception Codes)
- EXCEPTION_TEST_PLAN.md (test specifications)
- utils.c (exception handler implementations)
