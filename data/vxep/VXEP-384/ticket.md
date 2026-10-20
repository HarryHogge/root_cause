# VXEP-384: VXE 545 Commanded aborted launch due to unusual behavior on ascent

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2024-04-29
- **Updated:** 2026-03-02
- **Resolved:** 2025-08-05
- **Reporter:** Pat Wells
- **Assignee:** Rajesh Budhabhatti
- **Creator:** Pat Wells
- **Labels:** TIQUILA, Weekly-incident-tracker
- **Links:** relates to RMA-279 (VXE-545 ESC/Motor RMA 240701-1); relates to VA-221 (Evaluate using Havoc escs on vxe. ); relates to XKIT-2503 (Test 5V Enable Solutions on Xkit nose cone with production Hargrave ESC (p/n: 100-114708)); relates to VXEP-198 (VXE450 Implement CA: Procurement Evaluate/Order new datecode FDMS86540 MOSFETs (IPN: 100-110341)); relates to ENG-3034 (Aircraft 450 VTOL Landing Crash-ESC Damage)
- **Customer:** TIQUILA
- **Vehicle Tail Number:** 545
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

## 1.1        Operator Description of the Incident

The trials team arrived on location at approx. 0845 to set up the GCS and support equipment for the day's flying. As we were operating in a new location a magnetometer check was carried out and a subsequent magnetometer swing completed. Following this the UA was used for ground testing for approx. 2 hrs. For the ground testing only the payload and main battery were fitted. On completion of the ground testing the UA was fully assembled with all pre-flight checks and GCS launch wizard completed successfully. These checks include motor checks for all 4 VTOL lift motors and main motor, pitot-static checks, payload operation and control surface operation. The immediate area around the UA was cleared (out to 30m) and it was confirmed that all trial pers and support pers were in the designated area. With no indication of issues or faults the command was given to launch the UA. On launch, the UA's VTOL motors spun up and lifted the UA clear of its cradle, approx. 3ft above ground, but the UA appeared to be underpowered and unstable. The UA then dipped its right wing and travelled backwards (either being blown by the wind or following its automatic abort profile). The right-wing tip impacted the ground and dragged until the aircraft settled on the ground (prior to the RP's commanded abort). The command was given to abort the take-off which the RP carried out using first, the hand controller and then the Ctrl-A keyboard shortcut until the rotors stopped spinning. The UA was made safe and returned to the cradle. The UA was inspected for damage with preliminary minor damage found of the right-wing tip and payload housing. The launch wizard was carried out as a post flight activity and all systems functioned correctly. As the reason for the UA's behavior was still unknown and further investigation required the UA, payload, and batteries were quarantined. The planned sortie was subsequently flown with our second UA without incident.
# 2        Summary

During a flight test lift-off, the aircraft did not execute a vertical take-off but instead it dragged backwards and failed to lift off. This was caused by the rear-right motor not producing sufficient thrust. Motor-ESC pair were shipped to SLO site and tested on a Dynamometer[CC1] . Upon test, it was determined that the rear-right motor was producing considerably lower torque than expected. While trying to determine if the motor or ESC were malfunctioning, we tested each with a stock Motor or ESC. Both performed normally. When we put them together, the original pair performed normally and the problem was gone.
Upon further investigation we found the problem with the soft-start circuit and managed to replicate this problem on stock ESC in house. When the soft-start circuit is malfunctioning, it reduced the force delivered by the motor. Thermal imaging indicated that one of the 4 parallel connected MOSFETs was shorted between Source and Drain. This would essentially bypass the current limiting due to disabled soft-start feature and deliver normal current to the motor.  Over time this circuit gets damaged with one or more MOSFETs Q20-Q23 drain-source short. While it does not provide soft-start function, the ESC deliver’s normally rated force.
To prove this theory, we shorted the gate of soft-start circuit of a standard ESC and ran the test on Dynamometer. Test results were identical to what we saw with VXE545 motor-ESC pair; low force until throttle PWM=1500 and thereafter normal force. Upon examining the ESC we found that same as the VXE545 ESC, one of the soft-start MOSFETs was shorted between Source and Drain.
At this point we concluded that the issue with VXE545 was a faulty soft-start circuit limiting current to motor and delivering low force. [CC2]

 AAR and video of incident attached.

## Corrective Action

## 1.1           Replace current ESC with upgraded version from an ESC manufacturer.

The current VTOL ESC is old design from when the company and aircraft were smaller. Upgrading the ESC would provide increased reliability and features, but is a large scope project.
a.      The new ESCs being evaluated[CC1]  require a 5V supply. This will call for either changing the wire harnesses to supply 5 volts or to incorporate an intermediary board to intercept the ESC supply and using a regulator generate 5V.
b.      Mechanical formfactor of the new ESCs being evaluated differs from current ESC. This would require altering the ESC mounting scheme.
c.      The heat sink of new ESCs being evaluated is larger than VXE ESC heat sink and would require some mechanical changes to the boom.
d.      The new ESCs being evaluated could enable CAN commanding and telemetry, which would be more reliable, provide useful data, but require multiple hardware and software changes.
## 1.2         Include a motor fault flag during the LW spin up test that triggers if the VTOL controller detects current anomaly.

https://jenaero.atlassian.net/browse/VXEP-596 
https://jenaero.atlassian.net/browse/VXEP-595 
In this case, comparing the ibatt1/ibatt 2 current with the expected current and flagging a fault if less than expected current is observed would detect this problem.  The software may also have to be changed in order to prevent an operator from running two motors at once during launch wizard.
## 1.4       Incorporate flyback diodes across MOSFETs Q7, Q13, Q19 and Q20 – ON HOLD

The motor back EMF can damage the MOSFETs and cause an intermittent failure. A corrective action would be to incorporate flyback diodes across MOSFETs Q7, Q13, Q19 and Q20.[CC2]  We believe this time would be better spent on CA1 (upgrading and qualifying to new ESCs for VXE30)
## 1.5       Corrective Recommendations:

### 1.5.1       Improve wire routing and support of VTOL ESCs. – Requirement for upgrade project

Below are a few recommendations, while not directly related to this issue, they can prevent failures in future:
Motor uses 10 AWG phase wires. These wires enter the side of ESC case and bends at 0.5” radius to be soldered to the ESC board. This is a stranded conductor 0.15” thick. Per IPC/WHMA-A-620, the minimum bend radius should be 0.9”. Such a short radius on heavy gauge wiring induces considerable stress on the solder joint holding the wire to the ESC board. It is recommended we allow more space for the wires to bend at a larger bend radius. Additionally, we should provide some form of stress relief to the phase wiring inside the ESC housing. This could be used to hold the wires and reduce the stress on the solder joints. A temporary fix would be to solder the phase wires as shown below to achieve 0.9” bend radius.[CC3]  We believe this time would be better spent on CA1 (upgrading and qualifying to new ESCs for VXE30)
 

Figure 12 Suggested Solder position
### 1.5.2       Increase air flow to VTOL ESC heat sinks – Requirement for upgrade project https://jenaero.atlassian.net/browse/VXEP-638 

Mount the ESC on the top side of the boom. Presently the ESC is mounted on the bottom side of the boom where the heat sink is facing away from the airflow. This should be added as a objective design requirement for the upgraded ESC design project.
### 1.5.3       Add temperature sensor to VTOL ESCs. Abort launch at limits. Requirement for upgrade project https://jenaero.atlassian.net/browse/VXEP-638 

Incorporate a temperature sensor in the ESC and have software access to abort a launch in case of excessive temperature rise. VTOL ESC heat dissipation arrangement is fundamentally faulty. The MOSFETs dissipate heat through the metal tab provided at the bottom of the case. In our PCB, this will inject heat into the PCB enclosure. ESC Heat sink is useless because it is positioned on the side of MOSFETs that do not conduct heat. We have had failures because of this issue. Redesign and re-layout the ESC board to position the MOSFET bottom sides in contact with the heat sink. This will be added as a threshold design requirement for the upgraded ESC design project.

## Plan

- Investigation complete. See C/CAs
- @Rajesh Budhabhatti Finalize changes requested in report and let Cameron know when 100% done so he can review. Coordinate with @Pat Wells what information and format he would like to deliver to the customer.
- I think we should review the CAs with Sam and Doug. LM may escalate and ground ESCs until we replace them, but replacing is the best path forward. We may be able to assuage their concerns by highlighting that VTOL ESCs are relatively rare (compared to total number of flights, still too high IMO) and damage in this case was minimized by the aircraft detecting the problem and aborting.

## Issue Status

See https://jenaero.sharepoint.com/:w:/r/sites/FlightSafety/Shared%20Documents/Incident%20Reports/VXE-545/Internal%20Investigation%20Report%20VXE-545.docx?d=w57b5fa9248f94d948131abdb3c408827&csf=1&web=1&e=6lAcwc
Customer Version:  https://jenaero.sharepoint.com/:w:/r/sites/FlightSafety/Shared%20Documents/Incident%20Reports/VXE-545/Investigation%20Report%20VXE-545.docx?d=w4c71e8783cdf451fbf4683f723ab82f3&csf=1&web=1&e=fSajlP 
Investigation complete. See C/CAs

## Root Cause

Soft-start circuit in theVXE545 position 3 VTOL ESC was permanently OFF (i.e.. MOSFETs Q20-Q23 Off). This was causing the motor to get less current and deliver lower force. With the Soft start function OFF, the bulk capacitors would be disconnected from the circuit. The motor would operate, but with considerably lower force, as noticed by the customer. [CC1] [CC2] [RB3] [CC4] These components could be have been defective from the manufacturer, or damaged from heat or transients. It is very difficult to determine the cause of damage to integrated circuits. We believe time spent further investigating would be better spent on CA1 (upgrading and qualifying new ESCs for VXE30)

## Comments (103)

### Cameron Chapman, 2024-09-16

@Rajesh Budhabhatti please focus on completing the report first. There are still numerous issues and old information. After that, I can review and we can update the above fields.

### Rajesh Budhabhatti, 2024-09-17

- @Rajesh Budhabhatti Have you reviewed the pre-flight launch wizard runs and previous flights to see if this issue could have been caught before this attempt? Looking at AAR report from April 30, it looks like only motor 1 (UTC 156.8) and Motor 3 (UTC 166.8)  were tested during pre-flight launch wizard test. Corresponding VTOL graph ends at UTC 0 so I cannot tell what the ibatt1, ibatt2 currents were when the motors were tested. 
- Test ideas
- On a different engineering ESC, Starting with 1 Remove some of the parallel FETs and see if the behavior is repeated.
- @Mark Squillante mentioned @Connor Peebles mentioned a batch of ESCs that had poor FET soldering. Need to document and link to that. Should there be a containment? Can this be correlated to that batch?
- @Pat Wells. Report successful flights or any further issue. LM has grounded this aircraft until we provide a report.
- Finish root cause report and deliver to Pat, who will curate it for the customer: Investigation Report VXE-545.docx

### Mark Squillante, 2024-09-17

@Rajesh Budhabhatti bad batch of FETs has been documented here: https://jenaero.atlassian.net/browse/VXEP-198 
Also linking to this Jira incident

### Rajesh Budhabhatti, 2024-09-17

Root cause narrowed down to the soft-start circuit of the ESC assembly in position 3 (right rear).  Aircraft approved for flight with replaced ESC Assy. 
Determining what corrective actions to implement as a result from the investigation. 
- VXE545 flight history log here: 
- VXE545 was involved in a total of 22 flights with 14.1 hours of flight time with the customer. During all these flights it used the same Left and Right Lift booms and lift motors, indicating there were no motor or ESC swaps and these motors performed as expected. As a matter of fact, other than the main and HLB batteries, no other component was swapped throughout the 14.1-hour flight time over 22 flights. Both main and HLB batteries were used in previous successful flights.

9/4/2024: 
Additional tests were conducted on stock ESC-Motors by removing one MOSFET on Hi-side and Low-Side to see if the strange behavior was due to defective MOSFET. Tests were negative. The ESC-Motor performed normally. Test results are included in the investigation report.
9/6/2024
@Cameron Chapman While probing the 545 ESC I found that Soft-start circuit MOSFETs were shorted. Upon further investigation, it was found that Q20-one of 4 MOSFETs in parallel was shorted. This explains the low torque because the MOSFET starves the motor of current. Trying to find out why there was a glitch at PWM=1500.
9/10/2024
Further investigation in Soft-Start circuit:
A possible scenario to the problem we were seeing in field and earlier testing but have not been able to replicate is this:
The soft-start circuit was malfunctioning. The R-C circuit (C12, R40, R41) isolates the ground from motor for 0.47s thereby limiting the current to the motor. After the RC time constant, the circuits turns ON the MOSFETs Q20-23 and enables full current to the motor. During the field operations and lab test, this circuit was not turning the MOSFETs ON (or turning them ON after PWM=1500 or  about 16s) thus starving the motor, resulting in lowered torque.
At some point in time, one of the soft-start MOSFETs (Q20) failed with Source-Drain in shorted state. This bypasses the soft-start function and motor doesn’t see current limiting during the start or normal operations. As a result, in all subsequent tests, motor PWM-Torque/Force resembled a normally functioning motor. 
Further investigation and questions:
- What corrective actions needed to prevent this from happening?
- Confluence document on behavior of good, working soft-start circuit along with signal characteristics.

Update 9/10/24
I have managed to replicate the issue on end-of-life ESC. The problem occurs when the soft-start circuit does not come ON. I shorted the gate resistor to ground and took dyno readings before and after the short. After the shorting, I got the Dyno reading precisely what we saw with 545 ESC. Thereafter, I removed the gate short and took one more reading. This reading showed the motor performing normally. 
Update 9/11/24
It seems that when soft-start circuit is disabled (MOSFETs Q20-Q23 Off) and the ESC is throttled to PWM>1500, it blows the soft-start MOSFETs. However, AARs show that the 545 m3 was operated at 90% throttle. The Dyno tests were conducted using lab power supply with current limit set to 35A. Is it possible that under HLB power, the ESC with soft-start circuit disabled would continue to produce low force without blowing the mosfets?
- Test spare EOL ESC on battery HLB power and see if it fails.

9/12 Update
I got a baseline using an EOL ESC with power supply and with HLB. When I tried to run the ESC-Motor with Soft-start circuit disabled, the ESC stopped working. I am not sure if this is because of the ESC-Motor I was using, so I have another pair I will be trying this out tomorrow. Earlier times when the soft-start circuit failed, the ESC-Motor continued to work normally. This time the pair is not operating at all. 
I found out that the ESC’s Phase MOSFET was damaged and stopped the motor from working.

### Cameron Chapman, 2024-09-18

I think we should review the CAs with Sam and Doug. LM may escalate and ground ESCs until we replace them, but replacing is the best path forward. We may be able to assuage their concerns by highlighting that VTOL ESCs are relatively rare (compared to total number of flights, still too high IMO) and damage in this case was minimized by the aircraft detecting the problem and aborting.

### Rajesh Budhabhatti, 2024-09-19

@Cameron Chapman @Pat Wells Updated investigation here: Investigation Report VXE-545.docx

### Rajesh Budhabhatti, 2024-09-19

This report is for internal use only. Internal Investigation Report VXE-545.docx. I will post a link to the document to be shared with the customer shortly.

### Rajesh Budhabhatti, 2024-09-19

@Cameron Chapman @Pat Wells Here is the draft of investigation report to share with the customer. Let me know if you want me to make any changes. Investigation Report VXE-545.docx

### Pat Wells, 2024-09-20

@Cameron Chapman @Rajesh Budhabhatti I did a bit of clean up on the customer version of the report that’s located on SharePoint.  
Converted to PDF (Attached to this ticket). 
Sending to customer today.  

Thank you for for all the effort on this.

### Rajesh Budhabhatti, 2024-09-20

@Pat Wells Hi Pat, pdf looks good. Thank you.

### Rajesh Budhabhatti, 2024-09-20

@Cameron Chapman Hi Cameron, I have compiled a document per CA to help software evaluate ESC health during LW. Once you approve it, let me know who to share it with. A method for evaluating ESC health through current measurement.docx

### Cameron Chapman, 2024-09-20

Thanks @Rajesh Budhabhatti we should follow up with that and other CA in the associated CA task. https://jenaero.atlassian.net/browse/VXEP-596  in this case.  I will follow up there.

### Rajesh Budhabhatti, 2024-09-20

Will do. Thanks.
Get Outlook for iOS<https://aka.ms/o0ukef>

### Cameron Chapman, 2024-09-26

@Pat Wells responding to customer questions. We could schedule an internal meeting to review these and any other potential workarounds or CAs. 
- Have we previously investigated a soft start issue with the ESC’s? Matt Curran @LM thought he recolected that we did.
- Yes. During VXE30 development, we discovered that 1 soft start FET did not have enough current capacity, so we updated the design to spread the current across 4.
- For internal reference. Since then, we have discovered other flaws with the cicuit, such as FETs do not have equal impedance, so the load will not always split evenly and can still overload FETs. See details in the internal report.

- In the report under Corrective actions we list Remove or bypass soft start circuit. Are we considering this? Would it require new hardware or a software change?
- Hardware change. As mentioned in the internal report, we believe this time would be better spent on CA1 (upgrading and qualifying to new ESCs for VXE30). I think this information would be ok to share with a customer, but you, Pat, and Sam would know best.
- Which CA are we chosing to implement?
- EEs are pursuing:
- 7.1	Replace current ESC with upgraded version from an ESC manufacturer.
- 7.5.3	Add temperature sensor to VTOL ESCs. Abort launch at limits. Requirement for upgrade project
- 7.5.3	Add temperature sensor to VTOL ESCs. Abort launch at limits. Requirement for upgrade project
- Joint SW/EE task, but may not get priority:  
- 7.2	Include a motor fault flag during the LW spin up test that triggers if the VTOL controller detects current anomaly.
- Are there any work arounds from an operator’s perspective. What should they be looking for? Anything to do special or not do?
- Not currently. Sadly these ESCs are not super reliable. Most would need some SW updates like 7.2. Make sure they are flying within published limits. Potentially extra attention to the sounds and power level readings during the launch wizard spinup.

### Pat Wells, 2024-09-26

@Cameron Chapman 
For question number 3 our customer facing report does not list all of those CA’s that you mentioned from the internal report. 
With that being said all that I can really reference in the response is 7.2 fault flag CA.

### Cameron Chapman, 2024-09-27

@Pat Wells sorry I did not have time to review the customer version before it was sent. I recommend adding this CA to the customer report as that will be the primary one we will be pursuing, if it is not too late to amend the report. As long as that doesn’t cause them to do anything drastic like ground their fleet until it ESCs are upgraded? 
- 7.1 Replace current ESC with upgraded version from an ESC manufacturer.
- For the FET bypass, I recommend stating we believe this time would be better spent on CA1 (upgrading and qualifying to new ESCs for VXE30)

### Alexander Alan Arnold, 2025-01-10

@Pat Wells If the RMA and report has already been completed can we close it?

### Pat Wells, 2025-01-10

@Alexander Alan Arnold it doesn’t look like the CA has been implemented yet. 
@Cameron Chapman thoughts?

### Cameron Chapman, 2025-01-10

Agreed. As an organization, we should discuss and decide if we want issues like these with long term CAs to stay open, or to close them and link to a collector project to implement the CA. I think something like ensuring all critical/urgent CAs are implemented or schedules, then closing and linking to longer term could be a good method. 
This specific issue could use a lot of clean up, but if the customer is satisfied, then effort cleanup may not be worth it. We all know we need new ESCs ASAP.  I think getting that project into the hopper for VXE would be a good priority for our company. 
@Pat Wells

### Christa Meck, 2025-08-05

Closing per previous comment.

### Pat Wells, 2024-05-17

@Cameron Chapman, checking back in on this.

### Cameron Chapman, 2024-05-17

@Pat Wells given the launch wizard plots, it is pretty clear the issue is with the RR motor assembly. I do not suspect any issues with the battery. It should be ok to use.

### Pat Wells, 2024-06-20

Note, 6/20 have not received AAR from customer after suggested motor swap.

### Pat Wells, 2024-07-02

RR motor received in SLO, @Sean Odell will deliver to engineering for evaluation.

### Sean Odell, 2024-07-02

@Greg Fryer Jeff from LM gave me 545’s motor and I would like to hand deliver it to your team. Who should I deliver it too?

### Greg Fryer, 2024-07-02

@Sean Odell please coordinate with @Cameron Chapman You can deliver it to the table outside Barry’s office, rather than hunting down a particular person. Please be sure it’s tagged (and this ticket is listed). Thanks!

### Cameron Chapman, 2024-07-02

This part of the plan is OBE now that we have the motor. 
- Operator Suggested
- Inspect motors and blades for visible damage. Replace blade if damaged.
- Spin each motor with power off. Report any differences. This can sometimes indicate bearing issues.
- Replace motor assembly and repeat launch wizard test. Red tag RR motor assembly for further investigation and return to EA.
- Send data logs or review to make sure all motor currents are similar during preflight.
- Determine if wingtips are ok for flight or need to be replaced.
- Confirm with EA ok for flight or not.

### Sean Odell, 2024-07-02

@Cameron Chapman @Rajesh Budhabhatti The ESC/Motor SN C-S100345 has been delivered to desk outside Barry's office per instruction. This is from LM MOD VXE-545

### Rajesh Budhabhatti, 2024-07-02

Thank you @Sean Odell @Cameron Chapman I will inspect the ESC/Motor assembly, run some tests and update results on Jira.

### Rajesh Budhabhatti, 2024-07-03

Good morning @Sean Odell @Cameron Chapman . Yesterday I examined the VTOL motor UK-MOD serial number C-S100345. You were right to assume that there was something wrong with the motor. Here is the performance comparision with a stock motor. I will do some more investigation to see if the fault is with the motor or the ESC. Please see the findings here: Investigation Summary VXE-545.docx

### Cameron Chapman, 2024-07-03

Thanks @Rajesh Budhabhatti a useful plot comparison plot is plotting torque vs PWM for each motor run on the same plot. This can be an effective way to clearly indicate differences. In this case, it is obvious something is wrong with that assembly. As always, please keep the fields above updated with each step of the investigation.

### Pat Wells, 2024-07-16

@Rajesh Budhabhatti @Cameron Chapman AAR file added for post motor replacement test (15 July) as requested previously.

### Cameron Chapman, 2024-07-16

@Rajesh Budhabhatti @Adrian Garcia or @Jeremy Kostel are either of you able to look at the AAR uploaded recently to see if the motor looks normal and ready to fly? This is very high priority, so please see if someone is available today.

### Jeremy Kostel, 2024-07-16

FYI @Adrian Garcia @Cameron Chapman @Pat Wells 
The AAR added today (V545_15) does not display any VTOL throttle and very low VTOL power on either vtol or xcomm logs. Cameron mentioned it might be helpful to share the ftp process to download all VTOL logs with them

### Pat Wells, 2024-07-16

@Jeremy Kostel I’ll reach out to the customer on the VTOL logs

### Pat Wells, 2024-07-16

@Jeremy Kostel just so I’m clear.  Does it appear that the customer did not run up the VTOL motors?  Or is the data somehow corrupt or indicating another problem.  Want to be sure that I’m passing this along correctly when I send them the update and request for more logs.

### Jeremy Kostel, 2024-07-16

@Pat Wells I am not 100% sure, but to me from these graphs it does look like they spun the VTOL motors and that the file was somehow corrupted 
[embedded image-20240716-202504.png]


[embedded image-20240716-202525.png]

### Rajesh Budhabhatti, 2024-07-16

I compared the ESC/Motor combination with a standard motor/ESC and found that it delivered considerably lower torque at lower throttle. I suspect the motor. See the results here: Investigation Summary VXE-545.docx

### Cameron Chapman, 2024-07-18

@David Grosher the VTOL current in these logs seems to indicate that the motors were run, but the throttle values read 0 in both the VTOL and XCOM logs according to @Jeremy Kostel. Is this expected when running launch wizard (or if the used motor test page). Could we correlate these runs with commands in any logs? 
@Jeremy Kostel how does the motor current and duration compare to a normal launch wizard run? The magnitude not matching between the three runs on that plot seems concerning. I would not approve flight based on this data alone. FYI @Pat Wells

### Cameron Chapman, 2024-07-18

@Rajesh Budhabhatti in that case, can you please test the motor and ESC with connected to different motors and ESCs to isolate the issue, then determine the cause? Again, please update plan and status as you progress. I have updated it this time.

### Rajesh Budhabhatti, 2024-07-18

@Cameron Chapman Will do. Thanks.

### David Grosher, 2024-07-18

@Cameron Chapman I do see a throttle command in the VTOL data log of another flight. Although, I do not see that in the MxM1/2/3/4 signals.
[embedded image-20240718-173718.png]

### Jeremy Kostel, 2024-07-18

@Cameron Chapman I pulled AAR’s for two different flights that look as I would expect, below are the comparison graphs of all 3 (VT545 is the key one for this ticket). I am not familiar enough with the launch wizard settings to know if this was a choice to only spin two motors instead of all four, but from this data the motors seem to be acting as expected, though having launch wizard data for all 4 motors would be helpful.
[embedded image-20240718-181225.png]

[embedded image-20240718-180010.png]
[embedded image-20240718-180105.png]

### Pat Wells, 2024-07-18

@Jeremy Kostel @Cameron Chapman the launch wizard does allow the operator to spin all four lift motors and the forward propulsion motor.  Each motor can be spun separately.

### Cameron Chapman, 2024-07-18

@Pat Wells understood. What we are asking Dave is are those throttle commands logged when a user uses launch wizard or the webpage. 
@David Grosher should the MxM1/2/3/4 signals be logged in those cases? Any ideas why they are not in this case?

### Cameron Chapman, 2024-07-18

@Jeremy Kostel the first two looked normal. This third pulse looks strange. It seems to be a motor pulse, but a much different waveform and magnitude than the others. 
[embedded image-20240718-233317.png]

### David Grosher, 2024-07-18

@Cameron Chapman The MxM1/2/3/4 signals are logged. But the throttle commands are not present in the signal at this point when the blips are commanded from the launch wizard. They are present in the other signals that I plotted below: FL CW, FR CCW, RR CW, RL CCW.

### Jeremy Kostel, 2024-07-19

@Cameron Chapman The third pulse you mentioned does not seem to be a motor pulse, although I am not sure what the aircraft is actually doing at that time (Potentially homing?). No throttle is being commanded. It is common across all the AARs I have compared. Here are the 3 AARs from my last comment compared for the last pulse. Note: Vehicle 545 is the only one that dips into negative current after the pulse (min value: ~ -0.3A)

[embedded image-20240719-153411.png]

[embedded image-20240719-153419.png]

[embedded image-20240719-153426.png]

[embedded image-20240719-155412.png]

### Cameron Chapman, 2024-07-19

@Jeremy Kostel good point. those lower current pulses are homing. According to Dave the plots for FL CW … are closer to final throttle than MxM1-4 are. MxM1-4 can be blank in some circumstances (like LW). FL CW… are closer to final throttle.
In that case, since there is a clear issue with the returned assembly, and the launch wizard runs look identical, this aircraft seems ok to fly. Please ask them to watch and listen closely for any issues during launch wizard and takeoff, and be ready to abort in the (seemingly unlikely) event that an motor issue is observed during takeoff. @Pat Wells 
We will continue to troubleshoot C/CA of that assembly.

### Rajesh Budhabhatti, 2024-07-19

Switching Customer ESC for stock ESC to isolate the fault. Will do Dyno test and provide results when done.

### Pat Wells, 2024-07-22

@Cameron Chapman information and flight clearance relayed to customer.  Asked for feedback after they launch. 
Customer is still expecting a root cause report on failed esc/motor assy. @Rajesh Budhabhatti

### Rajesh Budhabhatti, 2024-07-22

@Pat Wells @Cameron Chapman Hi Patrick, I did some testing and suspect the ESC but I need to do some more testing. I will get back to you when I have more information. Thank you.

### Pat Wells, 2024-07-25

@Rajesh Budhabhatti @Cameron Chapman TIQUILA customer queried me again today on an estimated completion date for our esc/motor final report. 
Additionally customer asked if we believe this is an isolated issue or recurring failure?

### Rajesh Budhabhatti, 2024-07-25

@Pat Wells Hi Patrick, I am just finishing up the investigation and will have the report up in less than an hour. It does not look like a recurring issue. The motor-esc combination is fixed and working, however during the investigation we had to dismantle pair and may not be worth returning this pair to the customer. I will post some pictures as well.

### Rajesh Budhabhatti, 2024-07-25

@Pat Wells Hello Pat, here is the investigation report. Investigation Summary VXE-545.docx

### Cameron Chapman, 2024-07-25

@Pat Wells @Rajesh Budhabhatti before finalizing this report and sending to the customer, we should identify the history of this motor assembly. Was it recently installed as a spare, or the original set with this aircraft. Early findings seem to indicate a bad solder joint, so the history may help determine if it was more due to inspection and lack of testing, or something like wear or previous overheat.

### Pat Wells, 2024-07-26

@Cameron Chapman @Rajesh Budhabhatti 
From the customer:  The motor was the original one delivered with the aircraft. We or the Authority have not replaced anything on AV 545 since it was delivered to the UK last year.
 Is this sufficient to release the final report to the TIQ customer?

### Cameron Chapman, 2024-07-30

@Pat Wells no. 
@Rajesh Budhabhatti please complete report and update fields above now as you progress (I have said this so many times). Please let me know when complete. @Jeremy Kostel or @Adrian Garcia you are welcome to assist if no higher priority work.

### Cameron Chapman, 2024-07-30

@Hayden Jeanor can you please review the attached report and actions below and list any actions, questions, or concerns?

### Jeremy Kostel, 2024-07-30

@Rajesh Budhabhatti I added a quick summary of my findings from the AAR containing the LW (post motor swap) to your report. It was compared against two other LW’s from successful flights and was consistent with what would be expected. No reason to believe this is not specific to the motor/ESC combo.

### Hayden Jeanor, 2024-07-31

@Cameron Chapman @Rajesh Budhabhatti Reviewed the following documents https://jenaero.sharepoint.com/:w:/r/sites/FlightSafety/_layouts/15/Doc.aspx?sourcedoc=%7B963C09DA-CED0-4DD2-9B95-91B30BC0DF69%7D&file=Investigation%20Summary%20VXE-545.docx&action=default&mobileredirect=true https://jenaero.sharepoint.com/:p:/r/sites/FlightSafety/_layouts/15/Doc.aspx?sourcedoc=%7B0717D651-8A48-4E11-BFC6-F85DF955AE80%7D&file=AV545TakeoffAbort.pptx&action=edit&mobileredirect=true . Assuming the test data in reports accurately represents M3 motor/ESC performance, I agree with the logical deductions and dispositions made during the investigation. Great work!

 I also agree that a good corrective action would be to include a flag during the LW spin up test. Off the top of my head i would say each motor should pull >4A during our spin ups otherwise a flag should be thrown.

### Cameron Chapman, 2024-07-31

Thanks @Hayden Jeanor , can you please update the fields above accordingly?

### Hayden Jeanor, 2024-08-01

@Cameron Chapman @Rajesh Budhabhatti  this is the report we intend to give to the customer right? https://jenaero.sharepoint.com/:w:/r/sites/FlightSafety/_layouts/15/Doc.aspx?sourcedoc=%7B963C09DA-CED0-4DD2-9B95-91B30BC0DF69%7D&file=Investigation%20Summary%20VXE-545.docx&action=default&mobileredirect=true I will review and edit for easier consumption if so

### Cameron Chapman, 2024-08-01

@Hayden Jeanorwe can treat this report as internal. As long as it is understandable, clear, and logical, we can call it done. @Pat Wells's group can then determine what information to relay to the customer.

### Pat Wells, 2024-08-01

@Cameron Chapman are there any corrective actions planned for this hardware failure?  Customer is likely to ask.

### Cameron Chapman, 2024-08-01

@Pat Wells Yes. The report is not complete. We still need to try to figure out what caused this condition and how we could have caught it (did it exist after production, or did previous flight overstress cause it?). With MAGNSS, I have not had time to review this report.  @Hayden Jeanor or @Rajesh Budhabhatti please investigate that and include corresponding CAs

### Cameron Chapman, 2024-08-05

@Pat Wells I added some actions to the plan for @Rajesh Budhabhatti .

### Pat Wells, 2024-08-15

@Cameron Chapman FYSA 
This case was put into the plan to be worked to closure during the Sprint planning meeting held on 8/14.  Sprint 8/19-8/23.

### Cameron Chapman, 2024-08-15

@Rajesh Budhabhatti please work this issue if you do not have any critical MAGNSS work. See plan above.  Is this something @Laszlo Juhasz @Giovanni Gonzalez or @Paula Diaz could help with. Please coordinate with them.

### Rajesh Budhabhatti, 2024-08-15

Will do. Thanks

### Rajesh Budhabhatti, 2024-08-19

Following tests were performed week of August 12-16: 
Multiple runs of stock ESC-Motor pair to replicate poor solder joint failed to replicate the Dynometer readings displayed by VXE545 motor when it was returned and before it was fixed.
An in-depth analysis of VXE545 motor to measure its Total Harmonic Distortion and Phase Imbalance indicates that VXE545 motor is operating within our Quality margins.
While Researching the history of VXE545, only thing I found was an unrelated NCR regarding the Avionics board used in VXE545. This does not seem to have any bearing on the incident noticed in the field. Here is the NCR:  NCR List - Avionics Board Assy Conformal Coat Containment (sharepoint.com)

### Rajesh Budhabhatti, 2024-08-19

VXE-545 customer asset got modified without proper authorization. To avoid such errors in future, I have written a procedure for working on customer asset here: Procedure for working on Customer Assets.docx

### Rajesh Budhabhatti, 2024-08-20

I ran a baseline test on both 545 motor-ESC and Stock EOL motor-ESC and compared them side by side. I found that while the 545 motor-ESC were not exhibiting the torque-force dip at PWM=1500, it was still producing considerably lower torque and force throughout the PWM span. I am doing some more testing followed by probing the ESC to find the root cause.

### Cameron Chapman, 2024-09-03

@Pat Wells I updated the fields above and added a lot of comments to the report. I have asked Raj to review, update, and schedule a review meeting with me and Laszlo

### Rajesh Budhabhatti, 2024-09-05

I started probing the ESC board and found what seems like one of the soft-start MOSFETs is shorted. Tomorrow I will do some more testing to see how this may relate to low torque we were seeing during first tests.

### Pat Wells, 2024-09-09

@Cameron Chapman any ideas in terms of an ECD for the final report on the motor / esc assembly?
I really need to get this to the customer as despite our recommendations they still have the aircraft grounded until they understand why the assembly failed.

### Cameron Chapman, 2024-09-09

@Rajesh Budhabhatti can you please quickly summarize your latest findings and provide an ECD for when this report will be ready for review? FYI @Pat Wells

### Rajesh Budhabhatti, 2024-09-10

Good morning Cameron,
I have summarized my finding and plan to resolve this issue in status section here: https://jenaero.atlassian.net/browse/VXEP-384#icft=VXEP-384 VXE 545 Commanded aborted launch due to unusual behavior on ascent - Jira (atlassian.net)<https://jenaero.atlassian.net/browse/VXEP-384>
I still have more investigation to do to conform and possibly replicate what we have been seeing but it seems logical that we have identified the issue.
Best regards
Raj

### Rajesh Budhabhatti, 2024-09-10

@Cameron Chapman Done. See the status section above. Thanks.

### Pat Wells, 2024-09-12

@Cameron Chapman checking in for a status.  It looks like there was additional work done yesterday.
Not clear on where we are with closing this out.

### Pat Wells, 2024-09-16

@Cameron Chapman and @Rajesh Budhabhatti checking in for any updates ahead of the Air Worthiness brief with TIQ on Wed 9/18.
They are expecting the final report on the motor/esc assembly.

### Rajesh Budhabhatti, 2024-09-16

@Cameron Chapman Hi Cameron, per your note cc3, do you want me to do a report on what it would take to replace VTOL ESC with new Hargrove one? Should we do this as a separate Jira task?

### Cameron Chapman, 2024-09-16

@Rajesh Budhabhatti  https://jenaero.atlassian.net/browse/VA-221

### Cameron Chapman, 2024-09-16

@Rajesh Budhabhatti please focus on completing the report first. There are still numerous issues and old information. After that, I can review and we can update the above fields.

### Rajesh Budhabhatti, 2024-09-17

- @Rajesh Budhabhatti Have you reviewed the pre-flight launch wizard runs and previous flights to see if this issue could have been caught before this attempt? Looking at AAR report from April 30, it looks like only motor 1 (UTC 156.8) and Motor 3 (UTC 166.8)  were tested during pre-flight launch wizard test. Corresponding VTOL graph ends at UTC 0 so I cannot tell what the ibatt1, ibatt2 currents were when the motors were tested. 
- Test ideas
- On a different engineering ESC, Starting with 1 Remove some of the parallel FETs and see if the behavior is repeated.
- @Mark Squillante mentioned @Connor Peebles mentioned a batch of ESCs that had poor FET soldering. Need to document and link to that. Should there be a containment? Can this be correlated to that batch?
- @Pat Wells. Report successful flights or any further issue. LM has grounded this aircraft until we provide a report.
- Finish root cause report and deliver to Pat, who will curate it for the customer: Investigation Report VXE-545.docx

### Mark Squillante, 2024-09-17

@Rajesh Budhabhatti bad batch of FETs has been documented here: https://jenaero.atlassian.net/browse/VXEP-198 
Also linking to this Jira incident

### Rajesh Budhabhatti, 2024-09-17

Root cause narrowed down to the soft-start circuit of the ESC assembly in position 3 (right rear).  Aircraft approved for flight with replaced ESC Assy. 
Determining what corrective actions to implement as a result from the investigation. 
- VXE545 flight history log here: 
- VXE545 was involved in a total of 22 flights with 14.1 hours of flight time with the customer. During all these flights it used the same Left and Right Lift booms and lift motors, indicating there were no motor or ESC swaps and these motors performed as expected. As a matter of fact, other than the main and HLB batteries, no other component was swapped throughout the 14.1-hour flight time over 22 flights. Both main and HLB batteries were used in previous successful flights.

9/4/2024: 
Additional tests were conducted on stock ESC-Motors by removing one MOSFET on Hi-side and Low-Side to see if the strange behavior was due to defective MOSFET. Tests were negative. The ESC-Motor performed normally. Test results are included in the investigation report.
9/6/2024
@Cameron Chapman While probing the 545 ESC I found that Soft-start circuit MOSFETs were shorted. Upon further investigation, it was found that Q20-one of 4 MOSFETs in parallel was shorted. This explains the low torque because the MOSFET starves the motor of current. Trying to find out why there was a glitch at PWM=1500.
9/10/2024
Further investigation in Soft-Start circuit:
A possible scenario to the problem we were seeing in field and earlier testing but have not been able to replicate is this:
The soft-start circuit was malfunctioning. The R-C circuit (C12, R40, R41) isolates the ground from motor for 0.47s thereby limiting the current to the motor. After the RC time constant, the circuits turns ON the MOSFETs Q20-23 and enables full current to the motor. During the field operations and lab test, this circuit was not turning the MOSFETs ON (or turning them ON after PWM=1500 or  about 16s) thus starving the motor, resulting in lowered torque.
At some point in time, one of the soft-start MOSFETs (Q20) failed with Source-Drain in shorted state. This bypasses the soft-start function and motor doesn’t see current limiting during the start or normal operations. As a result, in all subsequent tests, motor PWM-Torque/Force resembled a normally functioning motor. 
Further investigation and questions:
- What corrective actions needed to prevent this from happening?
- Confluence document on behavior of good, working soft-start circuit along with signal characteristics.

Update 9/10/24
I have managed to replicate the issue on end-of-life ESC. The problem occurs when the soft-start circuit does not come ON. I shorted the gate resistor to ground and took dyno readings before and after the short. After the shorting, I got the Dyno reading precisely what we saw with 545 ESC. Thereafter, I removed the gate short and took one more reading. This reading showed the motor performing normally. 
Update 9/11/24
It seems that when soft-start circuit is disabled (MOSFETs Q20-Q23 Off) and the ESC is throttled to PWM>1500, it blows the soft-start MOSFETs. However, AARs show that the 545 m3 was operated at 90% throttle. The Dyno tests were conducted using lab power supply with current limit set to 35A. Is it possible that under HLB power, the ESC with soft-start circuit disabled would continue to produce low force without blowing the mosfets?
- Test spare EOL ESC on battery HLB power and see if it fails.

9/12 Update
I got a baseline using an EOL ESC with power supply and with HLB. When I tried to run the ESC-Motor with Soft-start circuit disabled, the ESC stopped working. I am not sure if this is because of the ESC-Motor I was using, so I have another pair I will be trying this out tomorrow. Earlier times when the soft-start circuit failed, the ESC-Motor continued to work normally. This time the pair is not operating at all. 
I found out that the ESC’s Phase MOSFET was damaged and stopped the motor from working.

### Cameron Chapman, 2024-09-18

I think we should review the CAs with Sam and Doug. LM may escalate and ground ESCs until we replace them, but replacing is the best path forward. We may be able to assuage their concerns by highlighting that VTOL ESCs are relatively rare (compared to total number of flights, still too high IMO) and damage in this case was minimized by the aircraft detecting the problem and aborting.

### Rajesh Budhabhatti, 2024-09-19

@Cameron Chapman @Pat Wells Updated investigation here: Investigation Report VXE-545.docx

### Rajesh Budhabhatti, 2024-09-19

This report is for internal use only. Internal Investigation Report VXE-545.docx. I will post a link to the document to be shared with the customer shortly.

### Rajesh Budhabhatti, 2024-09-19

@Cameron Chapman @Pat Wells Here is the draft of investigation report to share with the customer. Let me know if you want me to make any changes. Investigation Report VXE-545.docx

### Pat Wells, 2024-09-20

@Cameron Chapman @Rajesh Budhabhatti I did a bit of clean up on the customer version of the report that’s located on SharePoint.  
Converted to PDF (Attached to this ticket). 
Sending to customer today.  

Thank you for for all the effort on this.

### Rajesh Budhabhatti, 2024-09-20

@Pat Wells Hi Pat, pdf looks good. Thank you.

### Rajesh Budhabhatti, 2024-09-20

@Cameron Chapman Hi Cameron, I have compiled a document per CA to help software evaluate ESC health during LW. Once you approve it, let me know who to share it with. A method for evaluating ESC health through current measurement.docx

### Cameron Chapman, 2024-09-20

Thanks @Rajesh Budhabhatti we should follow up with that and other CA in the associated CA task. https://jenaero.atlassian.net/browse/VXEP-596  in this case.  I will follow up there.

### Rajesh Budhabhatti, 2024-09-20

Will do. Thanks.
Get Outlook for iOS<https://aka.ms/o0ukef>

### Cameron Chapman, 2024-09-26

@Pat Wells responding to customer questions. We could schedule an internal meeting to review these and any other potential workarounds or CAs. 
- Have we previously investigated a soft start issue with the ESC’s? Matt Curran @LM thought he recolected that we did.
- Yes. During VXE30 development, we discovered that 1 soft start FET did not have enough current capacity, so we updated the design to spread the current across 4.
- For internal reference. Since then, we have discovered other flaws with the cicuit, such as FETs do not have equal impedance, so the load will not always split evenly and can still overload FETs. See details in the internal report.

- In the report under Corrective actions we list Remove or bypass soft start circuit. Are we considering this? Would it require new hardware or a software change?
- Hardware change. As mentioned in the internal report, we believe this time would be better spent on CA1 (upgrading and qualifying to new ESCs for VXE30). I think this information would be ok to share with a customer, but you, Pat, and Sam would know best.
- Which CA are we chosing to implement?
- EEs are pursuing:
- 7.1	Replace current ESC with upgraded version from an ESC manufacturer.
- 7.5.3	Add temperature sensor to VTOL ESCs. Abort launch at limits. Requirement for upgrade project
- 7.5.3	Add temperature sensor to VTOL ESCs. Abort launch at limits. Requirement for upgrade project
- Joint SW/EE task, but may not get priority:  
- 7.2	Include a motor fault flag during the LW spin up test that triggers if the VTOL controller detects current anomaly.
- Are there any work arounds from an operator’s perspective. What should they be looking for? Anything to do special or not do?
- Not currently. Sadly these ESCs are not super reliable. Most would need some SW updates like 7.2. Make sure they are flying within published limits. Potentially extra attention to the sounds and power level readings during the launch wizard spinup.

### Pat Wells, 2024-09-26

@Cameron Chapman 
For question number 3 our customer facing report does not list all of those CA’s that you mentioned from the internal report. 
With that being said all that I can really reference in the response is 7.2 fault flag CA.

### Cameron Chapman, 2024-09-27

@Pat Wells sorry I did not have time to review the customer version before it was sent. I recommend adding this CA to the customer report as that will be the primary one we will be pursuing, if it is not too late to amend the report. As long as that doesn’t cause them to do anything drastic like ground their fleet until it ESCs are upgraded? 
- 7.1 Replace current ESC with upgraded version from an ESC manufacturer.
- For the FET bypass, I recommend stating we believe this time would be better spent on CA1 (upgrading and qualifying to new ESCs for VXE30)

### Alexander Alan Arnold, 2025-01-10

@Pat Wells If the RMA and report has already been completed can we close it?

### Pat Wells, 2025-01-10

@Alexander Alan Arnold it doesn’t look like the CA has been implemented yet. 
@Cameron Chapman thoughts?

### Cameron Chapman, 2025-01-10

Agreed. As an organization, we should discuss and decide if we want issues like these with long term CAs to stay open, or to close them and link to a collector project to implement the CA. I think something like ensuring all critical/urgent CAs are implemented or schedules, then closing and linking to longer term could be a good method. 
This specific issue could use a lot of clean up, but if the customer is satisfied, then effort cleanup may not be worth it. We all know we need new ESCs ASAP.  I think getting that project into the hopper for VXE would be a good priority for our company. 
@Pat Wells

### Christa Meck, 2025-08-05

Closing per previous comment.

## Attachments (17)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 20240423-Stalker VXE30_545_Incident-O (2) (1).mov | video | 2052 | 2024-04-29 | listed only |
| T95_VT545_240423.zip | archive | 1201 | 2024-04-30 | listed only |
| [T95_VT545_240423_121500_vtl00076 (1).csv](attachments/20305_T95_VT545_240423_121500_vtl00076%20(1).csv.md) | csv | 3883 | 2024-04-30 | converted |
| image-20240501-205934.png | image | 28 | 2024-05-01 | listed only |
| V545_15 Jul 24.zip | archive | 575 | 2024-07-16 | listed only |
| image-20240716-202504.png | image | 32 | 2024-07-16 | listed only |
| image-20240716-202525.png | image | 18 | 2024-07-16 | listed only |
| image-20240718-173718.png | image | 109 | 2024-07-18 | listed only |
| image-20240718-180010.png | image | 69 | 2024-07-18 | listed only |
| image-20240718-180105.png | image | 56 | 2024-07-18 | listed only |
| image-20240718-181225.png | image | 66 | 2024-07-18 | listed only |
| image-20240718-233317.png | image | 19 | 2024-07-18 | listed only |
| image-20240719-153411.png | image | 40 | 2024-07-19 | listed only |
| image-20240719-153419.png | image | 37 | 2024-07-19 | listed only |
| image-20240719-153426.png | image | 37 | 2024-07-19 | listed only |
| image-20240719-155412.png | image | 15 | 2024-07-19 | listed only |
| [Investigation Report VXE-545.pdf](attachments/23332_Investigation%20Report%20VXE-545.pdf.md) | pdf | 2604 | 2024-09-20 | converted |
