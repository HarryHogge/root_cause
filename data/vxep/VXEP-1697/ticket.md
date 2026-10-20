# VXEP-1697: Repair Avionics Box on AC 945 - PPS2

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2026-02-07
- **Updated:** 2026-02-25
- **Resolved:** 2026-02-25
- **Reporter:** Samuel Lopez
- **Assignee:** Samuel Lopez
- **Creator:** Samuel Lopez
- **Problem Type:** Discovered Issue

## Plan

- PPS2 from GNSS to Novatel observed is not pulsing correctly.
- Open Avionics Box and test continuity from one end of V2 harness 2121781-01 to the other.
- Replace harness.
- Re-assemble avionics box
- Note all observations

## Comments (8)

### Samuel Lopez, 2026-02-07

10:00 am
- Abnormality #1.  A lot of FOD in the avionics box.  Loctite flakes and a loose plastic washer.
- Abnormality #2.  The Novatel-GNSS board stack is loose.  Freely wiggles.  A standoff  was broken.
- Normal.  Continuity of PPS2 from GNSS to MCMC measures normally.
- Abnormality #3.  We did not expect to see that the both the PPS1 and PPS2 signals are inverted.  They measure pk to pk from 0 to negative 3v3.
- Abnormality #4.  And that the PPS2 line has a DC offset.  So that one actually measures from -1.8V with the pulses at -3.3V.
- Abnormality #5.  There is a 3.3V DC voltage between MCM ground and Novatel/GNSS ground.

1:00pm
Current harness 2121520 is monochromatic (all white colors) making it very likely that a voltage line or twisted pair was swapped.  Replacing harness 2121520-01.

### Samuel Lopez, 2026-02-07

PPS1 measures as expected, pulses from 0V to 3.3V.
PPS2 does not measure as expected.  Peak to peak voltage should be 0 to 3.3V with 1 hz spikes (active low).  Instead, the peak to peak voltage measures 0 to 1.8 V, though the frequency is correct at 1 hz.

[embedded image-20260209-180651.png]

### Samuel Lopez, 2026-02-09

PPS2 continues to measures 1.8V peak to peak even when harnesses are changed and when GNSS is disconnected from MCM board.  GNSS board was replaced with a fresh board off the line (Novatel board remained so).  After this, the PPS2 measured normally at 0 to 3.3V peak to peak.

### Samuel Lopez, 2026-02-09

Avionics Box for AC 945 is being re-assembled by Robbie Clemens.  The box will then go through standard electronic checkouts and will be installed in AC 945 to confirm that the PPS2 line is behaving normally.

### Samuel Lopez, 2026-02-11

Monday 2026-02-09
The av box was re-assembled.  Although the EventOut2 line now outputs the correct pulse at normal voltage.

### Samuel Lopez, 2026-02-11

Monday February 9.

Discovered that the MCM GPIO 12 line was behaving erratically when Ryan Smith sends a pulse signal to it.  There is a DC offset between 0 and Vcc and the pulse is having trouble reaching Vcc as shown below.  After a time, the gpio pin stopped working altogether, probing it reveals only ground noise.  

[embedded image-20260211-194124.png]

### Samuel Lopez, 2026-02-11

Tuesday, February 10
The protection diode between the gpio and GND was found to be open.  Bethany Ponce replaced the Hadrion carrier board on the MCM board stack after which the gpio pin acted normally.

### Samuel Lopez, 2026-02-11

Wednesday, 2026-02-11
With the fresh Hadron board, the MCM_GPIO_12 pin is exhibiting the same behavior as before.  It has a DC offset when pulsing as shown below.  Investigating is ongoing.
[embedded image-20260211-200215.png]

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20260209-180651.png | image | 176 | 2026-02-09 | listed only |
| image-20260211-194124.png | image | 43 | 2026-02-11 | listed only |
| image-20260211-200215.png | image | 264 | 2026-02-11 | listed only |
