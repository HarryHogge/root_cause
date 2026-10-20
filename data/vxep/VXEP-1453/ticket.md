# VXEP-1453: New E140 Assemblies DCDC getting hot during operation.

- **Issue type:** Incident (8D)
- **Status:** New
- **Priority:** Highest
- **Created:** 2025-07-24
- **Updated:** 2026-03-02
- **Reporter:** Cameron Chapman
- **Assignee:** John Gober
- **Creator:** Cameron Chapman
- **Labels:** MOLSON
- **Links:** clones VXEP-1452 (New E140 Assemblies video quality issues); is cloned by VXEP-1454 (E140 gimbal getting hot when connected to aircraft.)
- **Customer:** MOLSON
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

Files: VXEP-1452 New E140 Assemblies video not working DCDC getting hot during operation
Investigation Summary test plan and data New E140 Assemblies video not working DCDC getting hot during operation.xlsx
Gimbal SN/Issue Trackerhttps://jenaero.sharepoint.com/:x:/s/FlightSafety/ESjhkbjkZ4hHkZzRRBBjOS4BPZ-Gn1g97DWqg7P1wqAqBA?e=7b16H5

- Assembly 1 (In Canada)
- Please gather PN+SN of the aircraft, gimbal, gimbal harness\
- It was my (Tim M) office. Myself and a MOLSON VXE operator.
Testing in the context of we connected a gimbal with new cable to VXE30 and powered everything on. This didn't work and the gimbal got hot.
 
Notably, we powered up the gimbal connected while on the stand and it worked fine. Didn't notice overheating
Everything involved had the latest software versions.
- Gimbal installed on VXE591
Battery power
Gimbal 6172 but can't confirm at this time. I've asked the other guy if he remembers.
Unknown info re harness
Gimbal plate was one of the new ones brought from HSV by Jackson

Assembly 2 (In HSV)
- Please gather PN+SN of the aircraft, gimbal, gimbal harness
- The unit I (Alex A)  tested was not at the molson site. It was connected to a 140G2 , Hadley will be bringing back the molson cable after completes the swap tomorrow
- "3. The gimbal converter overheating was discovered on while the gimbal was powered on a bench cable assembly"
- We used the power supply that comes from the gimbal field support kit

## Plan

- Complete this incident investigation summary, cause, corrective action, etc. https://jenaero.atlassian.net/wiki/spaces/EF/pages/23363854/Incident+Troubleshooting+and+Resolution+Tracking. 
- Review this doc and add findings to summary E140 cable surge test troubleshooting findings.docx
- In tracker sheet above. Record SN, configuration, and test details of gimbals, cables, aircraft, power source, etc for the ones that overheated.
- Complete actions in the tracker sheet.
- Record where issue was discovered, with which equipment (gimbal and harness PN, rev, SN).
- Summarize how the issues were missed during original testing.
- Ex: was tested with ground harness, not aircraft.
- Document existing ATP and added steps to ensure similar issues won't happen again, and that they would have caught the issue.
- Engineering peer review of DCDC board, design verification, and acceptance test.
- Laszlo peer review and sign off on vault. Cameron review after.
- PN and SN tracker of everything shipped, returns. Involve production, quality, etc.

## Comments (2)

### Mike DeJesus, 2025-08-18

@Justin Hogan  could you please note the testing youve completed in the findings doc (Plan step 1) or drop your tracker here?
@John Gober @Laszlo Juhasz @Connor Peebles  please provide any investigation documents on this topic here so we can start consolidating the findings.

### Justin Hogan, 2025-08-19

Gimbal Harness table.xlsx

## Attachments (0)
