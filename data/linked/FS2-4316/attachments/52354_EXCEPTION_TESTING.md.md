# EXCEPTION_TESTING.md

Attachment 52354, text, 7 KB, added 2026-04-02 by Scott Hunter.

# Exception Handler Testing Guide

## Overview
This document describes how to test the exception handlers in the xcomm application to verify proper exception capture and crash logging.

## Building with Exception Tests

To enable exception testing, define `BUILD_EXCEPTION_TESTS` in your build configuration:

```c
// In Build.h or as a compiler flag:
#define BUILD_EXCEPTION_TESTS
```

## Available Test Functions

### 1. `TriggerException(uint8_t exception_code)`
Triggers a specific exception type based on the exception code (0-31).

### 2. `TestStackOverflow_ISR()`
Tests ISR stack overflow detection by causing deep recursion.

### 3. `TestStackOverflow_Task()`
Tests FreeRTOS task stack overflow detection.

### 4. `TestAllExceptions()`
Helper function with examples of all tests (uncomment one at a time).

## Exception Types Testable

| Code | Name | Description | Triggerable |
|------|------|-------------|-------------|
| 0 | EXCEP_IRQ | Interrupt | No (automatic) |
| 1 | EXCEP_MOD | TLB modified | Complex |
| 2 | EXCEP_TLBL | TLB load error | Complex |
| 3 | EXCEP_TLBS | TLB store error | Complex |
| **4** | **EXCEP_AdEL** | **Address error (load)** | **Yes** |
| **5** | **EXCEP_AdES** | **Address error (store)** | **Yes** |
| **6** | **EXCEP_IBE** | **Bus error (ifetch)** | **Yes** |
| **7** | **EXCEP_DBE** | **Bus error (data)** | **Yes** |
| **8** | **EXCEP_Sys** | **Syscall** | **Yes** |
| **9** | **EXCEP_Bp** | **Breakpoint** | **Yes** |
| **10** | **EXCEP_RI** | **Reserved instruction** | **Yes** |
| 11 | EXCEP_CpU | Coprocessor unusable | Complex |
| **12** | **EXCEP_Overflow** | **Arithmetic overflow** | **Yes** |
| **13** | **EXCEP_Trap** | **Trap (divide by zero)** | **Yes** |
| 14 | - | Reserved | No |
| 15 | EXCEP_FPU | FPU exception | Conditional |
| 16-31 | Various | Implementation specific | Varies |

## Usage Example

```c
#ifdef BUILD_EXCEPTION_TESTS

// Test address error on load (misaligned access)
void MyTestTask(void *params)
{
    vTaskDelay(pdMS_TO_TICKS(5000));  // Wait for system to stabilize
    
    AddMessage("About to trigger EXCEP_AdEL test...");
    TriggerException(EXCEP_AdEL);
    
    // System will crash here - examine crash data:
    // - _excep_code should be 4
    // - _excep_addr should point to the faulting instruction
    // - CRASH_FUNC should show (SYS_FUNC, 204) -> 200 + exception code
    // - diag[5] = SP, diag[6] = RA
}

#endif
```

## Testing Procedure

### For Each Exception Type:

1. **Build with tests enabled**
   - Define `BUILD_EXCEPTION_TESTS`
   - Build and program the device

2. **Trigger ONE exception**
   - Call `TriggerException(code)` from a task or test function
   - The system will crash (this is expected!)

3. **Verify crash data capture**
   - Check that crash dump was written
   - Verify `_excep_code` matches expected value
   - Verify `_excep_addr` points to faulting instruction
   - Verify `CRASH_FUNC` shows `(SYS_FUNC, 200+exception_code)`
   - Verify Stack Pointer (SP) in diag[5]
   - Verify Return Address (RA) in diag[6]
   - Verify `_bad_virtual_addr` for address exceptions

4. **Reset and test next exception**

### Stack Overflow Testing:

1. **ISR Stack Overflow**
   ```c
   TestStackOverflow_ISR();
   ```
   - Should eventually corrupt ISR stack
   - Check `IsrStackCheck()` before crash
   - Verify crash detection

2. **Task Stack Overflow**
   ```c
   TestStackOverflow_Task();
   ```
   - Should trigger FreeRTOS stack overflow hook
   - Verify `vApplicationStackOverflowHook()` is called
   - Check task stack watermark before overflow

## Expected Crash Data for General Exceptions

When `_general_exception_handler()` catches an exception:

```c
_excep_code = 0-31           // Exception type
_excep_addr = 0xXXXXXXXX     // PC where exception occurred
_excep_addr_nested = ...     // Nested EPC
_bad_virtual_addr = ...      // Bad address for AdEL/AdES
_cause_str_short = "..."     // Human-readable name
CRASH_FUNC = (SYS_FUNC, 200+exception_code)
CRASH_ADDR = _excep_addr
diag[5] = Stack Pointer (SP)
diag[6] = Return Address (RA)
```

## Expected Crash Data for TLB Refill

When `_simple_tlb_refill_exception_handler()` catches an exception:

```c
CRASH_FUNC = (SYS_FUNC, 6)
CRASH_ADDR = _excep_addr
CRASH_DIAG0 = _excep_code
CRASH_DIAG1 = _bad_virtual_addr
diag[5] = Stack Pointer (SP)
diag[6] = Return Address (RA)
```

## Expected Crash Data for Other Handlers

- **NMI**: `CRASH_FUNC = (SYS_FUNC, 5)`
- **Cache Error**: `CRASH_FUNC = (SYS_FUNC, 7)`

## Safety Notes

⚠️ **WARNING**: These tests will intentionally crash your system!

- Run in a controlled test environment only
- One test at a time
- Have a debugger attached to examine crash state
- Set breakpoint in `infinite_loop()` at line 1360 in utils.c
- Use `exit_exception_handler = true` in debugger to return from exception

## Debugging Tips

1. **Set breakpoints** in exception handlers before testing
2. **Examine variables** while stopped in `infinite_loop()`:
   - `_excep_code`
   - `_excep_addr`
   - `_bad_virtual_addr`
   - `_cause_str_short`

3. **Disassemble** the faulting address (`_excep_addr`) to see what instruction caused the exception

4. **Check crash log** after reset to verify data was persisted

## Example Test Sequence

```c
// Week 1: Test address exceptions
TriggerException(EXCEP_AdEL);   // Day 1
TriggerException(EXCEP_AdES);   // Day 2

// Week 2: Test bus errors  
TriggerException(EXCEP_IBE);    // Day 1
TriggerException(EXCEP_DBE);    // Day 2

// Week 3: Test instruction exceptions
TriggerException(EXCEP_Sys);    // Day 1
TriggerException(EXCEP_Bp);     // Day 2
TriggerException(EXCEP_RI);     // Day 3

// Week 4: Test arithmetic exceptions
TriggerException(EXCEP_Overflow); // Day 1
TriggerException(EXCEP_Trap);     // Day 2

// Week 5: Test stack overflows
TestStackOverflow_ISR();          // Day 1
TestStackOverflow_Task();         // Day 2
```

## Verification Checklist

For each exception test:

- [ ] Exception code captured correctly
- [ ] Exception address points to faulting instruction
- [ ] Stack pointer captured in diag[5]
- [ ] Return address captured in diag[6]
- [ ] Bad virtual address captured (for address errors)
- [ ] Cause string matches exception type
- [ ] Crash data persisted to flash/log
- [ ] Crash data survives reset
- [ ] Debug output shows correct function name
- [ ] System enters infinite loop as expected
- [ ] Debugger can examine all crash variables

## Reference Documentation

- PIC32MZ Reference Manual Section 50 (CPU): 
  https://ww1.microchip.com/downloads/en/DeviceDoc/60001192B.pdf
  
- PIC32MZ Datasheet Table 7-1 (Exception Codes):
  https://ww1.microchip.com/downloads/aemDocuments/documents/MCU32/ProductDocuments/DataSheets/PIC32MZ-Embedded-Connectivity-with-Floating-Point-Unit-Family-Data-Sheet-DS60001320H.pdf

- MPLAB XC32 Compiler User's Guide:
  https://ww1.microchip.com/downloads/aemDocuments/documents/DEV/ProductDocuments/UserGuides/MPLAB-XC32-Compiler-UG-PIC32M-DS-50002799.pdf
