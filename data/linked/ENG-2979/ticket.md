# ENG-2979: VXE493 Rearward Drift on Landing

- **Issue type:** Problem
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2023-06-28
- **Updated:** 2025-06-02
- **Resolved:** 2025-05-21
- **Reporter:** Daniel Lloyd
- **Assignee:** Eric Brewer
- **Creator:** Daniel Lloyd
- **Labels:** TIQUILA
- **Links:** relates to VXEP-17 (TPTR-56 AV reported as not being able to hold position during landing in high winds); relates to FS2-849 (VXEP-17 TPTR-56 AV reported as not being able to hold position during landing in high winds); relates to FS2-1149 (VIT2-323 Wind analysis)

## Description

Aircraft 493 was reported as not being able to hold position during landing in high winds resulting in a rearward drift and landing downwind of the planned landing zone.

## Comments (28)

### Craig Burton, 2023-07-14

The flight data log shows the landing ground wind speed as 9 MPH.  Was this recorded pre- or post-flight?

### Daniel Lloyd, 2023-07-14

I was there for that flight but was not the operator. I assume that was post flight based on how the GCS software functions. It seemed to be much more windy than that.

### Craig Burton, 2023-07-14

Thank you, Daniel.  Could there have been a thermal blowing through the LZ at the time of landing?
Another question:  the notes file in the data pack states “Estimated range, bearing from vehicle to LZ:  35 feet 182 degrees”, but the flight data log shows the Landing Error Distance as 168 and Landing Error Direction of 47.  I’m trying to reconcile these differences.  Can you estimate how far away from the LZ the vehicle actually touched down?

### Daniel Lloyd, 2023-07-14

I don’t recall a thermal. It was a particularly winding day with ground winds near 20 MPH which is not unusual at that location.  I also noted the differences in the landing numbers.
“35 feet 182 degrees”, this seems consistent with the aircraft’s location after being moved back to the GCS after landing. It landed much further away than 35 feet. The bearing of 182 does not line up with the runway but is consistent with the GCS location which was south of the runway. Maybe the software captures this data at the time the AAR is created.
“168 feet 47 degrees”, this is consistent with the runway (04/22). 168 feet seems a bit far but much more accurate than 35 feet. I suspect it is correct.

### Craig Burton, 2023-07-18

Hi @Daniel Lloyd,  I’m not seeing any XCOMM or VTOL logs in this data pack.  Would you happen to have those files?

### Daniel Lloyd, 2023-07-19

This happened at Helendale during the MOD Tiquila training.
@Pat Wells

### Daniel Lloyd, 2023-07-19

It doesn’t look like the operator downloaded the FDR. Those files are not currently available. I may be able to get something in a week or two.

### Pat Wells, 2023-08-03

@Daniel Lloyd any update on obtaining the files?

### Daniel Lloyd, 2023-08-14

As I mentioned before the FDR was not downloaded after the flight. I attached an AAR from the next day and one from last week in my shop. I don’t think they will help.
@Pat Wells

### Cameron Chapman, 2023-08-24

Linking subtasks to parent.

### John Clark, 2023-08-28

@David Grosher preliminary report attached. VXE493 Investigation.pptx

### David Grosher, 2023-11-08

@John Clark The data from 08/03 is not in the timeframe when this issue was first reported.  Please include the data from June flights in the report.

### Former user, 2023-12-07

We attempted HIL test. We did not see drift from the HIL test data.
Ryan Christino will attach HIL data and a quick summary on the ticket.

### David Grosher, 2023-12-08

@Former user The investigation requires analyzing data from the two flights in June.  The analysis should be added to the power point investigation.  HIL tests alone are not adequate.

### Sam Miller, 2024-01-18

@David Grosher , can you please re-assign the review of flight data to another person to close this one out?

### Daniel Lloyd, 2024-01-18

@Eric Brewer Lockheed won’t let me use TEAMS outside of Lockheed

### Eric Brewer, 2024-01-22

No problem @Daniel Lloyd.  I was trying to piece together from the logs what the issue is.  Is there a description of what the operators saw in each of the flights that was flagged as an issue?  If easier to do a quick call let me know.

### Daniel Lloyd, 2024-01-22

@Eric Brewer How about a call at 6615722487

### Daniel Lloyd, 2024-01-22

https://maps.app.goo.gl/XNjc16TLs8Hb8hVS8

### Daniel Lloyd, 2024-01-22

https://maps.app.goo.gl/t8kXrZbw7dbsk5PFA

### Eric Brewer, 2024-01-23

Notes from discussion with Daniel (Daniel if I misrepresented anything feel free to update):
Issue occurred on June 26, the log set above that does not have full logs.  Second set of logs was downloaded on June 27th, believed to be from a flight the next day but was downloaded in hopes it would contain any information about the issue the day prior.  June 27th flight did not display any issues.  Log data is format “T95_V493_yymmdd_hhmmss”.  Daniel is not familiar with the August 3 log set.
For the event in question, wind was about 20mph.  Aircraft was coming in on vertical descent, was getting block backward downwind from the landing zone.  The operators in this case allowed the aircraft to land on its own, it landed ~168' short of the runway.  Note that the ‘…notes.txt’ file indicates the aircraft was 35' from the landing zone.  Daniel believes this is in error and was actually the landing error after the operators carried it back toward the landing zone.
In the past they have tried to use ‘nudge’ control mode to bring it back toward the landing zone.  As they try to push it forward, the angle of attack reduces and that reduces lift on the wing and the aircraft drops.  They stopped trying to nudge it forward because it was dropping toward the ground.  On landing they no longer use the forward prop as they do on climbout.  When Daniel asked Dustin Gamble (sp?) about it, it sounded like when they had the main prop on it increased lift on the main wing (blowing a lot of air across the wing), and creating lift was counterproductive when trying to descend.  If you use the forward motor the rotors throttle way down.
Daniel has not seen this issue before or after this one flight event, and he is at a lot of VXE flights (all training events etc).  Daniel does not believe they have flown in winds similar to what they saw on this day.
https://maps.app.goo.gl/XNjc16TLs8Hb8hVS8 is approximate GCS location.
https://maps.app.goo.gl/t8kXrZbw7dbsk5PFA is approximate target tdp location.

### Daniel Lloyd, 2024-01-23

@Eric Brewer some edits
Notes from discussion with Daniel (Daniel if I misrepresented anything feel free to update):
Issue occurred on June 26, the log set above that does not have full logs. Second set of logs was downloaded on June 27th, believed to be from a flight the next day but was downloaded in hopes it would contain any information about the issue the day prior. June 27th flight did not display any issues. Log data is format “T95_V493_yymmdd_hhmmss”. Daniel is not familiar with the August 3 log set. The 3 August AAR was one that Daniel collected from the aircraft while in his shop.
For the event in question, wind was about 20mph. Aircraft was coming in on vertical descent, was getting block backward downwind from the landing zone. The operators in this case allowed the aircraft to land on its own, it landed ~168' short of the runway. Note that the ‘…notes.txt’ file indicates the aircraft was 35' from the landing zone. Daniel believes this is in error and was actually the landing error after the operators carried it back toward the landing zone. GCS
In the past they have tried to use During that landing they used ‘nudge’ control mode to bring it back toward the landing zone. As they try to push it forward, the angle of attack reduces and that reduces lift on the wing and the aircraft drops. They stopped trying to nudge it forward because it was dropping toward the ground. On landing they no longer the autopilot does not use the forward prop as they do it does on climbout. When Daniel asked Dustin Gamble (sp?) about it, it sounded like when they had the during early flight test development if the main prop was on it increased lift on the main wing (blowing a lot of air across the wing), and creating lift was counterproductive when trying to descend. If you use the forward motor the rotors throttle way down.
Daniel has not seen this issue before or after this one flight event, and he is at a lot of VXE flights (all training events etc). Daniel does not believe they have flown in winds similar to what they saw on this day.

### Eric Brewer, 2024-01-25

@Daniel Lloyd , do you happen to recall if there were any lateral position and/or roll excursions encountered also or was it mostly stable laterally and just drifted backward?  We are attempting to recreate the issue in our simulator.

### Daniel Lloyd, 2024-01-25

@Eric Brewer I was not part of the crew flying that aircraft but I do recall looking over at it briefly and it appeared to be a normal stable VXE landing.

### Daniel Lloyd, 2024-01-25

@Eric Brewer Let me see if I can get you in contact with the pilot.

### Daniel Lloyd, 2024-01-25

Can you give me your Edge email address? @Eric Brewer

### Eric Brewer, 2024-01-25

Thanks, that would be much appreciated.  My email is ebrewer@edgeautonomy.io

### Eric Brewer, 2024-01-30

High rate VTOL logs were not available for this flight.  I was able to review the 1hz logs.  It appears that the wind was at or above the 20mph limit for much of the approach which probably contributed to the rearward drift.  Interestingly, the logs only appeared to show ~40' of drift vs. the 168' mentioned.  I’m not sure what drives the discrepancy, perhaps the target touchdown point was moved?
[embedded: image-20240130-213136.png]
We were unable to reproduce this issue in our HILSim as it does not accurately  model VTOL flight conditions above 20mph.

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V493_230626_121353_01_pack.zip | archive | 473 | 2023-06-28 | listed only |
| T95_V493_230627_094757_01_pack.zip | archive | 2531 | 2023-08-14 | listed only |
| T95_V493_230803_124237_pack.zip | archive | 2824 | 2023-08-14 | listed only |
| [RE Stalker VXE Landing .msg](attachments/18537_RE%20Stalker%20VXE%20Landing%20.msg.md) | msg | 662 | 2024-01-30 | converted |
| image-20240130-213136.png | image | 846 | 2024-01-30 | listed only |
