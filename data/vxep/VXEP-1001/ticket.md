# VXEP-1001: 2025 ADP (cameras and heated pitot) Test Plan and Execution.

- **Issue type:** Epic
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2025-02-11
- **Updated:** 2025-09-11
- **Resolved:** 2025-09-11
- **Reporter:** Cameron Chapman
- **Assignee:** Rajesh Budhabhatti
- **Creator:** Cameron Chapman
- **Parent:** VXEP-266 VXE (all) ADP: Heated Pitot/New SA CAM/Remove other obsolete components
- **Issue Status:** 2/25: “I just finished the flight mode thermal testing and would be compiling the results in the test report. “ Raj

## Description

| Confluence Page: | https://jenaero.atlassian.net/wiki/spaces/PDAO/pages/163643414/Air+Data+Pod+Updates+and+Heated+Pitot+Initial+and+Havoc |
| Main Project JIRA | https://jenaero.atlassian.net/browse/VXEP-266 |
| HP Test | https://jenaero.atlassian.net/browse/VA-1346 |
| SA Camera Test Planning and Execution | https://jenaero.atlassian.net/browse/VXEP-1001 |
| Shared Folder: | https://jenaero.sharepoint.com/:f:/r/sites/EngineeringTeam/Shared%20Documents/Electrical/SA%20Camera%20Replacement?csf=1&web=1&e=c6XIc6 |

SA Camera Test Plan.docx

## Plan

- SA Camera Test Plan.docx

Spreadsheet for tests SA Camera system Temp data.xlsx
Tests. 
- Replicate ground operations and determine limits and following actions
- Determine max temp equipment can operate continuously.
- If not 50C+solar load ~60C, determine plan for ground operations. Ex: keep off until pre-flight, add ground cooling. Coordinate with @Scott Whitney tasks to implement these actions. 
- Solar loading test of ADP. Determine effect of solar load on ADP temps.
- Replicate flight operations. 
- Make a test setup drawing/document for wind tunnel testing at various temps. Ex: fan in a chamber.
- Account for reduced airflow due to altitude.
- Review test results and record in requirements sheet.
- @Rajesh Budhabhatti please indicate status of each of the above and link to the test data or summary location.
- Complete all subtasks

## Comments (3)

### Rajesh Budhabhatti, 2025-02-12

Some of the document links here. They will be moved to appropriate places after the testing is done. 
Camera testing folder: Camera Testing
Camera test plan: SA Camera Test Plan.docx
Test Data: SA Camera system Temp data.xlsx
ADP requirement: 2025 ADP Requirements.xlsx

### Cameron Chapman, 2025-02-17

@Rajesh Budhabhatti Nice test procedure. SA Camera Test Plan.docx
Review notes:
 
- I linked this procedure to the JIRA task for testing. Please do that in the future and track correspondence there https://jenaero.atlassian.net/browse/VXEP-1001
- Drilling holes into the camera to measure internal temps seems risky. Can the cameras report their own temps? Do we know the hottest spots on the camera to instrument and the mfr recommended max temp?
- What is Jn temp?  Which Jn?
- Do you have any abort temps where you would shut off the test, or are you confident the equipment will protect itself without damage (or it is easy to replace)?
- Has anyone verified a 150 cfm fan is realistic airspeed? Are we accounting for less cooling at altitude?
- Which chamber are you testing in? I think we have large curing booths at 50C that could be a good option. Smaller chambers can add more unrealistic airflow from their chamber fans. We could block airflow from the enclosure if needed
- It looks like there is a separate spreadsheet for measurement already. If so, we could prevent duplication by deleting it from the word doc and linking it instead.
- -40C seems extreme. Check requirements for LRR lowest temp. We should test the equipment to that lower end as well. We could start with the lower temps, as they should be less risk of damage. Be careful of condensation when cooling.
- Why do you start with 0 and 5fps? Should we run the camera just like the aircraft runs it, for more realistic timing.
- Why does the diagram say 24VDC? The system is all 12V. Is that for the fan?

FYI @Jacob Troyer

### Rajesh Budhabhatti, 2025-02-26

While the 60C flight mode test (fan On), the Sightline encoder dropped the frame rate to 6 fps and continued to operate, however; the image quality degraded. Upon further examination, it appears that FLIR camera is fine but the MIPI camera is only displaying distorted monochromatic image. Replacing the MIPI camera with a new one did not improve the image quality so it seems that Sightline encoder board got damaged.

## Attachments (0)
