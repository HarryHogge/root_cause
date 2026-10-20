# VXEP-1987: VXE 1016 Battery warning aircraft RTB

- **Issue type:** Incident (8D)
- **Status:** D6 - Implementing Corrective Actions
- **Priority:** Highest
- **Created:** 2026-09-01
- **Updated:** 2026-10-07
- **Reporter:** Michael Lindsay
- **Assignee:** Ted Trowbridge
- **Creator:** Michael Lindsay
- **Labels:** MOLSON, RCCA, Weekly-incident-tracker, battery
- **Links:** relates to VXEP-1557 (VXE 930 Main battery to avionics power chain led to emergency landing); relates to VXEP-1865 (VXE 930 - Vehicle broke orbit, wouldn’t take commands and behaved erratically.)
- **Customer:** MOLSON
- **Vehicle Tail Number:** 1016
- **Vehicle Configuration:** VXE30 Adv Nav, Battery Configuration
- **Problem Type:** Production Issue
- **Root Cause:** Operator flying outside of wind limits. Battery endurance estimates not accurate in those conditions.
- **Incident Type:** Mission Failure/Abort
- **Severity:** 1 - Flight Critical
- **Executive Summary:** Probable cause based on CA would point to Operator Error.

## Description

During the last flight of the day, with approx. 2 hours of remaining endurance, the aircraft was around 14 kms away at 2000 ft when we received a battery warning and the aircraft completed a RTB.  The aircraft landed with approx. 75 mins of endurance remaining.
Location: Tuktoyaktuk NWT Canada
Main Battery SN: 3-2229

## Corrective Action

@Scott Whitney does your team want to review this and make endurance estimates more accurate above wind limits, warn operators they are flying above limits, or just remind them not to fly above limits and close? 
- Ex: if power consumption is consistently outpacing estimated endurance rate, shouldn’t remaining endurance adjust to new rate?

@Drew Hildreth determine how we want to discuss wind limits with customers and impact on endurance.

## Issue Status

--Smisek Notes--
See comments. TLDR system appears to be operating as currently designed. It’s relatively accepted by experienced operators that the endurance remaining values are not great. 
During this flight the system was operated at and beyond current published environmental limitations. During cruise, AP indicated up to 60fps of wind (60fps = 40.9mph). On the ground the IAS was jumping from 20fps up to 32fps (32fps =21.8mph).
During orbit the aircraft was toggling in and out of our dash mode (as designed) to maintain positive/forward ground speed. Average power throughout the flight was closing in on 700W, which is high but not abnormal based on high winds aloft.
GCS logs confirm general comments regarding operator statement on endurance remaining. See first statement of this section. 

Unsure if there would be any corrective actions for the system side of this (regarding improved endurance estimates). Defer to Dave and team for that. 
Link to comment with charts and additional description 
https://jenaero.atlassian.net/browse/VXEP-1987?focusedCommentId=101341 
---

## Comments (13)

### Michael Lindsay, 2026-09-01

@Cameron Chapmanthis is the Jira ticket for 1016 that had the battery warning with approx. 2 hrs of life remaining on the battery.  I have uploaded the AAR and have the battery in the office in Ottawa.  Where would you like me to sent the battery?

### Cody Smisek, 2026-09-01

@Michael Lindsay @Cameron Chapman What’s wrong with the battery? I see nearly 60fps of wind during this flight with apvlife trending accordingly and landing with ~30% SoC.

### Michael Lindsay, 2026-09-01

@Cody Smisek@Cameron Chapman  They got a low battery warning and the aircraft RTB with 2 hours of endurance displayed on the GCS (VXESUAV) it landed with approx 75 mins endurance as per the operator. I can see the warning in the debug file (12:14:45:559) and the event log (118:15:984) but I can’t see any indication of low energy in the XComm event log.  They had a similar issue on 930 I linked the Jira tickets.  No issue has been found with 930 so they are wondering it they is possibly and issue with the battery.

### Cameron Chapman, 2026-09-01

@Michael Lindsay I will checkout logs, but agree with Cody on first impression. 930 issue was a voltage dropout indicating a connection issue (unable to find on the aircraft, so we think it could be in the battery). This one doesn’t seem to have a dropout, and seems lore likely aircraft was flying outside of wind limits, used more energy than normal, and the endurance algorithm doesn’t well estimate power consumption in winds like that. Unless other issues exist with this battery, it is likely ok to fly as is. CA for this issue may be to remind them not to fly outside of limits (if data review proves that was the case)

### Cameron Chapman, 2026-09-01

@Michael Lindsay do you have any more info on flying conditions that could verify the readings mentioned (ground wind measurements, prior flight AARs from the same day, etc)?

### Cameron Chapman, 2026-09-01

@Scott Lovett is anyone available to do data review to confirm the flying over limits concern and recommend CAs?

### Cody Smisek, 2026-09-01

TLDR, unless we are provided additional information that obviously indicates some type of problem, the aircraft appears to be operating as currently designed. 
@Michael Lindsay Low energy RTB occurs based on the APs calculation of several variables. Described on slide 7 of this ticket and screenshot provided for easy reference. https://jenaero.atlassian.net/browse/FS2-4161 . 
[embedded: image-20260901-212646.png]
 The aircraft was being operated at or in exceedance of current published wind limitations for both ground and cruise. During cruise, AP indicated up to 60fps of wind (60fps = 40.9mph). On the ground the IAS was jumping from 20fps up to 32fps (32fps =21.8mph).
[embedded: image-20260901-212804.png]
During orbit the aircraft was toggling in and out of our dash mode (as designed) to maintain positive/forward ground speed. Average power throughout the flight was closing in on 700W. If  
[embedded: image-20260901-213050.png]
If we review our endurance section of the manual, which certainly is a finger wag estimate, we see that 14km (~8.5mi) we’d expect no more than 2hrs time on station in 40mph winds. I think that’d be generous.  
[embedded: image-20260901-213232.png]
Below are a few variables plotted against time. Sorry some units / axis titles are missing. 
[embedded: image-20260901-213751.png]

Below is from the ‘log’ file which is the Legacy GCS data. I think one could certainly argue that the estimated endurance remaining is pretty poor. But I don’t think this is something new / surprising to long time operators of this system. Dave’s team would need to weigh in on whether that aspect is ‘expected’ (I think it is) and whether they have time or resources to improve it. 
[embedded: image-20260901-220744.png]

### Michael Lindsay, 2026-09-01

@Cameron Chapman I will see if I can get anymore details regarding the wind conditions and any additional AARs form prior flights that day. As this was the last flight of the day. @Cody Smisek

### Cody Smisek, 2026-09-02

@Michael Lindsay @Cameron Chapman It was windy. There’s no need for additional details. Please review my previous comments and issue status. Tag Dave if we feel it’s worth bringing up the endurance estimate issue.

### Cameron Chapman, 2026-09-02

@Cody Smisek good point. C/CA updated.

### David Grosher, 2026-09-16

@Eric Brewer Can we re-evaluate this given the issue with the wind and ground speed rolling over that was observed at CANJAM?

### Eric Brewer, 2026-09-16

@David Grosher I took a quick look.  GPS was available for this entire flight, so the issue present in Churchill was not here.  The groundspeed was within bounds (though really fast due to the winds).
[embedded: image-20260916-203427.png]
Another quick update on the Churchill logs - the groundspeed displayed in the apGpsGs is direct from the NovAtel, and is not (intended to be) used by the RTB calculations.

There is a bug though where both DR and the receiver groundspeed and position are briefly written to the DR state, which causes a big jump in position - that was actually what caused the RTB in the Churchill case.  See ticket for details.

[FS2-5118] Low energy RTB in denied. - Jira

### Zachary Mann, 2026-10-07

Still looking into endurance limits – Ted Trowbridge looking into it further.

## Attachments (8)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T115_V1016_260825_110150_pack.zip | archive | 3834 | 2026-09-01 | listed only |
| image-20260901-212646.png | image | 32 | 2026-09-01 | listed only |
| image-20260901-212804.png | image | 17 | 2026-09-01 | listed only |
| image-20260901-213050.png | image | 3 | 2026-09-01 | listed only |
| image-20260901-213232.png | image | 96 | 2026-09-01 | listed only |
| image-20260901-213751.png | image | 406 | 2026-09-01 | listed only |
| image-20260901-220744.png | image | 26 | 2026-09-01 | listed only |
| image-20260916-203427.png | image | 15 | 2026-09-16 | listed only |
