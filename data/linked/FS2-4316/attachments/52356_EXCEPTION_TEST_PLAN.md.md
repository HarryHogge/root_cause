# EXCEPTION_TEST_PLAN.md

Attachment 52356, text, 48 KB, added 2026-04-02 by Scott Hunter.

# Exception Test Plan
## PIC32MZ Exception Handler Validation

**Purpose:** Validate that all exception handlers correctly capture diagnostic data and that the test infrastructure works as designed.

**Prerequisites:**
- Firmware built with `BUILD_EXCEPTION_TESTS = 1`
- Device accessible at target IP (e.g., 10.129.151.2)
- Python script `trigger_exception_test.py` available
- Access to crash dump retrieval mechanism

---

## Understanding CRASH_ADDR

**CRASH_ADDR** contains the EPC (Exception Program Counter) register value - the address of the instruction that caused (or was executing when) the exception occurred.

### Expected CRASH_ADDR Patterns:

**Most Tests (AdEL, AdES, DBE, Sys, Bp, RI, Overflow, Trap, TLB):**
- CRASH_ADDR will be in flash memory range: **0x9D000000 - 0x9D1FFFFF**
- Points to the specific instruction inside the test function that faulted
- Can be looked up in .elf file to find exact source line
- Should be inside `TriggerException()` or `TestTlbRefill()` functions

**Instruction-fetch to 0xFFFFFFFF (Test 6) - SPECIAL CASE:**
- `CRASH_FUNC` is expected to be **6 (TLB Refill)**, not **206 (IBE)**
- Reason: CPU checks TLB mapping before alignment/physical validity
- `CRASH_ADDR` = **0xFFFFFFFF** (attempted fetch EPC)
- `CRASH_DIAG[1]` = **0xFFFFFFFE** (BadVAddr with bit 0 cleared)
- True IBE (`system 206`) requires aligned + mapped + physically invalid instruction source (rare/difficult to force)

**Stack Overflow Tests (0xF0, 0xF1):**
- CRASH_ADDR is **unpredictable** - depends on when/how overflow is detected
- Could be inside recursive function at various depths
- Could be in exception handler if corruption detected
- Could be in FreeRTOS context switch or stack check code
- May show corrupted values if stack really overflowed

**Post-Test Analysis:**
- Use CRASH_ADDR with `addr2line` tool to find source line for most tests
- Example: `addr2line -e build/firmware.elf 0x9D012345`
- Each test below includes specific addr2line verification instructions

---

## Test Procedure

For each test:
1. Send UDP command via Python script
2. Wait for device to crash (infinite loop in exception handler)
3. Retrieve crash dump via debugger or crash retrieval mechanism
4. Verify crash dump values match expected results
5. Power cycle device to prepare for next test

---

## Test Cases

### Test 1: Address Error (Load) - AdEL
**Command:**
```bash
python trigger_exception_test.py 10.129.151.2 4
```

**Expected Behavior:**
- Message logged: "TEST: Triggering AdEL - Address error (load)"
- System crashes attempting to read from unaligned address 0x00000001

**Expected Crash Dump:**
- `CRASH_FUNC`: `SYS_FUNC`, code = **204** (200 + 4)
- `CRASH_ADDR`: **~0x9D0xxxxx** - address of load instruction in TriggerException() that reads from 0x00000001
- `CRASH_DIAG[5]`: Stack pointer (SP) at exception time
- `CRASH_DIAG[6]`: Return address (RA) at exception time
- Exception code: **4** (EXCEP_AdEL)

**Real-world AdEL scenario:** Stack corruption can also cause AdEL on function return:
- **CPU checks faults in this order (precedence) - EMPIRICALLY VALIDATED:**
  1. **TLB mapping** (checked FIRST - highest priority) → TLB Refill if unmapped/null
  2. **Alignment** (checked second, if mapped) → AdEL/AdES if fails
  3. **Physical memory** (checked third, if mapped+aligned) → IBE/DBE if invalid

- **Corrupted return address results:**
  - **Null/aligned** (0x00000000): **TLB Refill (code 6)** - fails TLB lookup immediately
    - Aligned but unmapped → TLB handler (precedence: checked first)
    - Check CRASH_FUNC=6, CRASH_DIAG[0]=2 (TLBL), CRASH_DIAG[1]=0x00000000 (BadVAddr)
  - **Unaligned AND unmapped** (0xFFFFFFFF): **TLB Refill (code 6)** - fails TLB lookup before alignment check
    - Both misaligned AND unmapped, but TLB checked first
    - BadVAddr has bit 0 cleared: CRASH_DIAG[1]=0xFFFFFFFE (from 0xFFFFFFFF)
    - Exception code: CRASH_DIAG[0]=2 (TLBL), NOT AdEL
  - **Unaligned but mapped** (0x9D012345): **AdEL exception (code 204)** - passes TLB, fails alignment
    - Mapped (passes first check)
    - But unaligned → AdEL (precedence: checked second)
    - CPU attempts `jr $ra` to unaligned address in valid memory region
  - **Aligned but unmapped** (0x12345678): **TLB Refill (code 6)** - fails TLB lookup
    - Aligned (would pass second check)
    - But unmapped → TLB handler (precedence: checked first)
    - Check CRASH_FUNC=6, CRASH_DIAG[0]=2, CRASH_DIAG[1]=0x12345678
  - **Aligned, mapped, but invalid physical** (very rare): **IBE (code 206)** - passes TLB and alignment, fails memory access
    - Aligned (passes second check)
    - Mapped via TLB entry (passes first check)
    - But TLB maps to invalid physical address → IBE (precedence: checked third)
    - Requires TLB manipulation - very difficult to test
- For instruction-fetch corruption cases, `CRASH_ADDR` captures the attempted fetch address.
- `CRASH_DIAG[6]` is RA and often points to the call site after the indirect jump/call, not the corrupted target itself.
- Check CRASH_DIAG[5] (SP) to locate stack corruption

**addr2line Verification:**
- ✅ CRASH_ADDR should resolve to: `dummy = *(volatile int *)0x00000001;` in TriggerException()
- Command: `addr2line -e build/firmware.elf <CRASH_ADDR>`
- Expected output: `c:/Users/.../utils.c:<line_number>`

---

### Test 2: Address Error (Store) - AdES
**Command:**
```bash
python trigger_exception_test.py 10.129.151.2 5
```

**Expected Behavior:**
- Message logged: "TEST: Triggering AdES - Address error (store)"
- System crashes attempting to write to unaligned address 0x00000003

**Expected Crash Dump:**
- `CRASH_FUNC`: `SYS_FUNC`, code = **205** (200 + 5)
- `CRASH_ADDR`: **~0x9D0xxxxx** - address of store instruction in TriggerException() that writes to 0x00000003
- `CRASH_DIAG[5]`: Stack pointer (SP)
- `CRASH_DIAG[6]`: Return address (RA)
- Exception code: **5** (EXCEP_AdES)

**addr2line Verification:**
- ✅ CRASH_ADDR should resolve to: `*(volatile int *)0x00000003 = 0xDEADBEEF;` in TriggerException()
- Command: `addr2line -e build/firmware.elf <CRASH_ADDR>`
- Expected output: `c:/Users/.../utils.c:<line_number>`

---

### Test 3: TLB Refill (from IBE test intent) - TLBL
**Command:**
```bash
python trigger_exception_test.py 10.129.151.2 6
```

**Test Intent:** Originally designed to test IBE (Bus Error on instruction fetch)

**Actual Behavior (EMPIRICALLY VALIDATED):**
- Address 0xFFFFFFFF is BOTH misaligned (ends in binary `11`) AND unmapped
- CPU checks TLB mapping FIRST (highest priority), before alignment
- Because 0xFFFFFFFF is unmapped, TLB Refill exception triggers
- CPU never gets to alignment check (which would have been AdEL)
- CPU stores BadVAddr with bit 0 cleared: 0xFFFFFFFF → 0xFFFFFFFE
  - (Note: 0xFFFFFFFF = `...11111111` binary, 0xFFFFFFFE = `...11111110` binary)
  - Hardware implementation detail - CPU clears least significant bit when storing to BadVAddr
  - This is NOT full word alignment (would be 0xFFFFFFFC with bottom 2 bits = `00`)

**Breadcrumb Trail (Execution Order):**
1. **GcsInterface.c:252**: `CRASH_FUNC(XCMISC_FUNC, 106)` - UDP handler (100 + test_code 6)
2. **utils.c:1523**: `CRASH_FUNC(SYS_FUNC, 100)` - TriggerException entry marker
3. **utils.c:1545**: Jump to 0xFFFFFFFF via function pointer
4. **utils.c:1604**: `CRASH_FUNC(SYS_FUNC, 6)` - TLB refill handler catches it

**Expected Crash Dump (VALIDATED WITH ACTUAL RESULTS):**
- `CRASH_FUNC`: `SYS_FUNC`, code = **6** (_simple_tlb_refill_exception_handler)
- `CRASH_ADDR`: **0xFFFFFFFF** - EPC captures where CPU tried to fetch instruction
- `CRASH_DIAG[0]`: **0x00000002** - Exception code from Cause register (TLBL)
- `CRASH_DIAG[1]`: **0xFFFFFFFE** - BadVAddr (address with bit 0 cleared by CPU hardware)
- `CRASH_DIAG[5]`: **Stack pointer (SP)** at exception time (e.g., 0x80061DA0)
- `CRASH_DIAG[6]`: **Return address (RA)** - points to instruction after bad_func() call in TriggerException (e.g., 0x9D1057B8)

**Trace Pattern:**
```
func(-1) system 100  ← TriggerException entry breadcrumb
func(0) system 6     ← TLB refill handler (final)
```

**Key Finding:** This test validates that **TLB mapping is checked BEFORE alignment** in CPU exception precedence.

**To Test True IBE:** Would require:
- Address that is **aligned** (passes alignment check)
- Address that is **mapped** via TLB entry (passes TLB check)
- TLB entry points to **invalid physical memory** (triggers IBE)
- This is very difficult without TLB manipulation - deferred

**Real-world scenario:** If a corrupted function pointer has value 0xFFFFFFFF:
- **Result**: TLB Refill (code 6), NOT IBE
- Check CRASH_FUNC=6, CRASH_DIAG[0]=2 (TLBL), CRASH_DIAG[1]=0xFFFFFFFE
- For other corrupted values, see CPU exception precedence in Test 1

**addr2line Verification:**
- ❌ CRASH_ADDR (0xFFFFFFFF) is NOT a code address - addr2line will FAIL
- ✅ Instead use CRASH_DIAG[6] (RA) to find the call site in YOUR CODE
- Command: `addr2line -e build/firmware.elf <CRASH_DIAG[6]>`
- Expected: Points to instruction after `bad_func();` call in TriggerException()
- Example RA: 0x9D1057B8 → utils.c line with function pointer call

---

### Test 4: Bus Error (Data) - DBE
**Command:**
```bash
python trigger_exception_test.py 10.129.151.2 7
```

**Expected Behavior:**
- Message logged: "TEST: Triggering DBE - Bus error (data)"
- System crashes attempting to read from invalid physical address 0xFFFFFFFF

**Expected Crash Dump:**
- `CRASH_FUNC`: `SYS_FUNC`, code = **207** (200 + 7)
- `CRASH_ADDR`: **~0x9D0xxxxx** - address of load instruction in TriggerException() that reads from 0xFFFFFFFF
- `CRASH_DIAG[5]`: Stack pointer (SP)
- `CRASH_DIAG[6]`: Return address (RA)
- Exception code: **7** (EXCEP_DBE)

**addr2line Verification:**
- ✅ CRASH_ADDR should resolve to: `dummy = *invalid_addr;` in TriggerException()
- Command: `addr2line -e build/firmware.elf <CRASH_ADDR>`

---

### Test 5: Syscall - Sys
**Command:**
```bash
python trigger_exception_test.py 10.129.151.2 8
```

**Expected Behavior:**
- Message logged: "TEST: Triggering Sys - Syscall exception"
- System crashes executing `syscall` instruction

**Expected Crash Dump:**
- `CRASH_FUNC`: `SYS_FUNC`, code = **208** (200 + 8)
- `CRASH_ADDR`: **~0x9D0xxxxx** - address of syscall instruction in TriggerException()
- `CRASH_DIAG[5]`: Stack pointer (SP)
- `CRASH_DIAG[6]`: Return address (RA)
- Exception code: **8** (EXCEP_Sys)

**addr2line Verification:**
- ✅ CRASH_ADDR should resolve to: `asm volatile("syscall");` in TriggerException()
- Command: `addr2line -e build/firmware.elf <CRASH_ADDR>`

---

### Test 6: Breakpoint - Bp
**Command:**
```bash
python trigger_exception_test.py 10.129.151.2 9
```

**Expected Behavior:**
- Message logged: "TEST: Triggering Bp - Breakpoint exception"
- System crashes executing `break 0` instruction

**Expected Crash Dump:**
- `CRASH_FUNC`: `SYS_FUNC`, code = **209** (200 + 9)
- `CRASH_ADDR`: **~0x9D0xxxxx** - address of break instruction in TriggerException()
- `CRASH_DIAG[5]`: Stack pointer (SP)
- `CRASH_DIAG[6]`: Return address (RA)
- Exception code: **9** (EXCEP_Bp)

**addr2line Verification:**
- ✅ CRASH_ADDR should resolve to: `asm volatile("break 0");` in TriggerException()
- Command: `addr2line -e build/firmware.elf <CRASH_ADDR>`

---

### Test 7: Reserved Instruction - RI
**Command:**
```bash
python trigger_exception_test.py 10.129.151.2 10
```

**Expected Behavior:**
- Message logged: "TEST: Triggering RI - Reserved instruction"
- System crashes executing invalid instruction word 0xFFFFFFFF

**Expected Crash Dump:**
- `CRASH_FUNC`: `SYS_FUNC`, code = **210** (200 + 10)
- `CRASH_ADDR`: **~0x9D0xxxxx** - address of invalid instruction (0xFFFFFFFF) in TriggerException()
- `CRASH_DIAG[5]`: Stack pointer (SP)
- `CRASH_DIAG[6]`: Return address (RA)
- Exception code: **10** (EXCEP_RI)

**addr2line Verification:**
- ✅ CRASH_ADDR should resolve to: `asm volatile(".word 0xFFFFFFFF");` in TriggerException()
- Command: `addr2line -e build/firmware.elf <CRASH_ADDR>`

---

### Test 8: Arithmetic Overflow - Overflow
**Command:**
```bash
python trigger_exception_test.py 10.129.151.2 12
```

**Expected Behavior:**
- Message logged: "TEST: Triggering Overflow - Arithmetic overflow"
- System crashes on ADD instruction overflow (INT_MAX + 1)

**Expected Crash Dump:**
- `CRASH_FUNC`: `SYS_FUNC`, code = **212** (200 + 12)
- `CRASH_ADDR`: Address of the ADD instruction in inline assembly
- `CRASH_DIAG[5]`: Stack pointer (SP)
- `CRASH_DIAG[6]`: Return address (RA)
- Exception code: **12** (EXCEP_Overflow)

**Note:** May not trigger if overflow exceptions are disabled in CPU status register.

**addr2line Verification:**
- ✅ CRASH_ADDR should resolve to: `asm volatile("add %0, %1, %2" ...)` in TriggerException()
- Command: `addr2line -e build/firmware.elf <CRASH_ADDR>`

---

### Test 9: Trap (Divide by Zero) - Trap
**Command:**
```bash
python trigger_exception_test.py 10.129.151.2 13
```

**Expected Behavior:**
- Message logged: "TEST: Triggering Trap - Divide by zero"
- System crashes on divide by zero

**Expected Crash Dump:**
- `CRASH_FUNC`: `SYS_FUNC`, code = **213** (200 + 13)
- `CRASH_ADDR`: **~0x9D0xxxxx** - address of divide instruction in TriggerException()
- `CRASH_DIAG[5]`: Stack pointer (SP)
- `CRASH_DIAG[6]`: Return address (RA)
- Exception code: **13** (EXCEP_Trap)

**Note:** May not trigger on MIPS if integer division by zero doesn't trap (implementation-specific).

**addr2line Verification:**
- ✅ CRASH_ADDR should resolve to: `dummy = 1 / divisor;` in TriggerException()
- Command: `addr2line -e build/firmware.elf <CRASH_ADDR>`

---

## BadVAddr Investigation Tests (14-17)

### Purpose
Systematically determine how the CPU modifies the BadVAddr register when handling TLB exceptions with unaligned unmapped addresses.

### Test Addresses & Binary Patterns
| Test | Address    | Binary (last byte) | Last 2 bits |
|------|------------|-------------------|-------------|
| 14   | 0xFFFFFFFD | `11111101`       | `01`        |
| 15   | 0xFFFFFFFB | `11111011`       | `11`        |
| 16   | 0x00000001 | `00000001`       | `01`        |
| 17   | 0x00000003 | `00000011`       | `11`        |

### Hypothesis to Test
- **Option A**: CPU clears bit 0 only (LSB) → 0xFFFFFFFD becomes 0xFFFFFFFC, 0xFFFFFFFB becomes 0xFFFFFFFB, etc.
- **Option B**: CPU clears bits 0-1 (word alignment) → All become word-aligned (bottom 2 bits = `00`)
- **Option C**: Something else entirely

### Test 14: BadVAddr Investigation - 0xFFFFFFFD
**Command:**
```bash
python trigger_exception_test.py 10.129.151.2 14
```

**Expected Crash Dump:**
- `CRASH_FUNC`: `SYS_FUNC`, code = **6** (_simple_tlb_refill_exception_handler)
- `CRASH_ADDR`: **0xFFFFFFFD** - EPC captures where CPU tried to fetch
- `CRASH_DIAG[0]`: **0x00000002** - Exception code (TLBL)
- `CRASH_DIAG[1]`: **[TO BE DETERMINED]** - BadVAddr value (key finding)

**Actual Results:**
```
CRASH_FUNC: SYS_FUNC, code 6
CRASH_ADDR: 0xFFFFFFFD
CRASH_DIAG[0]: 0x00000002 (TLBL)
CRASH_DIAG[1]: 0xFFFFFFFC (bit 0 cleared: 0xFFFFFFFD → 0xFFFFFFFC)
CRASH_DIAG[5]: 0x80061DA0 (SP)
CRASH_DIAG[6]: 0x9D105814 (RA)
xcmisc: 114 (100 + test code 14)
```

---

### Test 15: BadVAddr Investigation - 0xFFFFFFFB
**Command:**
```bash
python trigger_exception_test.py 10.129.151.2 15
```

**Expected Crash Dump:**
- `CRASH_FUNC`: `SYS_FUNC`, code = **6** (_simple_tlb_refill_exception_handler)
- `CRASH_ADDR`: **0xFFFFFFFB** - EPC captures where CPU tried to fetch
- `CRASH_DIAG[0]`: **0x00000002** - Exception code (TLBL)
- `CRASH_DIAG[1]`: **[TO BE DETERMINED]** - BadVAddr value (key finding)

**Actual Results:**
```
CRASH_FUNC: SYS_FUNC, code 6
CRASH_ADDR: 0xFFFFFFFB
CRASH_DIAG[0]: 0x00000002 (TLBL)
CRASH_DIAG[1]: 0xFFFFFFFA (bit 0 cleared: 0xFFFFFFFB → 0xFFFFFFFA)
CRASH_DIAG[5]: 0x80061DA0 (SP)
CRASH_DIAG[6]: 0x9D105814 (RA)
xcmisc: 115 (100 + test code 15)
```

---

### Test 16: BadVAddr Investigation - 0x00000001
**Command:**
```bash
python trigger_exception_test.py 10.129.151.2 16
```

**Expected Crash Dump:**
- `CRASH_FUNC`: `SYS_FUNC`, code = **6** (_simple_tlb_refill_exception_handler)
- `CRASH_ADDR`: **0x00000001** - EPC captures where CPU tried to fetch
- `CRASH_DIAG[0]`: **0x00000002** - Exception code (TLBL)
- `CRASH_DIAG[1]`: **[TO BE DETERMINED]** - BadVAddr value (key finding)

**Actual Results:**
```
CRASH_FUNC: SYS_FUNC, code 6
CRASH_ADDR: 0x00000001
CRASH_DIAG[0]: 0x00000002 (TLBL)
CRASH_DIAG[1]: 0x00000000 (bit 0 cleared: 0x00000001 → 0x00000000)
CRASH_DIAG[5]: 0x80061DA0 (SP)
CRASH_DIAG[6]: 0x9D105814 (RA)
xcmisc: 116 (100 + test code 16)
```

---

### Test 17: BadVAddr Investigation - 0x00000003
**Command:**
```bash
python trigger_exception_test.py 10.129.151.2 17
```

**Expected Crash Dump:**
- `CRASH_FUNC`: `SYS_FUNC`, code = **6** (_simple_tlb_refill_exception_handler)
- `CRASH_ADDR`: **0x00000003** - EPC captures where CPU tried to fetch
- `CRASH_DIAG[0]`: **0x00000002** - Exception code (TLBL)
- `CRASH_DIAG[1]`: **[TO BE DETERMINED]** - BadVAddr value (key finding)

**Actual Results:**
```
CRASH_FUNC: SYS_FUNC, code 6
CRASH_ADDR: 0x00000003
CRASH_DIAG[0]: 0x00000002 (TLBL)
CRASH_DIAG[1]: 0x00000002 (bit 0 cleared: 0x00000003 → 0x00000002)
CRASH_DIAG[5]: 0x80061DA0 (SP)
CRASH_DIAG[6]: 0x9D105814 (RA)
xcmisc: 117 (100 + test code 17)
```

---

### BadVAddr Investigation Summary

**Pattern Discovered:**
```
Test  | Address      | Binary (last 2 bits) | BadVAddr     | Binary (last 2 bits) | Operation
------|--------------|----------------------|--------------|----------------------|----------
6     | 0xFFFFFFFF   | 11                   | 0xFFFFFFFE   | 10                   | Cleared bit 0
14    | 0xFFFFFFFD   | 01                   | 0xFFFFFFFC   | 00                   | Cleared bit 0
15    | 0xFFFFFFFB   | 11                   | 0xFFFFFFFA   | 10                   | Cleared bit 0
16    | 0x00000001   | 01                   | 0x00000000   | 00                   | Cleared bit 0
17    | 0x00000003   | 11                   | 0x00000002   | 10                   | Cleared bit 0
```

**Conclusion:**

**EMPIRICALLY VALIDATED:** The PIC32MZ CPU hardware clears **bit 0 (LSB only)** when storing an address to the BadVAddr register during TLB exception handling.

- This is **NOT** full word alignment (which would clear bits 0 and 1 to make bottom 2 bits = `00`)
- This is **NOT** dependent on the original address value
- This appears to be a hardware implementation detail - possibly a 2-byte (halfword) alignment or simply an LSB clearing operation
- The pattern holds consistently across all test addresses (high addresses near 0xFFFFFFFF and low addresses near 0x00000000)

**Practical Implications:**
- When analyzing crash dumps, BadVAddr will ALWAYS be even (bit 0 = 0)
- To determine the actual faulting address, you may need to check CRASH_ADDR (EPC) instead
- For instruction fetch exceptions, EPC contains the actual address that caused the fault
- The CPU's clearing of bit 0 in BadVAddr is a known behavior of this MIPS implementation

---

### Test 10: ISR Stack Overflow
**Command:**
```bash
python trigger_exception_test.py 10.129.151.2 0xF0
```

**Expected Behavior:**
- Message logged: "TEST: ISR stack overflow test requested"
- Deep recursion with large stack frames overflows ISR stack
- May trigger various exceptions depending on what gets corrupted

**Expected Crash Dump:**
- `CRASH_FUNC`: Varies - could be any exception depending on what stack corruption hits
- `CRASH_ADDR`: Likely inside `recursive_isr_overflow()` function
- `CRASH_DIAG[5]`: Stack pointer - should show SP near or past bottom of ISR stack
- `CRASH_DIAG[6]`: Return address - may be corrupted

**Note:** This test may produce different exception types depending on exactly how the stack overflows.

**addr2line Verification:**
- ⚠️ CRASH_ADDR is UNPREDICTABLE - may be:
  - Inside `recursive_isr_overflow()` at various recursion depths (~0x9D0xxxxx)
  - In exception handler code if corruption detected
  - Corrupted/invalid address if stack severely overflowed
- If CRASH_ADDR looks valid (~0x9D0xxxxx), try: `addr2line -e build/firmware.elf <CRASH_ADDR>`

---

### Test 11: Task Stack Overflow
**Command:**
```bash
python trigger_exception_test.py 10.129.151.2 0xF1
```

**Expected Behavior:**
- Message logged: "TEST: Task stack overflow test requested"
- Deep recursion with large stack frames overflows task stack
- Should trigger FreeRTOS stack overflow detection or exception

**Expected Crash Dump:**
- `CRASH_FUNC`: May vary - FreeRTOS stack check or memory exception
- `CRASH_ADDR`: **Variable/unpredictable** - could be:
  - Inside recursive_task_overflow() at various depths (~0x9D0xxxxx)
  - In FreeRTOS context switch code
  - In FreeRTOS stack overflow hook
  - May show corrupted value if stack overflow severe
- `CRASH_DIAG[5]`: Stack pointer - should show SP past task stack boundaries
- `CRASH_DIAG[6]`: Return address - may be corrupted

**Note:** FreeRTOS may catch this before exception handler if stack overflow checking is enabled.

**addr2line Verification:**
- ⚠️ CRASH_ADDR is UNPREDICTABLE - may be:
  - Inside `recursive_task_overflow()` at various recursion depths
  - In FreeRTOS task switching or stack checking code
  - Corrupted/invalid address if stack severely overflowed
- If CRASH_ADDR looks valid (~0x9D0xxxxx), try: `addr2line -e build/firmware.elf <CRASH_ADDR>`

---

## Tests NOT Triggerable

The following exception types cannot be reliably triggered with software, but if they occur in production, here's what to expect:

### EXCEP_IRQ (0) - Interrupt
**Why not triggerable:** This is the normal interrupt processing path, not an exception.

**If encountered in crash dump:**
- `CRASH_FUNC`: **200** (SYS_FUNC, 200 + 0)
- Indicates exception occurred during interrupt processing
- Would suggest ISR corruption or nested exception
- `CRASH_ADDR`: Points to instruction that faulted within ISR
- Extremely unusual - likely indicates serious system corruption

---

### EXCEP_MOD (1) - TLB Modified Exception
**Why not triggerable:** Requires TLB manipulation; PIC32MZ uses fixed memory mapping.

**If encountered in crash dump:**
- `CRASH_FUNC`: **201** (SYS_FUNC, 200 + 1)
- Indicates attempt to write to TLB page marked read-only
- `CRASH_ADDR`: Address of instruction attempting write
- `_bad_virtual_addr`: The memory address that was being written to
- Possible causes: Memory protection violation, corrupted TLB entry

---

### EXCEP_TLBL (2) - TLB Load Exception
**Why not triggerable:** Requires TLB manipulation; PIC32MZ uses fixed memory mapping.

**If encountered in crash dump:**
- `CRASH_FUNC`: **202** (SYS_FUNC, 200 + 2)
- Indicates TLB miss on load (similar to page fault on other architectures)
- `CRASH_ADDR`: Address of load instruction
- `_bad_virtual_addr`: The memory address being read
- Note: Most null pointer dereferences go to TLB refill handler (code 6) instead

---

### EXCEP_TLBS (3) - TLB Store Exception
**Why not triggerable:** Requires TLB manipulation; PIC32MZ uses fixed memory mapping.

**If encountered in crash dump:**
- `CRASH_FUNC`: **203** (SYS_FUNC, 200 + 3)
- Indicates TLB miss on store (similar to page fault on write)
- `CRASH_ADDR`: Address of store instruction
- `_bad_virtual_addr`: The memory address being written
- Note: Most null pointer writes go to TLB refill handler (code 6) instead

---

### EXCEP_CpU (11) - Coprocessor Unusable
**Why not triggerable:** FPU (Coprocessor 1) is enabled; hard to disable at runtime.

**If encountered in crash dump:**
- `CRASH_FUNC`: **211** (SYS_FUNC, 200 + 11)
- Indicates attempt to use coprocessor that's not enabled
- `CRASH_ADDR`: Address of coprocessor instruction (likely FPU operation)
- Possible causes:
  - FPU disabled in status register (unusual)
  - Coprocessor 2 usage (not available on PIC32MZ)
  - Corrupted CPU status register

---

### EXCEP_FPU (15) - Floating Point Exception
**Why not triggerable:** FPU exceptions (invalid operation, divide by zero, overflow, underflow) are typically masked/disabled.

**If encountered in crash dump:**
- `CRASH_FUNC`: **215** (SYS_FUNC, 200 + 15)
- Indicates FPU detected exceptional condition:
  - Invalid operation (NaN operand, invalid conversion)
  - Division by zero
  - Overflow
  - Underflow
  - Inexact result
- `CRASH_ADDR`: Address of floating point instruction that faulted
- Requires FPU exception enable bits to be set in FCSR register
- Very rare in embedded systems (exceptions usually masked, producing NaN/Inf instead)

**To enable (for testing):**
```c
// Would need to modify FCSR (FPU Control Status Register) enable bits
// Not recommended for production code
```

---

### EXCEP_IS1 (16) - Implementation Specific 1
**Why not triggerable:** Implementation-specific, not documented for PIC32MZ.

**If encountered in crash dump:**
- `CRASH_FUNC`: **216** (SYS_FUNC, 200 + 16)
- Consult PIC32MZ errata and family reference manual
- May indicate undocumented CPU behavior or silicon bug
- Very rare

---

### EXCEP_CEU (17) - CorExtend Unusable
**Why not triggerable:** CorExtend not available on PIC32MZ.

**If encountered in crash dump:**
- `CRASH_FUNC`: **217** (SYS_FUNC, 200 + 17)
- Should never occur on PIC32MZ (no CorExtend support)
- If seen, indicates serious CPU corruption or invalid instruction

---

### EXCEP_C2E (18) - Coprocessor 2 Exception
**Why not triggerable:** Coprocessor 2 not available on PIC32MZ.

**If encountered in crash dump:**
- `CRASH_FUNC`: **218** (SYS_FUNC, 200 + 18)
- Should never occur on PIC32MZ (no CP2 support)
- Possible causes:
  - Corrupted instruction stream
  - Executing from invalid memory region

---

### EXCEP_TLBRI (19) - TLB Read Inhibit
**Why not triggerable:** Requires TLB configuration with read-inhibit pages.

**If encountered in crash dump:**
- `CRASH_FUNC`: **219** (SYS_FUNC, 200 + 19)
- Indicates attempt to read from memory marked no-read
- `CRASH_ADDR`: Address of load instruction
- `_bad_virtual_addr`: Memory address with read-inhibit
- Would require special TLB configuration (not typical for PIC32MZ)

---

### EXCEP_TLBEI (20) - TLB Execute Inhibit
**Why not triggerable:** Requires TLB configuration with execute-inhibit pages.

**If encountered in crash dump:**
- `CRASH_FUNC`: **220** (SYS_FUNC, 200 + 20)
- Indicates attempt to execute code from memory marked no-execute
- `CRASH_ADDR`: The address where execution was attempted (the NX page)
- Useful security feature (DEP - Data Execution Prevention)
- If enabled, would catch stack buffer overflow exploits
- Would require special TLB configuration

**Possible causes:**
- Executing from stack or heap (if NX enabled)
- Corrupted function pointer
- Buffer overflow jumping to data region

---

### EXCEP_WATCH (23) - Watchpoint
**Why not triggerable:** Requires hardware watchpoint configuration via debug registers.

**If encountered in crash dump:**
- `CRASH_FUNC`: **223** (SYS_FUNC, 200 + 23)
- Indicates hardware watchpoint hit
- Configured via CP0 WatchLo/WatchHi registers
- `CRASH_ADDR`: Instruction that triggered watchpoint
- Can watch for:
  - Specific address reads
  - Specific address writes
  - Specific instruction fetches
- Typically only used during active debugging with JTAG/debugger

---

### EXCEP_MCHECK (24) - Machine Check
**Why not triggerable:** Hardware error detection; cannot simulate in software.

**If encountered in crash dump:**
- `CRASH_FUNC`: **224** (SYS_FUNC, 200 + 24)
- Indicates serious hardware error detected by CPU:
  - Bus error
  - Parity error
  - Cache error (may also trigger cache error handler instead)
  - Memory controller error
- `CRASH_ADDR`: Instruction being executed when error detected
- **CRITICAL:** May indicate hardware failure, bad RAM, or signal integrity issues
- Check hardware: power supply stability, temperature, signal integrity
- Review DERRADDR (Data Error Address) and IERRADDR (Instruction Error Address) if available

---

### EXCEP_DSPDIS (26) - DSP Disabled
**Why not triggerable:** DSP ASE not available/configured on PIC32MZ.

**If encountered in crash dump:**
- `CRASH_FUNC`: **226** (SYS_FUNC, 200 + 26)
- Indicates attempt to use DSP instructions when DSP disabled
- `CRASH_ADDR`: Address of DSP instruction
- Should not occur on PIC32MZ unless:
  - Executing corrupted instruction stream
  - Running code compiled for different MIPS variant

---

## Validation Checklist

For each test, verify:

- [ ] Log message appears before crash
- [ ] 100ms delay allows message to be logged
- [ ] Device crashes (stops responding)
- [ ] Crash dump is retrievable
- [ ] `CRASH_FUNC` code matches expected value (200 + exception_code)
- [ ] `CRASH_ADDR` points to reasonable address (inside program memory)
- [ ] `CRASH_DIAG[5]` (SP) is within valid stack range
- [ ] `CRASH_DIAG[6]` (RA) points to valid code address
- [ ] Exception code in dump matches test number
- [ ] Device recovers after power cycle
- [ ] Bootloader remains intact (can reflash)

---

## Special Case: TLB Refill Handler

Some exceptions (particularly null pointer dereferences) may trigger `_simple_tlb_refill_exception_handler` instead of `_general_exception_handler`.

**Note:** Test 12 (0xF2) explicitly tests the TLB refill handler.

**Expected Crash Dump (TLB handler):**
- `CRASH_FUNC`: `SYS_FUNC`, code = **6** (not 200+code)
- `CRASH_ADDR`: Program counter at exception
- `CRASH_DIAG[0]`: Exception code from Cause register
- `CRASH_DIAG[1]`: BadVAddr - the virtual address that caused the exception
- `CRASH_DIAG[5]`: Stack pointer (SP)
- `CRASH_DIAG[6]`: Return address (RA)

---

### Test 12: TLB Refill Exception (0xF2)

**Command:**
```bash
python trigger_exception_test.py <device_ip> 0xF2
```

**Expected Behavior:**
- Log message: "TEST: TLB refill exception - null pointer dereference"
- Device crashes due to null pointer (0x00000000) dereference
- Triggers `_simple_tlb_refill_exception_handler` (not general handler)

**Expected Crash Dump Values:**
- **CRASH_FUNC:** **6** (SYS_FUNC, TLB refill handler)
  - ⚠️ Note: This is 6, not 206 - TLB handler uses different numbering scheme
- **CRASH_ADDR:** **~0x9D0xxxxx** - address of store instruction in TestTlbRefill() that writes to null pointer
- **CRASH_DIAG[0]:** Exception code from CAUSE register (likely 2 or 3 for TLB load/store)
- **CRASH_DIAG[1]:** Bad virtual address = 0x00000000 (the null pointer)
- **CRASH_DIAG[5]:** SP (stack pointer) at exception time
- **CRASH_DIAG[6]:** RA (return address) at exception time

**Special Notes:**
- This explicitly tests the separate TLB refill exception vector
- Confirms that SP/RA capture works correctly in TLB handler
- CRASH_DIAG[1] provides the faulting address (0x00000000)
- Different crash code from general exceptions (6 vs 200+code)

**addr2line Verification:**
- ✅ CRASH_ADDR should resolve to: `*null_ptr = 0xDEADBEEF;` in TestTlbRefill()
- Command: `addr2line -e build/firmware.elf <CRASH_ADDR>`
- Expected output: `c:/Users/.../utils.c:<line_number>`

---

### Test ID 18: Unaligned Data Read from Flash ✅ COMPLETED

**Command:**
```bash
python trigger_exception_test.py <device_ip> 18
```

**Test Purpose:**
- Tests whether hardware supports unaligned data access in Flash memory (0x9D region)
- Reads 32-bit value from address 0x9D000001 (flash start + 1, mapped but misaligned)

**ACTUAL RESULTS (2026-02-18):**
- ✅ **CRASH CONFIRMED** - AdEL exception triggered
- **CRASH_FUNC:** **204** (SYS_FUNC, 200 + 4 = AdEL)
- **CRASH_ADDR:** 0x9D0E617C (load instruction in TriggerException case 18)
- **CRASH_DIAG[5]:** 0x80061D98 (SP)
- **CRASH_DIAG[6]:** 0x9D105844 (RA)
- **Breadcrumb:** xcmisc 118 → system 100 → system 204
- **File:** testScriptOutput/DataAccess_Tests/X260218T.009

**CRITICAL FINDING:**
**PIC32MZ does NOT support unaligned memory access in Flash (0x9D region)**
- Unaligned data read from flash triggers AdEL (Address Error - Load) immediately
- This is REGION-SPECIFIC behavior (see Test IDs 20-21 for RAM comparison)

**Analysis Implications:**
- AdEL/AdES exceptions WILL occur in real crashes for unaligned flash access
- Automated analysis must handle AdEL/AdES comprehensively
- Must check memory region (flash vs RAM) when analyzing AdEL exceptions
- Flash region: 0x9D000000 - 0x9DFFFFFF (KSEG0 cached)
- Flash region: 0xBD000000 - 0xBDFFFFFF (KSEG1 uncached)

---

### Test ID 19: Data Read from Unmapped Address ✅ COMPLETED

**Command:**
```bash
python trigger_exception_test.py <device_ip> 19
```

**Test Purpose:**
- Tests TLB Refill exception with data access (not instruction fetch)
- Reads from unmapped address 0xFFFF0000
- Validates BadVAddr vs EPC pattern for distinguishing data access from instruction fetch

**ACTUAL RESULTS (2026-02-18):**
- ✅ **CRASH CONFIRMED** - TLB Refill exception triggered
- **CRASH_FUNC:** **6** (SYS_FUNC, TLB refill handler)
- **CRASH_ADDR:** 0x9D0E6194 (load instruction in TriggerException case 19)
- **CRASH_DIAG[0]:** 0x00000002 (TLBL - TLB load exception)
- **CRASH_DIAG[1]:** 0xFFFF0000 (BadVAddr - the unmapped address)
- **CRASH_DIAG[5]:** 0x80061D98 (SP)
- **CRASH_DIAG[6]:** 0x9D105844 (RA)
- **Breadcrumb:** xcmisc 119 → system 100 → system 6
- **File:** testScriptOutput/DataAccess_Tests/X260218T.010

**Pattern Validation:**
- ✅ BadVAddr (0xFFFF0000) ≠ EPC (CRASH_ADDR = 0x9D0E6194)
- ✅ This confirms data access pattern (load from unmapped address)
- ✅ Distinguishes from instruction fetch where BadVAddr ≈ EPC

**Analysis Implications:**
- Automated analysis can use BadVAddr ≠ EPC to identify data access faults
- When BadVAddr ≠ EPC and both unmapped: likely null/bad pointer dereference
- CRASH_DIAG[0] confirms load vs store (2=TLBL, 3=TLBS)

---

### Test ID 20: Unaligned Data Read from RAM - Manual Cast ✅ COMPLETED

**Command:**
```bash
python trigger_exception_test.py <device_ip> 20
```

**Test Purpose:**
- Tests unaligned data access in RAM memory (0x80 region)
- Uses manual pointer cast to bypass compiler optimizations
- Compares RAM behavior vs flash (Test ID 18)

**ACTUAL RESULTS (2026-02-18):**
- ✅ **NO CRASH** - Test completed successfully
- **Message:** "TEST 20: Exception test completed without crash"
- **Breadcrumb:** xcmisc 120 (100 + 20)
- **File:** testScriptOutput/DataAccess_Tests/XCEVLOG (4).txt
- **Ran 3 times:** All successful

**CRITICAL FINDING:**
**PIC32MZ DOES support unaligned memory access in RAM (0x80 region)**
- Same unaligned access that crashes in flash works fine in RAM
- This is REGION-SPECIFIC hardware behavior
- RAM memory controller handles unaligned access transparently

**Analysis Implications:**
- AdEL exceptions in RAM are UNLIKELY (hardware supports it)
- AdEL exceptions in Flash are LIKELY (hardware does NOT support it)
- When analyzing AdEL, check CRASH_ADDR memory region:
  - Flash (0x9D/0xBD): Expected for unaligned access
  - RAM (0x80/0xA0): Unexpected, indicates different problem

---

### Test ID 21: Unaligned Data Read from RAM - Compiler-Aware ✅ COMPLETED

**Command:**
```bash
python trigger_exception_test.py <device_ip> 21
```

**Test Purpose:**
- Tests compiler handling of packed struct unaligned fields
- Normal field access where compiler knows about `__attribute__((packed))`
- Validates whether compiler generates safe byte-by-byte access

**ACTUAL RESULTS (2026-02-18):**
- ✅ **NO CRASH** - Test completed successfully  
- **Message:** "TEST 21: Exception test completed without crash"
- **Breadcrumb:** xcmisc 121 (100 + 21)
- **File:** testScriptOutput/DataAccess_Tests/XCEVLOG (4).txt
- **Ran 3 times:** All successful

**FINDING:**
**Packed structure fields work safely in RAM**
- Test ID 20 proves hardware supports unaligned RAM access
- Test ID 21 confirms packed structs work regardless of compiler optimization
- Both manual cast AND normal field access succeed

**Analysis Implications:**
- Packed structures used throughout codebase (export.h) are SAFE
- They're allocated in RAM where unaligned access is supported
- No special compiler handling required (though compiler may optimize anyway)
- AdEL from packed struct access would only occur if struct in flash

---

### Tests 18-21 Summary: Memory Region Behavior

| Test | Memory | Access Type | Address | Result | Exception |
|------|--------|-------------|---------|--------|-----------|
| 18 | Flash (0x9D) | Unaligned int read | 0x9D000001 | ❌ CRASH | AdEL (204) |
| 19 | Unmapped | Data read | 0xFFFF0000 | ❌ CRASH | TLB Refill (6) |
| 20 | RAM (0x80) | Unaligned int read (cast) | 0x80xxxxxx+1 | ✅ NO CRASH | None |
| 21 | RAM (0x80) | Unaligned int read (packed) | 0x80xxxxxx+1 | ✅ NO CRASH | None |

**Conclusion:** Unaligned memory access support is **REGION-SPECIFIC** on PIC32MZ:
- ✅ **RAM (0x80, 0xA0):** Transparent unaligned access support
- ❌ **Flash (0x9D, 0xBD):** NO unaligned access support - triggers AdEL/AdES

---

## Tests 27-32: AdEL and IBE Exception Investigation

**Implementation status:** Tests 27-32 are implemented and routable in firmware; empirical run results are still pending.

### Test ID 28: Unaligned Instruction Fetch from Flash 🔄 PENDING

**Objective:** Determine if instruction fetch from odd address triggers AdEL

**Command:**
```bash
python trigger_exception_test.py <device_ip> 28
```

**Test Code:**
```c
case 28:  // Test unaligned instruction fetch from flash (jump to odd address)
    void (*odd_func_ptr)(void) = (void (*)(void))(((unsigned long)&TriggerException) | 0x1);
    odd_func_ptr();  // Jump to odd address
```

**Expected Behavior:**
- Jump to odd address in flash (function address | 0x1)
- CPU attempts instruction fetch from unaligned address
- Unaligned instruction fetch should trigger AdEL

**Expected Crash Dump Values:**
- **CRASH_FUNC:** **204** (AdEL - Address Error (Load))
- **CRASH_ADDR:** Odd address in flash (BadVAddr ≈ EPC, distinguishes from data access)
- **Breadcrumb:** xcmisc 128

**Analysis Focus:**
- Confirms instruction fetch always requires alignment (even if data access doesn't)
- BadVAddr should equal (or be very close to) EPC
- Compare with Test ID 19 where BadVAddr ≠ EPC (data access)

---

### Test ID 29: Unaligned Instruction Fetch from RAM 🔄 PENDING

**Objective:** Determine if RAM supports unaligned instruction fetch (vs data access)

**Command:**
```bash
python trigger_exception_test.py <device_ip> 29
```

**Test Code:**
```c
case 29:  // Test unaligned instruction fetch from RAM
    static unsigned long ram_code[2] = {
        0x03e00008,  // jr $ra (MIPS return instruction)
        0x00000000   // nop (delay slot)
    };
    void (*odd_ram_func)(void) = (void (*)(void))(((unsigned long)ram_code) | 0x1);
    odd_ram_func();  // Jump to odd address in RAM
```

**Expected Behavior:**
- Jump to odd address in RAM containing valid MIPS code
- CPU attempts instruction fetch from unaligned RAM address
- **Likely:** AdEL (instruction fetch probably requires alignment even in RAM)
- **Alternative:** May work if RAM supports unaligned instruction fetch

**Expected Crash Dump Values:**
- **Most Likely:** CRASH_FUNC = 204 (AdEL)
- **Alternative:** NO CRASH (would be surprising but informative)
- **Breadcrumb:** xcmisc 129

**Analysis Focus:**
- Compare instruction fetch vs data access alignment requirements
- Tests 20-21 showed RAM supports unaligned *data* access
- This tests unaligned *instruction* fetch from RAM

---

### Test ID 30: Unaligned Data Write to Flash - AdES 🔄 PENDING

**Objective:** Trigger AdES (Address Error - Store) with unaligned write

**Command:**
```bash
python trigger_exception_test.py <device_ip> 30
```

**Test Code:**
```c
case 30:  // Test unaligned data write to flash (AdES test)
    volatile int *misaligned_ptr = (volatile int *)0x9D000001;  // Flash + 1
    *misaligned_ptr = 0xDEADBEEF;  // Attempt write
```

**Expected Behavior:**
- Attempt to write 32-bit value to unaligned flash address
- Flash doesn't support unaligned access (established by Test ID 18)
- Should trigger AdES (Store variant, like Test ID 18 triggered AdEL for load)

**Expected Crash Dump Values:**
- **CRASH_FUNC:** **205** (AdES - Address Error (Store))
- **CRASH_ADDR:** 0x9D000001 or nearby (BadVAddr showing misaligned store target)
- **Breadcrumb:** xcmisc 130

**Analysis Focus:**
- First empirical test of AdES (all previous were AdEL)
- Confirms flash doesn't support unaligned writes (matching read behavior)
- Validates store vs load exception codes

---

### Test ID 31: Instruction Fetch from Peripheral Region - IBE 🔄 PENDING

**Objective:** Attempt to trigger IBE (Instruction Bus Error) by jumping to peripheral

**Command:**
```bash
python trigger_exception_test.py <device_ip> 31
```

**Test Code:**
```c
case 31:  // Test instruction fetch from peripheral/MMIO region
    void (*periph_func)(void) = (void (*)(void))0xBF800000;  // Peripheral base
    periph_func();  // Jump to peripheral region
```

**Expected Behavior:**
- Jump to peripheral/SFR region (aligned address)
- Peripheral region is mapped but not executable
- May trigger IBE if bus responds with error
- **Alternative:** Could trigger different exception depending on memory map

**Expected Crash Dump Values:**
- **Target:** CRASH_FUNC = 206 (IBE - Instruction Bus Error)
- **Alternative:** CRASH_FUNC = 6 (TLB) if peripheral not in TLB
- **Alternative:** May execute garbage and crash differently
- **Breadcrumb:** xcmisc 131

**Analysis Focus:**
- IBE requires: aligned + mapped + physically invalid
- Peripheral access might generate bus error
- May help distinguish IBE vs TLB vs AdEL

---

### Test ID 32: Instruction Fetch from End of Flash 🔄 PENDING

**Objective:** Test boundary condition at end of flash region

**Command:**
```bash
python trigger_exception_test.py <device_ip> 32
```

**Current Routing Note:**
- `TriggerException(32)` is reachable via `GCS_CMD_EXCEPTION_TEST` datagram command.

**Test Code:**
```c
case 32:  // Test instruction fetch from end of flash region
    void (*end_flash_func)(void) = (void (*)(void))0x9D1FFFFC;  // Near end of 2MB flash
    end_flash_func();
```

**Expected Behavior:**
- Jump to last valid address of flash region (or slightly beyond)
- If beyond physical flash: may trigger IBE (aligned, mapped, but invalid)
- If within flash but no valid code: will execute garbage

**Expected Crash Dump Values:**
- **If beyond physical flash:** CRASH_FUNC = 206 (IBE)
- **If within flash:** Likely garbage execution, unpredictable crash
- **Breadcrumb:** xcmisc 132

**Analysis Focus:**
- Tests flash boundary behavior
- May reveal IBE vs TLB precedence at region boundaries
- Helps understand memory mapping limits

---

### Test ID 27: Instruction Fetch from Uncached Flash 🔄 PENDING

**Objective:** Compare cached (KSEG0) vs uncached (KSEG1) flash access

**Command:**
```bash
python trigger_exception_test.py <device_ip> 27
```

**Test Code:**
```c
case 27:  // Test instruction fetch from uncached flash region
    void (*uncached_func)(void) = (void (*)(void))0xBD000000;  // KSEG1 flash start
    uncached_func();
```

**Expected Behavior:**
- Jump to flash via KSEG1 (uncached) vs normal KSEG0 (cached)
- Should work normally if same physical flash is valid
- Tests if caching affects exception behavior

**Expected Crash Dump Values:**
- **Likely:** NO CRASH if valid code at flash start
- **Alternative:** Different exception behavior if caching affects memory controller
- **Breadcrumb:** xcmisc 127

**Analysis Focus:**
- Validates cached vs uncached doesn't affect exception precedence
- Confirms KSEG0 vs KSEG1 both access same physical flash
- Baseline test before analyzing real crashes

---

## Test Summary: Tests 27-32 Focus Areas

| Test | Focus | Address | Expected Exception | Analysis Goal |
|------|-------|---------|-------------------|---------------|
| 27 | Uncached flash | 0xBD000000 | None? | Baseline cached vs uncached behavior |
| 28 | Instruction fetch alignment (flash) | 0x9Dxxxxxx+1 | AdEL (204) | Confirm instruction fetch requires alignment |
| 29 | Instruction fetch alignment (RAM) | 0x80xxxxxx+1 | AdEL (204)? | Compare RAM instruction vs data alignment |
| 30 | Unaligned write (flash) | 0x9D000001 | AdES (205) | First AdES test, confirm write behaves like read |
| 31 | Peripheral execution | 0xBF800000 | IBE (206)? | Attempt to trigger IBE from MMIO region |
| 32 | Flash boundary | 0x9D1FFFFC | IBE (206)? | Test physical memory limits |

**Primary Goals:**
1. **AdEL/AdES Understanding:** Distinguish instruction fetch vs data access alignment requirements (Test IDs 28-30)
2. **IBE Triggering:** Empirically discover how to trigger CRASH_FUNC=206 (Test IDs 31-32)
3. **Baseline Behavior:** Establish normal uncached access for comparison (Test ID 27)

---

## Success Criteria

**Test suite passes if:**
1. All testable exceptions trigger device crashes
2. Crash dumps contain expected `CRASH_FUNC` codes (including TLB test = 6)
3. Stack pointer and return address values are reasonable
4. Exception codes match test numbers (for general exceptions)
5. Device always recovers after power cycle
6. Bootloader remains functional throughout all tests
7. Hardware unaligned access behavior validated (Test ID 18)
8. Data vs instruction fetch distinction validated (Test ID 19)

**Known acceptable variations:**
- Overflow test may not trap (CPU-dependent)
- Divide by zero may not trap on some MIPS implementations
- Stack overflow tests may produce varying exception types
- Test ID 18 is expected to crash on PIC32MZ (AdEL 204), because unaligned flash access is not supported

---

## Test Execution Log Template

```
Test #  | Code | Exception       | Command                         | Result | CRASH_FUNC | Notes
--------|------|-----------------|----------------------------------|--------|------------|-------
1       | 4    | AdEL            | trigger_exception_test.py IP 4   | PASS   | 204        |
2       | 5    | AdES            | trigger_exception_test.py IP 5   | PASS   | 205        |
3       | 6    | TLB Refill      | trigger_exception_test.py IP 6   | PASS   | 6          | Was IBE intent
4       | 7    | DBE             | trigger_exception_test.py IP 7   | PASS   | 207        |
5       | 8    | Sys             | trigger_exception_test.py IP 8   | PASS   | 208        |
6       | 9    | Bp              | trigger_exception_test.py IP 9   | PASS   | 209        |
7       | 10   | RI              | trigger_exception_test.py IP 10  | PASS   | 210        |
8       | 12   | Overflow        | trigger_exception_test.py IP 12  | ?      | 212        | May not trap
9       | 13   | Trap            | trigger_exception_test.py IP 13  | ?      | 213        | May not trap
10      | 0xF0 | ISR Stack       | trigger_exception_test.py IP 0xF0| PASS   | Varies     |
11      | 0xF1 | Task Stack      | trigger_exception_test.py IP 0xF1| PASS   | Varies     |
12      | 0xF2 | TLB Refill      | trigger_exception_test.py IP 0xF2| PASS   | 6          | Null write
13      | 18   | Unaligned HW    | trigger_exception_test.py IP 18  | ?      | None/204   | HW validation
14      | 19   | Data Read       | trigger_exception_test.py IP 19  | PASS   | 6          | BadVAddr pattern
```

Replace `IP` with actual device IP address (e.g., `10.129.151.2`).

---

## Troubleshooting

**No crash occurs:**
- Check `BUILD_EXCEPTION_TESTS = 1` is defined
- Verify firmware was rebuilt and reflashed
- Check exception test code is uncommented

**Wrong CRASH_FUNC code:**
- Verify exception is being caught by correct handler
- Check if TLB refill handler is being used instead (code = 6)

**Device won't recover:**
- Power cycle device
- Bootloader should always work
- Reflash firmware if necessary

**Messages not logged:**
- Increase delay from 100ms to 500ms
- Check logging infrastructure is working

---

## Post-Test Analysis

After completing all tests, analyze patterns:

1. Which exceptions consistently trigger correctly?
2. Which produce unexpected exception codes?
3. Are SP/RA values always reasonable?
4. Do certain tests corrupt memory differently?
5. Can crash dumps be reliably retrieved?

This data validates that the exception handling infrastructure correctly captures diagnostic information for post-mortem debugging of real crashes.
