# VXEP-1454: E140 gimbal getting hot when connected to aircraft.

- **Issue type:** Incident (8D)
- **Status:** New
- **Priority:** Highest
- **Created:** 2025-07-25
- **Updated:** 2026-03-02
- **Reporter:** Cameron Chapman
- **Assignee:** Justin Hogan
- **Creator:** Cameron Chapman
- **Labels:** MOLSON
- **Links:** clones VXEP-1453 (New E140 Assemblies DCDC getting hot during operation.); relates to VXEP-1466 (E140 GSC laser ENA/DIS switch not working. )
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
“Not burning but still hot to touch. Still hotter than normal I would say” That said, one was significantly hotter than the other so could be cable specific?? 
Notably, we powered up the gimbal connected while on the stand and it worked fine. Didn't notice overheating
Everything involved had the latest software versions.
- Gimbal installed on VXE591
Battery power
Gimbal 6172 but can't confirm at this time. I've asked the other guy if he remembers.
Unknown info re harness
Gimbal plate was one of the new ones brought from HSV by Jackson

## Plan

- @Justin Hogan  to support the following.
- Record SN, configuration, and test details of gimbals, cables, aircraft, power source, etc for the ones that overheated.
- Record where issue was discovered, with which equipment (gimbal and harness PN, rev, SN).
- Summarize how the issues were missed during original testing.
- Ex: was tested with ground harness, not aircraft.
- Document existing ATP and added steps to ensure similar issues won't happen again, and that they would have caught the issue.
- Engineering peer review of DCDC board and payload configurations, design verification, and acceptance test.
- Laszlo peer review and sign off on vault. Cameron review after.
- PN and SN tracker of everything shipped, returns. Involve production, quality, etc.
- Can track above via linked CAS
- investigation summary,
- incident descriptions,
- linked C/CAs, etc. like we do for flight incident

## Issue Status

not functional may just be it needed the ethernet fix (depending on how hot you meant)
“Not burning but still hot to touch. Still hotter than normal I would say”

## Comments (0)

## Attachments (0)
