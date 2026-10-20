# VXEP-1397: VXE 734 landing away from intended PLZ.

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-07-10
- **Updated:** 2025-09-16
- **Resolved:** 2025-09-16
- **Reporter:** Alexander Alan Arnold
- **Assignee:** David Grosher
- **Creator:** Alexander Alan Arnold
- **Labels:** Edge_Asset
- **Vehicle Tail Number:** VXE 734
- **Vehicle Configuration:** VXE 30, E140, Battery Config
- **Issue Status:** Likely operator error: accidental enabling of manual nudge.
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

734 seems to be drifting during landing. The first flight did not experience this issue. The second flight was normal until during the landing the Aircraft arrived above the PLZ with Lift Motors engaged and drifted well past the intended landing zone.  
734 has been grounded due to the safety risk the unexpected drift causes. 
Attached are AAR, Mission Files, and Screenshots showing the UAV trail to where the AV touched down versus the intended PLZ. 
The Issue is contained in data pack T95_V734_250710_103708_pack.zip 
The previous Non-Issue flight is located in T95_V734_250710_095019_pack.zip

## Comments (12)

### Greg Fryer, 2025-07-10

@David Grosher @Scott Whitney just reassigned to you, since needs analysis first.

### Alexander Alan Arnold, 2025-07-10

Attached Mishap form with Operator Statements. @David Grosher @Scott Whitney

### David Grosher, 2025-07-10

@Eric Brewer FYSA.

### Drew Hildreth, 2025-07-11

@Eric Brewer @David Grosher We are down to one asset for USSS Training here in HSV. If we could get a quick look and a potential CA that would be great. The Training Team has a lot of flights to get in and it will be very difficult with only one asset.

The other two assets we have are at MFIX or this wouldn’t be quite so hot.

### Eric Brewer, 2025-07-11

@Drew Hildreth I took a look through the logs.  It looks like when the drift occured, the autopilot was in ‘manual nudge’ mode, and the nudge commands were 0.  That starts around time 1390 in the plot below.  Then I see the nudging commands start around 1422 (non-zero pitch and roll commands).  Is it possible that the autopilot was inadvertently placed in manual nudge during the drift?

[embedded: image-20250711-151535.png]

### Drew Hildreth, 2025-07-11

@Eric Brewer I have reached out to the team and asked them. I will let you know. Talking to the team in the office here today, they say that isn’t standard practice to do something like that. I’ll let you know what I hear. Thank you for looking into this

### Alexander Alan Arnold, 2025-07-11

[embedded: image-20250711-152551.png]
 In the event log 2 minutes after the RTB command you see the U-Drive Activated, and then 1 minute later we see the pause commands 


[embedded: image-20250711-152931.png]

In the debug log at 10:45:22.180 the Aircraft entered land mode 
@Eric Brewer

### Alexander Alan Arnold, 2025-07-11

[embedded: image-20250711-155831.png]
IN the debug again there is a line VTOLCanUdrive Now: 1 Does this line mean that the Manual Nudge is active? @Eric Brewer @Scott Whitney

### Eric Brewer, 2025-07-11

@Alexander Alan Arnold I believe that line means that the dialogue that allows nudge is active, not necessarily that it’s activated.

### Jackson Riley Curvin, 2025-09-16

@Eric Brewer @David Grosher @Drew Hildreth do any of you see an issue with closing this?

### David Grosher, 2025-09-16

@Jackson Riley Curvin Nope, I think it should be closed.

### Jackson Riley Curvin, 2025-09-16

operator error

## Attachments (12)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [Mishap Reporting Procedure Form SS 2.pdf](attachments/30514_Mishap%20Reporting%20Procedure%20Form%20SS%202.pdf.md) | pdf | 506 | 2025-07-10 | converted |
| T95_V734_250710_095019_pack.zip | archive | 2777 | 2025-07-10 | listed only |
| T95_V734_250710_103708_pack.zip | archive | 3079 | 2025-07-10 | listed only |
| distance from PLZ to actual tocuhdown.PNG | image | 2273 | 2025-07-10 | listed only |
| gus courtland_first successful flight.vmis | other | 4 | 2025-07-10 | listed only |
| lisa courtland1_second flight drift upon landing.vmis | other | 4 | 2025-07-10 | listed only |
| map screenshot zoomed in.PNG | image | 2062 | 2025-07-10 | listed only |
| map screenshot zoomed out.PNG | image | 1376 | 2025-07-10 | listed only |
| image-20250711-151535.png | image | 98 | 2025-07-11 | listed only |
| image-20250711-152551.png | image | 13 | 2025-07-11 | listed only |
| image-20250711-152931.png | image | 69 | 2025-07-11 | listed only |
| image-20250711-155831.png | image | 71 | 2025-07-11 | listed only |
