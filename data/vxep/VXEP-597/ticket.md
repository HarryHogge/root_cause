# VXEP-597: VXE 600 Nose cone fan failing to shut off after fuel cell cool down

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed, but added to Bermuda Triangle List
- **Resolution:** Cannot Reproduce
- **Priority:** Highest
- **Created:** 2024-09-03
- **Updated:** 2026-03-02
- **Resolved:** 2025-03-20
- **Reporter:** Pat Wells
- **Assignee:** David Grosher
- **Creator:** Pat Wells
- **Labels:** TIQUILA, Weekly-incident-tracker
- **Links:** relates to ENG-3086 (Nose fan failing to shut off); relates to FS2-2542 (VXEP-597 - Investigate state machine has no land transition data); relates to RMA-459 (VXE-600 Card Swap & Expansion 250429-9)
- **Customer:** TIQUILA
- **Vehicle Tail Number:** 600
- **Corrective Action:** Explanation of Normal Operational Behavior - Provided in Report
- **Issue Status:** Investigation & Report Complete, awaiting review and submission by @Pat Wells to customer.
- **Incident Type:** Other (Record"Event Type: XXXXXX" in the description)
- **Severity:** 4 - Annoyance

## Description

From LM FSR:
The nose fan on V530 and V600 failed to shut off once the fuel cell is cooled down.  GCS had already been packed up, so don’t have the actual temperature on V530, but V600’s fan was still running while temp was <100°C.  In both cases, battery power was disconnected while the fan was still running.
See photo of temperature reading attached.
AAR for V600 is attached for configuration.  Fuel cell might have cooled below 150°C before the FDR was successfully downloaded.

AAR attached

## Plan

- Sean to write a report for customer.
- Review Data to determine what is happening and whether the behavior is abnormal. 
- Determined to be normal and conflicting with data provided to team.
- Explain Nose Cone fan operation and when it should be operating to assist customer and close out investigation.

Report - Investigation Report VXE-530&600_9OCT2024.pdf

## Root Cause

Suspected Operator Error. Fuel Cell cannot operate Nose Cone Fan without connected to battery at described temperature/operation state as there are no other sources of power on aircraft. Possible partial disconnect of the battery by removing VTOL Harness (from center wing) and not Avionics/Fuel Cell/Nose Cone Fan harness (from Fuselage).

## Comments (37)

### Cameron Chapman, 2024-09-03

Assigning to @Sean Wendling . 
- It seems like there should have been a fuel cell shutdown command that may have been missed. 
- Is this documented in any training, automated, or prompted anywhere?
- Can the fuel cell provide a small amount of power at ~100C? This statement is surprising “In both cases, battery power was disconnected while the fan was still running.” Should be able to tell when the HLB was likely disconnected by looking at Vbatt, cell voltage, etc.

@Dana Holley if you know the fuel cell shutoff part.

### Dana Holley, 2024-09-05

@Cameron Chapman Yes - we train that way, however this sounds like the report was generated from Lockheed FSR. Also documentation does state to shutdown fuel cell in the Fuel Cell Postflight procedure.

### Cameron Chapman, 2024-09-07

We can also look for a shutdown command or lack there of in the command logs.

### Pat Wells, 2024-09-16

@Sean Wendling & @Cameron Chapman  checking in for any updates ahead of the Air Worthiness brief with TIQ on Wed 9/18

### Sean Wendling, 2024-09-17

To answer @Cameron Chapman , at 100C internal temperature the fuel cell is not able to make any energy. Fuel Cell chemical reactions don’t start occurring until at least 400C. 
I am looking through the data, and I am not exactly sure what happened here. Did they disconnect the battery while the fuel cell was running? The data appears incomplete as I can’t see the behavior in question, however, if the battery is disconnected and fuel cell is in cooldown, it should be impossible for the fan to be running. 
The nose cone fan is being directed to operate through the end of the data file, and I can see the fuel cell cooldown in the data. I don’t know how the fan would be running without battery being plugged in…. If battery was not connected, and fuel cell is off the only explanation I could think assuming what I mention above is that maybe wind was turning the fan blades on the ground? Data doesn't show high winds that day though..

### Cameron Chapman, 2024-09-17

[embedded: image-20240917-213158.png]

[embedded: image-20240917-213145.png]

[embedded: image-20240917-213243.png]
@Sean Wendling that makes sense and seems to be supported by the data.
When is the fan supposed to come on? From the data, it seems like it comes on during startup and cooldown, and disables when the fuel cell reaches temp. That seems backwards, unless the fuel cell provides its own cooling at that point.

### Sean Wendling, 2024-10-01

As discussed in the Incident Meeting today (10/1/2024), the data demonstrates normal Nose Cone Fan behavior. The Fan should be functional when the aircraft is not in forward flight while the fuel cell is on. The Fan does this, and this is not abnormal behavior to continue to operate until the battery is disconnected. 
Once fuel cell is off (or not in Operate/under 650C) it is not able to produce power, therefore without fuel cell or battery being connected, it is impossible that the nose cone fan be running. Data from below graph shows all available data, fuel cell cools down, battery still connected, after landing, the nose cone fan turns on and is on until the battery is disconnected.
[embedded: newplot (20).png]
We should be safe to close this issue.

### Sean Wendling, 2024-10-01

Hey @Cameron Chapman , I am lost in this workflow, how to I move this issue from D2 to Complete/D8? (Do you mind showing me so I can do it in the future without needing guidance?)

### Cameron Chapman, 2024-10-01

@Sean Wendling 
[embedded: image-20241001-205228.png]

[embedded: image-20241001-205254.png]

### Sean Wendling, 2024-10-09

Hey @Cameron Chapman , just want to confirm something about this ticket. in VXE aircraft (Fuel Cell Config) the Connector on the starboard side of the HLB is for main forward flight (ieFuel Cell in/out) power, and the other connector is for VTOL motors, right? I want to include clarification in the report that “disconnecting” the VTOL harness from the HLB does not constitute “disconnecting” the battery in case there is any misunderstanding. 
[embedded: image-20241009-141733.png]

### Cameron Chapman, 2024-10-09

@Sean Wendling Correct. The right one in the picture is for the avionics, fan, and forward flight.

### Sean Wendling, 2024-10-09

(@Sam Miller , @Cameron Chapman ) I reviewed a handful of flight logs and I see that if fuel cell is online/not in forward flight, in all cases, (even under 150C) the front nose cone fan is on. I wanted to check with you guys on this because I know yesterday there was a question of whether when <150C the nose cone fan should have shut off.  
I am going to advise the customer in the report that the fan is normally on when these two conditions are met: Fuel Cell is online (meaning connected and in FC config) and the aircraft is not in forward flight.  Before I do this, I wanted to make sure this is also your understanding so we don't confuse the customer and lead to more tickets like this haha. Thanks!

### Sam Miller, 2024-10-09

Thanks for looking into this Sean.  I have personally witnessed the front fan shutting off when the fuel cell cooled off.  We have trained that in the event you’ve packed up the GCS, the fan shutting off is the indicator that the fuel cell is cool enough to put in the case.  So I think either something’s broken in the code, something has changed, or the shutoff temp is different than we have assumed.

### Sean Wendling, 2024-10-09

Okay sounds good, I am glad that I asked haha. In that case I am going to be a bit ambiguous about that part and focus on the reported problem. Thanks!

### Cameron Chapman, 2024-10-09

@Sean Wendling , @David Grosher's group could provide the specific logic that turns on and off the fan (if needed, may not be worth investigating).

### Sean Wendling, 2024-10-09

@Cameron Chapman , Given how busy he is I’m not sure I want to push too far for this one. I have attached a copy of the report. Do you mind reviewing it quick to ensure it matches the preferred format and content is aligned with what we have discussed so far. Its very strange creating a report for something like this lol.

### Cameron Chapman, 2024-10-09

@Pat Wells @Sean Wendling would be the best person to review/edit documents that are going to a customer. I did a brief review, not in detail. It looks good. I think a conclusion/root cause section with a few sentences would be helpful.  Ex: Suspected operator error. Fuel cell fan cannot operate with battery disconnected (no power source).

### Sean Wendling, 2024-10-09

@Cameron Chapman great! I can add that and re-upload. 
@Pat Wells , I will tag you once final edits are complete. 
Thanks guys

### Cameron Chapman, 2024-10-09

@Sean Wendling I recommend deleting the upload and adding a link to sharepoint. Uploads are static and cannot add comments, track changes, etc. Sharepoint links allow a lot more collaboration. See locations here https://jenaero.atlassian.net/wiki/spaces/EF/pages/23363854/Incident+Troubleshooting+and+Resolution+Tracking.

### Sean Wendling, 2024-10-09

Hey @Pat Wells , Report is complete. Pdf and Word Copies are in the incident folder. If there are any edits you need me to make please feel free to reach out. Investigation Report VXE-530&600_9OCT2024.docx

### Pat Wells, 2024-10-14

@Sean Wendling report looks good. Thank you
I will pass along to TIQ customer.

### Pat Wells, 2024-10-14

@Sean Wendling It appears that we may have misunderstood what exactly was being reported here.
I received the following feedback from the customer:
When the subject aircraft landed, AARs were downloaded, tail booms and wings were removed, and the main batteries remained in and fully connected to the fuselages as the fuel cells cooled. His question was why did the nose cone fan continue to operate after the fuel cells had cooled down below the threshold temperature.  He notes and acknowledges that the batteries were connected during this anomaly. 

@David Grosher FYSA

### David Grosher, 2024-11-14

@Pat Wells This flight looks very strange. There were no transitions through the landing state machines that are typically there. I can see that it launched and transitioned to FW, but it simply detected a landing without having gone through the landing state machine, which is quite strange. This is likely why the fan did not shut off, since it needs to be in the landed state prior to checking the temperature threshold. I will likely need to have Jason look at this in more detail.

### David Grosher, 2024-11-14

This flight appears to have been glide landed, this may lead to a bug in the state machine resulting in the fan not being turned off. This needs to be further investigated to ensure it was safely recovered. 
@Pat Wells @Scott Whitney @Jason Scherer FYSA.

### David Grosher, 2024-11-15

@Eric Brewer Look at the state machine transitions that this vehicle went through to land. Make sure it is safe and consistent with glide landings.

### Eric Brewer, 2024-11-19

@David Grosher it looks like the fuel cell fan logic should work as expected.  I don’t have logs of the temperature going low enough to turn off (AAR is gathered before that), but with the glide landing the state machine ends up in FS_LANDED, which has the logic shown below. This should turn off the fuel cell once it’s cooled.
[embedded: image-20241119-155102.png]

[embedded: image-20241119-155201.png]

[embedded: image-20241119-155222.png]

### Eric Brewer, 2024-11-20

@Pat Wells , are we able to ask if there are any other logs available?  The captured AAR ends before the temp drops below the threshold to turn off the fan.  Looking at the code the logic should still work correctly to turn it off after a glide landing, so we’d need more data in order to determine why the fan would not be powered off.

### Pat Wells, 2024-11-20

@Eric Brewer  I will ask about additional logs.

### Pat Wells, 2024-11-21

@Eric Brewer added two additional AAR’s for VXE-530 that was mentioned as also having the same issue.  LM does not have any additional AAR’s.
Note, I did confirm with LM that both of these aircraft were glide landed.

@David Grosher FYSA

### Eric Brewer, 2024-11-21

@Scott Whitney FYI.

### Eric Brewer, 2024-11-21

thanks @Pat Wells .  Unfortunately none of these datasets show the case where the fuel cell is on and below temp but the fan is still on.  @Cody Smisek is going to look and see if we can find any example data from similar flight/FC shutdown here but otherwise we may need to ask them to gather data for us to debug this issue.  The command to shut down the fan does come from the autopilot though so if the autopilot is powered down and the fuel cell is still running that would explain why the fan doesn’t shut down.
@David Grosher @Scott Whitney FYI.

### Eric Brewer, 2024-11-25

@Pat Wells confirmed we do not have any data for this condition here, and we typically don’t do glide landings.  If this is a use case they plan to continue using until they can update to the latest software then we would need more data in order to debug this issue.
@David Grosher @Scott Whitney FYI.

### Pat Wells, 2024-12-05

@Eric Brewer any updates?  Is there path forward for this?

### Eric Brewer, 2024-12-05

@Pat Wells I do not think we can debug this without more data.  We specifically would want an AAR log set that includes the time when the temperature has reduced but the fuel cell fan is still on.  
The logsets I have, the XComm and fuel cell logs cut off when the reactor temp is still high.  If the flight logs have not been cleared it’s possible they are still on the aircraft.  The last xcomm log on the 133603 log set is ‘T95_V530_240822_133603_xcl00118.csv'.  If there is an xcl00119.csv/xcl00120.csv it’s possible these might contain the data we’re looking for.  If these logs do not exist, it may indicate the avionics were powered down before the incident, in which case I’m not positive would be a use case we had tested. @David Grosher @Scott Whitney FYI.

### Pat Wells, 2024-12-06

@Eric Brewer I’ll make the request one more time.
@David Grosher @Scott Whitney FYSA

### Pat Wells, 2025-03-17

@David Grosher @Eric Brewer receommend we send this to the Bermuda triangle.  Any objections?

### Eric Brewer, 2025-03-17

@Pat Wells no objections from me.

## Attachments (14)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| IMG_1595.jpeg | image | 1189 | 2024-09-03 | listed only |
| T95_V600_240823_101808_01_pack (1).zip | archive | 8167 | 2024-09-03 | listed only |
| image-20240917-213145.png | image | 30 | 2024-09-17 | listed only |
| image-20240917-213158.png | image | 34 | 2024-09-17 | listed only |
| image-20240917-213243.png | image | 46 | 2024-09-17 | listed only |
| image-20241001-205228.png | image | 13 | 2024-10-01 | listed only |
| image-20241001-205254.png | image | 28 | 2024-10-01 | listed only |
| newplot (20).png | image | 74 | 2024-10-01 | listed only |
| image-20241009-141733.png | image | 517 | 2024-10-09 | listed only |
| image-20241119-155102.png | image | 33 | 2024-11-19 | listed only |
| image-20241119-155201.png | image | 16 | 2024-11-19 | listed only |
| image-20241119-155222.png | image | 13 | 2024-11-19 | listed only |
| T95_V530_240822_133603_pack.zip | archive | 2259 | 2024-11-21 | listed only |
| T95_V530_240822_151625_pack.zip | archive | 1849 | 2024-11-21 | listed only |
