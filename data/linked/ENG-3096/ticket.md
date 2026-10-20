# ENG-3096: W1 disappeared after passing Mission Check in Launch Wizard

- **Issue type:** Problem
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2024-08-23
- **Updated:** 2025-06-02
- **Resolved:** 2024-09-27
- **Reporter:** Garret Moose
- **Assignee:** Pat Wells
- **Creator:** Garret Moose
- **Links:** relates to VXEP-556 (VXE 600 W1 disappeared after passing Mission Check in Launch Wizard)

## Description

Mission from previous day was opened, edited, and saved as today’s mission.  Simulation was run and passed.  Launch Wizard was run.  Mission Check passed.  A few screens later mission (and DTED) was uploaded to V600.  GCS was disconnected from the aircraft.
To have a backup GCS on standby, a second GCS was connected to V600 and the mission was Saved from Vehicle.  Simulation was run and failed.  Error: Less than 2 Waypoints in Launch Segment.
Upon inspection, there was no W1 on either GCS.  Dotted green line went from L to R2.  There was no waypoint 1 on either GCS.
AAR attached.
What would have happened if they had not downloaded the mission to a 2nd GCS, run a sim, and caught this?  What would the aircraft do if launched with no W1?

## Comments (8)

### Pat Wells, 2024-08-23

@Garret Moose  received

### Pat Wells, 2024-09-05

@Garret Moose 
Questions from the engineers conducting the investigation.

- Which GCS was the AAR generated from? GCS1 or GCS2?
- Do they know the times or name of the mission in question so we can associate it with a point in the logs?
- Was WP1 observed to be missing on GCS1 after it was restarted and re-downloaded the mission? Or had it been left up/running since originally uploading the mission that passed LW checks?

### Garret Moose, 2024-09-09

AAR we created on the first GCS.  The absence of W1 was noticed on the second GCS when it failed a mission simulation.  It was then observed that W1 was missing on the first GCS and concluded that W1 vanished on the first GCS before the mission was uploaded to the aircraft (and then saved from the aircraft to the second GCS).  I just uploaded a second AAR.  It might have been saved after noticing W1 was missing and before the flight.  I believe the mission was re-saved with the same name after adding W1 back in.  I will ask it they can provide the previous mission which was opened and edited to create this mission.

### Garret Moose, 2024-09-09

From looking at the Event.txt, it appears that they started up the GCS software, cleared the mission that automatically loaded, opened “20240807-REIVER LOOK 2 Short Range Ant Mission.vmis”, edited it, and saved it (at 25:28 and 50:24) as “20240813-Short_Range antenna sortie.vmis” (with a typo on the date in the name of the file - date should have been 20240823).  They started the launch wizard, uploaded the mission to the plane, saved it to the second GCS, discovered W1 missing, discovered it also missing on first GCS, and (at 65:39) re-loaded the mission on first GCS to see if it was missing from the saved version of the mission (it was).  W1 was added back into the mission and saved at 67:43.  I do not see a “Data pack saved” until after the flight, so I do not think one was produced that includes a version of “20240813-Short_Range antenna sortie.vmis” without W1.  I will see if they can provide “20240807-REIVER LOOK 2 Short Range Ant Mission.vmis”.

### Pat Wells, 2024-09-09

@Garret Moose acknowledged

### Pat Wells, 2024-09-27

@Garret Moose final investigation report attached.

### Garret Moose, 2024-09-30

Was how the GCS showed L and R2 (with no waypoint #1) investigated?

### Pat Wells, 2024-09-30

@Garret Moose I’ll check with the team.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V600_240823_101808_01_pack.zip | archive | 8167 | 2024-08-23 | listed only |
| T95_V600_240823_101808_pack.zip | archive | 4906 | 2024-09-09 | listed only |
| [VXE-600-Investigation.pdf](attachments/23535_VXE-600-Investigation.pdf.md) | pdf | 878 | 2024-09-27 | converted |
