# VXEP-27: TPTR-95 Dell adapters for SGCS2 Not working

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2023-08-23
- **Updated:** 2023-09-27
- **Resolved:** 2023-09-27
- **Reporter:** Allen Gardner
- **Assignee:** Greg Fryer
- **Creator:** Allen Gardner
- **Links:** is caused by GCSS-81 (Dell Adapter Send recommendation to LM for PTR closure. ); relates to ENGPRJA-50 (GCS Laptop configuration needs update and designation)
- **Customer:** TIQUILA
- **Incident Type:** Mission Failure/Abort
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

During TO1 STALKER FAT, the dell adapters for SGCS2 were not working as expected

## Corrective Action

Release part in vault that identifies only the latest version. Complete.
Complete CCB of that release. Complete.

## Root Cause

Because the Dell adapters were delayed, we ordered a couple from eBay. Unfortunately those turned out to be an older model that was not compatible with the SGCS1 Lind DC-DC converter and SGCS2 Lind PoE Injector. During FAT, we received the delayed Dell order and found that the latest model functioned properly. We replaced the older model with the new model into SGCS1-108, SGCS1-109, SGCS1-110, and SGCS2-52. No part number changes or BOM changes were required.

## Comments (2)

### Sam Miller, 2023-08-24

Because the Dell adapters were delayed, we ordered a couple from eBay.  Unfortunately those turned out to be an older model that was not compatible with the SGCS1 Lind DC-DC converter and SGCS2 Lind PoE Injector.  During FAT, we received the delayed Dell order and found that the latest model functioned properly.  We replaced the older model with the new model into SGCS1-108, SGCS1-109, SGCS1-110, and SGCS2-52.  No part number changes or BOM changes were required.

### Cameron Chapman, 2023-08-24

Recommend moving to closure following confirmation from LM of PTR closure request. Will be CCBd with laptop.

## Attachments (0)
