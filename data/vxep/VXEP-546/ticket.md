# VXEP-546: VXE 470 transitioned to VTOL at 2400 AGL then crashed

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Confirmed
- **Priority:** Highest
- **Created:** 2024-08-20
- **Updated:** 2026-08-11
- **Resolved:** 2026-08-11
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Ted Trowbridge
- **Creator:** Alexander Alan Arnold
- **Labels:** GS_Closed, MARSOC, Software, Weekly-incident-tracker
- **Links:** relates to FS2-2185 (Investigate VXEP-546 (VTOL transition at > 2k' resulting in crash)); relates to FS2-2186 (Document Incident VXEP-546 (VTOL transition at > 2k' resulting in crash)); relates to GCSS-345 (Prevent "Pattern Altitude AGL" from being set to a very high altitude); relates to GCSS-352 (GCS creates mission MSL values based on the origin point instead of the terrain data); relates to FS2-2342 (VXEP-512 - Investigation and GCS CAs for Transition to VTOL above 2000ft); relates to FS2-2682 (VXEP-546 Test Case); relates to FS2-2736 (VXEP-546 Launch speedgoat from elevation >50ft from SLO Office); relates to FS2-2825 (Firmware CAs (VXEP-556) for Transition to VTOL above 2000ft)
- **Customer:** MARSOC
- **Vehicle Tail Number:** 470
- **Problem Type:** Other (explain in description)
- **Incident Type:** Aircraft Damage
- **Monitor Type:** None
- **Severity:** 1 - Flight Critical

## Description

Report received from operator Frank K:
STALKER 470 WAS SENT TO PLZ BY OPERATOR DUE TO TRACKING ANTENNA NOT FOLLOWING THE AIRCRAFT. OPERATOR SAYS THAT WHEN THE AIRCRAFT ENTERED PLZ PATTERN, IT BEGAN DESCENT AT ROUGHLY 2,400 FT AGL AND WENT TO 1,500 FT AGL BEFORE VTOL BATTERY DIED. IT BEGAN TO SPIRAL DOWN. THE OPERATOR WAS UNABLE TO ABORT VTOL IOT LOOK AT ALTITUED TABLE OR MANUALLY LAND. THE AIRCRAFT CRASHED INTO TREES, RESULTING IN CATASTROPHIC DAMAGE TO THE CENTER WING, BUT NOTHING ELSE.
ACCORDING TO THE OPERATOR AND GROUND CREW, CONTROL OF THE AIRCRAFT WAS TOTALLY LOST WHEN SENT TO ITS PRIMARY LANDING PATTERN. CENTER WING IS BEYOND REPAIR, BUT ALL OTHER PIECES AND COMPONENTS SEEM TO BE IN WORKING ORDER. 

AAR attached, missing VTOL data
Incident report attached
Current Investigation Report: Vehicle Investigation VXEP-546 v470.pptx

## Corrective Action

@Ted Trowbridge 
- The GCS should prevent VTOL transition at AGL altitudes too high to recover.
- The GCS has a bug where the AGL altitude of the patterns are not calculated correctly.  The issue becomes problematic when the GCS is not located near the area of operations and the AGL referenced from the GCS differs from the launch.

## Plan

- @Steve Gonzales to finalize report, CA tasks, and incident summary fields.
- Is there a max altitude where the aircraft will not enter VTOL descent? If not, could there be? @Jason Scherer 
- There is not currently a limit on altitude for VTOL transition prior to descent. A ticket has been created in the GCS project to prevent high altitude transitions like this from occurring. [GCSS-345] Prevent "Pattern Altitude AGL" from being set to a very high altitude - Jira (atlassian.net) @Ted Trowbridge
- Continue to update report with supporting data while waiting for mission file to confirm.
- Investigation report has been attached with initial supporting data. More data will be added to show timeline and refute alternative causes.

## Root Cause

GCS Software bug that calculates incorrect MSL values for mission waypoints when the origin is located at significantly different elevations.

## Comments (39)

### Jason Scherer, 2024-08-23

So, it looks to me like the launch point is actually incorrect. The launch point is not 316' MSL as the mission table suggests. The XComm log shows an MSL of 2,936' as the HOME point before launch. The Launch and the PLZ points are nearly on top of each other and yet have 3,224' of MSL difference in the mission table. 
The PLZ mission actually looks correct. It should have had the vehicle transition at ~600' AGL. Seems like since the launch point was incorrect the entire mission was incorrectly elevated. The vehicle should have descended from launch W1 to R2 as the elevation drops off quite a bit. Instead, the vehicle climbs another 1,500'. Then on the RTB the vehicle climbs again to achieve the true MSL. So, the mission has the PLZ over 3,200' above the launch point.
Somehow the launch point got an incorrect MSL value.

### Jason Scherer, 2024-08-26

Ok I have figured out what happened. The GCS/Origin point was set ~24km away at an elevation of ~16-23'. This is probably why the tracking antenna did not work as well. I was able to find the origin location in the AAR and mostly recreate the mission. I have a nearly identical mission view table now.
I’ll update the slides in the investigation report tomorrow morning.

### Jason Scherer, 2024-08-27

I’m not sure if the origin being far away was intentional, but after discussing this with Dave and team this is a corner case that should be supported. So, the root cause of this issue is a software bug that uses origin elevation instead of waypoint terrain elevation on mission updates.

### Jason Scherer, 2024-08-27

@David Grosher @Alexander Alan Arnold @Pat Wells I have updated the report based on the finding of the GCS software bug. Let me know if any further updates are needed.

### David Grosher, 2024-09-24

@Ted Trowbridge FYSA, see the CAs above.

### David Grosher, 2024-10-02

@Pat Wells @Sam Miller I think we should consider issuing an airworthiness notification regarding this issue.

### Pat Wells, 2024-10-04

@David Grosher talked to Sam about this today and he agress.
Would like to sync up sometime next week to discuss path forward.

### Pat Wells, 2024-10-08

@David Grosher is this investigation report that Jason produced cleared for release to customer?

### David Grosher, 2024-12-04

@Pat Wells Yes, this can be released. We are finishing up a fix.

### Pat Wells, 2024-12-20

@David Grosher @Ted Trowbridge 
The PMA-263 customer has come back with some questions regarding the advisory notice we released for this issue.  If possible could you please assist in answering the below questions?

What happens during Mobile operations? If an Operator has selected Mobile Mount antennas and has chase GCS on for example?  
Can we still perform Handoffs?  It has been awhile but if handing off to another GCS with a different antenna location that may be +/- 50 ft would this cause issues?

### David Grosher, 2024-12-20

@Scott Whitney FYSA

### Pat Wells, 2025-01-03

@Scott Whitney just checking back in reference the customer’s questions.

### Scott Whitney, 2025-01-08

@Pat Wells - We are working on ways to test this scenario. We will should have a response soon.

### Pat Wells, 2025-01-13

@Scott Whitney Thanks, standing by.  The customer has inquired multiple times now on this question.

### Pat Wells, 2025-01-15

@Scott Whitney @David Grosher just checking in for updates if any are available.
Thanks

### Scott Whitney, 2025-01-22

@Pat Wells , we are working on setting up the environment to answer PMA's questions. I will keep you updated

### Pat Wells, 2025-02-25

@Scott Whitney @David Grosher just checking in for updates if any are available.

### Scott Whitney, 2025-02-27

@Pat Wells - in regards to the original issue of the vehicle transitioning at 2400ft. There is a fix in the upcoming SW release 6.4. Below are notes:
Summary of the Issue 
- In 6.3.4 and earlier, the GCS would allow the vehicle to transition from Fixed-wing flight to VTOL Recovery at altitudes that are too high and would result in the Hybrid Lift Battery running out of power before safely landing.

Fix for the issue 
- Interlock on GCS for high-altitude GOTO to PLZ IP2+
- GCS fix for Elevation issue with moved origin (Will Rescind recent AN.
- Need to review with FLOPs

[embedded image-20250227-164214.png]


In regards to the questions from PMA:
Original question: “What happens during Mobile operations? If an Operator has selected Mobile Mount antennas and has chase GCS on for example? Can we still perform Handoffs?  It has been awhile but if handing off to another GCS with a different antenna location that may be +/- 50 ft would this cause issues?” 
In chase mode during mobile operations, the operators can still perform handoffs. The AC will stay at the current MSL even after the hand off to another GCS that is +/-50 ft. 
Chase mode example: If GCS1 has control of the AC and is in GCS Chase mode, then disconnects from the AC, and the AC will loiter for 2 minutes while trying to reconnect. If the AC and GCS do not reconnect, the AC will continue its mission. If another GCS (GCS2) were to connect to the AC and command Chase GCS, the AC would redirect to the GCS2 position at the same MSL regardless of GCS2's altitude.
The only issue I can anticipate is that the second GCS is at a higher altitude than the vehicle MSL and collides with the terrain.

### Christa Meck, 2025-08-05

@Scott Whitney @Ted Trowbridge @Alexander Alan Arnold Are we ok to close this investigation now that 6.4 is released?
Leaving open until 12 Aug for feedback.

### Alexander Alan Arnold, 2025-08-05

@Christa Meck @Pat Wells I do not know if the fix was ever implemented, if it wasn't then I say we cannot close it out.

### Jason Scherer, 2024-08-26

Ok I have figured out what happened. The GCS/Origin point was set ~24km away at an elevation of ~16-23'. This is probably why the tracking antenna did not work as well. I was able to find the origin location in the AAR and mostly recreate the mission. I have a nearly identical mission view table now.
I’ll update the slides in the investigation report tomorrow morning.

### Jason Scherer, 2024-08-27

I’m not sure if the origin being far away was intentional, but after discussing this with Dave and team this is a corner case that should be supported. So, the root cause of this issue is a software bug that uses origin elevation instead of waypoint terrain elevation on mission updates.

### Jason Scherer, 2024-08-27

@David Grosher @Alexander Alan Arnold @Pat Wells I have updated the report based on the finding of the GCS software bug. Let me know if any further updates are needed.

### David Grosher, 2024-09-24

@Ted Trowbridge FYSA, see the CAs above.

### David Grosher, 2024-10-02

@Pat Wells @Sam Miller I think we should consider issuing an airworthiness notification regarding this issue.

### Pat Wells, 2024-10-04

@David Grosher talked to Sam about this today and he agress.
Would like to sync up sometime next week to discuss path forward.

### Pat Wells, 2024-10-08

@David Grosher is this investigation report that Jason produced cleared for release to customer?

### David Grosher, 2024-12-04

@Pat Wells Yes, this can be released. We are finishing up a fix.

### Pat Wells, 2024-12-20

@David Grosher @Ted Trowbridge 
The PMA-263 customer has come back with some questions regarding the advisory notice we released for this issue.  If possible could you please assist in answering the below questions?

What happens during Mobile operations? If an Operator has selected Mobile Mount antennas and has chase GCS on for example?  
Can we still perform Handoffs?  It has been awhile but if handing off to another GCS with a different antenna location that may be +/- 50 ft would this cause issues?

### David Grosher, 2024-12-20

@Scott Whitney FYSA

### Pat Wells, 2025-01-03

@Scott Whitney just checking back in reference the customer’s questions.

### Scott Whitney, 2025-01-08

@Pat Wells - We are working on ways to test this scenario. We will should have a response soon.

### Pat Wells, 2025-01-13

@Scott Whitney Thanks, standing by.  The customer has inquired multiple times now on this question.

### Pat Wells, 2025-01-15

@Scott Whitney @David Grosher just checking in for updates if any are available.
Thanks

### Scott Whitney, 2025-01-22

@Pat Wells , we are working on setting up the environment to answer PMA's questions. I will keep you updated

### Pat Wells, 2025-02-25

@Scott Whitney @David Grosher just checking in for updates if any are available.

### Scott Whitney, 2025-02-27

@Pat Wells - in regards to the original issue of the vehicle transitioning at 2400ft. There is a fix in the upcoming SW release 6.4. Below are notes:
Summary of the Issue 
- In 6.3.4 and earlier, the GCS would allow the vehicle to transition from Fixed-wing flight to VTOL Recovery at altitudes that are too high and would result in the Hybrid Lift Battery running out of power before safely landing.

Fix for the issue 
- Interlock on GCS for high-altitude GOTO to PLZ IP2+
- GCS fix for Elevation issue with moved origin (Will Rescind recent AN.
- Need to review with FLOPs

[embedded image-20250227-164214.png]


In regards to the questions from PMA:
Original question: “What happens during Mobile operations? If an Operator has selected Mobile Mount antennas and has chase GCS on for example? Can we still perform Handoffs?  It has been awhile but if handing off to another GCS with a different antenna location that may be +/- 50 ft would this cause issues?” 
In chase mode during mobile operations, the operators can still perform handoffs. The AC will stay at the current MSL even after the hand off to another GCS that is +/-50 ft. 
Chase mode example: If GCS1 has control of the AC and is in GCS Chase mode, then disconnects from the AC, and the AC will loiter for 2 minutes while trying to reconnect. If the AC and GCS do not reconnect, the AC will continue its mission. If another GCS (GCS2) were to connect to the AC and command Chase GCS, the AC would redirect to the GCS2 position at the same MSL regardless of GCS2's altitude.
The only issue I can anticipate is that the second GCS is at a higher altitude than the vehicle MSL and collides with the terrain.

### Christa Meck, 2025-08-05

@Scott Whitney @Ted Trowbridge @Alexander Alan Arnold Are we ok to close this investigation now that 6.4 is released?
Leaving open until 12 Aug for feedback.

### Alexander Alan Arnold, 2025-08-05

@Christa Meck @Pat Wells I do not know if the fix was ever implemented, if it wasn't then I say we cannot close it out.

## Attachments (10)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [Copy of MISHAP Report 8333.xlsx](attachments/22496_Copy%20of%20MISHAP%20Report%208333.xlsx.md) | xlsx | 46 | 2024-08-20 | converted |
| T95_V470_240818_210151_pack.zip | archive | 2024 | 2024-08-20 | listed only |
| VTOL_VXE470ZIP.zip | archive | 86189 | 2024-08-20 | listed only |
| image-20240821-172011.png | image | 52 | 2024-08-21 | listed only |
| image-20240821-172100.png | image | 18 | 2024-08-21 | listed only |
| image-20240822-153542.png | image | 15 | 2024-08-22 | listed only |
| image-20240822-153651.png | image | 19 | 2024-08-22 | listed only |
| image-20240822-165049.png | image | 15 | 2024-08-22 | listed only |
| 20240819 Crash.PNG | image | 2770 | 2024-08-23 | listed only |
| image-20250227-164214.png | image | 9 | 2025-02-27 | listed only |
