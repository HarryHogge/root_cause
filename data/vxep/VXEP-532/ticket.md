# VXEP-532: VXE 551 Significant HLB state of charge drop with fuel cell

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-08-12
- **Updated:** 2025-03-20
- **Resolved:** 2025-03-20
- **Reporter:** Pat Wells
- **Assignee:** Sean Wendling
- **Creator:** Pat Wells
- **Labels:** Edge_Asset
- **Links:** is cloned by VXEP-533 (VXE 551 software crashed while trying to create a racetrack orbit in flight)
- **Vehicle Tail Number:** 551
- **Vehicle Configuration:** Fuel cell
- **Other Stakeholder (as required):** Greg Fryer
- **Root Cause:** Under investigation. Related to A/C power need increase due to Environment or Operational factors.
- **Incident Type:** Mission Failure/Abort
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

Edge FLOPS asset being operated at live demo/exercise

Statement from Operator:
Aircraft 551 with fuel cell config lost significant HLB percentage, 98% to under 60%, during a short 30-45 min timespan, with no significant changes in environmental factors (wind speed and direction) or flight path. The aircraft also flew for roughly 3 ½ hours before this occurred. This issue

Also on this flight, the software crashed while trying to create a racetrack orbit in flight. We had to manually exit the software to reconnect to the aircraft. (created separate incident for this https://jenaero.atlassian.net/browse/VXEP-533 )

Secondary Minor Occurrence Incident - 8/12/2024 - Observed by AA FC Engineer
This issue occurred again where HLB drained from >95% to approximately 68% requiring team to reduce altitude and change the flight plan to reduce power requirement and allow HLB to reach safe level. Unknown at this time if the HLB was the same SN, but should be noted for this investigation. (reported by @Sean Wendling )
AAR attached

## Plan

- Data review. @Sean Wendling Look especially at fuel cell output produced vs aircraft power demanded.
- @Pat Wells can you please request an inspection of the HLB contacts post incident?
- “aircraft also flew for roughly 3 ½ hours before this occurred” was this on the same or a different flight? Logs indicate it was the same flight.
- “the software crashed while trying to create a racetrack orbit in flight” when did this happen in reference to HLB power drop? Before, during, after?
- Is the operator alerted when the average power is higher than the fuel cell output for an extended time? Should they be? Seems like it would be useful for instigating important troubleshooting or RTBs.

## Issue Status

Data Review in progress. Confirmed Fuel Cell & Battery functioning as necessary. Aircraft apPower at a heightened state of output requirement resulting in reduction of HLB charge status.
Data captured in powerpoint here.

## Comments (16)

### Pat Wells, 2024-08-12

@Sean Wendling  FYI fuel cell related issue.  Edge asset

### Sean Wendling, 2024-08-13

Hey @Pat Wells , is this ticket from Northern Strike Exercise??
I was just up there yesterday… lol. I will review the data today and get back to the team about options. I was flying yesterday when a similar situation occurred and I noticed the on demand power requirement was super high unexpectedly (No changes to wind speed or altitude). We may have to be cross function in the investigation. Thanks!

### Sean Wendling, 2024-08-13

@Dana Holley Hey Dana, with the HLB drain issue we had yesterday, I want to evaluate this alongside the instance from earlier in the exercise. When you have time, could you please add the AAR? I just want to see if it was the same HLB and see if I can find out why the A/C required so much power all of the sudden. Thanks!

### Dana Holley, 2024-08-13

@Sean Wendling Pat Wells should have this for you!

### Cameron Chapman, 2024-08-13

@Sean Wendling to add details of what he witnessed at the flight. He mentioned fuel cell was making normal power, but aircraft was demanding more for some reason. Sean, were there any abnormal weather conditions, like wind, climb.

### David Grosher, 2024-09-04

@Eric Brewer Can you look into the increased power demand. The hardware has checked out OK.

### Eric Brewer, 2024-09-05

@David Grosher added a few plots here.  I did not note any significant differences in throttle setting or flight condition that would explain the battery drain.

### Pat Wells, 2024-12-05

@Sean Wendling do we have any further updates on this?

### Sean Wendling, 2024-12-10

Hey @Pat Wells , I reviewed this data back a few months ago, and I saw that the fuel cell was operating normally, but the aircraft apPower was elevated in the time periods that the HLB% dropped. I am not sure what caused the increase in the needed power at that point, but as far as I can tell, the Fuel Cell and Battery were operating normally in both cases.

### Sean Wendling, 2024-12-10

@Robert Redfield FYI

### Pat Wells, 2024-12-10

@Everett Werner FYI See Sean’s latest comment.

### Everett Werner, 2024-12-10

@Pat Wells @Sean Wendling 
[embedded image-20241210-202509.png]
There is a noticeable increase in the power integral (graph 2) during the time which we see the battery state decreasing (graph 3)
The fuel cell is outputting full power during the time when the battery state is decreasing so I believe that the fuel cell is ok.
The amount of wind measured by the aircraft increases throughout the flight, I think it's possible that there is a downdraft, and more power is being required to maintain altitude. The integral indicates that the vehicle is having a hard time maintaining altitude due to a constant low pressure.
[embedded image-20241210-203423.png]

### Alexander Alan Arnold, 2025-01-10

@Sean Wendling  @Everett Werner Based on the traffic below are we saying the fuel cell does not need to be investigated and we are ready to assign this to a different engineer to investigate something else on this one? This seems like a training deficiency/operator error and this should be moved to D8 and close it out. 

FYSA@Pat Wells

### Everett Werner, 2025-01-10

@Alexander Alan Arnold It appears to be environmental effects to me, increase in required power to fly.

### Alexander Alan Arnold, 2025-01-10

I agree which points to a training deficiency in understanding the proper way to utilize the fuel cell config. So the hardware is preforming as expected in adverse wind conditions. Operators need to monitor wind and demand on the battery to implement better practices during windy conditions. @Everett Werner @Sean Wendling @Pat Wells

### Sean Wendling, 2025-03-17

@Pat Wells  Can this be closed or re-assigned? At this point, appears that the latest investigation efforts are directed at understanding why the aircraft needed more power and overwhelmed the available output from the fuel cell. and that seems to be resolved as well.

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V551_240809_121102_pack.zip | archive | 5595 | 2024-08-12 | listed only |
| newplot (15).png | image | 114 | 2024-08-20 | listed only |
| image-20241210-202509.png | image | 396 | 2024-12-10 | listed only |
| image-20241210-203423.png | image | 137 | 2024-12-10 | listed only |
