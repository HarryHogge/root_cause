# VXEP-910: VXE 562 lost comms and descended into terrain uncommanded

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** High
- **Created:** 2025-01-24
- **Updated:** 2026-09-09
- **Resolved:** 2025-04-23
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Jason Scherer
- **Creator:** Alexander Alan Arnold
- **Labels:** Crash, Mismatched_SW/FW, PMA263, Software, Training, Weekly-incident-tracker
- **Links:** relates to RMA-465 (VXE-562  250116-1); relates to FS2-3027 (Review VXEP-910 Investigation and Create Report)
- **Customer:** PMA263
- **Vehicle Tail Number:** VXE 562
- **Vehicle Configuration:** standard battery
- **Issue Status:** Investigation Complete
- **Root Cause:** - Vehicle received command to “Land Now” resulting in an immediate emergency descent.
- **Incident Type:** Aircraft Damage
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

Investigation Report: Vehicle Investigation VXEP-910.pptx
SharePoint Folder: VXEP-910 VXE562 Lost Comms and Descended into Terrain
AAR pulled using EDGE SLO GCS, debug and other applicable files may contain irrelevant data. 
Note: In v6.4 there is a new margin of safety on the HLB energy check that results in a more robust check prior to a land now.  
Special payload harness was connected to blue bulgin and transponder port. Removed to check origin. Photo attached. 
xcomm 4.67 154F build CRC 55CF3E55
VTOL 1.52 6799 build CRC 9E66896E
FW 6.05m C4D9
Silvus 4.0.3.14 FW
2231 MHz / 20MHz BW
Link Distance 50000
Max Power
Legacy


The MO and I setup fuselauge and wing 562 with the HD45 payload. All components of the AV were in proper operable condition. Everything was good during preflight checks, and the weather was clear. VO was conducting ISR over MOUT 3 and in attempt to gain better visual, VO pushed north of the river, where comms were lost. AV begain it's VTOL descent on it's own without going back to lost comms orbit. AV landed in the forest.

## Corrective Action

- Follow ADs and update SW/FW on fleet.
- Enable check on the GCS to inform operator that the firmware is out of date.

## Comments (16)

### David Grosher, 2025-01-28

@Rodney Linch Do we have this aircraft yet? 
@Alexander Alan Arnold FYSA

### Rodney Linch, 2025-01-28

@David Grosher - delivered to EN a few minutes ago.

### David Grosher, 2025-02-14

@Cameron Chapman Can you pull data from this aircraft?

### Cody Smisek, 2025-02-14

@David Grosher @Cameron Chapman I’m running around doing hands on today. I can grab real quick.

### Cody Smisek, 2025-02-14

@David Grosher AAR and relevant xcomm/VTOL files are in the folder listed above.

### David Grosher, 2025-02-14

@Jason Scherer The current investigation has been added to the ISSUE STATUS field. Please review and assemble a report.

### Jason Scherer, 2025-02-28

@Alexander Alan Arnold Did we ever get an operator statement other than the title of this investigation? It looks to me like the vehicle was commanded to land now which would result in the immediate transition to VTOL and vertical decent regardless of terrain. I looked at the version of code flown, and the only way to get this log in the flight data is if the GCS sends a land now command.
[embedded image-20250301-001257.png]

### Alexander Alan Arnold, 2025-02-28

@Jason Scherer the operator statement is in the attachments they don’t state that they sent the command. But we’ve noticed that our PMA 263 Customer doesn’t always know what happens when they click certain buttons. If the data is there and conclusive to support operator error we should elaborate on it. It will help us build a case to be more involved in their training

### Jason Scherer, 2025-02-28

@Alexander Alan Arnold Sorry, I guess I didn’t check the attachments before asking. 
As for the land now command, the evidence we have shows the vehicle received a system command to recover which activates the “Land Now” states also known as “Land Immediately!” on the GCS. We have no GCS logs that I am aware to confirm how the GCS decided to send that command to the vehicle. My quick analysis in the GCS code indicates that there may be code paths that could lead to this behavior during link outages like what occurred in this incident. However, in my oldest AARs this setting is disabled. Meaning for this path to be valid they were either running old software that had it enabled or they enabled it themselves. Both options would be unsupported behavior. Without GCS data, and based on what I know about our GCS at the time, I have to assume it was an Operator command. I’ve tagged Mike B in the report in case he can shed some more light on this.
Otherwise, I’ve added what I can to the report. Let me know how we should proceed or if you want any changes.
@David Grosher

### Jason Scherer, 2025-03-03

@Alexander Alan Arnold Per Dave this report is good to go unless we get GCS logs.

### Alexander Alan Arnold, 2025-03-03

Reviewing now @Jason Scherer

### Rodney Linch, 2025-04-15

@Alexander Alan Arnold - issue status shows ‘investigation complete.’ Can I return 562’s cases to RMA?  Reviewing all the notes, is it safe to say this was operator error?

### Alexander Alan Arnold, 2025-04-15

@Rodney Linch This was non warranty and operator error to my knowledge confirm with @Pat Wells and @Drew Hildreth

### Drew Hildreth, 2025-04-15

@Rodney Linch This is operator error. Please get through the Material Disposition process and start working on a Paid Quote for this one.

### Pat Wells, 2025-04-23

@Alexander Alan Arnold this is complete. Please move to done

### Alexander Alan Arnold, 2025-04-23

Operator error

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [Stalker Loss of Link 26 Sep (3)(562).pdf](attachments/25597_Stalker%20Loss%20of%20Link%2026%20Sep%20(3)(562).pdf.md) | pdf | 2884 | 2025-01-24 | converted |
| Media (36).jpg | image | 245 | 2025-02-14 | listed only |
| image-20250301-001257.png | image | 11 | 2025-02-28 | listed only |
