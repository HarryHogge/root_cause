# VXEP-720: VXE 490 main battery percentage reporting incorrectly during flight with MB's (S/N's 1967 and 1737)

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2024-10-14
- **Updated:** 2026-10-02
- **Resolved:** 2026-08-11
- **Reporter:** Pat Wells
- **Assignee:** Tom Westrich
- **Creator:** Pat Wells
- **Labels:** GS_Closed, Redwire, Weekly-incident-tracker
- **Links:** relates to VXEP-748 (VXE 674 734 main battery percentage reporting incorrectly S/N's 2101 & 2088); relates to VA-2115 (2 MB's (S/N's 1967 and 1737) do not seem fly intended 4 hrs on V490 ); relates to VXEP-759 (Simulation Overestimating Power Consumption); relates to VXEP-640 (IRAD: B40 Battery Charger); relates to SMUP-50 (Guidance and manual updates for battery checker based on SoC being for wrong battery chemistry); relates to VXEP-2008 (V979 OGCS and Battery Checker Discrepancy)
- **Customer:** Redwire
- **Vehicle Tail Number:** 490
- **Issue Status:** identified root cause and dispo’ed NCR’ed materials
- **Root Cause:** [VXEP-720] VXE 490 main battery percentage reporting incorrectly during flight with MB's (S/N's 1967 and 1737) - Jira
- **Incident Type:** Mission Failure/Abort
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

Statement from operator (Edge FLOPS):
Aircraft/GCS would show 50% on the main battery, but when updating the mission, the sim would indicate there wasn’t enough endurance to complete the 20 minute mission. After landing the battery checkers would show 15-20%. Proving the simulation was correct about low endurance. This situation was consistent with both batteries fully charged. 

AAR’s attached

## Corrective Action

[VXEP-720] VXE 490 main battery percentage reporting incorrectly during flight with MB's (S/N's 1967 and 1737) - Jira
- Guidance to ignore SOC % on checker and charger for Amicell batteries.
- Link to charger replacement project. @Tom Westrich do you anticipate still wanting a battery checker or just replacing this with the new charger.https://jenaero.atlassian.net/browse/VXEP-640
- https://jenaero.atlassian.net/browse/VXEP-759

## Plan

- @Pat Wells can you please ask them to tag and quarantine this battery until further investigation?
@David Grosher - done
- Data review. 
- How much endurance should be required to takeoff and fly the 20 minute mission?
- Compare use wh and SOC drop vs expected.
- Recommend next steps


- determine corrective action
- open an separate issue regarding the sim inaccuracies
- create a slide deck to report findings and close out investigation
- address is the Vlife variance in this flight needs to be further investigated
[embedded image-20241031-221815.png]

## Comments (28)

### Cameron Chapman, 2024-12-19

@Josh Burrell Approximate mapping below. Battery issues and resulting CAs like this one should be assigned for AA. @Tom Westrich should we assign those to @Christopher Ridgard  or someone else? FYI @David Grosher 
| HLB |  |  |  |  | Main Battery |  |  |
| %SOC | Vnl calc | V/cell |  |  | %SOC | Pack Voltage (no load) | Cell Voltage |
| 100 | 29.31 29.3*2=58.6 4.2*14=58.8 | 4.19 |  |  | 100 | 29.9 | 4.3 |
| 90 | 28.58 | 4.08 |  |  | 75 | 27.83 | 3.98 |
| 80 | 28.00 | 4.00 |  |  | 50 | 26.3 | 3.76 |
| 70 | 27.50 | 3.93 |  |  | 20 | 24.7 | 3.53 |
| 60 | 27.06 | 3.87 |  |  | 15 | 24.4 | 3.49 |
| 50 | 26.73 | 3.82 |  |  | 5 | 23.7 | 3.38 |
| 40 | 26.49 | 3.78 |  |  | 0 | 21.3 | 3.05 |
| 30 | 26.32 | 3.76 |  |  | 30 | 25.4 | 25.4/7=3.6286 |
| 25 | 26.23 | 3.75 |  |  |  |  |  |
| 20 | 26.14 | 3.73 |  |  |  |  |  |
| 10 | 25.80 | 3.69 |  |  |  |  |  |
| 0 | 24.54 | 3.51 |  |  |  |  |  |

### David Grosher, 2024-12-19

@Cameron Chapman @Josh Burrell The CA is an update to the Manual which is why it was assigned to Josh. The charger work that Tom is doing would also resolve this in the longer term but that shouldn’t be tracked here.

### Tom Westrich, 2024-12-20

@Cameron Chapman , We are about to post for our Battery Product Engineer (like Sean Wendling, but for batteries/chargers) who would handle battery CAs, but this doesn’t look like an issue they or AA would have issued a CA for.

### Josh Burrell, 2025-01-30

@David Grosher @Cameron Chapman Can someone please point me in the right direction. @Tom Westrich is saying they wouldn’t have issued a CA so is there a real need for a manual update?

### David Grosher, 2025-01-30

@Josh Burrell, @Tom Westrich would own the resolution of this issue in terms of whether any change in communication is required. This issue stems from an incident on our own asset. It was determined that the Batter Checker in the FSK provided incorrect SoC data based on an incorrect battery model in the checker for the Amicell battery chemistry. I honestly don’t know what if any guidance is provided to customers on the battery checker.

### Cameron Chapman, 2025-01-30

@Tom Westrich the current battery checkers and chargers report an incorrect SOC for Amicell and Amprius packs. Why would we not issue CAs for that? 
Proposed:
- Guidance to ignore SOC % on checker and charger for Amicell batteries (ideally manual update or other supplement).
- Link to charger replacement project. @Tom Westrich do you anticipate still wanting a battery checker or just replacing this with the new charger.

@Josh Burrell  FYI

### Tom Westrich, 2025-01-30

@Cameron Chapman , @Josh Burrell , I agree that a manual update to limit the reliance on the checker to provide accurate SOC indication on the battery is a good CA.  I was confused because we have zero ability to inform change on the checkers, which makes a CA on the Checkers a moot point.

### Josh Burrell, 2025-01-31

@Dana Holley Here’s an easy one for the OPS can you add a note please?

### Dana Holley, 2025-02-03

@Cameron Chapman  @Tom Westrich I have noticed that if the battery does not trickle charged @ 99% to completion @ 100%, then battery variance in SOC may vary quite significantly. Do we have more than one instance of a fully charged battery where this occurs? There is also a voltage range in the manual stating the charge range should be from 25.5-26V, which I’ve seen set incorrectly from Edge and/or the end user, which could have some effects. Unplugging during balancing may also cause further issues. Many variables to this.
I haven’t had any issues with the accuracies of the battery checker (if battery is fully charged) and we heavily rely on the checkers as it provides efficiency and expediency. If the suggested guidance was followed in the manuals to ignore SOC % on checker and charger, then we are also stating our batteries chargers may not provide 100% charge to our batteries and that they should be only accurately checked in SUAV after connecting to the GCS software. 
 I would propose the following as a CAUTION in the MX Man -Battery Charging section and Ops Man- Battery Life section. “ Operators should only use the VXE SUAV Aircraft Status window or appropriate Launch Wizard steps to accurately reference state of charge (SOC) percentage for HLB and main batteries. Do not solely rely on the SOC percentage of the battery checker or charger.” @Josh Burrell

### Cameron Chapman, 2025-02-05

@Dana Holley mostly curious, as I have not had time to check. Does the checker report a different SOC between 4.2v/cell and 4.3v/cell when plugged into a main batt? It may be minor, but it may be reading 100% both for a fully charged battery and one charged only to 4.2. It should be much more accurate for HLBs as they are standard lipo cells. It will have issues for amprius cells on the low end if ever used with them (we are planning not to)

### Dana Holley, 2025-02-07

@Cameron Chapman @Tom Westrich Not 100% sure as I’ve always practiced the described procedures listed. Please let me know what action we should take for the Ops Manual. I have listed a statement we could add pending if information I have provided was not the cause for this issue. @Josh Burrell

### Cameron Chapman, 2025-02-11

@Tom Westrich can you confirm these checkers will be obsoleted once the new chargers are rolled out? Can you open a subtask to obsolete them in that project and link here if so.

### Drew Cunnien, 2025-03-04

@Josh Burrell @Dana Holley @Cameron Chapman 
Per @Tom Westrich that is correct: the checkers will be obsoleted once the new chargers are rolled out.

We agree with Dana’s verbiage: I would propose the following as a CAUTION in the MX Man -Battery Charging section and Ops Man- Battery Life section. “ Operators should only use the VXE SUAV Aircraft Status window or appropriate Launch Wizard steps to accurately reference state of charge (SOC) percentage for HLB and main batteries. Do not solely rely on the SOC percentage of the battery checker or charger.”

This seems to be the best way to address this in the manuals while the new stuff is developed.
@Alex Senita

### Josh Burrell, 2025-03-04

@Drew Cunnien @Dana Holley the proposed wording reads like a NOTE, is there any threat to the aircraft based on what we’re telling them to do? If we want a Caution we need to tell them what will happen if they don’t follow it.

### Drew Cunnien, 2025-03-26

@Josh Burrell @Dana Holley I apologize, there was a decision.

We agree with you Josh, that this should be a NOTE not a CAUTION. As far as we can tell this issue does not pose a significant threat to the aircraft.

Apologies for the late reply!

### Dana Holley, 2025-03-26

@Josh Burrell @Drew Cunnien Josh is correct in that it’s currently written like a NOTE. If the aircraft can crash, which it could, then it must be a CAUTION with the wording that  suggests an aircraft crash may occur if guidance is not followed. Are we putting this in both manuals and the OS?

### Josh Burrell, 2025-03-26

@Dana Holley I’m thinking we need it in all three that way it doesn’t get missed. @Drew Cunnien you want to give us the final version of the Caution to add?

### Christa Meck, 2025-08-05

@Dana Holley @Josh Burrell We got the documentation all sorted?  I see this is related to https://jenaero.atlassian.net/browse/SMUP-50  which isn’t done yet so just checking in.

### Pat Wells, 2026-08-11

@Josh Burrell was the documentation updated to reflect this guidance?

### Josh Burrell, 2026-08-11

@Pat Wells Adding this NOTE: 
Operators should only use the VXE SUAV Aircraft Status window or appropriate Launch Wizard steps to accurately reference the SOC percentage for HLB and main batteries. Do not solely rely on the SOC percentage of the battery checker or charger.

### Drew Cunnien, 2025-03-04

@Josh Burrell @Dana Holley @Cameron Chapman 
Per @Tom Westrich that is correct: the checkers will be obsoleted once the new chargers are rolled out.

We agree with Dana’s verbiage: I would propose the following as a CAUTION in the MX Man -Battery Charging section and Ops Man- Battery Life section. “ Operators should only use the VXE SUAV Aircraft Status window or appropriate Launch Wizard steps to accurately reference state of charge (SOC) percentage for HLB and main batteries. Do not solely rely on the SOC percentage of the battery checker or charger.”

This seems to be the best way to address this in the manuals while the new stuff is developed.
@Alex Senita

### Josh Burrell, 2025-03-04

@Drew Cunnien @Dana Holley the proposed wording reads like a NOTE, is there any threat to the aircraft based on what we’re telling them to do? If we want a Caution we need to tell them what will happen if they don’t follow it.

### Drew Cunnien, 2025-03-26

@Josh Burrell @Dana Holley I apologize, there was a decision.

We agree with you Josh, that this should be a NOTE not a CAUTION. As far as we can tell this issue does not pose a significant threat to the aircraft.

Apologies for the late reply!

### Dana Holley, 2025-03-26

@Josh Burrell @Drew Cunnien Josh is correct in that it’s currently written like a NOTE. If the aircraft can crash, which it could, then it must be a CAUTION with the wording that  suggests an aircraft crash may occur if guidance is not followed. Are we putting this in both manuals and the OS?

### Josh Burrell, 2025-03-26

@Dana Holley I’m thinking we need it in all three that way it doesn’t get missed. @Drew Cunnien you want to give us the final version of the Caution to add?

### Christa Meck, 2025-08-05

@Dana Holley @Josh Burrell We got the documentation all sorted?  I see this is related to https://jenaero.atlassian.net/browse/SMUP-50  which isn’t done yet so just checking in.

### Pat Wells, 2026-08-11

@Josh Burrell was the documentation updated to reflect this guidance?

### Josh Burrell, 2026-08-11

@Pat Wells Adding this NOTE: 
Operators should only use the VXE SUAV Aircraft Status window or appropriate Launch Wizard steps to accurately reference the SOC percentage for HLB and main batteries. Do not solely rely on the SOC percentage of the battery checker or charger.

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V490_241007_121207_pack.zip | archive | 3496 | 2024-10-14 | listed only |
| T95_V490_241008_112513_pack.zip | archive | 3020 | 2024-10-14 | listed only |
| T95_V490_241010_102426_pack.zip | archive | 3263 | 2024-10-14 | listed only |
| image0.jpeg | image | 4744 | 2024-10-14 | listed only |
| image-20241031-221815.png | image | 287 | 2024-10-31 | listed only |
