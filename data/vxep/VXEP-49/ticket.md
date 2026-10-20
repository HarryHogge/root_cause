# VXEP-49: Scope "Sea Feature" implementation

- **Issue type:** Sub-task
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2023-09-11
- **Updated:** 2026-03-30
- **Resolved:** 2026-03-30
- **Reporter:** Kat Gulstad
- **Assignee:** David Grosher
- **Creator:** Kat Gulstad
- **Parent:** VXEP-32 TPTR-32 Launch from Waterborne Vessel (SRD-691)

## Description

What resources would it take to Integrate a “sea” feature:
- Turn magnetometer off while launching from a boat. The reason being that most decks are made of steel, which skews magnetometer data
- Remove “back up 10 ft” command in “Aborted Launch”
- When launching from a stationary boat, software, vehicle motion data from the IMU is averaged for calibration

Could you give me an estimate of:
- How many engineers/engineering hours it would take to implement this?
- What additional resources would you need to implement this?
- Are there any current blockers that would impact building, testing, or integrating this feature?

## Comments (3)

### David Grosher, 2023-09-13

@Kat Gulstad For requirements, I think the following are required:  
- Shipboard recovery
- Sea state
- Speed of the ship
- EMI specifications

As far as design is concerned the following is probably necessary:
- Optical flow from a downward camera
- Differential GNSS from the ship
- Newer GNSS hardware that is resistant to interference.
- Partial Fixed wing control in conjunction with attitude control such that tracking a moving ship is possible. This would require mode logic changes to the landing controller.  It will likely also require changes to the legacy FW controller if we do this before the UAP is completed.
- A navigation filter to estimate the biases in the accelerometer and gyro.

Potential Blockers: 
- Depending on the relative speed of the ship and wind it may be that a ship moving slower is more dangerous and impossible to land on because there isn’t enough power in the lift battery to track and land. At faster speeds then there would be enough Lift over the wing.

### Kat Gulstad, 2023-09-13

@David Grosher for your first few points:
- The vehicle must be able to recover on a ship
- The sea needs to be calm in order to land
- Speed + Blocker = @Sam Miller is there a maximum ship speed, or is this definitively 0 mph?
- EMI
- The ships will be made of steel, currently the only noted impact is to the instrumentation data. Other EMI impacts of will need to be investigated.

### David Grosher, 2023-09-15

@Kat Gulstad With respect to EMI, we need to ensure that there is no significant interference on the used GNSS bands.  Right now we are adversely impacted to power bleeding into the L1 band from adjacent bands.  There would also be comms concerns.  Naval ships are emitting a lot of power off their various RF systems. 
With respect to ship movement on recovery, it honestly isn’t realistic to assume no motion and a calm sea state, even if the UK MoD made such concessions. In reality, if we were to implement a system that was this constricted it wouldn’t ever be used by the end customer. Given that the launch requirement was sea state 3 with I think a relative speed of 17 knots including wind, we should aim for the same on recovery.

## Attachments (0)
