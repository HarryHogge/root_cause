# XKIT-1716: SB40 Vehicle Power Switch

- **Issue type:** Epic
- **Status:** In Process
- **Priority:** Medium
- **Created:** 2024-04-02
- **Updated:** 2026-07-10
- **Reporter:** Cameron Chapman
- **Assignee:** Erik Hanson
- **Creator:** Cameron Chapman
- **Parent:** XKIT-2994 Develop Havoc Block 5 EWIS Design (PDR & CDR)
- **Links:** relates to VXEP-386 (Develop Replacement for AS150 Connections); relates to XKIT-760 (Main AS150 replacement issue-Develop new battery power connectors for Havoc Block 5); relates to XKIT-2038 (Decide if Havoc will have switchable aircraft power); relates to XKIT-2033 (Perform Market Survey/Down-Select, All Connectors); relates to SP-206 (Improve Power Connector, Contacts, and Signal Connectors); relates to VXEP-390 (Develop Anti-Spark Solution); is duplicated by XKIT-4080 (Design Main Power Switch); relates to XKIT-3486 (Determine HB5 Main Power Switch Wire Routing); blocks XKIT-3486 (Determine HB5 Main Power Switch Wire Routing)
- **Tech Lead:** Cameron Chapman

## Description

Files: https://jenaero.sharepoint.com/:f:/s/IRAD/EptnhS0cC0JFrURVP2U_eakBlgJOXtLJ5LSQ34En0OxuNw?e=ptqXgN 
Latest diagram New Startup State Diagram Block 40 - Power Button Commanding BMS FINAL
 EPS Havoc Block 5 Diagrams.pptx
Latest AA battery level diagrams saved to power systems tab of System Architecture Diagram, Block 35 (FKA Havoc B5).vsdx

## Issue Status

Multiple operators have suggested improvements to power switch behavior, but we have been unable to drive consensus on this. @Greg Fryer  or @Sam Miller may be able to decide where this is in priority and improved operations. 
CBP recommended improvements (none specified) https://jenaero.sharepoint.com/:w:/s/GlobalSupport2/IQAhDSqUEJ2xS4hcktakU1d4AbN1x1zql6SUr68TM_0E198?e=c0a789

## Comments (21)

### Artis Bertulis, 2024-04-03

I definitely want a power switch on the vehicle, I understand the safety reasons for it being on the tail, but I’m not a big fan of that location (or wings too for that matter), just because that would require relying on an additional part being installed and working to be able to power ON/OFF the vehicle, also not sure if there would be a risk of plugging in the tail and switching off the aircraft.
Although closer to the props, I’d like the switch to be on the fuselage and just not approach the vehicle if the center wing’s middle light is red (system armed). 
If there’s ever a case that we’d need to use that switch to power down an uncommand lift system operation, I’d rather not approach the vehicle regardless of the switch location.

### Cameron Chapman, 2024-04-10

@Laszlo Juhasz @Mark Squillante and @Rajesh Budhabhatti I think we need to get this and the power contact project moving for havoc. Are you available to divide up this work and work on it? Thank you.

### Rajesh Budhabhatti, 2024-04-10

Yes, I have some time before tomorrow afternoon when Dyno will be free. I’ll start looking into it.
Raj

### Mark Squillante, 2024-04-10

@Cameron Chapman @Rajesh Budhabhatti @Laszlo Juhasz can we set up a short meeting to discuss this in more detail?

### Cameron Chapman, 2024-04-10

@Mark Squillante yes, please schedule one. You are always welcome to send a meeting invite. We can reply if we think not needed or no time.

### Carl Graf, 2024-05-15

@Cameron Chapman @Mark Squillante any progress on this task?

### Cameron Chapman, 2024-05-15

@Carl Graf following up here https://jenaero.atlassian.net/browse/XKIT-2038

### Carl Graf, 2024-05-15

@Cameron Chapman can we consolidate this task into one ticket?

### Cameron Chapman, 2024-05-15

@Carl Graf it is a large project, so it will have many tasks. The linked ticket should really be titled “Decide if Havoc will have switchable aircraft power”. Changing it to that.

### Cameron Chapman, 2025-02-28

Archiving old description: 
Discussed with @Scott Stuckey. 
I think the best way to solve the anti-spark requirement will be to develop a power disconnect for all batteries and fuel cells. This could also help a lot with SD card corruption and other firmware issues by helping our systems shut down more gracefully. @David Grosher 
Terminology:
- Switch: the part the operator interacts with.
- Relay: The part that handles all of the currents and disconnects power.

Requirements:
- Need to have
- Minimize power loss.
- Ensure thermally stable in our vehicle OAT and with heat sources like the fuel cell or current through relay
- Nice to have.
- Help electronics shut down more gracefully. Ex: Small delay that sends signal to shut down before removing power.

Ideas:
- Switch
- Switch is on the tail (away from props). Normally open (so that we could still power up fuselage without the tail).
- Relay
- Would the most ideal place for these be in each battery and the fuel cell?  If not, it would probably be near those items.

Tasks:
- Get idea approved @Greg Fryer
- Concept design for switch and relay. Types, locations, connections, power calculations, etc.

### Hayden Jeanor, 2025-03-04

Purpose of switching 28V then 60V:
- prevents use from starting power without 60V
- allows only powering avionics while on the bench
- does not require user to be next to motors when power is initially applied
- but the user still needs to pitot press after power is applied
- safety requirement: mitigation against exposed voltage above 28V from shorting

### Cameron Chapman, 2025-03-13

Moving answered questions to here 
Questions: 
- Are there any vehicle actions that require a power cycle. Ex: updating FW, troubleshooting, etc. . 
- Currently for VSM flights customer is required to power cycle the vehicle between each flight. 
General troubleshooting often requires that, one example would be a pitot calibration failure during launch wizard - the pop-up asks to power cycle the vehicle. 
And as a safety measure if either lift system, fwd propulsion spins up, or even fuel cell fails and starts smoking - having a way to shut it down immediately without an over the radio link would be great.
- Have we ever needed an emergency shutoff switch? Yes for Havoc. Unsure for VXE30. Have needed power cycle often.
- Are there any shutoff requirements. Checking. See plan.
- Do we want to enable powering the avionics with a main battery only? This would make troubleshooting, ground test, programming, etc easier.  Cam thinks yes.

Greg asked: 
- Will the ESCs talk w/28V applied only, such that we can verify presence prior to 60V power application? ESC can be powered with as little at 15V (15V-60V)
- Is the switch more of an arm/disarm (e.g. allows power, but still won't go if software doesn't see the ESCs (no booms)), is that too complex in software? Maybe, but like you said, probably more reliable than a traditional switch.
- ---If not, how does the system prevent 60V power loss in flight if the switch fails? (e..g corrodes and shorts closed)
- ---If yes, how does the user force 60V off if the system lands but thinks it's still in flight? Is that even a serious issue?

 
In this chat, can we assemble a list of possible questions, make sure we have folks who can answer those in the working session, and then have the meeting? Cameron - can you take responsibility for collecting the questions and re-posting as we develop? Sounds good. I'll track them in the JIRA too, as we know how easy it is to lose info in chats

### Erik Hanson, 2025-04-15

Current status:
- Draft state diagram reviewed by product owners and sent out to AA
- Button types have been down selected and are on order
- AA was asked and agreed to create a Battery State Diagram to be reviewed by SLO - not complete

### Cameron Chapman, 2025-04-16

Asked on teams 4/16 and added above. 
Dave Grosher Erik Hanson apologies if I am repeating previous conversations. I will record the answer in the JIRA referenced earlier.
- would it be ok to remove the CW LED button once we install a power shutoff button to the B35 tail?
- Do we want/need the LED functionality of the CW button to indicate anything?
- What are other options to indicate vehicle power on? Could we change the logic for blinkers/nav to turn on when powered up and off on takeoff?

### David Grosher, 2025-04-16

@Cameron Chapman @Erik Hanson @Scott Whitney @Craig Burton  @Ted Trowbridge FYSA. 
I think the design scope has changed significantly since I reviewed this design a few weeks ago. I do not think it will be possible to have the operator turn on the 60V and non-critical 28V bus. I think these buses need to be automatically powered following the described checks and possibly a timeout. The current design will result in work and new interfaces across the OGCS (possibly the legacy GCS), VSM, XCOMM, and MB BMS.

I would propose the logic largely be contained to the MB BMS based on the power switch and CAN bus evaluation. The XCOMM can forward status messages to the GCS for some limited operator awareness.

### Cameron Chapman, 2025-04-16

@David Grosher Sounds good. I created this subtask to sort out and implement the plan. https://jenaero.atlassian.net/browse/XKIT-4323

### Tom Westrich, 2025-04-18

Initial switch actions discussed on 4/16 here: 
[embedded: image-20250418-101553.png]

### Tom Westrich, 2025-04-18

Updated battery state diagram here (original stored in System Architecture visio document).[embedded: 56V Battery State Diagram 20250418 (7fb784f2-28db-4959-89e9-675499a72482).pdf] .
@David Grosher @Cameron Chapman @Erik Hanson @Scott Whitney @Craig Burton @Ted Trowbridge , This state diagram is representative of our (TreeTown/Ann Arbor’s) understanding.  I think that with this architecture, we can be fairly flexible about the response actions to 1) physical installation of the batteries and 2) actuation of the tail switch.  After that, remaining control functions can be accomplished over CAN, or internally to the batteries.  However, I think it would be risky to have the battery decide when to start and stop 56V output; we should still rely on some A/V supervisory control to reduce the risk of unintended 56V shutdown.

### David Grosher, 2025-04-18

@Tom Westrich I have an interlock in the design from the avionics to provide an isflying flag on the CAN bus that should be FALSE before the bus is powered down. @Scott Hunter FYSA
For startup, I don’t think we can support the commanded 56v power up by May for the MVP. We could include that in the backlog possibly for a follow-on delivery.

### Tom Westrich, 2025-04-19

Open questions from TreeTown (Mike):
- If the battery is in CRITICAL (i.e., 28V critical on), is there any need to move back to MONITOR (CAN transceiver on)?  Or should the battery simply move back to OFF (low power sleep)?
- If it does not matter, the battery could stay in MONITOR (instead of OFF) in any of these cases, and then have a auto timeout to default to OFF if no commands are received in a [TBD] period?
- If the battery is in CRITICAL (i.e., 28V critical on), what action does the switch provide?
- If the battery is ON (all outputs on), should the battery ignore all switch activity, relying on CAN commands to change state?  Do we need any other protections to keep a false switch action from opening 56V?
- This is not blocking hardware development/ordering, but will block software development: Where does the software to evaluate if the 56V circuit should be closed reside?  
- Note, I suppose that this would impact hardware development if the route for detection includes some kind of impedance test?
- Can we avoid all of the software evaluation by routing the switch wiring through each of the CWJ1/P1 and CWJ2/P2 connections before it hits the tail switch?  It seems like we have extra pins available in each of the relevant connectors.  With this design, a closed switch circuit would automatically allow the batteries to detect that all 56V elements are engaged, and then we could either
- Start 28V Critical only and wait for AV CAN command to turn on 56V
- Start 28V Critical only and evaluate CAN traffic to determine if 56V can be enabled
- Start 28V Critical only and wait [TBD] seconds before enabling 56V (without external CAN commands)
- Start all outputs immediately

### Carl Graf, 2025-08-11

@Erik Hanson any updates to this ticket? I think some of the Child Tasks are complete. Please update and tag me. Thanks!

## Attachments (7)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image002.png | image | 4 | 2024-04-10 | listed only |
| image003.png | image | 1 | 2024-04-10 | listed only |
| ~WRD0000.jpg | image | 1 | 2024-04-10 | listed only |
| [MIL-HDBK-454 High Voltage (30+VDC).docx](attachments/27181_MIL-HDBK-454%20High%20Voltage%20(30+VDC).docx.md) | docx | 170 | 2025-03-14 | converted |
| [56V Battery State Diagram 20250418 (7fb784f2-28db-4959-89e9-675499a72482).pdf](attachments/28314_56V%20Battery%20State%20Diagram%2020250418%20(7fb784f2-28db-4959-89e9-675499a72482).pdf.md) | pdf | 223 | 2025-04-18 | converted |
| [56V Battery State Diagram 20250418.pdf](attachments/28313_56V%20Battery%20State%20Diagram%2020250418.pdf.md) | pdf | 223 | 2025-04-18 | converted |
| image-20250418-101553.png | image | 131 | 2025-04-18 | listed only |
