# XKIT-760: Main AS150 replacement issue-Develop new battery power connectors for Havoc Block 5

- **Issue type:** Epic
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** High
- **Created:** 2023-10-27
- **Updated:** 2026-06-24
- **Resolved:** 2026-05-25
- **Reporter:** Cameron Chapman
- **Assignee:** Scott Stuckey
- **Creator:** Cameron Chapman
- **Links:** duplicates VXEP-386 (Develop Replacement for AS150 Connections); duplicates VXEP-477 (Old, internal work - Develop plan for latching power connectors (AS150 Replacements)); relates to XKIT-761 (Evaluate using crimped and locking signal connectors for new X-kit connectors); relates to XKIT-1716 (SB40 Vehicle Power Switch); relates to VXEP-628 (Systemic VXE30 VTOL ESC Reliability Issues ); relates to VXEP-231 (VXE-496 with 550 wing set-failure during VTOL transition-AS150 contact issues)
- **Sprint:** VXE-3 X-Kit Sprint 10/30-11/20, VXE-3 X-Kit Sprint 11/17-12/07, VXE-3 X-Kit Sprint 12/11-12/29
- **Production Stakeholder:** Emalee Johnson
- **Supply Chain Stakeholder:** Kenneth Weber
- **Leadership Stakeholder:** Greg Fryer

## Description

5/17 Meeting Plan
AS150 Replacement RVTM.xlsx
Power contacts and connectors
https://jenaero.atlassian.net/browse/XKIT-760 
Folders
- https://jenaero.sharepoint.com/:f:/r/sites/IRAD/Shared%20Documents/General/Projects/05%20Havoc%20Block%205%20(Development%20to%20Production)/Electrical%20Wiring%20Interconnect%20Systems%20(EWIS)/Connectors%20and%20Contacts?csf=1&web=1&e=XLlim2
- C:\Users\cchapman\OneDrive - Edge Autonomy\Projects\IRAD Projects\05 Havoc Block 5 (Development to Production)\Electrical Wiring Interconnect Systems (EWIS)\Connectors and Contacts
- Part information. All-Parts.xlsx

Methode Tests Methode Contact Tests.docx

Requirements 
- Need to have
- Done by havoc production. Ideally some form of it for July deliveries.
- not compatible with VXE30 to prevent plugging 60V into 28V VXE30.
- locking features or verification of full mate (ex: blind mate).
- Fully mated indicator (Ex lock visible, clicks, cannot be assembled partially). @Laszlo Juhasz designed magnetic locking solution (potential for patent on this design being looked into), also latching mechanism is an option
- new contacts not from not Chinese mfr (AMASS) - @Laszlo Juhasz coordinating with Methode Power Solutions https://www.methodepowersolutions.com/products/power-connectors-contacts/. NDA process currently underway.
- Antispark solved in some form (connector, power relay, etc). - will discuss with Methode to ensure they can accommodate.
- Supports worst case power profiles (ideally with room to grow).
- Scales up and down for each power connector application we need. (can be different connectors, contacts, not all require antispark if assembled in correct order).
- Sealed.
- Nice to have 
- Crimped contacts - will discuss with Methode to ensure they can accommodate.
- Combine data and power connectors?

Tasks:
- Check in with connector mfrs. Can they commit to those timelines? Review their proposals.
- Evaluate options.
- Cross functional review.
- Downselect.
- Implement in batteries, aircraft, etc.

## Comments (11)

### Cameron Chapman, 2023-10-27

closing duplicate

### Cameron Chapman, 2023-10-27

Reopening the linked issue if for VXE. This is for Xkit.

### Cameron Chapman, 2024-04-10

@Laszlo Juhasz @Mark Squillante @Rajesh Budhabhatti here is a project for power connectors. @Stephen Peters have you worked on this at all?

### Stephen Peters, 2024-04-11

@Cameron Chapman, @Tom Westrich did some concepting with COTS TE blade connectors but aside from that no. [embedded: ENG_CS_1773096_SEC01_BOARD_TO_BOARD_0210.pdf]

### Rajesh Budhabhatti, 2024-05-02

@Laszlo Juhasz , @Cameron Chapman Stefanie Polk has received and returned a fully executed NDA regarding the hot swappable connector to Eric Finn at Astron. We are good to share Laszlo’s design with the vender.

### Cameron Chapman, 2024-05-02

@Rajesh Budhabhatti sounds good. Thank you for the update. We should also keep other quotes moving to compare (Ex: ODU, glenair). It might be easiest to track the status of each quote as a subtask in this project.

### Rajesh Budhabhatti, 2024-05-02

@Cameron Chapman Will do. I will work with Laszlo and keep the quotes moving as subtasks. Also, thank you for the OJT, it helped me a lot.

### Rajesh Budhabhatti, 2024-05-09

Method is ready for a meeting and exchange of data. Internal meeting is set for 5/10/24 to discuss and collaborate with Steven P, AA team, Cameron, Laszlo and Raj to move connector development.

### Rajesh Budhabhatti, 2024-05-10

Meeting date is moved to Friday 5/17/2024 by Steven Peters.

### Rajesh Budhabhatti, 2024-05-10

@Cameron Chapman @Stephen Peters @Dylan Peters @Tom Westrich @Laszlo Juhasz 
Meeting Summary: Attendees: Stephen Peters, Tom Westrich, Dylan Peters, Laszlo Juhasz, Raj Budhabhati
During the meeting, Stephen Peters brought up the topic of their ongoing work on an anti-spark connector and expressed interest in learning about our solution. Laszlo Juhasz then presented the details and a video demonstration of his magnetic latching anti-spark connector. He also explained that the pins used were sourced from Method.
Upon mentioning our intention to pursue a patent, Stephen offered the assistance of their patent attorney. The group discussed an alternative solution involving a switch/relay to prevent sparking, but ultimately favored Laszlo's solution for its reliability and simplicity. Stephen also volunteered to help with the mechanical design of the connector and offered to assist with bench testing.
It was agreed that the Havoc connector should be distinct from the VXE30 connector to avoid confusion. There was some debate over the placement of current limiting resistors, with the consensus being that they should be located in the battery connector.
A follow-up meeting has been scheduled for Friday, May 17, 2024. Raj will coordinate with the AA team's patent attorney and manage tasks in Jira.

### Rajesh Budhabhatti, 2024-06-04

Sharepoint folder created to hold the related documents here: New_Battery_Power_Connector

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [ENG_CS_1773096_SEC01_BOARD_TO_BOARD_0210.pdf](attachments/20005_ENG_CS_1773096_SEC01_BOARD_TO_BOARD_0210.pdf.md) | pdf | 5010 | 2024-04-11 | converted |
