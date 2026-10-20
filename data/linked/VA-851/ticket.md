# VA-851: VXE450 Implement CA: Proposed Lift ESC Board Updates

- **Issue type:** Task
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Medium
- **Created:** 2023-11-20
- **Updated:** 2025-06-02
- **Resolved:** 2025-06-02
- **Reporter:** Connor Peebles
- **Creator:** Connor Peebles
- **Labels:** 1711P01-Lift_ESC, 1711P01D-Lift_ESC
- **Links:** blocks VXEP-51 (Internal - Aircraft 450 VTOL Landing Crash - ESC soft start)

## Description

[embedded: corrective.JPG]
- Short term design updates to consider:
- 30V limit version of U1
- In the case that VBATT is applied (as per this incident). The current design is 25V max limited.
- Reverse current bypass Schottky diode
- So reverse current does not pass through  the inside of the IC U1. 1.
- RC Snubber circuit across the starter MOSFETs
- Suppress voltage transients across starter MOSFETs.
- Starter MOSFETs only switch on startup, so this update won’t draw excess power and heat. 2.

## Comments (1)

### Cameron Chapman, 2023-11-20

@Connor Peebles great work on this investigation. With the cascading failures, I don’t think a 30V version of U1 would have kept the ESC alive. We could evaluate the likelihood of it helping, as it’s an easy change, but the effort may be better spent qualifying the VXE2024 ESCs for VXE30.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| corrective.JPG | image | 255 | 2023-11-20 | listed only |
