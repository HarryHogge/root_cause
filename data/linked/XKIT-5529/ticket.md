# XKIT-5529: V1038 Troubleshooting Steps

- **Issue type:** Task
- **Status:** New
- **Priority:** Low
- **Created:** 2026-06-25
- **Updated:** 2026-07-20
- **Reporter:** Jeremy Kostel
- **Assignee:** Alexander Alan Arnold
- **Creator:** Jeremy Kostel
- **Links:** relates to VXEP-1933 (VXE 1038 VTOL motors failed to shut off after transition to fixed wing flight); relates to XKIT-5550 (SLO EE Troubleshooting Plan)

## Description

Test plan for V1038 aircraft

## Plan

@Alexander Alan Arnold  to coordinate returning to SLO for troubleshooting. Please add tracking info when availalble. 
Per Jeremy: We werent able to recreate the real issue that I was looking for. However there we some good findings on the weirdness with M1 (front left). At a minimum I would request a replacement ESC and motor at that location. But really I would like to get the aircraft back to SLO for troubleshooting if possible. M1 behavior doesnt match expected behavior but could be an unrelated issue from what happened.

## Issue Status

HSV FLOPs performed the full test plan. We were unable to replicate the issue. Requested HSV to return the aircraft to SLO for further investigation

## Comments (9)

### Alexander Alan Arnold, 2026-07-06

@Jeremy Kostel We are going to get started on this today however the operators note point to the main battery being 15 and HLB 53 not HLB 61 listed in the baseline config. Do we know where the 61 SN came from?

### Jeremy Kostel, 2026-07-06

@Alexander Alan Arnold check the first section of this for more details, but basically the SNs listed here are what the battery SW is reporting in the logs. That does not mean it matches visibile labels

### Michael Mohr, 2026-07-07

@Jeremy Kostel @Cody Smisek Uploaded the test data I gathered from yesterday and today. I involved both S/N 53 and 61 HLBs in the testing.

### Jeremy Kostel, 2026-07-07

@Michael Mohr awesome thanks Michael. Ill review

### Alexander Alan Arnold, 2026-07-09

@Jeremy Kostel Were you able to find anything from the testing?

### Jeremy Kostel, 2026-07-09

@Alexander Alan Arnold We werent able to recreate the real issue that I was looking for. However there we some good findings on the weirdness with M1 (front left). At a minimum I would request a replacement ESC and motor at that location. But really I would like to get the aircraft back to SLO for troubleshooting if possible. M1 behavior doesnt match expected behavior but could be an unrelated issue from what happened. 
FYSA @Scott Whitney

### Alexander Alan Arnold, 2026-07-09

@Jeremy Kostel alright thank you, Ill work with addison to see what he wants to do. this aircraft also needs inspection to see if its effected by the JST crimp Issue.

### Jeremy Kostel, 2026-07-09

@Alexander Alan Arnold if sent back to SLO we could handle both here

### Cameron Chapman, 2026-07-20

Moving completed steps from Plan field. Plan should be used for what is next, not what is done. 
**V1038 Test Procedure (Field Use)**

**Pre-Test Verification: Battery Serial Number Check**

Purpose:
Confirm that the batteries used match the units from the V1038 incident flight and verify that the physical serial numbers match what is reported in logs.
**Steps**

- Install Batteries
- Use the batteries from the V1038 incident flight for baseline testing.
- Check Physical Serial Numbers
- Record serial numbers from the battery labels/stickers.
- Pull XCOM Event Log
- Locate entries similar to:

```
[17:06:33.543 505.543] MB
[17:06:33.544 505.544] 0x000019  online: yes
[17:06:33.554 505.554] HLB
[17:06:33.555 505.555] 0x000032  online: yes

```
- Convert Serial Numbers
- Values shown (e.g., 0x000019, 0x000032) are hexadecimal
- Convert to decimal using an online converter
- Compare Results
- Verify log-reported SN matches physical sticker SN
- Note any mismatches

**If Verified**

- Proceed with baseline test procedure

**If Mismatch Found**

- Record discrepancy
- Continue testing, but flag results for review

**Baseline Setup**

- MB SN 15
- HLB SN 61
- Original batteries, surfaces, booms
- These are the software reported SNs
- The intent is to use the exact ones from flight
- We tested both HLB S/Ns 53 and 61. There was some internal debate on which was actually installed in aircraft 1038 during the incident but decided to just involve both in the testing.

**Test Steps (Do every time)**

- Assemble aircraft
- Power ON → wait 5 minutes
- Check:
- LW motors
- Control surfaces
- Stay powered ON → another 5 minutes
- Pull AAR
- Send AAR to SLO

**Run This Test for Each Config Below**

**1. Baseline**

- Run test as-is
- Test ran with Main Battery 15 and HLB 53

[embedded: AAR_V1038_B35_20260706T210701Z (58196dea-b3c1-4618-8f75-37d6cf02ab1a).zip]
- Test ran with Main Battery 15 and HLB 61
- Left front lift motor was hesitant

[embedded: AAR_V1038_B35_20260707T131811Z (8da5e8b9-9259-4f0c-976a-46458e81392c).zip]
**2. Swap MB**

- Install different MB (record SN) 25
- Run test
- Test ran with Main Battery 25 and HLB 53

[embedded: AAR_V1038_B35_20260706T212809Z (23b04f2e-625b-43ae-89f9-fa245b35fa9d).zip]
- Test ran with Main Battery 25 and HLB 61

[embedded: AAR_V1038_B35_20260707T160642Z (a5c90586-c2dc-43c6-b259-df93006ccb7e).zip]
**3. Swap HLB**

- Put original MB back (SN 15)
- Install different HLB (record SN)
- Run test
- Test ran with Main Battery 15 and HLB 61
- Front left motor failed to spin on first motor test. It made a loud buzzing sound for what would have been the duration of the check (same sound as the hesitation in the first video). We spun the front left prop several more times to try and recreate but it spun each time. It did hesitate a couple times and when it homed, it did so in reverse a couple times also.

[embedded: AAR_V1038_B35_20260707T125747Z (6ac5072f-2a97-4ceb-aff9-7ea9e32a1d54).zip]
- Hesitation

[embedded: MicrosoftTeams-video (1).mp4]
- Home in reverse

[embedded: MicrosoftTeams-video.mp4]

**4. Swap Surfaces**

- Use original MB + HLB
- Install from different aircraft:
- Left aileron
- Right aileron
- Rudder
- Elevator
- Run test
- Test ran with Main Battery 15 and HLB 61 with surfaces from aircraft 1022
- Left front motor hesitant.

[embedded: AAR_V1038_B35_20260707T133716Z (c54ad285-e09b-446c-b3e9-07c6601447c6).zip]
- Test ran with Main Battery 15 and HLB 53 with surfaces from aircraft 1022

[embedded: AAR_V1038_B35_20260707T140057Z (a67412ba-e7c0-473d-8607-829592054286).zip]
**5. Swap Booms**

- Return to full original config
- Install booms from another aircraft
- Run test
- Test ran with Main Battery 15 and HLB 53 with booms from aircraft 1022

[embedded: AAR_V1038_B35_20260707T151858Z (9412290e-dbc9-4f07-8a5c-32530c78b818).zip]
- Test ran with Main Battery 15 and HLB 61 with booms from aircraft 1022

[embedded: AAR_V1038_B35_20260707T153908Z (e21de363-fd96-4a68-942c-102830c7c146).zip]
**Notes**

- Record all serial numbers
- Note any warnings or issues
- Make sure AAR is saved for each run

## Attachments (11)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_V1038_B35_20260706T210701Z (58196dea-b3c1-4618-8f75-37d6cf02ab1a).zip | archive | 10631 | 2026-07-20 | listed only |
| AAR_V1038_B35_20260706T212809Z (23b04f2e-625b-43ae-89f9-fa245b35fa9d).zip | archive | 14100 | 2026-07-20 | listed only |
| AAR_V1038_B35_20260707T125747Z (6ac5072f-2a97-4ceb-aff9-7ea9e32a1d54).zip | archive | 22359 | 2026-07-20 | listed only |
| AAR_V1038_B35_20260707T131811Z (8da5e8b9-9259-4f0c-976a-46458e81392c).zip | archive | 27136 | 2026-07-20 | listed only |
| AAR_V1038_B35_20260707T133716Z (c54ad285-e09b-446c-b3e9-07c6601447c6).zip | archive | 30541 | 2026-07-20 | listed only |
| AAR_V1038_B35_20260707T140057Z (a67412ba-e7c0-473d-8607-829592054286).zip | archive | 35451 | 2026-07-20 | listed only |
| AAR_V1038_B35_20260707T151858Z (9412290e-dbc9-4f07-8a5c-32530c78b818).zip | archive | 41034 | 2026-07-20 | listed only |
| AAR_V1038_B35_20260707T153908Z (e21de363-fd96-4a68-942c-102830c7c146).zip | archive | 45355 | 2026-07-20 | listed only |
| AAR_V1038_B35_20260707T160642Z (a5c90586-c2dc-43c6-b259-df93006ccb7e).zip | archive | 51984 | 2026-07-20 | listed only |
| MicrosoftTeams-video (1) (e6435b23-dd4c-49b6-bbc7-54904a56f598).mp4 | video | 5050 | 2026-07-20 | listed only |
| MicrosoftTeams-video (dfd483aa-c8dc-4ca8-be82-4d65c176ca06).mp4 | video | 1214 | 2026-07-20 | listed only |
