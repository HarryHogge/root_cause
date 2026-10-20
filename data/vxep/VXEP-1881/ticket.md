# VXEP-1881: VXE 884 Mishap-Lift ESC Failure

- **Issue type:** Incident (8D)
- **Status:** D4 - Investigating Root Cause
- **Priority:** Highest
- **Created:** 2026-05-06
- **Updated:** 2026-10-20
- **Reporter:** Stephan Johnson
- **Assignee:** Samuel Lopez
- **Creator:** Stephan Johnson
- **Labels:** GS_Closed, Hardware, RCCA, USAACE_(2-13th), Weekly-incident-tracker
- **Links:** relates to RMA-1024 (VXE-884 RMA 260513-1); relates to VXEP-628 (Systemic VXE30 VTOL ESC Reliability Issues )
- **Customer:** USAACE
- **Vehicle Tail Number:** VXE-884
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical
- **Executive Summary:** Investigation on standby due to other priorities. Probable cause Hardware Failure.

## Description

Operator statement: 
At 1030 Local, the aircraft departed following successful preflight checks of all surfaces, servos, and motors conducted by SFC Garcia and CW3 Krabbe. Although the mission and flight routes were completed without initial issue, the aircraft exhibited anomalous behavior during its 1040 Local landing sequence; while in VTOL descent, the vehicle drifted and executed an uncommanded 90-degree turn to the south. At approximately 10 feet AGL, the aircraft pitched down and impacted the ground, resulting in the separation of the center wing. Immediately following the impact, the UGCS populated critical warnings regarding low energy, loss of GPS lock, and a lift system fault.

## Plan

- Synch with @Samuel Lopez for physical investigation status. If none, I recommend the following from the standard ESC troubleshooting steps here https://jenaero.atlassian.net/browse/VXEP-628 
- Inspect what can be seen before removing from boom (wire damage, smell of burning, prop/hub issues, etc. 
- If all seems normal, remove props. Run ESC with no propeller load. See if it runs normally. Record normal vs abnormal RPM, motor signals, etc.
- open ESC. Inspect/smell for damage.
- Run on dyno under load.
- Run flight profile on dyno. https://jenaero.sharepoint.com/:p:/s/FlightSafety/EXQUfU9atqRNh2r13Q3--m0BlJCaJUcm5OPxeeOmJEmdAQ?e=VZ0ObR

## Issue Status

Aircraft in SLO. Assigned investigation to @Samuel Lopez 
Summary of comments below: 
 it looks to me like a left front lift motor failure.  I’d inspect it for signs of damage.  Left front command goes high at the same time it pitches down and rolls left.


9_3_2026
Failure not reproducible in SLO.  Nevertheless, root cause is likely Left Front Motor.  Report is attached below.
https://redwireglobal.sharepoint.com/:p:/r/sites/FlightSafety/Shared%20Documents/Active%20Cases/VXE-884%20Left%20Front%20Motor%20crash/VXE%20884%20Investigation.pptx?d=w523b6693fca24990a72203723c8e6b3a&csf=1&web=1&e=y1k3NF

## Comments (37)

### Scott Lovett, 2026-05-12

Needs additional GS review

### Pat Wells, 2026-05-12

@Michael Mohr @Jackson Riley Curvin @Alexander Alan Arnold @Stephan Johnson where is the flight data on this?  I’m looking at an email that says we retrieved it. 
@Scott Lovett

### Drew Hildreth, 2026-05-21

@Michael Mohr @Stephan Johnson what is going on with this one? It’s in SLO now, need to know what we figured out so @Lauren Velasquez can push to the appropriate engineering team

### Michael Mohr, 2026-05-21

@David Grosher Would the CNo dropout towards the end of the recovery cause it to nosedive like they say it did?

### David Grosher, 2026-05-21

@Michael Mohr No, probably not. The Cno dropping is probably related to the aftermath. But I would need to dive into the details to know for sure. It sounds like the issue started earlier though. I would look into the drifting and turn first.

### Michael Mohr, 2026-05-21

@David Grosher Can I assign this to you then? It just showed up there.

### Drew Hildreth, 2026-06-01

@David Grosher can you get somebody to take a look at this one? Being the Army Schoolhouse, this is a going to raise some questions soon.

### Eric Brewer, 2026-06-02

@Drew Hildreth @Michael Mohr @David Grosher it looks to me like a left front lift motor failure.  I’d inspect it for signs of damage.  Left front command goes high at the same time it pitches down and rolls left.


[embedded: image-20260602-161554.png]

### Drew Hildreth, 2026-06-02

@Eric Brewer Eric, thank you for this.

### Drew Hildreth, 2026-06-02

@Lauren Velasquez @Zack Garcia See below comment from Eric. Please reach out to Cameron and find out who has bandwidth to look at this.

@Scott Lovett @Alexander Alan Arnold please start working on the report for this.

### Cameron Chapman, 2026-06-02

@Lawrence Nichols  can you work on this?

### Lawrence Nichols, 2026-06-02

@Eric Brewer could you please provide the matlab scripts that you utilize to plot this information?

### Eric Brewer, 2026-06-02

@Lawrence Nichols the script is checked in here:
data-analysis / matlab / flightAnalysis_vtol.m — useful-scripts — Bitbucket

I’m not sure how many MATLAB licenses we have within the company though so I’m not sure if the scripts are widely used outside the GNC group.  I believe someone was also working on converting this to python so it can be used by others - let me knwo if you want me to try to track that down for you.

### Lawrence Nichols, 2026-06-02

@Eric Brewer yes please it would be helpful for me to have for vehicle investigations and also other tasks where I need to analyze data. Atleast until grafana and the aar dashboard uploader are back up and running. It seems like i don’t have access to the linked repository, it also doesn’t show me an option to request access.

### Eric Brewer, 2026-06-03

@Lawrence Nichols sounds good.  I chatted with @Everett Werner and he will be putting together a version that you can use.

### Lauren Velasquez, 2026-07-07

@Cameron Chapman Customer is reaching out for an update/ warranty determination. Where are we on this investigation? I see Lawrence is no longer available. @Zack Garcia @Drew Hildreth   FYSA

### Cameron Chapman, 2026-07-07

@Lauren Velasquez @Drew Hildreth assigning to @Samuel Lopez who the EE team recommended as initial assignee for investigations. Please discuss with him where this fits in his priorities or with Greg you would like investigations to take higher priority over other tasks.
I will be available to help assignees with troubleshooting ideas, process, etc.

### Lauren Velasquez, 2026-07-17

@Samuel Lopez Customer is inquiring update on this unit, specifically warranty determination. Have we accomplished enough to make a determination on that? @Drew Hildreth @Zack Garcia FYSA

### Samuel Lopez, 2026-07-17

@Lauren Velasquez 

We have not.  I will move this near the front of the line.

### Lauren Velasquez, 2026-08-11

@Samuel Lopez Hi Sammy, Have we reached a clear disposition on this AC?

### Pat Wells, 2026-08-12

@Drew Hildreth @Alexander Alan Arnold given who the customer is on this we need to prioritize efforts on this investigation.

### Stephan Johnson, 2026-08-25

@Samuel Lopez have you had a chance to look at this bird now that it’s back in SLO?

### David Grosher, 2026-09-01

@Jeremy Kostel FYSA

### Samuel Lopez, 2026-09-03

@Stephan Johnson 
yes, please take a look at the following report.

https://redwireglobal.sharepoint.com/:p:/r/sites/FlightSafety/Shared%20Documents/Active%20Cases/VXE-884%20Left%20Front%20Motor%20crash/VXE%20884%20Investigation.pptx?d=w523b6693fca24990a72203723c8e6b3a&csf=1&web=1&e=y1k3NF

### Mathew Papaleo, 2026-09-21

@Samuel Lopez hey i took the motor in question out of the boom, and ran it on the bench test over in electronics. the motor does not home correctly after the signal harness is disconnected.

### Samuel Lopez, 2026-09-23

@Mathew Papaleo Let’s meet today to discuss this por favor

### Mathew Papaleo, 2026-09-24

@Samuel Lopez i removed the left front motor and brought it to electronics and found that the motor does not home correctly. maybe a fault of the motor or esc….

### Mathew Papaleo, 2026-09-25

in the report i noticed messages of low energy. how do lift motors behave when the hlb runs out of power?

### Lauren Velasquez, 2026-09-29

@Samuel Lopez Was there a clearer disposition made for this after your discussion w/ @Mathew Papaleo ?

### Samuel Lopez, 2026-09-29

@Lauren Velasquez Let me talk with Drew today about this.

### Stephan Johnson, 2026-10-01

@Jeremy Kostel do you think D4 is an accurate description of this, or can we update this to D6?

### Jeremy Kostel, 2026-10-02

@Stephan Johnson thanks for the ping. Reviewing this one today. Ill let you know if status should change

### Samuel Lopez, 2026-10-14

Upon further examination, it is determined that the left front motor over throttled because the VTOL commanded it and a re-examination was performed to establish why.  The center wing panel was opened and one of the brass ballast weights on the VTOL board stack was found to be hanging as shown below.   A closer look reveals that the nylon screws had broken off.
The question is, did the crash cause the ballast weight to break off inside the center wing panel?  Or had it previously broken off which then caused the MPU 9250 to miscalculate acceleration?

[embedded: image-20261014-182959.png]
[embedded: image-20261014-183221.png]

### Samuel Lopez, 2026-10-14

@Stephan Johnson I think we need to have just a few more discussions to make sure we understand root cause before saying moving to D6.

### Drew Hildreth, 2026-10-20

@Jeremy Kostel can we get a clear RMA Disposition on this. Customer is beating the PM up and we need to get this moved out.

### Jeremy Kostel, 2026-10-20

@Drew Hildreth We moved this one down the priority list in order to get work done on V932. Please advise on which you want worked
FYSA @Alexander Alan Arnold

### Drew Hildreth, 2026-10-20

@Jeremy Kostel Thanks Jeremy. Keep driving on 932 for now.

## Attachments (29)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| Fuse.jpg | image | 296 | 2026-05-13 | listed only |
| Payload.jpg | image | 233 | 2026-05-13 | listed only |
| boom1.jpg | image | 391 | 2026-05-13 | listed only |
| ctrtwing1.jpg | image | 218 | 2026-05-13 | listed only |
| ctrwing3.jpg | image | 648 | 2026-05-13 | listed only |
| ctrwing4.jpg | image | 202 | 2026-05-13 | listed only |
| cttrwing2.jpg | image | 225 | 2026-05-13 | listed only |
| elev1.jpg | image | 434 | 2026-05-13 | listed only |
| elev2.jpg | image | 278 | 2026-05-13 | listed only |
| fuse1.jpg | image | 270 | 2026-05-13 | listed only |
| fuse2.jpg | image | 337 | 2026-05-13 | listed only |
| fuse3.jpg | image | 333 | 2026-05-13 | listed only |
| fuse4.jpg | image | 158 | 2026-05-13 | listed only |
| fuse5.jpg | image | 200 | 2026-05-13 | listed only |
| lift1.jpg | image | 294 | 2026-05-13 | listed only |
| lift2.jpg | image | 191 | 2026-05-13 | listed only |
| rudder.jpg | image | 390 | 2026-05-13 | listed only |
| wing1.jpg | image | 240 | 2026-05-13 | listed only |
| wing2.jpg | image | 222 | 2026-05-13 | listed only |
| 884_VTOL.zip | archive | 343412 | 2026-05-19 | listed only |
| 884_XCOMM.zip | archive | 138604 | 2026-05-19 | listed only |
| AAR_V884_20260429T171550Z.zip | archive | 20085 | 2026-05-19 | listed only |
| 884 Fuselage Intake.jpg | image | 4046 | 2026-06-02 | listed only |
| [884 Intake.pdf](attachments/59633_884%20Intake.pdf.md) | pdf | 3572 | 2026-06-02 | converted |
| 884 Wing Box Intake.jpg | image | 4105 | 2026-06-02 | listed only |
| XCOMM_VXE884 full pull.zip | archive | 16833 | 2026-06-02 | listed only |
| image-20260602-161554.png | image | 241 | 2026-06-02 | listed only |
| image-20261014-182959.png | image | 21567 | 2026-10-14 | listed only |
| image-20261014-183221.png | image | 17206 | 2026-10-14 | listed only |
