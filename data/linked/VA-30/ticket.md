# VA-30: Edge internal troubleshooting-VXE 407 -VTOL AP Froze-Error during transition for landing, VTOL AP WD

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-05-21
- **Updated:** 2026-03-02
- **Resolved:** 2025-05-21
- **Reporter:** Cameron Chapman
- **Assignee:** David Grosher
- **Creator:** Cameron Chapman
- **Labels:** 8-28-Sprint, TIQUILA-Blocker
- **Links:** relates to VXEP-466 (IRAD: Unified Autopilot); relates to VA-49 (VXE407 Develop Root Cause by (hopefully)Replicating Watch Dog Event on HIL); relates to VXEP-11 (TPTR-5 VXE 407: (VTOL-AP-WD) Unexpected Behavior Seen During Vertical Landing); relates to RMA-122 (VXE407 230519)
- **Customer:** TIQUILA
- **Corrective Action:** Investigating watchdog issues here https://jenaero.atlassian.net/browse/FS2-749
- **Root Cause:** Investigating watchdog issues here https://jenaero.atlassian.net/browse/FS2-749

## Description

This issue will track troubleshooting of the incident by Edge personnel, to better communicate and prep for customer meetings. 
See this link for original shared investigation.
https://jenaero.atlassian.net/browse/VIT2-291 
Detailed timeline and findings: https://jenaero.sharepoint.com/:w:/r/sites/EngineeringTeam/Shared%20Documents/Electrical/Investigations/VXE407%20Error%20during%20transition%20for%20landing/VIT2-291%20v407.docx?d=w80ab90f74c5a43d9b4f07accfce392a5&csf=1&web=1&e=aUmGHB 
Investigation status

 Bigger issue for unified AP. John thinks likely software. Maybe systemic.
 
Investigation Plan
- Scott Hunter doing a lot of related work trying to simulate/replicate this issue and fix.
- Dave to email Allen and Sam recommended actions. Once they confirm, communicated approved status and plan with LM. If they approve, proceed with recommended actions below
- Replace red AP board.
- Red AP board is red tagged, then installed into an upcoming HIL. The AP board and HIL should be labelled with this incident number. Add AP SN to this issue. Report if the issue ever happens again, and the circumstances of the occurrence.
- Return the 407 aircraft for RMA and SCO flight with new AP board.

@Pat Wells need inconclusive root cause workflow. 

Original text:
From Garret: Error during transition for landing. Pop up said Emergency glide landing active. ELZ red. Commanded go to IP4 of ELZ while in IP2 of ELZ. On downwind, aircraft engaged lift rotor system. Commanded Land Immediately. Did not get option for User Landing Control. Aircraft taxied while descending and landed at PLZ.
 
Payload was a drop payload.
From my point of view I observed vehicle turn on the VTOL system, it looked like all rotors were spinning, then it looked like it aborted, dived down for airspeed, then started the emergency glide in pattern. On the downwind it transited to VTOL. It was pretty far out and I was concerned we did not have enough hybrid lift battery to come back. I requested Garret command a land immediately so it would descend and land out rather than taxi back. He sent the command but it did not take. As it was VTOL taxi-ing back I asked our crowd of guests to move out of its path because its path was directly over the people and the battery was draining. During landing the operator did not get the nudge pop up. It did land on the LZ. Motor did not shut off but we used the VTOL control cut and safe. At touch down it was about 15% HLB SOC.
The aircraft conducted two successful flight before this issue in Helendale, CA.
This aircraft is back at Edge in the engineering area, near the window/HIL area.

## Plan

Dave to discuss known potential causes and corrective actions, then fill out the fields below. See duplicate info above, which was entered before we had these fields here. 
- Investigating watchdog issues here https://jenaero.atlassian.net/browse/FS2-749
- Returning aircraft to RMA.
- Update linked VIT2 with relevant information. Move to monitor or close.

@Pat Wells need inconclusive root cause workflow.

## Issue Status

Unable to replicate, seems to be problem in the VTOL AP. Have seen this issue on several aircraft, but most times it happens while idle. It is a much bigger problem when it happens during VTOL flight or transition (this case).  Bigger issue for unified AP. John thinks likely software. Maybe systemic.

## Comments (28)

### Cameron Chapman, 2023-05-21

Attached 12V screenshots. It looks like 12V switch just powers the SA cam, and 12V Aux measures both aux lines.
[embedded: MicrosoftTeams-image-20230522-041546.png]
[embedded: MicrosoftTeams-image (1)-20230522-041551.png]
[embedded: image-20230522-041642.png]

### Cameron Chapman, 2023-05-21

@Hayden Jeanor for this issue, it was recommended we do our detailed troubleshooting and communication on this internal issue, so that we can develop a coherent message for external stakeholders and customers. Please use it for investigation.  
Ideas to test. 
- Check if 12V aux still has power.
- See if air data board and sa cam Ethernet traffic were still active during the reset. They are both powered by the same 12v input as the vtol ap.
- Reset VTOL AP using reset button. See if rebooting the board creates the same cycling behavior as seen in the plots.
- Also see if 12V aux disables when VTOL AP is reset.
- Find drop payload documentation and see how it is powered. Do we have the drop payload from this flight available?
- Inspect everything for damage/shorts. Inspect reset button on VTOL AP especially.
- Evaluate not populating the VTOL AP reset button. It seems like it could do more harm than good. Is it used during any programming.

### Hayden Jeanor, 2023-05-22

Tested today (5/22/2023):
- still trying to determine VTOL AP fault from data analysis
- the 12.8V power oscillation is present in normal flights. However, this incident reported less current (~300mA)  than a normal flight (~1.3A) leading up to the incident
- the 12VAux current also cuts out during transition in normal flights, but the current (~150mA) was also less than a normal flight (~750mA) leading up to the transition
- the two flights were powering separate payloads with this line, so a difference in them makes sense
- powered up and connected to FW AP
- 12V Aux measured on Aux port 1 and 2: 12.93V present at both ports
- Testing VTOL AP on Iron Bird trying to replicate behavior seen in logs:
- tested reset button behavior 
- loss of connection via the UI
- a new log is created
- does not seem evident that the reset button was accidentally engaged during the incident
- tested behavior of a voltage dip when powering VTOL AP:
- loss of connection via the UI @ ~4V
- a new log is created
- does not seem evident that the reset button was accidentally engaged during the incident

Will dig into CW tomorrow

### Cameron Chapman, 2023-05-23

Thanks Hayden for the troubleshooting and detailed findings. Some additional ideas:
- Are those currents still measuring less than a normal avionics box during ground test?
- Inspect CW boards and wiring after this. Wiggle/shake test to see if processor resets from intermittent power.
- Measure oscillations in higher resolution (o-scope on the current sense resistor). See if we can figure out what is oscillating.

### Cameron Chapman, 2023-05-25

@Hayden Jeanor when you say normal flights below, do you mean normal flights on this vehicle or another? Comparing to another vehicle would be the best comparison? 
@David Grosher

### Hayden Jeanor, 2023-05-25

@Cameron Chapman I was comparing to flights on another vehicle

### Hayden Jeanor, 2023-05-25

update from today (5/25/2023):
- pulled CW cover and inspected VTOL AP and interface board
- no physicals non-conformances discovered
- performed pull and wiggle test on any wires connected to VTOL interface and AP board
- no intermittency observed
- After further analysis, i am starting to think that it is unlikely this is a power delivery issue
- Even though we dont have log data of the current sent to the VTOL AP and interface (AIR_PWR) the fact that the ADP is reporting back ias and alt is indicative that there was enough voltage present on that line during the incident
- we know the watchdog was triggered
- I am looking into the conditions that would cause the watchdog to not reset the MCU

### David Grosher, 2023-05-30

@Hayden Jeanor @Cameron Chapman The watch dog reset was caught by the software.  It performed a crash dump which can be seen in the event log of the VTOL AP once it recovered from the task lock condition that it found itself in. In the trace of the task lock it appears that it was hung on writing the event log.  Scott on the SW team will be looking into this when he completes his current work on an unrelated bug fix. 
My concern is that there is a hardware issue that is potentially leading to an issue with the SD card microcontroller. Do we have an idea which component is causing the power oscillations? And do we know why the main 12V bus was pulling so much less power than normal?

### Hayden Jeanor, 2023-05-30

@David Grosher I think there might be some confusion, understandably so. I want to make sure you know that the I12V signal on the Xcomm log does not include the current sent to the VTOL AP and VTOL AP interface board. The two current sensors on the Xcomm that are reading 12V buses are reading the +12.8V_Limit and 12V_Aux buses shown in the power tree.  I can only assume that the current sensors are here instead of Air_Pwr (the buss that the VTOL AP is ran off of) because these current sensor locations were chosen for XE25 design and were never changed for VXE30. The I12V current includes power sent to the SA Cam board, sightline board, and the nose cone blinkers and fan.
[embedded: image-20230530-194203.png]
[embedded: image-20230530-195422.png]
[embedded: image-20230530-195444.png]
Air_pwr has no current sense in line
[embedded: image-20230530-200324.png]

I assume the oscillations on the I12V signal are from Q5 switching. I can look into the behavior of this bus further, but i figured it was not relevant to a VTOL AP malfunction. 
As for your concerns about the SD card, what do you mean about the SD card MCU? Do you mean the SPI buses that are used to communicate with the PIC32 MCU?
The two main questions that i have been trying to answer this morning:
- what caused the program to “go into the weeds”
- most likely hardware related, but disconcerting that we couldn't find in the logs - maybe not looking hard enough?
- Why the WD did not trigger a reset
- what are the conditionals that the software checks before allowing the wd to reset
- @John Clark mentioned that Gordon defined this in an NMI that is executed when the wd is triggered, but i cant seem to find this NMI interrupt handler in the source code. John let me know if you you are familiar with the location of this, i thought it would be in the wdt.c file, but its not
- [embedded: image-20230530-201911.png]
could be hardware checks in the NMI that prevent a system reset

### David Grosher, 2023-05-31

@Hayden Jeanor Thanks for the detailed overview of where the current was measured. I didn’t realize that we were measuring a different 12V bus.
John is out of town on vacation this week. He is the one that mentioned that there was another microcontroller involved with writing to the SD card. Perhaps he was referencing the SPI driver?  My understanding is that there were issues here previously when the system was powering down. 
As for the location in the software where the WDT is caught, there is a #define called BUILD_INTWDT.  The logic checks if the aircraft is flying and that is in wdTaskTest() in TaskSetup.c, which is called in clockTick() in utils.c.  The logic here also appears to be what triggered a crash dump report, which is what implicated the event logging task as the issue.  This logic is only executed if the watchdog task is not running, which would only be the case if higher prio tasks are stuck. 
Perhaps this is a dumb question, but I’m not familiar with the electronics design at this point. Are all of different power buses isolated from each other? Essentially, I’m wondering if sudden changes on one bus would result in voltage fluctuations on another bus.

### Cameron Chapman, 2023-06-01

They aren’t isolated from each other, but are current limited, so a surge on one 12V may bring down the shared 28V input momentarily, but should be current limited quickly after that. 
They do all share grounds, so transients on one could affect others, but this would be short term spikes.

### Hayden Jeanor, 2023-06-02

Sorry for the delayed reply, I got caught up in other projects. Thanks for the response @Cameron Chapman  about bus interconnection. 
Form looking at the firmware I want to outline a couple of knowns during the events of the incident, let me know if i am incorrect about any of them: 
- we know the watchdog timed out
- still dont know what caused this, but the program got hung up (likely) or we hit a corner case condition where the program did not kick the dog frequently enough (unlikely).
- Not sure the sequence or priority of tasks, but it seems like Clocktick() was called while the WD was timed out instead of the WD immediately causing a system reset. In this func, BUILD_INTWDT = 1 calls wdTaskTest() to determine if the WD will allow a system reset or if it will clear the WD. 
- In wdTaskTest() the func allows the WD to cause a system reset if the plane isnt flying. However, it allows the WD to be cleared because the plane was flying.
- Without a system reset, the program exits the “hung up state” ~50s later during FW emergency landing and continues its transition for landing


It seems the WD was functioning properly according to how Gordon programmed it to. Not sure if this was the best design choice to ignore a watchdog because the planes in the air, but what do i know.

Im glad i answered my question of why the WD did not cause a system reset, but now i am focusing on the two questions:
- what caused the hang up
- could be hw, but unlikely that it is power delivery to the MCU in my opinion. Maybe power delivery/malfunction to a peripheral that the program was waiting on?
- how did it exit the hung up state without a system reset
- possibly the problem was intermittent and returned to normal, allowing the program to resume?

### Hayden Jeanor, 2023-06-08

Havent really been investigating this issue this week because I havent been able to identify a subsystem of hardware failure from the logs. I think it would be better to track though the software logic during the incident to hopefully identify a potential cause for an AP hang up (hardware or software). Otherwise, im looking for a needle in a haystack to determine what hardware peripheral or subsystem was the potential cause of the hang up. 
I would look into it myself, but i think the investigation now requires a larger understanding of the AP firmware as well as the inputs that it depends on for operation. Let me know if you need any more support. I can further inspect/test hardware subsystems, but i think such an effort would be frivolous if the problem is potentially intermittent and we are unable to isolate it down to a subsystem.

### David Grosher, 2023-06-08

@Hayden Jeanor The VTOL AP event log implicates the writing of the event log in the trace of the crash dump (see below). So I think the peripheral to check would be the microSD card (maybe the SPI driver as well?). Having said that, I’m not sure what testing is possible on your side in terms of isolating this specific peripheral on the board. 
[embedded: image-20230608-214214.png]

### Hayden Jeanor, 2023-06-08

@David Grosher sounds good, i can look into the SD card. However, im trying to understand the thought process a little more. Pardon my ignorance, but i dont fully understand what you mean by the “event log implicates the writing of the event log in the trace of the crash dump.” Do you mean that the event log reported that the AP was reading and logging data and should have been logging it in the SD card during the ~50s window that we are missing data in the VTOL flight logs? Otherwise, would you elaborate further? Thanks!

### David Grosher, 2023-06-08

@Hayden Jeanor Yeah, I thought that might sound confusing when I wrote it. There was a crash dump in the event log that was recorded after the AP recovered some ~50 seconds later. That crash dump contains a trace of the function calls when the crash dump data was logged. At the top of the trace the function that was called is actually the event logging function, which would implicate the function as being the source of our problem.  The event logging function is writing to the SD card, which is why I suspect that system.  Sorry for the confusion. 
My question for you is whether we can actually isolate the SD peripheral system and try to induce a failure?

### Hayden Jeanor, 2023-06-08

@David Grosher thanks for the elaboration. That makes a lot more sense. It would make a lot more sense for the program to get hung up here, if the event logging function reads from the SD card at all. ie, if it was trying to read data that it couldn’t form the SD card because of a possible SD card system malfunction, the program would wait for it. Do you know if it read from he SD card at all in this func, or only writing? Either way, ill look into it.

### Hayden Jeanor, 2023-06-22

Sorry its taken me so long to get back to this, its been continuously about second on my priority list since my last update. But i was looking into trying take electrical quality measurements of the microSD card on the red AP, but the lines that we are looking to measure are in between the AP and the AP interface board, so they are pretty much impossible to get to while the system is powered.  I started to look at little into the SPI drivers in the source code to determine what conditions would cause the controller to wait on the peripheral, but I know @Garrett O'Neill was interested in helping with this investigation. I will assign to him if hes able to provide any new insight with a fresh set of eyes. If we are really adamant about doing more hardware investigation, we can try to pull the SD card to see if it has any non-conformance, but I feel that would be rather difficult to diagnose and less fruitful.

### Hayden Jeanor, 2023-06-26

per my conversation with @David Grosher , I wanted to double peer review my response to LM regarding V407:

Hi Matt, apologies for the delayed response. Although this ticket hasn't been updated recently, I want to assure you that we have been actively working on the investigation over the past month. Let me provide you with a concise summary of our findings so far:
During the VTOL transition, the red VTOL AP encountered an issue where it became hung up. Typically, this would trigger a hardware reset of the AP microcontroller through the WD (watchdog) mechanism. However, Gordon implemented a condition in the code to prevent this reset if the aircraft detected that it was in flight. As a result, the VTOL AP remained stuck in its current state, possibly due to an infinite loop, deadlock, or waiting for an external peripheral to respond.
While the VTOL AP was stuck, the fixed wing AP took over for approximately 50 seconds until, somehow, the VTOL AP managed to exit its hung up state. We're still unsure about the exact cause of the microcontroller getting stuck or how it resolved itself. However, we do have a crash restart dump that allows us to trace the function call stack back to the specific function running during the incident (although we can't confirm if the stack dump was captured during the incident itself). The function at the top of the stack during the "crash" was the one responsible for writing to the event log.
Given that the suspected problematic function involves reading and writing from the microSD card on the VTOL AP, we are currently conducting hardware and software investigations in this specific area. On the software side, we are exploring potential scenarios that could have caused the observed behavior during the incident. We are running test cases on the functions suspected to be buggy and closely monitoring their responses to determine if we can replicate the same issue. Since the problem is intermittent, it's challenging to investigate the hardware, but we're still working on identifying any potential hardware non-conformities.
Based on the information we have, we are now more confident in narrowing down the problem to the red VTOL AP board. However, we would prefer to have more time with the entire system for troubleshooting. If it's time-sensitive for LM, we can replace the VTOL AP board and send the vehicle back for RMA through the system checkout process. Please let us know your preference. Thanks!

fyi @Cameron Chapman

### Cameron Chapman, 2023-06-27

Thanks Hayden. Good summary.
I will schedule a meeting to discuss what to quarantine/return. 
 If we are pretty confident the issues is likely due to the red VTOL AP board, we should quarantine that one, replace it, and evaluate the rest of the aircraft for repair/replace. In general, we should prioritize first isolating the issue as much as possible, then returning the equipment back to customers. 
It might be more digestible to add bullet summaries at the end of the post. 
Investigation plan:
Potential Corrective Actions:
After adding those, I think that would be ok to post to the LM issue, but we should confirm with Dave first.

### Cameron Chapman, 2023-06-29

Assigned to Dave. See investigation status and plan above for next steps.

### Hayden Jeanor, 2023-07-20

Upon full visual inspection of VTOL AP and VTOL AP interface boards, found no non-conformities. The SD was fully seated and seemed to be making solid contact with each of the pins as shown by the contact marks in the picture below. The only thing to note was that this AP board was assembled before we started putting a bead of RTV on the SD card to hold it in place
[embedded: image-20230720-224108.png]
[embedded: image-20230720-224048.png]
[embedded: image-20230720-224057.png]
[embedded: image-20230720-224026.png]
[embedded: IMG_0007-19800101-070000.jpg]

### John Clark, 2023-08-16

@Cameron Chapman @Hayden Jeanor how may I identify this VTOL AP? I need to find the HIL it was placed into.

### Hayden Jeanor, 2023-08-16

@John Clark per our conversation, the VTOL AP was not allocated to a HIL yet. I removed VTOL AP interface board from V407 CW. Both are the the right of my workbench on the misc eng rack.

### Cameron Chapman, 2023-08-24

Linking subtasks to parent

### Cameron Chapman, 2023-12-04

@David Grosher here was the latest status for this aircraft. Is it still correct? 
@Pat Wells or @Greg Fryer do we need LM approval to do this, or are we approved to proceed. 
- Replace red AP board.
- Red AP board is red tagged, then installed into an upcoming HIL. The AP board and HIL should be labelled with this incident number. Add AP SN to this issue. Report if the issue ever happens again, and the circumstances of the occurrence.
- Return the 407 aircraft for RMA and SCO flight with new AP board.

### David Grosher, 2023-12-05

@Cameron Chapman Yes, the plan is still accurate.

### Cameron Chapman, 2023-12-05

@David Grosher Thank you. Are we clear to copy the fields above to https://jenaero.atlassian.net/browse/VIT2-291, then move it to closure or monitor, or would you like to handle those communications in a different way? Also, do you have a WD investigation project you could link to issues like this in the C/CA? 
Is this a good one? https://jenaero.atlassian.net/browse/FS2-749 
FYI @Pat Wells

## Attachments (14)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| MicrosoftTeams-image (1)-20230522-041551.png | image | 287 | 2023-05-21 | listed only |
| MicrosoftTeams-image-20230522-041546.png | image | 247 | 2023-05-21 | listed only |
| image-20230522-041642.png | image | 82 | 2023-05-21 | listed only |
| image-20230530-194203.png | image | 263 | 2023-05-30 | listed only |
| image-20230530-195422.png | image | 46 | 2023-05-30 | listed only |
| image-20230530-195444.png | image | 22 | 2023-05-30 | listed only |
| image-20230530-200324.png | image | 38 | 2023-05-30 | listed only |
| image-20230530-201911.png | image | 88 | 2023-05-30 | listed only |
| image-20230608-214214.png | image | 64 | 2023-06-08 | listed only |
| IMG_0007-19800101-070000.jpg | image | 4267 | 2023-07-20 | listed only |
| image-20230720-224026.png | image | 2374 | 2023-07-20 | listed only |
| image-20230720-224048.png | image | 3923 | 2023-07-20 | listed only |
| image-20230720-224057.png | image | 2501 | 2023-07-20 | listed only |
| image-20230720-224108.png | image | 2957 | 2023-07-20 | listed only |
