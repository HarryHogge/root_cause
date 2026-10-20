# VXEP-722: NVIDIA sent us a PCN about new memory

- **Issue type:** Problem
- **Status:** Assigned
- **Priority:** Medium
- **Created:** 2024-10-15
- **Updated:** 2025-12-16
- **Reporter:** Greg Fryer
- **Assignee:** Craig Burton
- **Creator:** Greg Fryer
- **Links:** relates to ENG-3604 (DRAM Update to Jetson Orin NX 16GB AI Computer); relates to MS-871 (MCM:  Evaluate Hadron-DM carrier board)
- **Issue color:** purple
- **Production Stakeholder:** Desiray Johnston
- **Supply Chain Stakeholder:** Perry Richardson
- **Other Stakeholder (as required):** Trevor Gronner

## Description

NVIDIA sent us this document about new memory on the board, and requests agreement within 30 days. or at 90 days they default to acceptance. Impact starts Jan 1 2025.

## Comments (16)

### Greg Fryer, 2024-10-15

@Craig Burton logged this here, we still have several weeks to respond.

### Craig Burton, 2024-10-18

ConnectTech will be releasing a BSP (board support package) for JetPack 5.1.4 in order to support the new DRAM from NVIDIA.  I followed up with a question about the ETA of the BSP and will update this ticket when I hear back.
[embedded file]
FYSA @David Grosher @Trevor Gronner @Jo Brown

### Craig Burton, 2024-10-18

Response regarding ETA from ConnectTech:
Unfortunately no I do not have an ETA at this time. According to the PCN from NVIDIA the new modules will not start shipping until Jan 1, 2025. We would need one of the new modules in order to fully validate that the new BSP is working properly, so it likely would not be until sometime after this date that we would be able to release a BSP.

@Greg Fryer

### Greg Fryer, 2024-10-18

@Craig Burton (And @Perry Richardson in case my guess is right):
Does this mean that we have a project to execute the following:
- We need to make sure we have enough hardware in hand by 01 Jan 2025 to get through # months (# = 3 or some other number).
- We have a project to do in conjunction with ConnectTech, so that anything we get after 01 Jan can work. We either need to ask them for a guess, or make a guess.

If I’m right, we need @Perry Richardson to take care of #1, with an agreed assumption, and likely @Scott Whitney to set up the project for tracking #2.
@David Grosher @Kenneth Weber FYSA.

### Perry Richardson, 2024-10-18

@Greg Fryer @Craig Burton @Kenneth Weber  As of today looks like we have supply to cover demand until May 2025.
| 100-117448-01 | NVIDIA JETSON ORIN NX | 900-13767-0000-0A0 |
| Stock | 126 |  |
| Open PO | 90 |  |
| Total Supply | 216 |  |
|  |  |  |
| Demand | 52 |  |
| Retrofits | 49 | Not sure if this is part of the 52. |
| Total Demand | 101 |  |
|  |  |  |
| Avg Demand/Mth | 12 |  |
| Supply/mths | 8.4 |  |
|  | Supply until- May 2025 |  |

### Craig Burton, 2025-01-29

I reached out to ConnectTech for an update.  They do not have the BSP available yet.
I unfortunately still do not have a firm date on when we will be releasing a JetPack 5.1.4 BSP for Orin-NX. However I can confirm that this is in our software teams queue and they are looking to get a BSP out since these new modules have started shipping.

I receive updates on their BSP mailing list, so I will report back when I get any updates or reach out for another one directly.

### Craig Burton, 2025-01-30

I followed up with the question “do you believe the BSP will be available prior to the end of March?” and this is the reply:

I am currently trying to get a more accurate answer for you but yes we should be able to release a JetPack 5.1.4 BSP before the end of March. I will keep you updated once I have more information.

### Craig Burton, 2025-03-10

ConnectTech has provided us with a download link for their BSP for Jetpack 5.1.4, which supports this manufacturing change.  Following Edge testing (as yet undefined), we will need to incorporate it into our Production image prior to utilization of any of the new boards.
FYSA @David Grosher @Scott Whitney @Jo Brown

### David Grosher, 2025-03-10

@Trevor Gronner @Desiray Johnston I wanted to make sure you are tracking this. 
@Perry Richardson Are these boards isolated from the previous deliveries? Maybe this is a question for production.

### Perry Richardson, 2025-03-10

@David Grosher Last delivery was 12/27/2024. Nvidia was not supposed to ship with the memory after Jan. 1st 2025. Will Check Inventory with date code. Need to get with Nvidia on label marking for new version

### Trevor Gronner, 2025-03-10

@Luca Lauritzen @Nina Menon FYSA, NVIDIA is sending us boards (100-117448-01) with new memory. In the document attached, they state that you can tell if the board may be impacted by the 699 level part number ending a number greater than or equal to 302. We may receive mixed shipments that have both the old and new memory. Any boards with the new memory will require a process change (assuming it all passes software testing).

### Trevor Gronner, 2025-03-13

@Catherine Wagner @Nigel Goodison It looks like 100-117448-01 has a change (new memory) that may impact new shipments coming in. We don’t have a specific cut in date from the vendor and they warned that we may get mixed shipments.  In the document attached, they state that you can tell if the board may be impacted by the 699 level part number ending a number greater than or equal to 302. Is there any way we can flag this part number so that any parts that come through receiving inspection are quarantined until engineering has a chance to test and approve the change?

### Catherine Wagner, 2025-03-13

@Trevor Gronner @Perry Richardson  Procurement can flag it FAI and I will keep them segregated. Do we know if current inventory is the old or new?
FYA@Nigel Goodison

### Trevor Gronner, 2025-03-13

@Catherine Wagner We believe current inventory is the old memory since it arrived in December 2024 (before the supplier date given for the soonest possible time we would see the new memory). I haven’t had time to go check the boards to confirm, yet.
@Nigel Goodison @Perry Richardson FYSA

### Perry Richardson, 2025-03-13

@Catherine Wagner @Nigel Goodison @Trevor Gronner @Luca Lauritzen @Nina Menon  Sent the supplier(Arrow) a picture of the barcode(the only to determine if old memory or new memory) on a board we have in Inventory. With this Arrow was able to confirm that this board is with the Old Memory .                                                                                                                                                            
FROM ARROW:
Here is the decoded data:
DATAMATRIX: 1613024600330,48B02DFB92FF,699-13767-0000-301,161-0546-10X
From the part marking specification, the format is:
[embedded 117448-01.png]
In short, the 699 level PN on this specific module is 301. Hence, this is an older module without the new DRAM mentioned in the PCN.

### Perry Richardson, 2025-03-13

@Catherine Wagner @Nigel Goodison @Trevor Gronner @Luca Lauritzen @Nina Menon  Just a FYI. Our shipment is due here in May. Changing PO’s to FAI so Catherine can hold in QA.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [PCN211361_NDA.pdf](attachments/23959_PCN211361_NDA.pdf.md) | pdf | 2107 | 2024-10-15 | converted |
| [RE NVIDIA Orin NX 16GB - DRAM product change notice.msg](attachments/24052_RE%20NVIDIA%20Orin%20NX%2016GB%20-%20DRAM%20product%20change%20notice.msg.md) | msg | 92 | 2024-10-18 | converted |
| 117448-01.png | image | 69 | 2025-03-13 | listed only |
