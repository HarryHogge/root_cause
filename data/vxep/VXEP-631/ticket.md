# VXEP-631: VXE 458 Fuel cell anomalies and false firmware update notification

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed, but added to Bermuda Triangle List
- **Resolution:** Cannot Reproduce
- **Priority:** Highest
- **Created:** 2024-09-12
- **Updated:** 2026-08-14
- **Resolved:** 2025-04-15
- **Reporter:** Pat Wells
- **Assignee:** Ted Trowbridge
- **Creator:** Pat Wells
- **Labels:** MARSOC, Training, Weekly-incident-tracker
- **Customer:** MARSOC
- **Vehicle Tail Number:** 458
- **Other Stakeholder (as required):** Sean Wendling
- **Issue Status:** Data review in Progress
- **Root Cause:** Believed to be a firmware issue
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

Statement from operator: Frank
Attached are the flight logs from the flights that were getting the fuel valve % at 100% and the life % at 0%. I tried to download the fuel cell firmware to a fully assembled Stalker and the download was unsuccessful for multiple fuel cells and multiple times. It says that I need to be on XComm firmware 0x04000027 to be able to perform this update successfully. 

Operator also reported decreased endurance performance with Fuel Cell.
Operator received notification that fuel cell required firmware update which was incorrect.
Software version 6.3.4 
AAR’s attached

## Plan

- Data Review @Sean Wendling  FUEL CELL IS GOOD
- Determination of Airworthiness of Fuel Cell & AC
- Determination of Root Cause and Disposition for Repair
- Need to evaluate false firmware update notification
- Dave & Mike Berger to review why this is occuring.

## Comments (13)

### Pat Wells, 2024-09-12

@Sean Wendling @Alexander Alan Arnold FYSA

### Sean Wendling, 2024-09-13

Hey @Alexander Alan Arnold & @Pat Wells , Initial review shows that the fuel cell is healthy, and capable of producing 450W. When I look at the power need from the system, it appears relatively normal.
What is interesting, is that the system only recorded a burn of 645g of fuel, and the initial fuel weight was 868g. While it is not a guarantee that a fuel cell should fly for 8hrs in all scenarios, and I suspect that the flight conditions would inhibit a “Full” flight… it should have been able to fly at least another 1.25hrs. 
I remember in our phone call you mentioned that he said something about it only had “50g” remaining, can you refresh my memory on that? It could also be a miscalculation on entering the mass at the beginning of the run. The total mass of the tank (including tare) and the “tare” mass are necessary when entering the fuel. Could they have misreported here somehow?
Good news is I dont think they will need to return it. I will keep digging on my end, but if yoy have any more information that would be excellent!
Thanks, Sean

### Pat Wells, 2024-12-05

@Sean Wendling any updates on the path forward for this?

### Sean Wendling, 2024-12-10

@Pat Wells Hey Pat, this is a First Generation D450 Fuel Cell, I think that the GCS6.3.4 has been recommending fuel cell update by mistake. There is no new firmware for this fuel cell, and GCS should not be recommending for them to update. This will probably require someone on the GCS software side to review.
On the issue of Fuel Burn, I will try to dig a bit deeper for some recommended actions. I suppose this one got lost waiting to hear if there was any additional info they could provide.

### Sean Wendling, 2024-12-10

@Robert Redfield FYI

### Alexander Alan Arnold, 2025-01-10

@Sean Wendling Since we cannot provide any further information about the fuel cell flight can we potentially link the SW bug to this issue and move this to D6 since the root cause is a bug in the SW and the CA will a SW update? 

FYSA @Pat Wells

### Pat Wells, 2025-03-17

@Sean Wendling any updates on this?

### Sean Wendling, 2025-03-17

Hey @Pat Wells , I don't have any additional updates. I reached out to Dave back in September to see why this is like this. Given that the GCS software will be updating next week, I think that its probably safe to close out as I suspect that with the new GCS, we are wiping this issue. 
@David Grosher Have you heard this reported anywhere (fuel cell dialog offering a firmware update that isnt posted yet)? and if not, do you anticipate that GCS6.4.0 will address the concern in this ticket?

### David Grosher, 2025-03-17

@Sean Wendling @Pat Wells I’ll assign this to @Ted Trowbridge and we will address the GCS issue. I had not been tracking this issue.

### Sean Wendling, 2025-03-17

@David Grosher No problem Dave, it fell off my radar as well. Thanks!

### Alexander Alan Arnold, 2025-04-08

@Ted Trowbridge Any updates on this?

### Ted Trowbridge, 2025-04-09

It says that I need to be on XComm firmware 0x04000027 to be able to perform this update successfully.

@Alexander Alan Arnold All AARs provided on the ticket indicate the XCOMM version was 0x04000045 which satisfies the minimum version (0x04000027) required to update the FC firmware.  
 I tried to download the fuel cell firmware to a fully assembled Stalker and the download was unsuccessful for multiple fuel cells and multiple times.

Can we get clarification on what was done here?  Are the attached logs complete or was another vehicle being used with older XCOMM firmware?

### Alexander Alan Arnold, 2025-04-09

“ this is a First Generation D450 Fuel Cell, I think that the GCS6.3.4 has been recommending fuel cell update by mistake. There is no new firmware for this fuel cell, and GCS should not be recommending for them to update. This will probably require someone on the GCS software side to review.”

@Ted Trowbridge
Above is Seans comment from December 10th saying that the GCS should not be recommending SW updates. Since this was so long ago I do not believe we will be able to get any more data from the customer. I also believe this fuel cell may be involved with the current recall involving the improper calculations for fuel burn. 

I can ask Pat if he wants to put this in the Bermuda triangle and just close it.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V458_240907_084733_pack.zip | archive | 4711 | 2024-09-12 | listed only |
| T95_V458_240908_035626_pack.zip | archive | 649 | 2024-09-12 | listed only |
| T95_V458_240908_190214_pack.zip | archive | 744 | 2024-09-12 | listed only |
