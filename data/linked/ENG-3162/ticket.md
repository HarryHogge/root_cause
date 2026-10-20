# ENG-3162: VXE490, 491 Oscillation

- **Issue type:** Problem
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2023-02-24
- **Updated:** 2025-06-02
- **Resolved:** 2023-09-06
- **Reporter:** Former user
- **Assignee:** Jack Waeschle
- **Creator:** Former user
- **Labels:** Engineering
- **Links:** relates to ENG-659 (Review center wing harness routing procedures and evaluate if improvements are needed. ); relates to ENG-3021 (V507 Lift ESC fwd fight to VTOL transition anamoly); relates to ENG-3051 (V501 Lift ESC transition startup anomaly investigation); relates to ENG-3056 (V499 Lift ESC transition startup anomaly investigation); relates to VA-389 (Get write up from wing flapping during VTOL prior incidents, review if applicable to TIQ incident VXEP-18); relates to VXEP-18 (TPTR-59 Wing vibrations during VTOL Landings); clones VXEP-154 (VXE-401 - Wing oscillation with antennas attached); relates to XKIT-1143 (Mechanical Support of Wobble Wing Testing)

## Description

During pause and descent, VXEs490 and 491 exhibited vertical flapping of their wings.
This behavior has been observed on:
406 - during a checkout flight(?) on 4/6/23, 1-2 mph wind, already shipped to customer
414 with 306 CW - Small oscillation
490
491 - Consistently exhibits the behavior with crosswind, most prone to oscillate of our assets. Large Oscillation
- Also with CW 4024 - Large oscillation
- Part of specific testing detailed in comments

481 - straight into the wind, 1 out of 3 or 4 flights
507 - Average oscillation

Currently, we suspect lift booms or joiners influence the behavior, but this is an evolving issue and we have not made decisive conclusions yet.
The behavior was observed both with VTOL Firmware 1.44 (previous customer release) and 1.52 (current release).

## Comments (22)

### Former user, 2023-02-24

See attached email from Enoch for photos from VXE 490, 491, 300 Center Wings. Summary below:
Hi guys,
I opened the center panels of 490 and 491. I noticed some differences between the way that their wires were restrained. Both differed in a meaningful way from 300’s center panel. The wire bundle on the RHS (as pictured below) has a section protected by heat shrink that is not wrapped in with the rest of the bundle.
 
- On 491 this section is only zip tied to the SA cam ethernet line.
- On 490, the situation is similar, and the wires running through the HS are pulled tight.
- On 300, the wires are all well constrained.

I don’t think that this is causing all the issues we have seen, but it certainly is not helping. I propose that we refasten the harnesses on 490 and 491 and repeat some flight tests.
 
Let me know your thoughts.
 
Best,
Enoch

### Former user, 2023-02-24

While reviewing the pictures, I also noticed that the cable bundles coming into the bottom of the 491’s AP have significant slack and contact the wall of the center tray. This may also be contributing to the high vibration levels.
This photo compares 300 (left) to 491 (right).
[embedded: image-20230224-234559.png]
490 has a similar issue, but to a lesser degree.
My plan is to resecure the wires on 491 to address both issues that I observed. I’ll leave 490 alone for now. We can fly these on Sunday to see if the vibe levels improve.

### Former user, 2023-02-24

@Cameron Chapman FYI

### Cameron Chapman, 2023-02-27

Created this issue to evaluate routing procedure improvements. https://jenaero.atlassian.net/browse/ENG-659

### Former user, 2023-02-28

I reworked the wiring in 491 on Friday 02-24 (see below for a before and after). 
[embedded: IMG_20230224_162841058.jpg]
[embedded: IMG_20230224_164844158.jpg]
491 was flight tested on Sunday 02-26 after the modifications. The aircraft still exhibited oscillatory behavior on landing. As before, these oscillations are particularly apparent when the aircraft is at hover power.
The mechanical team is continuing with their inspection of aircraft components. I will keep this thread updated with our findings and plan.

### Former user, 2023-02-28

Last Friday, @Jack Waeschle @Gerrit Sperling and I compared individual component dimensions and weights between 376 and 491. The only clear difference we found were wing tip latch hole sizes. 491 has new latches that were designed with slightly larger holes (~.015). All new aircraft have this, so we think that it is unlikely that it is contributing to the oscillatory behavior. 

We observed variations in a few other measurements, but, if I had to guess, these specific measurements have a +/- .005 measurement error biased on how they were taken. We don’t believe that we are going to find any 'smoking gun' here. I recommend pausing this activity for now. It can be revisited with a better measurement set up later on if other investigation paths turn into dead ends. 

@Former user, @Greg Fryer Let me know your thoughts.

### Former user, 2023-02-28

Today we continued mechanical checks of 490 and 491. We focused on assembled wing stiffness.

Supporting the wing at its tips and loading at the center, we obtained the following data:
[embedded: image-20230301-004207.png]
*I added trend lines to data that represented low, medium and high stiffness.

Observations:
- 490 and 491 have virtually the same wing stiffness.
- 490 and 491 have the stiffest wings in our sample.
- 300 has the least stiff wing in our sample.

This stiffness difference could be a result of aircraft wear and use. 300 is one of our oldest and most used VXEs. Aircrafts 407 and 410 vehicles from the RMA area. I do not know their exact history, but I believe they have also seen significant flight time.

This difference could also be due to some physical difference between 490/491 and the other aircraft.

I think this investigation path should continue. I recommend testing more new aircraft that have not shown any oscillatory behavior.

### Former user, 2023-03-02

Flight test and shop measurement data can be found here: Wing oscillations at hover power
Today @Jack Waeschle @Former user and I met to come up with a test plan that we would like to carry out on Friday.
Here is the test matrix that we are proposing:
*All flights, climb to 200ft AGL and abort. Pause for 10s at 25ft AGL when descending.
*During pause, conduct a high-rate capture from VTOL ‘Flight’ web page.
| Test | Fuselage | CW | Lift booms | Joiners | Wing tips | FW AP Firmware | XCOMM Firmware | VTOL Firmware |
| 1 | 491 | 491 | 491 | 491 | 491 | 6.05m | 4.67 | 1.52 |
| 2 | 490 | 490 | 490 | 490 | 490 | 6.05m | 4.67 | 1.52 |
| 3 | 491 | 491 | 491 | 491 | 491 | 6.05m | 4.67 | 1.44 |
| 4 | 490 | 490 | 490 | 490 | 490 | 6.05m | 4.67 | 1.44 |
| 5 | 491 | TBD | TBD | TBD | TBD | 6.05m | 4.67 | 1.52 |
| 6 | 491 | TBD | TBD | 491 | 491 | 6.05m | 4.67 | 1.52 |
| 7 | 491 | TBD | 491 | 491 | 491 | 6.05m | 4.67 | 1.52 |
| 8 | 491 | TBD | 491 | TBD | TBD | 6.05m | 4.67 | 1.52 |
| 9 | 491 | 491 | TBD | TBD | TBD | 6.05m | 4.67 | 1.52 |

We would like to conduct these tests as follows:
[embedded: TestFlow.drawio.png]

### Jack Waeschle, 2023-03-06

On Friday, we attempted to run through our flight test plan, however there was insufficient wind at SMR for either 490 or 491 to exhibit the oscillatory behavior, so testing is postponed until we have more adverse weather.

### Jack Waeschle, 2023-03-09

Considered testing today after the hydrogen flight(s) but weather was forecast to have insufficient wind. Weather dependent, considering testing on Monday, March 13th.

### Jack Waeschle, 2023-03-21

Tentatively planning to run test plan on Thursday afternoon at SMR after SCO flights. Winds are forecast to be 5-15 mph with 20 mph gusts, so hopefully these conditions will induce the oscillation.

### Jack Waeschle, 2023-03-24

The weather yesterday was significantly different than forecast, with WSW winds at 5-6 mph with 8 mph gusts (that's what I measured). I did not complete my test plan, but there were three flights with oscillation in the SCO and RMA flights.
1:21 PM, VXE 491 with Center Wing 4024
- Significant oscillations during pause (see video below).

[embedded: VXE 491 with 4024 center wing.MP4]
- landing with a crosswind
- Flight log data shows a separation of the power of the two front motors during the initial descent of landing, potentially a yaw command trying to fight the weathervane effect from the crosswind. The right motor had higher power than the left while the rear two motors more closely matched each other. See the left side of the image below.

[embedded: Landing Power_Motors_VXE491_Wobble.png]
- At hover, there was power oscillation between the right and left side, with the front and rear motors matching power. See screenshot below.

[embedded: VXE491_Wobble_Detail.PNG]
For context, the very next flight without wing oscillation during landing is shown below. This flight the vehicle weathervaned into the wind, so there was no crosswind.
[embedded: Landing Power_Motors_VXE491_No_Wobble.png]

3:21 PM, VXE 414 / Frankenstein aircraft (414 fuselage, 306 center wing, ??? branch cable)
- Minor oscillation on hover. Noticeable, but not significant enough that we would classify it as a problem.

[embedded: VXE 414 - Minor Oscillation.MP4]

3:51 PM, VXE 507, Flight 1
- Significant oscillation on hover.
- Crosswind from SW while plane landed facing NW.
- Same separation of power signals behavior seen above with VXE 491 with a crosswind.

[embedded: VXE 507 - Oscillation.MP4]

VXE 507, Flight 2 & 3
- No oscillation on either flight
- vehicle weathervaned into the wind, so no crosswind


Going Foward
I plan to measure the stiffness of the VXE 491 wing with Center Wing 4024 on Monday after Final Assembly has finished sealing it.
Previously this oscillatory behavior was only observed in higher winds with aircraft facing straight into the oncoming air, but this was an example of how very moderate crosswinds can also trigger it. This warrants further investigation.

### Jack Waeschle, 2023-03-27

I measured the stiffness of the VXE 491 wingtips + spars + 4024 center wing today that resonated on Thursday during landing, and it is on the stiffer side of the distribution. I also measured the same assembly with 4030 center wing (one that didn’t resonate, however the plane weathervaned into the wind for that landing, so there was no crosswind) and found a similar stiffness.
[embedded: image-20230327-201024.png]

### Jack Waeschle, 2023-04-14

On Thursday morning (4/13), @Ryan Christino and I carried out the testing plan created by Enoch, Will and I a few weeks ago. I still have yet to dive into the sensor data, but broader findings are summarized below.
Wind varied slightly between flights, but generally was 5-7 mph with gusts up to 10 mph from the NNW. The wing oscillations occur when the aircraft is subjected to a crosswind. This was accomplished by launching the aircraft facing East and aborting the flight at around 40 or 50 feet before the aircraft had fully weathervaned into the wind. After pausing, the aircraft would maintain its approximately NE bearing. Potentially these yaw commands are part of the vibration issue, however correlation is not causation.

Flight Summaries
VXE 491 achieved significant oscillations/wobble in our current configuration of software under the conditions outlined above.
We then rolled the VTOL software back to the previous customer release (1.44) and the same oscillations were observed.
After rolling the VTOL software forward to the current version, we swapped the entire wing from 300 (the least stiff we have measured) including using the old spar joiner tubes that have recently been replaced on that aircraft.
300 Wing produced completely smooth hover, suggesting this oscillation is a product of the mechanical properties of our newer wings.
300 Wing with 491 Wing Tips produced very smooth hover.
300 Center Wing with 491 Wing Tips, Joiners & Lift Booms produced moderate wobble.
We repeated this flight and observed moderate/high wobble.
300 Center Wing and Joiners with 491 Wing Tips & Lift Booms produced moderate/low wobble.
491 Wing with 300 Lift Booms produced low wobble.
300 Wing with 491 Lift Booms produced medium/low wobble.

Takeaways
This testing was very useful to getting a better understanding of this phenomenon. I believe the Lift Booms are a major contributor, but this is a more complex issue than a single component, as the last two tests show. This appears to be a mechanical issue, as rolling the software back produced no observable change. However, I suspect the yaw control of the aircraft also plays a role.

Actions
Next week I plan to dive into the sensor data and look for variation between the smooth flight with the 300 Wing assembly and those that produced wobble. Ryan took two bursts of high frequency data for most or all flights, so there should be lots of valuable lessons to learn there.
Additionally, I plan to inspect the lift booms and joiners from 300 to compare to the measurements I have from 491.
I will update this ticket with my findings.

### Cody Smisek, 2023-04-19

Attaching video from 481. Sorry, taken from 50-100ft away.

### Jack Waeschle, 2023-05-03

Measured components on VXE 300 today with @Gerrit Sperling. Comparing to VXE 491, the most significant differences are the weights of the wingtips. VXE 300’s wingtips are 35.5 and 11 grams lighter, respectively, than VXE 491’s. Additionally, the spar joiner tubes are about a gram lighter, and 14 thou shorter in cross sectional height. This has already been corrected for VXE 300 by replacing the spar joiner tubes, but for my testing I intentionally used the older ones. The lighter wingtips appear to have a negligible effect on the oscillatory behavior.
In short, this dimensional inspection failed to find any smoking guns. Detailed numbers from this inspection can be found in Condor → Engineering → 900 → Old Users → Enoch → Flight Test → 20230222_491&376 Flight Test - Investigating continued oscillations → Dimensional checks & wiring inspection

### Jack Waeschle, 2023-09-06

[embedded: Wing Vibration Report.docx]
As part of https://jenaero.atlassian.net/browse/VA-389 I created a report mostly summarizing this ticket. It contains recommendations for future investigation. If these are prioritized in future sprints, the issue will be tracked in relevant tickets within the VA board.
Closing this ticket for now.

### Jack Waeschle, 2023-09-07

Wing Vibration Report.docx
^ Link to sharepoint location

### Greg Fryer, 2023-09-27

This has been noticed during TIQUILA FAT, but since determined to not be a flight/safety risk moving this from Monitor to Done.

### David Grosher, 2023-10-18

Note: Jack and Ryan’s study included burst data collected at 100Hz. This data shows a resonance mode between 7.9 - 8.7 Hz across the dataset.  This will result in an aliased mode in the ~10Hz data that is between 1.3 and 2 Hz, which is what we observe in the data from v401.

### Jack Waeschle, 2023-10-23

[embedded: image-20231023-224617.png]
The graph above shows 1 second of wobble for vehicle 491

Motor 1 is front left                     Motor 2 is front right


Motor 3 is back left                     Motor 4 is back right

The power is oscillating between the right and left sides of the vehicle at a frequency of ~8.7 Hz. To me this indicates an issue with gains resulting in an underdamped system.
For reference, here is burst data from the flight just before where VXE491 faced into the wind and did not wobble.
[embedded: image-20231023-230220.png]
Without wobble, there is no separation in power between the right and left sides. The amplitude of power commands is greatly reduced, and the frequency increased.
@Everett Werner @Ryan Christino @David Grosher

### David Grosher, 2023-10-24

@Jack Waeschle @Ryan Christino I plotted the PSD of the Gyro roll rate and saw a mode at 7.9-8.7Hz across all of the datasets that Jack provided me. The mode is there in all datasets including ones marked as “no wobble”. The power in the mode generally increased as frequency increased and the wobble became visible (per the test notes) as the frequency increased past 8.3-8.4 Hz.  We would need to ensure attenuation across a range from ~8.2 - 9 Hz to ensure we address variability in the manufacturing process (it would be great to validate that range with more data and/or mechanical analysis).

## Attachments (19)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [Center panel wiring differences.msg](attachments/12859_Center%20panel%20wiring%20differences.msg.md) | msg | 2694 | 2023-02-24 | converted |
| image-20230224-234559.png | image | 3976 | 2023-02-24 | listed only |
| IMG_20230224_162841058.jpg | image | 2333 | 2023-02-28 | listed only |
| IMG_20230224_164844158.jpg | image | 1854 | 2023-02-28 | listed only |
| image-20230301-004207.png | image | 38 | 2023-02-28 | listed only |
| TestFlow.drawio.png | image | 60 | 2023-03-02 | listed only |
| Landing Power_Motors_VXE491_No_Wobble.png | image | 306 | 2023-03-24 | listed only |
| Landing Power_Motors_VXE491_Wobble.png | image | 340 | 2023-03-24 | listed only |
| VXE 414 - Minor Oscillation.MP4 | video | 879498 | 2023-03-24 | listed only |
| VXE 491 with 4024 center wing.MP4 | video | 541798 | 2023-03-24 | listed only |
| VXE 507 - Oscillation.MP4 | video | 656083 | 2023-03-24 | listed only |
| VXE491_Wobble_Detail.PNG | image | 227 | 2023-03-24 | listed only |
| image-20230327-201024.png | image | 66 | 2023-03-27 | listed only |
| Vibration Investigation Burst Data Flights 4-13.zip | archive | 1002 | 2023-04-17 | listed only |
| VXE481_20230414.mp4 | video | 31819 | 2023-04-19 | listed only |
| image-20230906-000912.png | image | 316 | 2023-09-05 | listed only |
| [Wing Vibration Report.docx](attachments/16141_Wing%20Vibration%20Report.docx.md) | docx | 1190 | 2023-09-06 | converted |
| image-20231023-224617.png | image | 360 | 2023-10-23 | listed only |
| image-20231023-230220.png | image | 227 | 2023-10-23 | listed only |
