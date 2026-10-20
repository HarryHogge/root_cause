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
[embedded image-20241119-155102.png]

[embedded image-20241119-155201.png]

[embedded image-20241119-155222.png]

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
[embedded image-20241119-155102.png]

[embedded image-20241119-155201.png]

[embedded image-20241119-155222.png]

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
