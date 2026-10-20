# VXEP-811: VXE-470 Crash on VTOL descent-flying overweight-HW not inspected?

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2024-12-03
- **Updated:** 2026-08-31
- **Resolved:** 2026-01-20
- **Reporter:** Pat Wells
- **Assignee:** Michael Mohr
- **Creator:** Pat Wells
- **Labels:** MARSOC, Training, Weekly-incident-tracker
- **Links:** relates to VA-93 (Record typical, max, and max tested lift current and voltage profiles. Save test data to confluence. Establish and implement limits and abort if exceeding.); relates to VXEP-628 (Systemic VXE30 VTOL ESC Reliability Issues )
- **Customer:** MARSOC
- **Vehicle Tail Number:** 470
- **Plan:** Investigation complete. See C/CA
- **Incident Type:** Aircraft Damage
- **Severity:** 4 - Annoyance

## Description

Witness statement received from operator:

STALKER 470 WAS SENT TO PLZ BY OPERATOR DUE TO LOW BATTERY. WHILE TRASITIONING FROM FIXED FLIGHT TO VERTICAL FLIGHT, GROUND CREW (SSGT JOSEPH CAROZZA) WAS GIVING COMMANDS TO MYSELF (SSGT FRANK KRUPICZOWICZ). GROUND CREW INDICATED THAT THE STALKER NEEDED TO GO RIGHT. THE COMMAND WAS GIVEN, BUT NOT EXECUTED BY STALKER 470. ADDITIONALLY, STALKER 470 SEEMED TO NOT PAUSED FOR LIDAR SENSING AT 13 OR 3 FEET, BUT RATHER CAME STRAIGHT DOWN, BOUNCED OFF THE DECK, AND INTO AN OBJECT. GROUND CREW RADIOED FOR IMMEDIATE MOTOR KILL, WHICH WAS GIVEN.                               
AIRCRAFT WAS RECOVERED IN ITS ENTIRETY AS THE INCIDENT HAPPENED AT THE PLZ.                                                                                                                                                                                                                    UPON VISUAL INSPECTION, BOTH VERTICAL BOOMS WERE DAMAGED, WITH THE LEFT VERTICAL BOOM HAVING THE REAR PROPELLER AREA SEVERELY DAMAGED AND THE RIGHT VERTICAL BOOM HAVING A SIZEABLE CRACK ON IT. STALKER 470 WAS RECONNECTED TO AT THE STATION TABLE AND IT WAS DETERMINED THE HD 55 AND SNAKE EAGLE WERE NOT RECEIVING POWER. AN ADDITIONAL STALKER BODY (STALKER 427) WAS ON HAND TO TEST THE OPERABILITY OF THE HD 55 AND SNAKE EAGLE. BOTH PAYLOADS WORKED ON FUSELAGE 427. POTENTIAL LOSS OF POWER MAY HAVE CAUSED THE CRASH. 


AAR attached

## Corrective Action

Remind operators of VXE30 MGTOW limits and the risks of exceeding them. 
https://jenaero.atlassian.net/browse/VA-93 
https://jenaero.atlassian.net/browse/VA-221

## Issue Status

Initial log review complete, report attached https://redwireglobal.sharepoint.com/:p:/r/sites/FlightSafety/Shared%20Documents/Incident%20Reports/VXE470CrashOnDescent/VXE470_Crash.pptx?d=w656c46ca8d3a45f79b71a48c5fc0bb4e&csf=1&web=1&e=3Osjv7
They definitely seem to have been flying overweight.  @Pat Wells can determine how to best message this and the warranty implications.
| VXE30 Standard MB+HLB no payload | 43.5 |
| HD55 | 5.2 |
| Snake Eagle | ? |
| Mod A kit | 4.45 |
| Config TOW | 53.15+Snake Eagle |
|  |  |
| Standard MGTOW | 49 |

## Root Cause

Aircraft appears to have been flying over MGTOW by ~3.9 lbs. This likely exceeded the capacity of the lift ESC and damaged it. 
Lift system did not have sufficient power to keep the vehicle airborne during the descent.  Likely ESC failure or bad connector.
Based on the throttle (railed for RF) and the current readings (higher for right), it seems the issue is likely due to RF ESC.

## Comments (22)

### Eric Brewer, 2024-12-04

@David Grosher @Pat Wells @Greg Fryer I took a look through the logs and compiled a report.  The lift system did not have enough power to arrest the descent, I suspect due to a bad connection to one side of the lift system (right side throttles were pegged so I suspect that’s the side that wasn’t able to draw full power).  Recommend inspecting the connections.  @Cameron Chapman FYI.
It’s also plausible a CG imbalance on descent would look like this - was this a wing drop flight where maybe one side was still remaining on landing?

### Pat Wells, 2024-12-04

@Alexander Alan Arnold please reach out to Frank reference inspecting the connection.

### Cameron Chapman, 2024-12-04

@Eric Brewer if the connection was bad, the current would drop when the throttles railed. It seems more likely an ESC or prop failure (probably ESC) on the right side. Likely ESC. Plotting commanded vs actual roll and pitch may help. 
We could have them inspect power connectors or return the equipment for inspection. Opening up the ESC case would be most informative, but I don’t think we want customers doing this as it could cast more concerns on our ESC reliability. 
@Alexander Alan Arnold I recommend customers do not plug in batteries and equipment after a crash, as this could further damage equipment or start battery fires.

### Eric Brewer, 2024-12-04

@Cameron Chapman added chart 5, there is a short time where there is a roll transient consistent with not enough lift from the right side (vehicle commanding left roll that is not followed well).

### Alexander Alan Arnold, 2024-12-06

@Pat Wells Pictures added

### Pat Wells, 2024-12-06

@Cameron Chapman @Eric Brewer pictures added

### Cameron Chapman, 2024-12-10

@Alexander Alan Arnold it is hard to tell from pictures compared to in person if anything looks off. Smell tests can also often indicate burning or electronics damage. Can you please include a comment either way for these and in the future when uploading photos? I will update the plan section.

### Alexander Alan Arnold, 2024-12-11

Do the logs say what weight was flying? HD 55 AND SNAKE EAGLE may be too much. We could ask if not

HD55 weighs 5.2 lbs, and then he had the MOD A kit attached with the SNAKE EAGLE Connected so it is leaning towards the AV being over weight @Eric Brewer

### Eric Brewer, 2024-12-11

@Cameron Chapman @Alexander Alan Arnold current draw does not look out of the ordinary when compared with other flights.

### Eric Brewer, 2024-12-20

@Cameron Chapman @Alexander Alan Arnold are we OK to move this to ‘implementing corrective action’?

### Alexander Alan Arnold, 2024-12-23

@Eric Brewer are we OK to move this to ‘implementing corrective action’? Id say yes.

### Cameron Chapman, 2024-12-23

@Eric Brewer @Alexander Alan Arnold I think no. We don’t have a confirmed or likely cause. We should either perform the steps in the plan, change the plan and update the other fields, or place it on hold if we think we will be able to perform those later. Moving back to D4.

### Eric Brewer, 2024-12-23

@Cameron Chapman updated fields above from discussions below.  The suspected root cause is RF ESC failure.  If there additional steps we can take to investigate that please recommend.

### Cameron Chapman, 2024-12-24

@Eric Brewer @Alexander Alan Arnold I missed a critical message below. Sorry about that. If they were flying a standard configuration, they definitely seem to have been flying overweight. 
@Alexander Alan Arnold did the customer mention the TOW or what batteries they were flying with? What is the weight of Snake eagle payload? I recommend asking those question if unknown.
@Eric Brewer is any of that information in the logs?
It is possible they were flying with an alternate approved configuration, per VXE-ES-23-002 Increased VXE30 Payload Weight (Modified Gains), Engineering Supplement. 
| VXE30 Standard MB+HLB no payload | 43.5 |
| HD55 | 5.2 |
| Snake Eagle | ? |
| Mod A kit | 4.45 |
| Standard Config TOW | 53.15+Snake Eagle |
|  |  |
| Standard MGTOW | 49 |

VXE30 Weight and MGTOW Summary
| Summary | Lbs |
| VXE30 Standard MB+HLB no payload | 43.5 |
| Standard MGTOW | 49 |
| Standard max payload weight | 5.5 |
| Max payload weight XE25 Main Battery | 9.3 |
| Max payload weight modified gains and transition alt | 8.5 |

### Pat Wells, 2024-12-27

@Alexander Alan Arnold  any updates to Cameron’s questions?

@Cameron Chapman  I highly doubt that they were flying with any alternate approved configuration by Edge.  Assuming the data will reveal that in the gains.

### Alexander Alan Arnold, 2024-12-27

@Cameron Chapman the customer stated that the weight of the Snake Eagle and the HD55 came out to 9.4 lbs. the batteries should be the standard main battery and HLB for VXE 30

### Cameron Chapman, 2024-12-29

@Pat Wells operator appears to have been flying over MGTOW. Assigning to you to communicate with them and update any RMA/Warranty info. See fields above.

### Alexander Alan Arnold, 2025-01-10

@Pat Wells Seems like operator error due to flying overweight how do you want to proceed?

### Pat Wells, 2025-01-10

@Alexander Alan Arnold we need to approve the report and provide it to the PM. Will not be covered under warranty. 
Once we’re good on the report we can move this to closed.

### Alexander Alan Arnold, 2025-01-10

@Cameron Chapman @Eric Brewer Can you guys finalize the report when you have some time so we can discuss the incident with the Customer and appropriate PM?

### Cameron Chapman, 2025-01-10

@Pat Wells I think it is pretty clear they were flying overweight. Can your group summarize in a report as needed, and let us know if you have any questions?

### Pat Wells, 2025-01-10

@Alexander Alan Arnold FYSA

## Attachments (7)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V470_241202_041020_pack.zip | archive | 3554 | 2024-12-03 | listed only |
| CW to fuselage cable.jpeg | image | 1606 | 2024-12-06 | listed only |
| boom connector (1).jpeg | image | 1820 | 2024-12-06 | listed only |
| boom connector 2.jpeg | image | 2006 | 2024-12-06 | listed only |
| center wing HLB connector.jpeg | image | 2354 | 2024-12-06 | listed only |
| fuselage to CW cable.jpeg | image | 2544 | 2024-12-06 | listed only |
| main battery connector.jpeg | image | 2384 | 2024-12-06 | listed only |
