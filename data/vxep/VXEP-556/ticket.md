# VXEP-556: VXE 600 W1 disappeared after passing Mission Check in Launch Wizard

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-08-23
- **Updated:** 2026-03-02
- **Resolved:** 2025-02-25
- **Reporter:** Pat Wells
- **Assignee:** Ted Trowbridge
- **Creator:** Pat Wells
- **Labels:** TIQUILA, Weekly-incident-tracker
- **Links:** relates to ENG-3096 (W1 disappeared after passing Mission Check in Launch Wizard); relates to MS-405 (VXEP-556 Support); is caused by GCSS-359 (Launch allowed after deleting W1 during Launch Wizard); is caused by GCSS-364 (FTP of mission.txt does not use integrity checks); relates to RMA-459 (VXE-600 Card Swap & Expansion 250429-9)
- **Customer:** TIQUILA
- **Vehicle Tail Number:** 600
- **Incident Type:** Mission Failure/Abort
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

Received from LM:
Mission from previous day was opened, edited, and saved as today’s mission. Simulation was run and passed. Launch Wizard was run. Mission Check passed. A few screens later mission (and DTED) was uploaded to V600. GCS was disconnected from the aircraft.
To have a backup GCS on standby, a second GCS was connected to V600 and the mission was Saved from Vehicle. Simulation was run and failed. Error: Less than 2 Waypoints in Launch Segment.
Upon inspection, there was no W1 on either GCS. Dotted green line went from L to R2. There was no waypoint 1 on either GCS.
What would have happened if they had not downloaded the mission to a 2nd GCS, run a sim, and caught this? What would the aircraft do if launched with no W1?

AAR Attached

## Comments (16)

### Greg Fryer, 2024-09-04

Moved to @Ted Trowbridge to investigate and log potential bug.

### Ted Trowbridge, 2024-09-05

**Preliminary Findings:**

Simulation was run and passed. Launch Wizard was run. Mission Check passed. A few screens later mission (and DTED) was uploaded to V600. GCS was disconnected from the aircraft.

- If the mission passed the launch wizard checks then the launch route on the GCS must have had two waypoints.
- After upload to the vehicle there is an integrity check done on the mission (similar to a hash/crc) that would have failed if the vehicle received a corrupted version of the mission with only one waypoint in the launch route. The logs indicate all uploads were verified successfully so we can assume the vehicle must have had a valid launch route.
- To allow downloads from another GCS a separate copy of the mission file is uploaded (via a side channel) to the vehicle but there are no integrity checks for the upload. A failed transfer could leave a bad mission file that doesn't reflect what's actually loaded in the autopilot to be flown.
- The logs indicate a possible link fault during FTP of the side channeled mission:

```
T95_V600_240823_101808_xcevlog.txt
...
[09:04:00.660 1273.660] ap link fault: local rx okay ap rx bad
[09:04:01.490 1274.490] ftp login attempt from:  10.0.108.50
[09:04:01.508 1274.508] ftp login attempt from:  10.0.108.50
[09:04:01.576 1274.577] ftp rx: SD1:/mission.txt
[09:04:01.697 1274.697] ftp rx done: SD1:/mission.txt
[09:04:07.812 1280.812] ap link restored
...

```
To have a backup GCS on standby, a second GCS was connected to V600 and the mission was Saved from Vehicle. Simulation was run and failed. Error: Less than 2 Waypoints in Launch Segment.

- Suspect that the corrupted mission was downloaded, and the simulation failed as expected due to the missing waypoint.  The mission loaded in the autopilot would still be valid and this check prevented overwriting it with the corrupt/invalid version.

What would have happened if they had not downloaded the mission to a 2nd GCS, run a sim, and caught this?

- I believe the mission loaded in the autopilot to be flown was valid and contained 2 waypoints in the launch route. It would have launched and flown normally.

What would the aircraft do if launched with no W1?

- I don’t see a way the vehicle could get into this state.  Will need to follow up with the embedded team and/or run a HIL test with a special GCS build to determine what would happen in this unlikely situation

**Questions:**

- Which GCS was the AAR generated from?  GCS1 or GCS2?
- Do they know the times or name of the mission in question so we can associate it with a point in the logs?
- Was WP1 observed to be missing on GCS1 after it was restarted and re-downloaded the mission?  Or had it been left up/running since originally uploading the mission that passed LW checks?

@Greg Fryer @Pat Wells @Michael Berger

### Pat Wells, 2024-09-05

@Ted Trowbridge 
Questions sent to customer.

### Pat Wells, 2024-09-09

@Ted Trowbridge information received below from LM FSR
I’ve also attached the additional AAR that he referenced to this ticket. 

AAR we created on the first GCS. The absence of W1 was noticed on the second GCS when it failed a mission simulation. It was then observed that W1 was missing on the first GCS and concluded that W1 vanished on the first GCS before the mission was uploaded to the aircraft (and then saved from the aircraft to the second GCS). I just uploaded a second AAR. It might have been saved after noticing W1 was missing and before the flight. I believe the mission was re-saved with the same name after adding W1 back in. I will ask it they can provide the previous mission which was opened and edited to create this mission.
From looking at the Event.txt, it appears that they started up the GCS software, cleared the mission that automatically loaded, opened “20240807-REIVER LOOK 2 Short Range Ant Mission.vmis”, edited it, and saved it (at 25:28 and 50:24) as “20240813-Short_Range antenna sortie.vmis” (with a typo on the date in the name of the file - date should have been 20240823). They started the launch wizard, uploaded the mission to the plane, saved it to the second GCS, discovered W1 missing, discovered it also missing on first GCS, and (at 65:39) re-loaded the mission on first GCS to see if it was missing from the saved version of the mission (it was). W1 was added back into the mission and saved at 67:43. I do not see a “Data pack saved” until after the flight, so I do not think one was produced that includes a version of “20240813-Short_Range antenna sortie.vmis” without W1. I will see if they can provide “20240807-REIVER LOOK 2 Short Range Ant Mission.vmis”.

### Pat Wells, 2024-09-16

@Ted Trowbridge  checking in for any updates ahead of the Air Worthiness brief with TIQ on Wed 9/18

### Ted Trowbridge, 2024-09-16

@Pat Wells  i’ll provide an update before 2024-09-18

### Scott Whitney, 2024-09-17

@Wesley Reynolds

### Ted Trowbridge, 2024-09-17

**Update**

Further investigation has shown it is possible to launch the vehicle without W1 if the waypoint is deleted after the launch wizard mission checkout step is completed.  We were unable to determine the exact cause of W1 being deleted in this case, but an errant keypress or mission file corruption are possible explanations.
We were able to reproduce a similar situation in the HIL by purposefully deleting W1 after the mission checkout step but before downloading the mission to the vehicle.  The mission simulation passes without flagging any errors. (Only the launch wizard mission checkout page will check for the presence of two launch waypoints)
Operators should not launch if they notice the launch route does not have two waypoints.  The system has not been fully tested to verify safe launch behavior.  Limited HIL testing has shown the vehicle will safely launch and proceed to the primary mission waypoints, but the launch departure heading for transition from VTOL to fixed wing flight is unpredictable.  This would present a flight risk if there were launch heading restrictions due to obstacles, terrain, wind, or other factors.
When the mission contains W1, a predictable launch heading is followed as the vehicle transitions to fixed wing flight.  I’ve filed https://jenaero.atlassian.net/browse/GCSS-359 to track and fix the issue.
@Pat Wells @Greg Fryer

### Pat Wells, 2024-09-23

@Ted Trowbridge are you near closing this out from the customer’s perspective as far as root cause and advice to operators? I see that there appears to be some possible corrective actions in the works. 
Customer is enquiring as apparently this anomaly has an aircraft grounded.

### Ted Trowbridge, 2024-09-26

Investigation complete: VXE-600-Investigation.pptx
Two corrective actions (bugs) logged against GCS.

### Pat Wells, 2024-09-26

@Ted Trowbridge thank  you.
@David Grosher looking for a green light from you on the final report before I release to TIQ customer. I don’t have any issues or concerns with it.

### David Grosher, 2024-09-27

@Pat Wells This is good to go out to the customer.

### Pat Wells, 2024-09-27

Thank you

### Pat Wells, 2024-09-30

@Ted Trowbridge @David Grosher 
Customer came back with a question:
”Was how the GCS showed L and R2 (with no waypoint #1) investigated?”

### David Grosher, 2024-09-30

@Pat Wells @Ted Trowbridge My understanding of that question is the following: “We don’t believe the operator changed the mission plan intentionally after passing the checks, how then could the W1 waypoint have been lost?” is that correct?

### Pat Wells, 2024-10-08

@David Grosher 
@Ted Trowbridge 
The customer has come back with questions on our report.  I know our stance is that we’ve provided a report and we’re moving on. 
Just to be safe is there anything below from the customer that we want to address?  There’s a mention that we some things:

We’re confident that W1 was not deleted between the LW check and uploading the mission to the AV, which is still making us query how W1 disappeared?
- The report does not address the fact that the screen showed L followed by R2 (no waypoint 1) and the Table View showed L followed by R1 (possibly the reverse).  Either way, the screen and the Table View should show the same thing.

- If the pilot did delete W1, and the integrity check uploading W1 to the aircraft works as advertised, then an operator can ensure the mission in the plane has W1 by verifying the mission on the screen has W1 immediately before or after uploading the mission to the plane.  If the pilot didn’t delete W1, then we aren’t sure as to what happened to W1 and we  don’t know how to ensure it doesn’t happen again.

 
If you and the team could provide some feedback on the above please? Updated report with comments would also help

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V600_240823_101808_01_pack.zip | archive | 8167 | 2024-08-23 | listed only |
| T95_V600_240823_101808_pack.zip | archive | 4906 | 2024-09-09 | listed only |
| [VXE-600-Investigation.pdf](attachments/23534_VXE-600-Investigation.pdf.md) | pdf | 878 | 2024-09-27 | converted |
