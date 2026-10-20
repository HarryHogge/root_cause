# FS2-2616: Climb abort FC fault but AC did not abort take off

- **Issue type:** Bug
- **Status:** To Do
- **Priority:** Medium
- **Created:** 2024-12-06
- **Updated:** 2026-09-04
- **Reporter:** Ruysser Gabler
- **Assignee:** Jason Scherer
- **Creator:** Ruysser Gabler
- **Environment:** Takeoff in light snow, light winds, 0°F. Winds aloft 5.5 mph @ 274, temps aloft: -2°F. Light snow continued throughout the flight. Landed in light snow.
- **Links:** relates to FS2-2854 (Jason's Open Investigations); relates to VXEP-1661 (VXE 674 (HSV FLOPS) Will Not Connect in VXE SUAV)
- **Sprint:** FS2 Sprint 40

## Description

During demo in Alaska AC 499 had Fc installed. While climbing through 200ft during VTOL takeoff, the VTOL control window displayed “Climb abort, fuel cell fault”. The VTOL system did not abort the take off and continued to transition. The XCOMM window and fuel cell control windows did not display a fault. The fuel cell continued to operate without issue throughout the flight. 

Next day had the same thing happen. While climbing through ~40ft during VTOL takeoff, the VTOL control window displayed “Climb abort, fuel cell fault” again. The XCOMM window and fuel cell control windows did not display a fault. The aircraft continued to transition and flew without issue.

## Comments (4)

### Michael Berger, 2024-12-07

@Scott Whitney This is an issue with the vehcile firmware.
In the file ApmParser.cpp, in the fuction CApmParser::PowerMonitor() at about line 4000 the following code in xcomm_202
generates the specified message. The GCS just displays the specified text.
The xcomm is reporting the error, but then not doing anything about the error.
```
#ifdef BUILD_AMI
	if(testfc && g_AMIParser.GenFault())	// fuel cell was running but quit during launch
	{
		gApmStatus.Options &= ~APM_POWER;	
		gApVtolStatus.Faults |= VT_FAULT_POWER;
			
		if((gApVtolStatus.Faults != fault) && IsVtolFlying())
		{
			g_XCommControl.DebugMsg("Climb abort, fuel cell fault", 4);
			AddMessageHex(faultstr, gApVtolStatus.Faults);
		}
		fault = gApVtolStatus.Faults;
	}
#endif
```
Please move to FS2 Jira and reassign

### Ruysser Gabler, 2024-12-09

@Michael Berger Any idea why the Xcomm FC page would be reporting no error for the fuel cell? Is it possible that the error the GCS is reading is not actually an error?

### Michael Berger, 2024-12-09

@Scott Whitney @Ruysser Gabler The GCS is displaying the error message text sent from the XComm. It is just text which the GCS displays. The GCS has no idea what the text says.
The XComm could be incorrectly sending the error message, but that would need to be fixed in the XComm.

### Scott Whitney, 2024-12-10

Thanks @Michael Berger. Moving to FS2 backlog and reassigning to Jason.

This was seen in the MCM 1.1 flight test as well.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| Media.jfif | image | 420 | 2024-12-06 | listed only |
| T95_V499_241113_164522_pack.zip | archive | 2898 | 2024-12-06 | listed only |
| T95_V499_241114_074943_pack.zip | archive | 6390 | 2024-12-06 | listed only |
