# ENG-3149: 457 - Magnetometer heading error with lift power

- **Issue type:** Problem
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2022-06-13
- **Updated:** 2025-06-02
- **Resolved:** 2022-08-26
- **Reporter:** Former user
- **Assignee:** John Clark
- **Creator:** Former user
- **Links:** is duplicated by ENG-3103 (457 - Front left motor started late during takeoff AND Mag Fault); relates to AP-2 (Add flag to firmware to indicate when primary VTOL magnetometer is not functioning. Determine best course of action in that case); relates to XEO-213 (Need to develop process where every inserted contact is inspected, pull tested, and signed off.  )
- **Vehicle Tail Number:** 457

## Description

457 is still exhibiting issues with magnetometer as previously identified by Gordon (see email dated 5/21)

## Corrective Action

Assembly Shop: Replace cable
Engineering: Perform engineering testing to verify issue is resolved
SCO: Check calibration values and perform a ground check to verify sensors and flight readiness
Need to develop process where every inserted contact is inspected, pull tested, and signed off.  
Gordon to add flag to firmware to indicate when primary VTOL magnetometer is not functioning.

## Comments (9)

### Cameron Chapman, 2022-06-13

@Former user, I think this issue was caused by a defective magnetometer harness and resolved with a replacement harness. See NCR-220527 - 256. We could keep this ticket open until the connector inspections and Gordon’s sensor failure flag are released.

### Cameron Chapman, 2022-07-25

https://jenaero.sharepoint.com/sites/JAI_Operations/Lists/NCR%20List/Open%20NCRs.aspx?newTargetListUrl=%2Fsites%2FJAI%5FOperations%2FLists%2FNCR%20List&viewpath=%2Fsites%2FJAI%5FOperations%2FLists%2FNCR%20List%2FOpen%20NCRs%2Easpx&viewid=d8816046%2D6777%2D49d7%2D8136%2D3a2abaa4deb6&view=7&q=NCR%2D220527%20%2D%20256

### Cameron Chapman, 2022-07-25

7/25 corrective action status:
- Pull test procedure. Released, but not fully implemented in electronics.
- Generic cable inspection traveler. The one we reviewed with Matt. I think unreleased and Matt is working.
- Gordon added a flag that will indicate if the backup magnetometer is being used and will stop a launch if so. I think this firmware has not yet been released, but the release status of firmware is hard to find and not published in a way that I know of. Gordon and Matt would know best.

### Cameron Chapman, 2022-07-26

Linked another instance of this issue on 457

### Former user, 2022-08-24

@John Clark please follow up to see if there was a resolution to this, thank you

### Cameron Chapman, 2022-08-25

@Former user , I think this issue is ready to close. Incomplete corrective actions are tracked in linked tickets. Do you agree? Do you think you should be the person to officially close/mark done these tickets?

### Cameron Chapman, 2022-09-16

@John Clark , here is the magnetometer issue fix. Can you verify this portion makes it into the next software release. 
- Gordon added a flag that will indicate if the backup magnetometer is being used and will stop a launch if so.

### John Clark, 2022-10-13

Plan:
- Verify build contains this fix. (see 1. in next comment from Cameron Chapman)
- Complete GCS SW update & validation (required for flight test) Planned 2022-10-21
- Flight test with updated firmware to qualify, Planned week of 10/24. 2022-10-28
- @Gordon Jennings planned to be at test flight and verify flight test sufficient to verify the change.

### Christa Meck, 2024-05-21

Moved from old VIT project to VIT2 project per Cameron's request (https://jenaero.atlassian.net/browse/JA-86#icft=JA-86)

## Attachments (0)
