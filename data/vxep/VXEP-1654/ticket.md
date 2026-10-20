# VXEP-1654: VXE-799 aileron servo locked

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2025-12-22
- **Updated:** 2026-10-09
- **Resolved:** 2026-08-07
- **Reporter:** Michael Mohr
- **Assignee:** Samuel Lopez
- **Creator:** Michael Mohr
- **Labels:** GS_Closed, PMA263, RCCA, Software, Weekly-incident-tracker
- **Links:** relates to RMA-873 (A799 RMA 260105-1); relates to XKIT-5360 (B40 913 Crash (2026/03/04))
- **Issue color:** teal
- **Customer:** PMA263
- **Vehicle Tail Number:** 799
- **Corrective Action:** Replaced Fixed Wing AP on Avionics box with firmware version 6.50s
- **Root Cause:** Non-responsiveness of Left Servo has been traced to microcontroller of Fixed Wing AP not outputting a PWM signal.
- **Incident Type:** Squawk
- **Severity:** 2 - Degraded Performance - No Workaround
- **Applicable Subsystem:** Avionics and Flight Controls

## Description

From customer:
“I have what I believe to be an Avionics issue that is causing the left aileron to lock in a position below the trailing edge line. I am also unable to move the aileron with the trim  or surface check step of the launch wizard. 
I replaced the left wing, and the same issue occurred. 
I replaced the left lift boom, and the same issue occurred. 
I replaced the center wing and the same issue occurred. 
I used the original wings with a different fuselage and the left aileron was responding correctly. 
This led me to believe it could either be an issue with the original Fuselage wiring or the avionics. 
I replaced the avionics on the original fuselage, used the original wings, and the left aileron was responding correctly. This leads me to believe it is an avionics issue.
The servo can move freely when it is not powered on. As soon as I connect the wing tip to the lift boom, it will make any aileron servo shoot down below the trailing edge line of the wings and you feel resistance when you try to move it.”

## Vehicle Configuration

Standard VXE-30
Battery

## Plan

- There seem to be multiple issues. Issue follows avionics box. Test on ironbird. See if repeatable.  We should C/CA each. Ok to open subtasks if better to separate. 
- Unable to move left aileron. Seems to track fuselage avbox Please report status on if this worked on the iron bird or not. Review servo voltage and current compared to other surfaces. 
- Do other surfaces work with this box?
- Unable to command any servo movement via RC. 
- Record if registering in GCS. Ask FS how to troubleshoot.
- XCOM to vehicle CAN not working.
- Open avbox, inspect, and test to isolate C/CA.
- Identify C/CA.
- Pull data logs if unable to isolate easily?

## Issue Status

Issue resolved from avbox swap. Avionics box received. Need to test and identify C/CA. 


2/2/2026 - Smisek
Provided Sammy with additional input on what to check. Connect to IB, VTOL is not connecting via CAN to xcomm (separate hardware unrelated to incident was able to connect). Unable to command any servo movement via RC (separate unrelated avionics hardware was able to command RC servo movement).  
Next steps recommend determining why CAN is not working.

## Comments (22)

### Greg Fryer, 2025-12-30

@Lauren Velasquez Expecting this AVBox to come back via RMA, please link here once it arrives.

### Lauren Velasquez, 2025-12-30

@Greg Fryer RMA forms have been sent to the customer. Will link and comment when it arrives.

### Lauren Velasquez, 2026-01-12

@Greg Fryer  Avionics Box has arrived and in RMA. Please advise who you would like me to drop this off with.

### Cameron Chapman, 2026-01-13

@Lauren Velasquez was the issue resolved when replacing the avbox? @Drew Cunnien if a new avbox resolves the issue, what is the priority of getting C/CA?

### Lauren Velasquez, 2026-01-13

@Cameron Chapman I am not sure the extent of the avionics being swapped/tested. That may be a question for @Michael Mohr  ?

### Drew Cunnien, 2026-01-13

@Cameron Chapman Did you intend to ping me sir? I apologize, but I have no idea how to provide any input on this issue.

### Cameron Chapman, 2026-01-13

@Drew Cunnien sorry. Wrong @Drew Hildreth

### Samuel Lopez, 2026-01-27

- Issue not immediately reproducible on iron bird bench.
- If Left Aileron has a problem, issue would be a Servo output.
- Opened ticket to petition Flight to test Avionics box on an asset aircraft to try and reproduce the problem there.  Ticket in queue.
- After Flight test, propose opening Avionics box to inspect for FOD.

### Scott Lovett, 2026-02-02

@Samuel Lopez when is the SCO flight scheduled for this?

### Samuel Lopez, 2026-02-02

@Scott Lovett  I have put the order in.  Let me ask Desiray where in the queue this is.

### Cody Smisek, 2026-02-02

@Samuel Lopez What did you check on the IB? Did you run it through launch wizard? Are you proposing the next step is a flight?

### Samuel Lopez, 2026-02-02

@Cody Smisek The initial prognosis was that the left aileron was locking up.  This may happen due to a problem with the servo voltages.  When I checked those on the iron bird, I saw no failures.

I am not proposing a full flight but to turn on in an asset aircraft on the ground.  If no other errors occur, I intend to open it up and look for evidence of FOD.  

@Cody Smisek if you have alternative recommendations, I am open to hear them.

### Cody Smisek, 2026-02-02

@Samuel Lopez we have internal assets we can do this on right now. 
You checked voltages? Did you perform a sweep of servos via software / RC?

### Samuel Lopez, 2026-02-02

@Cody Smisek I did not do a sweep of voltages.  Also, what is RC?

### Cody Smisek, 2026-02-02

@Scott Lovett This issue needs to be tracked down at the IB level. There is no reason to currently involve production / SCO. I have provided @Samuel Lopez additional direction on how / what to check next using the IB. Additionally, we have an engineering asset that we can utilize (preferably not until we determine if this Avionics could cause damage to other hardware). 
I have updated status with today’s updates.

### Samuel Lopez, 2026-02-03

- CAN does not communicate from Avionicx box to VTOL.  VTOL address not visible on webpage.
- Suspect issue is FOD or tombstoned components on FWAP.
- Dispositioned to open the avionics box and inspect.

### Cody Smisek, 2026-03-06

@Cameron Chapman potential for servo checks

### Cameron Chapman, 2026-03-06

@Cody Smisek This one seems less likely. Same issue happened with 2 wings, unless they were both affected. We can still check the servo involved to make sure. @Samuel Lopez

### Samuel Lopez, 2026-04-03

The problem has been recreated on the iron bird bench.
- When moving the avionics box, only the servo going to the Right Aileron moves.  The servo going to the Left Aileron stays static.
- The PWM measured on the right servo measured 6.29V DC voltage rail and 50 Hz on the PWM line.  However, the same mesurements on the left servo are 6.29V DC and 0 Hz on the PWM line.
- The same setup was already used to confirm that the servos do work, albeit with a V30 Advanced NAv


This confirms that the issue is the Fixed Wing Auto Pilot.  There is a small chance that the problem could be the series resistor network R24, which is highly doubtful.  The likeliest explanation is that the microcontroller on the FWAP has broken down.
*One nagging concern.  The XCOMM page takes a full minute (or a bit more) to come on.  Once it does it works normally though.
Will reach out to Lauren to see if the customer wants a replacement back, if so, will petition production to replace the FWAP and close the box.

### Alexander Alan Arnold, 2026-08-07

Fixed wing autopilot failure. closing since FWAP was replaced.

### Samuel Lopez, 2026-04-03

The problem has been recreated on the iron bird bench.
- When moving the avionics box, only the servo going to the Right Aileron moves.  The servo going to the Left Aileron stays static.
- The PWM measured on the right servo measured 6.29V DC voltage rail and 50 Hz on the PWM line.  However, the same mesurements on the left servo are 6.29V DC and 0 Hz on the PWM line.
- The same setup was already used to confirm that the servos do work, albeit with a V30 Advanced NAv


This confirms that the issue is the Fixed Wing Auto Pilot.  There is a small chance that the problem could be the series resistor network R24, which is highly doubtful.  The likeliest explanation is that the microcontroller on the FWAP has broken down.
*One nagging concern.  The XCOMM page takes a full minute (or a bit more) to come on.  Once it does it works normally though.
Will reach out to Lauren to see if the customer wants a replacement back, if so, will petition production to replace the FWAP and close the box.

### Alexander Alan Arnold, 2026-08-07

Fixed wing autopilot failure. closing since FWAP was replaced.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 799 configuration.jpg | image | 232 | 2025-12-22 | listed only |
| T95_V568_251222_093829_pack.zip | archive | 1113 | 2025-12-22 | listed only |
| T95_V799_251222_093829_pack.zip | archive | 892 | 2025-12-22 | listed only |
