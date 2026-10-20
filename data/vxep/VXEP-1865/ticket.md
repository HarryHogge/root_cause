# VXEP-1865: VXE 930 - Vehicle broke orbit, wouldn’t take commands and behaved erratically.

- **Issue type:** Incident (8D)
- **Status:** D4 - Investigating Root Cause
- **Priority:** Highest
- **Created:** 2026-04-24
- **Updated:** 2026-09-02
- **Reporter:** Michael Lindsay
- **Assignee:** Eric Brewer
- **Creator:** Michael Lindsay
- **Labels:** Hardware, MOLSON, RCCA, Weekly-incident-tracker
- **Links:** relates to RMA-972 (VXE-930 RMA 260421-3); relates to VXEP-1557 (VXE 930 Main battery to avionics power chain led to emergency landing); relates to VXEP-1987 (VXE 1016 Battery warning aircraft RTB)
- **Customer:** MOLSON
- **Vehicle Tail Number:** 930
- **Vehicle Configuration:** Adv Nav
- **Problem Type:** Discovered Issue
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

The aircraft was flying within a 5km radius and the aircraft was acting erratic, it broke its orbit and wouldn’t take operators commands.
Spoke with the operator, he stated that following a battery sway of the HLB and Main battery they launched the aircraft on its mission.  While on its mission it showed that the main battery was low and commenced a RTB, during the RTB the battery life with back to its normal percentage and returned to the mission.  This happened one additional time during this flight so the operators elected to land the aircraft.

## Plan

- Dave is out for a while, but someone from FS could verify. I am guessing that this was caused by the voltage issue in the linked ticket. This may be expected behavior for a voltage fault. @Eric Brewer  may be able to confirm.

## Executive Summary

Waiting on separate 930 investigation data to resolve, believed voltage issue is causing behavior. Probable cause Battery.

## Comments (7)

### Alexander Alan Arnold, 2026-04-24

@David Grosher This one along with another tail experienced issues at a MOLSON test event, evaluating for erratic behavior is a little outisde our wheel house right now on the team any way you could have someone look at this one?

There are currently three MOLSON tails that have been sent back for investigation/evaluation

### Alexander Alan Arnold, 2026-04-24

I see a lot of vehicle low packet percentage in the event log, how would be connected to the internet or some type of Wi-Fi network negatively impact communication with the aircraft?

### Alexander Alan Arnold, 2026-04-24

@Michael Lindsay Can you get an extended statement on the erratic behavior or is the main concern that aircraft broke orbit/didnt take commands

### David Grosher, 2026-04-24

This flight flew an orbit until a GoTO to IP1 was received. At which point it recovered as expected. 
[21:42:02.490 1564.490] GoTo m,w 1  0
@Alexander Alan Arnold is tracking down whether this is the correct dataset. 
[embedded: image-20260424-194351.png]

### Alexander Alan Arnold, 2026-06-04

@Stephan Johnson Please get this data loaded into the GS tool when able

### Stephan Johnson, 2026-08-31

@Cameron Chapman my bad. This is the correct AAR. Is there anything further you need from us on this?

### Eric Brewer, 2026-09-02

@Alexander Alan Arnold @David Grosher it looks like there was quite a bit of wind in this flight, I see groundspeed up to 90fps while airspeed is still around 54.  Is there a report of how high the winds were?

[embedded: image-20260902-144130.png]
In any case I agree it seemed like it tracked the orbit ok so I’m not sure what erratic behavior was observed.

[embedded: image-20260902-144221.png]

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T115_V930_260325_142612_pack.zip | archive | 1924 | 2026-04-24 | listed only |
| image-20260424-194351.png | image | 163 | 2026-04-24 | listed only |
| 930 Full Data Pull.zip | archive | 50558 | 2026-06-03 | listed only |
| image-20260902-144130.png | image | 34 | 2026-09-02 | listed only |
| image-20260902-144221.png | image | 45 | 2026-09-02 | listed only |
