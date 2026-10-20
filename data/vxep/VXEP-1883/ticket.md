# VXEP-1883: VXE 910 is having intermittent Novatel resets

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** High
- **Created:** 2026-05-06
- **Updated:** 2026-10-12
- **Resolved:** 2026-10-12
- **Reporter:** Stephan Johnson
- **Assignee:** Eric Brewer
- **Creator:** Stephan Johnson
- **Labels:** Hardware, RCCA, Weekly-incident-tracker
- **Links:** relates to RMA-1075 (VXE-910 RMA 260804-01)
- **Customer:** S&P_PMO
- **Vehicle Tail Number:** VXE 910
- **Issue Status:** Waiting for aircraft return.
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

VXE 910’s Novatel intermittently has a heartbeat timeout every ~30 seconds to 5 minutes, causing autopilot GNSS lock issues.

## Plan

- Put v914 XCOMM and novatel interface boards and put them in the iron bird and see if the long configuration times are observed
- if yes, then scope on that interface to see if anything stands out
- @Lauren Velasquez@Drew Hildreth   please link RMA when available.

## Executive Summary

Pending additional egineering testing and potential hardware replacement. ACFT received in SLO 8/7. Probable cause Hardware Issue.

## Comments (13)

### Scott Lovett, 2026-05-12

Needs additional GS review before action

### Scott Whitney, 2026-05-14

Update from @Eric Brewer meeting:

Quick update from the meeting:

- They powered up 910, the novatel was still continuously resetting - every 30s.
- Loaded on test software.  Software still timed out on configuration once before successfully completing.  Uptime log was received intermittently which would have caused production software to time out.
- Checked NovAtel debug logs - no receiver crashes were in memory so no NovAtel crash issue.
- Removed Trillium payload and power cycled, xcomm was not able to pass configuration and timed out a couple times while I was watching.  The configuration step normally completes within 5s and it was taking more than 30.
- Given 1-4 I suspect an electrical issue causing the xcomm<->novatel serial link to be intermittent.  Dave you mentioned we had some electrical issues with some xcomm boards?  Guessing this could be related.
- They have an integration planned in the near future - want to see if they can send back one aircraft at a time? Can do integration with bird on ground - will advise us what works for them.

 
Drew if you're keeping documentation for the RMA make sure to note that it has test software on 910 - we had them load that build on (usually we'll check if nonstandard software is used when the aircraft comes back)
 

Plan from @David Grosher :
- Put v914 XCOMM and novatel interface boards and put them in the iron bird and see if the long configuration times are observed
- if yes, then scope on that interface to see if anything stands out

### Scott Lovett, 2026-07-06

Awaiting completion of 909 before starting on 910

### Lauren Velasquez, 2026-08-07

@Scott Lovett 909 is pending CofC at this time and will then be shipped back to the customer.

### Drew Hildreth, 2026-08-10

910 arrived in SLO 8/7/26

@Lauren Velasquez @Zack Garcia See Scott’s comments below about the SW. 

@Eric Brewer are we replacing the avionics on this aircraft or can we change a component out?

### Eric Brewer, 2026-08-10

@Drew Hildreth it’s up to the team how much debugging we want to take on.  The tests that we ran on site indicated issues with communications between xcomm and the novatel receiver.  In my mind the easiest thing to do is to replace the xcomm and the gnss interface board and all novatel components, but if we think that’s too heavy handed we’ll need to plan some time for more debugging.

### Stephan Johnson, 2026-08-25

@Drew Hildreth based on Eric’s input, would you be okay with moving forward on replacing the XCOMM?

### Drew Hildreth, 2026-08-25

@Stephan Johnson after an internal discussion with the team we decided to go with a new Avionics. It has been quoted and approved. Awaiting Scheduling.

### David Grosher, 2026-09-01

@Drew Hildreth How do you want to handle this ticket? @Jeremy Kostel FYSA.

### Stephan Johnson, 2026-10-05

@Jeremy Kostel have you guys had a chance to look at this bird yet?

### Jeremy Kostel, 2026-10-05

@Stephan Johnson sounds like we got a new avionics box in there. I would just recommend pushing the aircraft back through SCO as itll need to go through there anyways. @Eric Brewer could you give Carson a short summary of what to look for to see if the issue resolved?

### Eric Brewer, 2026-10-05

@Jeremy Kostel @Carson Buckley you’d be looking for any of these messages in the xcomm event log.

[embedded image-20261005-221821.png]
From the comments below it looks like we put in a whole new avionics box, is that right? If that’s the case we should be able to just do normal SCO as Jeremy says, if there were similar issues with GPS you’d notice.

### Stephan Johnson, 2026-10-12

Avionics assy replaced due to internal faults.

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_V910_20260506T175542Z.zip | archive | 159554 | 2026-05-06 | listed only |
| v909_v910.zip | archive | 39076 | 2026-05-06 | listed only |
| AAR_V910_20260506T175542Z (59c38a84-18e0-491d-a45e-6008f71976fc).zip | archive | 159554 | 2026-08-10 | listed only |
| image-20261005-221821.png | image | 58 | 2026-10-05 | listed only |
