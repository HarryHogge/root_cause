# VXEP-1998: B35X Vehicles Not Detecting CW Without LEMB CAN Connector Installed

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2026-09-14
- **Updated:** 2026-10-19
- **Resolved:** 2026-10-19
- **Reporter:** Jeremy Kostel
- **Assignee:** Alexander Alan Arnold
- **Creator:** Jeremy Kostel
- **Parent:** VXEP-1880 LEMB CAN EE Investigation
- **Epic Link:** VXEP-1880
- **Issue Status:** In Progress – Awaiting HSV Hardware Test

## Description

Army B35X aircraft reported an issue where the CW would not detect unless an LEMB battery was connected. This behavior is not expected. The only CANbus hardware change between Blk30 AdvNav and Blk35X was adding a splice to the existing HLB CAN connection and adding a new branch for the LEMB connector. B30 UAP iron bird and B30 IB both have the same hardware LEMB CAN connector and do not have CW detection issues with it unplugged, suggesting the hardware change itself is not the root cause.
Two Army aircraft showed the same unexpected behavior. There is concern that the CANbus on these units may have been damaged, potentially by operation with LEMBs. No known CAN failure mode should cause “works only with LEMB connected,” but given historical issues with LEMB damaging CAN, HW validation is needed.
HSV team has B35X assets available (1057, possibly 828). Need basic power‑up testing with a standard main battery (non‑LEMB) to confirm whether CW detection works as intended on a clean B35X hardware path.
Goal:
Verify whether the B35X CANbus hardware path correctly supports CW detection with a standard main battery and no LEMB connected.

## Plan

HSV team to identify a B35X asset available for testing (1057 preferred; 828 possible).
- Confirm configuration state of the aircraft (firmware, gains). No need to adjust configuration for this test unless required for basic power‑up.
- Follow test procedure (HSV):
- Power the aircraft using a standard main battery (not LEMB).
- Observe whether CW is detected.
- Move all the way through LW
- Report results and any anomalies
- Pull aircraft logs and attach to this ticket

- If CW is detected normally:
Strong evidence that Army aircraft have hardware damage or compromised CAN integrity.
Follow‑on action: escalate for Army aircraft inspection/recall review.

## Comments (4)

### Jeremy Kostel, 2026-09-14

FYSA @David Grosher

### Alexander Alan Arnold, 2026-09-14

@Jeremy Kostel first tested aircraft 6.6.1 and OGCS 1.4.2 vehicle type was 115, no issues with LW, changed vehicle type to 134 then loaded 6.6.1 35x firwmare to aircraft, then ran launch wizard no issues AARs attached

### Alexander Alan Arnold, 2026-10-19

@Jeremy Kostel does this need to stay open? or can we close it since we should not be building 35x anymore and the cudtomer aircraft are being converted to adv nav?

### Jeremy Kostel, 2026-10-19

@Alexander Alan Arnold yeah ill go ahead and close. Known LEMB issues

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_V1057_B30N_20260914T220417Z.zip | archive | 7499 | 2026-09-14 | listed only |
| AAR_V1057_B35X_20260914T222436Z.zip | archive | 7763 | 2026-09-14 | listed only |
