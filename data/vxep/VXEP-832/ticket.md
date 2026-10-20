# VXEP-832: VXE 591 Low HLB During Fuel Cell flight resulted in operator commanding emergency landing

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-12-12
- **Updated:** 2026-03-02
- **Resolved:** 2024-12-23
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Cody Smisek
- **Creator:** Alexander Alan Arnold
- **Labels:** FlightSystems, MOLSON, Weekly-incident-tracker
- **Links:** relates to FS2-2633 (VXE-591 Low HLB in Fuel Cell Flight leads to Emergency landing); relates to RMA-451 (VXE-591 241220-1)
- **Customer:** MOLSON
- **Vehicle Tail Number:** VXE 591
- **Vehicle Configuration:** VXE 30 Fuel Cell and HLB
- **Incident Type:** Aircraft Damage
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

Operator Statement 
1.Preflight checks complete, no faults recorded. No icing seen
2.Good VTOL launch and transition to forward flight
3.Approx. 30min loiter @500AGL
4.Commanded to climb to 800AGL, AC unable to climb, HLB showed immediate drop in capacity below VTOL threshold
5.Attempted racetrack to charge HLB to capacity IOT to attempt VTOL, AC unable
6.AC showed difficulty maintaining altitude, HLB showed difficulty maintaining charge showed below 20% and continued to decline to sub 5%
7.AC altitude continued to diminish over a 15 min period, Decision to Emergency land taken
8.ELZ deconflicted from other AC via range control, and AC was commanded to ELZ
9.ELZ successful and AC was recovered, Fuel cell was still running when AC was recovered, FDR downloaded.

## Corrective Action

Review training material and technical publications for operator guidance when operating fuel cell.  Update both if deemed deficient.

## Issue Status

Data review complete. 
Summary
Aircraft was operated in icing conditions (weather forecast/report provided by customer indicated freezing fog). Post incident photos show significant leading edge icing on horizontal stab and undetermined portion of wing. VTOL lift props appear to also have icing build up. Fuel cell operated as designed, outputting >450W throughout the flight (and 500W when in ‘emergency’ mode). Aircraft was in orbit for first 30mins averaging ~700W of power consumption resulting in a decrease of HLB SoC from 70% (after VTOL launch) to 50%. A climb was subsequently commanded to 800ft AGL, throttle initially increased to 100% but quickly decreased to ~60%, likely due to power limit implemented in AP code based on HLB SoC (to prevent using all power in a climb), thus aircraft did not climb as commanded. Flight was continued in attempt to charge battery, however energy consumption never decreased below fuel cell output, leading to glide landing at ELZ. 

Link to slides with visual data representation/explanation VXEP-832 VXE591 Fuel Cell Glide landing

## Root Cause

Required power to maintain forward flight exceeded nominal fuel cell output for ~30mins resulting in depleted hybrid lift battery and subsequent operator initiated glide landing. Flight into known icing conditions likely contributed to higher than normal cruise power (~700W).

## Comments (17)

### Alexander Alan Arnold, 2024-12-12

Attached are the two zip files they provided and a power point with details and pictures. @Greg Fryer

### Alexander Alan Arnold, 2024-12-12

FYI @David Grosher

### Cameron Chapman, 2024-12-12

@Christopher Ridgard FYI

### David Grosher, 2024-12-12

@Stephen Peters Can you check the performance of the FC?
@Ben Triplett Can you check anything that would impact the power demand of the system? Wind, airspeed calibration, Motor Performance, …

@Eric Brewer @Scott Whitney FYSA

### Stephen Peters, 2024-12-12

@Sean WendlingCan you take a look at this?

### Cody Smisek, 2024-12-12

Fuel cell ripping 500W. Where’s all the energy going?
[embedded: newplot (3).png]

### Cody Smisek, 2024-12-12

Now that is some in flight icing!
[embedded: image-20241212-202843.png]

### Cody Smisek, 2024-12-17

@Greg Fryer @Alexander Alan Arnold might be worth reaching back out to MOLSON to ensure they understand how to manage fuel cell flights before they have another incident.

### Cody Smisek, 2024-12-17

VXEP-832 VXE591 Fuel Cell Glide landing Feel free to use, delete, modify these quick slides I created.

### Cody Smisek, 2024-12-18

@Greg Fryer @Pat Wells @David Grosher See issue status for link to presentation with additional data. Root cause section filled out. Let me know if a review is needed.

### David Grosher, 2024-12-18

@Cody Smisek Looks good.

### Pat Wells, 2024-12-18

@Cody Smisek thanks.  I’ll review and release report to customer today.

### Greg Fryer, 2024-12-18

I moved this to D8, @Pat Wells kick it to done once the message goes out? We can re-open if anyone has an issue.

### Pat Wells, 2024-12-18

@Cody Smisek are you attributing the 700w power draw to the icing of the aircraft?
Customer is asking why it’s drawing 700w.

### Cody Smisek, 2024-12-18

@Pat Wells Your answer lies in the Root Cause section of this ticket. Yes, it is what seems most logical at this point given that they provided the pictures of icing on aircraft surfaces. 
I do not have a definitive amount of expected increase in power consumption when flying through icing. Could be determined through engineering test by 3D printing representative ice shapes and flying to quantify. But given we currently prohibit flight into icing, I don’t think it would currently be useful to our resources available. Yesterday, I was reviewing a university publication that estimated a nearly 80% increase in power consumption due to icing of forward propellers (in our case, customer did not provide indications of icing on fwd props, but seems very possible given the accumulation on horizontal stab).

### Pat Wells, 2024-12-18

@Cody Smisek thank you for clarifying.

### Pat Wells, 2024-12-23

Operator error

## Attachments (6)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 591 (1).zip | archive | 622 | 2024-12-12 | listed only |
| [591 VXE30 FS 10 Dec 24.pptx](attachments/24970_591%20VXE30%20FS%2010%20Dec%2024.pptx.md) | pptx | 8970 | 2024-12-12 | converted |
| 591(2).zip | archive | 3392 | 2024-12-12 | listed only |
| image-20241212-202843.png | image | 1691 | 2024-12-12 | listed only |
| newplot (3).png | image | 124 | 2024-12-12 | listed only |
| [Vehicle Incident Report MOLSON VXE591.pdf](attachments/25066_Vehicle%20Incident%20Report%20MOLSON%20VXE591.pdf.md) | pdf | 1894 | 2024-12-18 | converted |
