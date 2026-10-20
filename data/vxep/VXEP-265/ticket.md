# VXEP-265: VXE-606 Odd VTOL behavior during SCO/ Flight test

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2024-02-01
- **Updated:** 2026-03-02
- **Resolved:** 2025-08-05
- **Reporter:** Eric Brewer
- **Assignee:** David Grosher
- **Creator:** Eric Brewer
- **Labels:** TIQUILA
- **Links:** clones VXEP-263 (VXE-604 crash during SCO/ Flight test); relates to VXEP-263 (VXE-604 crash during SCO/ Flight test); relates to FS2-1407 (v606 VTOL Altitude loss investigation); relates to FS2-1423 (Explore vertical channel improvements to reduce effects of baro transients during VTOL flight.); relates to VA-1261 (Explore potential hardware modifications to improve baro sensor measurements in the presence of VTOL rotor wake.)
- **Customer:** TIQUILA
- **Vehicle Tail Number:** 604
- **Vehicle Configuration:** Battery
- **Production Stakeholder:** Artis Bertulis
- **Other Stakeholder (as required):** Matt Philley
- **Problem Type:** Other (explain in description)
- **Issue Status:** Complete
- **Incident Type:** Aircraft Damage
- **Severity:** 4 - Annoyance

## Description

Vertical flight phases of this vehicle seemed odd and unusual when compared to other vehicles in the same weather conditions. There were climbing hiccups during the first take-off, transition for the first landing made it loose over 70ft altitude (230ft), then climbing back to 300 ft and starting the landing sequence. Landing and landing pause for the 3rd flight seemed unstable and jumpy.
Aircraft: AC 606 new production aircraft
HLB: ??
Main Battery: ??

AAR files attached
Mishap report link: AC606Investigation.pptx
File location:Flight Safety - VXE 606 Odd VTOL Behavior - All Documents (sharepoint.com)

NCR: NCR List - AC 606 - Flight Test - odd VTOL behaviour (sharepoint.com)

## Corrective Action

- If the errors are of similar magnitude to those seen on this flight, I do not see this as a flight risk. The errors occur higher up off the ground, whereas the autopilot will be using the laser AGL measurement closer to the ground.
- No additional steps beyond what is listed below.

Explore potential improvements to vehicle vertical channel in critical phases of flight:
- Software modifications to improve sensor fusion and select the right sensors in the right phase of flight - https://jenaero.atlassian.net/browse/VXEP-269 
- Hardware modifications to improve baro measurement in the present of VTOL rotor wake. https://jenaero.atlassian.net/browse/VXEP-270

## Plan

- Please do the following:
- Let us know if you think this ADP could be a flight risk, or if it more likely just might lead to odd behavior or was caused by unique conditions.
- Any additional steps for this data or incident. CA tasks will be tracked in those separate tasks.
- Let us know if any of the CAs seem urgent and need to start.
- Let us know if you think this is ready to close.

I will close the AP NCR.

## Root Cause

Unstable flow of rotor wake causes inaccuracies in baro altimeter measurements when VTOL rotors are active.  The problem did seem worse with 606 and seemed to improve with a new VTOL AP.

## Comments (33)

### Cameron Chapman, 2024-02-05

@Eric Brewer @David Grosher do you have any updates for this aircraft? Can you please update the plan and status fields? Do you think this is caused by processor loading or something more hardware related? Would you recommend grounding this aircraft or continue with SCO/delivery?

### Eric Brewer, 2024-02-05

@Cameron Chapman thanks for reaching out, see issue status.  It appears this is related to a known issue with the altitude system.  @John Clark  is helping to track down the original issue to understand the disposition.  It’s either:
a) local pressure disturbances cause baro alt to be unreliable in certain wind/flight conditions
b) there is a hardware issue with the baro sensor
c) some combination.

### Cameron Chapman, 2024-02-05

@Carson Buckley @Artis Bertulis has any testing of the ADP been performed since this incident happened? Could we perform some pressure tests if not to test the hardware?

### Cameron Chapman, 2024-02-05

@Eric Brewer it seems like the issue was worst during VTOL. Does that match your analysis? If so, we should compare to relevant data like current, vibration, etc. It could be due to EMI, vibration, airflow from VTOL, etc. 
After the initial ADP test, we could perform a tether test to see if we can duplicate the issues.

### Eric Brewer, 2024-02-06

That’s right - definitely worse during VTOL.  I did take a look at a wider swath of reference flights, my take is that the issue is probably more fundamental - it seems like local flow from the rotors is disrupting the air around the static port.  Are you able to provide some pictures and/or specs of how it’s installed on the airplane?  That could provide clues as to why some flights are worse than others.
See plots here of a VTOL flight on a windy day for some comparison (from T95_V605_240125_105327_pack)
[embedded: image-20240206-131148.png]

### Matt Philley, 2024-02-06

@Cameron Chapman ADP checkout is performed per Doc# 111270 ADP Checkout procedure. If we repeat that would that cover the data you are interested in? We usually collect the following info
[embedded: image-20240206-155137.png]

@Eric Brewer 
The static port is located on the 107-101141 Air Data Pod
The Air Data Pod is installed on the 107-100455 Center Wing Assembly
I dont have the greatest pics at the ready, but I can grab a quick measurement in a few, but if you are not familiar here is the position in the aircraft
[embedded: image-20240206-155308.png]
[embedded: image-20240206-155524.png]

### Carson Buckley, 2024-02-06

@Cameron Chapman @Eric Brewer @Matt Philley AAR has been added after performing a Launch Wizard and powered hover test. No anomalies were noted in ADP operation (visually).
Also added: Right boom was noticed to have a creak when manipulated. It sounds like the split washers on the retaining screws, so may not be a contributing issue, but thought it was worthwhile to mention.

### Eric Brewer, 2024-02-06

@Carson Buckley thanks.   I took a look at the data, I don’t note any anomalies in the baro data here.

### Cameron Chapman, 2024-02-06

@Matt Philley performing that procedure would be great. Thank you. 
@Matt Weber should the issue Carson mentioned below be addressed? 
@Carson Buckley thank you for the hover test. We may want to repeat a full power tether test. as hover is much less power and likely less vibration.

### Matt Weber, 2024-02-06

@Carson Buckley @Cameron Chapman I checked out the creaking, and it looks like a resin/adhesive/paint/primer buildup along the skin, resulting in a slightly uneven surface on the center wing edge where the boom mounts.  A minor issue and very unlikely to be contributing to this behavior.

### Eric Brewer, 2024-02-07

Updated powerpoint and description with conclusions and next steps.  I’m inclined to close this investigation and we can pursue https://jenaero.atlassian.net/browse/VXEP-269 and https://jenaero.atlassian.net/browse/VXEP-270 as time permits to improve the vertical tracking of the fleet.  @Matt Weber @Cameron Chapman @Carson Buckley @Matt Philley @David Grosher

### Cameron Chapman, 2024-02-07

Thank you @Eric Brewer . Moving to closure. @Matt Philley 606 is approved to resume the normal process.

### Cameron Chapman, 2024-02-07

@Eric Brewer tasks for VXE hardware usually go into the VA project (so they can be inserted into sprints). Software into FS. VXEP is problem project (kanban flow) You should change the issue type of the CAs to something like improvement.

### Matt Philley, 2024-02-07

@Cameron Chapman @Eric Brewer what is the disposition and justification for the aircraft so we can update the NCR? From the presentation it just says:
- CAN Baro altitude shows significant discrepancies from LRF and GPS altitude estimates​
- Especially bad when in VTOL flight​
- Especially bad during transition or in wind​
- This does not appear to be a new issue, and is fundamental to how the baro sensor measures pressure around the unstable flow from the rotors


So it is a known issue, but it does not say “this aircraft is OK because….” which we need in order to approve the release of this aircraft. For example, does this known issue pose a risk for flight for Customers or does this aircraft have any more risk than any other aircraft…? Do other sensors or controls in the aircraft ensure this will not cause a crash during VTOL in wind for a Customer...?

### Eric Brewer, 2024-02-07

@Matt Philley I added a note in the powerpoint, @Cameron Chapman @David Grosher let me know if you agree.

[embedded: image-20240207-155032.png]

### Cameron Chapman, 2024-02-07

@Eric Brewer @David Grosher @Everett Werner your groups could better answer this question, but I imagine the LRF, magnetometer, and GPS position take a larger role in controlling VTOL. Is that correct? Could baro inaccuracies like this during VTOL increase the chances of a crash, especially if another sensor has an issue (trying to determine how urgent the fixes are)? 
I agree that since this aircraft shows no different risk than others we have already shipped, it should be ok to continue. @Matt Philley

### Matt Philley, 2024-02-07

@Eric Brewer @Cameron Chapman dig it! thanks for the support. NCR has been closed and AC606 will be moving forward in Production.

### Eric Brewer, 2024-02-07

@Cameron Chapman good question.  As a first step of exploring the vertical channel improvements we need to map out exactly what the logic is today.  Near the ground I believe we’re relying more heavily on the laser altimeter.

### Ruysser Gabler, 2024-02-13

606 was flight tested again yesterday on the 12th. On 3rd flight the transition behavior was weird again. Climbing and descending multiple times at start of transition and seemed to wander a lot in the air again. @Cameron Chapman @Eric Brewer AARs are attached
[embedded: T95_V606_240212_121117_pack.zip][embedded: T95_V606_240212_115405_pack.zip][embedded: T95_V606_240212_113229_pack.zip]

### Matt Philley, 2024-02-13

Copied from comment from Ryan S in NCR 2350
@Sam Miller watched the videos and suggests we swap out the VTOL controller and re-fly to see if it still has the issue. Let's hold on closing it up and try this. @Cameron Chapman @Matt Philley @Kyle England @Artis Bertulis @Ruysser Gabler @Eric Brewer

### Eric Brewer, 2024-02-13

The logs show similar discrepancies in baro alt vs. GPS, and were actually a bit worse on this past flight than the previous logs.  Can we inspect the air data system to see if anything is notably different?  
If not I’d recommend swapping out the air data unit. @Sam Miller @Cameron Chapman @Matt Philley @Kyle England @Artis Bertulis @Ruysser Gabler 
[embedded: image-20240213-201044.png]

### Eric Brewer, 2024-02-13

@David Grosher fyi.

### Eric Brewer, 2024-02-13

@David Grosher I did look through the code, there is some 1D fusion that can be done on the altitude estimate that would probably clean up a lot of the transients in flight, but it looks like it’s commented out in the code and maybe not plumbed up.
This is something we could try to enable and test once the UDP HIL is up and running.

### Artis Bertulis, 2024-02-19

Vehicle was flown last Friday with the VTOL AP replaced. All 3 flights were normal, performed the same as other aircraft that day. ADP did not get replaced. From flight OPS side I consider this vehicle as safe to fly. @Eric Brewer @Matt Philley

### Eric Brewer, 2024-02-19

Thanks @Artis Bertulis .  Let me know if there are data logs available that you’d like me to look at.

### Artis Bertulis, 2024-02-19

@Eric Brewer added the AARs to the ticket

### Eric Brewer, 2024-02-19

Thanks @Artis Bertulis .  Agreed the logs look much better.  I am not entirely clear on why replacing the VTOL board without the air data system would have improved things since the errors seemed to be in the CAN baro measurements.

### Matt Philley, 2024-02-19

@Eric Brewer ya its very odd… but everything seems to be performing more normal, so we will go ahead and close the NCR for this aircraft.
The removed avionics board assy will get its own NCR and be available for troubleshooting. @Ryan Ferguson FYSA as well.

### Matt Philley, 2024-02-19

NCR 2524 generated for removed SN T-S100267 Avionics Board Assy
Avi Board Assy - Odd VTOL Behavior from AC 606 - Detail NCR

### Eric Brewer, 2024-04-05

@Cameron Chapman @Matt Philley I saw the question above about what to do with the VTOL AP.  As the issue appears from the logs to be related to the baro sensor I’m at a loss as to why the autopilot swap fixed the issue, or what to investigate with the AP next.

### Cameron Chapman, 2024-04-08

@Eric Brewer agreed. It seems to have been replaced as a quick fix attempt without looking at the data in detail. If any hardware needed inspection, it would have been the ADP, which has shipped. Please do the following: 
- Let us know if you think this ADP could be a flight risk, or if it more likely just might lead to odd behavior or was caused by unique conditions.
- Any additional steps for this data or incident. CA tasks will be tracked in those separate tasks.
- Let us know if any of the CAs seem urgent and need to start.
- Let us know if you think this is ready to close.

I will close the AP NCR.

### Eric Brewer, 2024-04-08

@Cameron Chapman 
- If the errors are of similar magnitude to those seen on this flight, I do not see this as a flight risk.  The errors occur higher up off the ground, whereas the autopilot will be using the laser AGL measurement closer to the ground.
- No additional steps beyond what is listed above.
- Given 1) I do not think this is urgent with the data I have available at this time.
- I am OK to close this.

### Christa Meck, 2025-08-05

Closing this incident as it’s from Feb 2024 and any investigation is likely done at this point.

## Attachments (14)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V606_240206_073545_pack.zip | archive | 1130 | 2024-02-06 | listed only |
| VXE606 RBoom Creak.mp4 | video | 36350 | 2024-02-06 | listed only |
| image-20240206-131148.png | image | 152 | 2024-02-06 | listed only |
| image-20240206-155137.png | image | 18 | 2024-02-06 | listed only |
| image-20240206-155308.png | image | 43 | 2024-02-06 | listed only |
| image-20240206-155524.png | image | 274 | 2024-02-06 | listed only |
| image-20240207-155032.png | image | 47 | 2024-02-07 | listed only |
| T95_V606_240212_113229_pack.zip | archive | 1802 | 2024-02-13 | listed only |
| T95_V606_240212_115405_pack.zip | archive | 2724 | 2024-02-13 | listed only |
| T95_V606_240212_121117_pack.zip | archive | 1825 | 2024-02-13 | listed only |
| image-20240213-201044.png | image | 57 | 2024-02-13 | listed only |
| T95_V606_240216_100438_pack.zip | archive | 1756 | 2024-02-19 | listed only |
| T95_V606_240216_102519_pack.zip | archive | 2517 | 2024-02-19 | listed only |
| T95_V606_240216_103829_pack.zip | archive | 1978 | 2024-02-19 | listed only |
