# VXEP-548: VXE 300 CW not mounting securely and has some delamination

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-08-20
- **Updated:** 2024-09-11
- **Resolved:** 2024-09-11
- **Reporter:** Cameron Chapman
- **Assignee:** Jack Waeschle
- **Creator:** Cameron Chapman
- **Links:** relates to VA-1926 (Replace Aluminum bolts with titanium for wing shift bracket)
- **Vehicle Tail Number:** 300, 689
- **Production Stakeholder:** Trevor Gronner
- **Supply Chain Stakeholder:** Kenneth Weber
- **Other Stakeholder (as required):** Matt Philley
- **Problem Type:** Production Issue
- **Issue Status:** Root cause identified, determining any corrective actions required.
- **Incident Type:** Mission Failure/Abort
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

Videos with and without wing shift kit. 
@Cody Smisek please ensure 689 CW is checked with fuselage to ensure it is not an issue with the fuselage.
300CW with 689 fuselage
[embedded: MicrosoftTeams-video.mp4]
689 fuse with 300CW+wing shift bracket
[embedded: MicrosoftTeams-video (1).mp4]



689 with 689 CW. 
[embedded: MicrosoftTeams-video (3).mp4]
689 with 689 wing shift bracket
[embedded: MicrosoftTeams-video (2).mp4]

## Corrective Action

Draft (from @Greg Fryer )
- https://jenaero.atlassian.net/browse/VXEP-593
- https://jenaero.atlassian.net/browse/VXEP-601
- https://jenaero.atlassian.net/browse/VXEP-602
- https://jenaero.atlassian.net/browse/VXEP-603

## Plan

- Contact vendor to correct this issue on future orders of wing shift brackets
- Allen Peek contacted the vendor (Top Precision)
- Continue Engineering investigation:

With wing shift bracket
- Determine failure modes (insufficiently tapped holes, retaining washer interference)
- Issue appears isolated to insufficiently tapped holes in wing shift bracket
- Determine containment, service bulletin, etc.
- Find catalog part number for the spare wing shift bracket
- 107-102843 VXE30 Wing Shift Bracket (Contains 107-100205 and 5 aluminum screws)
- Determine if path forward is a replacement wing shift bracket or supplying customers with a tap to clear holes fully
- @Greg Fryer to make decision.
- Evaluate current stock of wing shift brackets for issue
- 11 out of 133 have this issue ( Wing Shift Bracket NCR )

Without wing shift bracket
- Determine failure modes (retaining washer interference)
- There is not a failure mode without the wing shift bracket. Unable to replicate binding issue with retaining washers.

## Root Cause

JW: Sep 4, 2024 Only failure mode found is insufficiently tapped holes in wing shift bracket. Wing bolts are unable to tighten all the way, leaving wing loosely attached to fuselage. Wing bolts are not too long.

## Comments (15)

### Jack Waeschle, 2024-08-22

Root cause determined: Threaded 1/4-20 holes on wing shift bracket are not fully tapped. The drawing specifies this as a thru all end condition, but our manufacturer is not tapping the whole hole. This prevents the wing bolts from fully screwing in.

### Jack Waeschle, 2024-08-22

[embedded: image-20240822-182706.png]

### Cameron Chapman, 2024-08-29

@Matt Weber @Jack Waeschle @Steve Stack should we kickoff a containment on this? It seems so

### Steve Stack, 2024-08-30

@Matt Weber @Jack Waeschle @Noah Chavez 
Noah, Cameron just shared this Jira ticket with me that documents a non-conformance with a center wing.  Please inspect all of our center wings for this condition and quarantine any found to be non-compliant.

### Steve Stack, 2024-08-30

@Cameron Chapman I didn't include you in my response Cameron - sorry about that.  Yes, we need to determine our exposure to other non-conforming center wings.

### Cameron Chapman, 2024-08-30

@Jack Waeschle @Noah Chavez@Matt Weber  has any action been taken to ensure the manufacturer taps the whole hole, and that we have a receiving inspection to do this? Should we send out a service bulleting to check any customer wing shift brackets?
Can you evaluate these center wings without a wing shift bracket to determine if it is an acceptable amount of movement?

### Matt Weber, 2024-08-30

Havoc flight test we experienced the same issue with center wings SN005/006 on fuse & wing shift bracket 376.  I could not replicate the issue again.  As mentioned before: the wing shift bracket is tapped poorly and the screws feel like they bottom out before they actually do.  I will go try on 689 if it is in the building.
Update: I tested 689 CW and found that the retaining washers are not free-spinning and can bind on the nylon screw when they are too low on the thread, once again feeling like the screw is bottomed out before it actually is.  Even if the washers are placed higher, back up inside the pocket, the washer jumps the threads and returns to the place shown when the screw is pushed from the bottom (i.e. wing placed on fuselage).  
[embedded: image-20240830-202924.png]

### Greg Fryer, 2024-08-30

Updated root cause to not be conclusive, since there’s no evidence for that cause. Also need to know which wing shift bracket SN @Jack Waeschle checked so we can see if we can replicate (or de-replicate) it with sufficient torque. Agree we can improve the part, need to find in production and issue NCR - likely provide tool to re-tap/drill brackets in house.

### Matt Philley, 2024-09-03

@Steve Stack @Noah Chavez to clarify this is not an issue with the center wing itself under normal conditions. 
It is an issue with the interaction with the centerwing and wing shift bracket not being able to consistently mount securely. The wing shift bracket is a sperate piece of hardware included in the Fuselage Transit Case PN 107-100205.
The wing shift bracket is not typically used, but is needed in situations where the center of gravity of the aircraft needs to be adjusted due to certain payloads and weight distribution of stuff on the vehicle. 
It does not seem this is widely used by Customers, so hopefully not too painful of a containment once final root cause is identified.

### Matt Weber, 2024-09-03

@Matt Philley The problem I saw and noted previously is indeed a problem with the center wing 689 itself under normal conditions.  It seems we have 3 possible issues when wings don’t mount properly:
- The bolts are too long and protrude past the underside of the center wing more than the thickness of the wing shift bracket (0.60”).  This would only affect mounting with the wing-shift bracket and not normal flight situations.  From the center wings I have measured I haven’t found any to be too long.  Worth noting that the wing-shift bracket could be too thin, but the few I measured were at their nominal 0.60”
- The holes in the wing shift bracket are not fully threaded and the center wing bolts bind.  This would only affect mounting with the wing-shift bracket and not normal flight situations.  From the few wing shift brackets I have tested, they all bind on the last 2-3 threads.
- The retaining washers on the center wing mounting hardware bind and do not allow the the screws to be fully seated with normal finger-tight thumbscrew torque.  I only checked 689, but this was the case.  This can affect mounting with and without the wing-shift bracket

### Jack Waeschle, 2024-09-03

@Noah Chavez completed a complete inspection of wing shift brackets in inventory: https://jenaero.sharepoint.com/sites/JAI_Operations/Lists/NCR%20List/DispForm.aspx?ID=4211&commentId=1&e=--vBXpAxbEquodwf454FPg&at=15&xsdata=MDV8MDJ8andhZXNjaGxlQGVkZ2VhdXRvbm9teS5pb3w1MjQ2NDRiMWI5YzM0ZTA5YTRkYjA4ZGNjYzU2ZjU4ZnwxODc2ZjYxYTNiZGI0ODQzYWU3MDc1ZWQwY2NiNzQwNHwwfDB8NjM4NjA5OTIxMDcyMjQ3MTA0fFVua25vd258VFdGcGJHWnNiM2Q4ZXlKV0lqb2lNQzR3TGpBd01EQWlMQ0pRSWpvaVYybHVNeklpTENKQlRpSTZJazFoYVd3aUxDSlhWQ0k2TW4wPXwwfHx8&sdata=UjBmY1A0ZE9UOHJkWHRUS1ZIV0N6akpBNzNndWUrc01oTFIwdUpGMEx5MD0%3D&clickparams=eyAiWC1BcHBOYW1lIiA6ICJNaWNyb3NvZnQgT3V0bG9vayIsICJYLUFwcFZlcnNpb24iIDogIjE2LjAuMTc4MzAuMjAxMzgiLCAiT1MiIDogIldpbmRvd3MiIH0%3D  
Out of 133 wing shift brackets in inventory, 11 had insufficiently tapped holes.
I inspected Vehicle 689 wing shift bracket and found the holes are insufficiently tapped, as seen below. The bolt bottoms out at this point.
[embedded: image-20240903-222837.png]
Vehicle 300 also has a non conforming wing shift bracket:
[embedded: image-20240903-222853.png]
As a random spot check, the wing shift bracket for 695 does feature fully tapped holes. Note screw pictured is not typically inserted into this hole, however it is also a 1/4 20 bolt so I used it for this spot check. This is how all wing shift bracket threaded holes should be (fully threaded).
[embedded: image-20240903-222902.png]

### Jack Waeschle, 2024-09-04

@Matt Weber and I completed more test fits today and found it hard/impossible to replicate the retaining washer binding issue. The retaining washer could add resistance while tightening the thumb screws down, but not to the point of feeling a bolt was fully tightened. Additionally, this issue was more pronounced when threading the nylon wing bolts into the Delrin wing shift bracket compared to attaching the wing to a fuselage directly. All of this is to say the issue described in this ticket appears isolated to the wing shift bracket.
689 center wing mounted securely to 689 fuse and 300 fuse. 689 center wing with 689 wing shift bracket (partially threaded) and 300 wing shift bracket (partially threaded) produced an unsatisfactory mate, with extensive gap/wiggle left in the interface after the wing bolts bottomed out the threads. 689 center wing with 695 wing shift bracket (fully threaded) mounted securely. All of this indicated the insufficient threads in the wing shift bracket cause this issue.

### Cameron Chapman, 2024-09-04

@Steve Stack @Greg Fryer @Matt Philley @Matt Weber there seem to be at least 1-2 issues with these that should drive some customer containment (see subtasks)  Who should drive that process?

### Greg Fryer, 2024-09-04

@Cameron Chapman I think the actions need to be updated to match the actual findings. e.g. there’s no friction issue. 
Based on Jack’s hallway briefing to me, I am debating if there is containment needed, beyond what’s in house (already done, vendor already notified). With zero occurrences in the field, we may simply need to generate a fix-it kit (both replace and tool based) for the support team to use if there are any instances.

### Greg Fryer, 2024-09-11

@Jack Waeschle Process released after review with Product Support. Once you finish https://jenaero.atlassian.net/browse/VXEP-626 please complete the investigation too (will take several clicks).

## Attachments (9)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| MicrosoftTeams-video (1).mp4 | video | 1666 | 2024-08-20 | listed only |
| MicrosoftTeams-video.mp4 | video | 1318 | 2024-08-20 | listed only |
| MicrosoftTeams-video (2).mp4 | video | 1581 | 2024-08-21 | listed only |
| MicrosoftTeams-video (3).mp4 | video | 1643 | 2024-08-21 | listed only |
| image-20240822-182706.png | image | 11 | 2024-08-22 | listed only |
| image-20240830-202924.png | image | 12438 | 2024-08-30 | listed only |
| image-20240903-222837.png | image | 1128 | 2024-09-03 | listed only |
| image-20240903-222853.png | image | 1188 | 2024-09-03 | listed only |
| image-20240903-222902.png | image | 1229 | 2024-09-03 | listed only |
