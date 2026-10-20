# VXEP-1034: VXE 734 Smoking Gimbal

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-02-18
- **Updated:** 2025-06-24
- **Resolved:** 2025-06-24
- **Reporter:** Alexander Alan Arnold
- **Assignee:** John Gober
- **Creator:** Alexander Alan Arnold
- **Labels:** Edge_Asset, Weekly-incident-tracker
- **Links:** relates to VXEP-813 (E140 Octopus/VXE30 Isolation Issues: Arcing to Fuselage, mag interference suspected)
- **Vehicle Tail Number:** VXE 734
- **Vehicle Configuration:** Standard VXE 30 Battery configuration
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical
- **Product/Tech Owner:** Charles David Madewell

## Description

EDGE ASSET
 date of the incident was 14 FEB 2025

Student noticed gimbal mounting plate was warm upon investigation noticed that the gimbal mounting plate was arching between the fuselage. Photos are attached as well.

Shared sheet for gimbal troubleshooting. VXEP-813 + 1034 E140 Octopus VXE30 mag interference suspected Mount Ground Loop

## Corrective Action

5 May 25: The proposed corrective action is to electrically isolate the gimbal with a new payload cable and mounting system.  Both of these fixes are in the works. We should have something to test with late this week.
https://jenaero.atlassian.net/browse/VXEP-1038 
https://jenaero.atlassian.net/browse/VXEP-1037

## Plan

Questions from Cam @John Gober @Alexander Alan Arnold 
- When will we have the non-conductive fix ready to test? https://jenaero.atlassian.net/browse/VXEP-1039

Actions
- Create a linked task for the identified fix and test results.

## Issue Status

Gimbal SN EPS 6182. Conductive plate and mount seem to have been in use (according to pictures), but non-conductive reported. Asked to confirm.. Power return and case appear common in the gimbal and Silvus assembly. This is not ideal, and is a common cause of ground loops. 
https://jenaero.atlassian.net/browse/VXEP-1037

## Root Cause

5 May 25: The root cause appears to be a ground loop facilitated by the gimbal having internal power and signal grounds tied to the chassis COMBINED with a path to ground on VXE30 through the fuselage and the Silvus.

## Comments (10)

### Alexander Alan Arnold, 2025-02-18

Linking VXEP 813 since data from incident is also in there, and it is related

### Alexander Alan Arnold, 2025-02-19

We installed EPS 6182 we did not have a conductive plate or metal mount installed during the testing of VXE 734. @Cameron Chapman

### Alexander Alan Arnold, 2025-02-19

After we discovered the grounding issue source on the gimbal we decided to investigate the aircraft.
It was determined that on the pain power assembly. We had the multimeter on pin 1 of the blue connector that plugs into the nose cone assembly and the other multimeter pin on the rear screw hole of the Silvus and we got a reading of 5 ohms. I will add pictures soon.

### Cameron Chapman, 2025-02-19

@Alexander Alan Arnold @John Gober the pictures appear to show a conductive plate and mount. I do not think such arcing would be possible if they were non-conductive. Can you please confirm?

### Alexander Alan Arnold, 2025-02-19

the pictures are from the incident, not the testing after the incident @Cameron Chapman   The mount and plate from the incident were conductive.

### Charles David Madewell, 2025-03-11

Replace existing MP-0067-063-01 Mount Plate with new G-10 Mount Plate 2122473-01.

### Cameron Chapman, 2025-04-29

@Mike DeJesus @John Gober  do you have updates for this incident? What is the status of the non-conductive fix rollout and containment?

### Pat Wells, 2025-05-01

@Alexander Alan Arnold please follow up with John on the status of this.  Suspect it should be finished.

### Alexander Alan Arnold, 2025-05-05

@John Gober Please update the root cause and Corrective actions for this issue, and let me know if this can be closed out.

### John Gober, 2025-05-05

@Alexander Alan Arnold @Pat Wells The root cause appears to be a ground loop facilitated by the gimbal having internal power and signal grounds tied to the chassis COMBINED with a path to ground on VXE30 through the fuselage and the Silvus. The proposed corrective action is to electrically isolate the gimbal with a new payload cable and mounting system.  Both of these fixes are in the works. We should have something to test with late this week.

## Attachments (6)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 9b2523f1-3e81-4644-a41d-364ad5aedb2f.jpg | image | 56 | 2025-02-18 | listed only |
| VXE-734 VTOL.zip | archive | 82848 | 2025-02-18 | listed only |
| VXE-734 XCOMM.zip | archive | 20220 | 2025-02-18 | listed only |
| a7f83c82-8d93-4121-b3d1-60c732ecce2f.jpg | image | 83 | 2025-02-18 | listed only |
| bb0e851b-ea76-4c1b-9153-998c6b315c3a.jpg | image | 84 | 2025-02-18 | listed only |
| f4d14c07-5526-4b61-8d72-856c662c8010.jpg | image | 63 | 2025-02-18 | listed only |
