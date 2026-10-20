# VXEP-305: VXE 481 - Motor issues and voltage fluctations during preflight.

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-03-25
- **Updated:** 2025-05-20
- **Resolved:** 2025-05-20
- **Reporter:** Cameron Chapman
- **Assignee:** Rajesh Budhabhatti
- **Creator:** Cameron Chapman
- **Corrective Action:** 4:/23/24: Replaced power connector. Issue resolved.
- **Root Cause:** 4/23/24: Excessive contact resistance in power connector causing voltage fluctuation.

## Description

during a motor check, the VTOL motors weren't able to spin up, made strange noises (see the video) and the HLB% in the software went up and down between 70% and  90%.
Troubleshooting performed:
- Checked boom power connectors - fully inserted, no damage, desoldering observed
- Checked HLB power connector - fully inserted, no damage, desoldering observed,
- Replaced the HLB - problem was no longer present.
- Installed back the previous HLB - problem was no longer present (multiple attempts were made)

Sharepoint shared location for associated files: https://jenaero.sharepoint.com/:f:/r/sites/EngineeringTeam/Shared%20Documents/Investigations/481%20Incident%20VXEP-305?csf=1&web=1&e=Z8DXsH

## Plan

- Check AS150 impedance of 481 CW. - done 3/25; 480uOhms before cleaning, 240uOhms after
- Check if 481 contacts were tested previously? Record findings and latest readings in the shared sheet. - measured 163uOhms 11/7. Data in spreadsheet
- 4/23/23: Create shared sharepoint location, link in description.  File saved here:  Investigation template VXE-481 Motor issue and voltage fluctuation during preflight.docx
- Data review to link the time in the video to vbatt plots. Plots created using Log files in Excel since the log files would not load in flight analysis tool. Plots showing testing props 1-4 and homing all 4 props as in the video.
- Report findings.

## Issue Status

AS150 impedance measured 480 uOhms before cleaning, 240 after cleaning. Both fail (limit is 235 uOhms).
4/23/23: Charted Battery current and voltage in correlation to the video. Large voltage drop observed when motors tried to activate.

## Comments (14)

### Cameron Chapman, 2024-03-25

[Friday 12:13 PM] Artis Bertulis
Need your help guys. So during a motor check, the VTOL motors weren't able to spin up, made strange noises (see the video) and the HLB% in the software went up and down between 70% and  90%.
Troubleshooting performed:
- Checked boom power connectors - fully inserted, no damage, desoldering observed
- Checked HLB power connector - fully inserted, no damage, desoldering observed,
- Replaced the HLB - problem was no longer present.
- Installed back the previous HLB - problem was no longer present (multiple attempts were made)

Seems good to go, but the concern is - could it happen again, during launch or landing, can I have someone take a look at this and give the "go-ahead" or "stop", or some more checks to do?
FDR will follow shortly

C0352.MP4
[Friday 12:14 PM] Artis Bertulis

Artis Bertulis
Need your help guys. So during a motor check, the VTOL motors weren't able to spin up, made strange noises (see the video) and the HLB% in the software went up and down between 70% and 90%. Troubleshooting performed: Checked boom power connectors - fully inserted, no damage, desoldering observ…


T95_V481_240322_112823_pack.zip
[Friday 12:19 PM]
Dave Grosher added Cameron Chapman to the chat and shared all chat history.
[Friday 12:19 PM] John Clark
IBatt1 and 2 look wrong. (Third try)
 
[Friday 12:19 PM] Dave Grosher
Cameron Chapman see the video above?
[Friday 12:20 PM] Dave Grosher
Seems like it might be a hardware issue


[Friday 1:00 PM] Dave Grosher
Maxime or Jack could help with 300. 
[Friday 1:03 PM] Artis Bertulis
I keep spinning the motors arming/disarming them and I can't replicate it again
[Friday 1:03 PM] Artis Bertulis
Lift motor and HLB connectors were all fully engaged we did check those right after the fact
[Friday 1:04 PM] John Clark
Cameron Chapman, do you have a body to deliver CW 300?
[Friday 1:07 PM] Cameron Chapman
Possibly. Still at lunch heading back soon. You can ask around ees and meches to see who is not working on MAGNSS
[Friday 1:07 PM] Artis Bertulis
I'll ask if Carson or Dominic has time
like 1
[Friday 1:08 PM] Artis Bertulis
Please confirm that it's running the right code, the same hardware? Dave Grosher
[Friday 1:08 PM] Artis Bertulis
And where to locate it - Carson will pick it up and deliver
[Friday 1:09 PM] Dave Grosher
Maxime and/or Jack, I think can help with the HW. I confirmed with Maxime that it doesn't have any mods to the CW. 
[Friday 1:11 PM] John Clark
I don't see it on the shop floor. Do we know where it is?
[Friday 1:14 PM] Greg Fryer
john and I found it near my office.
[Friday 1:15 PM] Greg Fryer
John will get the Wing Case (Tail 300) to Carson
[Friday 1:15 PM] Artis Bertulis
Carson is notified
[Friday 1:16 PM] Greg Fryer
The package is on the move. 
[Friday 1:17 PM] John Clark
Mission accomplished. Package out for delivery...
[Friday 1:18 PM] Artis Bertulis
So now the problem is time, we might do the first flight today, but we will not complete the whole test. 
The next week is fully booked with SCO/x-kit and demos. 
We are already considering to do parallel flights to be able to do SCO flights for all the aircraft we can’t do because of everything going on. I don’t know where this fits into all of that. I kindly ask Dave GrosherGreg Fryer to discuss this with the management
[Friday 1:20 PM] Dave Grosher
Yeah, we will discuss. 
[Friday 1:27 PM]
Artis Bertulis added Garrett Gerdes to the chat and shared all chat history.
[Friday 1:30 PM] Cameron Chapman
Artis. Can you please red tag the cw and battery involved?
[Friday 1:31 PM] Cameron Chapman
if you have down time, you could download and post all of the 3/22 csvs, but we can get that after if not
[Friday 1:32 PM] Artis Bertulis
Will red tag, and get the files
like 1
[Friday 1:43 PM] Artis Bertulis

Artis Bertulis
Will red tag, and get the files


03.22 VXE481 VTOL files.zip
[Friday 2:14 PM] Artis Bertulis
Wing received
like 2
[Friday 3:09 PM] Artis Bertulis
Flight 1 completed, flight time 40 min, no major issues
like 2
T95_V481_240322_143516_pack.zip
T95_V481_240322_BURST010.csv
[Friday 3:09 PM] Artis Bertulis
That's all the time we have today
[Friday 3:47 PM] Cameron Chapman
I think hayden is headed to vacation and I need to work MAGNSS. Is someone able to write an incident for this issue and deliver the wing to the electrical team for contact testing? Thank you
[Friday 3:58 PM]
Cameron Chapman added Laszlo Juhasz to the chat and shared all chat history.
[Friday 3:58 PM] Cameron Chapman
Laszlo can help with the contact testing when the wing is available. Does anyone know when we will need a working 481CW again?
[Friday 4:04 PM] Greg Fryer
I believe it's in the plan to use for next week, I will get Dave G. to update us (we are in a mtg together).
[7:49 AM] Artis Bertulis
481s wing and the HLB is left at the engineering area to troubleshoot
like 1
[7:49 AM] Artis Bertulis
We’ll proceed testing with 300s center wing
like 1
[9:27 AM] Laszlo Juhasz
I'm on it..

### Mark Squillante, 2024-03-25

@Laszlo Juhasz measured AS150 impedance at 480 uOhms before cleaning. After cleaning measured 240 uOhms. Both readings are failing readings.

### Cameron Chapman, 2024-03-25

@Kelly J Furlong @Kyle DeBernardi @Emalee Johnson 481 will need a new dual current sense assembly. 
- Are we able to take one from inventory?
- Is anyone from FA available to install it?

FYI @Carl Graf @David Grosher @Sean Odell

### Laszlo Juhasz, 2024-03-25

With the help of Emalee just found out that, the failed AS150 connector measuring high resistance most likely was never tested for resistance. (at least there is no record of it).
Also, there is a significant discoloring and indication of heath on the HLB connector, I’m attaching for reference. The battery is located in the battery isolation cabinet.  
[embedded: IMG_20240325_134217975_HDR.jpg]

### Everett Werner, 2024-03-27

I know everything is high priority right now, is there an estimate on when this might be resolved? if its not priority right now thats understandable. If there is anything I can do to help let me know. I am hoping to use asset 481 sometime next week if possible.

### Emalee Johnson, 2024-03-27

@Cameron Chapman We have a shortage on the stickers (107-114271) for the dual current sense harness so please don’t take any of the ones in inventory. We have 6 dual current sense harnesses without the sticker that are in final inspection so if those pass we can give you one of those. We can give you guys a sticker once they are received but we want to save the stickered assemblies for production. 
If your team needs FA hours to fix the center wing then @Kyle England will be the point of contact for that. 
@Kyle DeBernardi @Kelly J Furlong @Sandra Lopez @Carl Graf @David Grosher @Sean Odell FYI

### Cameron Chapman, 2024-03-27

@Emalee Johnson without a sticker sounds great.
@Kyle England is your team available to install it? 
Thank you

### Emalee Johnson, 2024-03-27

@Cameron Chapman I have the harness from QC, do you want me to give it to final?

### Cameron Chapman, 2024-03-27

@Emalee Johnson yes please.

### Cameron Chapman, 2024-04-10

@Rajesh Budhabhattior @Mark Squillante  please see actions in plan.

### Rajesh Budhabhatti, 2024-04-10

Created and shared a folder in Investigation reports called VEX_481-Motor issues and voltage fluctuations during flight. I have a blank investigation template and will populate it as we go along.

### Rajesh Budhabhatti, 2024-04-10

Is this vehicle on floor?

### Rajesh Budhabhatti, 2024-04-11

Created investigation report using standard template. Added plots to match the behavior seen on the preflight video and saved here: Investigation template VXE-481 Motor issue and voltage fluctuation during preflight.docx

### David Grosher, 2025-05-20

Completed but didn’t follow process so canceled.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 03.22 VXE481 VTOL files.zip | archive | 5835 | 2024-03-25 | listed only |
| C0352.MP4 | video | 236058 | 2024-03-25 | listed only |
| IMG_20240325_134217975_HDR.jpg | image | 2815 | 2024-03-25 | listed only |
