# ENG-3072: VTOL Controller stopped talking during EMC emission ground tests (aircraft not radiated)

- **Issue type:** Problem
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Medium
- **Created:** 2025-01-23
- **Updated:** 2025-06-11
- **Resolved:** 2025-06-11
- **Reporter:** Garret Moose
- **Assignee:** Pat Wells
- **Creator:** Garret Moose
- **Links:** relates to VXEP-915 (VXE30 EMI/EMC Issue and Improvement Collector); relates to VXEP-916 (VTOL Controller stopped talking during EMC emission ground tests (aircraft not radiated))

## Description

During EMC emissions testing, all 3 VTOL Controller froze.  Motor Test and Instrument Panel went solid white; Sensors froze.  Refreshed webpages to try to restore and got white screens.  Did not get VTOL Controller page or login screen.  Cycled power to VTOL Controller by disconnecting and reconnecting umbilical cord.  Refreshed web pages and got VTOL Controller login screen in all 3 window.  AAR T95_V478_20250122_140014 with FDR downloaded.  AAR has lots of data because plane had been powered up for 20+ hours since last Reset.  FDR took approximately 1 hours to download with 64 dB radio link, <2 dB interference,  <10 Queue size, and <30% airtime.

## Comments (11)

### Garret Moose, 2025-01-23

[embedded: T95_V748_250122_140014_pack.zip]

### Pat Wells, 2025-01-24

@Garret Moose per previous discussions on this topic. The current delivered aircraft is not designed to survive this environment.

### Garret Moose, 2025-01-27

Hi. Pat.  To which environment are you referring?  We were measuring emssions coming off of the aircraft when all three VTOL Controller webpage windows froze.  We were not subjecting the aircraft to any outside radiation (other than from the Silvus radio and LabSat3 GPS simulator).

### Pat Wells, 2025-01-28

@Garret Moose we’ve reopened the investigation based on your clarification of the issue.

### Pat Wells, 2025-01-28

@Garret Moose the team is asking for the other two AAR’s.  Are they available and if so could you please attach them?

Thanks

### Pat Wells, 2025-01-28

@Garret Moose another question from the team.  Could you share your process for the motor tests?

### Garret Moose, 2025-01-28

What other two AARs?  When the VTOL Controller webpage windows froze, I produced one AAR. 
I don’t remember exactly what tests we were doing when the VTOL Controller webpages froze, but immediately before my notes about the pages freezing is a note about completing the vertical and horizontal polarization RF measurements of the forward motor running at 50% throttle (with propeller blades, using Propulsion Test in the Jennings GCS software).   After that, we measured at various receiver antenna positions while running the forward motor at 50% throttle (no blades, Jennings GCS Propulsion Test) and running the three working lift motors at 15% (1150 microseconds) (no blades, using the VTOL Controller/Motor Test webpage).

### Pat Wells, 2025-01-29

@Garret Moose you said “All 3 VTOL controller froze”  That lead us to believe there were 3 instances and 3 AAR’s.
You only have one AAR.  Got it.

### Pat Wells, 2025-01-31

@Garret Moose revisiting the All 3 VTOL controllers comment.  Were there 3 separate controllers involved in this or is this all related to one (the same) controller?

### Garret Moose, 2025-02-03

During EMC testing, we were simultaneously monitoring three separate VTOL controller webpages: Instrument Panel, Motor Test, and Sensors.  During one  test we observed that all three VTOL controller windows were frozen.  The Instrument Panel and Motor Test pages went all white.  The Sensors page still showed data, but was not updating.

### Pat Wells, 2025-02-03

@Garret Moose  thanks for clarifying.  That makes more sense now.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V748_250122_140014_pack.zip | archive | 35564 | 2025-01-23 | listed only |
