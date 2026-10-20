# VA-93: Record typical, max, and max tested lift current and voltage profiles. Save test data to confluence. Establish and implement limits and abort if exceeding.

- **Issue type:** Epic
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** High
- **Created:** 2023-05-09
- **Updated:** 2025-05-21
- **Resolved:** 2025-05-21
- **Reporter:** Cameron Chapman
- **Assignee:** Connor Peebles
- **Creator:** Cameron Chapman
- **Labels:** 8-28-Sprint
- **Links:** relates to ENG-3084 (VXE 401 Failed VTOL Landing from 10ft (Crash)); relates to ENG-3061 (VXE 454 Center Wing Power Connector solder melted); relates to VXEP-479 (Test max power and duration limits of lift system.  ); relates to ENG-2987 (VXE371 Centerwing Boom Power Connecter Melted / signs of overheat or arcing); relates to ENG-3160 (Determine overcurrent abort limit, then implement auto-abort when present. Update manuals accordingly. ); relates to VA-236 (Compile a data set of SCO flights for lift currents during takeoffs/landings); relates to VA-106 (Document additional recommended corrective actions. Ex: takeoff abort if overlimit. If flying over MTOW, ensure slower climb rate and lower transition.); relates to VA-105 (Identify weakest points/additional tests we should perform); relates to VA-104 (Review flight profiles at max limits and conditions. Do we have any examples of flying at MTOW in worst conditions (max density altitude)); relates to VA-103 (Summarize qualification tests); relates to VA-102 (Record published limits and any guidance to exceed limits. Lower transition, slower climb rate, etc.); relates to VA-101 (Where and how are Ibatt1 and Ibatt2 measurements taken?); relates to VA-100 (Create summary document of findings so far. Recommend posting a link to a word doc saved here Investigations ); relates to VA-99 (Review VXE376 for overweight and above nominal current draw during AEWE); relates to VA-98 (Review VXE371 for overweight and above nominal current draw during AEWE); relates to VA-97 (SCO Should be performed at MGTOW, so that we verify each aircraft can operate in that configuration); relates to VA-377 (Document current profiles for Triclops configurations. ); causes VXEP-12 (TPTR-87 VXE 511 VTOL Connector Issues 516 CW. Contains Main connector/contact C/CAs); relates to VXEP-315 (VXE 459 Overshoot of LZ Mishap on landing, operator unable to nudge); relates to VXEP-274 (VXE 438 Lift motor failure resulting in crash); relates to FS2-2522 (B30+40: Implement 12V load shedding when vbatt gets too low or overcurrent detected. ); relates to VXEP-811 (VXE-470 Crash on VTOL descent-flying overweight-HW not inspected?)

## Description

Engineering Team - VTOL Max Current Draw Investigation - All Documents (sharepoint.com)
Working report Summary of Findings - Lift Current Profile Limits.docx
@Greg Fryer , can you please review this criteria and approve if and when we should implement in firmware and GCS SW?
@David Grosher @John Clark @Ryan Christino do you anticipate any issues with this criteria.
FYI @Pat Wells
Plan: 
https://jenaero.atlassian.net/browse/VA-2280 

@Ryan Christino defined the following worst case profile : Profile Summary: 200A for 40 seconds, then 150A for an additional 80 seconds. Total profile duration 120 seconds (<17% SOC). This simulates climb, immediate abort, and the maximum pause duration (pause aborts at 25% SOC). https://jenaero.atlassian.net/wiki/spaces/EE/pages/11272193/Power+and+Temperature+Profiles
In our contact testing, we determined that at the max acceptable contact impedance of 233uohms (measured across anti-spark pair), we have approximately 20% current margin before the contact gets near melting temperature.
[embedded: image-20231019-173319.png]
We also tested that 10% more duration on the climb phase did not lead to a large temperature different. Current magnitude is the most important factor.
[embedded: image-20231019-174121.png]
Damaged contact due to too high impedance see 511+516-investigation report.pptx
[embedded: image-20231019-175149.png]
 
Thermal Stress Test.xlsx
Therefore, I am proposing the following abort criteria:
- Average current for 10 seconds >220A (10% longer than worst case).
- Message to operator: “Abort: Lift current is too high. Please inspect lift power connector contacts, ensure compliance with VXE-ES-23-002 Increased VXE30 Payload Weight (Modified Gains), Engineering Supplement. Do not fly aircraft and contact customer service if not compliant.”
- Average current >200A for >44 seconds (10% longer than worst case):
- Message to operator: “Abort: Lift current and duration is too high. Please inspect lift power connector contacts, ensure compliance with VXE-ES-23-002 Increased VXE30 Payload Weight (Modified Gains), Engineering Supplement. Do not fly aircraft and contact customer service if not compliant.”
- HLB Voltage <21V for >1 seconds.
- Message to operator: “Abort: Low lift battery voltage detected.” I think there is already an abort limit in firmware. @John Clark can you confirm if there is, and the details if so.
- Create subtask for determining voltage limit to flag during launch wizard.




Goal of investigation: Create excel plots of a standard flight, the maximum limit of what we determine is safe, and an example of a flight that exceeded this limit and caused damage. This can be used to set auto abort limits, and to troubleshoot future flights. 
Outline will create subtasks
- Record published limits, published guidance to exceed limits, and where those are located.
- Increased VXE30 Payload Weight (Modified Gains Configuration)
- MGTOW of up to 52 lbs. with a density altitude limitation of 7.500 ft. 
- the transition altitude must be reduced to 200ft
- VXE-TM-23-001 VXE30 Payload Capacity, Tech Memo
- One method is to fly with an XE25 battery in place of the normal VXE30 battery per VXE-ES-23-001 Increased VXE30 Payload Weight (XE25 Battery), Engineering Supplement. This method renders the GCS endurance estimates inaccurate and reduces flight time. 
This is only recommended for localized missions.
- The second method is to modify configuration values in the software such as airspeed setpoints, climb rate, and transition altitude per VXE-ES-23-002 Increased VXE30 Payload Weight (Modified Gains), Engineering Supplement. This allows for the system to be flown at a higher MGTOW; flying at a higher MGTOW will slightly reduce system endurance. This method also requires the VXE30 to transition from a lower altitude. Here is a flowchart that summarizes this: 
[embedded: image-20230917-224816.png]
- @Ryan Christino, do you have power profiles for the conditions estimated in VXE-TM-23-001?
- Test connector and wire temperatures at those power profiles to see how much margin is left.
- Document additional recommended corrective actions.
- Recommend abort limits for too high of current during takeoff.
- Determine where measurements are/how actually taken for data provided in AAR.


Motivation for this project: Customer likely reflowed solder on a CW power connector during takeoff and crashed. They were flying at 200A lift current, when most of our qualification testing was 150A max (AS150 pins are also questionably rated to 150A). https://jenaero.atlassian.net/browse/VIT2-284 
Customer states they were flying ~50.6lb, transitioning at 200ft, but not changing climb rate. They also report they were told by EA and LM personnel it was ok to fly overweight. 
MTOW battery config is 48.0lb / 21.8kg
MTOW fuel cell config is 44.0lb / 20.0kg

## Sprint

VXE-1 Electrical-8, VXE-2 Everything Else 2024-03, VXE-1 Electrical 10/29, VXE-1 Electrical 11-20-12/10, VXE Product Dev & Sup 2024-07, VXE Product Dev & Sup 2024-05, VXE-1 Electrical-7, VXE Prod Dev & Sup 2024-08

## Comments (23)

### Cameron Chapman, 2023-05-10

FYI @Greg Fryer @Scott Stuckey @Ryan Christino @Former user @John Clark @Former user @Sam Miller @Laszlo Juhasz @Cody Smisek

### Cody Smisek, 2023-05-11

Attached word document for high altitude flights conducted by @Ryan Christino in August 2022. Selected 8 flights of the 19 for plotting (those more within our current published limitations). All exceeded 150A, some approached 200A.

### Cameron Chapman, 2023-05-12

Stephen from Ann Arbor has also done some data analysis to define battery requirements. He can help with this project. Sent Jira invite. @Tom Westrich

### Cody Smisek, 2023-05-17

just went through ~50 flights of AARs from SCOs over the past month, I approximate that the average takeoff current was 150A (or slightly more) for 45lb takeoffs.

### Cameron Chapman, 2023-05-22

Questions from conversation with Cody.
- Create summary document of findings so far. Recommend posting a link to a word doc saved here https://jenaero.sharepoint.com/:f:/r/sites/EngineeringTeam/Shared%20Documents/Electrical/Investigations?csf=1&web=1&e=y75Xr5
- Do we have any examples of flying at MTOW in worst conditions (max density altitude)?

### Cody Smisek, 2023-07-20

@Cameron Chapman sounds like this is a priority item, but I have no availability of time. Reassign as needed, I’m not aware of what resources are available in SLO. 
We do have examples of MTOW and above MTOW at high DA. I’ll link Ryan’s report.

### Cameron Chapman, 2023-07-23

@Connor Peebles 
Are you available to review, summarize, and provide a recommendation for the following linked tasks (possibly duplicates, but we want to gather info from each). Essentially, we would like to establish a lift profile limit, where the aircraft is ok to fly under, but automatically aborts past that profile to prevent connector and aircraft damage.
 
Laszlo, Cody, and Stephen Peters have already done some analysis in the linked tickets, but we need to collect the info and provide recommended limits. This will be important in determining max profiles for X-kit and VXE, and also if we need any harnesses changes for X-kit. 
 
You are welcome to have interns or other EEs help with this effort.
 
https://jenaero.atlassian.net/browse/ENG-1753  
https://jenaero.atlassian.net/browse/VIT2-328

### Cody Smisek, 2023-07-24

@Connor Peebles @Cameron Chapman FYI, on Friday I started compiling a data set of SCO flights for lift currents during takeoffs/landings. This was taken from 48 flights from April/May timeframe. I will upload this when it’s complete.

### Connor Peebles, 2023-07-26

@Madeleine Masiello I will ask for your assistance on this Jira

### Connor Peebles, 2023-08-16

@Cody Smisek Was the data set of SCO flights for lift currents from your previous comment uploaded?
@Madeleine Masiello

### Cody Smisek, 2023-08-21

@Connor Peebles No, I rapidly went through each via excel and approximated at the time. If this needs to be done we can do it (would be a good intern task).

### Cameron Chapman, 2023-08-24

Linking subtasks to parent

### Madeleine Masiello, 2023-09-06

On hold - Waiting for Liam to return to office to request help with software issues

### Cameron Chapman, 2023-09-12

Liam is back. @Connor Peebles would this be a good one for you to resume or handoff to someone like @Wesley Lilienthal ?

### Connor Peebles, 2023-09-12

@Cameron Chapman Either way is fine. Based on my workload it may take longer for me to do it, and Wesley could get familiar with data review

### Wesley Lilienthal, 2023-09-22

@Cameron Chapman Per discussion with @Connor Peebles, forgoing in favor of tasks included in the current sprint. Please advise if I should pick this up.

### Cameron Chapman, 2023-09-22

This is related to reliability issues in the current sprint, but it harder to define and reach completion. Ok to do those other tasks first.

### Cameron Chapman, 2023-09-22

@Wesley Lilienthalsounds good. Please transitions tasks to on hold when not working them. (Many other issues do not have accurate status, but that is the goal). I transitioned this one.

### Cameron Chapman, 2023-10-19

@Ryan Christino defined the following worst case profile : Profile Summary: 200A for 40 seconds, then 150A for an additional 80 seconds. Total profile duration 120 seconds (<17% SOC). This simulates climb, immediate abort, and the maximum pause duration (pause aborts at 25% SOC). https://jenaero.atlassian.net/wiki/spaces/EE/pages/11272193/Power+and+Temperature+Profiles 
In our contact testing, we determined that at the max acceptable contact impedance of 233uohms (measured across anti-spark pair), we have approximately 20% current margin before the contact gets near melting temperature. 
[embedded: image-20231019-173319.png]
We also tested that 10% more duration on the climb phase did not lead to a large temperature different. Current magnitude is the most important factor. 
[embedded: image-20231019-174121.png]
Damaged contact due to too high impedance see 511+516-investigation report.pptx
[embedded: image-20231019-175149.png]

Thermal Stress Test.xlsx
Therefore, I am proposing the following abort criteria: 
- Average current for 10 seconds >220A (10% longer than worst case). 
- Message to operator: “Abort: Lift current is too high. Please inspect lift power connector contacts, ensure compliance with VXE-ES-23-002 Increased VXE30 Payload Weight (Modified Gains), Engineering Supplement. Do not fly aircraft and contact customer service if not compliant.”
- Average current >200A for >44 seconds (10% longer than worst case): 
- Message to operator: “Abort: Lift current and duration is too high. Please inspect lift power connector contacts, ensure compliance with VXE-ES-23-002 Increased VXE30 Payload Weight (Modified Gains), Engineering Supplement. Do not fly aircraft and contact customer service if not compliant.”
- HLB Voltage <21V  for >1 seconds. 
- Message to operator: “Abort: Low lift battery voltage detected.” I think there is already an abort limit in firmware. @John Clark can you confirm if there is, and the details if so.
- Create subtask for determining voltage limit to flag during launch wizard.

@Greg Fryer , can you please review this criteria and approve if and when we should implement in firmware and GCS SW? 
@David Grosher @John Clark @Ryan Christino do you anticipate any issues with this criteria. 
FYI @Pat Wells

### Greg Fryer, 2023-10-19

@Cameron Chapman @David Grosher I approve the test criteria, and endorse the proposed limit checks. Endorse means “As part of a project to implement, we should check as much flight data as possible to validate it won’t abort excessive flights” I expect that to pass, but we owe the due diligence.
I also request further contact investigation to see about the fouling of the contact from (probably from the resistor?). Determine if there is a process we can do to mitigate.
Thanks to everyone for pushing this forward.

### David Grosher, 2023-10-19

@Cameron Chapman Have we looked at any flight data where there were heavy winds but within tolerance? I would expect that to result in a higher power draw.

### Cameron Chapman, 2023-10-20

@David Grosher yes. @Ryan Christino developed the profile below as the worst case profile. Heavy, windy, high altitude,etc. the limits are above that worst case profile.

### Cameron Chapman, 2024-04-01

@David Grosher since testing and replacing all contacts in the field is not feasible, I think this will be our best method to detect resistance issues and hopefully save some aircraft. Do you have anyone available to crunch some flight data to pick abort limits that do not cause unnecessary aborts, but trigger before failures? If not, it could be a good intern project for summer. 
We could first look at logs from failed aircraft with this issue.

## Attachments (8)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| HighAltPlots.docx | docx | 331 | 2023-05-11 | no text found |
| [High Elevation Test Report.docx](attachments/15529_High%20Elevation%20Test%20Report.docx.md) | docx | 2238 | 2023-07-20 | converted |
| MGTOW Discussion (Post High Elevation Round 1).pptm | other | 657 | 2023-07-20 | listed only |
| [Super Triclops AEWE Flights.docx](attachments/15554_Super%20Triclops%20AEWE%20Flights.docx.md) | docx | 179 | 2023-07-21 | converted |
| image-20230917-224816.png | image | 113 | 2023-09-17 | listed only |
| image-20231019-173319.png | image | 42 | 2023-10-19 | listed only |
| image-20231019-174121.png | image | 25 | 2023-10-19 | listed only |
| image-20231019-175149.png | image | 24 | 2023-10-19 | listed only |
