# VXEP-1701: Evaluate XCOM acceptance tests, document issues, and implement fixes.

- **Issue type:** Major Project
- **Status:** Assigned
- **Priority:** High
- **Created:** 2026-02-19
- **Updated:** 2026-03-11
- **Reporter:** Cameron Chapman
- **Assignee:** Scott Whitney
- **Creator:** Cameron Chapman
- **Links:** relates to VXEP-1692 (B40/30 XCOM WDT resets )

## Description

Sharepoint https://jenaero.sharepoint.com/:f:/s/EngineeringTeam/IgCmHcFgdXPeRbdcqQHWgJ8-AaTn-G522CHwO_3ML45Rhj0?e=i3TwV7
Investigation sheet.: https://jenaero.sharepoint.com/:f:/s/EngineeringTeam/IgCmHcFgdXPeRbdcqQHWgJ8-AaTn-G522CHwO_3ML45Rhj0?e=i3TwV7
Redlining and commenting on this version: 2120003-01 - Electronics - Xcomm Board (1607P01A) 1 - Build Procedure.pptx
Concerns reported by @Scott Whitney , @Ben Norris @Dustin Limon are you available to elaborate on these? 
- Test is using XCOM FW 4.67 FW. Latest release is 4.74. Test should be using firmware that will be loaded onto the hardware for shipment (usually latest released unless otherwise specified).
- Record any blockers why this cannot happen and scope to fix. Reportedly unable to use newer due to tools.
- Ensure there is a process to notify operators/for operators to check to ensure they are loading the latest FW.
- Pass/fail criteria seems to be based on uptime. 6+ hours of uptime. Test is 6 hours. If someone does not check right after the test they could miss resets. Ex: if left overnight, will show 12+ hours even if it reset during test. 
- Does not check for WD or other resets.
- Potential fix. Open XCOM log xc.txt. Verify only one set of logs exists during test period. Will change when going to 4.7.4. Need engineering analysis
- FSE and EE to review this test and determine improvements.

## Plan

Actions
- Immediate test
- Check 10 XCOM. compare fallout rate. 
- B30 XCOMs.
- B40 latest successful build of progression testing. Not original RC3. As far as we have run currently with no WD issues. @Brandon Slater @Logan Wright please post version here and send to @Ben Norris
- Run burn in test. Ramp to temp. Hold there. Plan on 48 hours but check and notify team at shorter intervals. Ex: 1,2,4,8,16 hrs (normal working hours acceptable)
- When feature complete again (progression testing complete), load that FW and rerun this test.
- XCOM Procedure/process improvements. @Michelle Greenwald 
- Make sure runtime matches test time/time since turned on.
- Update procedure and Traveler. @Michelle Greenwald
- Ensure both say no reruns. No reruns of board. Add to procedure. NCR if test fails for unexplainable purpose. (failures due to things like power outage seem ok to rerun). @Michelle Greenwald
- Add to procedure and train how to check for WDs at appropriate steps in the process (after burn in, maybe others) and instructions for what to do when observed (Write NCR, attach logs).
- Run latest released FW with all future tests. @Daniel Ceja 
- Production only uses release GCS version. Using CCB. Goes onto egg.
- Ask @Christa Meck @Alfredo Macias @Nicole Hess  about notifying when GCS FW is released. Is there a location where everyone could go to check latest released GCS SW?
- Go to \\egg\Released\PROD\SW, look for latest version of GCS installer. Ex: VXEGCS_V6.6.1_Installer. @Daniel Ceja  can you please update documentation to use this process for any procedure that needs latest SW (or develop another system to ensure equipment is always latest)?
- Check for WDs at the end of each test? Connecting to multiple boards and pulling logs would be easier with a VLAN switch. https://chatgpt.com/share/699e3945-dce0-800a-acc5-c787c7af338c
- Run latest released B40 FW on boards that will be B40. Label boards with B40 PN and perform mods before burn in and other production test.
- @Daniel Ceja
- Significant occurrence of WD 128 in logs. This has been tied to the practice of hot mating the boot loader connector to the XCOM during configuration. 
- Verify that the procedure says not to do this. 
- It seems vague since there is not a specific step to press the on button, but I can definitely see how this seems to indicate power should be turned on before connecting the boot loader. FYI Ben Norris
- [embedded: image-20260223-233503.png]
- Train all personnel about procedure steps and ensure this is not done.
- See if correlation to this practice and later WD failures.
- Can we have someone help summarize failure rate, firmware run during test, if it was retested, what level they were failed? Develop a better system to track them?
- Ask @Steve Stack  if @Kevin Aban  or @Natalie Lusk can help with that.
- Record which had initial WD128 errors and see if it can be correlated to later failures. Start with EE investigation ones.
- Attach test data to NCR for failed units.
- Review other procedures for similar improvements. @Michelle Greenwald 
- Do the procedures for other processor programming need similar updates (FW AP, ADP, B30 ESCs, BMS, etc?

## Comments (3)

### Cameron Chapman, 2026-02-19

Abel notes: 
- 6320 Test would have failed. WD during loading burn in software. Link to project related to updating burn in test to latest FW. Reportedly new FW has not been verified to work with their test. Had several WDs during test. Test looks at runtime vs time in bake in. If runtime is less.
- Going to verify with production test details now,

### Ben Norris, 2026-02-19

@Abel J. Markow @Cameron Chapman I have attached the XCOMM processing procedures to this ticket. For all firmware version discrepancies between testing and newest release is just due to a lack of resources for proper regression testing that jumping to the newest version will allow for all processing/testing. Also I spoke with the technicians and we do need to change the burn in pass/fail description since the test has a minimum run time of 6 hours but a failure is if the uptime is less than the difference between the start and stop time of the test instead of the fixed 6 hours.

### Cameron Chapman, 2026-02-23

Talking to Ben about the burn in process. He says they tested and recreated that the 128 WD happens when hot mating the boot loader connector, not demating it. This also matches up with the process that was being used. 
 
He thinks the procedure says to do this when powered off, but old practices bypassed that step. He will check and confirm the procedure. 
 
 
 
I will track in JIRA
 
We will also investigate if there is correlation between this initial 128 WD and further occurrences/burn in failures, to see if that practice seems to be damaging processors

## Attachments (7)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [2120003-01 - Electronics - Xcomm Board (1607P01A) 1 - Build Procedure.pptx](attachments/44673_2120003-01%20-%20Electronics%20-%20Xcomm%20Board%20(1607P01A)%201%20-%20Build%20Procedure.pptx.md) | pptx | 114377 | 2026-02-19 | converted |
| [2120003-01 - Electronics - Xcomm Board (1607P01A) 2 - Initialization Procedure.pptx](attachments/44671_2120003-01%20-%20Electronics%20-%20Xcomm%20Board%20(1607P01A)%202%20-%20Initialization%20Procedure.pptx.md) | pptx | 4179 | 2026-02-19 | converted |
| [2120003-01 - Electronics - Xcomm Board (1607P01A) 3 - Burn-In Procedure.pptx](attachments/44672_2120003-01%20-%20Electronics%20-%20Xcomm%20Board%20(1607P01A)%203%20-%20Burn-In%20Procedure.pptx.md) | pptx | 73988 | 2026-02-19 | converted |
| [2127399-01 - Electronics - XCOMM Board, No CAN Resistor 1 - Build Procedure.pptx](attachments/44668_2127399-01%20-%20Electronics%20-%20XCOMM%20Board,%20No%20CAN%20Resistor%201%20-%20Build%20Procedure.pptx.md) | pptx | 111339 | 2026-02-19 | converted |
| [2127399-01 - Electronics - XCOMM Board, No CAN Resistor 2 - Initialization Procedure.pptx](attachments/44666_2127399-01%20-%20Electronics%20-%20XCOMM%20Board,%20No%20CAN%20Resistor%202%20-%20Initialization%20Procedure.pptx.md) | pptx | 4182 | 2026-02-19 | converted |
| [2127399-01 - Electronics - XCOMM Board, No CAN Resistor 3 - Burn-in Procedure.pptx](attachments/44667_2127399-01%20-%20Electronics%20-%20XCOMM%20Board,%20No%20CAN%20Resistor%203%20-%20Burn-in%20Procedure.pptx.md) | pptx | 73992 | 2026-02-19 | converted |
| image-20260223-233503.png | image | 439 | 2026-02-23 | listed only |
