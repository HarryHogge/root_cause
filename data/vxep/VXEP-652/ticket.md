# VXEP-652: VXE 573 Cruise motor stopped during RTB, aircraft crashed

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-09-26
- **Updated:** 2026-09-09
- **Resolved:** 2025-01-10
- **Reporter:** Pat Wells
- **Assignee:** Cody Smisek
- **Creator:** Pat Wells
- **Labels:** Crash, FlightSystems, PMA263, Training, Weekly-incident-tracker
- **Links:** relates to RMA-360 (VXE-573 240924-4); relates to FS2-2321 (Create a consolidated report on mismatched SW/FW versions for VXE-572/573/574/628/688/594); relates to SMUP-45 (Review VXEP-652 and perform corrective actions)
- **Customer:** PMA263
- **Vehicle Tail Number:** 573
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical

## Description

Note, this is not new. Creating now as previously we didn’t receive data and now the aircraft is enroute to SLO so that the investigation can begin.  Incident is from the grouping with mis-matched software at 29 Palms. 8/26/24
Statement from operator
Cruise motor stopped during RTB and main battery rapidly depleted to 8%. Aircraft crashed

## Corrective Action

@Josh Burrell Evaluate manuals and advisory notice (AN-24-002) for appropriate guidance for returning to landing area. Update material if deficient.

## Issue Status

Data review complete. Aircraft returned to RMA
No additional logs will be provided by customer for this investigation.
VTOL AP removed from centerwing. Logs collected 12/19/24 CS
Fuse avionics would not connect via ironbird. Used APBL to check bootloader through ethernet. checked okay. opened avionics to remove SD card. With SD card removed, powered on avionics via ironbird, Xcomm was then accessible. Suspect corrupted SD. 12/19/24 CS
Additional note, when originally removing the SD card, unsure if RTV made for a non-normal disengaging of the mounting mechanism. Had a obvious ‘clunk’ when depressing. Was unable to duplicate after removal. 
Image copied to Jason’s Linux device for decrypting. However, log files were able to be retrieved after starting xcomm (no SD), inserting SD and then power cycling. Files added to data location.
Date of Crash 8/2/2024 - relevant xcomm file XCL00103
Xcomm FW 4.67
VTOL AP FW 1.53
Data located here VXEP-652 VXE573 Crash during RTB

## Root Cause

Aircraft descended (as commanded) while returning to PLZ resulting in controlled flight into terrain (CFIT). 
Appears operator may have issued a Go To IP2 during the RTB. At time of command, aircraft was ~4900ft msl. Impact elevation was ~3900ft msl. Autopilot was set to descend to ~3000ft msl.

## Comments (24)

### Adrian Garcia, 2024-12-06

@Cameron Chapman @David Grosher tried getting logs off the XCOMM but will not connect through Ethernet. I checked wires shark to see if it was getting any communication and it was not. The center wing has a ripped harness. I can unplug the vtol ap board and then hook it up to the iron bird to get the logs that way but I do not want to unplug anything without consent since this is an investigation and needs to be examined first. 

Fysa @Pat Wells

### Cameron Chapman, 2024-12-06

@David Grosher @Eric Brewer would pulling the SD cards and getting logs that way be more efficient and disturb less evidence than switching equipment to the ironbird? 
@Adrian Garcia do you see anything else abnormal with the equipment? This statement seems to indicate possible catastrophic shorting and burning, but it could also be a bad measurement/loose wire “Cruise motor stopped during RTB and main battery rapidly depleted to 8%. Aircraft crashed”
Fuel cell or main battery config? We may want to also ask what batteries were involved and where they are now.

### David Grosher, 2024-12-09

@Cameron Chapman I think documenting the state of the harness with some photos is fine.  After that let’s pull the boards and try to connect to the iron bird.

### Adrian Garcia, 2024-12-12

@Cameron Chapman @David Grosher this is the state of the harness. It looks to me like a strain rip. Additionally the AS150 do not seem to have any damage to them and the anti-spark was still measuring 6 ohms. 
[embedded d44e5757-d053-45eb-914a-57f2b35dd8ff.jpg]
[embedded 1538eb77-01b5-4107-a74e-c568598ba2b3.jpg]
[embedded caa06421-a95c-4e7c-be84-6369bb77e328.jpg]



[embedded image-20241209-164141.png]

### Cameron Chapman, 2024-12-17

Thanks @Adrian Garcia  please photograph under the cover once removed, then pull data logs.

### Adrian Garcia, 2024-12-19

[embedded 52824188-3944-456d-ae6e-b93d26ab294e.jpg]
[embedded 3cc3263e-4cdb-4dfb-af0b-0246936fa4d3.jpg]
[embedded 89d892e7-c884-4806-bf99-1115253e6b8a.jpg]
[embedded 1e23b507-a2b2-4e3a-9995-f415e4bc26d3.jpg]
[embedded 2afd333b-63e5-4f7d-9104-515b8b224138.jpg]
[embedded d80d1e89-af27-4ff8-abd4-acdee45d1b13.jpg]
[embedded 2afd333b-63e5-4f7d-9104-515b8b224138.jpg]
[embedded 1e817c5b-5bf0-4a20-a59d-ba65c9abdbb5.jpg]
[embedded bf7be34f-12b1-491d-bd04-4e3834ae871d.jpg]
[embedded aa756cd6-fbd6-474b-b630-cbca1ce40636.jpg]
[embedded c278ceca-0491-40aa-86a9-507f31ba3cba.jpg]
[embedded 39207fa9-45dd-458c-a337-731a6eb64756.jpg]

### Cody Smisek, 2024-12-19

@Pat Wells working on summarizing current data. But in interim, it appears xcomm stopped logging data just prior to the crash. FDR contains the crash portion but is much more limited in parameters to look at. 
Could you ask the customer if they have the AAR from this flight? The hope is that there’s a GCS specific file that would have been stored if they saved the AAR (even though they may not have gotten any other data from aircraft post crash). First glance is that without this log file, we likely wont have sufficient data to make a determination of cause. 

Just re-read the description section. Does that mean we will not receive the data from the customer?

### Pat Wells, 2024-12-20

@Cody Smisek the customer has provided all data that they are able to.

### Cody Smisek, 2024-12-20

@Pat Wells thanks for confirmation. I’ll provide a summary on what we have and we can go from there.

### Cody Smisek, 2024-12-20

@Pat Wells retracting my previous statements regarding data. I mismatched some logs. Looks like FDR contains same end data as xcomm. 
I reached out to Chris Joyce to get some additional information on geographically where the launch recovery location would have been for this, as the distance (from GCS) and altitude (AGL) at the last data line have me suspecting terrain may be a factor.

### Cody Smisek, 2024-12-21

@Pat Wells see updated root cause and updated slides. I would like to confer with the software team regarding how to identify DTED (unsure if contributing). Additionally, it’s unclear to me how to determine when the user issues the Go To command or if there was some auto waypoint sequencing that occurred. 
Regardless, I don’t think any additional findings would directly impact the path forward for this specific incident. The operator had ~2mins to recognize the aircraft was descending. 
@David Grosher FYI.

### David Grosher, 2024-12-23

@Cody Smisek Good job on the analysis. @Ted Trowbridge or @Craig Burton might be able to help with the DTED portion of the investigation.

### Cody Smisek, 2024-12-23

returned aircraft to RMA. FYI @Rodney Linch

### Craig Burton, 2024-12-23

@David Grosher  @Ted Trowbridge  Unfortunately, there is no way, logs or otherwise, to determine the reference elevations specified in the waypoints, or the general elevation data (VTED) that was loaded into the vehicle.
That said, the Edge GCS contains a fair amount of logic to ensure that the vehicle will clear terrain when flying toward IP1.  For example, even if the operator specifies a precise IP1 altitude, the GCS may increase that altitude to match, for example, the altitude of the last waypoint in the Primary mission, if it is higher, so that the vehicle doesn't encounter terrain between the two points.  See CSamsView::UpdateMissionAgl.   Here is a comment from that method:
```
// need to update the ip1s with the safe return altitude:
// should be the highest of:
//		current altitude if flying
//		last waypoint in primary mission
//		required terrain clearance in straight line from current location to ip1 (if flying)
//		required terrain clearance in straight line from last waypoint in primary mission to ip1
//		current ip1 setpoint
```
I mention this because the Root Cause specifies that the operator may have chosen to route directly to IP2, in which case none of the logic mentioned above would have been applicable.

### Cody Smisek, 2024-12-26

@Craig Burton the question was more for personal gain. I’m having a hard time understanding the altitudes presented in the presentation for this ticket. The local terrain doesn’t align with the AGL reported. But it seems other spots it was accurate. Not sure what was going on there.

### Craig Burton, 2024-12-26

@Cody Smisek, I think I understand what is happening with the AGL after looking at your PPT, specifically the map overlay showing the impact location 5.75 miles from launch:
[embedded file]
My theory is that this is not DTED related, but is rather VTED related.  VTED is a compressed (lossy) form of DTED unique (I think) to the Jennings AP.  VTED data is loaded immediately after the missions/routes in the launch wizard.  The GCS calculates a matrix of elevations for an ~11.9 x ~11.9 mile area, centered about the vehicle's reference latitude and longitude.  Using the map overlay from your PPT, the circular orbit lies outside of the VTED area:
[embedded file]
As such, the autopilot takes the highest elevation within the VTED area that it has encountered so far and assumes that every point outside the area is at that elevation -- that's why the AGL dropped:  the ground elevation outside the VTED area was 'raised':
```
short GPSNavigation::GetVtedMaxElevation(long x1, long y1, long x2, long y2)
{
	if(this);

	VtedCrash = '1';

	short elev = (short)navm->GetVDted()->GetMaxElevation(x1, y1, x2, y2);

	VtedCrash = '2';

//	if(elev==VTED_NO_COVERAGE) elev = 0;
	if(elev==VTED_NO_COVERAGE)		// fly off the map?  return the highest value so far... 
		return maxelev;

	if(elev==VTED_NO_INIT) elev = 0;

#ifdef VTED_BYTE
	elev *= 100;	// convert compressed altitude to absolute altitude
#endif
	if(elev > maxelev)
		maxelev = elev;

	VtedCrash = '3';

	return elev;
}
```
@David Grosher This has implications for LRR.

### Alexander Alan Arnold, 2025-01-10

@Pat Wells see below

### Pat Wells, 2025-01-10

@Cody Smisek @Craig Burton @Alexander Alan Arnold We’ve already released the AN and the required updates have been made to the operator’s manual that will be published on the next release.
Suggest moving this forward and closing it out.

### Cody Smisek, 2025-01-10

@Pat Wells Sure, I don’t see where that is stated but I will close out the ticket.

### Pat Wells, 2025-01-10

@Alexander Alan Arnold FYSA

### Alexander Alan Arnold, 2025-01-10

@Pat Wells see below

### Pat Wells, 2025-01-10

@Cody Smisek @Craig Burton @Alexander Alan Arnold We’ve already released the AN and the required updates have been made to the operator’s manual that will be published on the next release.
Suggest moving this forward and closing it out.

### Cody Smisek, 2025-01-10

@Pat Wells Sure, I don’t see where that is stated but I will close out the ticket.

### Pat Wells, 2025-01-10

@Alexander Alan Arnold FYSA

## Attachments (18)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 1538eb77-01b5-4107-a74e-c568598ba2b3.jpg | image | 59 | 2024-12-12 | listed only |
| caa06421-a95c-4e7c-be84-6369bb77e328.jpg | image | 45 | 2024-12-12 | listed only |
| d44e5757-d053-45eb-914a-57f2b35dd8ff.jpg | image | 62 | 2024-12-12 | listed only |
| image-20241209-164141.png | image | 15801 | 2024-12-12 | listed only |
| 1e23b507-a2b2-4e3a-9995-f415e4bc26d3.jpg | image | 106 | 2024-12-19 | listed only |
| 1e817c5b-5bf0-4a20-a59d-ba65c9abdbb5.jpg | image | 95 | 2024-12-19 | listed only |
| 2afd333b-63e5-4f7d-9104-515b8b224138 (cd855c9d-f3d2-4af7-952d-378711086fe7).jpg | image | 99 | 2024-12-19 | listed only |
| 2afd333b-63e5-4f7d-9104-515b8b224138.jpg | image | 99 | 2024-12-19 | listed only |
| 39207fa9-45dd-458c-a337-731a6eb64756.jpg | image | 98 | 2024-12-19 | listed only |
| 3cc3263e-4cdb-4dfb-af0b-0246936fa4d3.jpg | image | 74 | 2024-12-19 | listed only |
| 52824188-3944-456d-ae6e-b93d26ab294e.jpg | image | 65 | 2024-12-19 | listed only |
| 89d892e7-c884-4806-bf99-1115253e6b8a.jpg | image | 68 | 2024-12-19 | listed only |
| aa756cd6-fbd6-474b-b630-cbca1ce40636.jpg | image | 105 | 2024-12-19 | listed only |
| bf7be34f-12b1-491d-bd04-4e3834ae871d.jpg | image | 90 | 2024-12-19 | listed only |
| c278ceca-0491-40aa-86a9-507f31ba3cba.jpg | image | 118 | 2024-12-19 | listed only |
| d80d1e89-af27-4ff8-abd4-acdee45d1b13.jpg | image | 89 | 2024-12-19 | listed only |
| impact-map.png | image | 1403 | 2024-12-26 | listed only |
| orbit-outside-vted-coverage.jpg | image | 234 | 2024-12-26 | listed only |
