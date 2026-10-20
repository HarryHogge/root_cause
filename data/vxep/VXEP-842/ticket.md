# VXEP-842: VXE 601 Did not pause after Operator command during rapid landing

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-12-19
- **Updated:** 2026-03-02
- **Resolved:** 2025-02-19
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Pat Wells
- **Creator:** Alexander Alan Arnold
- **Labels:** TIQUILA, Weekly-incident-tracker
- **Customer:** TIQUILA
- **Vehicle Tail Number:** VXE 601
- **Vehicle Configuration:** VXE 30 standard fuel cell configuration
- **Corrective Action:** Follow published operating limitations.
- **Incident Type:** Aircraft Damage
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

TIQUILA
At the end of an uneventful sortie which was launched in order to re-set the currency of a Remote Pilot (RP) the final phase of the automatic vertical landing appeared more rapid than normal; the RP attempted to pause the landing but no response was observed in reaction to the command. The aircraft landed heavily and slightly left wing down. After landing it was noted that the video feed from the payload appeared to have a pink colouration;
 A post-flight check of the aircraft also identified that the aft landing pad appeared to be creased/compressed.
The surface wind measured by hand-held anemometer immediately prior to (and after) the landing (12 - 16 kts) was at the upper end permitted in the Operator's Manual (17 kts).
Prior to disassembling the aircraft all flying controls, motors and rotors were checked and were serviceable.
Operator Statement 

Movie of landing attached.

## Issue Status

Data review complete. Powerpoint updated. Awaiting final review from Pat on RCCA.
Aircraft in fuel cell configuration. HD55 payload (likely ~44-45lb TOW). Battery SoC trended down entire flight, likely due to winds and payload. 
Debug log contains two flights. Flight in question is 2nd, start time ~11:19:00
AP reported Winds aloft ~45fps (~30.5mph). This would be available on GCS to operator. Ops manual limitations are < 30mph. 
VTOL AP estimated winds during landing (not available to operator on GCS) ~40fps (27mph) at 40ft and 20fps (13.5mph) near landing altitude. ~15fps wind shear (loss of wind) occurred just prior to landing. 
No obvious lift system issues with regard to power.  
Landing pause was commanded after vehicle touched down. Both GCS and VTOL captured the command (ruling out a command not being sent/received). 
Files stored here VXEP-842 VXE601 Hard VTOL Landing

## Root Cause

Operator commanded pause after vehicle already touched down. Hard landing due to aircraft being operated at / exceeding published environmental (wind) limitations.

## Comments (14)

### Cody Smisek, 2024-12-20

@Alexander Alan Arnold I see that standard battery configuration was input into the details of this ticket. Any specific reason as to why? Looks like it was actually a fuel cell configuration. I went ahead and updated the details.

### Alexander Alan Arnold, 2024-12-20

@Cody Smisek Error on my part. Sorry.

### David Grosher, 2024-12-20

@Eric Brewer FYSA

### Cody Smisek, 2024-12-20

@Cameron Chapman @Hayden Jeanor 

[embedded image-20241220-190003.png]

### Cody Smisek, 2024-12-20

@David Grosher Not sure how we want to word RCCA on this. 
Had discussion with @Eric Brewer and @Everett Werner today regarding the flight. Concurred that VTOL controller tracking was not great, flight was very windy and pause commands occurred after landing.

### Pat Wells, 2025-01-02

@Cody Smisek & @David Grosher will we be able to provide a more detailed report for the customer?  I reviewed what has been created so far and it doesn’t appear to be finished.
@Alexander Alan Arnold FYSA

### David Grosher, 2025-01-02

@Cody Smisek Can you provide the following in the report: 
- Summary
- Timeline of the issue, correlate times from different logs.
- Possible contributing factors
- Data Analysis of each possible factor, draw specific conclusions from data plots and list key takeaways.
- Conclusion

We don’t want the customer to have to interpret data on their own. 
@Pat Wells @Eric Brewer FYSA

### Cody Smisek, 2025-01-06

will complete this morning.

### Alexander Alan Arnold, 2025-01-10

@Pat Wells Please review the report.

### Pat Wells, 2025-02-03

@Cody Smisek @David Grosher Could you please assist in answering the customer’s question below: 

From the data review conclusion what does the third statement mean?
‘VTOL rotor commands were saturated low during descent combined with poor attitude and vertical speed tracking which led to hard touchdown’
Was that a cause or an effect?

### David Grosher, 2025-02-03

@Pat Wells Wind during the VTOL phase of flight will lead to lift as the air moves over the wing. The result as the wind thresholds are met and/or exceeded will be that the lift system motors will saturate low resulting in degraded attitude control. If the wind is gusting or producing too much lift then the vertical speed control becomes degraded as well. To mitigate this issue we spill lift from the wings by pushing both ailerons up during the VTOL descent. But with enough wind this isn’t a big enough effect to counter act the lift from the wind. All of that is to say that it is an effect of the windy environmental conditions. 
@Cody Smisek FYSA

### Alexander Alan Arnold, 2025-02-18

@Pat Wells Anything else you need from this one or can we close?

### Pat Wells, 2025-02-18

@Alexander Alan Arnold We can close this out.

### Alexander Alan Arnold, 2025-02-19

closed, Operator error

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 20241217-Stalker Landing-O.MOV | video | 11455 | 2024-12-19 | listed only |
| 20241217-Training Mission Record.vmis | other | 4 | 2024-12-19 | listed only |
| T95_V601_241217_112505_pack.zip | archive | 3752 | 2024-12-19 | listed only |
| image-20241220-190003.png | image | 118 | 2024-12-20 | listed only |
