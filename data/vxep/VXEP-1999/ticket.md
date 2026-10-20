# VXEP-1999: B30 ADVNAV CANJAM CAN Issues

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2026-09-15
- **Updated:** 2026-09-18
- **Resolved:** 2026-09-18
- **Reporter:** Jeremy Kostel
- **Assignee:** Jeremy Kostel
- **Creator:** Jeremy Kostel
- **Links:** relates to XKIT-5172 (B40 CAN Issues Investigation); relates to VXEP-1880 (LEMB CAN EE Investigation); is fixed by FS2-5124 (Block 30 XComm : Mitigate XComm and BMS using the same CAN frame IDs, leading to bus errors)
- **Issue color:** green

## Description

Sharepoint Folder
Updated Description (proposed)
During CANJAM, internal assets V797 and V945 reported significant CAN health degradation on every flight. Updated prerelease firmware (6.81) logged CAN health messages on both the VTOL AP and XCOM, with XCOM showing sustained transmit difficulties throughout the event.
Subsequent testing has shown that this issue is not isolated to CANJAM assets. The problem appears to exist across all B30 platforms — including Standard, Advanced Nav, and UAP configurations.
Recent flight testing and bench evaluations across multiple B30 platforms identified recurring CAN bus errors whenever the HLB Smart Battery (BMS) was present. Initial suspicions included hardware noise, BMS protection components, or general electrical sensitivity. However, focused firmware analysis and bench testing isolated the underlying cause to a CAN message timing conflict between the XCOM and the BMS.
Both systems were transmitting on the same CAN message ID (0x5000). Because the BMS sends a reply immediately after XCOM sends a command, overlapping transmissions on the same ID occasionally occurred. When this happened, the bus interpreted the overlap as a bit‑level error, leading to bursts of CAN faults and occasional transmit lockouts (“bus‑off” events).
Testing confirmed that the root issue was not hardware‑related and not caused by the prior TVS diode concern. The problem originated from the XCOM firmware behavior, which sent multiple SmartBatt commands back‑to‑back once per second. This created tightly spaced BMS replies, increasing the probability of collisions on ID 0x5000.
A firmware change is now being implemented that staggered these SmartBatt commands, spacing them evenly rather than sending them together. Bench and platform testing shows that this update significantly reduces CAN error activity and resolves the immediate operational issue

## Corrective Action

See SW/FW ticket: [FS2-5124] Block 30 XComm : Mitigate XComm and BMS using the same CAN frame IDs, leading to bus errors - Jira

## Plan

- Firmware Fix Validation (Complete)
The XCOM SmartBatt command timing has been updated in test code to stagger periodic commands and avoid reply collisions on CAN ID 0x5000. Bench testing confirms CAN stability under the new timing.
- Cross‑Platform Confirmation (Complete)
Testing on B30 Standard, Advanced Nav, UAP, and the Advanced Nav Iron Bird shows consistent improvement and no recurrence of the prior CAN error pattern.
- Remaining Technical Work (Tracked Separately)
Additional protocol cleanup and long‑term recommendations (e.g., dedicated reply ID, removal of unused ack‑matching logic) are documented and tracked under a separate engineering ticket.

## Issue Status

Remaining work tracked in software ticket: [FS2-5124] Block 30 XComm : Mitigate XComm and BMS using the same CAN frame IDs, leading to bus errors - Jira

Status: Resolved
Severity: High (during initial discovery)
Reproducibility: 100% with prior firmware; no recurrence with updated timing
Scope: All B30 platforms, confirmed on both aircraft and bench setups
Root Cause: XCOM and BMS both using CAN ID 0x5000, causing occasional timing collisions when SmartBatt commands were sent in back‑to‑back bursts
Corrective Action: Implemented staggered SmartBatt command timing in XCOM firmware (details in linked technical ticket)

## Root Cause

A timing conflict on CAN ID 0x5000 caused occasional collisions between XCOM commands and automatic BMS replies. The prior firmware sent multiple SmartBatt commands back‑to‑back, creating tightly spaced BMS responses and triggering CAN bus errors. Updating the XCOM firmware to stagger these commands resolves the issue.

## Comments (3)

### Eric Brewer, 2026-09-15

[embedded file]
Lab data (ground power) for V689.

### Jeremy Kostel, 2026-09-15

Here are two CAN recordings from an Advanced Nav vehicle currently in the shop. The aircraft has no booms, wingtips, or tail installed, which should not impact this test since the B30 platform does not route CAN to those locations.
Recording details:
- First recording: Powered only by the bench supply (no batteries in the loop). This log is completely error‑free.
- Second recording: Powered from batteries with the HLB smart connector connected. This log does show CAN errors.

During CANJAM, the buses were saturated with errors even on the ground, so the presence of errors in the battery‑powered configuration here may be an early indicator of the same behavior.[embedded file] [embedded file] 
[embedded image-20260915-202020.png]

### Jeremy Kostel, 2026-09-15

Here is a roughly 10 minute long log from the B30 advanced NAV iron bird with the HLB smart connection connected
[embedded file]

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| B30_IB_With_HLB_L1.asc | other | 34453 | 2026-09-15 | listed only |
| U_AAR_V689_B30N_20260915T185606Z.zip | archive | 57424 | 2026-09-15 | listed only |
| V686_No_HLB_CANlog.asc | other | 9045 | 2026-09-15 | listed only |
| V686_With_HLB_CANlog.asc | other | 4554 | 2026-09-15 | listed only |
| image-20260915-202020.png | image | 58 | 2026-09-15 | listed only |
