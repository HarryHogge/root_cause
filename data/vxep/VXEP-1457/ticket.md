# VXEP-1457: VXE-626 GCS behaving abnormally,

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2025-07-28
- **Updated:** 2026-05-08
- **Resolved:** 2026-05-08
- **Reporter:** Jackson Riley Curvin
- **Assignee:** Ted Trowbridge
- **Creator:** Jackson Riley Curvin
- **Labels:** TIQUILA, Weekly-incident-tracker
- **Customer:** TIQUILA
- **Vehicle Tail Number:** VXE-626
- **Problem Type:** Discovered Issue
- **Incident Type:** Near Miss
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

On 22/07/25 at 19:51, A VHE 30 STALKER (EAGLE) Detachment, launched
 
All preflight checks were conducted and passed. Met was clear, dry and winds of 11.4 Kts. All within limitations. As the UA transitted East onto task, the GCS became JUMPY in area 12 (approx 8km from the GCS), and started populating mission elements (ORBIT HERE NOW) and repeatedly conducting SIM AND SYNC, roughly every 4-5 seconds. As the elements were repeating the update, it took control away from the GCS meaning the Pilot, Gnr Morrissey could not give the UA any positive commands and retain full control. The decision was made to close the VHE software on the GCS, reopen and reconnect to the UA in the attempt to rectify the issue. Upon reopening and reconnecting, the display appeared as normal to DOWNLOAD MISSION ELEMENTS. We conducted the download but despite saving the mission, it populated a previous mission outside of our AO (Area of Operations). This caused the UA to start to deviate from its commanded location. As the Authorising Officer (AO) and the Tac SSgt in control of the Detachments and Troop, also a Trained, Qualified, Current and Competent (TQCC) Captain, I made the decision to take control of the GCS while Bdr Turaganivalu had the Hand Controller. I placed the UA into U-Drive and commanded Bdr Turaganivalu to manually fly the UA as it was about to leave area 12 and enter area S at 1000ft AGL which would have breached airspace. Once in U-Drive, Bdr Turaganivalu manually flew the UA West in the authorised airspace back towards our location while I deleted the mission elements on the GCS. Once the old mission elements were deleted, the UA was back in area 7 and we had visual line of site (VLOS), I added mission elements to the UA and placed back un Autonomous to see if it reacted as commaded. It appeared to operate as normal. I then started to add additional elements using ORBITS and ZONE OVERLAYS. We noticed that when Zone Overlays were added, it caused the GCS to behave abnormally, again to be JUMPY and it deleted some of the Mission Elements from the GCS screen. However despite not displaying ORBIT 3 on the GCS, the UA continued to Orbit in the location commanded and at the altitude. The decision was then made to recover the UA and cease flying activity. The UA recovered as commanded in VTOL and inspected by the LAD Techs, showing no physical damage.

## Comments (11)

### David Grosher, 2025-07-29

can you assign this ticket to Ted, he is the IPT lead for GCS systems
Get Outlook for iOS<https://aka.ms/o0ukef>

### Pat Wells, 2025-07-30

@Ted Trowbridge FYSA

### Drew Hildreth, 2025-08-13

Good morning, @Ted Trowbridge . I know we have a million things going on. Have you had a chance to look at this?

### Ted Trowbridge, 2025-08-13

@Drew Hildreth I have not had a chance yet.  I’ll try to look and get an initial response back this week.

### Drew Hildreth, 2025-08-13

@Ted Trowbridge Thank you!

### David Grosher, 2025-08-15

@Jackson Riley Curvin Is it possible to request the zone overlays that were uploaded to the system prior to the observed poor performance?

### Ted Trowbridge, 2025-09-02

@Drew Hildreth the attached AAR data looks like it was pulled directly from XCOMM & VTOL via FTP - do we have an AAR from the GCS?  None of the GCS logs or settings are included so there’s almost nothing to investigate.

### David Grosher, 2026-01-30

@Drew Hildreth Can we either get logs or close this?

### Ted Trowbridge, 2026-05-08

@Drew Hildreth @Jackson Riley Curvin @Pat Wells @David Grosher 
Still not seeing any GCS logs or zone overlays attached, without them there is nothing to investigate.  I suspect even with GCS logs it will be difficult to determine what caused the issue.
Quite a bit of time has passed since this issue was raised, is the customer still tracking?  Can we backlog this and take it out of the active investigation queue?

### Pat Wells, 2026-05-08

@Jackson Riley Curvin let’s close this out. 

@Ted Trowbridge  FYSA

### Jackson Riley Curvin, 2026-05-08

@Ted Trowbridge I say we back log this issue

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 626_AAR_Data 2.zip | archive | 135376 | 2025-07-28 | listed only |
