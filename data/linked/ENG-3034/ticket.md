# ENG-3034: Aircraft 450 VTOL Landing Crash-ESC Damage

- **Issue type:** Problem
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2023-07-17
- **Updated:** 2026-08-31
- **Resolved:** 2025-05-21
- **Reporter:** Daniel Lloyd
- **Assignee:** Cameron Chapman
- **Creator:** Daniel Lloyd
- **Labels:** 8-28-Sprint, MARSOC
- **Links:** relates to XEO-113 (VXE Lift ESC improvements for next revision); relates to FS2-573 (Perform Pre-VTOL transition check on VTOL lift system); is blocked by FS2-588 (VIT2-327); relates to ENG-2971 (V450 Center Wing Screw Stuck); relates to RMA-130 (VXE-450 230726); relates to VA-761 (VTOL Lift motor life limit); is cloned by ENG-3052 (CLONE - Aircraft 450 VTOL Landing Crash); relates to VA-311 (VXE450 Implement Corrective Action: Eng create inspection guidance for MOSFETs. 107-102974 Lift ESC Assembly ); relates to VA-310 (VXE450 Review root cause and document Corrective Actions); relates to VA-309 (VXE450 Hands on troubleshooting. Identify root cause); relates to VXEP-44 (VXE-450 VTOL Landing Crash); relates to VA-444 (Evaluate replacing VXE30 ESCs); relates to FS2-755 (ESC Check prior to VTOL transition); relates to VXEP-628 (Systemic VXE30 VTOL ESC Reliability Issues ); relates to VXEP-384 (VXE 545 Commanded aborted launch due to unusual behavior on ascent)

## Description

Live copy Vehicle Investigation V450 V2.pptx
Aircraft was participating in operator training at Camp Lejeune NC. It was in the fuel cell configuration with a Trillium HD55 payload. This was the second flight on this day. During the LW the ground crew indicated that the right front lift motor sounded different during the spin-up checks. The check was repeated several times and determined to be fine. The launch was uneventful. Per the flight profile, at around twenty minutes into flight the aircraft was commanded to RTB. The aircraft transitioned to vertical flight and then continued to drift past the programmed LZ toward the south. Attempts to nudge the aircraft back to the LZ produced no effect. The aircraft was placed in manual nudge which also produced no effect. At some point the aircraft dropped suddenly to the ground. 
The crash site was isolated from the flying field by dense woodlands and had to be accessed by boat. Reports from the site were the aircraft was entirely consumed by fire. The center wing was recovered from within the trees.
Pictures and AAR data are not available until released by the customer.

Centerwing was spares CW SN 4008
Surviving Lift ESC Assy (Front Right) 107-101631-2 SN 069

## Comments (42)

### Cameron Chapman, 2023-07-17

FYI @John Clark . Standing by for AAR.

### Daniel Lloyd, 2023-07-18

Adding picture of the only recovered items, the forward right motor and the center wing. Also pictures of the CW lift boom power connectors.

### Cameron Chapman, 2023-07-18

Assigning to Dan to update if AAR or equipment becomes available for us to troubleshoot. Added MARSOC to operator field for tracking. 
FYI @Pat Wells @Greg Fryer

### Daniel Lloyd, 2023-07-18

This aircraft was not involved in any landings in tall grass during this class.

### Daniel Lloyd, 2023-07-19

NOTE:
AAR files uploaded. The 17 July file from 450 is the AAR created post mishap before and aircraft remains were located.
The 18 July AAR file from 439 was created with 450 center wing connected to surrogate fuselage 439.
@Cameron Chapman @Pat Wells

### Greg Fryer, 2023-07-19

@John Clark @David Grosher Data has arrived, needs review ASAP.

### David Grosher, 2023-07-19

As the landing video seems to indicate the Front Right lift motor doesn’t appear to be spinning. During the landing sequence there is a time when the right boom is pulling almost no current and that happens when the rear right motor is at zero throttle despite the forward right motor having the throttle set at >50%.  This would isolate the issue between the VTOL AP PWM driver to the Front Right ESC motor.  The vehicle would have likely drifted due to an inability to maintain the commanded pitch and roll. 
[embedded: image-20230719-183356.png]

### Cameron Chapman, 2023-07-19

It seems like the center wing is still relatively intact, and at least one of the ESCs look in tact (with a large impact). 
We could inspect the VTOL AP, connections, and ESC boards either in the field or request to have them sent back here for inspection and test. 
@Daniel Lloyd is the front right ESC in tact? Which of the options above do you recommend?

### Cameron Chapman, 2023-07-19

@David Grosher @John Clark should the vehicle have attempted to resume fix wing flight when data indicated that the lift motors were not operating correctly? Did it attempt to revert to FW flight? If not, should we open a corrective action for this improvement?
@Daniel Lloyd do you know of anything from previous flights that may have damaged the front right ESC/motor?

### John Clark, 2023-07-19

@David Grosher @Greg Fryer Report attached. Apologies for continuing to use Excel. Vehicle 450 incident report.pptx. Greg, I think we should look the aircraft over and try and find out why the motor failed. It would go to review after.

### Daniel Lloyd, 2023-07-19

Aircraft 450 was borrowed from another organization to fill in after the loss of two motors in the tall grass incidents. It’s history is not available and it is unknown if it had any prior rotor impacts.

### Daniel Lloyd, 2023-07-19

The RH forward lift motor and ESC seem pretty intact. That and the CW will be shipping to Edge on Thursday, 20 July.

### Daniel Lloyd, 2023-07-20

Tracking number for the aircraft cases.
587456701998
587456702001

### David Grosher, 2023-07-20

@Cameron Chapman For item 3 in the investigation plan: 
“Should the vehicle have attempted to resume fix wing flight when data indicated that the lift motors were not operating correctly? Did it attempt to revert to FW flight? If not, should we open a corrective action for this improvement? “
There is currently no logic implemented for this. I have added an item to the flight systems backlog. Kurt has also done some prototyping here in the past, but it was not released. The feature was not robust enough using boom currents. The intent is to revisit this when the new ESCs are integrated.

### Cameron Chapman, 2023-07-20

Thanks @David Grosher. Can you please link the item to this issue if a Jira item exists for it?

### Daniel Lloyd, 2023-07-20

Aircraft crash site location. https://goo.gl/maps/ERdXhb9WGnbRhPe87 
I added a picture to show the crash site relative to the programmed PLZ.

### Connor Peebles, 2023-07-20

Roughly plotted the expected power from the booms vs the measured power from the booms. It backs up John Clark’s report. The plane is trying to correct its approach for the entire landing but the motor it needs to do that is not functioning.

[embedded: image-20230720-231442.png]

### Cameron Chapman, 2023-07-24

Shipment delayed. Expected today.

### John Clark, 2023-07-24

@Cameron Chapman do we have an update on shipment? Who is doing triage?

### Cameron Chapman, 2023-07-24

@Connor Peebles mentioned that @Sean Odell was performing a receiving inspection of the parts. @Sean Odell are these parts ready for us to troubleshoot tomorrow?

### Connor Peebles, 2023-07-25

@Cameron Chapman @John Clark I received them and am investigating

### Connor Peebles, 2023-07-25

Inspect the VTOL AP, connections, and ESC boards. Aircraft arrived in SLO 7/24.
- Inspect AP for damage. Centerwing was spares CW SN 4008
- Perform input resistance, and PWM channels compare to normal.
- Scratch on Red AP Interface board, not serious. Centerwing tested and performs normally. Input resistance nominal.
- Open ESC lid, inspect for damage/burning smell.
- Perform input resistance, motor resistance, etc. measurement and compare to normal.
- Input resistance= 1.2MOhms, nominal is ~200KOhms → this suggest an open or break in circuit. PMW channels are normal.
- Inspect all hardware, connections
- Surviving Lift ESC Assy (Front Right) 107-101631-2 SN 069
- Mosfet Q20 found completely detached, R53 nearby also detached, signs of high temperature solder reflow, board damage. C9 and C10 negative leads nearby also had solder reflow which may result in intermittent connection.
- These mosfets are old datecode and their leads have low solderability; if not a ripple current or short problem I suspect a borderline solder joint that melted or broke which lead to overcurrent failure of the mosfet Q20.
- Investigation Photos
- CW-to-Boom Power, Right Side
- Some potting compound inside one of the EC5 connectors, probably not serious but can test impedance. May contribute to ripple current.

[embedded: IMG_0227.jpg]

### Connor Peebles, 2023-07-25

@John Clark Could I ask you or someone you can assign to decipher the flight data logs of AC450 and find the true flight hours of the plane? If this requires pulling the gains from the CW we will do that.
@Ryan Christino I am going to look at the Vehicle Manual but you may know: what is the recommended service interval of the Lift ESC Assy’s (and/or lift booms)? From a conversation it sounds like 150 flight cycles is the service interval but will confirm w/ the manual

### Daniel Lloyd, 2023-07-25

Manual states 150 flight cycle life limit. Records show aircraft had 48 flights.

### Cameron Chapman, 2023-07-25

@Sean Odell do you still record receiving inspections in a RMA ticket, or is that another method? I don’t see one linked.

### John Clark, 2023-07-26

@Connor Peebles if you provide the Avionics Box I can provide the maintenance log flight hrs as recorded. Also, please see @Daniel Lloyd comment below.

### John Clark, 2023-07-26

@Connor Peebles new ppt format 
[embedded: Vehicle Investigation V450.pptx]
for your findings.

### Daniel Lloyd, 2023-07-26

There is no avionics box. 
@John Clark

### John Clark, 2023-07-26

@Daniel Lloyd I’ll look around, but the Gains is where I would normally go to get the Maintenance Log Pages 1-4.

### Daniel Lloyd, 2023-07-26

The avionics box was destroyed in the fire. There are maintenance logs in the AAR gain.apx.txt and flightdataloggcs-6.0.12-0 files
@John Clark

### John Clark, 2023-07-26

@Daniel Lloyd @Connor Peebles from flight data logs.
[embedded: image-20230726-200226.png]

### Cameron Chapman, 2023-07-26

@John Clark do you know what causes the invalid date? Do the logs indicate this motor had 261 flights, or is that an error in the logs?
@Daniel Lloyd , when you said below records show 48 flights for the motor, was that referring to data log on the aircraft, or were the flight counts logged in a separate location?

### John Clark, 2023-07-26

@Cameron Chapman just looking at the Gains themselves, those may not be accurate entries. Not sure.
[embedded: image-20230726-215017.png]

### Daniel Lloyd, 2023-07-26

The T95_V450_230717_144609_flightdataloggcs-6.0.12-0.csv file is a file of all the flights from that GCS. That includes aircraft that are not 450. That file indicated that the aircraft had 48 flights. It is impossible that the aircraft would have 261 flights. This screen capture shows that 438 had the higher number of flights.
[embedded: image-20230726-215659.png]

### Connor Peebles, 2023-07-31

Fixing up some solder joints on the top of the ESC did not fix the dead board, the problem caused by the heat may be on the bottom or internal layers.

The motor phase lead solder joints were in good condition and did not exhibit signs of overheating.
Testing the motor independently was successful. The blade mount is bent and produces a wobble for the whole motor.

[embedded: IMG_E5326.MOV]

### Connor Peebles, 2023-08-01

On the bottom of the ESC, U1 (5V linear regulator) seems to have failed.

[embedded: IMG_0246.jpg]
This would then not power U2 which in turn powers the FET drivers. This would also cause the CPU to not power.

### Connor Peebles, 2023-08-01

Cleaned up some of the solder joints, still not powering up the ESC.
Replacing U1 then allowed normal functionality, despite the still missing MOSFET Q20, R53.

[embedded: IMG_0256.jpg]

### Cameron Chapman, 2023-08-03

@Connor Peebles , thanks for the great work. Can you please add ideas of how to test each of your theories to investigation plan?

### Cameron Chapman, 2023-08-03

Thanks @Connor Peebles reading the comments closer, it seems clear that the failure of u1 would cause the esc to stop working entirely.  So, you can mostly ignore my previous comment and update fields with those findings. Do you think u1 failed due to heat from the soft start fet?

### Connor Peebles, 2023-08-07

@Cameron Chapman The datasheet alludes to destruction from either continuous overcurrent OR continuous operation when in thermal protection shutoff. We will test both.

### Cameron Chapman, 2023-08-24

Linking subtasks to parent.

### Connor Peebles, 2023-11-21

Updated investigation fields with findings. Set VIT2 ticket to review stage, assigning @Cameron Chapman

## Attachments (25)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| IMG_1626[1].MOV | video | 102289 | 2023-07-18 | listed only |
| IMG_1627[1].MOV | video | 132462 | 2023-07-18 | listed only |
| IMG_1628[1].JPG | image | 4387 | 2023-07-18 | listed only |
| IMG_1629[1].JPG | image | 9765 | 2023-07-18 | listed only |
| IMG_1631[1].JPG | image | 2738 | 2023-07-18 | listed only |
| IMG_1632[1].JPG | image | 2762 | 2023-07-18 | listed only |
| IMG_1633[1].JPG | image | 2530 | 2023-07-18 | listed only |
| IMG_1634[1].JPG | image | 2346 | 2023-07-18 | listed only |
| IMG_1636[1].JPG | image | 2529 | 2023-07-18 | listed only |
| IMG_1637[1].JPG | image | 2110 | 2023-07-18 | listed only |
| IMG_1638[1].JPG | image | 2274 | 2023-07-18 | listed only |
| T95_V439_230718_091225_pack.zip | archive | 1901 | 2023-07-19 | listed only |
| T95_V450_230717_144609_pack.zip | archive | 468 | 2023-07-19 | listed only |
| Vehicle%20450%20incident%20report[1].pptx | pptx | 4 | 2023-07-19 | failed: BadZipFile: File is not a zip file |
| image-20230719-183356.png | image | 128 | 2023-07-19 | listed only |
| Capture.JPG | image | 158 | 2023-07-20 | listed only |
| image-20230720-231442.png | image | 100 | 2023-07-20 | listed only |
| IMG_0227.jpg | image | 4876 | 2023-07-25 | listed only |
| [Vehicle Investigation V450.pptx](attachments/15569_Vehicle%20Investigation%20V450.pptx.md) | pptx | 3453 | 2023-07-26 | converted |
| image-20230726-200226.png | image | 35 | 2023-07-26 | listed only |
| image-20230726-215017.png | image | 2 | 2023-07-26 | listed only |
| image-20230726-215659.png | image | 32 | 2023-07-26 | listed only |
| IMG_E5326.MOV | video | 42237 | 2023-07-31 | listed only |
| IMG_0246.jpg | image | 5910 | 2023-08-01 | listed only |
| IMG_0256.jpg | image | 6298 | 2023-08-01 | listed only |
