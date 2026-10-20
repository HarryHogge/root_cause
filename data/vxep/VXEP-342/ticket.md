# VXEP-342: VXE 439 The autopilot has detected one or more of its VTOL sensors have failed warning

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-04-11
- **Updated:** 2026-09-14
- **Resolved:** 2025-05-13
- **Reporter:** Pat Wells
- **Assignee:** David Grosher
- **Creator:** Pat Wells
- **Labels:** No_crash, PMA_263, Training, Weekly-incident-tracker
- **Links:** relates to SMUP-25 (Update all Software generated Warnings/Cautions/Alerts and VTOL Messages )
- **Issue color:** purple
- **Vehicle Tail Number:** 439
- **Root Cause:** Believed to be an operating procedure that needs to be updated to include restarting the wizard
- **Impacted Core Subsystems:** Aircraft

## Description

Information from customer:
We have experienced some preflight errors. "the autopilot has detected one or more of its VTOL sensors have failed. This can be caused by excessively high or low temperatures or a hardware fault. You will not be able to launch the vehicle at this time." 
Temperature was in the mid to high 70s ambient.  This was across multiple AVs and were used and at a location without metal structures near-by. 
____________________________________________________________________________
There is no work around or path forward when this happens.  Suggested to customer that they should fully cycle power on aircraft and restart the launch wizard. 

AAR file provided by customer is attached.

## Comments (2)

### Pat Wells, 2024-04-16

@Greg Fryer @David Grosher is there anyone that has some time to look at this. 
Received another ping from the customer this morning.  This issue is preventing them from completing required flights. 

See below from customer:

We have been fighting this for the past two weeks and have only been able to get 5 flights in as this error is constantly repeating.  We have tried separate aircraft, separate GCS, power cycles and Mag Checks and the error is still occurring as of today.

### David Grosher, 2024-04-16

@Pat Wells The error is that the FW AP IMU error checks failed in this case. That IMU includes a magnetometer.  Given that it seems to be failing across a range of aircraft I suspect that there could be an environmental issue. Perhaps local magnetic disturbances, rebar in a reinforced concrete structure is often overlooked.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V439_240410_112841_pack.zip | archive | 1003 | 2024-04-11 | listed only |
