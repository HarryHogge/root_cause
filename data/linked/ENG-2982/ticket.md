# ENG-2982: VXE 339 Mishap. Abnormal readings, behavior, and slow descent led to HLB empty and crash

- **Issue type:** Problem
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-03-10
- **Updated:** 2025-06-02
- **Resolved:** 2025-04-22
- **Reporter:** Cameron Chapman
- **Assignee:** Greg Fryer
- **Creator:** Cameron Chapman
- **Links:** relates to ENG-766 (Improve/automate flight data review process. ); relates to RMA-100 (VXE-339: 230313); relates to ENG-2969 (VXE 371 Very slow Landing); relates to GCS-861 (check altitude discrepancy reported from baro.); relates to AIR-3 (runtime checksum of ADB firmware); relates to GCSS-31 (Evaluate adding a ‘calibration altitude’ display on the airdata calibration steps of the launch wizard); relates to ENG-2137 (Baro and OAT Sensors Require Software Acceptance Variables for Launch ); relates to VA-246 (Convert subtasks listed to independent issues where appropriate. ); relates to ENG-3242 (Evaluate adding a ‘calibration altitude’ display on the airdata calibration steps of the launch wizard); relates to ENG-3241 (Troubleshoot ADB.  ); relates to VA-249 (Want ability to transition to Fixed Wing landing if operator notices VTOL issue (ex going to slow or battery too low). Maybe a descend faster button as well); relates to ENG-3240 (Compare gains and cals to normal.); relates to VA-248 (Review/ evaluate addition of anomalous value flags during initial ADB calibration and assembly); relates to VA-247 (Can you pull configuration from ADB to check if corrupt?); relates to ENG-3239 (Review launch wizard measurements. Should they have prevented launch or triggered an abort?); relates to ENG-3238 (Review previous flights and launch wizard for similar symptoms. ); relates to ENG-3237 (Is there a checksum for the ADB processor. Could there be?)

## Description

Flight Data folder VXE 339 3-9-23 mishap
Detailed Tracking (fedex.com)

Here is these series event leading up to V339’s crash:
Several flights today with this configuration.
Relaunched without removing aircraft wing or restarting GCS software.
 
- Launched with Manual Nudge Override Buttons.

- Landed with Manual Nudge Override Buttons.

- Downloaded FDR.

 
- Start Launch Wizard.  Selected Fuel Cell power source (only option).

- Waiting for aircraft response Retry 1, 2, 3, 4, 5.  Timed out.

- IP GREEN.  Datalink RED.

- Confirmed aircraft radio connected in Silvus webpage.

- Receiving SA video in Media Client.

- AP not talking.

- Disconnected and tried to reconnect.  Aircraft #339 is not on the network.

- Logged into XComm.

- Sensor page showed lots of 0.00 and - - - .

- Hardware page, set Web Control: Override ON, AP Power: OFF, AP Power: ON, Web Control: Override OFF.  No affect.

- Utilities page, Soft Reset.  No affect.

- Disconnected HLB.  No affect.

- Disconnected propane manifold until nose cone fan shut off and fuel cell hand were spinning down.

- Connected HLB and propane manifold.

- Reloaded XComm page and logged in again.

- Commanded fuel cell Start in XComm Fuel Cell page.

- Connected to aircraft in GCS software.

 
- Launch Wizard and normal launch.

- <Test point was to command (glide) Land Immediately while in U-Drive and confirm still had U-Drive control.>

- Put aircraft in a ground track at 400 ft AGL down Runway 22.

- Activated U-Drive and confirmed left and right turn response.

- (Forgot to activate Emergency Glide Landing before next step.)

- Commanded Land Immediately, OK.

- Aircraft transitioned to VTOL and began a vertical descent.

- Activated User Landing Control.

- Response to joystick nudge inputs seemed to be Manual Nudge mode, but indicator said Autonomous.

- Landed on runway approximately 750 m NE of launch location.

- Comms were weak, FDR was downloading slowly, so it was cancelled.

- 

- Drove stand to aircraft and placed aircraft on stand.

- Ran through Launch Wizard with no issues.

- “Aircraft temperature above normal limits” warning 2 or 3 times during launch wizard.

- Upon launch, aircraft transitioned immediately and accelerated forward barely off the ground. (We have SA video of the launch.)

- Altitude indicated -21000 ft and increasing at what seemed like a normal rate.

- Commanded RTB.

- Commanded Go to IP4.

- Airplane flew the landing pattern but continued to climb to 1000-1200 ft AGL.

- After IP5, aircraft transitioned to VTOL and began to descend.

- HLB 83%.

- Aircraft descended very slowly.

- Enabled Land at Emergency LZ.

- Commanded Land Immediately.

- Popup said something about not enough energy for VTOL landing, executing emergency glide landing, but continued VTOL descent.

- HLB <50%.

- Tried to increase rate of descent with full deflection Position Nudge.

- HLB <30%.

- Tried to increase rate of descent with full deflection Manual Nudge.

- As aircraft descended below ~300 ft it pitched down, then pulled up repeatedly.

- Aircraft weather-vaned into a variable wind from the south and moved forward (south) and was no longer over the runway.

- Aircraft turned ~ 90° right.

- HLB = 0°

- Pitched down, then pulled up (with zero vertical speed) approximately 10 ft off of the ground.

- Pitched down and impacted the ground about 80° nose down approximately 114 m south on the PLZ.

- Commanded Fuel Cell Stop.

- Recovered aircraft.

- Removed HLB.  Volts = 15 volts

- Connected new HLB.

- Repeated attempts to download FDR failed, but downloaded 18 files, 2 MB).

 
- Moved all gear to the building.

- Hardwired GCS to the aircraft with center wing attached.  Connected GCS software to aircraft.

- Media Client recording.  Command Stop and it Starts again (set to “Always in Flight”).  Seems like the plane thinks it’s flying even after having power cycled multiple times.

- Created an AAR in the building.  FDR downloaded with no error (27 files, 7.5 MB).

- Red light on center wing does not come on when plane is powered up.

## Comments (29)

### Cameron Chapman, 2023-03-10

Thanks @Daniel Lloyd and @Garret Moose for the detailed problem recording and Dustin for the data review.
 
I created an JIRA incident for this issue. It should be easier to track troubleshooting there. Please respond and create subtasks there. I will paste the correspondence so far there.  https://jenaero.atlassian.net/browse/VIT2-230 
 
Also adding John Clark
 
Corrected LRF seems to be working well
The LRF and ADB both seem to be providing bad data at points. They are powered and communicate independently. (ADB gets 12V from and sends CAN to the avionics box, LRF gets 5V from and sends its signal reading to the Lift AP).  They do share an ODU connector at the ADP. The ground lines connect to different sources, but are tied together in the XCOM.
 
This could indicate one of the following:
- Issue with the ADP ODU connector.
- Issue with the ground reference signals.
- Some physical issue in the pod.
- Something in FW.

 
Questions
- Was the SA CAM working throughout?
- It seems like we can do more data review, but will likely want to test the equipment in person. Can we start shipping the aircraft to SLO?

 
Thank you,
|  | Cameron Chapman Electrical Engineering Supervisor Edge Autonomy – SLO (formerly Jennings Aeronautics) Email: cchapman@edgeautonomy.io Phone: (970)389-5904 |

 
Confidentiality Notice
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.
 
Export Control Notice
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.
 
From: Lloyd, Daniel <daniel.lloyd@lmco.com> 
Sent: Friday, March 10, 2023 8:44 AM
To: John Tucker <jtucker@edgeautonomy.io>; Gamble, Dustin <dustin.gamble@lmco.com>; Carson Buckley <cbuckley@edgeautonomy.io>; Artis Bertulis <abertulis@edgeautonomy.io>
Cc: Curran, Matthew <matthew.curran@lmco.com>; Moose, Garret <garret.moose@lmco.com>; Sam Miller <smiller@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>; Allen Gardner <agardner@edgeautonomy.io>
Subject: RE: V339 Incident Report
 
339 damage;
Nosecone, unrepairable
Fuselage, minor crack near nosecone
Tail boom, unrepairable
Vertical stabilizer, broken mount bolt
Center wing, upper surface stress crack, damage from contact with Trillium retract handle
Left wing tip panel, broken mount clip
Left lift boom, unrepairable, cracked near motor mount
Right lift boom, unrepairable, cracked near motor mount
Fuel cell, damaged
 
 
From: John Tucker <jtucker@edgeautonomy.io> 
Sent: Friday, March 10, 2023 8:18 AM
To: Gamble, Dustin (US) <dustin.gamble@lmco.com>; Carson Buckley <cbuckley@edgeautonomy.io>; Lloyd, Daniel (US) <daniel.lloyd@lmco.com>; Artis Bertulis <abertulis@edgeautonomy.io>
Cc: Curran, Matthew (US) <matthew.curran@lmco.com>; Moose, Garret (US) <garret.moose@lmco.com>; Sam Miller <smiller@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>; Allen Gardner <agardner@edgeautonomy.io>
Subject: EXTERNAL: Re: V339 Incident Report
 
@Carson Buckley @Artis Bertulis for visibility 
 
Get Outlook for iOS
From: Lloyd, Daniel <daniel.lloyd@lmco.com>
Sent: Friday, March 10, 2023 5:18:43 AM
To: Gamble, Dustin <dustin.gamble@lmco.com>
Cc: Curran, Matthew <matthew.curran@lmco.com>; Moose, Garret <garret.moose@lmco.com>; John Tucker <jtucker@edgeautonomy.io>; Sam Miller <smiller@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>; Allen Gardner <agardner@edgeautonomy.io>
Subject: Re: V339 Incident Report
 
Thanks Dustin. I was able to get a more complete AAR last night but had Wi-Fi issues with getting it sent.
What was interesting in the shop last night was that when I connected to the aircraft it immediately started reporting fluctuations in altitude and high/low temperature warnings. Those eventually settled down to normal.
On Mar 10, 2023, at 05:06, Gamble, Dustin (US) <dustin.gamble@lmco.com> wrote:
﻿
That is an insane flight.

I think the entire event was driven by an airdata pod failure.

The xcomm log shows it transition right off the ground. It went full power on the VTOL and fixed wing all together. The laser range finder was reading 4ft off the ground as it was gaining airspeed for fixed wing flight.

The altitude reading from the barometric sensor in the air data pod was all out wack. The sensor was slewing from -32,733 to 32,563 which happens to be the range of a 16 bit integer. When it read high, that likely tricked the system to transition right away. The reverse happened on landing, when it saw low it made it think it was nearly on the ground so it did the super slow descent. GPS read 1ft/s VTOL descent. GPS shows vehicle started at 2,500 ft MSL and was a max of 3,359ft MSL or 859ft. That is the altitude it started its landing. The VTOL system was descending at ~1ft/s for 250 seconds. VTOL battery depleted at 2,978 ft MSL or 478 ft AGL.

The baro data comes in over CAN and we can confirm both the xcomm and VTOL controller recorded the erratic behavior. The temperature from the pod was also erratic, from -145.9 to 271.6 F. The airspeed was reading about 20 ft/s less than the GPS ground speed.

VTOL data is partial. The csv log only has the launch then it stops. No VTOL event log.

I don't think we have ever had a failure like this. There was no protection in the system to deal with it.

We will want to inspect and test the airspeed/baro pod. The pod could have lost it calibration. The xcomm can command the air data pod to do a calibration test which would mess it up but I don't see those messages in the xcomm event log.

I don't know how it can go from working fine all day to suddenly not working. For timing of events, the airdata baro readings go erratic 50 second after the launch wizard motor test or 118 seconds before the launch from the xcomm log. That timings needs a double check.

xcomm log has lots of DebugMsgInt Bus Faults and VAux messages. Also MESSAGE_VTOL 2  6. I don't know what those mean.

In addition to rooting this issue we need descent rate control in VTOL manual mode. That is an old request of mine from during VTOL development that I never got.


________________________________
From: Curran, Matthew (US)
Sent: Thursday, March 9, 2023 9:03:27 PM
To: Lloyd, Daniel (US)
Cc: Gamble, Dustin (US); Moose, Garret (US); John Tucker; Sam Miller; Cameron Chapman; Allen Gardner
Subject: Re: V339 Incident Report
Thanks. Good report.  Glad nobody was hurt.
Please remain in place for follow up testing tomorrow.
 I let MARSOC know we had an issue and we will keep them informed as we figure it out.  I did not elaborate, but we will need to.

On Mar 9, 2023, at 8:30 PM, Lloyd, Daniel (US) <daniel.lloyd@lmco.com> wrote:
﻿
Not sure this went out to everyone.

Begin forwarded message:
From: "Moose, Garret (US)" <garret.moose@lmco.com>
Date: March 9, 2023 at 19:22:08 PST
To: "Lloyd, Daniel (US)" <daniel.lloyd@lmco.com>
Subject: V339 Incident Report
﻿

Cheers,
Garret Moose
Stalker sUAS, Lead Instructor
Lockheed Martin Aeronautics Company
661-264-7130
** WARNING: This email originated from outside of the organization. Do not click links or open attachments unless you recognize the sender and know the content is safe. **

### Daniel Lloyd, 2023-03-10

The SA camera video was recorded as expected.

### Cameron Chapman, 2023-03-10

Here’s another AAR I got while in the shop. It looks like it may have everything.
 
Dan
 
From: Lloyd, Daniel (US) 
Sent: Thursday, March 9, 2023 6:24 PM
To: Curran, Matthew (US) <matthew.curran@lmco.com>; Dustin Gamble (US) (dustin.gamble@lmco.com) <dustin.gamble@lmco.com>; Moose, Garret (US) <garret.moose@lmco.com>; John Tucker <jtucker@edgeautonomy.io>; Sam Miller <smiller@edgeautonomy.io>; 'Cameron Chapman' <cchapman@edgeautonomy.io>
Subject: Aircraft 339 Mishap
 
Here’s the AAR. It kept getting an error downloading so have a look at this while I try to FTP the rest of the stuff.

### Daniel Lloyd, 2023-03-10

Added SA video

### Cameron Chapman, 2023-03-10

Update to earlier comment. The LRF seems to be operating normally, it read accurately 4ft due to low transition.

### Former user, 2023-03-10

Dan shipping back to SLO today
Detailed Tracking (fedex.com)

### Daniel Lloyd, 2023-03-10

Uploaded all AAR’s from Thursday flights

### Dustin Gamble, 2023-03-10

The fixed wing autopilot YawTemp matchs Xcomm xcl radOAT. Can we confirm YawTemp is from the airdata pod and not from the temperature sensor on the gyro inside the autopilot.

### Dustin Gamble, 2023-03-10

My messy excel sheets
[embedded: T95_V339_230309_162437_fdrrecov.xlsx][embedded: T95_VT339_230309_162437_vtl00023.xlsx][embedded: T95_V339_230309_162437_xcl01131.xlsx]

### Cameron Chapman, 2023-03-13

Fedex says we were closed when we were definitely open. Asking about them attempting again today
[embedded: image-20230313-172151.png]

### Cameron Chapman, 2023-03-13

@John Clark or @Kurt Burian is there any firmware or other information you recommend pulling from this ADB before we electrically test it?

### Former user, 2023-03-13

@Cameron Chapman  I don’t know of any other FW details. FYI VXE339 cases just arrived and are in inventory cage. I can bring them over shortly

### Connor Peebles, 2023-03-13

@Former user I acquired them, in engineering now

### John Clark, 2023-03-14

@Cameron Chapman ADB is completely managed by Kurt. Save whatever you can and proceed. Kurt is unavailable until after 3/17

### Cameron Chapman, 2023-03-16

@Connor Peebles , can you please update the investigation status (discoveries) and plan (proposed or planned steps, who should perform each) fields for this issue, and add a date updated for each? See my older email for how to fill those out.

### Connor Peebles, 2023-03-20

FYI @Maxime Jeanneau

### Kurt Burian, 2023-03-23

Hey, you guys ran into the glitch https://jenaero.atlassian.net/browse/VIT2-228  . That's why the plane didnt descend and the HLB died. @Cameron Chapman @Connor Peebles The bad airdata goofed the baro altitude and it started bouncing between states because of the sensor disagreement. We found this results in a 0.5 ft/s descent rate and the vehicle seemingly unresponsive in the linked issue.

### Connor Peebles, 2023-03-24

@Kurt Burian So from the multitude of sensors involved, if one/some start to disagree it could lead to this same glitch? And in 339’s case the faulty sensor is isolated to the Air Data

### Kurt Burian, 2023-03-27

@Michael Berger Quick suggestion for GCS improvements. We should have a ‘calibration altitude’ display on the airdata calibration steps of the launch wizard. We can make something automated to detect this, but if someone noticed 20k foot calibration rather then 2492' GPS altitude, we might have noticed this. I’ll post a chart reviewing the data shortly.

### Kurt Burian, 2023-03-27

[embedded: image-20230327-221942.png]
Laser only got a few blips near the ground. If pitch/roll > 20 degrees, the laser answer is unusable and ignored. More importantly, baro alt was all over the place +/- 20,000 ft. During cal the laser agl got a positive offset which caused the glitch during landing.
[embedded: image-20230327-222144.png]

### Connor Peebles, 2023-03-29

Setting investigation to review, corrective actions may be linked to new tickets.
Assigning to @Cameron Chapman for further disposition, FYI @Greg Fryer

### Greg Fryer, 2023-03-29

@Former user Is the incident report (spreadsheet) still being maintained? If so this one advanced. We should probably review with Sam regardless (and possibly others). 
@Cameron Chapman We should have a review before we actually execute the Corrective Actions. I am not sure the right answer is to display more data and ask the user to make another check. e.g. might be a place for us to pilot our “check for faults, and only bother the user if we detect one” approach. (Specifically for the GCS fix suggestion)

### Cameron Chapman, 2023-03-30

@Greg Fryer Agreed. We should automate where possible. Pilots already have many things to manually check. 
Seems like we need to identify who can review problems to approve determined cause and corrective actions (Problem review board?). Do we have anyone officially in charge of that? Not that I know of.

### Sean Odell, 2023-05-11

@Greg Fryer Is this aircraft in the position for me to take and complete the Quote for repair yet?

### Greg Fryer, 2023-05-18

@Sean Odell Yes. @Connor Peebles has repaired the Air Data Board on 339, but we recommend replacing the air data pod with a factory-fresh one. Please execute (will put this in the RMA as well).

### Greg Fryer, 2023-05-18

Advanced to working CAs. Unlikely all will be immediately tackled, based on workload of other critical issues. 
Cameron - regarding your note about moving them to independent issues, i have been carefully wording the sub-tasks so that they are an assignment to the right person to evaluate the question, and create a separate issue if so.

### Greg Fryer, 2023-05-18

@John Clark Please look at the sub tasks.

### Cameron Chapman, 2023-08-24

Linking subtasks to parent.

### Matt Philley, 2024-09-30

The 107-101649 SA Camera Assembly was pulled from this ADP to support bench testing for Engineering potentially for Heated Pitot project. Assy has been marked NOT FOR FLIGHT since it was removed from a Customer aircraft that was part of a root cause investigation, but SA Cam Assy was pulled since it was not linked to the cause. 

[embedded: image-20240930-171348.png]

## Attachments (22)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [339 XComm Remote Air.pptx](attachments/13021_339%20XComm%20Remote%20Air.pptx.md) | pptx | 1091 | 2023-03-10 | converted |
| MISB-03092023-162139-0.mpg | video | 31332 | 2023-03-10 | listed only |
| T95_V339_230309_113607_pack.zip | archive | 2372 | 2023-03-10 | listed only |
| T95_V339_230309_124929_pack.zip | archive | 1780 | 2023-03-10 | listed only |
| T95_V339_230309_142333_pack.zip | archive | 3417 | 2023-03-10 | listed only |
| T95_V339_230309_144317_pack.zip | archive | 3362 | 2023-03-10 | listed only |
| T95_V339_230309_151141_pack.zip | archive | 3324 | 2023-03-10 | listed only |
| T95_V339_230309_160510_pack.zip | archive | 1563 | 2023-03-10 | listed only |
| T95_V339_230309_162437_02_pack.allow | other | 2060 | 2023-03-10 | listed only |
| [T95_V339_230309_162437_fdrrecov.xlsx](attachments/13033_T95_V339_230309_162437_fdrrecov.xlsx.md) | xlsx | 807 | 2023-03-10 | converted |
| T95_V339_230309_162437_pack.zip | archive | 433 | 2023-03-10 | listed only |
| [T95_V339_230309_162437_xcl01131.xlsx](attachments/13034_T95_V339_230309_162437_xcl01131.xlsx.md) | xlsx | 9758 | 2023-03-10 | converted (cut) |
| T95_V339_230309_180102_pack.allow | other | 7533 | 2023-03-10 | listed only |
| T95_V489_230228_112205_pack.zip | archive | 2392 | 2023-03-10 | listed only |
| [T95_VT339_230309_162437_vtl00023.xlsx](attachments/13035_T95_VT339_230309_162437_vtl00023.xlsx.md) | xlsx | 4728 | 2023-03-10 | converted (cut) |
| [V339 Incident Report.docx](attachments/13016_V339%20Incident%20Report.docx.md) | docx | 17 | 2023-03-10 | converted |
| T95_V339_230310_134705_pack.zip | archive | 9982 | 2023-03-11 | listed only |
| image-20230313-172151.png | image | 34 | 2023-03-13 | listed only |
| image-20230327-221942.png | image | 154 | 2023-03-27 | listed only |
| image-20230327-222144.png | image | 154 | 2023-03-27 | listed only |
| 20230519_120102.zip | archive | 229842 | 2023-05-19 | listed only |
| image-20240930-171348.png | image | 467 | 2024-09-30 | listed only |
