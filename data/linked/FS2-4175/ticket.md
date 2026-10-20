# FS2-4175: B40 Endurance Test - Capture WD boots

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2026-01-07
- **Updated:** 2026-04-17
- **Resolved:** 2026-04-17
- **Reporter:** Scott Whitney
- **Assignee:** Scott Whitney
- **Creator:** Scott Whitney
- **Parent:** FS2-4309 B40 WD Investigation
- **Links:** relates to VXEP-1692 (B40/30 XCOM WDT resets )
- **Epic Link:** FS2-4309
- **Sprint:** FS2 Sprint 37, FS2 Sprint 36

## Description

Endurance test point moved to Investigation Summary-B40 increased XCOM WDs.xlsx
Data Folder: B40 Investigation Data
- Baseline: Test build 11/18 - COMPLETE
- Data: 2026-01-08: 
- 1/9: endurance_1_9_26_882_B40_11-18_all
- 1/8: endurance_1_8_26_882_B40_11-18_all
- 1/7 (endurance_1_7_26_882_B40_11-18_all)
- Date: 2025-01-07, 2026-01-08
- Vehicle: 882
- Firmware & Configs: https://jenaero.atlassian.net/wiki/x/AYAxOQ 
- FWAP: 11/18 build
- VTOL: 11/18 build
- XCOMM: 11/18 Build
- Baseline+ :Test build 11/18 xcomm with other RC1 binaries (baseline+) 
- Data: endurance_1_7_24_882_11-18xcomm_RC2ap_RC2vt
- Date: 2025-01-07
- Vehicle: 882
- FWAP & Configs: RC1 (12/19 build)
- VTOL & Configs: RC 1 (12/29 Build)
- XCOMM & Configs: 11/18 Build
- RC1 on 913: Test Release Candidate 1 on v913 COMPLETE
- Data: endurance_1_8_26_913_B40_RC1
- Date: 2026-01-08
- Vehicle: 913
- Firmware & Configs:  https://jenaero.atlassian.net/wiki/spaces/VXEA/pages/967180289/B40+Release+Candidate+1+-+RED+TAGGED?atlOrigin=eyJpIjoiMjdmOTc1MWZhMzM5NDJjODg3M2M4MTQ1NjM0ODhmZmIiLCJwIjoiYyJ9 
- FWAP: RC1 (12/19 build)
- VTOL: RC 1 (12/19 Build)
- XCOMM: RC 1 (12/19 Build)
- BLOCKED: RC 1 on v882+: Test Release Candidate 1 on 882 with new avionics (blocked by new avionics) 
- Data:
- Date:
- Vehicle: 882 (avionics from
- Firmware & Configs: https://jenaero.atlassian.net/wiki/x/AQB7P 
- FWAP & Configs: RC1 (12/19 build)
- VTOL & Configs: RC1 (12/19 Build)
- XCOMM & Configs: RC1 (12/19 Build)


IRON BIRD TESTS (configs match above but on B40 Ironbird):
- Baseline: endurance_ironbird_B40_11-18_all
- Baseline+:
- RC 1
- RC 2

## Comments (5)

### Scott Whitney, 2026-01-07

Production Request for new Avionics https://jenaero.sharepoint.com/:li:/s/JAI_Operations/IwBj9LQTDU-KT4rM_saavCGsASFl6b-bgXrTGoPNrAmDRZ8?e=mbdTS9
I have also requested that Jo Brown provides an MCM with JP6

### Scott Whitney, 2026-01-07

FYSA @David Grosher  @Scott Hunter

### Scott Whitney, 2026-01-08

Data from 1st motor spin unexpected_fwd_motor_spin.zip
- Vehicle: 882
- Firmware: Baseline 11/18

### Scott Whitney, 2026-01-08

2026-01-08 Notes from Investigation tag up:
Mixing of event log and data log on 882
- Memory allocation and deallocation
- could be caused by SD Card Reformat
- Pull avionics from 882 and swap SD card on XCOMM

v913 Status
- Cannot get data
- Battery provisions - could that be blocking 913 from doing endurance tests?
- Everett to create vehicle difference sheet

Iron Bird Endurance Test:
- Baseline (11/18 baseline firmware and configs)

- RC2

### Scott Whitney, 2026-04-17

Marking as complete. Endurance sheet is here: https://jenaero.sharepoint.com/:x:/s/EngineeringTeam/IQCef7D9-TpnS7zWSJcfxpGFAfeFp9CuqF0mtUyAnqdbB6Q?e=Lv7Hm2&nav=MTVfezA5QjdENjcxLUNDQTMtNDQxQy1BOEQ5LTEwRDk2OTdFMjYyMX0

## Attachments (0)
