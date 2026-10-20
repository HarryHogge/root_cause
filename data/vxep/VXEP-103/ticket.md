# VXEP-103: VXE-473 Crash on landing, failed to transition to VTOL

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed, but added to Bermuda Triangle List
- **Resolution:** Cannot Reproduce
- **Priority:** Highest
- **Created:** 2023-09-26
- **Updated:** 2026-08-14
- **Resolved:** 2025-08-07
- **Reporter:** Pat Wells
- **Assignee:** Eric Brewer
- **Creator:** Pat Wells
- **Labels:** MARSOC, Software, Weekly-incident-tracker, valid
- **Parent:** VXEP-573 Sustainment: VXE30 Incident Investigation
- **Links:** relates to ENG-3070 (Aircraft 473 Crash); relates to RMA-332 (VXE-473 RMA 240905); relates to VXEP-426 (VXE 489 Erratic Landing Behavior); relates to VXEP-1039 (Test non-conductive plate and/or gimbal mounts to see if that resolved the issue and meets other requirements. Release and implement if so.)
- **Customer:** MARSOC
- **Vehicle Tail Number:** 473
- **Corrective Action:** None. Upgrade to latest software, v6.3.4.
- **Problem Type:** Other (explain in description)
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical

## Description

Files: https://jenaero.sharepoint.com/sites/FlightSafety/Shared%20Documents/Forms/AllItems.aspx?csf=1&web=1&e=dp79vR&CID=d8f1cb48%2D3366%2D403b%2Db278%2D98a1b6cdc45c&FolderCTID=0x012000D03119522A011A40817D7F0F59E3A7EF&id=%2Fsites%2FFlightSafety%2FShared%20Documents%2FIncident%20Reports%2FVXEP%2D103%20VXE%2D473%20Crash%20on%20landing%2C%20failed%20to%20transition%20to%20VTOL&viewid=7181a7a2%2Dd286%2D47c9%2Dbdd3%2D9195ef18282c 
Reported this morning via text message from a deployed customer.
 “The aircraft was coming in for a recovery and was at its approach altitude and just never transitioned to VTOL and overshot past the intended recovery location and down a cliff face.”
 Wreckage has not been recovered. An AAR was not produced before the software was shutdown. I ask them to create an AAR now and send it. I asked them to find the logfile on the C: but it appears to be empty.

## Plan

11/15/24 Motor test on all 4 VTOL motors will be performed. @Pat Wells Booms were not shipped with the rest of the aircraft. Are you able to ask the customer if they recovered these booms? 
11/18/24 Booms were not shipped with the rest of the bird per RMA ticket: [RMA-332] VXE-473 240905 - Jira
@Eric Brewer can you please provide an updated investigation plan here now that we do not have the booms? Would testing with other booms help test the other portions of the aircraft?

## Issue Status

Logs pulled and stored here.  https://jenaero.sharepoint.com/sites/FlightSafety/Shared%20Documents/Forms/AllItems.aspx?csf=1&web=1&e=dp79vR&CID=d8f1cb48%2D3366%2D403b%2Db278%2D98a1b6cdc45c&FolderCTID=0x012000D03119522A011A40817D7F0F59E3A7EF&id=%2Fsites%2FFlightSafety%2FShared%20Documents%2FIncident%20Reports%2FVXEP%2D103%20VXE%2D473%20Crash%20on%20landing%2C%20failed%20to%20transition%20to%20VTOL&viewid=7181a7a2%2Dd286%2D47c9%2Dbdd3%2D9195ef18282c 
Landing abort caused by VTOL system failing to throttle up.  It takes about 14 seconds from when the motors are unsafed to when they actually start drawing current and affecting vehicle attitude.  By that time the vehicle is already flipped over.
See report images here.
Abort and crash appear to be caused by lift system not drawing current until well after commanded.
Customer needs to ship booms in order to perform motor tests.
Per Pat Wells, booms will not be expected to be shipped to Edge. 12/18/2024
Returned equipment to RMA 12/19/2024.

## Root Cause

Unknown delay in lift system startup caused crash on transition.  Issue exacerbated by land abort issues present with old software.  
If vehicle condition will support it, we can try to reproduce the issue with the motor test panel similar to https://jenaero.atlassian.net/browse/VXEP-426, it is possible the causes are related.  @Rajesh Budhabhatti @David Grosher @Cameron Chapman

## Comments (50)

### Pat Wells, 2023-10-03

@Greg Fryer working with customer to retrieve data files from GCS. Customer stated that the ACFT will not be recovered. We will not recieve AAR file from the ACFT.

### Pat Wells, 2023-10-04

@Greg Fryer Update as of today customer has recovered the ACFT. They will attempt to retrieve the AAR files.  The ACFT is currently at a deployed location and will not physically return before CY24.

### David Grosher, 2023-12-08

@Greg Fryer @Pat Wells Has data been retrieved from the AV?

### Pat Wells, 2023-12-08

@David Grosher no, the customer has not provided any data to date.

### David Grosher, 2024-08-12

@Pat Wells @Greg Fryer Can we close this issue?

### Pat Wells, 2024-08-12

@David Grosher disregard my last reply.  I deleted it.
Let me double check with customer as I think they recovered the air vehicle.

### Cameron Chapman, 2024-08-27

@Pat Wells your tracker says aircraft recovered 10/3. Is this correct? If so, can data now be uploaded?

### Pat Wells, 2024-08-27

@Cameron Chapman it was recovered from the crash site where it was deployed. 
We have not received the aircraft back yet from the customer.

### Cameron Chapman, 2024-08-28

Thanks @Pat Wells do they plan to try to pull logs first, or send it directly to us? We can update the plan field above accordingly.

### Pat Wells, 2024-08-28

@Cameron Chapman no idea.  They haven’t responded to multiple requests for information on this aircraft.

### Cameron Chapman, 2024-08-28

@Pat Wells understood. No worries as long as they are not expecting progress without returning an aircraft or data.

### Pat Wells, 2024-09-05

@Cameron Chapman aircraft arrived in SLO yesterday.
@Sean Odell will be delivering to engineering once the acceptance process is complete.

### Cameron Chapman, 2024-09-07

@Adrian Garcia please coordinate inspecting and powering up carefully to pull logs, post them here, then assign to Dave G once posted.

### Sean Odell, 2024-09-09

@Adrian Garcia @Pat Wells @Cameron Chapman @Greg Fryer Aircraft delivered to Engineering to start its evaluation.

### Adrian Garcia, 2024-09-09

@Cameron Chapman Currently pulling XCOMM logs but  the power wires on the CW harness are cut. I dont want to replace the CW harness before getting confirmation it is okay to do so. 
[embedded: image-20240909-221250.png]

### Cameron Chapman, 2024-09-09

@Adrian Garcia approved to remove the cover and closely inspect CW harness and demate all connectors from the VTOL AP . (Disconnect all CW harness connectors from the VTOL AP). As you demate each, inspect each to see if anything appears abnormal with the connector.

### Adrian Garcia, 2024-09-10

@Cameron Chapman When I opened the CW the AP board was not attached to the interface board. Other than that when I was pulling the harness off there was nothing unusual with the connectors. I replaced the center wing harness and powered on the board but will not connect to ethernet. @Brandon Slater can we meet up later and try to figure out why its not connecting over ethernet? 
[embedded: 820a80e1-8559-4ea5-886a-e1061e3f4986.jpg]
[embedded: 912fb997-d871-4e56-aafe-512d54258cb4.jpg]

[embedded: 00877723-deef-40e3-aae5-9556b2d35d30.jpg]

### Adrian Garcia, 2024-09-10

@Cameron Chapman assigning back to @David Grosher . Logs are in folder linked at the top. Only the last few logs on the XCOMM are included and all the VTOL logs are there because I got them through the SD card

### David Grosher, 2024-09-16

@Adrian Garcia Can you recover the event logs from the XCOMM? I see the datalogs from the XCOMM but not the event logs.

### Adrian Garcia, 2024-09-18

@David Grosher Added XCOMM Event logs to the folder above. Let me know if this is the correct one.

### David Grosher, 2024-09-18

@Pat Wells @Jason Scherer This looks like it would have experienced the now known land abort bug, with a crash detected 30 seconds later.  @Jason Scherer can you spend some time to close out the cause of the abort?     
[14:17:25.969 9073.970] ap dbg: vt lnd abort, health fail during taxi to lz
[14:17:56.865 9104.865] landing detected

### Jason Scherer, 2024-09-18

@David Grosher This was actually an attitude error that resulted in the landing abort which would have turned off VTOL motors and tried to glide land. This path in the old code did not result in activation of the land abort bug. It is covered by test case LA-02-010-01: LAND_WAITLZ (APM_ATT) which was a pass in our old code. 
XComm is the processor that monitors for attitude faults and sets the status bit (APM_ATT). If the roll or pitch values, reported by VTOL, exceeds a default of 50 degrees for 15 samples @1Hz in a row then the bit is set in the error state (0). 
If the fixed wing autopilot sees the error bit get set to 0, during this part of the VTOL transition, the VTOL landing is aborted, a command is sent to VTOL to safe the motors, and the fixed wing attempts to activate ELZ and glide land in fixed wing flight.
So that is what led to the land abort. Have to dig into the data a bit more to try and determine the root cause of the attitude fault during landing.

### David Grosher, 2024-09-19

@Eric Brewer Can you look into the attitude fault error that led to the attitude fault and land abort?
@Jason Scherer FYSA

### Eric Brewer, 2024-09-19

@David Grosher @Jason Scherer This looks to me like there was an issue with the VTOL system not kicking on.  The attitude fault occurred after the vehicle was already well on its way to flipping over.  Pitch/roll/heading matched pretty well, the VTOL throttle commands ramp up and then it’s about 14 seconds before the motors draw any current.  When they do finally draw current the vehicle flips over - this is likely either due to not all motors spooling up, or more likely that the integrators had wound up so the commands were no longer really valid.  The LF and RF motors are near max and the vehicle pitches up rapidly so that’s my best guess as to what happened. 
As to why the motors don’t spool up that’s less clear, the event logs indicate the motor was unsafed around the time that the command start being sent.  I did notice it looks like it had re-arm one time also.  I also linked to https://jenaero.atlassian.net/browse/VXEP-426 above, as we are investigating a slow motor response there as well (although not nearly as slow as what’s observed here).
[embedded: image-20240919-151655.png]

### David Grosher, 2024-09-24

@Eric Brewer To lay out next steps.

### Cody Smisek, 2024-10-07

Hardware is currently stored under the engineering stairwell area. Ready to return to RMA area when appropriate.

### Pat Wells, 2024-11-07

@Sean Odell please see comment below from Cody. 
@David Grosher are we ready to close this out with a final report?  Would like to get something to customer and potentially repair / replace aircraft.
@Jackson Riley Curvin FYSA

### Pat Wells, 2024-11-13

@Sean Odell @Jackson Riley Curvin See below

### David Grosher, 2024-11-14

@Cameron Chapman @Eric Brewer Can you pull together a report for this issue. It wasn’t clear if there was any identified reason the motors did not pull any power.

### Eric Brewer, 2024-11-15

@Rajesh Budhabhatti , would you be able to perform motor testing to see if we can reproduce the long wait time before the motors drew current?
@David Grosher @Cameron Chapman I put a link above to a quick report on what we know so far.

### Cameron Chapman, 2024-11-15

I think @Rajesh Budhabhatti needs to first focus on SA camera replacement, but he may be available to work on this if we hit a pause point on that project. @Adrian Garcia or @Giovanni Gonzalez may be available to run such a test. Adrian and Gio, please coordinate and let us know.

### Giovanni Gonzalez, 2024-11-15

@Cameron Chapman I am able to work on this

### Giovanni Gonzalez, 2024-11-15

@Eric Brewer @Cameron Chapman Lift booms are not in wing case. Need to locate booms in order to get VTOL motors and test them.

### Giovanni Gonzalez, 2024-11-18

@Cameron Chapman @Eric Brewer Booms were not shipped with the rest of the aircraft. We need to request that the customer ship these over to us in order to perform any motor tests.

### Cameron Chapman, 2024-11-18

@Pat Wells Booms were not shipped with the rest of the aircraft. Are you able to ask the customer if they recovered these booms?

### Pat Wells, 2024-11-18

@Cameron Chapman sent an email to customer regarding lift booms.

### Cody Smisek, 2024-12-18

@Pat Wells any updates on booms?

### Pat Wells, 2024-12-18

@Cody Smisek no and I would not expect that we’ll receive them.

### Cody Smisek, 2024-12-18

@Eric Brewer without booms, any additional work to be completed or ready to return hardware to RMA? I see RCCA sections already completed.

### Eric Brewer, 2024-12-19

@Cody Smisek No I don’t think there is much else we can do at this time.  If we learn anything with the 489 testing we can update this ticket also.

### Cody Smisek, 2024-12-19

@Pat Wells @Rodney Linch Had team’s discussion with Eric B. Returning equipment to RMA, without booms no reason to hold equipment at this time.

### Rodney Linch, 2024-12-19

@Jackson Riley Curvin - engineering returned cases to take up RMA space!

### Pat Wells, 2025-01-02

@Cody Smisek @Eric Brewer should we be expecting a completed report on this?  A look at what’s there now appears to be incomplete. 

@Jackson Riley Curvin

### Eric Brewer, 2025-01-02

@Pat Wells I updated the summary slide.  We are running some parallel investigation activities but I don’t have a completion date on them.  At this point our best guess is something in the FCS software, the ESC software, or some combination of the two.  Let me know if anything additional is needed for this investigation.  If it cannot close until we get to the root cause then we will need to expedite the parallel investigation (although it’s not guaranteed that will bear fruit in recreating the issue).
@Jackson Riley Curvin @Cody Smisek @Ben Triplett

### Pat Wells, 2025-03-17

@Eric Brewer any updates on the parallel investigation related to this?

### Eric Brewer, 2025-03-20

@Pat Wells , @Adrian Garcia is running some testing on 489.  489 experienced an SD card failure, and after replacement was unable to reproduce the observed issues.  It is unknown if the SD card failure was related to the motors being slow to spool or unrelated and coincidental.  @David Grosher FYI.

### Alexander Alan Arnold, 2025-04-15

Should this be a Bermuda triangle? @Drew Hildreth @Pat Wells

### Christa Meck, 2025-08-05

@Eric Brewer and/or @Pat Wells I just read the report and I didn’t see any conclusion.  Did we decide this is probably related to SD card since we never got the booms back and weren’t able to do more testing with actual equipment?
I’ll leave this open until 12 Aug for feedback and then I am closing it Bermuda Triangle.

### Pat Wells, 2025-08-05

@Drew Hildreth @Jackson Riley Curvin @Alexander Alan Arnold See below from Christa
Please advise and close out if necessary.

### Eric Brewer, 2025-08-05

@Christa Meck @Pat Wells @Jackson Riley Curvin @Alexander Alan Arnold no updates from my end since the last post - I do not have definitive conclusions and i don’t believe this is being actively worked.

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20240909-221250.png | image | 23664 | 2024-09-09 | listed only |
| 00877723-deef-40e3-aae5-9556b2d35d30.jpg | image | 117 | 2024-09-10 | listed only |
| 820a80e1-8559-4ea5-886a-e1061e3f4986.jpg | image | 133 | 2024-09-10 | listed only |
| 912fb997-d871-4e56-aafe-512d54258cb4.jpg | image | 113 | 2024-09-10 | listed only |
| image-20240919-151655.png | image | 69 | 2024-09-19 | listed only |
