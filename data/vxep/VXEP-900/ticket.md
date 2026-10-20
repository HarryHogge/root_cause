# VXEP-900: VXE 337 uncommanded aborted launches

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-01-15
- **Updated:** 2026-03-02
- **Resolved:** 2025-08-18
- **Reporter:** Pat Wells
- **Assignee:** Greg Fryer
- **Creator:** Pat Wells
- **Labels:** USASOC, Weekly-incident-tracker
- **Links:** relates to VXEP-608 (VXE 336 uncommanded aborted launch); relates to RMA-530 (VXE-337 RMA 250219-1); relates to FS2-2993 (Investigate VXEP-900 (v337)); relates to AV-14 (Stalker Air Vehicle Crit 2 (Workaround) Investigations)
- **Customer:** USASOC
- **Vehicle Tail Number:** 337
- **Plan:** Complete
- **Issue Status:** Complete
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround
- **Product/Tech Owner:** Greg Fryer

## Description

Statement from operator: 
AV 337 aborts itself within the first 20 feet of takeoff, and lands.
Jennings payload installed. SA camera was operational.
AAR attached.

Investigation Report: Vehicle Investigation VXEP-900.pptx
SharePoint Link: VXEP-900 - VXE 337 Uncommanded aborted launches

## Corrective Action

Immediate: (All complete)
Install missing bearing/bushing. Systemic: (All complete)
Review traveler/inspection for bushing check, since not visible after assembly. (Unclear if missed or incomplete maintenance action after delivery.)Update manual to emphasize step and care required.Ancillary (noted during investigation, but not germane to issue)
Include lift blade SN in travelers - already updated in new travelers.

## Root Cause

Functional:
- Motor 4 Lift Rotor installation was missing 1 of 2 bearings
- Causes: Motor 4 (Rear Left) appears to be underperforming causing the autopilot to overcompensate with increased throttle.
- Causes: Vehicle aborted launch due to excessive roll vibration.

Systemic (How was bushing missed)
- Unclear if production miss, or if maintenance step was done incorrect.

## Comments (51)

### David Grosher, 2025-01-16

@Cody Smisek Are they not following the procedure? Or, is there an issue with the hardware? Can we start an investigation.  If you don’t have time we can ask the flight science team to look at it.

### Cody Smisek, 2025-01-16

@David Grosher I went ahead and deleted my comment so we can follow the proper investigation process. 
Please assign to flight science team.

### Pat Wells, 2025-01-22

@David Grosher checking in for any updates on this.  Thanks

### David Grosher, 2025-01-28

@Pat Wells Can you link the previous ticket for this vehicle that had the same issue?

### Pat Wells, 2025-01-28

@David Grosher linked.

### David Grosher, 2025-01-28

@Pat Wells Is there a typo on one of these tickets, I see v336 and v337? @Jason Scherer FYSA
I see mentions of 337 in that other tickets comments. Perhaps there were two similar issues in the same investigation.

### Pat Wells, 2025-01-28

@David Grosher the previous linked investigation was two air craft in the exact same location doing that same thing.  No typo’s

### Pat Wells, 2025-02-03

@Jason Scherer has anyone had a chance to look at this?

### Jason Scherer, 2025-02-03

@Pat Wells Due to 6.4 release feature development, I have not had time to look at this yet.

Quick look right now. The launch abort was caused by a gyro fault. Looking deeper into the fault conditions in the code, this fault happens when we stop getting gyro data.  
DebugMsg Climb abort, VTOL controller fault
[15:18:06.391 936.391] DebugMsg   Sensor: gyro fault

### Pat Wells, 2025-02-12

@Jason Scherer anything further on this? The customer has reached out again for a status.

### Jason Scherer, 2025-02-12

@Pat Wells No further updates at this time.

### Pat Wells, 2025-02-12

@Jason Scherer do we need to get the aircraft in house for examination?
Really need some movement on this as the customer has requirements they can not meet with this aircraft grounded.
@Alexander Alan Arnold  FYSA

### Jason Scherer, 2025-02-12

@Pat Wells Is this incident more urgent than the 29 Palms miss-match SW report? I was informed that the 29 Palms report was the most important effort, so I am working through the backlog of incidents in support of that report. 
@David Grosher @Barry Mendez @Scott Whitney 
Need some guidance on Company priority. This ticket is one of 19 tickets I currently have for incident investigations of which over half are “highest priority”. Additionally, aside from investigations, I’m scheduled to support the integration of the Long Endurance Main Battery (LEMB) for the March LRR delivery which has also not started.

### Jason Scherer, 2025-02-12

Per Dave, this incident is next in line after the 29 palms investigations/report.

### Pat Wells, 2025-02-12

@Jason Scherer it is not higher priority. Was just hoping for some first look data for the customer since this has been in the queue for a month.

### Jason Scherer, 2025-02-21

I am now working on this investigation.

### Jason Scherer, 2025-02-22

@Cameron Chapman This vehicle aborted launch due to excessive roll vibration. The data indicates we might have an underperforming lift motor. Can you, or someone from your team review the data on slide 7 for confirmation and next steps. I am still looking for data to validate the gyro sensor is working, but it seems to be. I also need to confirm configs are correct, but the firmware is up to date.

@David Grosher FYSA

### Jason Scherer, 2025-02-22

I added the excel file I’m using to chart VTOL data to the SharePoint folder. Filename: T95_VT337_250115_101813_vtl00113-JS.csv

### Cameron Chapman, 2025-02-22

@Jason Scherer we could run this calculation, from this page. https://jenaero.atlassian.net/wiki/spaces/EF/pages/163446841/Troubleshooting+Guide+Common+Data+Review+Tasks+Comparisons 
If that provides additional information of an underpowered motor, the customer could either swap it and try again, or ship it back to us to investigate. ESCs and commonly sometimes motors have reliability issues. 
I would guess in likelihood.
- ESC
- Prop
- Motor


Power expected (based on throttle) vs actual comparison.
X= PWM
Y= power out (watts)
y = 0.0023x2 - 4.7378x + 2452.9
VTOL PWM to power expected.xlsx
 To covert from throttle value in vtol log to PWM
PWM = (Throttle value) * 855 + 1000
Liam may have added to plotter. See attached. Update this page if so.

### Jason Scherer, 2025-02-22

@Cameron Chapman I’ve plotted the expected power vs actual power of each boom. I’ve also plotted actual power of each boom compared with the expected individual motor power for comparison. Let me know what you think (slide 9). The data doesn’t seem conclusive to my untrained eye. I think the time scale is so quick that the averaging makes it hard to tell.
I updated my excel on SharePoint in case you think my charts are incorrect. I doubled checked them, and I believe I’m using the same calculations as your example.

### Jason Scherer, 2025-02-22

@Pat Wells  @David Grosher FYSA - This seems like an underperforming motor on the left boom which could be caused by ESC, Motor, or Props.
I’ll let Cameron review the recent power data I’ve plotted first, but given the chance this is simply a prop issue, what is the corrective action there? Do customers replace props themselves, do we send a tech to replace props, or do we just have them send the vehicle back to SLO for maintenance?

### Cameron Chapman, 2025-02-23

@Jason Scherer I think that equation is power per motor, but you the power measurement is for the whole boom. What do the plots like with adding y1+y2 with x1 x2 being the throttle of each motor? 
Did you check actual vs commanded roll, pitch, yaw? That may indicate something. 
I think if neither of these reveal anything, we should just request a close inspection of the prop and motor assembly, then if no issues, the whole motor assembly returned. We don’t seem to have enough data indicating a prop only issue. They should have spares available, or we could send one.

### Pat Wells, 2025-02-24

@Jason Scherer @Cameron Chapman The aircraft is on it’s way back to SLO for a closer look by your team.
It is an operator level maintenance task to replace lift props, motors and ESC’s.

### Eric Brewer, 2025-02-25

@Cameron Chapman I added those calculations to my scripts awhile ago.  The total power seems to line up with what’s measured but the estimated current does not, not sure if this indicates a voltage measurement issue (note this is not specific to this bird, rather this is about the same as the calculations normally look).

[embedded: image-20250225-141933.png]
For reference here is my code:

[embedded: image-20250225-142025.png]
Once we have the airplane in house we can have someone spin up the rotors and see if there is a vibe issue with the left rear.  The vibe filter that tripped the abort appears to look for frequencies in roughly the 30-70hz range (1800-4200RM).

### Rodney Linch, 2025-02-28

@Cameron Chapman - intake complete. Let me know if I can drop this off in Engineering. Thank you!

### Cameron Chapman, 2025-02-28

@Rodney Linch yes please. @Adrian Garcia can coordinate a motor test when available.

### Rodney Linch, 2025-02-28

Delivered, with tags, to the Engineering area.

### Cody Smisek, 2025-03-04

@Cameron Chapman @Adrian Garcia @Eric Brewer 
I just took a quick look at the hardware. Not sure how much more inspection we need to perform now. 
Immediately upon physical touch of suspect motor/rotor combination, I noticed the lift blade was not passing the ‘movement’ test. I removed lift blade from motor, and confirmed that a bushing was missing. (See photo). 
This appears to be root cause. In my opinion I don’t see any reason to continue further investigation. Let me know if I can assist further. 
[embedded: Media (42).jpg]
@Jason Scherer FYI

### Cody Smisek, 2025-03-04

added slide in presentation. Lift blade SN SB3105
I’m asking Desiray if she can provide information on how blade was delivered, as part of lift boom assembly or as a spare. Would likely be good to find out if these were customer swapped or came from Edge as an assembly, if the lift booms were tested here as is, hard to believe they’d pass inspection.

### Cody Smisek, 2025-03-04

Traveler versions at time of aircraft assembly did not include lift blade SNs (appears latest version do contain this information). Traveler added to folder

### Jeremy White, 2025-03-05

Are there any indications the customer modified software/hardware on VXE337?

### Pat Wells, 2025-03-05

@Cody Smisek I agree. I definitely want to know if this was caused by the customer.  I can’t imagine it would have passed SCO in this state?

### Cody Smisek, 2025-03-05

@Pat Wells @Jeremy White we will be unable to conclusively determine if this was delivered in this condition as the travelers do not contain the information required. 
We can review SCO flight test data to see if there was any similar vibration, but given they had 3 flights without issue, seems unlikely that data will provide anything either.

### Jeremy White, 2025-03-05

@Cody Smisek @Pat Wells I should have been clearer. This aircraft was used for the JHU Dead Center integration and has had issues since the integration event (I’m unsure how much/if they flew it prior). SOCOM Software Data Applications (SDA) is working with Anduril to integrate Lattice for Mission Autonomy on several systems. It does not seem like this was an issue here, but I wanted to confirm they had not modified any software/hardware prior to sending back to the customer (if we can).

I can provide additional data on Teams/call if interested.

### Pat Wells, 2025-03-05

@Cody Smisek are you finished with your report on this?  Can we move the aircraft back to RMA fo repair @Rodney Linch @Lauren Velasquez

### Cody Smisek, 2025-03-05

@Pat Wells I’m supporting other testing today and offsite. Seems very likely what I found was the cause. Have not had time to re review the state of the report. If no one else is going to review it from engineering then I’d say take it back and repair.

### Pat Wells, 2025-03-06

@Rodney Linch @Lauren Velasquez Please retrive this and have the lift prop bushing repaired.  Then SCO

### Rodney Linch, 2025-03-06

Roger.

### Cody Smisek, 2025-03-06

@Pat Wells I’ve added an additional slide to the presentation. I have no further inputs at this time. Would recommend this investigation findings go through review with someone else. Maybe @David Grosher ? 
Would also recommend that this aircraft is tested in the field and data is reviewed to confirm motor 4 is performing acceptably after repairs are complete. SCO data from the first 3 flights of aircraft had similar characteristics of incident flight.

### Pat Wells, 2025-03-06

@Cody Smisek in your last slide you stated “Motor defect” for the previous SCO flights. Are you talking about the missing bushing or potentially some other problem with the motor?

### Cody Smisek, 2025-03-06

@Pat Wells wording updated.

### David Grosher, 2025-03-06

@Cody Smisek @Pat Wells This looks good to me. I made some minor formatting changes.

### Cody Smisek, 2025-03-14

@Greg Fryer If we really stretch I can think of another 2 or 3 corrective actions related to training, autopilot automatic identification of motor issues, data analysis after SCOs, but I think those would be stretching. 
I made 1 corrective action that would help expedite the traceability of hardware. The traveler for this aircraft was not available digitally and is apparently stored in a private/restricted location. Not sure why. If we don’t think we need to make it public then I think this ticket is complete and can be closed. Assigned to you as I’m not sure who else could direct making those documents publicly shared and updated regularly.

### Pat Wells, 2025-03-17

@Cody Smisek I wanted to leave this open until after SCO so the data logs can be compared as per the request.

### Greg Fryer, 2025-04-16

@Cody Smisek @Pat Wells Finally getting back to real work, after LRR. We can certainly get them any time (digitized or not), if someone actually said no (vs. not knowing who to ask), please escalate to me directly.
I am more interested in making sure that we know how the part was omitted in production, or if it was a defective supplier part?

### Cody Smisek, 2025-04-16

As the SN for blades was not included during this timeframe of traveler version, I do not think we'll be able to determine if this was a production miss. @Greg Fryer 
Hardware looked practically untouched when we received it.

### Rodney Linch, 2025-04-16

@Cody Smisek - AAR data files uploaded from 4/15/2025 flight.

### Christa Meck, 2025-04-17

Removed parent to prep for Incident hierarchy change.  Parent is linked as Linked issue.

### David Grosher, 2025-08-15

@Greg Fryer I think this might be complete.

### Greg Fryer, 2025-08-15

For anyone watching, I am going to check the traveler/inspection steps on Monday, tweak the report to keep the CAs focused on causes, then close. Appreciate that the manual was already updated!

### Greg Fryer, 2025-08-18

Final comment for anyone watching. I have verified via Trevor that the work instructions call for the bushings, and also a quality check to verify install (since it cannot be checked after blade assy). PPT updated to end with itemized corrective actions. Closing.

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR 337 15 Jan 2025.zip | archive | 1233 | 2025-01-15 | listed only |
| image-20250225-141933.png | image | 35 | 2025-02-25 | listed only |
| image-20250225-142025.png | image | 53 | 2025-02-25 | listed only |
| Media (42).jpg | image | 129 | 2025-03-04 | listed only |
| T95_V337_250414_111903_pack.zip | archive | 2976 | 2025-04-16 | listed only |
