# VXEP-272: VXE-425 Crash on VTOL landing-ESC Damage

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-02-09
- **Updated:** 2026-08-31
- **Resolved:** 2025-12-01
- **Reporter:** Pat Wells
- **Assignee:** Cameron Chapman
- **Creator:** Pat Wells
- **Labels:** Hardware, MARSOC, Weekly-incident-tracker
- **Links:** relates to ENG-3076 (Aircraft 425 Crash); relates to VXEP-12 (TPTR-87 VXE 511 VTOL Connector Issues 516 CW. Contains Main connector/contact C/CAs); relates to RMA-218 (VXE 425 240221); relates to VXEP-198 (VXE450 Implement CA: Procurement Evaluate/Order new datecode FDMS86540 MOSFETs (IPN: 100-110341)); relates to VXEP-628 (Systemic VXE30 VTOL ESC Reliability Issues ); relates to VA-444 (Evaluate replacing VXE30 ESCs)
- **Customer:** MARSOC
- **Vehicle Tail Number:** 425
- **Other Stakeholder (as required):** David Grosher
- **Problem Type:** Other (explain in description)
- **Plan:** - @Steve Gonzales to finalize report, CA tasks, and incident summary fields.
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical

## Description

Stalker VXE-30 was descending and began to drift from the desired land
location. VO went to command land immediately since user landing controls
did not populate. Before VO could select land immediately the AV pointed
downward and crashed nose first within 3 seconds.
EVENT SUMMARY: This was the first time Stalker 425 was flown in country.
Stalker 425 had 2 successful flights prior to this back in the US. During
pre-flights, VO noticed that VTOL motors did not reach its usual test speed.
VO then swapped out the HLB and re-tested. Second test was a success. AV was
then launched and climbed to 1500 ft AGL with no issues. Once established at
altitude for about 5 mins, AV began having degraded GPS issues, causing the
AV to lose and regain GPS every couple of mins. VO would re-command it back
to its orbit once GPS was regained and kept a close eye on it. After about
an hour and no sign of it resolving, VO commanded it to land. Once at 800 ft
AGL, AV had no more GPS issues showing 7-9 satellites locked. AV entered its
VTOL landing at its set 200 ft AGL then VO saw as it began to descend down
it began to turn and drift away from its desired location. User landing
controls did not auto populate so VO went into the menu to selected VTOL
control panel IOT select land immediately to give the VO controls to nudge
the AV back to its desired location. Before the VO selected land
immediately, the AV nose pitched down fast and hard crashing nose first into
the ground.   
AV was in the battery configuration 
Weather: Winds from 129 @ 9 kts sky was partly cloudy
Entire AV and wings are destroyed
AAR file provided by operator attached
See report located here.

## Corrective Action

- Ensure all service bulletins are applied to aircraft equipment. ​
- This ESC design traces back to when the aircraft and company were smaller. EA is working on replacing the ESCs with a larger, more powerful, more professional, and more qualified ESCs.
- https://jenaero.atlassian.net/browse/VA-444
- Linking all ESC issues here for trend analysis. https://jenaero.atlassian.net/browse/VXEP-628

## Issue Status

Significant left aft ESC damage observed. Due to the extent of damage, it is difficult to determine the cause of the incident. 
Data review complete.  Log analysis points to power/current for vtol system going to zero.
See report located here.
Images indicate the removing excess potting compound SB was not applied. 

[embedded image-20240828-161137.png]
- ESC PCBA completely destroyed, unable to definitively determine origin point of destruction.
- VTOL SD card corrupted, thus far unable to pull logs from it. Trying to get mac address of VTOL CPU which would allow us to access SD card with @Kurt Burian's help. Stand by for update on this effort.

## Root Cause

Causes:​
- Photos indicate that service bulletin was not applied to HLB (VXE-SB-23-002 HLB Mate Indicator Field Installation, Service Bulletin). This potting can interfere with the ability of the connector to fully mate, which can increase contact impedance, which increases voltage ripple at the ESCs, which increases current and stress on the soft start FETs.​
- Known issue about rust/corrosion on MOSFET leads used on lift ESCs, which increases impedance. Due to ESC damage, it is difficult to determine if this issue was present. https://jenaero.atlassian.net/browse/VXEP-198 ​
- Significant damage observed to left aft ESC. Lift motor appears to lose thrust causing the vehicle to crash. ue to the amount of damage, it is difficult to determine where the damage started. It looks like destruction may have started in soft start circuit FETs. These components have caused failures before. ​

Cause 3 Leading Hypothesis​
On the majority of ESCs, the parallel FETs split the current evenly enough to ensure none are damaged. ​
It is suspected that due to variation in component fabrication and installation, occasionally FETs can have higher impedance, which causes more current to flow through less FETs, which can overcurrent, overheat, and damage them. The FETs can then fail shorted, which causes a cascading failure as the FET conducts even more current.
https://jenaero.atlassian.net/browse/VXEP-628

## Comments (52)

### Mark Squillante, 2024-08-28

@Cameron Chapman EC5 contacts are good on that ESC. 
Throttle 1 is left aft, 2 is left forward, 3 is right forward, 4 is right aft according to Cody.

### Hayden Jeanor, 2024-08-28

Looks like they are working with batteries with the over application of TS23 problem on their batteries
[embedded image-20240828-164333.png]

### Cameron Chapman, 2024-08-28

@Cody Smisek @Mark Squillante from VXE-FCD-XCOMM Log Glossary.docx 
vtThr1                  Vt reported motor 1 (front left) throttle value, 0 – 1.
vtThr2                  Vt reported motor 2 (front right) throttle value, 0 – 1.
vtThr3                  Vt reported motor 3 (rear right) throttle value, 0 – 1.
vtThr4                  Vt reported motor 4 (rear left) throttle value, 0 – 1.
From  VXE-FCD-VTOL Log Glossary.docx
mxM1                   Motor 1 (front left) output throttle. Logged at different points in the SW vs FL CW to see how different code paths might contribute the final throttle. May be blank when actual throttle is present. Check both. FL is closer to final throttle.
mxM2                   Motor 2 (front right) output throttle
mxM3                   Motor 3 (rear right) output throttle
mxM4                   Motor 4 (rear left) output throttle
Please let me know if you have evidence to the contrary.

### Mark Squillante, 2024-08-28

ESC PCBA destroyed, came out of enclosure in 2 pieces. I updated the ppt file with this info. See pics
[embedded file]
[embedded file]
[embedded file]
[embedded file]
[embedded file]
[embedded file]
[embedded file]

### Mark Squillante, 2024-09-03

@Cameron Chapman if you are able to point me to any thermal testing data on the lift ESC FETs that would be great. Thank you

### Cameron Chapman, 2024-09-03

@Mark Squillante not very organized, but some tests in this and parent folders. Lift ESC You are welcome to rearrange, create an index of tests, etc if that helps organize things.

### Cameron Chapman, 2024-09-11

Saving findings from plan
- How do the EC3 contacts for that motor seem? 
- EC3 contacts look good

@Eric Brewer would a bad aft left ESC cause this issue? Perhaps if the aft left ESC was taking too much power, it would cause the voltage to drop significantly for the front left ESC, which could then lead to the data seen below.
@Cameron Chapman the data to me looks consistent with the whole lift system turning off.  The characteristic nose dive is consistent with other birds I’ve seen that issue on.

### Eric Brewer, 2024-09-12

@Cameron Chapman , good question I’m not sure.  The data to me is consistent with the whole lift system losing power, but it’s possible one bad ESC could cause the others to lose power as well.  The initial attitude excursion is mostly pitch down, so either loss of power on a front motor, or total loss of power (vehicle pitches down in this case).

### Cameron Chapman, 2024-09-12

@Eric Brewer it seems like high throttle 1 and 4 supports the idea of the left boom losing power due to an ESC 4 short, but the current does not.

### David Grosher, 2024-09-24

@Cameron Chapman This appears to be a hardware issue.

### Jason Scherer, 2024-09-25

@Eric Brewer I took a quick look at the logs and there is a landing abort that was triggered due to an attitude fault. Could be that the failed ESC caused the attitude fault. 
[embedded image-20240925-161128.png]

### Alexander Alan Arnold, 2024-12-10

@Jason Scherer Any progress on this? @Cameron Chapman

### Cameron Chapman, 2024-12-10

@Alexander Alan Arnold see requested next steps in the plan field.

### Eric Brewer, 2024-12-11

@Cameron Chapman initial report indicates there were 2 flights in the US and this was its first flight in country.  I reviewed some of the flight logs, the current does spike over 200A total, but in reviewing other reference flights this does not appear out of the ordinary. @Alexander Alan Arnold

### Eric Brewer, 2024-12-20

@Cameron Chapman @Alexander Alan Arnold are we good to move this one to implementing corrective actions?

### David Grosher, 2025-01-07

@Cameron Chapman ping on the question below.

### Cameron Chapman, 2025-01-07

@David Grosher @Eric Brewer  yes. I encourage you to update the plan and other fields as well as an investigation proceeds. Updating them can make statuses more clear vs just comments.

### Christa Meck, 2025-08-05

@Cameron Chapman and/or @Pat Wells we are we at on this investigation?  Looks like some service bulletins were not applied and that resulted in the crash.  We ok to close this from here or is there any additional work to be done.
Leaving open until 12 Aug for feedback then closing.

### Pat Wells, 2025-08-05

@Drew Hildreth @Jackson Riley Curvin @Alexander Alan Arnold See below from Christa
Please advise and close out if necessary.

### Alexander Alan Arnold, 2025-08-05

@Pat Wells the root cause is unclear, and CA is not implemented, I think it would be fine to close out if CA was implemented.

### Pat Wells, 2024-02-20

@Cameron Chapman the operator did not note any contact damage. I’m in the process of having the equipment returned.  Currently it’s at a deployed location so it will be a bit before we see it.

### Cameron Chapman, 2024-02-20

@Pat Wells thank you for the correction. I read your previous message too quickly. I will update the fields accordingly.

### Pat Wells, 2024-03-01

Added pictures of extra HLB’s on site but not involved in mishap.  Extra HLB 1,2,3,4.jpg
Excess potting compound visible in pictures. Airworthiness directive does not appear to be applied.

### Pat Wells, 2024-04-02

Operator unable to locate actual HLB that was installed in ACFT during the mishap.

### Sean Odell, 2024-08-26

@Cameron Chapman VXE-425 delivered to Engineering for evaluation. Photos added onto RMA ticket.  
@Pat Wells FYSA

### Mark Squillante, 2024-08-26

@Cameron Chapman AS150 contact measured 240 uohms (limit is 235) before cleaning. After cleaning measured 205 uohms. Data recorded in AS150 spreadsheet. Anti-spark measures 6.4 ohms.
I am also attaching pictures of the contact before and after cleaning.
[embedded file]
[embedded file]

### Mark Squillante, 2024-08-27

Minimum voltage for a lift ESC to run is 7V regardless of throttle signal. Added this info to Confluence page.
EC5 contacts look fine
VTOL board stack appears to be fine although it got dislodged from the vibe isolators (likely from impact)
CSB shows no signs of physical damage
Smell of burnt electronics coming from inside the wing case but hard to isolate source of smell. Suspect one or more of the ESCs.
Smell of burnt electronics coming from the nose area inside the fuselage case.
AS150 power connector a little dirty but not unreasonable and looks to me like possible heat damage on the anti-spark isolator ring, or physical damage from impact (not from mating cycles or excess potting material).
@Cameron Chapman should I begin checking into lift ESCs for damage?

### Mark Squillante, 2024-08-27

Left aft ESC/motor not spinning up. Took cover off of ESC and it is quite cooked. 11 ohms measured between input power and ground
[embedded file]

### Cameron Chapman, 2024-08-28

@Mark Squillante good findings. Surprising, as the data log seems to indicate that the forward ESCs were having the most issues (as evidenced by their high throttles of 1-2). It may be hard to determine if this damage caused the issue, or if it was a result from impact. 
- How do the EC3 contacts for that motor seem?
- Please work with EE team to see if you can determine possible causes of this damage.

 @Eric Brewer would a bad aft left ESC cause this issue? Perhaps if the aft left ESC was taking too much power, it would cause the voltage to drop significantly for the front left ESC, which could then lead to the data seen below.  


[embedded image-20240828-161137.png]

### Cameron Chapman, 2024-08-28

Archiving old plan:
@Eric Brewer these plots are strange. While it does look like there was a sudden power drop, it does not behave as expected. If Thr1 and 2 are high and the voltage is measuring 22V+, there still should be power and current flowing to the ESCs. It seems like the ESCs stopped receiving commands. Was there any power fault reported?

[embedded image-20240827-153642.png]

@Mark Squillante , while the resistance is over the limit, it does not explain that behavior. can you please test the minimum voltage a lift ESC will run and add that info to confluence? https://jenaero.atlassian.net/wiki/x/AoDiF  please also inspect the power contacts, inside the CW, and report any anomalies. 
- Minimum voltage for a lift ESC to run is 7V regardless of throttle signal. Added this info to Confluence page.
- EC5 contacts look fine
- VTOL board stack appears to be fine although it got dislodged from the vibe isolators (likely from impact)
- CSB shows no signs of physical damage
- Smell of burnt electronics coming from inside the wing case but hard to isolate source of smell. Suspect one or more of the ESCs.
- Smell of burnt electronics coming from the nose area inside the fuselage case.

Does the antispark portion look damaged from heat, or just mating cycles? 
- AS150 power connector a little dirty but not unreasonable and looks to me like possible heat damage on the anti-spark isolator ring, or physical damage from impact (not from mating cycles or excess potting material).

@Hayden Jeanor this might relate to your current battery investigation.

### Cameron Chapman, 2024-08-28

@Mark Squillante can you also please update the linked ppt with your findings and update the fields above as your investigation progresses?

### Hayden Jeanor, 2024-08-28

Anyone have the raw AAR zip of the incident? or we were only able to recover individual logs?

### Mark Squillante, 2024-08-28

@Cameron Chapman EC5 contacts are good on that ESC. 
Throttle 1 is left aft, 2 is left forward, 3 is right forward, 4 is right aft according to Cody.

### Hayden Jeanor, 2024-08-28

Looks like they are working with batteries with the over application of TS23 problem on their batteries
[embedded image-20240828-164333.png]

### Cameron Chapman, 2024-08-28

@Cody Smisek @Mark Squillante from VXE-FCD-XCOMM Log Glossary.docx 
vtThr1                  Vt reported motor 1 (front left) throttle value, 0 – 1.
vtThr2                  Vt reported motor 2 (front right) throttle value, 0 – 1.
vtThr3                  Vt reported motor 3 (rear right) throttle value, 0 – 1.
vtThr4                  Vt reported motor 4 (rear left) throttle value, 0 – 1.
From  VXE-FCD-VTOL Log Glossary.docx
mxM1                   Motor 1 (front left) output throttle. Logged at different points in the SW vs FL CW to see how different code paths might contribute the final throttle. May be blank when actual throttle is present. Check both. FL is closer to final throttle.
mxM2                   Motor 2 (front right) output throttle
mxM3                   Motor 3 (rear right) output throttle
mxM4                   Motor 4 (rear left) output throttle
Please let me know if you have evidence to the contrary.

### Mark Squillante, 2024-08-28

ESC PCBA destroyed, came out of enclosure in 2 pieces. I updated the ppt file with this info. See pics
[embedded file]
[embedded file]
[embedded file]
[embedded file]
[embedded file]
[embedded file]
[embedded file]

### Mark Squillante, 2024-09-03

@Cameron Chapman if you are able to point me to any thermal testing data on the lift ESC FETs that would be great. Thank you

### Cameron Chapman, 2024-09-03

@Mark Squillante not very organized, but some tests in this and parent folders. Lift ESC You are welcome to rearrange, create an index of tests, etc if that helps organize things.

### Cameron Chapman, 2024-09-11

Saving findings from plan
- How do the EC3 contacts for that motor seem? 
- EC3 contacts look good

@Eric Brewer would a bad aft left ESC cause this issue? Perhaps if the aft left ESC was taking too much power, it would cause the voltage to drop significantly for the front left ESC, which could then lead to the data seen below.
@Cameron Chapman the data to me looks consistent with the whole lift system turning off.  The characteristic nose dive is consistent with other birds I’ve seen that issue on.

### Eric Brewer, 2024-09-12

@Cameron Chapman , good question I’m not sure.  The data to me is consistent with the whole lift system losing power, but it’s possible one bad ESC could cause the others to lose power as well.  The initial attitude excursion is mostly pitch down, so either loss of power on a front motor, or total loss of power (vehicle pitches down in this case).

### Cameron Chapman, 2024-09-12

@Eric Brewer it seems like high throttle 1 and 4 supports the idea of the left boom losing power due to an ESC 4 short, but the current does not.

### David Grosher, 2024-09-24

@Cameron Chapman This appears to be a hardware issue.

### Jason Scherer, 2024-09-25

@Eric Brewer I took a quick look at the logs and there is a landing abort that was triggered due to an attitude fault. Could be that the failed ESC caused the attitude fault. 
[embedded image-20240925-161128.png]

### Alexander Alan Arnold, 2024-12-10

@Jason Scherer Any progress on this? @Cameron Chapman

### Cameron Chapman, 2024-12-10

@Alexander Alan Arnold see requested next steps in the plan field.

### Eric Brewer, 2024-12-11

@Cameron Chapman initial report indicates there were 2 flights in the US and this was its first flight in country.  I reviewed some of the flight logs, the current does spike over 200A total, but in reviewing other reference flights this does not appear out of the ordinary. @Alexander Alan Arnold

### Eric Brewer, 2024-12-20

@Cameron Chapman @Alexander Alan Arnold are we good to move this one to implementing corrective actions?

### David Grosher, 2025-01-07

@Cameron Chapman ping on the question below.

### Cameron Chapman, 2025-01-07

@David Grosher @Eric Brewer  yes. I encourage you to update the plan and other fields as well as an investigation proceeds. Updating them can make statuses more clear vs just comments.

### Christa Meck, 2025-08-05

@Cameron Chapman and/or @Pat Wells we are we at on this investigation?  Looks like some service bulletins were not applied and that resulted in the crash.  We ok to close this from here or is there any additional work to be done.
Leaving open until 12 Aug for feedback then closing.

### Pat Wells, 2025-08-05

@Drew Hildreth @Jackson Riley Curvin @Alexander Alan Arnold See below from Christa
Please advise and close out if necessary.

### Alexander Alan Arnold, 2025-08-05

@Pat Wells the root cause is unclear, and CA is not implemented, I think it would be fine to close out if CA was implemented.

## Attachments (28)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| VXE 425 LOGS.zip | archive | 196 | 2024-02-09 | listed only |
| VTOL_VXE425.zip | archive | 142 | 2024-02-14 | listed only |
| XCOMM_VXE425.zip | archive | 10798 | 2024-02-14 | listed only |
| 1.jpg | image | 1896 | 2024-02-20 | listed only |
| 2.jpg | image | 1571 | 2024-02-20 | listed only |
| 3.jpg | image | 1413 | 2024-02-20 | listed only |
| 4.jpg | image | 1103 | 2024-02-20 | listed only |
| 5.jpg | image | 1244 | 2024-02-20 | listed only |
| 6.jpg | image | 711 | 2024-02-20 | listed only |
| 7.jpg | image | 627 | 2024-02-20 | listed only |
| 8.jpg | image | 641 | 2024-02-20 | listed only |
| Extra HLB 1.jpg | image | 731 | 2024-03-01 | listed only |
| Extra HLB 2.jpg | image | 803 | 2024-03-01 | listed only |
| Extra HLB 3.jpg | image | 674 | 2024-03-01 | listed only |
| Extra HLB 4.jpg | image | 617 | 2024-03-01 | listed only |
| AS150 after cleaning.jpg | image | 653 | 2024-08-26 | listed only |
| AS150 before cleaning.jpg | image | 650 | 2024-08-26 | listed only |
| IMG_20240827_142948164_HDR.jpg | image | 3619 | 2024-08-27 | listed only |
| IMG_20240827_142948164_HDR (4a543c46-e06f-4933-922f-207b6720a2aa).jpg | image | 3619 | 2024-08-28 | listed only |
| IMG_20240828_132734029_HDR.jpg | image | 4175 | 2024-08-28 | listed only |
| IMG_20240828_132804235_HDR.jpg | image | 3985 | 2024-08-28 | listed only |
| IMG_20240828_132825252_HDR.jpg | image | 614 | 2024-08-28 | listed only |
| IMG_20240828_132843974_HDR.jpg | image | 669 | 2024-08-28 | listed only |
| IMG_20240828_132917601_HDR.jpg | image | 535 | 2024-08-28 | listed only |
| IMG_20240828_132925040_HDR.jpg | image | 617 | 2024-08-28 | listed only |
| image-20240828-161137.png | image | 232 | 2024-08-28 | listed only |
| image-20240828-164333.png | image | 419 | 2024-08-28 | listed only |
| image-20240925-161128.png | image | 539 | 2024-09-25 | listed only |
