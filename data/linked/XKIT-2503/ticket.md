# XKIT-2503: Test 5V Enable Solutions on Xkit nose cone with production Hargrave ESC (p/n: 100-114708)

- **Issue type:** Bug
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Medium
- **Created:** 2024-07-03
- **Updated:** 2026-07-13
- **Resolved:** 2026-07-13
- **Reporter:** Hayden Jeanor
- **Assignee:** Jeremy Kostel
- **Creator:** Hayden Jeanor
- **Parent:** XKIT-1917 Track Havoc Blk 1 Conversion Kit Parts for Env Expansion (3x)
- **Links:** relates to XKIT-1882 (Replace Blown 5V regulator on V376 Avionics Box); blocks XKIT-1921 (Procure and deliver all new motors & ESCs for new XKit Asset); relates to VA-1684 (Evaluate increasing servo voltage and enable removing boost boards for MAGNSS avionics boxes. ); relates to ENG-346 (1607P01A Improvements. XCOM / XE240 PWR COMMS BD); relates to VXEP-384 (VXE 545 Commanded aborted launch due to unusual behavior on ascent); relates to XKIT-2934 (Complete Xcomm hardware modifications for 5v ESC change); relates to XKIT-2966 (NFF the old ESCs after qualifying the new); relates to XKIT-3016 (Rebuild V695 AV Box for HAVOC)
- **Epic Link:** XKIT-1917

## Description

Last time we tried to power one of the newer hardware versions of the Hargrave ESCs (https://jenaero.atlassian.net/browse/XKIT-1882 ), the 5V bus dropped out and was not able to support the load that the ESC put on the Xcomm’s voltage regulator. Attempted to fix by putting a capacitor on the ESC end of the line from 5V to ground. This damaged the regulator on the XCOM. 
 We have not tried to integrate another ESC into a nose cone since. Need to test on IB. 
Status: This needs to be fixed before we build any more Xkit assets. The latest fwd ESC version is not compatible with VXE30 avionics box.

## Sprint

Havoc 12/4-12/31, XKIT 10/2-10/22, Havoc 1/22-2/11, Havoc 10/23-11/12, Havoc 2/12-3/4, XKIT 8/21-9/10, XKIT 9/11-10/1, Havoc 11/13-12/4, Havoc 3/5-3/25, Havoc 3/26-4/15

## Plan

Completed:
- Replication of issue
- Root Cause Analysis
- Identified Path Forward
- Adapt XCOMM Board for testing
- Functional Testing
- Dyno Testing

Left to do:
- Get HAVOC IB operational and replicate testing on full system level (could also test this on VXE30 IB with a 60V power supply to ESC, but better to get havoc IB functional.
- If successful discuss scope of change
- @Jeremy Kostel it seems like we are pretty safe to make this change. Please do the following first.
- Quick word document summarizing consumption vs capacity.
- Include scope captures of current and voltages of the 5V line pre and post modification.
- Clearly mark nose as for use with 695 avionics box only. Change to Havoc only once all have been reworked.
- Assign new PN or config number for Havoc avbox and XCOM. Add documents to the vault as prototype.
- Identify time to rework 376 so that everything can be the same configuration.

## Issue Status

Problem has been identified and a possible solution has been partially tested.
Updated XCOMM board has been benchtop tested with the ESC and on the Dyno and both were a success.
Still need to check as an entire system. HAVOC IB is being worked on currently

## Comments (20)

### Jeremy Kostel, 2024-07-22

**Update:**

We are trying to get a spare together before flight testing on Wednesday (7/24). As a quick fix method, a DC-DC converter is being added to the nose cone (mnf p/n R-78W-0). 
[embedded: image-20240722-210345.png]
Initial testing was done with a 60V power supply connected to the ESC and a 28V power supply connected to the converter, which was connected to the 5V enable line.
The motor started and ran smoothly.
The 28V supply comes from the DC-DC converter connected to the fuel cell. 
X-Kit nose signal harness (p/n 126-115600) will need to be modified to incorporate the 28-5V converter. 

The question is how much testing needs to be done (i.e. hover test, functional checkout, sco check, etc) before feeling confident to use as a spare

### Jeremy Kostel, 2024-07-23

Potential quick fix shown here [embedded: 126-115600 5V Issue Quick Fix.pdf] 
**Initial Concerns:**

Because the 28V is already going through a DC-DC converter (60V-28V) we now have cascading converters. 
- Efficiency drop: I am not sure the efficiency of the 60-28V converter but the 28V-5V is 93%. Assuming 90% for 60-28, efficiency would be 0.93 x 0.90 = 83.7%.
- Noise: Cascading converters can cause increased noise which we know the ESCs are sensitive to
- Voltage Ripple from first converter: Will we need any type of filtering? I am not sure the specs on the 60-28V voltage ripple.

**Plan:**

Garrett is reviewing the harness change added to this comment. With his approval, I will power up the fuel cell and test to see if the ESC is functional. This is a quick test that does not require building an entire harness, but instead just a quick test harness
**Next Steps**

If the test is successful, next plan would be to build the harness shown above and then do a tethered test with the aircraft.

### Jeremy Kostel, 2024-07-24

**Post Testing Update:**

While attempting this solution on V376, an inadvertent connection between the Wing interface cable (part of Fuse signal harness) caused spark with HLB.
Testing was halted after this to assess V376 ( [XKIT-2624] VXE376 60V HLB Inadvertent Connection to CW Harness - Jira (atlassian.net) )

**Notes before incident:**

- Custom nose signal harness included the two ODU connectors with only the AV GND and AV (28V) lines present
- Pin 1 and pin 4 of the 10 pin ODU were spliced to the 5V converter
- Signal harness was built to receive PWM and PWM ground from a servo controller
- 5V signal was read on multimeter
- Converter working
- However, ESC still not enabling 
- It was not receiving the 8mA current needed
- troubleshooting stopped here for now

### Jeremy Kostel, 2024-07-26

[embedded: image-20240725-201748.png]
very quickly done schematic of the tester cable I made

### Jeremy Kostel, 2024-07-26

|  | Current draw on 5V enable line |
| Old FWD ESC | 6.9mA |
| new FWD ESC | 8.4mA |

### Jeremy Kostel, 2024-07-29

From Hargrave regarding the issue: 
- It appears the most likely reason for the brownout of your PSU  is due to the brick wall over current protection on the LDO (as opposed to thermal overcurrent protection). There is approx 8uF of local decoupling on the isolated side per unit, so this can cause repeated brown outs with that LDO. At 5V, the unit should be drawing under 8mA during operation, so 50 ohms series resistance to the ESC isolator power rail should be sufficient to avoid this behaviour.

### Jeremy Kostel, 2024-07-29

Minimum operating voltage on 5V enable line: 
| New ESC | 3.1V |
| OLD ESC | 2.5V |

### Jeremy Kostel, 2024-08-12

We have a 5V enable line on our ESC. This is supplied from the XCOMM board. The ESC PWR line from the xcomm has 100ohm resistor in series with ESC power. The ESC has an inrush current of ~32mA. This resistor is causing the 5V to drop too low to start the ESC, less than 3.4V (ESC min voltage) and is causing the issue. To solve this we have two options, make a change to the XCOMM board and change the 100ohm resistor to a 20ohm resistor. This option would create an XCOMM change, but the XCOMM would still be compatible with VXE30 as this line only goes to ESC_PWR which is not populated in VXE30. We also could progress with the DCDC converter from the 28V avionics power which would require a nose signal harness change

### Carl Graf, 2024-08-26

@Jeremy Kostel is this going to start up again, now that we are past MAGNSS?

### Jeremy Kostel, 2024-08-26

@Carl Graf working this as we speak

### Carl Graf, 2024-09-03

@Jeremy Kostel any updates here? Need to get this worked out and start converting asset #695 to support Havoc Prototype Envelope Expansion.

### Jeremy Kostel, 2024-09-03

@Carl Graf I got pulled onto the AS150 production stoppage early last week and still working that now. I have not been able to get back to this

### Jeremy Kostel, 2024-09-12

Update (9/12)
quick summary:
- refer to 8/12 update for more info
- ESC Power has a 100 ohm resistor on the XCOMM board. This resistance is too high, and causes too much of a voltage drop
- Removing this resistor solves the issue, and the XCOMM is still interchangeable between all systems as HAVOC is the only configuration to use the ESC Power line from the XCOMM

Schematics: 
- [embedded: image-20240912-211404.png]


[embedded: image-20240912-211516.png]
Test System:
- XCOMM board powered from power supply
- ESC powered from power supply
- Servo controller providing ESC PWM
- No other systems were involved in this specific testing

Testing:
- For this test the 100 ohm resistor will be removed
- solder pads for the resistor will be “jumped” together with solder

Results
- results are as expected, successful ESC operation
- no voltage drop present
- Total power consumption in steady state: 42mW (5v, 8.4mA)

Conclusions and next steps
- I would like to test this on the dyno
- same setup as shown here, but motor with props on and perform a simple ramp
- This is not expected to have any effect on the 5V line but would be good to verify before flying
- Once HAVOC I.B. is completed this would be good to test in the full system
- discuss the scope of this change
- in my opinion, this is the easiest of changes to allow for continued FWD flight.
- FC has no easily accessible 5V line and also is not ideal for grounding
- Any other 5V lines would require some major harness changes
- this requires no harness changes and is still compatible with all configurations of the aircraft

### Jeremy Kostel, 2024-09-13

Successful Dyno run completed this morning (9/13). Motor performance was as expected, and no cutouts or brownouts caused by the 5V enable line

### Jeremy Kostel, 2024-09-16

@Cameron Chapman Apologies, I forgot to tag you last week. Last two comments are the most recent updates on HAVOC ESC issue

### Cameron Chapman, 2024-09-16

@Jeremy Kostel thank you. Can you please list and estimate or measure total loads on this port vs capacity. You can add to this doc or a linked one Havoc Power Budget_DRAFT.xlsx
If we are planning a mandatory XCOM rework for Havoc, we should evaluate other easy changes like https://jenaero.atlassian.net/browse/XKIT-2900 and some from this list https://jenaero.atlassian.net/browse/ENG-346

### Jeremy Kostel, 2024-09-16

Worst case: 
- Power consumed on 5V line: 350mW
- draw from ESC: 42mW (5V @ 8.4mA)
- Draw from other IC’s:
- U23 (LTC1983-5) and U21 (AD8170ARZ)
- Total draw under full load 60mA
- Power available on 5V line: 750mW
- This is ~47% power consumption

### Cameron Chapman, 2024-09-25

@Jeremy Kostel it seems like we are pretty safe to make this change. Please do the following first.
- Quick word document summarizing consumption vs capacity.
- Include scope captures of current and voltages of the 5V line pre and post modification.
- Clearly mark nose as for use with 695 avionics box only. Change to Havoc only once all have been reworked.
- Assign new PN or config number for Havoc avbox and XCOM. Add documents to the vault as prototype.

### Jeremy Kostel, 2024-10-02

Quick report added to this ticket. HAVOC XCOM 5V Change.docx
note from Garrett before he left: “For now, I've created the PN "2119492-01" to apply to the new avionics box with the modified XCOMM”

### Christa Meck, 2026-07-13

No work done in over a year.  Canceling.

## Attachments (6)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20240722-210345.png | image | 46 | 2024-07-22 | listed only |
| [126-115600 5V Issue Quick Fix.pdf](attachments/22037_126-115600%205V%20Issue%20Quick%20Fix.pdf.md) | pdf | 1493 | 2024-07-23 | converted |
| image-20240725-201748.png | image | 49 | 2024-07-26 | listed only |
| image-20240912-211404.png | image | 10 | 2024-09-12 | listed only |
| image-20240912-211516.png | image | 339 | 2024-09-12 | listed only |
| [HAVOC XCOM 5V Change.docx](attachments/23769_HAVOC%20XCOM%205V%20Change.docx.md) | docx | 580 | 2024-10-02 | converted |
