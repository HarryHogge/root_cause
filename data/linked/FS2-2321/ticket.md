# FS2-2321: Create a consolidated report on mismatched SW/FW versions for VXE-572/573/574/628/688/594

- **Issue type:** Task
- **Status:** To Do
- **Priority:** Highest
- **Created:** 2024-09-25
- **Updated:** 2026-09-04
- **Reporter:** David Grosher
- **Assignee:** Jason Scherer
- **Creator:** David Grosher
- **Links:** relates to VXEP-598 (VXE 574 Aircraft made hard right turn away from PLZ during VTOL landing); relates to VXEP-611 (VXE 688 on landing transitioned to VTOL, aircraft continues forward flight and crashes into a mountain); relates to VXEP-605 (VXE 572 Multiple uncommanded aborted launches); relates to VXEP-732 (VXE 628 Crash on VTOL descent); relates to VXEP-652 (VXE 573 Cruise motor stopped during RTB, aircraft crashed); relates to VXEP-651 (VXE 594 Operator commanded RTB, AV went directly to IP5); relates to VXEP-896 (CLONE - VXE 688 Launch Aborts ); relates to FS2-2451 (Investigate VXEP-732 - Crash on VTOL Descent); relates to FS2-2837 (Investigate VXEP-605); relates to FS2-2838 (Investigate VXEP-598); relates to FS2-2854 (Jason's Open Investigations)

## Description

We have not received data for 573, 628 or 594, but they were managed by the same group as the other birds on this ticket, all of which had mismatched sw/fw versions. This task is to create a consolidated report demonstrating the operator error in flying these aircraft. Reference the Operators Manual, ADs, and any other published material along with the data provided. 
VXE-573, 628 and 594 are enroute to SLO and we should be able to pull data off of them at that point.     
See the Mismatched_SW/FW label in the VXEP project for linked issues. 
link to presentation: MissMatch-Firmware-Report.pptx

SW Airworthiness Directive for 6.2.9 release: [embedded: Airworthiness Directive (AD)_ Software Update_2024-03-18_A 1.pdf] 
SW Airworthiness Directive for 6.3.4 release: [embedded: Airworthiness Directive (AD) Software Update 2024-08-08_A (e5b5240d-1771-4f31-8f3b-4eeb386d4c93).pdf]

## Sprint

FS2 Sprint 40, FS2 Sprint 31, FS2 Sprint 32, FS2 Sprint 34, FS2 Sprint 29, FS2 Sprint 27, FS2 Sprint 30, FS2 Sprint 26, FS2 Sprint 33

## Comments (10)

### David Grosher, 2024-09-25

@Scott Whitney FYSA

### Jason Scherer, 2024-10-30

@David Grosher @Scott Whitney Still filling in some data, (Need to find the ADs) but let me know if I am missing any incidents/vehicles. I also setup the remaining links to incidents. 
[embedded: Mismatched-SWFW-Versions (79887fe1-866f-4c27-9021-e091140e1fce).xlsx]

### Alexander Alan Arnold, 2025-01-30

@Jason Scherer Do you have the report on this or at least a draft we can look at? Sorry in advance if I overlooked it the linked items.

### Jason Scherer, 2025-02-10

@David Grosher @Pat Wells @Alexander Alan Arnold Here is a first cut of the report. A few of the incidents we didn’t investigate due to old firmware per Greg’s input. If we want to add more detail, I can pull out each incident into a separate slide and look at the data in more depth. Just trying to get a feel for the level of detail that is desired. Let me know and I’ll update accordingly. [embedded: MissMatch-Firmware-Report.pptx]

### Jason Scherer, 2025-02-10

Looks like some of the titles are not scaling well in the browser. I’ll work on that.

### Jason Scherer, 2025-02-11

Added ADs to the ticket

### Jason Scherer, 2025-02-11

I have re-opened investigations into VXE-628, VXE-574, and VXE-688 to support this report. Previously, the investigations were not completed due to outdated firmware.

### Jason Scherer, 2025-02-12

Finished investigating https://jenaero.atlassian.net/browse/VXEP-732 

Now investigating https://jenaero.atlassian.net/browse/VXEP-598

### Pat Wells, 2025-02-18

@David Grosher @Jason Scherer are these additional investigations the internal tasks beyond what we planned to report to the customer on the operator errors?
Trying to determine if we can get a clean copy of the report for the customer as we’ve already closed all these out on our customer facing documents. 

@Alexander Alan Arnold FYSA

### David Grosher, 2025-02-18

@Pat Wells Yes, given the priority given to the 29 palms events we went back to look at these. The additional learnings have been added to the reports at the bottom below the consolidated report. We already provided them a couple of these with the initial draft, but we’ve added a few more details since then. Feel free to make a copy of the deck and remove them if you don’t want to pass them along.

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [Mismatched-SWFW-Versions (79887fe1-866f-4c27-9021-e091140e1fce).xlsx](attachments/24304_Mismatched-SWFW-Versions%20(79887fe1-866f-4c27-9021-e091140e1fce).xlsx.md) | xlsx | 11 | 2024-10-30 | converted |
| [MissMatch-Firmware-Report.pptx](attachments/26159_MissMatch-Firmware-Report.pptx.md) | pptx | 1161 | 2025-02-10 | converted |
| [Airworthiness Directive (AD) Software Update 2024-08-08_A (e5b5240d-1771-4f31-8f3b-4eeb386d4c93).pdf](attachments/26170_Airworthiness%20Directive%20(AD)%20Software%20Update%202024-08-08_A%20(e5b5240d-1771-4f31-8f3b-4eeb386d4c93).pdf.md) | pdf | 2907 | 2025-02-11 | converted |
| [Airworthiness Directive (AD)_ Software Update_2024-03-18_A 1.pdf](attachments/26168_Airworthiness%20Directive%20(AD)_%20Software%20Update_2024-03-18_A%201.pdf.md) | pdf | 1258 | 2025-02-11 | converted |
