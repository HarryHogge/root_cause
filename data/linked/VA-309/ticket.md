# VA-309: VXE450 Hands on troubleshooting. Identify root cause

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2023-08-23
- **Updated:** 2024-02-28
- **Resolved:** 2024-02-28
- **Reporter:** Connor Peebles
- **Assignee:** Connor Peebles
- **Creator:** Connor Peebles
- **Labels:** 8-28-Sprint
- **Links:** relates to ENG-3034 (Aircraft 450 VTOL Landing Crash-ESC Damage); blocks VXEP-51 (Internal - Aircraft 450 VTOL Landing Crash - ESC soft start); relates to VA-555 (Implementation of Permanent Magnetic Shaker for Testing (vibe table))
- **Sprint:** VXE-1 Cameron's Team 9-17, VXE-1 Electrical 10/29, VXE-1 Electrical 11-20-12/10, VXE-1 Electrical 10/9

## Description

Q20 failed, melted solder pads and was free in enclosure. Doesn’t cease motor function.
U1 failed, ceases ESC function, ceases motor function.

## Comments (9)

### Cameron Chapman, 2023-08-24

Linking subtasks to parent

### Cameron Chapman, 2023-09-03

@Connor Peebles Comments added to investigation ppt. Please review.

### Connor Peebles, 2023-09-29

RECAP: On the bottom of the ESC, U1 (5V linear regulator) seems to have failed.

[embedded: IMG_0246.jpg]
This would then not power U2 which in turn powers the FET drivers. This would also cause the CPU to not power.

### Connor Peebles, 2023-09-29

Setting up an experiment to try to replicate the damage to U1 to gain insight into the nature of the failure, we went through 3 different test scenarios:  - will it lead to crater failure? 
- Constant thermal shutoff
- Constant overcurrent
- Input overvoltage

### Connor Peebles, 2023-09-29

- constant thermal shutoff

[embedded: image-20230929-165248.png]
per the data sheet of U1, thermal shutoff occurs around 175C of the IC junction temperature. Using a blue heat gun, we could consistently get the thermal shutoff to occur, causing our output to go from 5V to 0V. After cooling down for less than 2 seconds it resumes normal function.
[embedded: IMG_E6014.JPG]
Performing this up to 10 times leads us to conclude that this did not cause the cratering failure we saw in 450.

### Connor Peebles, 2023-09-29

2. constant overcurrent
U1 is designed so that once it reaches overcurrent (~1.5A) the voltage starts to drop to compensate w/ a current fold back circuit.
[embedded: image-20230929-173318.png]
Using a 3.3Ohm high power resistor to attempt to pull ~3.5A; 
[embedded: image-20230929-173724.png]
We saw the voltage drop as expected and U1 heat up to ~161degC 
[embedded: IMG_E6017.JPG]
It could reach this temp for multiple cycle attempts, after which we started shorting U1 output and then input to ground to create current spikes of up to 3A. U1 could always recover and operate normally, this leads us to conclude that this did not cause the cratering failure we saw in 450.

### Connor Peebles, 2023-09-29

3. Input overvoltage (w/ high current)
Gradually increasing voltage from 12V to 30V, which then exceed the Vin maximum of the IC, did not immediately lead to failure. Disconnecteing and reconnecting Vin 5 imes in quick succession then caused the IC to fail, with similar cratering as seen in 450. 
[embedded: image-20230929-175647.png]
[embedded: IMG_0531.jpg]
- Note that during this test the High power resistor was still hooked up, which would lead to great inrush current.
- And the quickly disconnecteing and reconnecting could lead to reverse current through the IC becuase of the lack of a reverse current bypass diode. This was done for this test because on 1711P01 it is also lacking a reverse current bypass diode. This could be explored more.

Going to repeat this test again with a high value resistor to eliminate the inrush current variable
Repeated
- Does not happen with a load within operating limits (less than safe operating limits for U1 (under 1A))
- Repeatable with high load and overvoltage

### Connor Peebles, 2023-10-04

[embedded: Summary.JPG]
here is a summary of what happened

### Connor Peebles, 2023-10-04

some possible design CAs 
[embedded: corrective.JPG]

## Attachments (10)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| IMG_0246.jpg | image | 5910 | 2023-09-29 | listed only |
| IMG_0531.jpg | image | 5199 | 2023-09-29 | listed only |
| IMG_E6014.JPG | image | 2714 | 2023-09-29 | listed only |
| IMG_E6017.JPG | image | 2281 | 2023-09-29 | listed only |
| image-20230929-165248.png | image | 75 | 2023-09-29 | listed only |
| image-20230929-173318.png | image | 30 | 2023-09-29 | listed only |
| image-20230929-173724.png | image | 73 | 2023-09-29 | listed only |
| image-20230929-175647.png | image | 67 | 2023-09-29 | listed only |
| Summary.JPG | image | 334 | 2023-10-04 | listed only |
| corrective.JPG | image | 255 | 2023-10-04 | listed only |
