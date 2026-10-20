# VXEP-263: VXE-604 crash during SCO/ Flight test

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-01-31
- **Updated:** 2026-03-02
- **Resolved:** 2024-08-23
- **Reporter:** Pat Wells
- **Assignee:** David Grosher
- **Creator:** Pat Wells
- **Labels:** Bad_Mag_Data, TIQUILA, Weekly-incident-tracker
- **Links:** is cloned by VXEP-265 (VXE-606 Odd VTOL behavior during SCO/ Flight test); relates to VXEP-265 (VXE-606 Odd VTOL behavior during SCO/ Flight test); relates to FS2-1406 (v604 Crash investigation); relates to FS2-1419 (Test operation of RTOS to rule in or out processor loading issues for AV604 mishap.); relates to VXEP-268 (Add reasonableness test to total magnetometer magnitude in order to prevent grossly erroneous mag measurements from corrupting heading state.); relates to FS2-1432 (v604 Crash investigation); relates to VXEP-275 (VXE-406 crash on landing at AEWE (Edge asset)); relates to VA-2165 (Complete disposition of V604 - identify electronics to replace)
- **Customer:** TIQUILA
- **Vehicle Tail Number:** 604
- **Vehicle Configuration:** Battery
- **Problem Type:** Other (explain in description)
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical

## Description

During the 3rd flight after completing a full flight cycle a landing pause was performed (as part of the 3rd flight check). During this landing pause the vehicle was nudged left and right repeatedly and after a few nudge inputs the vehicle stopped responding to the controls, started an uncontrolled flyaway (at 10-15ft), and crashed into the ground.
Aircraft: AC 604 new production aircraft
HLB: 2-1287
Main Battery: 3-1307

AAR files attached
Mishap report link: AC604Investigation.pptx
File location: https://jenaero.sharepoint.com/:f:/r/sites/FlightSafety/Shared%20Documents/Incident%20Reports/2024-01-30%20VXE604%20Flight%20Test%20crash?csf=1&web=1&e=slDefE 

Link to videos: https://jenaero-my.sharepoint.com/personal/abertulis_edgeautonomy_io1/_layouts/15/stream.aspx?id=%2Fpersonal%2Fabertulis%5Fedgeautonomy%5Fio1%2FDocuments%2FShared%2F604%20mishap%2FVideos%20and%20pictures%2FC0579%2EMP4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview 

https://jenaero-my.sharepoint.com/personal/abertulis_edgeautonomy_io1/_layouts/15/stream.aspx?id=%2Fpersonal%2Fabertulis%5Fedgeautonomy%5Fio1%2FDocuments%2FShared%2F604%20mishap%2FVideos%20and%20pictures%2FC0580%2EMP4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview 

NCR: https://jenaero.sharepoint.com/sites/JAI_Operations/Lists/NCR%20List/DispForm.aspx?ID=2371&commentId=5&e=hws0DB569ECpUDqi1Wg_4w&at=15

## Corrective Action

Artis to work on interim internal guidance. If aircraft seems to be veering off due to bad mag data, switch to attitude mode (will ignore bad data) and nudge into position. This might not work if CPU is locked up, but worth a shot.  
Dave: “Implementing corrective action to detect and ignore bad mag data.” Same as 406. Handled together. https://jenaero.atlassian.net/browse/VXEP-268

## Plan

- Investigate whether erroneous mag was due to mag failure or some other electrical disturbance​
- Test if IMUsrc flag works. This would indicate if the bad data might have come from the primary or VTOL AP mag (known to be interefered with).
- Test if high CPU loading affects mag data received.  https://jenaero.atlassian.net/browse/FS2-1419
- Record what items could cause the “VTOL AP fail” message logged. Just sensor failure, or VTOL AP processor overload as well? Does this indicate mag issue?
- Consider code modifications to check total magnetic field for reasonableness before incorporating into the navigation filter
- https://jenaero.atlassian.net/browse/VXEP-268
- Have we looked at other accelerometer data for vibe issues? ETB: Yes, added results to backup slides of presentation.  TLDR: nothing apparently different in accelerometer data.
- Does FW mag look normal? ETB: Added plots to backup of presentation, TLDR: looks like fixed-wing nav filter was functioning OK.
- Link to the issue with 604 in ppt and JIRA. ETB: Done.
- Test to see if imusrc works when the primary magnetometer stops responding.

## Issue Status

Open.
Hypothesis: CPU load is often an instance of a task locking up, which leads to corrupting data on the mag.
Dave mentioned the external mag was being used the entire time for both events.
Completed power up. Magnetometer seemed to operate nominally during wiggle test of wires at both ends, manual vibration, and tether test to climb power. 
Also related to https://jenaero.atlassian.net/browse/VIT-31  (old archive so can’t direct link in jira)

## Comments (22)

### Greg Fryer, 2024-01-31

Going to see @Artis Bertulis and halt Flight Test until we isolate (I wager he already has, but to be sure). @David Grosher we likely need a pictorial view of the timeline - I am inferring from what you wrote that we lost ADP first?

### David Grosher, 2024-01-31

@Eric Brewer Can you attach your report to this issue.  And can you build in the timeline requested by Greg.

### Eric Brewer, 2024-01-31

Ppt attached, will update now to build timeline of data in sync with video.

### Eric Brewer, 2024-01-31

Updated ppt with timeline attached, let me know if you have questions.

### Eric Brewer, 2024-01-31

Moved ppt to sharepoint per Cameron.  Ppt is now here:
AC604Investigation.pptx

### Cody Smisek, 2024-01-31

added AAR from 481 tether test using 604 CW.

### Eric Brewer, 2024-02-01

I didn’t see any vtol logs in the 481 tether testing zip (it had vtol logs from the 604 flight).  Although it was strange, the vtol log had the same number (vtl00028.csv) but different name than flight log file:
T95_VT604_240130_151849_vtl00028 <-actual flight log file
T95_VT604_240131_135836_vtl00028 ← log in tether test (but contains same data as the flight)

### Eric Brewer, 2024-02-07

I added several slides to the end of the powerpoint.  Data seems to indicate that mag failover was likely based upon timing of VT Fault reported in xcomm logs that roughly correlates in time with when the mag became erroneous.

### Matt Philley, 2024-02-20

@Greg Fryer @Marc Richardson @Eric Brewer @David Grosher @Pat Wells it does not look like the investigation for AC604 has been completed? We got a verbal that the cause was related to the “burst” data collection, but it doesnt look like that was ever fully confirmed or finalized….?
Just a reminder so it doesnt fall completely off the radar.

### Eric Brewer, 2024-02-20

@Matt Philley , thanks for reaching out.  @Scott Hunter is still investigating and trying to reproduce this issue in our HIL.  You’ll also note there is a related issue https://jenaero.atlassian.net/browse/VXEP-275 where we saw a nearly identical issue cause a crash on V406.  Scott, please provide any updates you have.

### Matt Philley, 2024-02-21

@Marc Richardson risk assessment related to this topic has been attached

### Cody Smisek, 2024-11-07

@Greg Fryer issue status shows open, but ticket shows closed. aircraft cases are in engineering (unsure what’s in them, cases are sealed with tag). 
What should we do with equipment?

### Greg Fryer, 2024-11-07

@Cody Smisek Same as the other ticket, we need to provide disposition to production - e.g. is the AV deliverable or has it been written off? Likely need to check with production. @Desiray Johnston what is the status of 604 from a production perspective?

### Desiray Johnston, 2024-11-07

@Greg Fryer @Cody Smisek 604 was originally assigned to Tiquila and was removed once it crashed. Kyle and I reviewed the AC equipment and seems like minimal work to get it working to make it an asset.

### Greg Fryer, 2024-11-07

@Desiray Johnston Thank you! Do you need us to issue anything, or should we just move it back to final? Or did you already take it? 🙂

### Desiray Johnston, 2024-11-07

@Greg Fryer  can you have the team provide dispo and tag @Sandra Lopez @Sean Odell @Kyle England , then I will get our team to perform rework/repair.

### Greg Fryer, 2024-11-07

@Desiray Johnston Since it’s not a production bird, figure we should put it into the “production requests” including whatever the needed rework is. (I checked the NCR, it got closed once we exited it out of production.)

### Greg Fryer, 2024-11-08

I’m moving the dispo of the AV off the incident, to linked issue https://jenaero.atlassian.net/browse/VA-2165  so we don’t keep cluttering this up.

### Cody Smisek, 2025-06-05

@David Grosher @Greg Fryer I’m going to start picking parts from this aircraft and putting in official part storage. There’s no Root Cause on this ticket. In the powerpoint, mention of possible mag data issue, then in another linked ticket there’s mention of burst data being the issue. Either of you recall what the cause was? Can avionics be re-used for flight, or only good for iron bird / HILs?

### David Grosher, 2025-06-05

@Cody Smisek Use the hardware for iron birds / HILs. If I remember correctly this incident was related to corruption of the Mag data during context switching to/from tasks doing floating point math but not explicitly declaring FPU support within the task. I think there was also another issue where the bus that the magnetometer was on would crash periodically. Both issues have been resolved.

### Cody Smisek, 2025-06-05

@David Grosher @Greg Fryer I’m going to start picking parts from this aircraft and putting in official part storage. There’s no Root Cause on this ticket. In the powerpoint, mention of possible mag data issue, then in another linked ticket there’s mention of burst data being the issue. Either of you recall what the cause was? Can avionics be re-used for flight, or only good for iron bird / HILs?

### David Grosher, 2025-06-05

@Cody Smisek Use the hardware for iron birds / HILs. If I remember correctly this incident was related to corruption of the Mag data during context switching to/from tasks doing floating point math but not explicitly declaring FPU support within the task. I think there was also another issue where the bus that the magnetometer was on would crash periodically. Both issues have been resolved.

## Attachments (7)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AC 604 Crash Photos.zip | archive | 43365 | 2024-01-31 | listed only |
| [Post Mishap Report.docx](attachments/18550_Post%20Mishap%20Report.docx.md) | docx | 56 | 2024-01-31 | converted |
| T95_V481_240131_135836_pack.zip | archive | 14673 | 2024-01-31 | listed only |
| T95_V604_240130_151849_pack.zip | archive | 3488 | 2024-01-31 | listed only |
| [T95_V604_240130_BURST000.csv](attachments/18551_T95_V604_240130_BURST000.csv.md) | csv | 585 | 2024-01-31 | converted |
| [V604 VTOL crash notes.pdf](attachments/18553_V604%20VTOL%20crash%20notes.pdf.md) | pdf | 313 | 2024-01-31 | converted |
| [Risk Assessment - AC 604 and 406 CPU Loading and Mag Issue Crashes, Use As Is - 24.02.21.pdf](attachments/18890_Risk%20Assessment%20-%20AC%20604%20and%20406%20CPU%20Loading%20and%20Mag%20Issue%20Crashes,%20Use%20As%20Is%20-%2024.02.21.pdf.md) | pdf | 439 | 2024-02-21 | converted |
