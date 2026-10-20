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

[embedded image-20261014-182959.png]
[embedded image-20261014-183221.png]

### Samuel Lopez, 2026-10-14

@Stephan Johnson I think we need to have just a few more discussions to make sure we understand root cause before saying moving to D6.

### Drew Hildreth, 2026-10-20

@Jeremy Kostel can we get a clear RMA Disposition on this. Customer is beating the PM up and we need to get this moved out.

### Jeremy Kostel, 2026-10-20

@Drew Hildreth We moved this one down the priority list in order to get work done on V932. Please advise on which you want worked
FYSA @Alexander Alan Arnold

### Drew Hildreth, 2026-10-20

@Jeremy Kostel Thanks Jeremy. Keep driving on 932 for now.

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

[embedded image-20261014-182959.png]
[embedded image-20261014-183221.png]

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
