# VXEP-1368: VXE-542 Voltage issues

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2025-07-08
- **Updated:** 2026-03-02
- **Resolved:** 2025-12-31
- **Reporter:** Jackson Riley Curvin
- **Assignee:** Samuel Lopez
- **Creator:** Jackson Riley Curvin
- **Labels:** TIQUILA
- **Links:** relates to RMA-721 (VXE-542 RMA # 250630-1); relates to VXEP-1416 (VXE-542 RMA # 250630-1 - Investigation)
- **Customer:** TIQUILA
- **Vehicle Tail Number:** 542
- **Vehicle Configuration:** VXE-30
- **Corrective Action:** Microcontroller are now stored in calibrated McDry cabinet.
- **Severity:** 4 - Annoyance

## Description

LM noted low Imotor and Voltage as indicated on the GCS.  

- Carson Buckley recommended that RMA swap out the nose cone and note Imotor and Voltage readings; and they were also low (although higher than previous measurements using v542’s nose.

[embedded image-20250708-171804.png]
- Cameron Chapman recommended that I test 542’s nose cone using the Iron Bird in Electronics.  The Iron Bird results indicated that there are no issues with the nose cone.
- Given #2 above, Cameron recommended an Engineering Jira ticket be opened to track and support diagnosing the problem.

## Plan

2025-12-31
VXE-542 came in to Edge SLO where it was recognized to have symptoms associated with a faulty Fixed Wing AP, which was promptly replaced (see below).  The aircraft then tested normally and was sent back to the customer, who has received it and had no issues with it.  The customer has not requested a report and Drew Hildreth has recommended we close this investigation.
Fixed Wing AP microcontrollers: before the arrival of Steve Stack to the quality team, microcontrollers were incorrectly stored in the cage before assembly.  This was rectified with their storage in the McDry with the cabinet itself being regularly calibrated.  However, some amount of microcontroller made it on to the aircrafts.  This was further detailed in the investigation for VXE-519 (see below).
[VXEP-1446] VXE-519 Power Fluctuations - Jira
VXE-519 Investigation Report - Power Fluctuations.pptx

## Root Cause

Fixed Wing AP was faulty and causing erroneous power readings.  Cause suspected to be microcontrollers that were stored incorrectly before assembly.

## Comments (3)

### Cody Smisek, 2025-12-02

was assigned to Camron Richardson, reassigned to @Cameron Chapman to determine who can handle.

### Drew Hildreth, 2025-12-30

@Lauren Velasquez @Ronnie Baker Let’s have a quick conversation about this one this morning some time. Above talks about Nose Cone, but the Quote in the RMA is talking about an AutoPilot change. I want to make sure that we have our ducks in a row here as this is a TIQUILA asset.

@Samuel Lopez FYSA

### Samuel Lopez, 2025-12-31

This aircraft has been returned to customer.  Root Cause was Fixed Wing Autopilot microcontroller.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| VTOL_VXE542.zip | archive | 10815 | 2025-07-08 | listed only |
| XCOMM_VXE542.zip | archive | 5297 | 2025-07-08 | listed only |
| image-20250708-171804.png | image | 1351 | 2025-07-08 | listed only |
