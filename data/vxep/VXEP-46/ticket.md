# VXEP-46: VXE-444 Crash in Landing Pattern-XCOM PCB issue

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-08-31
- **Updated:** 2026-01-15
- **Resolved:** 2025-05-28
- **Reporter:** Pat Wells
- **Assignee:** Cameron Chapman
- **Creator:** Pat Wells
- **Labels:** MARSOC, Weekly-incident-tracker
- **Links:** relates to ENG-2992 (VXE 444 Crash in Landing Pattern); relates to VA-268 (VXE 444 Hands on troubleshooting. Identify cause and corrective actions.)
- **Customer:** MARSOC
- **Vehicle Tail Number:** 444
- **Root Cause:** - Capacitor C20 failed which caused the Fixed Wing Autopilot processor to lose power.
- **Incident Type:** Aircraft Loss
- **Severity:** 1 - Flight Critical

## Description

VXE444 crashed while transitioning from IP2 to IP4 in the landing pattern. Today for a test flight after installing 6.0.12 and performing all applicable SBs, AC444 went up for approx 25 minutes before we returned to land. We used a straight in approach based on terrain and other constraints. We departed a nearby orbit at 400 ft agl to enter our 400 ft land primary land plan. To avoid the IP2 orbit  based on a nearby radio tower, we commanded straight to IP4.
 
The gcs software still highlighted the IP2 orbit and started a left turn in which it lost altitude, quickly followed by a steep climb resulting in a possible stall and rolling off to the right into a steep dive that it didn't recover from. With so little altitude to work with, there wasn't time to complete command to Orbit 2 to see if a correction could be made. Aircraft is a near complete loss.

## Corrective Action

- Unified Autopilot Project
- Potentially update; single point failure SMT component, backup component

## Plan

- Update investigation summary ppt and review with Cameron.
- Check FDR for retract command sent.
Try to replicate issue with actual retract mechanism.
Try to replicate IP skip pattern in HIL. Retract hooked up.
- Make a case for Permanent Magnetic Shaker, PCB vibration testing, demonstrate SMT ceramic capacitor failure using tuned vibration.
- Look for current spike on Iretract to replicate issue seen on logs (C20 is drained to shut off 5V rail). 
- Run with similar processing demand than flight, monitor for an extended duration to see if an overcurrent or regulator failure happens. Suspect there is an inrush current associated with retract payload that is messing with the 5V rail on the AP.
- Not seeing Iretract current spike when manually replicating issue on other boards, swap around 444’s XCOMM and AP to narrow down which board is causing this current spike in Iretract.

## Issue Status

Updated 5/23: Detailed status here VIT2-252_ VXE444 Crash In Landing Pattern, Investigation Details.docx. Separate these into tasks….
- Replaced faulty C20, which allowed regulator to supply the 5V rail again. Can now connect to 444 w/out manually powering 5V rail.
- need to find source of overcurrent, suspect payload retract overcurrent. Try to replicate on HIL
- XCOMM seems to function normal.
- Could trace path of overcurrent through XCOMM, look for any other affected components
- LED D8 is broken on the FW AP and the 5V trace side is charred.
- Probably just got past production or moved along and ignored. Don’t think the LEDs should affect the circuit whether working or not.
- Review 12V current flight log to see if any signs of 5V overcurrent (5V regulator is powered by 12V regulator).
- 12V current looks normal entire time

## Comments (0)

## Attachments (0)
