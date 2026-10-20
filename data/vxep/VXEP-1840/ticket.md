# VXEP-1840: VXE 655 unable to connect

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2026-04-14
- **Updated:** 2026-10-06
- **Resolved:** 2026-07-20
- **Reporter:** Stephan Johnson
- **Assignee:** Ronnie Baker
- **Creator:** Stephan Johnson
- **Labels:** RCCA, TIQUILA, Weekly-incident-tracker
- **Links:** relates to RMA-960 (A655 RMA 260407-3); relates to VXEP-1838 (VXE 622 unable to connect); relates to FS2-4500 (Investigation of TIQ Aviboxes); relates to VXEP-1633 (VXE 540 Aircraft failed to connect, FWAP read all 0s. ); relates to VXEP-1971 (VXE 885 Erratic behavior in flight caused crash)
- **Customer:** TIQUILA
- **Part Number(s):** 107-111718
- **Vehicle Tail Number:** VXE-655
- **Incident Type:** Other (Record"Event Type: XXXXXX" in the description)
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

Operator attempted to connect with the aircraft and was unable to do so. Unknown if further troubleshooting was conducted due to lack of information.

## Plan

- Repeat and confirm symptoms reported
- Open and inspect avionics box
- Swap FWAP with known good, repeat and confirm fixed
- Swap MAGACC2 board on original FWAP, install into box. Confirm fix.
- @Ronnie Baker  to coordinate RMA, production rework.
- Isolate customer incident MAGACC2 board, measure for shorting. Remove shield and inspect for FOD/ Corrosion/ Shorting.
- Double check all of the above
- Remove MAGACC2 board and label. Prepare control samples to be sent out for decapsulation for delamination via CSAM analysis.

## Issue Status

- Accomplished here: [FS2-4500] Investigation of TIQ Aviboxes - Jira
- Nothing obvious, photos taken
- Swapped in AP SN:10877, confirmed issue resolved
- back to production to perform MAGACC2 swap (or FWAP swap if more economical)
- 5V ↔︎ GND = 320Ohms. 3.3V ↔︎ GND = 22kOhms. 3.3V ↔︎ 5V = 22kOhms.
- dsa
- dsa

## Comments (4)

### Cameron Chapman, 2026-04-21

Discussed with Scott and John. Found that there is an issue with the MPU in both 622 and 655.
Evidence is consistent with MPU 9250 issue and needs to be replaced
- MPU-9250 init fails
- then goes into a while loop and continues to fail Init

 
622
 
av655
 Discussed with Scott and John. Found that there is an issue with the MPU in both 622 and 655.
Evidence is consistent with MPU 9250 issue and needs to be replaced
- MPU-9250 init fails
- then goes into a while loop and continues to fail Init

[embedded: image-20260421-164937.png]

### Connor Peebles, 2026-04-21

Production to perform step 4 in plan above, retain MAGACC2 board for continued engineering investigation. Also posted in https://jenaero.atlassian.net/browse/RMA-960.
@Cameron Chapman @Stephan Johnson @Scott Whitney

### Connor Peebles, 2026-05-01

@Ronnie Baker @Lauren Velasquez Any status updates?

### Jackson Riley Curvin, 2026-07-20

Report sent to customer

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20260421-164937.png | image | 275 | 2026-04-21 | listed only |
| v655_dataLogs.zip | archive | 9388 | 2026-04-21 | listed only |
