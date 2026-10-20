# VXEP-1923: Air Data Board - Accelerometer Board House testing

- **Issue type:** Sub-task
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2026-06-19
- **Updated:** 2026-07-13
- **Resolved:** 2026-07-02
- **Reporter:** Samuel Lopez
- **Assignee:** Samuel Lopez
- **Creator:** Samuel Lopez
- **Parent:** VXEP-1827 Air Data Board - Failures

## Description

Redwire expects to have failures on the Air Data Boards for the foreseeable future relating to accelerometer MPU 9250 and the barometer MS5611-01BA.  A recent sample of 20 saw 45 percent of the boards fail due to faulty accelerometer.  A previous batch saw similar numbers for barometer failures.  These have been identified as component failures.

The Air Data Boards are manufactured by Green Circuits.  Once delivered to Redwire, firmware is loaded on to the boards and the boards go through the checkout procedure to confirm the components whether the barometer/accelerometer are working and can go through calibration.   If the components fail, they could be sent back to Green Circuits to be removed and replaced by their machines.
It is being explored whether Green Circuits can load the firmware and perform the part of the checkout procedure that tests the barometer/accelerometer.  
Method 1
Give Green Circuits a HIL box.
Green Circuits would load the firmware themselves using a Pickkit4 programmer.  They would also need a Redwire laptop to load the hex file with the programmer.  After that, Green Circuits will run through the checkout procedure with a HIL box using the XCOMM webpage.  
Complications
This would require for Redwire to provide GC with a HIL box.  Production have indicated that they don’t have one ready and would need to re-work an older one.
Redwire will (probably) also have to provide a laptop for both programming and loading the XCOMM webpage.  Both IT and Legal would need to be consulted.
GC will need to know username and password of the XCOMM webpage.  At a minimum an NDA would need to be signed.
Method 2
GC do not get a Redwire laptop and don’t need our sensitive XCOMM information.  They only get a HIL box and a Pickkit4 programmer.
The programmer will be upgraded ahead of time where they connect to the ADB, press the button, and the firmware is loaded.
GC is still given a HILbox.

## Plan

Kurt Burian will instead develop a test kit that will load a test firmware on the ADB.  This ADB will ‘self-test’ and flash different LEDs if accel/baro passes.  However, due to higher priorities, this task is on hold.  For the moment, accept losses of ADBs.

## Issue Status

Air Data Boards that fail due to z-axis accelerometer limits will be placed in NCR.  Once the pile of failures is large enough (50?), Joseph Young and Aidan Calveat will coordinate sending to Green Circuits for one-time ‘remove and replace’ of that component.  Half of those can be expected to fail as well.

## Comments (0)

## Attachments (0)
