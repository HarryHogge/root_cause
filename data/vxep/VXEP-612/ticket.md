# VXEP-612: SD Card Reliability Corrective Actions

- **Issue type:** Major Project
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-09-06
- **Updated:** 2026-02-07
- **Resolved:** 2025-03-18
- **Reporter:** Cameron Chapman
- **Assignee:** Samuel Lopez
- **Creator:** Cameron Chapman
- **Parent:** VXEP-444 Sustainment: VXE-30 (inc'l minor issues and improvements)
- **Links:** relates to VXEP-236 (Systemic SD card Investigation VXE-522 XCOM board failures at LM Source inspection); relates to ENG-806 (Corrupt SD cards are reaching Final before being detected); relates to ENG-1881 (No User Notification of Xcomm SD Card Corruption ); relates to ENG-346 (1607P01A Improvements. XCOM / XE240 PWR COMMS BD); is blocked by ENG-2735 (2119470-01 SD card replacement. Replace Red Grey SD Card PN: 100-104382  ); is blocked by ENG-2798 (Implement Solder Mask on Industrial SD Card for Peeling Label)
- **Project Tier:** Tier 1
- **Product/Tech Owner:** David Grosher
- **Tech Lead:** David Grosher
- **Program (Marquee):** VXE30 Incident Investigation
- **Job Number:** J100084 - VXE Incident Investigation

## Description

See subtasks and linked investigation https://jenaero.atlassian.net/browse/VXEP-236 
Plan, in order of priority:
- Provide instructions to FSRs to identify SD Card as problem, replace, and re-format SD Cards on their own or ship Avionics Box back to Edge Autonomy RMA to do so.
- https://jenaero.atlassian.net/browse/VXEP-319  Needs assignment. Hayden was working,
- CW: https://jenaero.atlassian.net/browse/VA-2082
- https://jenaero.atlassian.net/browse/VXEP-734

QE
- https://jenaero.atlassian.net/browse/VA-1928 (quality task, mostly done). @Steve Stack do you have any documents tracking quarantine of the old cards?

EE
- https://jenaero.atlassian.net/browse/VA-1929 
- New cards approved for new builds.  https://jenaero.atlassian.net/browse/ENG-2767
- Production cut-in, of selected rugged SD card(s) [see here for that process: https://jenaero.atlassian.net/browse/ENG-2735
- https://jenaero.atlassian.net/browse/VXEP-623 
- Need to determine if this is still needed if direct to mfr purchases.
- https://jenaero.atlassian.net/browse/VXEP-618
- https://jenaero.atlassian.net/browse/VXEP-625

SW
- Firmware/GCS update to enable SDcard reformat in the field: Boot with corrupt card, Flag the degraded system and prevent flight, Inform the operator of the issue and Provide a mechanism for the operator to reformat the SD card. https://jenaero.atlassian.net/browse/VXEP-413  https://jenaero.atlassian.net/browse/FS2-1661

Deferred/Not planned CAs: 
- To have this error fix itself, low level driver would need a rewrite to timeout and upper layer code would need to be modified to trigger a reformat ((DaveG) Will not do)
- a significant amount of SW work.
- https://jenaero.atlassian.net/browse/VXEP-320
- To attempt to prevent SD Card corruption: add a super-cap to power the XCOMM while the last write operations are completed after power has been disconnected Not supported by the evidence. Maybe better to replace SD cards with a more reliable type of memory. 
- XCOMM will need to understand that it has lost main power and is booting down
- During this, tell PIC32 to not read or write from SD Card
- https://jenaero.atlassian.net/browse/VXEP-321

## Comments (11)

### Greg Fryer, 2024-09-06

Admin notes:
- I completed the project assesment. Only the “planned milestone” setting is needed, should we conduct a design review for this, or do we simply review the change when it is created? (The latter is fine, as this is a Tier 1 project.)
- I moved the Epics over to VA, which will make it easier to manage child tasks under the epics in the sprints better, as needed.

### Cameron Chapman, 2024-09-06

@Greg Fryer apologies for the epics in non ideal locations, non-ideal issue types, etc. Crazy week (as always) and I think better to record critical actions as they come up, then move later if no time to place in the best location initially.

### Greg Fryer, 2024-09-06

@Cameron Chapman (and everyone else) no need to apologize! I should have included a 🙂 . I am happy to help sweep up the battlefield and clean up on the back end, just wanted to let you all know I did it. 100% the right thing to write down whatever we can, as we can, and clean up ‘whenever someone has time’.

### Matt Philley, 2024-12-10

@Greg Fryer @Cameron Chapman @David Grosher @Connor Peebles @Samuel Lopez @Scott Whitney 
FYSA I am going to try to clean up and close a bunch of these open SD Card Investigation tickets from the initial containment/investigation since we are closing out on the “containment” side and transitioning the longer-term actions to Dave’s robustness investigation.
The Flight Science Jira project has their own collector ticket which is linked to the 6.4 release, so I think this is a good time to close out a ton of older ones and point everything there now for a bit of a reset. 
https://jenaero.atlassian.net/browse/FS2-310

### Greg Fryer, 2024-12-10

@Matt Philley Endorsed, for the record.

### Greg Fryer, 2025-01-09

@Samuel Lopez @Matt Philley Have we reached the point of closing this? I see the only open tasks relate to thermal tape, and I think we can cancel those. The blocking changes are in implementation, so that should be clear as well. Please advise by noon today 2025-01-09, or I’ll go ahead and close.

### Matt Philley, 2025-01-09

@Greg Fryer the temperature indicating tape was still desired by Connor and Dave G last we talked about it and plan was to implement it in the MAGNSS Avi Box.
After resolving that thread though this should be OK to close.

### Greg Fryer, 2025-01-09

@David Grosher @Connor Peebles Given I have been hearing about this tape for a month or more, has the temperature-sensing tape itself turned into a science project? We cannot afford a time sink. Will we have this closed in the next couple days?

### David Grosher, 2025-01-09

@Matt Philley I was under the impression that you were sourcing the temperature sensing stickers and that you had ordered one for the high range. I don’t think we ever found a product that could latch the low range.

### Matt Philley, 2025-01-09

@David Grosher ya we found a candidate for high end. Details are in this ticket and I ordered some and handed them off to Connor and Liam to tinker in relation to MAGNSS since that is our “worst case” heat generation configuration https://jenaero.atlassian.net/browse/VXEP-618 
We do not have a solution for low end temperature cuz it doesnt seem like a thing people make.

### Samuel Lopez, 2025-03-18

This investigation is concluded.  Edge has replaced the SD cards with the more robust industrial versions.

## Attachments (0)
