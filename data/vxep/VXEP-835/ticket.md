# VXEP-835: VXE 568 turned 180 degrees entering VTOL, made strained noise then nose dived

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-12-12
- **Updated:** 2026-09-09
- **Resolved:** 2025-02-25
- **Reporter:** Alexander Alan Arnold
- **Assignee:** David Grosher
- **Creator:** Alexander Alan Arnold
- **Labels:** Crash, PMA263, Training, Weekly-incident-tracker
- **Links:** relates to RMA-435 (VXE-568 241209-2); relates to XKIT-1958 (Havoc 550 fuse 371 CW - Land Transition Failure 20240423); relates to FS2-3017 (Finish investigation and create report for VXEP-835)
- **Customer:** PMA263
- **Vehicle Tail Number:** 568
- **Vehicle Configuration:** VXE 30 standard battery configuration
- **Plan:** Review report for completness
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical

## Description

Investigation Report: Vehicle Incident Report VXEP-835 VXE568.pptx
SharePoint Folder: Flight Safety - VXEP-835 VXE 568 turned 180 degrees entering VTOL, made strained noise then nose dived - All Documents

Operator statement 
Vehicle was RTB and preparing to land as vehicle lift booms came on vehicle preformed a 180 degree turn and flew forward 50 ft vehicle made a strained noise rocked backward then dipped into a nose dive in an open field at 200 ft 

Incident occurred September 2024.

## Corrective Action

In accordance with released airworthiness directives, the customer should update all vehicles to the latest released software configuration.

## Issue Status

Root cause is a known old VTOL processor bug that causes task lockup in flight critical tasks. This bug was resolved in firmware updates included in release 6.2.9 & 6.3.4

## Root Cause

VTOL AP task lockup occurred during fixed wing flight leading to impact with terrain during subsequent VTOL landing attempt. VTOL was using AP 1.53 FW with known Priority Inheritance bug. Most likely an issue with the RTC on the I2C bus given the date was wrong in some logs and there were many instances of the RTC being updated in previous flights. Also this vehicle was using very old SW, multiple ADs were not implemented.

## Comments (19)

### Alexander Alan Arnold, 2024-12-12

Crashed aircraft discovered during FSR visit to TALSA PAC facility. We were unable to obtain logs for the aircraft. Aircraft is currently in RMA area at SLO @Greg Fryer

### Cameron Chapman, 2024-12-12

@Adrian Garcia @Giovanni Gonzalez can you please pull these logs when available. @Rodney Linch please link to RMA ticket when created and let us know when available for engineering.

### Rodney Linch, 2024-12-12

VXE-568 241209-2 (RMA-435) https://jenaero.atlassian.net/browse/RMA-435

### Cody Smisek, 2024-12-18

XCL00090 likely crash flight. 
Corresponding VTOL log (VTOL00078) seems to be missing the landing.

### Cody Smisek, 2024-12-18

@Greg Fryer @David Grosher This probably needs 3rd party (Software team member) review to verify my findings. @Jason Scherer pointed me to his previous analysis and I leveraged that. Linked folder contains a couple slides to support root cause.

### David Grosher, 2024-12-19

@Cody Smisek @Pat Wells I agree with Cody’s assessment of the issue. This was old software that missed multiple ADs, it was not flight worthy.

### Cody Smisek, 2024-12-19

Returning aircraft to RMA

### Alexander Alan Arnold, 2024-12-23

@Pat Wells Please review this one.

### Pat Wells, 2025-01-02

@Cody Smisek reviewed. Operator failed to update firmware is my take away on this one.   @Alexander Alan Arnold FYSA

### Pat Wells, 2025-01-31

@David Grosher looking at the report it does not clearly state the root cause.  Can we get something more concise to share with the customer?

### Pat Wells, 2025-02-19

@David Grosher circling back to this one. The report is not in a state that we can release to customer. Looking to get a little attention on this if possible.

### David Grosher, 2025-02-19

@Pat Wells We will update the report. 
@Jason Scherer There is corroborating evidence to support Cody’s conclusion.  The RTC was updated in FW flight prior to the incident and the RTC was incorrect on startup the next time. The RTC and I2C bus hanging was one of the leading causes of this type of event.  Freezing of the prio 1 data in the xcomm log from the VTOL is hard to correlate to these events because the date/time of the supposed event in the VTOL log has a timestamp from the previous day, but the log appears to clearly show an incident since it stopped prior to landing.  
[18:05:59.022 3780.022] rtc updated from gps time
[00:00:09.002] AP startup 1900/01/01 00:00:09.002

### Jason Scherer, 2025-02-22

I am now working on this investigation.

### Jason Scherer, 2025-02-24

@Pat Wells @Alexander Alan Arnold @David Grosher Report has been updated. Please review and let me know if you have any questions or would like any changes/additional information.

### David Grosher, 2025-02-24

@Pat Wells @Jason Scherer It looks good to me.

### Pat Wells, 2025-02-25

@David Grosher I’m sending report to PM to pass along to customer.  We’re going to close this out on the customer facing side.  Not sure if you need to keep it open for any further tasks. 

@Alexander Alan Arnold  FYSA

### David Grosher, 2025-02-25

@Pat Wells @Alexander Alan Arnold We can close this one out. There isn’t much else to do.

### Alexander Alan Arnold, 2025-02-25

Closed.

### Pat Wells, 2025-03-28

Not warrantied.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [Stalker Crash 25 Sep 2024 VXE568 PMA263.pdf](attachments/24984_Stalker%20Crash%2025%20Sep%202024%20VXE568%20PMA263.pdf.md) | pdf | 1237 | 2024-12-12 | converted |
