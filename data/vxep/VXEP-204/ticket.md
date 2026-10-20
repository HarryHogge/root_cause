# VXEP-204: Create SCO Travelers for Trillium Payloads

- **Issue type:** Sub-task
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2023-11-30
- **Updated:** 2025-06-10
- **Resolved:** 2025-06-10
- **Reporter:** Nina Menon
- **Assignee:** Trevor Gronner
- **Creator:** Nina Menon
- **Parent:** VXEP-151 Current Trillium Payloads do not exist in vault

## Description

Basic Travelers need to be created to include Payload SCO, Case label application, and CfC.
C:\JAI Vault 1\Production eng\1 - System Checkout & Flight Test\1 - Travelers\
101-108863 - Peer Review
101-111696 - Peer Review
101-111027 - Peer Review

## Comments (2)

### Matt Philley, 2024-03-28

@Nina Menon FYI new Trillium going thru SCO now PN 101-111027

### Matt Philley, 2024-03-28

@Nina Menon on the new 101-111027 traveler a couple comments for us to discuss:

- There is a field for the retract mechanism PN and SN, but we are ordering this payload as an assembly, so I am not sure if the retract has its own SN or that we are interested in capturing that. Other PNs we order separately even though they are assembled… so it will be case-by-case if that section is needed or not.


- Can we add the following text to the Complete Closeout QC Inspection block:
- Verify Trillium PN and Description match vendor PN in the vault
- Trillium Description may omit the “-MGI” since the Mid Grade IMU we specify is their “standard” option and so they will only include the IMU configuration as part of their description if it is a “non-standard” IMU.
- Verify Edge label was applied matching the label template in the vault and with no wrinkles, bubbles, liftin edges, etc.
- If IUID labels are required verify those are present and correct

## Attachments (0)
