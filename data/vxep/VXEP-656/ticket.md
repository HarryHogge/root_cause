# VXEP-656: Upgrade VXE30 55lb 15lb payload

- **Issue type:** Initiative
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** High
- **Created:** 2024-09-27
- **Updated:** 2026-09-30
- **Resolved:** 2026-09-30
- **Reporter:** Cameron Chapman
- **Creator:** Cameron Chapman
- **Links:** relates to VXEP-663 (Populate 55lb spreadsheet with flight science estimates/previous data )
- **Leadership Stakeholder:** Sam Miller

## Description

May be required for LRR to compete with competitor specs. See child issues. 
Files VXE30 55lbs

## Plan

Populating this sheet to classify parts as upgrade needed or recommended and ROM VXE30 55lbs.xlsx @Ryan Christino can you please populate the information you can determine, then I will add items such as contact current capacity and test data? 
- Hayden Can you please answer the following questions Greg requested Friday (and update the sheet accordingly)?
- Could the same ESCs and hardware configurations operate with a 7S and 14S battery in a VXE30 frame, then the firmware could adapt max power and other parameters accordingly?
- This would help determine/sell the 7S vs 14S question by allowing customers to use their existing 7S batteries.
- If not, what would we have to change to convert from one to another?

## Comments (5)

### Cameron Chapman, 2024-09-27

@Ryan Christino and @Everett Werner can you please indicate calculate if the VXE30 motors could support 55lb MGTOW (first calculate for standard conditions, report, then for extreme conditions (altitude and heat)). 
Please let us know how much current/power would be required for each using standard VXE30 batteries.

### Everett Werner, 2024-09-27

@Cameron Chapman  
I was under the impression that the expectation was that this portion of the effort would be ROMs but to answer your question:
I believe we have flown at 55lbs with vxe30 before so the vxe30 could support it in nominal conditions. I suspect we would need tests to validate the extreme conditions. @Ryan Christino do you know where we could find the dataset to validate power consumption? I feel fairly confident that we will require testing though.
Ryan says:
The VXE30 motor throttle is saturated at 55 lbs. near sea level at a slow climb rate. If we are more confident in the connectors / ESC / motors then we could bump the climb rate even a little slower and maybe make it work but will definitely require additional testing. My guess is that we can make the VXE30 fly okay at 53 lbs. at a low DA but 55 is going to be sketchy unless we can get back some margin on the system.

### Cameron Chapman, 2024-09-27

Thanks @Everett Werner and @Ryan Christino. In that case, do you think the quickest path to make VXE30 capable of reliably flying at 55 lbs would be to implement the Havoc motors short term and longer term optimize for VXE30? 
Are you referring to VTOL or FW motors? 
Can you please respond for both, and if you have any data for the FW ESC at that load. I am pretty sure the lift ESCs could not reliably support it.

### Ryan Christino, 2024-09-30

@Cameron Chapman I attached 4 VTOL logs from the heavy weight flight test. One is a baseline and the other three are VTOL climb / aborts at 55 lbs. with a few different configurations of asymmetric weight and climb rates. The power consumption when fully saturated is at about the 5-kW mark. I think you are correct in that the ESC’s are the “weak” link when operating at this upper end.  The VXE30 motors are going to be very marginal based on the temperature increase at those powers in the Launch-Land-Pause worst case profile however they could probably get us successful “nominal” flights with a capable ESC. I had an estimate that we would have about 80 seconds before the motors got too hot based on this testing (140F Ambient Assumed). Using the VXE30 motors as is with considerations for flight test procedures could be a way forward however a little risky. Using the Havoc motors would alleviate this issue although the KV on the Havoc motors is about half so we’d have to do some testing to make sure they would achieve the RPM and thrust at the lower voltage.
We did not perform any flights with fixed wing at 55 lbs. with the VXE30 in a baseline configuration so the forward motor power consumption could be best estimated from the X-Kit once we have some clean power numbers. An approximation for the power is 400-500W in cruise but we could definitely refine that number.

### Christa Meck, 2026-09-30

No work done in almost a year.  Canceling.

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [T95_VT406_211202_100237_vtl00437.csv](attachments/23540_T95_VT406_211202_100237_vtl00437.csv.md) | csv | 5003 | 2024-09-30 | converted |
| [T95_VT406_211202_101101_vtl00438.csv](attachments/23539_T95_VT406_211202_101101_vtl00438.csv.md) | csv | 3919 | 2024-09-30 | converted |
| [T95_VT406_211202_102116_vtl00439.csv](attachments/23538_T95_VT406_211202_102116_vtl00439.csv.md) | csv | 3803 | 2024-09-30 | converted |
| [T95_VT406_211202_104724_vtl00440.csv](attachments/23537_T95_VT406_211202_104724_vtl00440.csv.md) | csv | 3507 | 2024-09-30 | converted |
