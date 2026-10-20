# FS2-1050: Mitigate Structural Resonance (~8.4Hz) during VTOL Flight

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2023-10-20
- **Updated:** 2024-04-04
- **Resolved:** 2024-04-04
- **Reporter:** David Grosher
- **Assignee:** Alex Bogdanov
- **Creator:** David Grosher
- **Parent:** FS2-752 Vehicle Incident Investigation Support
- **Links:** blocks VXEP-154 (VXE-401 - Wing oscillation with antennas attached)
- **Epic Link:** FS2-752

## Description

- Work with the Mechanical team to validate that there is an expected structural mode at or near 8.4Hz.
- Perform similar mechanical analyses for x-kit with various different load configurations. Small/Large Tanks, munitions, small/large payloads, battery/fuel cell config.
- Determine ideal mounting locations of IMUs based on the order of the structural modes.
- Close the loop of the current Simulink model MC controller and 6DOF, produce bode plots of the current system, insert noise into the roll rate measurement that has a PSD approximated by the high frequency burst data previously collected (may need to put noise on Axyz and Gxyz, note Gx (roll rate) is dominant). Verify that an oscillation is present in the simulation.   Develop a notch filter to mitigate the oscillation
- Verify Notch filter works for all X-kit mass/inertia configurations in Simulink.
- Work with SW to implement the notch filter.

## Sprint

FS2 Sprint 11, FS2 Sprint 8, FS2 Sprint 10, FS2 Sprint 13, FS2 Sprint 16, FS2 Sprint 9, FS2 Sprint 14, FS2 Sprint 12, FS2 Sprint 15

## Comments (17)

### David Grosher, 2023-10-20

FYI, @Former user @Everett Werner

### Greg Fryer, 2023-11-15

@Ryan Christino I think I am going to get asked (based on customers seeing it) for how long we think the plan is to get this into the SW. (through full test and everything)
Can you start putting a status report in here, and an outline of a plan if it differs from the description? Just once or twice a sprint, not more than 5 minutes of time.
@David Grosher @Former user @Everett Werner FYI.

### David Grosher, 2023-11-15

@Greg Fryer Based purely on release schedules, the earliest would be a Q1 release probably slated for mid April.

### David Grosher, 2023-11-21

@Ryan Christino @Former user PSD from BURST007 (491 Wobble Crosswind Old Firmware).csv. This is data from the flight tests that Ryan and Jack performed. 
[embedded: image-20231121-184746.png]
8
| Frequency | Dataset | Max dB/Hz | Wobble observed |
| 8.1 Hz | 003 | 1 | No |
| 8.6 Hz | 004 | 27 | Yes |
| 8.4 Hz | 005 | 27 | Yes |
| 8.4 Hz | 007 | 23 | Yes |
| 8.5 Hz | 008 | 14.7 | Yes |
| 7.9 Hz | 009 | 7 | No |
| 7.9 Hz | 010 | 3 | No |
| 8.7 Hz | 011 | 12.3 | Yes |

### David Grosher, 2023-12-12

@Alex Bogdanov FYI

### Matt Philley, 2023-12-26

@David Grosher @Alex Bogdanov looks like yall have the ball on this one. We are seeing this regularly on Production Aircraft going through Test Flights now. We will continue to generate an NCR each AC for tracking purposes and Greg & Jack have been dispo-ing Use-As-Is.
Do you folks see any value in us reporting these occurrences to you or attaching that info to this Jira ticket or do you have all the data you need already?

### David Grosher, 2023-12-26

@Matt Philley My understanding is that the flight test team was collecting high frequency burst data on each SCO.  If we could get a link to that data it would be appreciated. We are trying to characterize the behavior across the fleet so that the solution is robust.

### Matt Philley, 2023-12-26

@Artis Bertulis can you provide that info for Dave?

### Artis Bertulis, 2023-12-26

@David Grosher @Matt Philley we keep the burst data together with the AARs on the Condor at “\\condor\Flight Ops\Flight test data\2023”. For SCO we typically do 3 flights, and we use landing Pause/Nudge on the 3rd flight, that’s when we usually observe the wobble. The 3rd landing is also when we do the burst, so you’ll see 3 AARs and 1 burst file (see below).
[embedded: image-20231226-162250.png]
If for some reason you do not have access to that folder in Condor - let me know

### Matt Philley, 2024-01-03

Occurrence on AC 592 - Use as is
AC 592 - Flight test - Wingtip wobble

### Matt Philley, 2024-01-16

Occurrence on AC 595
AC 595 - Flight Test - Wingtip wobble

### Matt Philley, 2024-01-17

Occurrence on AC 599
AC 599 - Flight Test - Wingip Wobble

### Matt Philley, 2024-01-18

Occurrence on AC 492 (RMA but total vehicle replacement) & AC 598
AC 492 - Flight Test - Wingip Wobble
AC 598 - Flight Test - Wingip Wobble

### Matt Philley, 2024-02-13

Occurrence on ASSET AC 499
AC 499 - Flight Test -Wingtip Wobble

### Matt Philley, 2024-02-14

Occurrence on AC612
AC 612 - Flight Test - Wingtip Wobble

### Matt Philley, 2024-02-19

Occurrence on AC 606
AC 606 - Flight Test - Wingtip Wobble

### Matt Philley, 2024-03-14

Occurrence on AC 629
AC 629 - Flight Test - Wingtip Wobble

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20231121-184746.png | image | 94 | 2023-11-21 | listed only |
| image-20231226-162250.png | image | 38 | 2023-12-26 | listed only |
