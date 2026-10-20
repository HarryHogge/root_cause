# VXEP-1489: VXE-499 Failed to transition to VTOL, Crash

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Confirmed
- **Priority:** Highest
- **Created:** 2025-08-28
- **Updated:** 2026-09-03
- **Resolved:** 2026-08-11
- **Reporter:** Michael Mohr
- **Assignee:** Jacob Troyer
- **Creator:** Michael Mohr
- **Labels:** GS_Closed, Redwire, Weekly-incident-tracker
- **Links:** relates to RMA-796 (VXE-499 RMA 250905-1)
- **Customer:** Redwire
- **Vehicle Tail Number:** 499
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical
- **Components (EA Aircraft):** Aircraft, full assembly

## Description

Conducting battery training flight with a student. Student commanded RTB. After IP4, student commanded abort per FE04/instructor. Nominal behavior during abort and second PLZ. At IP5, aircraft failed to transition to VTOL. Commanded Orbit Here Now. Aircraft turned toward Orbit Here Now location but continued to descent into the ground. Activate User Landed Control did not populate until aircraft was on the ground. We continued to have contact with aircraft via Silvus until batteries pulled by ERT. All flight behavior was nominal aside from one instance. On launch, student selected launch, Activate User Landing Control populated, aircraft took approximately 30 seconds to initiate launch.
(Secondary description) 
During landing, the aircraft approached its transition point and the standard beeps were heard. The VTOL motors did not initiate and the vehicle flew past the point. The message was relayed to the operator and I relocated so that I could keep eyes on the aircraft until it eventually went down in the field near the GCS. I would like to add to what was said above about the delayed launch. When the aircraft does its pause at 20 feet after takeoff, it held the position for what seemed like 4-5 seconds. It was definitely longer than usual.

## Vehicle Configuration

VXE30
E140 MWIR
HLB 2-2198
Main 3-1623

## Plan

Recommended next steps: @Alexander Alan Arnold  or @Steve Gonzales  are you available to do those?
- Create separate linked Jira incidents for each issue.
- Aircraft not following commands “At IP5, aircraft failed to transition to VTOL. Commanded Orbit Here Now. Aircraft turned toward Orbit Here Now location but continued to descent into the ground. Activate User Landed Control did not populate until aircraft was on the ground.”
- Was the aircraft inspected before relaunching? Should it have been grounded for investigation? Aircraft was heavily damaged after incident. It was not relaunched.
- VTOL Issue
- For the VTOL failure one, I recommend zooming in plotting the Ibatt current around the voltage drop (take the 200A burst out of the plot). A large voltage drop with a small amount of current indicates a resistance issue (likely AS150 contact). We could perform a resistance measurement on the contacts, look at flight history for evidence of degradation or extreme profile runs, link this to AS150 systemic investigation and add those steps to typical processes, etc.

## Comments (6)

### David Grosher, 2025-08-28

@Michael Mohr @Cameron Chapman @Connor Peebles It appears to be a power issue, throttle commands are sent on VTOL transition, voltage sags but no current is pulled. There is no indication of a HLB cell issue. 

[embedded image-20250828-155107.png]
[embedded image-20250828-155457.png]

### Jackson Riley Curvin, 2025-08-28

@David Grosher   could the aircraft think that it had low battery and glide land?
[embedded fbc9ed4e-feca-4724-a817-5d605093f440.jpg]

### Cameron Chapman, 2025-09-08

See plan field for recommended next steps

### Ronnie Baker, 2025-11-07

A/C 333 and 334 are Mod complete and can be shipped back to the customer.

### Pat Wells, 2026-08-11

@Michael Mohr who is the customer on this. 
@Alexander Alan Arnold where did we end up with this investigation. It looks like it just stopped.

### Alexander Alan Arnold, 2026-08-11

@Pat Wells This is the Riga internal asset that has been repaired and flown multiple times without issue since repair.

## Attachments (22)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 499event.txt.png | image | 109 | 2025-08-28 | listed only |
| Image (1).jpg | image | 146 | 2025-08-28 | listed only |
| Image (10).jpg | image | 169 | 2025-08-28 | listed only |
| Image (2).jpg | image | 151 | 2025-08-28 | listed only |
| Image (3).jpg | image | 197 | 2025-08-28 | listed only |
| Image (4).jpg | image | 179 | 2025-08-28 | listed only |
| Image (5).jpg | image | 194 | 2025-08-28 | listed only |
| Image (6).jpg | image | 177 | 2025-08-28 | listed only |
| Image (7).jpg | image | 140 | 2025-08-28 | listed only |
| Image (8).jpg | image | 177 | 2025-08-28 | listed only |
| Image (9).jpg | image | 196 | 2025-08-28 | listed only |
| Image.jpg | image | 10426 | 2025-08-28 | listed only |
| T95_V499_250828_141550_pack.zip | archive | 2762 | 2025-08-28 | listed only |
| VTOL_VXE499.zip | archive | 126828 | 2025-08-28 | listed only |
| VXE499 028Aug2025.mp4 | video | 2018 | 2025-08-28 | listed only |
| [VXE499 28AUG2025 Mishap Reporting Procedure Form.pdf](attachments/31835_VXE499%2028AUG2025%20Mishap%20Reporting%20Procedure%20Form.pdf.md) | pdf | 463 | 2025-08-28 | converted |
| XCOMM_VXE499.zip | archive | 43296 | 2025-08-28 | listed only |
| [eventlog.txt](attachments/31863_eventlog.txt.md) | text | 101 | 2025-08-28 | converted |
| fbc9ed4e-feca-4724-a817-5d605093f440.jpg | image | 105 | 2025-08-28 | listed only |
| fullscreen.PNG | image | 4409 | 2025-08-28 | listed only |
| image-20250828-155107.png | image | 72 | 2025-08-28 | listed only |
| image-20250828-155457.png | image | 19 | 2025-08-28 | listed only |
