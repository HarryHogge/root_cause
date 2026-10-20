# VXEP-1971: VXE 885 Erratic behavior in flight caused crash

- **Issue type:** Incident (8D)
- **Status:** D4 - Investigating Root Cause
- **Priority:** Highest
- **Created:** 2026-07-30
- **Updated:** 2026-10-20
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Samuel Lopez
- **Creator:** Alexander Alan Arnold
- **Labels:** Hardware, RCCA, Weekly-incident-tracker
- **Links:** relates to ENG-1750 (MPU-9250 Chips have high failure rate, are obsolete, and have a high rate of conterfeits.); relates to ENG-2047 (Green AP's (0002P01G) need to have gyro/accel pass/fail criteria reviewed); relates to VXEP-1827 (Air Data Board - Failures); relates to RMA-1100 (VXE-885 RMA 260831-1); relates to RMA-1104 (EPS6516); relates to VXEP-1840 (VXE 655 unable to connect); relates to VXEP-1838 (VXE 622 unable to connect); relates to VA-2937 (Update Mag/Accel Build Procedure to prevent use of excessive flux when soldering RF shield cover.)
- **Customer:** USAACE
- **Vehicle Tail Number:** VXE 885
- **Vehicle Configuration:** VXE 30 ADV NAV , battery, e140g2
- **Incident Type:** Aircraft Loss
- **Severity:** 1 - Flight Critical
- **Executive Summary:** aircraft undergoing hardware investigation in engineering.

## Description

DATE OF INCICDENT 7/29/2026

After launch the AV performed takeoff procedures with no issues and transitioned to mission area North of the runway. While loitering the operator was attempting to get the Epsilon software to establish link. The instructor walked them through the process with no indication of issues from the AV. Once video link was established the image showed the AV was at an odd angle. The instructor set the payload to pilot view to confirm and check the attitude indications of the AV. There were no warnings or signs of an issue outside of the attitude showing that the AV was doing barrel rolls and performing random dives before gaining lift and climbing for a short time before stalling and doing it again. After attempting to confirm the AV condition it was less than 300’ AGL and warnings began appearing on the software with the audible tones. By the time the operator and instructor were attempting to gain control the AV had struck the ground and lost link with the control station.

## Plan

- @Lauren Velasquez please deliver to engineering. @Jeremy Kostel and @Samuel Lopez  to coordinate investigation. Recommend testing and inspecting connection to FWAP gyro, and FWAP to XCOM
- Seems to be caused by FWAP gyro MPU9250 failure probably on the  1710P01A board
- Maybe linked to recent MPU9250 increased failure rate. Sammy to link. we also had quality issues with magacc boards a while ago, FOD, solder balls, etc. I think that was contained before 885, but worth checking.
- @Eric Brewer some FS ideas to potentially deal better with gyro failures.  
- Would land immediately have been a better COA than trying to recover FW control?
- Should there be a max gyro bias limit above which we flag something is wrong with the gyro before flight.
- If the gyro data freezes, should we stop using it in attitude calculations, and/or alert the operator/recommend land immediately?


GS Corrective Provide hardware for investigation through RMA Process.

## Issue Status

Summary of findings in comments: 
- looks like a gyro malfunction of some sort.  The gyro bias of the fixed-wing pitch gyro is over 10 degrees per second for most fo the flight, and then around the time of the attitude divergence the gyro reading is constant for tens of seconds

Root cause determined as excess flux on mag/accel board and internal report available for review.  Awaiting to hear from Dave Grosher if findings are sufficient to edit report as customer-facing.
VXE 885 Sharepoint
https://redwireglobal.sharepoint.com/sites/FlightSafety/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FFlightSafety%2FShared%20Documents%2FActive%20Cases%2FVXE%2D885%20FWAP%20Crash&sortField=Modified&isAscending=false&viewid=0c1aa895%2D9073%2D46b2%2Db705%2Dfcb1f8f035fb&newTargetListUrl=%2Fsites%2FFlightSafety%2FShared%20Documents&viewpath=%2Fsites%2FFlightSafety%2FShared%20Documents%2FForms%2FAllItems%2Easpx

## Comments (33)

### Lauren Velasquez, 2026-09-21

@Drew Hildreth AC cases have been tagged- if any components are removed, those should also be tagged.  Tags are available in the RMA cell.

### Samuel Lopez, 2026-09-22

@Jeremy Kostel @Cameron Chapman @Lauren Velasquez @Eric Brewer 

The instrument panel on the xcomm webpage of VXE 885 is down.  See images below.  However, the XCOMM is still working because it keeps re-loading new log files.  This likely means that XCOMM is still working while FWAP is down.  Conversely, instrument panel of VTOL webpage works fine.
Additionally, most of the autopilot measurements on the sensors webpage are dead.  The compass does not react to motion of the fuselage. 

Recommend removing the avionics box from the aircraft and opening it for visual inspection (solder balls, burn, etc).  If there is no visual irregularities, swap out fixed wing ap for a working asset to confirm that it’s solely the fixed wing and not xcomm, novatel, anything else.



[embedded Instrument Panel - 885.png]
[embedded image-20260922-215531.png]

### Cameron Chapman, 2026-09-22

@Samuel Lopez Sammy Lopez, nice work on this one. I agree with your recommendation. One idea before removing the FWAP, we may want to open and inspect and test the avbox as an assembly before removing the FWAP. Ex: if the issue is a loose connection, then that evidence might disappear when someone inspects and removes the FWAP. You might want to insert an engineering review at that point to see if any FWAP lights come on, loose connections, etc https://jenaero.atlassian.net/browse/VXEP-1971

### Jeremy Kostel, 2026-09-22

@Cameron Chapman agree with Cameron. Also, not sure how you were connecting to the aircraft @Samuel Lopez . If you were going through hood payload port, I would double check with a direct connection to AV box. Additionally, I think its usually worth it to power the AV box by itself on a bench and repeat the test before opening the box. If you already connected via grey alden with the avionics box by itself, you can ignore those steps.

### Samuel Lopez, 2026-09-25

@Jeremy Kostel 
September 24, 2026
The av box was removed from the aircraft and tested on the iron bird.  The instrument panel still reads all zero values as does the ap sensor data.
Next steps.  Open av box and look for loose connections, solder balls, etc.  If none found, replace the FWAP.
Av box has been opened. No visual irregularities.  Av box was then powered on the iron bird.  There are red flashing lights underneath the mag/accel board D8 and D7.  
Asset FWAP
An asset FWAP on production’s bench was observed to behave in the following way – D8 was permanently on and D7 is pulsing.  Per John Clark, “this is normal behavior.”
VXE-885 FWAP
On AV 885, both D7 and D8 are blinking twice and then taking a pause.  Abnormal.  Ribbon cable looks completely intact and jiggling it produces no effect.  Per John Clark, “this is undefined behavior.”  The FWAP may be resetting.
The 5V power supply measures 4.992V and is, then, not the problem.  Root cause nearly reduced to FWAP. 
Next steps. Will now replace VXE-885 FWAP with an asset FWAP and re-test av box.  Additionally, will test VXE-885 FWAP by itself using production setup.

### Samuel Lopez, 2026-09-29

@Drew Hildreth and @Jeremy Kostel 
This investigation concluded that the plane crashed due to breakdown of the microcontroller on the FWAP.  RW has known about susceptibilities of this obsolete component for some time.  The investigation report is in progress.  The last I heard, Connor Peebles is working to replace the FWAP with something similar to the VTOL stack.

I am working on the investigation at this time which I am pasting the description.  Please review at your own leisure.

### David Grosher, 2026-09-30

@Samuel Lopez what does “breakdown of the microcontroller on the FWAP” mean exactly? And what susceptibilities are you specifically refering to? 
The issue status above seems to indicate a bias on one of the gyro channels in the IMU, which is not the part of the microcontroller.

### Samuel Lopez, 2026-09-30

@David Grosher @Jeremy Kostel 

By ‘breakdown of the microcontoller’, I mean that there is a hardware problem with that component.  The controller has shutdown various parts of the circuit - including the mag/accel board since the buck converter responsible for powering it is disabled by the microcontroller.

By ‘susceptibilities’, as RW has known for some time, this microcontroller is an obsolete part that dates back to the 2000s and long since discontinued.  RW has known for a couple of years now that these are prone to defects due to humidity if improperly stored before assembly.  Even so, for this year, 23% of Fixed Wing APs become scrap.

### David Grosher, 2026-09-30

@Samuel Lopez @Jeremy Kostel To be frank, I don’t see the evidence in the discussion of this ticket or in the report to credibly link humidity, a buck converter, production scrap rate, the obsolescence of the part or anything beyond the failed IMU channel to this incident. The fact that a processor does not work as expected following a crash does not mean that it was the root cause of a crash.

### Jeremy Kostel, 2026-10-01

@David Grosher @Samuel Lopez Agree with Dave’s assessment here. I don’t believe we’ve reached a conclusion on this. While we did have issues related to storage and humidity - our processes have been changed to mitigate this issue. Additionally, I don’t believe the scrap rate applied here is relevant information, as that simply identifies that our production process successfully identifies non-conforming boards and removes them from the facility. I am meeting with Sammy today to talk through next investigation steps.

### Samuel Lopez, 2026-10-01

@Jeremy Kostel @David Grosher 

Thanks for your feedback.  I talked with Jeremy this morning and we have come up with a gameplan moving forward.  Today I will test the mag/accel board to check it’s functionality independent of the FWAP.

### Samuel Lopez, 2026-10-05

@David Grosher and @Jeremy Kostel 

Appreciate both of yours' feedback from last week.  After re-examining, here are the latest results.

The av box for #885 was used for all the following tests.
·       A test asset Fixed Wing AP with Tail# 1091 was swapped in. The ap sensors and instrument panels now functioned as expected.
·       The mag/accel board from the #885 FWAP was removed and soldered on to this working #1091 FWAP.  Once again, ap sensors and instrumental panel read zeroes.  This highly suggests that it’s the mag/accel board and not the full FWAP that is malfunctioning.
·       A fresh mag/accel board was then soldered on to the original #885 FWAP and re-tested on the same av box.  Ap sensors and instrument panels work normally again.  This confirms that the mag/accel board was at fault.
 
Initial assessment that microcontroller was defective was incorrect.  Furthermore, per John Clark, if the mag/accel board is defective, “the system almost certainly will not run since that's flight critical.”
Since there is a cover on the mag/accel board, the PCB is not able to be visually inspected for irregularities.  We can try to cut open the original #885 mag/accel board for visual inspection tomorrow.

### Jeremy Kostel, 2026-10-06

@Samuel Lopez Good findings. A few questions also shared over teams, but better to add info here:

1. I thought you initially reported that two different converters on the FWAP weren’t working? One with an enable pin, and one where the enable pin was left floating.
    1.1 Do both converters work with the MPU removed?
    1.2 Do both converters work with the good MPU/do they stop working on the known good FWAP with the bad MPU
    1.3 Any explanation for why the converter with a floating enable pin would stop working with a bad MPU?
- Understood the magAcc PCB is difficult to inspect, have you done any testing with the board by itself?
- Would be good to check for obvious shorts and or power via external supply and see if current draw seems appropriate

Ive also linked two different Jiras (V622 and V655) that are also reported MPU9250 failures

### Samuel Lopez, 2026-10-06

@Jeremy Kostel 
- Not quite, there are two converters called 5V and VSERVO both are LT1376-5 (of which both are five volt converters).  Only the VSERVO was disabled on the FWAP when the board wasn’t working.
- No.  Only the 5V works when the MPU is removed.
- Yes, they both work with the good MPU.  The VSERVO is disabled with the bad MPU.
- The reason the 5V converter works with the enable pin floating is because the datasheet shows that when floating, the converter will be default on.
- Inspecting the Mag/Accel PCB is today’s task.  Since it’s under a cover, Ben N advised to cut it open with an exacto knife.  There is a history of solder balls accumulating on the board underneath the cover though it was addressed in the Jira below.  Another thing I can try doing is to power the Mag/Accel board by itself and make sure the two
- LDOs are functioning.  If they are, that just about reduces it to the MPU 9250.

[VA-59] VXE509 CA - Implement checks on traveler for solder balls, F.O.D., and undried moisture before soldering the shield on. - Jira

### Samuel Lopez, 2026-10-06

October 6, 2026
@Jeremy Kostel @David Grosher 
At the previous update, the mag/accel from VXE#885 was placed on a working board #1091.  This caused the #1091 board to no longer work and for the ap sensors and other function to read zeroes.
The cover was cut off of the #885 mag/accel board and it was observed there was an excess of flux covering the circuitry (see photos below).  The board was then cleaned using alcohol and the #1091 FWAP re-tested.  After this, the ap sensors worked normally.  


[embedded Image (1).jpg]
I will post the before and after photos in the sharepoint.

### Jackson Riley Curvin, 2026-10-12

@Samuel Lopez  what are the next steps for this investigation?

### Samuel Lopez, 2026-10-13

@David Grosher @Jeremy Kostel 
Here is the link for the internal Investigation.  Dave, can if this looks satisfactory, I can modify this to make it customer facing.

https://redwireglobal.sharepoint.com/:p:/r/sites/FlightSafety/Shared%20Documents/Active%20Cases/VXE-885%20FWAP%20Crash/VXE-885%20Investigation%20-%20internal.pptx?d=wdb94409e6d4d472b828e46b079521db6&csf=1&web=1&e=uPkgV4
I am also working with Production Engineering to make a change to the build procedure advising our technicians not to use excess flux.
@Jackson Riley Curvin the investigation portion is mostly finished.  We are now just wrapping up the reports.

### Drew Hildreth, 2026-10-20

@Jeremy Kostel similar to 884, customer is beating the PM up about this one. Can you take a look at what Sammy provided below and give us a clear RMA Disposition so we can get this moving as well?
@David Grosher can you also take a look and let us know what you think.

### Jeremy Kostel, 2026-10-20

@Drew Hildreth We have a meeting to review the report with Dave tomorrow, but he may be able to get to it sooner.
As far as a dispo - this aircraft took substantial damage to pretty much every composite structure as well as some harness damage and we have now opened the avionics box.
If this is high priority, can we just get them a new aircraft? Turnaround time would likely be faster

### Drew Hildreth, 2026-10-20

@Jeremy Kostel Thank you Jeremy. Yes, it is a high priority. I assumed that it would basically need to be rebuilt.

### Samuel Lopez, 2026-09-30

@David Grosher @Jeremy Kostel 

By ‘breakdown of the microcontoller’, I mean that there is a hardware problem with that component.  The controller has shutdown various parts of the circuit - including the mag/accel board since the buck converter responsible for powering it is disabled by the microcontroller.

By ‘susceptibilities’, as RW has known for some time, this microcontroller is an obsolete part that dates back to the 2000s and long since discontinued.  RW has known for a couple of years now that these are prone to defects due to humidity if improperly stored before assembly.  Even so, for this year, 23% of Fixed Wing APs become scrap.

### David Grosher, 2026-09-30

@Samuel Lopez @Jeremy Kostel To be frank, I don’t see the evidence in the discussion of this ticket or in the report to credibly link humidity, a buck converter, production scrap rate, the obsolescence of the part or anything beyond the failed IMU channel to this incident. The fact that a processor does not work as expected following a crash does not mean that it was the root cause of a crash.

### Jeremy Kostel, 2026-10-01

@David Grosher @Samuel Lopez Agree with Dave’s assessment here. I don’t believe we’ve reached a conclusion on this. While we did have issues related to storage and humidity - our processes have been changed to mitigate this issue. Additionally, I don’t believe the scrap rate applied here is relevant information, as that simply identifies that our production process successfully identifies non-conforming boards and removes them from the facility. I am meeting with Sammy today to talk through next investigation steps.

### Samuel Lopez, 2026-10-01

@Jeremy Kostel @David Grosher 

Thanks for your feedback.  I talked with Jeremy this morning and we have come up with a gameplan moving forward.  Today I will test the mag/accel board to check it’s functionality independent of the FWAP.

### Samuel Lopez, 2026-10-05

@David Grosher and @Jeremy Kostel 

Appreciate both of yours' feedback from last week.  After re-examining, here are the latest results.

The av box for #885 was used for all the following tests.
·       A test asset Fixed Wing AP with Tail# 1091 was swapped in. The ap sensors and instrument panels now functioned as expected.
·       The mag/accel board from the #885 FWAP was removed and soldered on to this working #1091 FWAP.  Once again, ap sensors and instrumental panel read zeroes.  This highly suggests that it’s the mag/accel board and not the full FWAP that is malfunctioning.
·       A fresh mag/accel board was then soldered on to the original #885 FWAP and re-tested on the same av box.  Ap sensors and instrument panels work normally again.  This confirms that the mag/accel board was at fault.
 
Initial assessment that microcontroller was defective was incorrect.  Furthermore, per John Clark, if the mag/accel board is defective, “the system almost certainly will not run since that's flight critical.”
Since there is a cover on the mag/accel board, the PCB is not able to be visually inspected for irregularities.  We can try to cut open the original #885 mag/accel board for visual inspection tomorrow.

### Jeremy Kostel, 2026-10-06

@Samuel Lopez Good findings. A few questions also shared over teams, but better to add info here:

1. I thought you initially reported that two different converters on the FWAP weren’t working? One with an enable pin, and one where the enable pin was left floating.
    1.1 Do both converters work with the MPU removed?
    1.2 Do both converters work with the good MPU/do they stop working on the known good FWAP with the bad MPU
    1.3 Any explanation for why the converter with a floating enable pin would stop working with a bad MPU?
- Understood the magAcc PCB is difficult to inspect, have you done any testing with the board by itself?
- Would be good to check for obvious shorts and or power via external supply and see if current draw seems appropriate

Ive also linked two different Jiras (V622 and V655) that are also reported MPU9250 failures

### Samuel Lopez, 2026-10-06

@Jeremy Kostel 
- Not quite, there are two converters called 5V and VSERVO both are LT1376-5 (of which both are five volt converters).  Only the VSERVO was disabled on the FWAP when the board wasn’t working.
- No.  Only the 5V works when the MPU is removed.
- Yes, they both work with the good MPU.  The VSERVO is disabled with the bad MPU.
- The reason the 5V converter works with the enable pin floating is because the datasheet shows that when floating, the converter will be default on.
- Inspecting the Mag/Accel PCB is today’s task.  Since it’s under a cover, Ben N advised to cut it open with an exacto knife.  There is a history of solder balls accumulating on the board underneath the cover though it was addressed in the Jira below.  Another thing I can try doing is to power the Mag/Accel board by itself and make sure the two
- LDOs are functioning.  If they are, that just about reduces it to the MPU 9250.

[VA-59] VXE509 CA - Implement checks on traveler for solder balls, F.O.D., and undried moisture before soldering the shield on. - Jira

### Samuel Lopez, 2026-10-06

October 6, 2026
@Jeremy Kostel @David Grosher 
At the previous update, the mag/accel from VXE#885 was placed on a working board #1091.  This caused the #1091 board to no longer work and for the ap sensors and other function to read zeroes.
The cover was cut off of the #885 mag/accel board and it was observed there was an excess of flux covering the circuitry (see photos below).  The board was then cleaned using alcohol and the #1091 FWAP re-tested.  After this, the ap sensors worked normally.  


[embedded Image (1).jpg]
I will post the before and after photos in the sharepoint.

### Jackson Riley Curvin, 2026-10-12

@Samuel Lopez  what are the next steps for this investigation?

### Samuel Lopez, 2026-10-13

@David Grosher @Jeremy Kostel 
Here is the link for the internal Investigation.  Dave, can if this looks satisfactory, I can modify this to make it customer facing.

https://redwireglobal.sharepoint.com/:p:/r/sites/FlightSafety/Shared%20Documents/Active%20Cases/VXE-885%20FWAP%20Crash/VXE-885%20Investigation%20-%20internal.pptx?d=wdb94409e6d4d472b828e46b079521db6&csf=1&web=1&e=uPkgV4
I am also working with Production Engineering to make a change to the build procedure advising our technicians not to use excess flux.
@Jackson Riley Curvin the investigation portion is mostly finished.  We are now just wrapping up the reports.

### Drew Hildreth, 2026-10-20

@Jeremy Kostel similar to 884, customer is beating the PM up about this one. Can you take a look at what Sammy provided below and give us a clear RMA Disposition so we can get this moving as well?
@David Grosher can you also take a look and let us know what you think.

### Jeremy Kostel, 2026-10-20

@Drew Hildreth We have a meeting to review the report with Dave tomorrow, but he may be able to get to it sooner.
As far as a dispo - this aircraft took substantial damage to pretty much every composite structure as well as some harness damage and we have now opened the avionics box.
If this is high priority, can we just get them a new aircraft? Turnaround time would likely be faster

### Drew Hildreth, 2026-10-20

@Jeremy Kostel Thank you Jeremy. Yes, it is a high priority. I assumed that it would basically need to be rebuilt.

## Attachments (8)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| DOD SAFE-7Lpnr6NvEtRwzWtA.zip | archive | 381799 | 2026-07-30 | listed only |
| IMG_20260729_112529_125.zip | archive | 182865 | 2026-07-30 | listed only |
| VXE30 885.zip | archive | 6783 | 2026-07-30 | listed only |
| image-20260731-113127.png | image | 156 | 2026-07-31 | listed only |
| image-20260731-113300.png | image | 142 | 2026-07-31 | listed only |
| Instrument Panel - 885.png | image | 89 | 2026-09-22 | listed only |
| image-20260922-215531.png | image | 109 | 2026-09-22 | listed only |
| Image (1).jpg | image | 1929 | 2026-10-06 | listed only |
