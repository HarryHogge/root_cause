# VXEP-1196: Respond to FoSUAS 4/7 Email

- **Issue type:** Corrective Action
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2025-04-08
- **Updated:** 2026-10-07
- **Resolved:** 2026-10-07
- **Reporter:** Cameron Chapman
- **Assignee:** Pat Wells
- **Creator:** Cameron Chapman
- **Parent:** VXEP-999 VXE 598 with VXE 596 Center Wing. Lost connection to VTOL AP and ADB and crashed. 
- **Links:** relates to VXEP-999 (VXE 598 with VXE 596 Center Wing. Lost connection to VTOL AP and ADB and crashed. )
- **Plan:** Confirm if we want to complete actions above. Add to here if so.

## Description

Cam responses underlined. Some are for internal purposes. Please review before sending. 

Vo,
VXE-598 Mishap Report Summary/ Comments from PMA-263 FoSUAS:
 
After a thorough examination of the aircraft involved in the crash and a comprehensive review of the flight logs from the day of the incident, it has been determined that multiple factors contributed to the crash of VXE 598.
 
- During fixed-wing flight, the aircraft operator initiated a climb of 4,000 feet, which is twice the recommended climb duration for such a maneuver (see Slide 6).

The Operator’s Manual has a recommended climb duration stating that motor cooling and to prevent motor over-heating as the reason for this recommendation. There is no mention of the battery or battery connector. Is there data or testing showing that a normal climb induced voltage at the connector for a 4000-foot climb would result in this failure?
No, as discussed previously, we have data to show that such a climb would not cause issues on a normal connector pair. The investigation discussion mentioned this climb profile would have exacerbated the identified root cause of high connector impedance due to impartial mate and non-conforming contacts. 
 
Operator’s Manual reads the following on 2000 ft climbs, caution point to motor “Climbs of more than 2000 ft using a battery should be done in steps of 2000 ft or less with 5 minutes of level cruise in between climbs to allow the motor to cool down. CAUTION - Continuous climbs of more than 2000 ft can overheat and damage the motor.” Later in the manual is this Note also pointing to the motors “NOTE - When planning a mission, a 5-minute cool down cruise loiter is recommended for every 2000ft of altitude gain. This is to allow the motor to cool.”
 
Would recommend if it is a hard limit of the system, software limits be applied, if it’s just a recommendation, leave it to operator discretion.  I am not aware of any data to support this. I am guessing it is left over from B25. I agree we should automate. B35 ESCs will measure motor temperature for both lift and fwd. @Scott Hunter @David Grosher  are we planning to implement warnings, aborts, etc based on the new ESC and other telemetry available on B35? Are we tracking that anywhere yet? 
- Additionally, the main battery connectors were not fully mated, resulting in overheating of the connectors. This overheating disrupted the electrical flow in the system (see Slide 9).

What is the normal voltage? The connector is rated at 40, from what we understand.
The normal voltage depends on the battery state and flight loads, but was approximately 28.5V before the fault. I am guessing he is asking about the connector current rating. EC5s are rated to 40A recommended 90A max. AS150 70A RC 150A MC. I think we want to avoid discussing the hobby contacts. We have data and lots of flight history showing temperatures are reasonable with confirming contacts.  We are planning to upgrade these with B35. 
 
David Cudd asked Pat Wells what the normal voltage should be, and he was checking with the Edge engineers. However, we would not assume that the connecter was not properly plugged in multiple days in a row unless it was damaged in some way, it’s possible that it melted the first time and was not able to plug in fully, but we would not expect improper seating multiple days. We are not able to locate directions on plugging in the battery. The connector does have a bump, it “locks” into but I wouldn’t say you’d hear it “click,” it’s mostly a friction fit.
We measured non-conforming contact dimensions on the equipment involved. This increases the difficulty of mating fully and the risk of a high impedance connection. 
- Has the document to inspect for full mate been sent yet?

 
Based on flight logs from, 1/26, 1/25, 1/24, 1/23, Amp draw was in the 50+A range, it’s unclear if that amp draw is normal during climb or not. It could be that the mating connector was not seated for all these flights or was damage in some way/point.  If mating the connector is an issue, then the connector should have a method of positively locking into the battery (long-term solution) or procedures for ensuring positive lock (short term).  A more robust connector should be necessary if the “normal” amp draw exceeds the rated 40A constant and 90A max amperage draw to the connector.
Agreed. We plan to release improved connectors and contacts with B35. 
Is there a way to check this on the ground during pre-flights? This overvoltage happened quickly once the motor began to spin up for the climb. 
Yes, this is/will be in the full mate inspection document Pat’s group is working on. 
- The disruption in the electrical flow caused the fixed-wing autopilot to reset multiple times during the flight, causing it to lose crucial calibration settings necessary for normal flight. As a result, the aircraft operated in an unrecoverable state for the remainder of the flight (see Slide 7).

Could/should the aircraft recover gracefully from loss of power for autopilot (avionics battery or pull from VTOL battery)?  Can additional sensors be installed or current on board sensors such as GPS.etc to identify and relay to the avionics when the aircraft is in flight, in movement, and safe on deck? Is disruption of power and electrical flow a repeatable common concern?
 This is mostly a question for @David Grosher. IMO losing AP power is the main concern. I am guessing most APs won’t recover well with intermittent power during flight. Yes, see the linked AS150 contact investigation. This will be challenging to message to customers. We suspect many of them are due to OOS contacts and impartial mates. Our latest plan was to focus on verifying full connector insertion  
DGROSHER: I do not believe that it is reasonable to expect a single string system to recover after power loss. Biases on the IMU will be different when power is restored to the system.  This is the only instance of a FW AP reset that I have seen in the past 2 years that I have been here, so I don’t believe this incident in and of itself would justify the development effort and associated increased cost of the system to implement a redundant avionics architecture. 
To prevent recurrence of this issue, if the frequency justifies the effort, could the default avionics mission profile be modified or designed to automatically recognize the GCS-loaded profile? In cases of conflicting profiles, the GCS profile should always take precedence. Question for Dave. 
- These three factors have been identified as the causes of the incident. In response, Edge Autonomy has implemented corrective actions, including updates to the Operator's Manual, an Advisory Notice, and a planned software update. We have a high level of confidence that these corrective actions will address or resolve the issues that contributed to this mishap. 
- Cam 4/15-Who entered this statement? I think those actions will help, but the risk of partially mated, out of spec, and inconsistent AS150s should be reduced with planned communications, but not resolved until they are replaced in B35.

Agree with Op manual update/clarification. A pre-release draft of Advisory Notice AN_25_006 was shared with the team for review. Feedback was provided to Edge, but the final published version of the advisory notice did not incorporate any of the suggested changes regarding the numerous issues and concerns raised. To mitigate the potential risk of aircraft loss, these concerns should be addressed in a revised advisory notice to ensure clear communication with operators and training support.
 Has this been implemented?   Yes it was released on Web Manuals.  We are not making his suggested revisions. 
Per the software update- Will climbs above the suggested 2000 ft limit be actively prevented? Alternatively, could the system automatically initiate a 5-minute loiter period before permitting further ascent? Or could the GCS simply warn the operator of the risks associated with climbing above the suggested altitude without a prior loiter period?
 Question for Dave. See B35 plan above. It seems like we would want more hardware testing before implementing automatic software limits without test data to verify it is necessary and/or helpful. 
If I can further elaborate on any of these comments, please let me know.
R/
 
Edward Finch Jr. (Eddie)
FoSUAS Marine Corps IPTL
Navy and Marine Corps Small Tactical UAS Program Office (PMA-263)
Edward.f.finch2.civ@us.navy.mil
240-587-4646 (Work Cell)
301-904-8413 (Cell)

Additional questions:
- In the event that the autopilot looses power and restarts during flight what exactly does the aircraft do?  ie does it fly uncontrollably, does it climb, does it run the forward propulsion motor at full power, does it just glide to the ground with no motors on? @David Grosher  The flight system is no longer powered, there is no control. Depending on the phase of flight, the length of time the system is unpowered and which power buses were involved the behavior will change. This is a critical failure that will most likely result in the loss of the system.  The VTOL system does have a chance of recovery but the FW AP does not because it performs the state management of the aircraft. It will not return to an active flight mode. @David Grosher further clarification of the question. They understand that it is a critical failure. They want to know if there is any chance of knowing what happens next?  Their fear is that it will continue to fly uncontrollably until the battery is depleted.  No, it will not command a forward throttle and will descend. There is limited lateral control on the ailerons to attempt to maintain level flight. However, because the bias on the IMU was lost, it may not succeed.
- What did this aircraft (598) do after the autopilot restarted? @David Grosher  The AP went through its normal initialization process. Because the AP state machine does not support initialization in flight it did not activate its control loops, with the exception of aileron control.  @David Grosher to clarify the question. They are asking what did this aircraft due after the power loss event?  ie did it just glide to the ground, nose over and crash etc? In this case the system appears to have glided down until crashing.
- Do we have any additional data to support that the AS150 connector overheated ( outside of the resistance readings we’ve already provided. @Cameron Chapman @Steve Gonzales @Pat Wells No, I am having Gio do an additional test this morning thought that could support the overheating.  Note, I had the failed connector analyzed with a 3D surface analyzer but have not received the report yet.  This morning's testing did not change the resistance measured.  We will run more test on 4/15. 
- Cam 4/15-@Steve Gonzales @Pat Wells  The high antispark resistance has been a consistent indication of overheating. I think the standard resistance is checked in production. We could add the following to the test plan
- Verify when this harness was built, the AS resistance was checked and in spec (which would indicate something during used changed it (overheat))
- We could run a test harness not fully inserted and purposefully overheat it and measure resistance before and after. 
- We should add these results to a general troubleshooting confluence, this investigation, and possibly a summary of AS150 issues. These documents may have been started already (need to search)/
- Do we have data to support that the current draw seen during climb in this mishap is within normal ranges that we would expect, ie compared to what we would see on other aircraft. @Cameron Chapman @Steve Gonzales There are development data stating that FW flight climb rate should be limited in current, time, and overall power and would affect connectors but the data is lacking.  I need to compile known good data sets to compare FW flight at climb.  This may take some time to find, compile and run.  
- Cam 4/15-One of the EEs (I think @Jeremy Kostel) ran the exact profile the customer ran and the temperatures were well within range. Would that be helpful?
- If we want to compare to typical current levels for that configuration of aircraft, this would be a flight log analysis task, which Dave’s group is much more skilled.  
- I have been trying to collect average and worst case profiles here. Please review that, use if helpful, and add or correct info as helpful. https://jenaero.atlassian.net/wiki/spaces/PDAO/pages/11272193/VXE30+Power+and+Temperature+Profiles
- If the autopilot restarts during flight does the aircraft use DTED or the Mission waypoints altitude?  (This is the customer’s question, understand it makes no sense)  @David Grosher DTED is elevation data it would never be used as the commanded altitude, however at times it could be used to derive the altitude command. The Mission waypoints would not be used either because they are stored in volatile memory for operational security, so the AP would no longer have access to them on restart.  It should be noted that the baro offset was lost on the reset of power resulting in the observed changed altitude measurement. DTED data loaded into memory would also be lost on a power reset.

## Comments (14)

### Cameron Chapman, 2025-04-08

@Pat Wells I added some responses underlined in the description field. Let me know how you would like to proceed.

### Pat Wells, 2025-04-08

@Cameron Chapman thank you for the information.  Just FYSA the Advisory notice on the connector mating was released last week on Web Manuals.

### David Grosher, 2025-04-08

@Pat Wells I added some comments where I was tagged above.

### Hayden Jeanor, 2025-04-08

@Cameron Chapman B35 ESCs will measure motor temperature for both lift and fwd

### Pat Wells, 2025-04-10

@David Grosher @Cameron Chapman  J Vo and I had a meeting with the customer this morning regarding our responses to their questions.  This meeting generated additional questions that I’ve added above.  If possible please assist in answering them at your soonest opportunity.  Their most important question is number 1 regarding the aircrafts behavior after an autopilot reset. 

@Drew Hildreth FYSA

### Pat Wells, 2025-04-11

@David Grosher @Cameron Chapman gentle reminder that we’ve got some due outs in the questions above.

### David Grosher, 2025-04-11

@Pat Wells My questions are addressed above.

### Pat Wells, 2025-04-11

@David Grosher @Cameron Chapman I’ve added a bit of clarification to a couple of the questions if there’s anything you’re able to add.
Thanks

### David Grosher, 2025-04-11

@Pat Wells Minor updates to address the clarifying comments.

### Pat Wells, 2025-04-14

@Steve Gonzales Cameron is on PTO and he referred me to you for answers to the additional questions above from the customer.  I’ve tagged you above as well.

### Pat Wells, 2025-04-14

@Steve Gonzales Did you miss question number 4?
Thanks

### Christa Meck, 2026-10-07

@Pat Wells Is this something that still needs to be followed and worked?

### Pat Wells, 2026-10-07

@Christa Meck no I don’t believe so.

### Christa Meck, 2026-10-07

Marking Done as it looks like some stuff happened here.

## Attachments (0)
