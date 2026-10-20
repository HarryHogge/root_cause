# FS2-603: Trace support

- **Issue type:** Epic
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2023-07-26
- **Updated:** 2024-02-29
- **Resolved:** 2024-02-29
- **Reporter:** Former user
- **Assignee:** Former user
- **Creator:** Former user
- **Components:** WDT Investigation
- **Fix versions:** Release 6.3.4
- **Links:** blocks VXEP-9 ((Duplicate) TPTR-74 VXE 510 Watchdog Software Fault); blocks VXEP-41 (TPTR-74 VXE 510: (VTOL AP WD) Consolidated Watch Dog tracking); blocks VXEP-11 (TPTR-5 VXE 407: (VTOL-AP-WD) Unexpected Behavior Seen During Vertical Landing); relates to FS2-1012 (Rework Trace interface to #ifdef'd code prior to merge into main)
- **Sprint:** FS2 Sprint 4, FS2 Sprint 5

## Description

NOTE: Consider closing Epic and moving bug into the Embedded SW Robustness initiative. 
FreeRTOS provides a fine-grained trace feature that allows logging mutex, queue, and task activity at high rates.
This feature may be useful for debugging priority inversion, deadlock, and livelock.
Custom hook version:
https://www.freertos.org/rtos-trace-macros.html
Paid Version:
https://www.freertos.org/FreeRTOS-Plus/FreeRTOS_Plus_Trace/FreeRTOS_Plus_Trace.html 
https://percepio.com/tracealyzer/licensing/

## Comments (1)

### Scott Whitney, 2024-02-07

Marking this as Done. Remaining work from https://jenaero.atlassian.net/browse/FS2-1286 is being superseded by work done on https://jenaero.atlassian.net/browse/FS2-1263

## Attachments (0)
