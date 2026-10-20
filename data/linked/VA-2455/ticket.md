# VA-2455: Mod Payload A-Kit "Gen 2" (originally "long term fixes")

- **Issue type:** Epic
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2025-02-12
- **Updated:** 2026-06-16
- **Resolved:** 2026-06-16
- **Reporter:** Greg Fryer
- **Assignee:** Tobi Ogunro
- **Creator:** Greg Fryer
- **Parent:** VXEP-1008 Mod Payload A-Kit Gen 2 design/release/test (Long term issue resolution)
- **Links:** is blocked by VA-2533 (Resolve and Release Mod Payload Standard antenna interface issue.); relates to VXEP-1074 (MOD-A Kit Cable, Connector and AHRS Issues)
- **Job Number:** J100078 - Sustainment: VXE-30

## Description

**BOM & Drawing Updates**


**Task 1: Fix Fastener Issues in MCM Connector https://jenaero.atlassian.net/browse/VA-2521**

Description:
- Update PN: 111-105025 to a new part number due to incorrect BOM references.
- Remove Items 21 & 22 from the BOM and replace them with PN: 2119692-01 (Spare Bolt Kit, MOD PAYLOAD Harness Connector).
- Update BOM 111-105201 to reference the new part number instead of 111-105025.

Subtasks:
Replace PN: 111-105025 with a new part number.Remove Items 21 & 22 from the BOM.Update Note #7 in 111-105025 to specify the use of 2119692-01 instead of existing hardware.Modify BOM 111-105201 (Item #3) to reference the new part number.Obtain engineering approval and release revised BOMs.**Task 2: Update Drawings for RF Harness Material Specification https://jenaero.atlassian.net/browse/VA-2550**


Description:
- The vendor Koaxis was not using the specified material in the drawings for:
- PN: 2120034-01 (RF HARNESS, PHASE MATCH, PAYLOAD, V2)
- PN: 2120010-01 (CENTERWING RIGHT RF HARNESS, PHASE MATCH, V2)
- Add a note specifying that equivalent material is acceptable.

Subtasks:
Modify PN: 2120034-01 and PN: 2120010-01 drawings to include a note:
"Equivalent material may be used, provided it meets the required performance specifications."Ensure note placement is clear and visible.Fill out NCRCommunicate changes to Koaxis and ensure vendor compliance.**2. RF Cabling & Connector Fixes**

**Task 3: Resolve RF Cabling Misalignment in MOD Payload Standard Antenna https://jenaero.atlassian.net/browse/VA-2533**


Description:
- The Array Antenna Mount (PN 111-105524) has an issue where connectors do not extend far enough, causing signal loss (dB drop) when interfacing with the Bloodhound Antenna Array.
- A new part number is required for the contact holder and RF cable assembly.
- The Wing Tip Antenna Array Mount is not interchangeable, so a new PN is needed.

Subtasks:
Redesign Contact Holder & RF Cable Assembly to extend male contacts outward.Assign new part numbers for the contact holder and RF cable assembly.Assign new part number for the Wing Tip Antenna Array Mount Assembly.Update BOMs and work instructions accordingly.**Task 5: Investigate AHRS GPS Timestamp Intermittency https://jenaero.atlassian.net/browse/VXEP-1138**


Description:
- The AHRS GPS unit intermittently fails to send GPS data in the correct 1PPS format for Bloodhound.
- Some SBG units work, while others do not.
- Investigation is required to determine whether this is a configuration or firmware issue.

Subtasks:
Review GPS unit logs & error reports.Compare working vs. non-working SBG units.Investigate possible configuration differences.Test with firmware updates or reconfiguration.

## Comments (1)

### Christa Meck, 2026-06-16

All related work is complete.  Marking this done.

## Attachments (0)
