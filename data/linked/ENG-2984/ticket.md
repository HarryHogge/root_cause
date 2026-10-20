# ENG-2984: 732 Fuel Cell Flameout

- **Issue type:** Problem
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2024-11-17
- **Updated:** 2025-06-02
- **Resolved:** 2025-02-25
- **Reporter:** Daniel Lloyd
- **Assignee:** Pat Wells
- **Creator:** Daniel Lloyd
- **Labels:** TIQUILA
- **Links:** relates to VXEP-780 (VXE 732 Fuel cell flameout while in flight)

## Description

Flight profile was to fly a full endurance fuel cell flight with Tequila baseline HD55 payload. 
On the 13 November flight the aircraft was loaded with a fully serviced propane tank (922g of propane). Weight and balance was checked, aircraft weight was 44.7lbs. The aircraft was flown in a racetrack pattern. The flight was on track for an estimated 6.5 hrs when at about 5.2 hrs the fuel cell indicated an error and was no longer charging the hybrid battery. The HLB was approximately 55% and the VTOL control window indicated about 7 min of battery remaining. The fuel cell was commanded to stop, and then start was commanded. This did not correct the problem. The hybrid battery charge state was a little questionable for a VTOL landing so an uneventful glide landing was performed. Post flight it was determined that the cause of the fuel cell error was fuel starvation. The fuel tank was empty but the software indicated one hour of fuel remaining. 
On the 14 November flight the aircraft was again loaded with a fully serviced propane tank (922g of propane).  Prior to flight we leaked checked the system (from fuel tank to the fuel cell fitting in the nose) with the tank and manifold that was flown the day prior – no leaks detected.  We then leak checked using the manifold we were going to fly for the second flight– no leaks detected.  We flew the same plane, V732, with a different fuel tank, a different manifold, and different filter, and different fuel cell.  At approximately 6:00 into the flight, fuel cell control window indicated ~100 grams of propane remaining, and fuel cell control window and GCS telemetry indicated ~45 minutes endurance remaining, and the fuel cell stopped producing power.  The fuel cell status in the GCS telemetry said ERROR and flashed red.  The aircraft remained on mission.  The aircraft was commanded Go to IP4 of the PLZ while the HLB still had plenty of energy for a vertical landing with no issues. Post flight it was determined that the cause of the fuel cell error was fuel starvation. The fuel tank was empty but the software indicated fuel remaining. 
When the fuel cell stops in flight, or “shuts down” the software will begin non-stop chiming, there’s a pop-up that the fuel cell has shutdown inflight, and that the aircraft will automatically RTB for low energy. These things did not happen for either flight when the fuel cell quit generating power. On the first flight the data will show that those events occurred but that was because we commanded a shutdown.
Without intervention, we believe the plane would have remained on mission until the HLB was at 21 volts, commanded zero throttle, and glided down to the ground while continuing to navigate the mission.  We believe the aircraft should treat a loss of fuel cell power as a “fuel cell has stopped” and execute an Automatic Low-Energy RTB.
Please analyze the data and determine why the fuel cell ran out of fuel while still indicating fuel onboard.

## Comments (8)

### Daniel Lloyd, 2024-11-17

@Pat Wells @Garret Moose

### Daniel Lloyd, 2024-11-17

The weather was similar both days with light winds.

### Pat Wells, 2024-11-18

@Daniel Lloyd received. I’ll get an investigation started on this ASAP.

### Pat Wells, 2024-12-10

@Daniel Lloyd the Ann Arbor team has requested that this fuel cell be returned for further investigation.

### Daniel Lloyd, 2024-12-10

@Pat Wells Which one would they like? On 13 November we flew S/N 510 and then 14 November we flew S/N 509. We had the same results both days. This is mentioned in paragraph three, “We flew the same plane, V732, with a different fuel tank, a different manifold, and different filter, and different fuel cell.”

### Pat Wells, 2025-01-16

@Daniel Lloyd @Garret Moose Ann Arbor is asking for both fuel cells. 
@Rodney Linch will be reaching out to coordinate the RMA process.

### Pat Wells, 2025-02-04

Error discovered in fuel cells.  Advisory notice will be released with a plan to re-work affected units.

### Pat Wells, 2025-02-25

Final report attached to this ticket.

## Attachments (8)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| IMG_2821.jpg | image | 2439 | 2024-11-17 | listed only |
| IMG_2822.jpg | image | 1758 | 2024-11-17 | listed only |
| IMG_2825.jpg | image | 1632 | 2024-11-17 | listed only |
| IMG_2826.jpg | image | 2090 | 2024-11-17 | listed only |
| Screenshot 2024-11-17 174821.JPG | image | 270 | 2024-11-17 | listed only |
| T95_V732_241113_073820_pack.zip | archive | 6776 | 2024-11-17 | listed only |
| T95_V732_241114_081728_pack.zip | archive | 7357 | 2024-11-17 | listed only |
| [InvestigationReport_VIT2-500_Rev1.pdf](attachments/26486_InvestigationReport_VIT2-500_Rev1.pdf.md) | pdf | 1329 | 2025-02-25 | converted |
