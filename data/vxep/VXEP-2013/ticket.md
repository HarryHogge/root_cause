# VXEP-2013: Vehicle 426 Repeatedly Lost GPS and Attempted Dead Reckoning

- **Issue type:** Incident (8D)
- **Status:** D2 - Gathering Information
- **Priority:** High
- **Created:** 2026-10-06
- **Updated:** 2026-10-12
- **Reporter:** Zachary Mann
- **Assignee:** Eric Brewer
- **Creator:** Zachary Mann
- **Labels:** Hardware, RCCA, Weekly-incident-tracker
- **Customer:** MARSOC
- **Part Number(s):** 426
- **Vehicle Tail Number:** 426
- **Vehicle Configuration:** VXE-30 (Block Series), Standard Battery, Advanced Nav
- **Problem Type:** Other (explain in description)
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround
- **Components (EA Aircraft):** Aircraft, full assembly
- **Executive Summary:** Repeatedly Experiencing Loss of GPS Causing Dead Reckoning

## Description

When initially started it will show anywhere between 19-25 satellites then around 3-5 minutes later it will lose all satellites and enter dead reckoning mode. 
2 days ago, the customer preflighted and launched without issue 3-5 minutes into the flight the gps' dropped out, dead reckoning occurred. I commanded an immediate rtb to land, it started heading home, regained link, entered landing pattern down to 300ft to enter vtol however a/c lost gps link again and overflew LZ. It then activated the emergency glide down landing all the while regaining and losing link with gps and now long range antenna connection. It eventually glide landed after a few iterations of sporadic antenna and gps link losses and direction changes. 
Also, about 3 weeks ago we were actively gps spoofed which also caused an emergency glide down landing so my initial thoughts were it was happening again but it appears that wasnt the case.

## Comments (3)

### Eric Brewer, 2026-10-06

@Zachary Mann @Alexander Alan Arnold it looks like the Novatel is stopping its outputs to the autopilots.  The reset logic is able to get it to come back for a short period but then it’s dropping out again.  Was this in theater?  If so it’s plausible there is something in the received signals that is messing up the novatel.  If we have access to the bird I’d like to recommend we request the debug data from the novatel (we have to connect to it via putty and issue some commands).  If those show a fault in the receiver we can have NovAtel provide some insight into why the receiver is not outputting data.

If there are no faults on the receiver then that might point to a hardware fault in which case the unit would need to be returned for rework.  Was the bird damaged in the glide landing or is it still in service?

Somewhat related, but if this happens again on this or another bird, ‘land immediately’ can be used in conjunction with manual nudge to get the vehicle down safely in the case of GPS loss.  It will not abort land immediately due to a GPS fault.  Operators may require training on manual nudge though if they don’t have it already.  @David Grosher @Scott Whitney FYI.

### Zachary Mann, 2026-10-07

@Eric Brewer I know @Alexander Alan Arnold pinged you. Working with him on next steps to get the data requested.

### Zachary Mann, 2026-10-12

Update 10/12/2026: Still awaiting information from Novatel

## Attachments (6)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| VTOL_VXE426 (0fbe671e-aac5-47ed-94e2-f911e0f51d53).zip | archive | 71546 | 2026-10-06 | listed only |
| XCOMM_VXE426 (0bb11c15-4115-487c-8194-495368c40c9e).zip | archive | 21410 | 2026-10-06 | listed only |
| XCOMM_VXE426.zip | archive | 21410 | 2026-10-06 | listed only |
| 77bb9579-266a-4cf5-8d70-f19e50926b99.jpg | image | 11 | 2026-10-12 | listed only |
| AAR_V918_B30N_20261009T171329Z.zip | archive | 45686 | 2026-10-12 | listed only |
| b9c3a0e6-c295-431e-baf0-44537f98d44b.jpg | image | 16 | 2026-10-12 | listed only |
