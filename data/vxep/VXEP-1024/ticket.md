# VXEP-1024: 107-102066 Capacitor pressure relief features sealed.

- **Issue type:** Engineering Change
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2024-01-08
- **Updated:** 2025-02-14
- **Resolved:** 2025-01-24
- **Reporter:** Ben Norris
- **Assignee:** Gary Angelus
- **Creator:** Ben Norris
- **Labels:** Electronics_Drafting, Production
- **Issue color:** purple
- **Part Number(s):** 107-102066, 107-101141
- **Production Stakeholder:** Ben Norris
- **Engineering Change Level:** Level 0 - Scope of change is obvious to assigned engineer

## Description

1/18/24 Update:
Moved to Engineering Change. This has been determined to be an Improvement and not a Problem, so prioritize accordingly.

Change Requested:
Remove requirement for e20 to be used to “seal” the end of Capacitor C1 on 107-102066 Rev E. Investigation below indicates it is not required. 

[embedded file]

Original Concern:
Noticed by @Ben Norris that the Capacitor used on the Air Data Pod Harness is sealed with EA-20 on both ends defeating the purpose of the relief features built into the capacitor. Recommend testing to verify whether sealing the capacitor results in catastrophic failure of capacitor casing upon pressure build up in capacitor. @Laszlo Juhasz also observed that sealing the pressure relief feature is likely to cause catastrophic failures.
ADP Assy PN: 107-101141
SA Camera Tray Assy PN: 107-101649
ADP Harness PN: 107-102066
Cap PN: 100-108918, CAPACITOR, ALUMINIUM, 470UF 20% 50V RADIAL

## Comments (21)

### Matt Philley, 2024-01-08

Current Game Plan:
Production (Ben N) to prepare the following samples:
- Qty 3-4 caps with no adhesive
- Qty 3-4 caps with Toughseal (previous flexible “rubbery” adhesive)
- Qty 3-4 caps with E20 (current rigid structural epoxy)

Qty ~1 hr of time request from @Laszlo Juhasz to test the caps to failure paying attention to severity of failure especially for things like creation of fire.
Depending on the results we need to determine if we treat this is a true issue and look at quarantines, field rework, production stop work, etc. or if this is just an opportunity for improvement.

### Matt Philley, 2024-01-08

@Barry Mendez @Greg Fryer associated Jira to investigate capacitor potential issue in ADP

### Matt Philley, 2024-01-08

@Cameron Chapman @Laszlo Juhasz got blessing from Greg and Barry to spend an hour or so for an assessment for Sustainment.

### Matt Philley, 2024-01-08

@Ben Norris can you notify the masses once the caps are ready?

### Cameron Chapman, 2024-01-08

@Laszlo Juhasz I discussed with @Matt Philley 
Test plan.
- See if potting is needed (waterproof test).
- Install capacitor variants in scrap air data pod. Compare failure damage of each variant to see if any are risky to personnel or unrelated ADP systems (I would guess no).

### Ben Norris, 2024-01-09

@Laszlo Juhasz @Matt Philley The Capacitors have been dropped off at Laszlo’s bench this morning.

### Matt Philley, 2024-01-09

@Desiray Johnston @Greg Fryer @Cameron Chapman @Marc Richardson 
Based on discussion yesterday Production has been given the direction to continue building per the current revision AT RISK. 
That decision is based on the fact we have yet to have a problem with a cap popping in flight in the history of the program, so the potential occurrence is extremely low. Additionally, we do not anticipate the inclusion of the E20 to have a meaningful change to the impact of the failure if the capacitor did fail in the aircraft. 
We will keep an eye on this though and depending on the results of Laszlo’s test we can evaluate that decision again.

### Matt Philley, 2024-01-11

@Laszlo Juhasz any update or an estimated time when you will be able to test these?

### Laszlo Juhasz, 2024-01-16

@Ben Norris @Matt Philley @Cameron Chapman  Gents, I’ve done with the regression and “pop-corn” test and the report is attached.

### Matt Philley, 2024-01-16

@Laszlo Juhasz @Cameron Chapman 
My understanding of the results is as follows. Please let me know if I understood correctly or not:
- If the cap was “sealed” or not did not change the magnitude of the capacitor failure, therefore there is no risk or issue with delivered or currently manufactured product in the aircraft. So, all ADP’s are acceptable as-is and no further action needed
- There was no benefit to sealing the cap for moisture intrusion, so there may be an improvement to eliminate the practice of “sealing” the cap.
- The “seal” was also suspected to be used to try and insulate the top of the cap from the connector inside the ADP due to the tight installation, but that was not mentioned in your report. Is that a concern at all?

### Cameron Chapman, 2024-01-17

@Matt Philley the seal was added for moisture, not insulation. I am ok to approve omitting this seal for all caps going forward and keeping this issue open until the document is updated.

### Matt Philley, 2024-01-17

@Cameron Chapman easiest path would be to just keep making them to the existing drawing if there is no issue and we can treat removing the e20 as an improvement. 
I will work on submitting a change Jira and linking these.

### Cameron Chapman, 2024-01-17

Thanks @Matt Philley . We can also just change this issue to a eng change issue type, to reduce the number of issues.

### Matt Philley, 2024-01-18

@Cameron Chapman @Greg Fryer Based on the investigation and notes below I moved this to an Engineering Change issue type for the Improvement request to remove the e20 callout for the capacitor. I also changed it to Unassigned since it was previously Laszlo who did the investigation. 
Let me know if I fumbled the Jira issue type transition.

### Nadia Brown, 2024-03-20

@Matt Philley @Cameron Chapman I just read through this and all the comments to catch myself up on all that has transpired regarding this issue. 

I’ll go ahead and update 107-102066 as listed in the change request in the description of this ticket, but does this also affect the other PNs listed on this ticket? Should I implement the same changes to them?

### Nadia Brown, 2024-06-27

@Connor Peebles 107-102066 is ready for review. It’s the only one I edited, since I saw no other mentions of 107-101141 and this ticket appears to only be for 107-102066.

### Greg Fryer, 2024-10-03

I’m just digging through our backlog of incomplete changes, trying to find easy things to finish.
@Connor Peebles It looks like this stalled out, while it is minor having the documents stuck in change state is risky - we should either finish this or cancel the change entirely. May want to work with @Gerrit Sperling to see about getting all the design definition files up to the same revision.
At the risk of making it take any longer, could get the drafting team to bring this up to standard?
@Cameron Chapman FYI or maybe SA.

### Cameron Chapman, 2024-10-03

@Gary Angelus can you please review and release this if it looks good?

### Tobi Ogunro, 2025-01-23

@Gary Angelus Should this be transitioned to done?

### Gary Angelus, 2025-01-23

@Tobi Ogunro , yes done.

### Gary Angelus, 2025-01-23

@Tobi Ogunro , yes done.

## Attachments (8)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 107-102066 Rev E Drawing Snapshot.png | image | 224 | 2024-01-08 | listed only |
| ADP Routing Showing Cap Placement.png | image | 1760 | 2024-01-08 | listed only |
| Example of Cap that pops at Pressure Relief Valve.png | image | 227 | 2024-01-08 | listed only |
| Image (4).jpg | image | 776 | 2024-01-08 | listed only |
| Image (5).jpg | image | 641 | 2024-01-08 | listed only |
| Cap Samples.jpg | image | 482 | 2024-01-09 | listed only |
| [Electrolytic Capacitor Ingression and Popcorn Test.docx](attachments/18344_Electrolytic%20Capacitor%20Ingression%20and%20Popcorn%20Test.docx.md) | docx | 329 | 2024-01-16 | converted |
| image-20240118-151030.png | image | 78 | 2024-01-18 | listed only |
