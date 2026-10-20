# FS2-1419: Test operation of RTOS to rule in or out processor loading issues for AV604 mishap.

- **Issue type:** Task
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Medium
- **Created:** 2024-02-06
- **Updated:** 2024-04-24
- **Resolved:** 2024-04-24
- **Reporter:** Eric Brewer
- **Assignee:** Scott Hunter
- **Creator:** Eric Brewer
- **Fix versions:** Release 6.3.4
- **Parent:** FS2-1674 Fix for Bad Mag data
- **Links:** relates to VXEP-263 (VXE-604 crash during SCO/ Flight test); is cloned by FS2-1420 (Add a button to the webpage to toggle a low-priority `while (1) {}` task on and off); is a parent of FS2-1420 (Add a button to the webpage to toggle a low-priority `while (1) {}` task on and off); relates to FS2-1432 (v604 Crash investigation)
- **Epic Link:** FS2-1674
- **Sprint:** FS2 Sprint 16, FS2 Sprint 14, FS2 Sprint 17, FS2 Sprint 15

## Description

Create a low priority task in the RTOS with a simple task such as “while(1)” to eat up spare CPU cycles. Run other CPU-intensive tasks such as burst logging and see if the RTOS appropriately allows flight critical processes to continue to operate without degradation.

## Comments (3)

### Gabriel Staples, 2024-02-06

I volunteer to do the portion of this ticket where we add a low priority while (1){} type task. I’d add a button to the webpage to turn such a task on and off. Ticket I made: https://jenaero.atlassian.net/browse/FS2-1420

### Scott Hunter, 2024-02-29

I created a sceme for this and https://jenaero.atlassian.net/browse/FS2-1420 where the while loops are enabled/disabled via a #define in Build.h. The loops are activated via UDP from an external computer, not necessarily the GCS.
The code is prepped to merge to main_robustness

### Scott Hunter, 2024-04-24

The ability to insert data or a command into the VTOL and XCOMM processors is established in other branches and has been merged in to release candidates. 
Placing a while(1) loop inside a given task is a trivial task from this point. It makes sense to keep the code a little cleaner and avoid the clutter of another block of code enabled via #if/#endif

## Attachments (0)
