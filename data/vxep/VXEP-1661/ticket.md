# VXEP-1661: VXE 674 (HSV FLOPS) Will Not Connect in VXE SUAV

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** High
- **Created:** 2026-01-08
- **Updated:** 2026-10-07
- **Resolved:** 2026-10-07
- **Reporter:** Anthony Hansen
- **Assignee:** Jackson Riley Curvin
- **Creator:** Anthony Hansen
- **Links:** relates to FS2-2616 (Climb abort FC fault but AC did not abort take off); relates to RMA-883 (VXE-674 RMA 260127-2)
- **Issue color:** purple
- **Vehicle Tail Number:** 674
- **Severity:** 1 - Flight Critical
- **Impacted Core Subsystems:** Aircraft, Payloads

## Description

We did a flight that lasted just over an hour with the aircraft (non-Advanced Navigation, E140 LWIR and Fuel Cell). We landed the plane and left the fuel cell on. We cut power to both aux ports, removed the E140 LWIR gimbal, and plugged in the E140 MWIR. Applied power again to both AUX ports and the gimbal powered up (it did sound like some power was going to the MWIR, although it did not perform a BIT). Going through the launch wizard again, the aircraft was resetting the autopilots. It froze on the VTOL AP reset and didn’t count down anymore for at least 5 minutes. We cancelled the Launch Wizard and at some point, we lost connection to the aircraft. We could not connect to the aircraft in the software again. We can see some data populating in the software when it attempts to connect in VXE SUAV.
We have tried to power cycle the plane multiple times, tried 2 different laptops (both RJ45 ports) and also used the top AUX cable to hardwire to the plane. 
The VXE SUAV has the error “Failed to Connect with Vehicle”. When attempting to connect to the vehicle again, you will get the error “Vehicle #674 is already connected to another GCS”.
I have attached some photos from the GCS as well as the previous flight’s AAR.

## Vehicle Configuration

Non-Advanced Navigation
Fuel Cell
VXE SUAV
E140 LWIR and E140 MWIR

## Plan

- @Anthony Hansen can you please report the PN and SN of the gimbals and interface harnesses involved(good practice for any issue)?
- @Scott Whitney is anyone available to review these logs?
- @Samuel Lopez can you please inspect and see if you can power up and connect with a power supply? (start with input resistance check before power).

## Issue Status

VXEP-1661 VXE674 AP GCS No comms - Data location here
Several issues within this incident
- Inability to communicate with AP via Legacy GCS after when MWIR powered on
- Previous flight AAR shows,
- Fuel cell under performing (<400W and stack voltage 20v) - Suspected stack failure
- A launch abort message during launch, but no actual abort occurred (needs code review to understand how/why) 
- xcfc shows drop to 0 during launch, likely causing the abort message. Appears to be ‘normal’ for fuel cell flights (reviewed flights from 2023), cause unknown.
- Linked previous report of this issue, known issue in xcomm. Unresolved.
- In event inability to communicate with AP while on ground, how should an operator power down a fuel cell?

## Comments (23)

### Cody Smisek, 2026-01-08

@Anthony Hansen @Sean Wendling Can you confirm that this is or isn’t an acceptable practice?

### Sean Wendling, 2026-01-08

@Cody Smisek @Anthony Hansen Fuel Cell needs the HLB to function properly. Disconnecting the HLB from the aircraft should only be done when the fuel cell is off. If it is done when the fuel cell is on, the fuel cell cannot function regardless of the connection of propane and will not cooldown properly.
For future reference this is not an acceptable practice. You can disconnect the center wing connection to the HLB, but not the Fuselage connection. I don’t know whether this contributed directly to the VTOL AP freezing, but disconnecting the HLB from the aircraft would be a full aircraft power cycle as the fuel cell would not really be producing power by itself.

### Anthony Hansen, 2026-01-08

@Sean Wendling We surely do not make it a normal practice to disconnect the main power on the HLB to shut down the fuel cell. We couldn't connect to the aircraft in VXE SUAV to properly shut down the fuel cell. The fuel cell continued to run for 30-45 minutes as we were attempting different ways to connect to the plane again in the software. It was obvious to us that it was not shutting down on its own as the exhaust was still really hot. We ran out of options to turn off the fuel cell and we ended up having to pull main power and the propane line. 
As likely a separate issue, over the course of the flight (just over an hour), the fuel cell never produced more than 370 watts or so. The fuel flow was pegged at 196 g/hr as well. There was no wind during the flight. To be fair, after all the flight operations were complete, we tested the regulator. It showed around 9.5 psi. So that might have been the fuel cell issue.

### Jackson Riley Curvin, 2026-01-08

@Cody Smisek  this all of the test ive have conducted today 
- took 674 AV box and installed on Iron Bird still did not work
- installed Iron Bird AV box in 674 fuselage it worked
- opened XCOMM throughput on 674 av box, SN populated but no build info. can bus traffic is zero because I did not have center wing connected.
[embedded Image (20).jpg]
- installed 674 AV box back into its fuselage, and fully assembled the Aircraft, when power was applied the servos jumped to home then immediately lost power and would not respond when rolling the aircraft left or right.
- Went to the Hardware page in the XCOMM and checked the servo power and they were off, so I clicked Override on and turned them on, and the servos responded when I rolled the aircraft left and right. I then turned Override off, and the servo power turned off.
[embedded Image (21).jpg]
- I also replaced the SD card and reformatted it, cycled power with the same results.
- I checked the smart Battery Status as well as Remote Air Data pages as well see pictures below.
[embedded Image (23).jpg]

[embedded Image (24).jpg]

### Cody Smisek, 2026-01-08

@Jackson Riley Curvin Did you pull xcomm logs prior to replacing SD card?

### Cody Smisek, 2026-01-08

@Jackson Riley Curvin regardless, i think it’s reasonable to suspect FWAP is not going to be fixable. I think bad mag boards have led to similar issues. 
Would recommend return avionics (at minimum) to SLO. 
Probably also hold off on using the MWIR until we figure out root cause or have at least a better idea of what’s going on. 
logs from the SD card removed would be useful. Do not connect SD to another AP, whole encryption deal occurs.

### Anthony Hansen, 2026-01-14

@Auston Terry

### Auston Terry, 2026-01-14

@Cody Smisek  are you receiving the Avionics in SLO? I’ll set up the shipping tomorrow.

### Cody Smisek, 2026-01-14

@Auston Terry Should be sent to SLO RMA and distributed from there.

### Lauren Velasquez, 2026-01-27

@Ronnie Baker Please deliver A674 to @Cody Smisek

### Lauren Velasquez, 2026-01-28

@Cody Smisek please confirm you received this.

### Cody Smisek, 2026-01-28

@Lauren Velasquez I have not

### Lauren Velasquez, 2026-01-28

@Cody Smisek @Ronnie Baker Can you please hand deliver this to Cody.

### Cody Smisek, 2026-01-28

@Lauren Velasquez unlikely that I will be the one working this incident. Can be dropped off in engineering area and we will get someone assigned.

### Lauren Velasquez, 2026-01-28

@Cameron Chapman  Where would you like this to be Dropped off? I would like to avoid losing track of anything.

### Cameron Chapman, 2026-01-28

@Lauren Velasquez Please coordinate with @Samuel Lopez. What is the status of the investigation equipment tracking process? Can you point to that? We can review to see if steps should be added to ensure engineering keeps track of things in the same system.

### Lauren Velasquez, 2026-02-04

@Samuel Lopez  This Avionics and Mag mount antenna (96x-3-14-1019) are in the RMA area

### Ronnie Baker, 2026-02-17

@Samuel Lopez Let me know when you are available to pick this up.

### Samuel Lopez, 2026-04-06

First Observations
- The XCOMM webpage loads just fine.
- However, the instrument panel does not display the voltages and other measurements.
- Opening the XCOMM log file, it’s the fixed wing autopilot that’s not displaying appropriate measurements  as shown below.
- Servos do not react to movement in the av box.
- Highly suspect fixed wing autopilot of failure
- Next step is to open AV box and inspect fixed wing ap.  If nothing can be found wrong, replace Fixed Wing AP.

### Stephan Johnson, 2026-10-07

FWAP replaced

### Ronnie Baker, 2026-02-17

@Samuel Lopez Let me know when you are available to pick this up.

### Samuel Lopez, 2026-04-06

First Observations
- The XCOMM webpage loads just fine.
- However, the instrument panel does not display the voltages and other measurements.
- Opening the XCOMM log file, it’s the fixed wing autopilot that’s not displaying appropriate measurements  as shown below.
- Servos do not react to movement in the av box.
- Highly suspect fixed wing autopilot of failure
- Next step is to open AV box and inspect fixed wing ap.  If nothing can be found wrong, replace Fixed Wing AP.

### Stephan Johnson, 2026-10-07

FWAP replaced

## Attachments (7)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| Already Connected.png | image | 157 | 2026-01-08 | listed only |
| Error.png | image | 93 | 2026-01-08 | listed only |
| Image (20).jpg | image | 1539 | 2026-01-08 | listed only |
| Image (21).jpg | image | 1494 | 2026-01-08 | listed only |
| Image (23).jpg | image | 1715 | 2026-01-08 | listed only |
| Image (24).jpg | image | 116 | 2026-01-08 | listed only |
| T95_V674_260107_094424_pack.zip | archive | 2891 | 2026-01-08 | listed only |
