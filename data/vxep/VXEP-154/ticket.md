# VXEP-154: VXE-401 - Wing oscillation with antennas attached

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2023-10-18
- **Updated:** 2024-08-23
- **Resolved:** 2024-08-23
- **Reporter:** Cameron Chapman
- **Assignee:** David Grosher
- **Creator:** Cameron Chapman
- **Links:** relates to VXEP-146 (VXE-401 Loss of operator control during aborted landing); is cloned by ENG-3162 (VXE490, 491 Oscillation ); relates to RMA-174 (VXE-401 231023-1); is blocked by FS2-1050 (Mitigate Structural Resonance (~8.4Hz) during VTOL Flight)
- **Issue Status:** Flight Systems investigating control loop resonance, if/once verified, SW update expected.
- **Severity:** 1 - Flight Critical

## Description

Creating this to troubleshoot separate issues on the same flight. See linked issue for background and video.

## Plan

- Determine if this wobble could be a safety of flight, or decrease lifespan. It is not.
- Determine C/CA or link to a project for that if so.
- Determine acceptable level of wobble without having to record an incident. Notify customer service. Evaluating incidents as requested.
- Determine if resonance in the control loop contribute to this oscillation, or was it a related issue discovered, but not the cause of the oscillation? Seems like the latter, but I want confirm with someone more familiar.
 https://jenaero.atlassian.net/browse/FS2-1050


Customer provided video of the mishap
 https://photos.app.goo.gl/YnQCSLnEcUNyUWTU9

## Comments (9)

### Greg Fryer, 2023-10-25

@David Grosher I assigned this to you, per our discussion that you would put it into Flight Systems task list. Please link the Epic(s) you make as blockers to this incident.
I put it on hold, you can advance once you have time to work.

### Sean Odell, 2023-10-26

@Cameron Chapman @David Grosher @Greg Fryer Aircraft evaluated, photos taken, added to RMA ticket for reference. I am bringing over the aircraft today.
@Pat Wells FYSA

### Cameron Chapman, 2023-10-26

@Greg Fryer did you mean to assign this mechanical sounding incident to @David Grosher  or did you mean to assign this software sounding one https://jenaero.atlassian.net/browse/VXEP-146 to him? We split the different incidents from the same flight, as they seem to be unrelated.

### Cameron Chapman, 2023-11-08

@Ryan Christino is having this aricraft on site useful for this troubleshooting, or should it be returned to the customer?

### Greg Fryer, 2023-11-08

@Cameron Chapman To answer your very old question, yes I put this on Dave’s plate because we found the resonance in teh control lop (see the linked task). You may know that already. The other I am holding to process, but Dave and Team are doing the work.

### Ryan Christino, 2023-11-08

@Cameron Chapman The current plan for this issue is to finish the VTOL simulation we are working on and attempt to inject noise at a frequency matching the oscillation into the control loop. We will then adjust the controls, either using a notch filter or with tuning, to account for that specific frequency messing with the controller. We have the frequency identified from previous testing and will not need to replicate the issue at this time.
To answer your question: We will not require that specific aircraft on site to troubleshoot this issue. Eventually, when we have our solution vetted out, not sure of the timeline, we will need an asset to test our fix on. I’m fairly confident we can get this to occur on a different aircraft so returning the asset may make more sense right now.

### Cameron Chapman, 2023-11-08

@Ryan Christino I added your plan to investigation plan field above. Please keep those fields updated as you go in the future.

### Cameron Chapman, 2023-11-08

@Greg Fryer and @Ryan Christino thanks for the updates. To clear up C/CA, does the resonance in the control loop contribute to this oscillation, or was it a related issue discovered, but not the cause of the oscillation? Seems like the latter, but I want confim with someone more familiar.

### Cameron Chapman, 2023-12-05

Dave asked Artis and team to collect VTOL data to collect data on where structural nodes are. Will design a notch filter to filter out this in control loop.

## Attachments (0)
