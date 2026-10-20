# VXEP-1548: VXE 863 VTOL motors cut during landing resulting in unintended glide landing

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-10-14
- **Updated:** 2026-08-07
- **Resolved:** 2026-01-14
- **Reporter:** Alexander Alan Arnold
- **Assignee:** David Grosher
- **Creator:** Alexander Alan Arnold
- **Labels:** USBP
- **Links:** relates to FS2-3882 (Investigation: VTOL motors cut during landing); relates to VXEP-1692 (B40/30 XCOM WDT resets ); relates to VXEP-1978 (VXE 863 Loss of Link warning resulted in uncontrolled descent ); relates to RMA-820 (VXE-863 RMA 251022-1)
- **Customer:** USBP
- **Vehicle Tail Number:** VXE 863
- **Vehicle Configuration:** VXE-30, battery, gimbal (unknown)
- **Root Cause:** Watchdog reset on xcomm processor caused invalid detection of landing state.
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical

## Description

Operator Statement
On October 10, 2025, at approximately 2053 hours, the US Border Patrol Tucson Sector sUAS team experienced a mishap involving the Edge Autonomy VXE-30 #863 during the landing sequence. 
After approximately 2 hours and 28 minutes of flight, we commanded the aircraft to return to the primary landing zone and begin the landing sequence. The aircraft entered the landing pattern as normal. The aircraft transitioned to VTOL and began descending. Several seconds into the descent, the VTOL lift motors appeared to shut off, causing the aircraft to pitch into a sharp dive and transitioned to a northbound glide. The GCS operator stated that the VTOL launch/landing popup never came up on the screen, but the laptop did make a noise (like the windows doorbell chime) at the time it normally pops up during landing. The aircraft continued gliding approximately 2,000 feet north of the landing area. After approximately 30 seconds, we observed that the aircraft had completed a glide landing and was on the ground.  No warnings or errors were displayed on the GCS. The GCS showed the aircrafts main battery at 24% and the VTOL HLB to be at 68% after the glide landing.
We located the aircraft at the last known coordinates displayed on the GCS. The VXE-30 appeared to have glided into a bush before ground impact. Observable damage was limited to the elevator and the elevator-to-tail attachment point. The payload remained clear of the ground and appeared undamaged; subsequent functional checks appeared to show the payload was operating normally.  The batteries involved have been tagged and separated.

## Corrective Action

Remove memory allocation/deallocation associated with File I/O on XCOMM. (Note: this is being delivered with v6.6, it will address ~90-95% of dynamic memory allocation)

## Plan

@David Grosher  did you want electrical to investigate this specific HW, since it had a higher frequency, or try to find issues on internal XCOM assets first. 
@Drew Hildreth where is the XCOM involved that had these issues? Is there a linked RMA?

## Issue Status

Investigation complete, root cause of VTOL motor cutoff identified.  Slides here.
The root cause was an xcomm watchdog reset. 
Investigation of watchdog events ongoing.

## Comments (17)

### Alexander Alan Arnold, 2025-10-14

@David Grosher This incident happened on the night of the tenth, but we just received data today.

### David Grosher, 2025-10-14

@Alexander Alan Arnold It looks like there was a WDT on the XCOMM which led to a 2nd datalog in the XCOMM that wasn’t included in the AAR package. This is the 2nd WDT on 863s XCOMM during an investigation. We are tracking this as an issue that we intend to fix in the next SW release, but this particular set of hardware appears to be more prone to the issue. It would be prudent to RMA the aircraft and swap the XCOMM board.  In the meantime, can we ask for a dump of the XCOMM SD card. I would like to get XCL00098.csv and all of the event logs to search for additional issues.

### Alexander Alan Arnold, 2025-10-14

@David Grosher If I have them do the FTP procedure and download files that way would that get you what you need?

### David Grosher, 2025-10-14

@Alexander Alan Arnold Yes that would work. I only need the data from the XCOMM.

### Michael Mohr, 2025-10-22

@David Grosher Uploaded XCOMM and also VTOL.

### Drew Hildreth, 2025-10-22

@Michael Mohr Let’s get this moving. This aircraft crashed 10/10. We got the data that we needed so get with @Lauren Velasquez and get the aircraft moving to SLO.

### David Grosher, 2025-10-31

@Scott Whitney Can we have one of the SQA team work this?

### Scott Whitney, 2025-10-31

@David Grosher - Can do. I will have @Logan Wright take a look next week. https://jenaero.atlassian.net/browse/FS2-3882 used to track on FS2 board

### Jackson Riley Curvin, 2025-11-12

@David Grosher @Logan Wright @Scott Whitney  This is from XCL00098
[embedded: image-20251112-194224.png]

### David Grosher, 2025-11-12

@Jackson Riley Curvin THis is a counter that is reset everytime it is logged. When the logging changes rates from 10 Hz to 0.1Hz you will see this 100x change. This isn’t an issue.

### David Grosher, 2025-11-21

The system transitioned into descent and then LAND_COMPLETE almost immediately. This is very strange. The data is in XCL0098.csv during the event. Note: the CPU time is hard to track because the XCOMM had a WDT in the middle of the flight. It seems like the landing was detected prematurely resulting in the lift motors being safed.  
[embedded: image-20251121-195302.png]

### David Grosher, 2025-11-21

VTOL data, that jump in the baro looks suspicious. Maybe the change in the baro offset was the result of the WDT on the XCOMM? The XCOMM CPUTime was 2138 when the landing occurred, which appears to be close to the jump in the offset. 
[embedded: image-20251121-201532.png]
[embedded: image-20251121-201753.png]

Lift Throttles for timing reference: 
[embedded: image-20251121-201657.png]

### Eric Brewer, 2025-11-24

@David Grosher @Jackson Riley Curvin @Logan Wright @Scott Whitney @Drew Hildreth I created a report linked above.  The root cause was an xcomm watchdog reset, Dave advises we have seen 5-10 watchdog resets with the latest software but haven’t traced root cause.

### Drew Hildreth, 2025-12-02

@Eric Brewer thank you for the report. What are the thoughts on disposition with this aircraft? Replace the Xcomm and flight test? or more to it?

Additionally, the aircraft has some other damage that will need to be addressed.

### Eric Brewer, 2025-12-02

@Drew Hildreth  - @David Grosher do you have thoughts here? If we think it’s a (random?) memory error that we don’t have a good handle on would replacing xcomm do any good?

### Drew Hildreth, 2025-12-02

@Eric Brewer memory here too… I know we talked about it before that it is a SW deal, but this aircraft had multiple instances which makes me wonder if there is a hardware issue lingering.

### David Grosher, 2026-01-14

Completed CA with File I/O refactor delivered in v6.6

## Attachments (17)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| CENTER WING.jpg | image | 2870 | 2025-10-14 | listed only |
| ELEVATOR.jpg | image | 2697 | 2025-10-14 | listed only |
| GCS1.jpg | image | 3885 | 2025-10-14 | listed only |
| GCS2.jpg | image | 4414 | 2025-10-14 | listed only |
| GCS3.jpg | image | 3706 | 2025-10-14 | listed only |
| HLB TESTED.jpg | image | 3824 | 2025-10-14 | listed only |
| LEFT WING.jpg | image | 3157 | 2025-10-14 | listed only |
| RIGHT WING.jpg | image | 2435 | 2025-10-14 | listed only |
| T95_V863_251010_182413_pack.zip | archive | 3577 | 2025-10-14 | listed only |
| TAIL BOOM.jpg | image | 4638 | 2025-10-14 | listed only |
| VTOL_VXE863.zip | archive | 69348 | 2025-10-22 | listed only |
| XCOMM_VXE863.zip | archive | 19231 | 2025-10-22 | listed only |
| image-20251112-194224.png | image | 16 | 2025-11-12 | listed only |
| image-20251121-195302.png | image | 55 | 2025-11-21 | listed only |
| image-20251121-201532.png | image | 16 | 2025-11-21 | listed only |
| image-20251121-201657.png | image | 12 | 2025-11-21 | listed only |
| image-20251121-201753.png | image | 11 | 2025-11-21 | listed only |
