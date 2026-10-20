# VXEP-944: VXE 614 Erratic behavior and propulsion failure led to crash

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2025-01-31
- **Updated:** 2026-05-08
- **Resolved:** 2026-05-08
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Drew Hildreth
- **Creator:** Alexander Alan Arnold
- **Labels:** GS_Closed, TIQUILA, Weekly-incident-tracker
- **Parent:** VXEP-573 Sustainment: VXE30 Incident Investigation
- **Links:** relates to RMA-551 (VXE-614 RMA 250305-1); relates to ENG-346 (1607P01A Improvements. XCOM / XE240 PWR COMMS BD); relates to VXEP-1307 (SB40x - N376VX: Network Issue); relates to VXEP-1310 (VXE689 - Network Issues); relates to XKIT-4730 (SB40x - N376VX: Network Issue); relates to XKIT-5360 (B40 913 Crash (2026/03/04))
- **Customer:** TIQUILA
- **Vehicle Tail Number:** VXE 614
- **Vehicle Configuration:** Standard Battery configuration
- **Problem Type:** Discovered Issue
- **Issue Status:** 11/4 Report sent to customer. Waiting to hear back
- **Incident Type:** Aircraft Loss
- **Severity:** 1 - Flight Critical

## Description

Main PowerPoint 
Chipset Investigation Updated VXE614 Chipset Customer Report.pptx


Sharepoint https://jenaero.sharepoint.com/sites/FlightSafety/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FFlightSafety%2FShared%20Documents%2FActive%20Cases%2FVXE614%20%2D%20Crash%20After%20Takeoff (in progress).
TIQ Operator statement
The intent of the sortie was to operate the system progressively out to 10km iaw the current LEC on area and was briefed and authorised accordingly. The detachment was well rested and ready to fly and the met conditions were within limits (light winds, nil cloud, good visibility)
 
The first Launch Wizard was successful up until the point of the motor check. At this point, the A/C failed to arm the motors during Launch Wizard. The Launch Wizard was subsequently cancelled and restarted. The GCS then received a warning displaying words to the effect of “Centre Wing not detected, ensure centre wing is connected securely before attempting Launch Wizard”. The A/C was disconnected, the centre wing removed, and power cycled to the A/C. The Launch Wizard was then passed successfully, and the A/C was launched iaw SOPs. The A/C conducted a successful VTOL take off at 14:03 and transitioned to fixed wing flight at approximately 150 - 200ft. Almost immediately upon transitioning, the A/C entered a sharp left-hand turn. The GCS indicated that the A/C had failed to intercept WP1 and was trying to turn around in order to make its way back to WP1. The A/C then began to behave erratically, conducting left and right hand turns before attempting to climb vertically. The pilot was instructed to command the A/C to “go to” Orbit 2 in order to allow the system to settle and for the crew to determine their next actions. The aircraft continued to fly erratically, and the pilot was instructed to command “go to” IP1 (the start of the recovery leg) in order to attempt to recover the aircraft. Upon receiving the command “go to” IP1 the aircraft appeared to fly as instructed and in a safe manner. Upon intercepting IP5 (the point at which the A/C transitions to VTOL mode) the A/C looked to transition to VTOL; however the VTOL motors appeared to failed to engage fully, and the A/C continued forward flight with no Main propulsion. At this point the “Failure to transition to VTOL” Emergency Procedure Immediate Action was carried out iaw the current Flight Reference Cards and the A/C was commanded to “Orbit Here Now”. The A/C main Propeller failed to engage causing the A/C to fail to maintain forward momentum and hold altitude. The A/C entered an orbit flight profile whilst decreasing in height. At this point the A/C was observed to lose safe separation with the ground causing it to impact approx 200m from the planned point of recovery at 14:09hrs. All component parts of the A/C were recovered and the A/C, GCS and Main Battery/HLB have been appropriately quarantined. An attempt was made on two occasions to get the data from the Flight Data Recorder (FDR); however, a pop up message displayed stating “FDR Retrieval Error”

## Corrective Action

Aircraft Dispo@Rodney Linch 5/12/25 Please replace:
- Left aileron servo motor and ESC, left aileron servo boost board, left servo mechanical linkage, related harnesses.
- Xcomm pcb, FWAP pcb, FWAP gps pcb, Xcomm harness to CW, CW harness to left aileron.
- VBatt to CW harness.
- Replace harness VTOL to Xcomm.
- VTOL and VTOL interface pcb (esd precaution)
- Left aileron/wing tip mechanical structure.
- Left Boom 4pin harness to wing tip.

@Rodney Linch please hold off on replacing the above. Customer desires root cause first. (asked if still true 5/21). 614 is being scheduled with production to be repaired.
- Processes Implemented, but after this equipment was shipped. ​
- Improved handling and storage of electronic assemblies and components. ESD, humidity, bake outs, assembly improvements, etc.​
- Partially implemented. Improvements ongoing​
- Ensure chipsets are ESD safe, humidity compliant, and processed properly throughout supply chain. https://jenaero.atlassian.net/browse/ENG-2957  ​
- Longer term, potential architectural changes: ​
- Planned PCB Updates: ​
- Update so that critical power supplies cannot be disabled. Evaluate adding front end protection to 3.3V regulator, separating critical and non critical PCB power supplies, add redundance, etc. Added to here https://jenaero.atlassian.net/browse/ENG-346  ​
- Increase BIT and other automatic health checks, ​Added to roadmap https://jenaero.atlassian.net/wiki/x/DACLKw

Firmware Corrective Actions​
- Near Term​
- Re-evaluate logic that caused false “landed”/”launched” states to occur during fixed wing flight. Implement changes to prevent future occurrences. (Note: this happened due to the low registered airspeed and ground speed during the large pitch oscillations). STATUS: Not Started, does not pose critical risk to the aircraft.​
- Long Term​
- Given the state of the aircraft an automated abort to FW glide ELZ could have been possible. Re-evaluate logic to determine if this can be done consistently and safely (given the system should be slowing down in this state this may be dangerous). Additionally, consider using fixed wing IMU data to trigger attitude faults that begin landing aborts. STATUS: Not Started, needs further analysis and design as this automation would pose risk to the system during a transition phase when the aircraft is actively slowing down below stall speeds.


Voltage Transients Added to https://jenaero.atlassian.net/browse/VXEP-944 
•Voltage transients are inherent in aerospace and circuits should be designed with overvoltage protection
•XCOMM PCB improvements:
•Remove direct connection of IN_PWR_SEL & MDIX (most damage observed) to the 3.3V supply by adding series resistance and capacitive filtering
•Add overvoltage protection to the 3.3V supply, which supplies critical components on the XCOMM PCB
•Stalker Block 40 improvements:
•Critical and non-critical power separation
•Motor (propulsion) bus isolated from 28V bus via DC-DC converter
•Robust grounding architecture to help mitigate EMI noise
28V Hot Mating (Without Anti-Spark)
•Remind operators about standard assembly procedures and cations not to hot mate certain connections.
•Stalker Block 40 can be fully assembled before power is enabled and includes switches for payloads to prevent hot mating without anti-spark
•Review and update operator manuals for clearer guidance not to hot mate. @Josh Burrell

## Plan

@Drew Hildreth  I updated the CA tasks. Has the customer accepted the presentation? Do we have any more actions for this?

## Root Cause

Possible root cause is a VTOL or VTOL ESC or in circuit wiring intermittent low resistance short condition.  27.5@20A 1.375 ohms if single phase.

## Comments (50)

### Alexander Alan Arnold, 2025-01-31

This incident has just been brought to our attention. we are working with the customer to retrieve data and equipment at this time and will upload the files once we have them. @Greg Fryer

### Greg Fryer, 2025-01-31

@David Grosher Suspect we will need analysis of the logs first. Could of course be a hardware issue with the VTOL, but I’m shifting it over to you for starters. Note no FDR yet (@Pat Wells mentioned in email he is working with them to get the FDR)
@Alexander Alan Arnold FYI.

### David Grosher, 2025-02-03

@Alexander Alan Arnold @Eric Brewer @Pat Wells Data uploded

### Pat Wells, 2025-02-03

@David Grosher attached data provided by customer

### Cameron Chapman, 2025-03-06

@Steve Gonzales this equipment arrived today. Can you please review the investigation and inspect it?

### Rodney Linch, 2025-03-06

@Steve Gonzales - both cases brought to engineering area. RMA intake complete.

### Pat Wells, 2025-03-11

@Cameron Chapman Are there any updates on this?

### Cameron Chapman, 2025-03-11

@Steve Gonzales TIQUILA meeting tomorrow. Can you please coordinate investigation today?

### Jason Scherer, 2025-03-11

@Alexander Alan Arnold If we could get GCS logs that would be helpful as well.

### Alexander Alan Arnold, 2025-03-11

This happened almost 6 weeks ago is the data still going to be there?  And can you send me the file path you want the data from @Jason Scherer

### Adrian Garcia, 2025-03-11

@Cameron Chapman I helped @Steve Gonzales with initial inspections today on the aircraft. Here are my gatherings as of now: 
- Servos are working as intended
- I tested the servos with a servo controller and they responded accordingly
- Since servo1 was showing the transient, I set up the right side of the aircraft to measure continuity on signals SERVO1, RAIL, and GND_AIL

Next steps: 
- Hook up XCOMM to Iron Bird and check for: 
- ethernet connection 
- update: AV Box connected to webpage
- How servos respond to AV box movement (look more at right aileron)  
- Update: servos responded as expected

### Jason Scherer, 2025-03-11

@Alexander Alan Arnold Disregard, I didn’t realize this was an incident we had already investigated pretty far. I thought this was an investigation we hadn’t started yet. 

The GCS would have prompted to create an AAR even if the vehicle wasn’t connected. So, unless they deleted it, the AAR would still be on the GCS that was used for the flight.

### Adrian Garcia, 2025-03-13

I could not replicate the I12V and netS1P4SaCam seen in the incident on the Iron Bird. Here are my findings: 
[embedded: image-20250313-164918.png]
[embedded: image-20250313-164933.png]
I may have understood the experiment that was asked of, but I physically disconnected the the center wing harness and the SaCam ethernet connector off the VTOL Interface board. 

 @Cameron Chapman

### Pat Wells, 2025-03-17

@Adrian Garcia @Steve Gonzales any further updates on this? I’ll be briefing the customer tomorrow 18 March and they will ask.

### Steve Gonzales, 2025-03-17

@Pat Wells Yes, the update is the regulator circuit around U26 on the XComm pcb is suspect.  That circuit provided unstable power to the VTOL board.  Load testing is planned for this week.

### Pat Wells, 2025-03-24

@Steve Gonzales checking in for updates.  Will be briefing customer tomorrow morning.

### Steve Gonzales, 2025-03-24

3/24/25 Update, some noise is present on the 12.8VDC line from U26 but is generally stable with a load.  Working on other items this week and did not have a dedicated resource to continue.
[embedded: image-20250324-233129.png]

### Steve Gonzales, 2025-03-25

3/25/25 @Giovanni Gonzalez @Adrian Garcia IPC level inspection of regulator circuit. Load to 7W for 20min min duration and scope. Inspect wiring to VTOL. Measure R from reg to VTOL.  pls complete by 3/26/25

### Giovanni Gonzalez, 2025-03-25

12.8V regulator to VTOL unloaded: 
[embedded: VXE614 12.8 Regulator Unloaded Waveform.png]
12.8V regulator to VTOL with 7W load for 20 min:
[embedded: VXE614 12.8 Regulator with load Waveform.png]
12.8V Air regulator unloaded:
[embedded: VXE614 12.8 Air Regulator Unloaded Waveform.png]
12.8V Air regulator with 7W load for 20 min:
[embedded: VXE614 12.8 Air Regulator with load Waveform.png]
@Steve Gonzales

### Pat Wells, 2025-03-31

@Steve Gonzales any updates?  We have a customer brief tomorrow morning.

### Giovanni Gonzalez, 2025-04-01

[embedded: 12.8V Xcomm Regulator Cont..jpg]
[embedded: 12.8V Xcomm Regulator Inductor.jpg]
[embedded: 12.8V Xcomm Regulator Inductor 2.jpg]
[embedded: 12.8V Xcomm Regulator U5.jpg]
[embedded: 12.8V Xcomm Regulator.jpg]
From manual inspection and images of the 12.8V Xcomm Regulator there does not appear to be any cold solder joints or visible defects on the hardware. Vibration testing will be performed tomorrow 4/2/25

### Giovanni Gonzalez, 2025-04-01

[embedded: 12.8V Air PWR Regulator 3.jpg]
[embedded: 12.8V Air PWR Regulator 2.jpg]
[embedded: 12.8V Air PWR Regulator.jpg]
12.8V Air PWR regulator which goes to CW does not show any visible defects

### Pat Wells, 2025-04-02

@Steve Gonzales is there an ETA for completion of the report?
Thanks

@Drew Hildreth FYSA

### Steve Gonzales, 2025-04-02

@Pat Wells I was planning on troubleshooting the hardware until the weeks end then we can have a call on Monday am to determine next steps.  Did you need a complete ppt report before then in its current state?  Or we can finish the report based on our troubeshooting this week and have it ready for your review by eob 4/7?

### Pat Wells, 2025-04-02

@Steve Gonzales understood. I will plan to review 4/7 EOD.  Thanks

### Pat Wells, 2025-04-07

@Steve Gonzales reminder that the customer is expecting the report tomorrow.  

@Cameron Chapman  FYSA

### Cameron Chapman, 2025-04-07

@Pat Wells are they expecting a complete investigation and report tomorrow, or a report that shows progress and reflects the latest status and next steps by tomorrow? FYI @Steve Gonzales  Moving to teams for quicker responses.

### Cameron Chapman, 2025-04-08

Pasting complete items from plan field. 
- Added 3-10 ideas and next steps 4/4
- Update ppt and these fields every time an investigation is worked. This investigation will likely have to be summarized and presented to the customer Tuesday.
- Inspect servo and adjacent moving parts. Look for clearance of moving surfaces vs normal. Report if abnormal if not.
- Vibration of XCOM and harness, or whole vehicle.
- It isn't super clear from a quick review of the timeline. How do the spikes on the 12/6V busses compare to when the VTOL AP loses connection. It seems very possible that the VTOL motors kicking on or changing throttle sharply could create power/transient issues to a similar effect.
- Abel may have some evidence of this happening in other scenarios. We could have him look at this data and circuit. (Spikes are from ESC/Motors probably not servo motor)
- Supported by this statement in the ppt "Left side throttles increase significantly just before VTOL motors power off (indicates roll imbalance)"
- I noticed the VTOL AP stops during transition ~10 seconds after the FW abort, transition to VTOL. We have had a lot of issues during transition. 
- Both CAN devices stop responding at the same time, indicating power fault. If
- Inspect for the following:
- signs of stuck servo
- use a servo controller to control servos
- issues that would cause a VTOL power fault,
- connector or wire 
- Measure GND_AIL, SERVO1, SERVO2, LAIL, and RAIL from black Alden Connector to center wing boom connector
- If there is continuity Servo lines are fine
- If there is no continuity, isolate to where continuity is lost
- VTOL or XCOM PCB damage 
- inspect VTOL PCB
- Inspect XCOM PCB
- hook up Avionics box to Iron bird and remote control aileron servos
- Measure Servo1 PWM signal from the source and to the end of the Boom
- Recreate this test on the ironbird. Does SA cam losing ethernet link would cause it to draw less power (less traffic), or will it keep trying to stream even if nothing is receiving it? If the former (my guess) this plot could support the loss of power bone. We could measure on the ironbird normal operation, ethernet unplugged, and CW disconnected and compare logs. (maybe finally figure out why logs oscillate so much while we are at it). Do we have blinker status logged? I am curious if that is what causes these oscillations
- @Giovanni Gonzalez  are you able to coordinate this testing on the ironbird?
- [embedded: image-20250206-233902.png]
- Test servo position if pwm or power removed (when commanded up before)
- If the servo was hard over it was likely plugged into power but getting a bad pwm signal - although i don’t know that for sure.  It went 100fps so i’d assume it would backdrive toward neutral if completely unpowered
-

### Pat Wells, 2025-04-10

@Steve Gonzales @Cameron Chapman is there anything discovered so far that would indicate operator error or poor maintenance? 
Customer is asking a getting aircraft repaired / replaced.

### Adrian Garcia, 2025-04-10

@Steve Gonzales here is the link to all the photos we took today - V614 - adrian.zip

### Steve Gonzales, 2025-04-10

@Pat Wells @Cameron Chapman Adrian and I have found the failed component.  It was the ethernet switch 1 IC on the Xcomm board that failed, possibly from an ESD event, processing step or other TBD.  Report update planned for 4/11.  I will mssg. you when complete for review.

### Steve Gonzales, 2025-04-15

@Pat Wells I added slide 29 for your review. Correlation with the erratic flight behavior and overall crash still in process. It is possible there is a second/corresponding failure mode we have not yet found.

### Steve Gonzales, 2025-04-18

@Pat Wells Updating power point for review by early Monday the 21st.

### Steve Gonzales, 2025-04-21

@Pat Wells @Cameron Chapman @David Grosher Please review 614 PPT and let me know thoughts / what needs to be improved before the customer call tomorrow.

### Pat Wells, 2025-04-21

@Steve Gonzales acknowledged and reviewing now.

### Rodney Linch, 2025-04-29

@Steve Gonzales - we picked up 614’s fuselage and wing cases. The fuselage case is missing the fuselage.  Can you point me in the right direction as to where I may pick it up?

### Steve Gonzales, 2025-04-29

@Rodney Linch Hi, 2 days ago it was just to the right of the rightmost HIL bench in engineering.  It may have moved but should be in that general area.  I will look around later today.

### Rodney Linch, 2025-04-29

@Steve Gonzales we picked up the cases. The fuselage is missing its avionics box.  Can we get that as well?

### Rodney Linch, 2025-05-07

@Steve Gonzales - I scoured the area and didn’t see it.  Let me know if you find it!

### Cameron Chapman, 2025-05-21

Moving old info from fields above. 
Plan:
Investigation Paths
Servo Function Investigation Plan:​
- Manually block servo movement. Measuring 6.1VDC line for pulses and possibility to interfere with VTOL power or function. Try recreate spikes seen on servo bus with other scenarios. Ensure logging rates match data​
- Simulate effect of failed servo and see if it could create failure modes like this. Production has seen stuck servos approximately 1/50. ​
- Run servo through in-house test procedure developed with servo OEM. Testing planned EOB 4/8/25. 
- Test ran by Nigel Goodison, left aileron servo passed with no issues
- Perform visual internal inspection. We have approval to open per Nigel Goodison – QC.

VTOL AP Power Fault Investigation Plan:​
- Recreate i12V data​
- Power V614 Avionics box and CW and physically disconnect ethernet to the SaCam (J31 on VTOL interface board) and the CW Harness. ​
- Power V614 Avionics box and Center Wing and vibrate CW and try to create an intermittent connection and capture netS1P4SaCam and I12V.​
- Investigate source of i12V oscillation. Record results in the data log glossary. Compare to other flights and ironbird. ​
- Do we have logs of blinker status. It powers SA cam and blinkers. Suspecting blinkers causing current oscillation. ​
- Review data for possible anomalies caused by VTOL motor power ​
- Abel may have some evidence of this happening in other scenarios. We could have him look at this data and circuit. (Spikes are from ESC/Motors probably not servo motor)​
- Supported by this statement in the ppt "Left side throttles increase significantly just before VTOL motors power off (indicates roll imbalance)"​
- 4/4/25 Steve 
A.  Perform insulation analysis of motor windings, ESC and harness with a megger scheduled for 4/8.
B.  Vibe if necessary to induce failure mode, scheduled for 4/10 or 4/11.

General Checks from deep dive 4/9/25:
- Investigate build of 26 pin ODU - Adrian/Gio
- Solder Cup to Solder Cup distance on back shell/ solder to solder cup distance
- Use megger to test the potential between solder joints on 26 pin ODU
- Pull 52 pin Alden connector 100-107311 from inventory for testing
- For signals go to around 300V with the megger
- For power Steven will come up with limit
- Production test of fuselage signal harness and CW connector 
- obtain resistance report of test
- Preflight ground checkout
- Determine how VTOL motors are read during preflight check. - Steve
VTOL motors are not read during preflight spin up, visual check only.
- Determine if ailerons are checked - Steve
Ailerons, rudder and elevator are checked through visuals only.
- Confirm power draw of esc matched throttle during flight
- Right after it took off and was in forward flight aircraft detected a landing - Steve
May be triggered by low airspeed, or X.  Data path of CAN Bus is from VTOL AP to Xcomm and back to VTOL AP, connection may have been intermittent to allow for comm in one instance and not in another.
- Possible FWAP/ magnetometer board issue
- Run FWAP board through production testing - Gio
- Produce new chart for vibration PPT slide 24 - Steve
Added chart with Xcomm timing.  High vibration before lost communication occurred.
- Confirm blinker modes with Jason - Steve
Blinkers by default are off during take-off and fwd flight, turning on during landing.  They also can be manually turned on.  No other modes readily available.

Xcomm Failure Found, Investigation Plan 4/10/25:
Xcomm was powered up with U5, U26 at 0.2V, U18, U19, U25 at 0V, U3 low at 2.0V.  Suspect failed soler/component or FOD around 3.3VDC circuit U3 regulator or U24 microprocessor.
- Thermal camera Xcomm board.
- Inspect 3.3VDC U3 circuit, connections and U22 reference voltage.
- Measure voltage on enable lines.
- Check for FOD on U26.
- Replace U3.

Status:
4/17/25 Moving task slide from ppt to here:
1.Inspect servo and adjacent moving parts. Look for clearance of moving surfaces vs normal. Report if abnormal if not.
2.Artificially blocking servo. Measuring pulses and possibility to interfere with VTOL power or function.
3.Vibration of XCOM and harness, or whole vehicle.
4.May be able to open up servo and inspect. Need to check if we have any proprietary restrictions against this. Check with supply chain.
5.Simulate effect of failed servo and see if it could create issues like this.
6.It isn't super clear from a quick review of the timeline. How do the spikes on the 12/6V busses compare to when the VTOL AP loses connection. It seems very possible that the VTOL motors kicking on or changing throttle sharply could create power/transient issues to a similar effect.
1.Abel may have some evidence of this happening in other scenarios. We could have him look at this data and circuit. (Spikes are from ESC/Motors probably not servo motor)
2.Supported by this statement in the ppt "Left side throttles increase significantly just before VTOL motors power off (indicates roll imbalance)"
7.I noticed the VTOL AP stops during transition ~10 seconds after the FW abort, transition to VTOL. We have had a lot of issues during transition. Is there any sequence of firmware commands or states that could end in a locked processor, or is it much more likely primarily hardware? Would we have evidence of that if so?

3/11/25
Servos tested using servo controller and they responded accordingly. They do not seem stuck. 
Servo1 line power had continuity all across the aircraft. 
No physical debris present on aileron.
3/31/25 @Pat Wells 
Initial HW testing was not able to replicate failure modes seen, due to amount of time spent, test equipment available, and test method maturity.  The below corrective actions are intended to reduce the highest probability failure modes understood by the current evaluation performed by FW/HW.  Replacing the below seeks to reduce failures by:
- Right aileron stuck:  Lowers risk of failure due to intermittent connection at the servo motor and boost board.  Lowers risk of a faulty motor/boost board.  Eliminates risk of an out of spec mechanical dimension or movement by the aileron linkage.  Harness change lowers the risk of a cabling short/open/high resistance.
- Loss/Noisy CW power:  Lowers risk of failure of power to the CW from the Xcomm and signal connections.
- Boost board V spikes:  Lowers risk of spike caused from a VBattt feed connection issue.
- False landing: Lowers risk of loss of serial communication between Xcomm and FWAP.
- ADP power/communication:  Lowers risk of communication/pwr issue between the ADP and VTOL and Xcomm.

4/4/25
Completed tests:
PCB inspection around U26, U5, U1, Xcomm general, VTOL general, FWAP general, Harness connection points from above 1-5, vibrated booster board 25,50,75,100Hz while monitoring 6.1V output to left aileron and actuating, monitored 12.8 output of Xcomm to VTOL pcb at VTOL while vibrating harness at connection with the aforementioned frequencies. Monitored current draw on 28V main while physically moving harnesses.  PWM monitored to left aileron.  Jason updated the timing to match between xcomm and vtol and improved some slides.
4/9/25
XCOMM did not connect to webpage and upon closer inspection the majority of the power LEDs did not turn on. This means that a component within the buck’s circuitry was failing. Most notably, the 12V regulators that go to the SaCam and the Vtol Int board were reading 200mV. See https://jenaero.sharepoint.com/:x:/r/sites/FlightSafety/_layouts/15/Doc.aspx?sourcedoc=%7B5BE081FE-49CD-4168-BF88-FDC230682D53%7D&file=V614%20Regulator%20Outputs.xlsx&action=default&mobileredirect=true  for more info

### Steve Gonzales, 2025-10-07

Submitted customer report for review on 10/1/25

### Cameron Chapman, 2025-11-04

@Drew Hildreth  I updated the CA tasks. Has the customer accepted the presentation? Do we have any more actions for this?

### Drew Hildreth, 2025-11-04

@Cameron Chapman Dhruti responded with the following… 


- What does at next Revision mean and is there a timeline? I told her that there is no current timeline for a Revision
- Of the improvements articulated in Slide 11, are any of these likely to be implemented for VXE30? I owe this.. how would you like me to respond?
- Do EA have an idea of when the Operator Manuals will be updated to cover ‘Hot Mate’? This is already covered in the manual. Looking to clarify on next release.
- Do EA recommend any additional inspections/actions in the interim for VXE30? I told her no, because the card in internal to the Avionics and they can’t open that, nor would they be able to see it if they tried.

### Cameron Chapman, 2025-11-04

@Drew Hildreth 
Of the improvements articulated in Slide 11, are any of these likely to be implemented for VXE30? I owe this.. how would you like me to respond?
- We are targeting to implement these and other improvements with unified autopilot, but with a small, heavily loaded team, there is a decent chance that the XCOM board will not be updated in the initial version of that. We do not have timeline and scope finalized for that yet. You are welcome to call if easier to discuss.

### Cameron Chapman, 2025-11-04

@Cameron Chapman It also depends how you define VXE30. Such changes might be categorized as a VXE30 successor depending on the scope (B31 potentially)

### Cameron Chapman, 2026-03-06

@Madeleine Masiello there was a suspected servo fault at the start of this timeline. Now that we have info on servo issues, are you able to find and report the servos involved in this crash and test them according to the latest pegasus guidance?

### Madeleine Masiello, 2026-03-09

@Cameron Chapman RMA has informed me and confirmed that VXE614 has been sourced and went back to the customer 12/01/2025

### Cameron Chapman, 2026-03-31

Talked to Maddie. Unable to find servo in engineering.

### Christa Meck, 2026-05-06

@Drew Hildreth @Cameron Chapman @Alexander Alan Arnold  What is needed from the CCB on this item?

### Christa Meck, 2026-05-08

Per conversation with @Drew Hildreth This Incident work item can be closed as the aircraft has been returned to the customer.  
The Team is still interested in tracking the XCOMM improvements outlined in https://jenaero.atlassian.net/browse/ENG-346 as some of them are corrective actions from this Incident.
This work item is linked to https://jenaero.atlassian.net/browse/ENG-346 and those XCOMM improvements can be monitored there.

## Attachments (37)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| Screenshot 2025-01-31 111926.png | image | 598 | 2025-01-31 | listed only |
| Screenshot 2025-01-31 112006.png | image | 847 | 2025-01-31 | listed only |
| Screenshot 2025-01-31 112016.png | image | 379 | 2025-01-31 | listed only |
| VXE614_AAR_data (49ade98d-7341-418e-b15c-e0de7b612ad3).zip | archive | 82667 | 2025-02-03 | listed only |
| VXE614_AAR_data.zip | archive | 82667 | 2025-02-03 | listed only |
| image-20250313-164918.png | image | 28 | 2025-03-13 | listed only |
| image-20250313-164933.png | image | 28 | 2025-03-13 | listed only |
| image (13).jpg | image | 52 | 2025-03-24 | listed only |
| image-20250324-233129.png | image | 496 | 2025-03-24 | listed only |
| VXE614 12.8 Air Regulator Unloaded Waveform.png | image | 50 | 2025-03-25 | listed only |
| VXE614 12.8 Air Regulator with load Waveform.png | image | 55 | 2025-03-25 | listed only |
| VXE614 12.8 Regulator Unloaded Waveform.png | image | 42 | 2025-03-25 | listed only |
| VXE614 12.8 Regulator with load Waveform.png | image | 42 | 2025-03-25 | listed only |
| 12.8V Air PWR Regulator 2.jpg | image | 6749 | 2025-04-01 | listed only |
| 12.8V Air PWR Regulator 3.jpg | image | 6723 | 2025-04-01 | listed only |
| 12.8V Air PWR Regulator.jpg | image | 6945 | 2025-04-01 | listed only |
| 12.8V Xcomm Regulator Cont..jpg | image | 6924 | 2025-04-01 | listed only |
| 12.8V Xcomm Regulator Inductor 2.jpg | image | 6797 | 2025-04-01 | listed only |
| 12.8V Xcomm Regulator Inductor.jpg | image | 6585 | 2025-04-01 | listed only |
| 12.8V Xcomm Regulator U5.jpg | image | 6714 | 2025-04-01 | listed only |
| 12.8V Xcomm Regulator.jpg | image | 6819 | 2025-04-01 | listed only |
| VXE 614 Hardware Images.zip | archive | 74068 | 2025-04-07 | listed only |
| VXE 614 Test Setups.zip | archive | 7092 | 2025-04-07 | listed only |
| VXE 614 Waveforms.zip | archive | 258 | 2025-04-07 | listed only |
| image-20250206-233902 (d2bdb7fe-dc32-46f1-b2c0-584d11dc5688).png | image | 78 | 2025-04-08 | listed only |
| [FR-2505055.pdf](attachments/29899_FR-2505055.pdf.md) | pdf | 22544 | 2025-06-13 | converted |
| [SolderIronResistanceValues.xlsx](attachments/30463_SolderIronResistanceValues.xlsx.md) | xlsx | 9 | 2025-07-09 | converted |
| [IPC-TM-650.pdf](attachments/30534_IPC-TM-650.pdf.md) | pdf | 29 | 2025-07-11 | converted |
| ansi s20.20 levels.jpg | image | 167 | 2025-07-15 | listed only |
| as150 1.jpg | image | 1431 | 2025-07-17 | listed only |
| as150 2.jpg | image | 1682 | 2025-07-17 | listed only |
| as150 3.jpg | image | 1360 | 2025-07-17 | listed only |
| as150 4.jpg | image | 1459 | 2025-07-17 | listed only |
| as150 5.jpg | image | 1682 | 2025-07-17 | listed only |
| as150 6.jpg | image | 1756 | 2025-07-17 | listed only |
| as150.jpg | image | 1631 | 2025-07-17 | listed only |
| [List of item to replace.docx](attachments/33188_List%20of%20item%20to%20replace.docx.md) | docx | 115 | 2025-10-20 | converted |
