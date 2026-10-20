# VXEP-14: TPTR-88 Fuel Cell Failure During Startup

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2023-08-23
- **Updated:** 2024-02-28
- **Resolved:** 2024-02-28
- **Reporter:** Allen Gardner
- **Assignee:** Cameron Chapman
- **Creator:** Allen Gardner
- **Links:** is blocked by VA-712 (Identify and execute CAs for TIQ TPTR-88 (SW issue in cathode fan)); relates to VXEP-26 (TPTR-96 Fan RPM shown incorrectly on GCS during fuel cell start up)
- **Customer:** TIQUILA
- **Severity:** 3 - Degraded Performance - With Workaround
- **Impacted Disciplines:** Hardware, Quality Assurance

## Description

During STALKER FAT Testing, one of the D450+ Fuel Cells (SN:510) failed during start up.  Fault code 17440 was observed and rebooting the fuel cell did not resolve the issue. This was observed during set up of system through operators manual and prevented steps for SRD-6 in fuel cell configuration to be passed.

## Corrective Action

Related to PTR-96 Cathode fan calibration values have been expanded.  CAR in process for updating production fuel cells. 
See TPTR-58_EAES 8D Failure Analysis_10.9.2023.pptx
[embedded: image-20231108-034517.png]

## Issue Status

Root cause determined.  Implementation of CARS in process.  
See TPTR-58_EAES 8D Failure Analysis_10.9.2023.pptx

## Root Cause

Software issue.  Cathode fan calibration values did not cover all failure modes.
[embedded: image-20231108-034415.png]

See TPTR-58_EAES 8D Failure Analysis_10.9.2023.pptx

## Comments (9)

### Allen Gardner, 2023-08-25

@Cameron Chapman Can you create a task to determine root cause?

### Cameron Chapman, 2023-09-05

@Tom Westrich @Sean Wendling I'm told TIQUILA PTRs are engineering's top priority. Can someone please provide status for this one? Can you please track and link the corrective actions in JIRA.

### Sean Wendling, 2023-09-06

Hello All, I received SN510 and was able to recreate the error here. Cathode Fan failed to operate during warm-up and during diagnostics. Once it was replaced with a new blower, the system functioned as intended. The cause is determined to be either lock-rotor failure or a unprotected high power draw that damaged the blower motor. We have observed this failure in the past and are currently working with our developer’s software team and are expecting a software update to apply to all systems. I will continue to update this ticket as we apply updates and follow through with our validation plan implementing the correction.

### Greg Fryer, 2023-10-19

@Cameron Chapman @Sean Wendling I created an Epic in VA to get this organized like our others. As you identify any further tasks, please create them under that Epic https://jenaero.atlassian.net/browse/VA-712 
This will automatically take care of linking and such.

### Cameron Chapman, 2023-11-06

@Sean Wendling can you please provide the following information to process this issue to closure? 
- Do you have a link to the CARs mentioned in the root cause?
- Which software version fixes this issue? Is it fixed in the fuel cell software, GCS, elsewhere?
- What equipment versions does this affect?
- What is the release date of that software?
- Is there a service bulletin that will be applied to shipped equipment?

### Sean Wendling, 2023-11-07

Hey Cameron, I attached the 8D report published for this cathode issue. Initially we had it under TPTR-58, I think there may have been some confusion on where it was to go. I think that covers number 1.
2. Software that corrects for this issue is under the firmware embedded into the blower control boards inside the Fuel Cell. In the current main fuel cell software, the software on these boards are not reported. In the next revision we intend to add this reporting so that users can validate the proper software is in use.
3. This issue is only for D450+ (serial numbers >500). Note, while we were developing the corrected blower board software, an alternative CA was created for immediate production needs. The CAs were characterized as “Calibration Settings Only” and “Blower Software Update” (with the latter bein the preferred solution). Therefore, there are some early deliveries with a “Calibration Settings Only” CA. This corrects the problem, however it does not allow for rapid cooldown which is a new feature for D450+.  Regardless, all active D450+ systems that have been delivered have received one of these two acceptable CAs.
4. I am unsure of the exact release date. Validation started in mid-September and it was implemented widely before October. All TIQ systems have this software. 
5. At this time, I am not sure that service bulletin is required as all active systems have one of the two CAs. Updating this software at this time is not possible outside of Ann Arbor, as it requires direct connection to the blower boards. 
Let me know if that helps, or if any additional reporting/information is required!
Thanks, Sean

### Cameron Chapman, 2023-11-07

It looks like this issue is ready to close. @Sean Wendling do you agree? 
@Former user or @Greg Fryer , is there a formal TPTR closure process?

### Sean Wendling, 2023-11-09

I would agree. I think this would be cleared for closure.
Additional note, not sure where we would like to highlight it (I can update and add to the report), but at the request of LM a note has been added to the Quality Document that ships with Fuel Cells as an additional containment measure.

### Greg Fryer, 2024-02-28

Note: I am closing this based on the work being complete. Not aware of PM currently tracking any open TPTRs, but we can always reset if needed.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [TPTR-58_EAES 8D Failure Analysis_10.9.2023.pptx](attachments/17406_TPTR-58_EAES%208D%20Failure%20Analysis_10.9.2023.pptx.md) | pptx | 7568 | 2023-11-07 | converted |
| image-20231108-034415.png | image | 36 | 2023-11-07 | listed only |
| image-20231108-034517.png | image | 49 | 2023-11-07 | listed only |
