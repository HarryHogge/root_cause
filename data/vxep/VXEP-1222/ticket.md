# VXEP-1222: VXE 826 Crash

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** High
- **Created:** 2025-04-22
- **Updated:** 2026-03-02
- **Resolved:** 2025-06-24
- **Reporter:** Cameron Chapman
- **Assignee:** David Grosher
- **Creator:** Cameron Chapman
- **Labels:** Investigation-Priority
- **Links:** relates to RMA-813 (VXE-826 RMA 250924-1 )
- **Issue Status:** Investigation being tracked here. We can use this for tracking 826 repair?
- **Severity:** 1 - Flight Critical

## Description

Files (AAR and Photos): VXE 826 Crash 4-22-25
Investigation Summary Link: VXE 826 - Crash - Investigation Summary.pptx
NCR: AC 826 - Flight Test - Rapid disassembly
Aircraft Configuration Info:
- Catalog: 500-2121509-03, Stalker Block 35X
- This flight had E140 SN 6096 (regulator style gimbal harness similar to 2123104-01)
- Trellesware pylon SN 002, flown from
- OGCS 1.2.0.2 on standard laptop
- AC was flying 6.4 FW

## Plan

Cam-I recommend starting investigation summary and incident first, to start collecting what we know, plan going forward, etc
Scott Discussed with Ryan B about the plan forward (any input is welcome)
- Build up v826 and power up. @Connor Peebles to provide EE dispo, @Scott Stuckey for mechanical. 
- Check harnesses
- Check to see if trellusware is affecting power
- pull any additional logs
- Take out Avionics 
- inspect avionics power to 7700
- inspect 7700

## Comments (5)

### Cameron Chapman, 2025-04-22

it turned on vtol as normal, then it pegged the velocity commands to try to get to the landing zone position (position and velocity correctly didn't try to use the frozen gps position, but the estimates drift quickly when GPS drops out)
 
I ensured 826 was safe to power up. We are getting some serial traffic to and fro the OEM7700

 
but cannot SSH into it
 
based on the below first reported oem timeout the last heartbeat received before the timeout started was XComm CPU Time ~7,164.967. That's when whatever happened happened.

 
Very slight uptick in current on 12V at 7167 Actually I think this is just noise.

Zoomed out on the x-axis a bit.

 

 
 
we don't have in-air re-init...
 
After plugging in the CW, the 7700 seems to finish initializing. I can SSH into it and get more serial traffic

and access NAS

(not under a repeater)
 
Eric Brewer
📷

Doesn't look like it with the current firmware.
 
I'm going to leave it alone now and let software decide if they need anymore logs (maybe from the 7700 itself maybe).
It is at my bench.
 
Connor Peebles
I'm going to leave it alone now and let software decide if they need anymore logs (maybe from the 7700 itself maybe).  It is at my bench.

Do you know how to pull logs from the OEM? 
 
i don't know that it stores any through a power cycle, but we can check/ask
 
At the very least we could let it run for a while, pull an AAR, and check the serial data rate/event logs for dropouts.
 
Have we ever seen a OEM7700 reset on it's own before?
 
it's 60C (140 F), does that seem right? were the avionics hot?
 
Jason Scherer
Have we ever seen a OEM7700 reset on it's own before?

i have not.
 
I'll email novatel to see what logs we might be able to get after the fact 
 
Eric Brewer
it's 60C (140 F), does that seem right? were the avionics hot?

The spec shows it rated to 85C
 
Eric Brewer
it's 60C (140 F), does that seem right? were the avionics hot?

That sadly is not very hot for our electronics
 
Jason Scherer
The spec shows it rated to 85C

yea - was just wondering if maybe it was hotter out on the flight line and overheated (just seemed hotter than i thought it would sitting in the lab...)
 
Discuss with Ryan B about the plan forward (any input is welcome)
- Build up v826 and power up 
- Check harnesses
- Check to see if trellusware is affecting power
- pull any additional logs
- Take out Avionics 
- inspect avionics power to 7700
- inspect 7700

 
Scott Whitney
Discuss with Ryan B about the plan forward (any input is welcome)    Build up v826 and power up    Check harnessesCheck to see if trellusware is affecting powerpull any additional logs  Take out Avionics    inspect avionics power to 7700inspect 7700

See if we can pull any residual logs from OEM. Eric has an email to Novatel. 
 
<sadness>...

 
Scott Whitney
Discuss with Ryan B about the plan forward (any input is welcome)    Build up v826 and power up    Check harnessesCheck to see if trellusware is affecting powerpull any additional logs  Take out Avionics    inspect avionics power to 7700inspect 7700

I think it is a good time to start recording info in an incident and ppt. Ex: operator statement. important plots, timeline, etc

### Ruysser Gabler, 2025-04-22

Operator statement: 
AC 826 had an incident today in completing flight number 3. 
This flight had E140 SN 6096, Trellesware pylon SN 002, flown from OGCS 1.2.0.2 on standard laptop 
AC was flying 6.4 FW
Weather 3mph from S 53 deg F
AC has flown 3 flights already for SCO check out, this flight was for Trellesware checkout with E140 to complete flight 3. 
Summary of crash: Had some Trellesware issues before flight with networking, AC was on for a good bit of time before launch. Completed LW and launched normally. Flew 2-3 orbits then sent to PLZ (PLZ was placed at standard location and direction). AC tracked PLZ normally until final. On final the AC turned just next to IP5 may have been shortly before or after. GCS stopped AV trail at that point. AC turned right and said it was in transition for landing even though VTOL was not on. AC did tight right turn and VTOL came on, continued to descend while front motor seemed to be on and VTOL on at same time. User activated landing control position and attempted to nudge from buildings also attempting pause. AC lost connection to GCS and rapidly disabled upon touch down.

### David Grosher, 2025-05-19

This incident was on non-released hardware and non-released software it should be part of the VXEP project. 

There is still an ongoing hardware investigation. Software/Firemware has been released to catch this issue, warn the operator and facilitate safe recovery of the aircraft. Note: new procedures are associated with this delivery.

### Scott Whitney, 2025-05-20

Production Requests for Mechanical Replacements:
- qty 2) Wing Tip Clip: 107-100454 (link)
- (qty 2) Joiner Tubes: 107-101454 (link)
- (qty 1) Elevator Carrier: 107-102042 (link)
- (qty 1) Lift Boom: 107-100431-L/R (link)

### David Grosher, 2025-06-24

Issue is not with released hardware/software.

## Attachments (0)
