# VXEP-1478: CAN Resistors - Testing

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2025-08-18
- **Updated:** 2025-10-15
- **Resolved:** 2025-10-15
- **Due:** 2025-08-20
- **Reporter:** Samuel Lopez
- **Assignee:** Samuel Lopez
- **Creator:** Samuel Lopez
- **Labels:** EE
- **Parent:** VXEP-1319 Improvements 2122839-01 Modified Air Data Board
- **Epic Link:** VXEP-1319
- **Start date:** 2025-08-18

## Description

Testing integrity of CAN signals on new 2122839 Air Data Boards without terminating resistor R10.  Check functionality on both B30 and B40 ironbirds.

## Plan

- Lower priority, but we should next see if the CAN interface is ever tested in electronics by itself (so it would require a test terminator).
- Next we could do similar testing for the rest of the CAN system (with the ADB resistor removed)

## Issue Status

Results are found here.
CAN Results.pptx

Test Data is found her.e
ADB CAN Termination

## Comments (3)

### Samuel Lopez, 2025-08-18

- Specify which ironbird it was tested on. The ppt seems to indicate B40. It should be tested on both, but B30 is priority. Please separate sections of report into B30 and 40 (slide groups can help)
- Indicate on each slide where the measurements were performed.
- Lower priority, but we should next see if the CAN interface is ever tested in electronics by itself (so it would require a test terminator)
- Next we could do similar testing for the rest of the CAN system (with the ADB resistor removed)

### Samuel Lopez, 2025-09-10

Testing for this has concluded.  The ADB works well with and without the CAN resistor.  All results are in the attached powerpoint.

### Samuel Lopez, 2025-09-12

Results Update:

Testing for B40 shows no discernible change when removing the CAN terminator from ADB.  B40 has two other CAN terminations, Left Boom and Tail Boom.
Testing for B3x shows no discernible change when removing the CAN terminator from ADB.  B3x has two other CAN terminations, XCOMM and VTOL AP.

View CAN Results powerpoint for diagrams.

## Attachments (0)
