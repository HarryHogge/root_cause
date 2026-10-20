# VXEP-1282: B30 689 - MCM failure after return from HSV-Nose fuse blown

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** High
- **Created:** 2025-05-16
- **Updated:** 2025-05-19
- **Resolved:** 2025-05-19
- **Reporter:** Cameron Chapman
- **Assignee:** Jackson Riley Curvin
- **Creator:** Cameron Chapman
- **Labels:** MCM-Issue
- **Links:** is cloned by VXEP-1283 (B30 300 - 5/14 MCM failure - had been set to be able to auto DHCP which let it randomly drop the 10 network); relates to XKIT-4250 (Schedule a meeting to discuss the non-critical outputs and how to control power to each); relates to XKIT-4203 (Develop 28V Power Budget & Electronics Architecture)
- **Corrective Action:** - Move MCM to flight critical bus (still with effuse proection in B34 https://jenaero.atlassian.net/browse/XKIT-4203
- **Issue Status:** 689 came back from Huntsville with a blown Nose Fuse, so no power was getting to the MCM. Fixed now
- **Severity:** 1 - Flight Critical

## Description

Need to populate issue summary and plan. 
Dave 5/14  “lost an MCM on v689 after its return from HSV. I understand it hasn't been looked into. Today (5/14) we lost one on v300 and v757 had an unexplained reset at the flight line. It sounds like we have a very serious issue on our hands that will require hardware support”

## Plan

@Jackson Riley Curvin do you know the history of this vehicle and what might have blown the nose fuse? Is your team available to review data logs if not?

## Comments (5)

### Jackson Riley Curvin, 2025-05-16

@Cameron Chapman  I do not know the history of it as I was not directly involved in the demo, I just know that it was set up for display purposes the FSRs can start reviewing the data and see if find anything unusual.

### Scott Whitney, 2025-05-16

@Cameron Chapman  - @Connor Peebles to get the MCM back in a good state.

### Connor Peebles, 2025-05-16

@Scott Whitney The data logs will definitely tell you when the fuse was blown, unless it happened in less than a data log interval (which is possible if it was a big enough power-short on a 10 second data log)

### David Grosher, 2025-05-19

Internal asset with no records of usage or config. Closing Issue.

### David Grosher, 2025-05-19

No data to investigate. Internal system.

## Attachments (0)
