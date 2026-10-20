# VA-31: EA Internal: 516 center wing damaged. 511 fuselage+516CW LW motor test failed.

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2023-08-09
- **Updated:** 2026-03-02
- **Resolved:** 2023-11-09
- **Reporter:** Cameron Chapman
- **Assignee:** Laszlo Juhasz
- **Creator:** Cameron Chapman
- **Labels:** 8-28-Sprint, TIQUILA-Blocker
- **Links:** relates to ENG-2181 (EA Internal: VXE511 Aborted Launch at 2ft, VTOL ESCs stuck in initialization loop); relates to ENG-1685 (ENG incidents should have the same fields and workflow as VIT2 incidents.  Should create corrective action and containment issues in ENG as well. ); relates to FS2-690 (Eng 2182); relates to FS2-695 (ENG-2183 VTOL AP WDT investigation); is cloned by VA-35 (511 CW Input power connector damaged); relates to VA-33 (VXE511 Aborted Launch at 2ft, VTOL ESCs stuck in initialization loop); relates to VA-36 (VXE 542 107-102264 Current Sense Power Harness has reflow on the AS150 pin); relates to VXEP-481 (8D #24 – CW to HLB AS150 Connection Issues​ Corrective Actions); relates to VXEP-385 (New Connectors and Contacts, Overall Requirements Review); relates to VA-44 (VXE 516 Try to replicate the damage caused by the high current and the partially mated connectors.); relates to VA-43 (VXE 516 Need to determine if the same battery was involved (demand the battery was used during these incidents)); relates to VXEP-13 (TPTR-51 516 VTOL Motors failed to engage during Launch Wizard 511/516 CW damage); relates to VXEP-12 (TPTR-87 VXE 511 VTOL Connector Issues 516 CW. Contains Main connector/contact C/CAs); relates to VA-320 (VXE 516 Identify and Review C/CA); relates to FS2-952 (Do any of the flight logs list what equipment was connected? If not, could we add this feature?); relates to VXEP-21 (TPTR-53, Ctr Wing 511 Loose article Identified in the center wing); relates to RMA-129 (VXE 516 230705 TIQ); relates to VA-330 (TPTR-87 VXE 511 VTOL Connector Issues)
- **Customer:** TIQUILA
- **Part Number(s):** VXE30
- **Vehicle Configuration:** HLB (S/N 2-1801), 516 CW, 511 fuselage.
- **Corrective Action:** See https://jenaero.atlassian.net/browse/VXEP-12
- **Other Stakeholder (as required):** Matt Philley
- **Plan:** - Closing as duplicate of https://jenaero.atlassian.net/browse/VXEP-12
- **Root Cause:** Link: 8D #TBD - Dual Current Sense AS150 Overheating.pptx

## Description

Closing as duplicate of https://jenaero.atlassian.net/browse/VXEP-12 

This issue is being used to track the launch wizard failure and the 516 damage. See https://jenaero.atlassian.net/browse/ENG-2200 for related 511 CW damage.
See external issue for initial troubleshooting: https://jenaero.atlassian.net/browse/VIT2-322 
Please save files and plots here https://jenaero.sharepoint.com/:f:/r/sites/EngineeringTeam/Shared%20Documents/Investigations/Old%20Docs-use%20flight%20safety%20Incident%20Reports%20-%20Shortcut%20now/VIT2-322,%20Tail%20516-Fuse%20511%20and%20516-Wing?csf=1&web=1&e=PmlXN0 
After discovering a loose object in CW 511 we switched to the wing set from 516. One flight of 511 with 516 wing set was conducted. After that flight one of the students mentioned that the HLB (S/N 2-1801) had a strong smell from around the discharge connector. The connector looked normal. During the LW for the second flight the motor check failed to spin the lift rotors more than a half turn. The VTOL Control Window indicated VTOL launch not OK and the HLB voltage was fluctuating 7-27V. The LW was canceled. At this point we were no longer going to fly this aircraft. I inspected the CW high voltage connector and it appears to have some discoloration. For troubleshooting we tried a different HLB and were able to complete the LW without issue. We also retried the original HLB and passed the LW without issue. It seemed like a good day to not crash a plane so we did not attempt a flight.

## Issue Status

Closing as duplicate of https://jenaero.atlassian.net/browse/VXEP-12 

The Avionics compartments covers were removed from both of the CWs and visually inspected for markings of possible over-heated wires, components, PCB traces. There were no noticeable marks or damages. 
516-
- VTOL data corrupt. Still should have some data in XCOM log. 
- VTOL 26 and 29 are attached
- There is an overcurrent in the logs; can be caused by not fully connecting.
- Shows damage at the top of anti-spark contact. , Resistance across the resistor measured at 96.9 ohms. usually ~6ohms. This was likely damaged from the increased heat.
- Left wing connector also shows black residue and melted solder, which indicates overheating and high current.
- At a base current of 150A a fully mated connector has a slower increase of temperature compared to if it is not fully mated. This is also true for currents that are above 150 A.
- When the connectors are not fully mated, and knocking is applied to the connector there is a drop in current. This simulates vibration experienced during launch
- Impedance of the contact after the incident measured higher than a new contact, but not high enough to cause this damage if fully mated. May have been a contributing factor if partially mated. Measured 188uohms, passing <180 uohms for a new assembly.

## Comments (20)

### Cameron Chapman, 2023-08-09

@John Clark can your team please help with the following? Greg approved asking. 
- On separate plots, can you please plot the currents, voltages, and throttles of VTOL00029 vs an earlier flight?
- A higher current could have caused this damage.
- A higher resistance connections could have also (which would be visible in the logs by a lower measured voltage and higher throttles).

Please save files and plots here: https://jenaero.sharepoint.com/:f:/r/sites/EngineeringTeam/Shared%20Documents/Investigations/VXE%20Wing%20516%20Fuselage%20511%20VTOL%20Power%20Issue?csf=1&web=1&e=RlYDz5

### John Clark, 2023-08-09

@Cameron Chapman can you please provide the AAR for VTOL00029 and the “earlier” flight. I do NOT have access to the link in your request. Please, always attach.

### Cameron Chapman, 2023-08-09

@John Clark  see https://jenaero.atlassian.net/browse/VIT2-322 . This is the internal issue continuing that investigation. You previously reviewed this data there.

### John Clark, 2023-08-09

@Cameron Chapman here is the requested data. 
[embedded: charts.docx]

### Cameron Chapman, 2023-08-09

Thanks John for posting those plots. Do you have the excel files that generated those plots available? Can you please post them here if so? https://jenaero.sharepoint.com/:f:/r/sites/EngineeringTeam/Shared%20Documents/Investigations/VIT2-322,%20Tail%20516-Fuse%20511%20and%20516-Wing?csf=1&web=1&e=0CI18P&xsdata=MDV8MDF8fDQwZDBiYjQ1YjViMjQ3ZTQxMmQ2MDhkYjk5MWRmZTNlfDE4NzZmNjFhM2JkYjQ4NDNhZTcwNzVlZDBjY2I3NDA0fDB8MHw2MzgyNzIxMjYzMDE2MzkzODJ8VW5rbm93bnxWR1ZoYlhOVFpXTjFjbWwwZVZObGNuWnBZMlY4ZXlKV0lqb2lNQzR3TGpBd01EQWlMQ0pRSWpvaVYybHVNeklpTENKQlRpSTZJazkwYUdWeUlpd2lWMVFpT2pFeGZRPT18MXxMMk5vWVhSekx6RTVPamt4TWpJNU9HWXdNMk5pTXpRNU1EWmlZMkkwT1RObU56UmlOelExWkdVeFFIUm9jbVZoWkM1Mk1pOXRaWE56WVdkbGN5OHhOamt4TmpFMU9ESTRNelUxfGY4MTAyZjE2OGEyNTQyY2UxMmQ2MDhkYjk5MWRmZTNlfDkxMmJjY2QzYTY0ODQ1ZjhhZTBmN2ViMzM2YTZlYjZm&sdata=YzU0VnZxcUVsakdxcERTSGh5VThzMlZlKzlJaG9DTmdIR1hMRnAzQzFkRT0%3D&ovuser=1876f61a-3bdb-4843-ae70-75ed0ccb7404%2Cchapman%40edgeautonomy.io . I think we should make posting files to shared locations standard practice going forward. Much easier to modify existing graphs rather than everyone download and plot separately. Is the VTOL battery voltage available for these flights? I do not see them in the document.

### Cameron Chapman, 2023-08-09

Excel files are uploaded to the sharepoint.

### Matt Philley, 2023-08-14

@Cameron Chapman @John Clark @Laszlo Juhasz who is investigating the dual current sense issue currently? It looks like we have the same thing now presenting on AC 542 this morning. Its an AC that previously had SCO flights, we replaced the Avionics Board Assy due to conformal coat stuff last week and were just gunna do an SCO check and Check Flight, but Carson had the same failure, pressed connector on harder, resolved issue, but when removing the connector noted that the solder had reflowed. 
I will add more details once I get back to my desk. 
AC 542 - SCO - AS150 Solder Reflow in Dual Current Sense

### Matt Philley, 2023-08-14

@Laszlo Juhasz I added a link to the Root Cause section of this Jira ticket to an 8D template for this investigation. Dont worry about all the other stuff, but please start dropping info in the “D4 - Root Cause” section of the presentation. Dont worry about making it look pretty. I can help with some of that and formatting. Main thing is to start gathering an organizing details about the test setup, test procedure, and test results. 
I will be grabbing the harness from AC 542 so we can use that for some more testing.

### Matt Philley, 2023-08-14

@Laszlo Juhasz @Cameron Chapman @Greg Fryer To catch folks up and document the finding from today:
I will include more organized info/details in the 8D presentation linked in the Root Cause section of the description of this Jira ticket, but we found there to be build up at the base of the AS150 connector of the Hybrid Lift Battery. This does prevent the connector from being able to be fully seated.
We removed some and measure it to be around 0.075” thick.
I coordinated with Laszlo to see if this would be enough to spike the resistance and cause that excessive temp climb. We will try and test for that ASAP.

This is from HLB SN: 2-1803 that came back as part of this investigation:
[embedded: image-20230814-212532.png]
  This is from an HLB used in SCO, SN: 2-1948. This is the one we removed a piece ~0.075” thick
[embedded: image-20230814-212554.png]

### Cameron Chapman, 2023-08-14

Thanks @Matt Philley . An important thing to note, HLB 2-1803 was involved in this incident, not the original incident this issue documents. It could be related to the cause of this issue (similar problem, different battery), but was not the cause of this specific one.

### Cameron Chapman, 2023-08-18

@Adrian Garcia and @Laszlo Juhasz please see new actions in inv plan.

### Laszlo Juhasz, 2023-08-22

@Matt Philley @Cameron Chapman @Sean Odell @John Clark @Adrian Garcia The connection and disconnection force were tested, and a video compiled to  https://jenaero.sharepoint.com/:v:/r/sites/EngineeringTeam/Shared%20Documents/Investigations/VIT2-322,%20Tail%20516-Fuse%20511%20and%20516-Wing/Connect_Disconnect%20_test.mp4?csf=1&web=1&e=QFhSXx. Basically, it’s showing about equal force to connect and disconnect the connector at about ~15lb dry and ~11lb with greased O-ring.

### Cameron Chapman, 2023-08-24

Linking subtasks to parent

### Cameron Chapman, 2023-08-29

@Laszlo Juhasz and @Adrian Garcia please update investigation status with major findings and plan with remaining steps for each of your top investigations.

### Cameron Chapman, 2023-11-08

@Adrian Garcia or @Mark Squillante , can you please run this battery test soon?

### Mark Squillante, 2023-11-08

Battery given to @Ben Norris for testing, should be completed this afternoon.

### Mark Squillante, 2023-11-09

Battery test complete. I’m not sure exactly what the pass/fail criteria is but there are a couple of items in red in the 2-1801 retest spreadsheet. Looks like possibly some cell voltages are unbalanced. Also included are the original test results from April.
[embedded: 2-1801 retest.zip]
@Cameron Chapman

### Cameron Chapman, 2023-11-09

@Mark Squillante please always save files to sharepoint, rather than uploading. Please do not use zip files.
Please save files and plots here https://jenaero.sharepoint.com/:f:/r/sites/EngineeringTeam/Shared%20Documents/Investigations/Old%20Docs-use%20flight%20safety%20Incident%20Reports%20-%20Shortcut%20now/VIT2-322,%20Tail%20516-Fuse%20511%20and%20516-Wing?csf=1&web=1&e=PmlXN0 . Pass/fail criteria are in the vault procedure. Search the HLB PN. Thank you.

### Mark Squillante, 2023-11-09

Here is the location of the HLB test results: https://jenaero.sharepoint.com/:f:/r/sites/EngineeringTeam/Shared%20Documents/Investigations/Old%20Docs-use%20flight%20safety%20Incident%20Reports%20-%20Shortcut%20now/VIT2-322,%20Tail%20516-Fuse%20511%20and%20516-Wing/511%20HLB%20Test%20results?csf=1&web=1&e=a65dJt

### Christa Meck, 2025-04-17

Removed parent to prep for Incident hierarchy change.  Parent is linked as Linked issue.

## Attachments (8)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| charts.docx | docx | 1565 | 2023-08-09 | no text found |
| [511 and 516 charts.docx](attachments/15808_511%20and%20516%20charts.docx.md) | docx | 1796 | 2023-08-10 | converted |
| [Vehicle Investigation V516+511.pptx](attachments/15809_Vehicle%20Investigation%20V516+511.pptx.md) | pptx | 22024 | 2023-08-10 | converted |
| image-20230814-212532.png | image | 344 | 2023-08-14 | listed only |
| image-20230814-212554.png | image | 1018 | 2023-08-14 | listed only |
| 516 CW input power conn.JPG | image | 2692 | 2023-08-18 | listed only |
| 516 wing connector Residue.jpg | image | 352 | 2023-08-18 | listed only |
| 2-1801 retest.zip | archive | 61 | 2023-11-09 | listed only |
