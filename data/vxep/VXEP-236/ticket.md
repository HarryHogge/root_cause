# VXEP-236: Systemic SD card Investigation VXE-522 XCOM board failures at LM Source inspection

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-01-12
- **Updated:** 2026-07-08
- **Resolved:** 2025-05-19
- **Reporter:** Pat Wells
- **Assignee:** David Grosher
- **Creator:** Pat Wells
- **Labels:** GS_Closed
- **Parent:** VXEP-444 Sustainment: VXE-30 (inc'l minor issues and improvements)
- **Links:** is cloned by VXEP-237 (VXE-529 XCOM board failures at LM Source inspection); relates to FS2-1661 (XCOM board failures at LM Source inspection); relates to VXEP-235 (Source new version of PN 100-104382 SD Card, current version is expiring); relates to FS2-310 (VXEP - SD Card file corruption (VXEP-236,237,414)); relates to RMA-276 (VXE-499 Center Wing 240625 Edge Riga FLOPS); relates to RMA-300 (VXE 590 Center Wing 240731-1  MOLSON); relates to RMA-301 (VXE 635 Center Wing 240731-2 MOLSON); relates to RMA-307 (240812-1 Center Wing VXE-595); relates to RMA-236 (VXE 532 Center Wing 240418-1); relates to RMA-286 (VXE-623 TIQ MOD 240703-1); relates to RMA-248 (VXE-548 240516  ); relates to RMA-323 (240823-4 PMA263 VXE-503 Center Wing); relates to RMA-322 (240823-3 Center Wing Tail # 4019 Spare); relates to RMA-321 (240823-2 Center Wing VXE-628); relates to RMA-320 (240823-1 Center Wing VXE-596); relates to RMA-309 (VXE-529  Avionics box 240819); relates to VXEP-612 (SD Card Reliability Corrective Actions); relates to RMA-355 (VXE-540 Center Wing 240923-2); relates to RMA-340 (RMA 240911 VXE-685); relates to RMA-364 (VXE-706 241001); relates to RMA-362 (VXE-633 240926-1); relates to VA-2122 (Red AP replaced SD card and unable to access files after format); relates to VA-2123 (VXE-592 Purple SD corruption observed); relates to VXEP-1134 (Connector Epic to MP)
- **Customer:** TIQUILA
- **Vehicle Tail Number:** 522 & 529
- **Corrective Action:** - Tracked here:https://jenaero.atlassian.net/browse/VXEP-612
- **Other Stakeholder (as required):** Connor Peebles
- **Severity:** 2 - Degraded Performance - No Workaround
- **Impacted Disciplines:** Hardware
- **Impacted Core Subsystems:** Comms Systems
- **Product/Tech Owner:** David Grosher
- **Program (Marquee):** VXE30 Incident Investigation
- **Job Number:** J100084 - VXE Incident Investigation

## Description

Corrective Actions: https://jenaero.atlassian.net/browse/VXEP-612 
Systemic investigation SD Card Failure investigation.pptx
Sheet data: https://jenaero-my.sharepoint.com/personal/dgrosher_edgeautonomy_io/Documents/Documents/SD%20investigation%20data%20summary.xlsx?web=1 
Original Files:  Larger Scale SD Card investigation
New Location: https://jenaero.sharepoint.com/:f:/r/sites/IRAD/Shared%20Documents/General/Projects/VXE_Quality_Improvements/Engineering%20Investigation%20-%20LM%20SCAR%2034139-0%20(SD%20Card%20Issue%20Aircraft%20Connection%20Issue)?csf=1&web=1&e=dRlsHU 
 Action Item List - SD Card and Aircraft Connection.xlsx

## Plan

Updated 10/21 
- Update ppt to latest status. Add main investigation info and plans. Cam, Connor, etc.
- Kickoff 8D investigation @Matt Philley @Steve Stack
- https://jenaero.atlassian.net/browse/VXEP-741
- https://jenaero.atlassian.net/browse/VXEP-738 
- Data requested. Need to populate.
- In progress testing; testing both old & new SD cards to failure https://jenaero.atlassian.net/browse/XKIT-2713
- »Attempt to recreate on VXE card.
- »Attempt to prove new cards are more rugged and qualify them
- [VXEP-627] VXE-522 / VXE-529 / VXE-508 Follow up testing: Thermal Cycle SD Cards to Failure - Jira (atlassian.net)
- [VXEP-636] VXE-522 / VXE-529 / VXE-508 Follow up testing: Gather thermal profile on 100-104382 while installed in standard VXE30 box - Jira (atlassian.net)
- Ordering thermal tape to apply to shipping cases to record max storage temps. Testing SD card temps during operation with MAGNSS testing.
- [VXEP-331] VXE-522 / VXE-529 / VXE-508 Follow up testing: Test SD Card connection while on shaker table - Jira (atlassian.net)
- Abel discussing with SanDisk failure investigation/electron microscope.

## Issue Status

See https://jenaero-my.sharepoint.com/personal/dgrosher_edgeautonomy_io/Documents/Documents/SD%20investigation%20data%20summary.xlsx?web=1

## Root Cause

- SD Card became corrupted. There are many different reasons an SD Card can become corrupted. We know the SD card write operation occurs in blocks every few seconds, if a power event occurred mid-write it could have corrupted the data or the card may have been faulty from the factory.
- Code is stuck waiting for a SD Card read in its initialization routine
- Removing the corrupted SD Card allows boot to succeed.
- Voltage leakage while unpowered and in storage causes a stored bit to flip from 1 to 0 and results in file and file system corruption.

## Comments (41)

### Pat Wells, 2024-01-12

@Douglas Baker @Marc Richardson 
FYSA

### Cameron Chapman, 2024-01-12

@Pat Wells are you available to assist with the following.
- Search for a Jira incident for each of the issues below. Create one if not able to find one quickly. 
- 529
- #1 - RTV voids -Assign to @Matt Philley or @Marc Richardson 
#2 #3 - Gouge lift boom L -Assign to Matt.
#4 - AC not connecting to GCS -Assign to Matt to locate the hardware, then assign to me once delivered.
- 522
- -AC cannot connect to GCS -Assign to Matt to locate the hardware, then assign to me once delivered.

### Matt Philley, 2024-01-16

@Cameron Chapman @Pat Wells the remaining issues on AC529 (RTV voids and “gouge”) have already been addressed by @Steve Stack 
The aircraft are already back with LM Source Inspection.

### Pat Wells, 2024-01-16

@Cameron Chapman the only two issues LM is requesting RCCA on is the Xcom failures in the two ACFT. (AC not connecting to GCS).
@Matt Philley  FYSA

### Matt Philley, 2024-01-16

Added some aircraft history to the description

### Connor Peebles, 2024-03-20

Electrically these boards are OK.
 
They both had the same problem upon start-up where the micro-controller goes from calling the bootloader to initializing the HEX file and then it would get stuck in a loop here where it continuously resets every 5 seconds or so in an attempt to properly initialize the HEX file. This is probably due to some corruption in the HEX file as stored on these XCOMMs.
 
Attempts to re-flash one of the XCOMMs leads to the expected “the device is code protected” error, as normally an XCOMM update is done through the webpage and not the initial programming software. Maybe we can get them re-flashed, but it just goes to show that it is something wrong with the code and not with the hardware.
 
This is from my observations and rudimentary understanding of the code.

### Cameron Chapman, 2024-03-20

@Connor Peebles great work diagnosing these. Some follow up questions. 
- What do you think could have caused this corruption? The aircraft seemed to operate normally during initial checkout, SCO, and another SCO 3 months later, but then not work 2 months after that.
- If the issue was with the code and not the hardware, it seems likely this would happen on more vehicles, rather than 2 very close tail numbers that were likely assembled, checked out, and stored at similar times. 
- Might be related to a payload or other unique LM setup at that time.
- Do you think the next steps should be the following:
- Check with software group to see if they would like to save existing files to determine the cause of the corruption.
- After that, attempt to reflash and see if everything operates normally.
- Possibly allocate to a HIL for continued testing/monitoring.

### Connor Peebles, 2024-03-22

@Cameron Chapman 
- Yes, it is a curious issue. I have some ideas for checking other lines on the board such as the SPI lines to make sure something isn’t pulling up when it should be pulling down.
- If it is corrupted firmware, then really the only things that could do that are hardware failure, a significant radiation event, or some in-system rewriting.
- .
- Once the XCOMM is first flashed, it becomes code protected. From then on, the only way to push code to the XCOMM is through the GCS or the webpage, which can’t be accessed in their current state.
- APBL (JAI Software Bootloader) will not connect to the XCOMMs either.
- I can keep spending time trying to reflash these XCOMMs, but the likely-hood of successful troubleshooting would probably greatly increase if this case was handed off entirely to the software group.


I’ll spend some more time hardware troubleshooting before passing it off to software.

### Greg Fryer, 2024-03-25

@David Grosher Looks like we need to assign someone from the SW team to look. Stupid question: who’s got time, since this is highly visible.

### Cameron Chapman, 2024-04-02

@Connor Peebles this issue seems to be getting hotter from the customer perspective. Do you have any time today to complete your actions and handoff to software? 
@David Grosher do you have anyone available to support? 
FYI @Kat Gulstad

### David Grosher, 2024-04-02

@Cameron Chapman @Connor Peebles Where is the investigation report? I see hints of analysis in the comments.

### Connor Peebles, 2024-04-02

@David Grosher @Cameron Chapman I did not make an incident report yet

### Connor Peebles, 2024-04-02

@David Grosher I will update the investigation report with current findings in a moment, but in the meantime it would greatly help if SW could identify exactly what is going on with the LED’s seen on this video: VXE522_LOOP.mp4, found in: Flight Safety - Videos - All Documents (sharepoint.com)

Basic summary is:
- The PIC32 is not being reset by any reset pin
- The 3.3V regulator powering the PIC32 is working fine
- The PIC32 never loses power
- The 3 blue LEDs on the back of the XCOMM are resetting with the Red/Blue/Green LEDs that are usually associated with the PIC32 bootup.
- The ENABLE pins the the SERVO POWER regulators are being cycled when this happens.
- Which points to the PIC32 pulling those pins in some function again and again, in some state between bootload and firmware initialize
- This is why I believe there is some sort of loop that we are stuck in


I’ll keep poking around, but if SW can identify a specific component or function through where the initialization gets halted, that would be much appreciated.
@Cameron Chapman

### Scott Whitney, 2024-04-02

I will talk with @Kurt Burian about looking into this when he returns tomorrow.

### Connor Peebles, 2024-04-03

I’ll comment on 522 and 529 in this thread as they are now somewhat diverging:
Both 522 and 529 XCOMM came back with this same looping problem: (see here: VXE522_LOOP.mp4) where it would not fully boot.
522:
Last week, it seems like I was able to temporarily connect to 522 XCOMM over MPLABs and was able to push the bootloader onto it again. Most attempts and any attempts to do so of 529 would reject connection saying “this device is code protected” so we know the former flash is still on there.
After pushing the bootloader, the XCOMM was no londer in the loop but I haven’t been able to connect to 522 XCOMM over APBL. The firmware flash is probably still on it.
529:
529 XCOMM we removed the SD Card and the XCOMM was able to fully boot and make it to the XCOMM webpage: 
We put the SD card back into the XCOMM and could see that some files were corrupted. The SD card was reformatted and it now works again with the SD Card installed.
[embedded: image-20240403-180502.png]

I am not aware of how the boot-up sequence interacts with the SD Card, but I am pretty sure that whatever was corrupted on the SD Card kept the boot-up from finishing and put it into that loop.
@David Grosher @Cameron Chapman @Scott Whitney @Kurt Burian

### Connor Peebles, 2024-04-03

assigning to @Scott Whitney, ready to handoff for software troubleshooting. The XCOMMs for 522 and 529 are on my workbench, same SD Cards are still installed. The investigation report in the description is update to current status.

### Kurt Burian, 2024-04-03

Talked to Connor and sounds like replacing the SD cards fixed the issue. We have seen boot failure both from SD card read errors and firmware downgrade causing memory corruption. We know the SD card write operation occurs in blocks every few seconds, if a power event occurred mid-write it could have corrupted the data or the card may have been faulty from the factory. To prevent the former we would need a super-cap to power the XCOMM while the last write operations are completed after power has been disconnected. We already store a backup of the SD card data in flash memory which allows the system to rebuild corrupted files in most circumstances, however, if the file system on the card is completely inaccessible these mechanisms likely wont work, requiring a card reformat.
One of the troublesome boards has already been reformatted so I wont be able to breakpoint the line number it gets stuck on during initialization, however, I will try to hook a debugger up to 5-5306 and determine where its failing and if a ‘try/catch’ type solution could be feasible.

### Kurt Burian, 2024-04-03

Flashed with 4.67 debugger. Code is stuck waiting for a SD Card read in its initialization routine. Removing the corrupted SD Card allows boot to succeed. To have this error fix itself, low level driver would need a rewrite to timeout and upper layer code would need to be modified to trigger a reformat, a significant amount of work.  
Attempted SD Card reformat. No change in behavior after format. Tried reformatting disk using windows laptop. Drive was not recognized by Windows. 
Next Action: Suggest replacing SD Card on 5-5306.
[embedded: image-20240404-023330.png]
[embedded: image-20240404-024052.png]

### Connor Peebles, 2024-04-04

Thanks Kurt! I’ll update the Jira tickets and the investigation reports with your findings, suggested corrective action. I think we have all the information we need to give a good answer to LM.
I’ll summarize this as very low flight risk, but there is risk of failure on the ground (failure to boot) which is about as high as the odds of an SD becoming corrupted (which isn’t common but not really rare, ask any photographer).

### Connor Peebles, 2024-04-04

Moving Jira tickets to D5

### Kurt Burian, 2024-04-04

Placed 5-5306 back on Connors bench. Needs new SD card along with production bootloader and firmware reinstalled. Suggest standard SEO checkout before returning to customer.

### Connor Peebles, 2024-04-04

@Cameron Chapman For review.
I updated the combined Investigation Report, as well as all the fields. I also created linked subtasks for the corrective actions.

### Cameron Chapman, 2024-04-05

Hi @Kat Gulstad we have identified cause and potential corrective actions. Since this issue will not happen during flight (unless the XCOM rebooted, which would already likely cause a crash), no containment should be required, just directions to the customer for how to verify and remedy this issue. 
Let us know what else we can help with for this. Assigning to you.

### Matt Philley, 2024-04-08

@David Grosher @Cameron Chapman @Steve Stack @Ryan Ferguson 
Follow-up on the suspected vendor issue comments about the SD Cards.
PN:  100-104382 - Sandisk Ultra Micro SD Card, 64GB (SDSQUNC-064G-GN6MA)

I spoke with Ryan F and we have the following notes/comments:
- Any reference to there being a vendor issue was more of a “suspected” cause. There has been no specific trend identified with any specific vendor lot or batch.
- These cards are not marked with any specific lot or batch information. They were historically ordered from Amazon, but now through Fastenal.
- We suspect this might be a situation where the vendor spec for this card might have a larger acceptance window in one or more parameters then what the XCOM board wants. (i.e. some read/write speed or something)
- We think there could be opportunity to dive deeper to take a corrupted SD card and perform read/write speed analysis or some other compare/contrast analysis to see if we can find some parameter that is performing different we can point to and maybe develop some form of screening procedure
- Carson mentioned that during development Gordon tried 20+ different brand, spec, size, SD cards to try and find something that would work, so this may also point to some “uncontrolled” parameter that is important to the XCOM but may not be readily controlled by vendor(s). Or perhaps that SD cards are just not the robust “production” solution in this situation and it was something that made sense for development when some percentage of failures was more tolerable.

NOTE: The model of SD card we are using for XCOM and Red AP did change and the vault was never updated(?)
https://jenaero.atlassian.net/browse/VXEP-235 
Is: Sandisk - SDSQUAB-064G-GN6MA [we may have been using this since Jan 2023?? found in AC 508, 522, and 529 XCOMM]
Was (still currently shown in vault): Sandisk - QUNC-064G-GN6MA

### Matt Philley, 2024-04-08

@Kat Gulstad @Pat Wells @Cameron Chapman @David Grosher @Steve Stack 
FYSA
AC 508 (RMA for FBI for similar connection issue) troubleshooting per Connor’s guidance shows same issue as AC 522 and 529 where removal of the SD card allows board to start-up. Connor agreed this appears to be the same cause. We have replaced the SD card and its going through rework/checkout in Eshop now. 
AC 525 (RMA for USASOC for “GCS could not connect to AC”) this is already in SCO post-rework, but was determined to be an SD card failure. SD card was replaced and checkout successful in Eshop. 
These two are recent RMAs within similar timeframe as TIQUILA… with same issue.

### David Grosher, 2024-04-08

@Kat Gulstad @Pat Wells @Cameron Chapman @Matt Philley @Steve Stack FYSA
I spoke with Kurt regarding this issue and we believe it may be possible unblock the initialization when a corrupted SD card is present. The containment would be to trigger a fault such that the launch Wizard can’t be passed, send the operator an error message and enable the reformat of the SDcard via the same webpage functionality that currently exists. Given that at least one SD card could not be reformatted this won’t work in every case, but it could allow for some number of the issues to be resolvable in the field.

### Matt Philley, 2024-04-08

Duplicating this comment since I am not sure if its related to investigation or just the approval of this yet…
Ryan and I did a spot-check on some old problem XCOM and red AP boards hes been collecting and it looks like for some period of time… maybe mid-2022 to mid-2023(?) we were using a mixture of both SD cards. No idea if this relates to our SD card corruption issue, but worth knowing either way. 
We found “new” SDSQUAB-064G-GN6MA SD cards in boards from 2022.
We also found “old” QUNC-064G-GN6MA SD cards in boards from mid-2023.

### Connor Peebles, 2024-04-08

@Cameron Chapman I added:
 https://jenaero.atlassian.net/browse/VXEP-331 
https://jenaero.atlassian.net/browse/VXEP-332 and
https://jenaero.atlassian.net/browse/VXEP-333 
as follow-up testing tasks.
@Matt Philley @Ben Norris @David Grosher

### Ryan Ferguson, 2024-04-08

One source of failure we have known of for some time is power cycling while the SD card is being accessed.  This is hard to pin down the severity of the issue due to the lack of more detailed information on how often this occurs.  If there is value in this, I can write a script for the TAS to power cycle a batch of 8 “sacrificial” APs with fresh SD cards.  It can boot up the autopilot, wait a random time between 0 and 5 minutes, then abruptly pull power from the AP.  I can have the TAS check every few boots to determine if the AP is still alive and the SD card functioning.  If I set this up over a weekend we can get a pretty large number of power cycles with no impact to production.

Would there be value in such a study being performed?  This could estimate approximately how many times an autopilot can be rebooted on average before it is expected to have a corrupt SD card due to this failure mode.

### Ryan Ferguson, 2024-04-08

I would also like to provide another possibility which gets around the electrical design limitations of the autopilot and X-comm.  We have certification requirements from the customer which prevent us from making changes to either board, but the addition of a supercapacitor would possibly help with the SD corruption issues.  It may be possible for us to add a supercapacitor to the existing boards by soldering leads to a capacitor and terminating it with a DF13 header, allowing us to simply plug in the supercapacitor as an add-on to the existing boards.  We can retrofit planes with this cheap and easy solution as needed.  There would be some other constraints that the EE team will have to investigate before this is a viable option (reverse voltage on the 3.3v regs, voltage monitoring, etc) but this could be an option to pursue as a short-term solution before we spin either board in the future.

### Ryan Ferguson, 2024-04-08

I was also asked to note how I detect SD corruption in the TAS.  Since I screen large batches of autopilots every run, the SD corruption detection has become an incredibly important function in the automation.  The TAS has 3 main methods of detecting SD corruption:
- Document Source: The index page of the autopilot will show document source: ROM if there is no SD card available.  If the TAS detects this, it will attempt to reformat the SD card and reboot.  If the autopilot doesn’t change to show Document Source: SD after a couple rounds of this, the TAS will reject the autopilot as it is almost definitely experiencing a hardware failure in the SD card or related circuitry.  The TAS could use some updates here however as sometimes the failure goes away after a simple reboot without doing any reformatting.
- File Structure Corruption: If I list the root file structure using FTP, I will get a string of all files and folders.  Python expects the encoding of these characters to be ISO-8859-1 (Had to make assumptions, our AP documentation doesn’t specify FTP encoding).  If an SD card is corrupted, it will frequently return characters that do not fit in this encoding.  This is rarely a hardware related failure (have yet to see it caused by anything other than power cycles), so the TAS will attempt to reformat the SD card and reboot.  Just like the document source failure mode, the TAS will try this twice before rejecting.
- No response over HTTP: One of the first steps the TAS performs is to log in to all autopilots and get their index pages.  If an autopilot experiences the boot loop failure seen in aircraft 525’s X-comm, the TAS will terminate the run.  This is usually a failure so severe the TAS cannot properly detect the failure source and can be caused by many other failure modes.  The operator must then do some investigation on their own to determine actual root causes.


If examples of these checks are needed, I can provide code snippets from the TAS repos.  The file structure corruption would be in theory pretty easy to detect automatically from the autopilot or GCS and prompt the operator to reformat prior to flight.

### Ryan Ferguson, 2024-04-17

I have completed my study to determine if autopilots having power pulled from them unexpectedly can cause corruption.

Test methodology:
The TAS codebase was stripped to perform this test.  The code alternates between two modes for every cycle:
-- Randomized power cycle mode: The TAS powers up all 8 autopilots then chooses a random number from 0 to 300 seconds, corresponding with up to 5 minutes.  The TAS waits that many seconds then turns off the autopilot.  This random number is chosen for each of the 8 autopilots, allowing for more variation in timing.
-- Corruption check mode: The TAS powers up all autopilots, waits 30 seconds, then attempts to ping each autopilot.  It will then attempt to log into the autopilot for 5 minutes.  Once logged in, it will attempt to read the document source (normally SD) from the index page.  After this, it will check the SD card for corruption using the file structures corruption method noted in the previous comment.  If it detects corruption, the TAS will attempt to reformat the SD card.  Once all checks are completed, the TAS shuts down the autopilot.
For every cycle the TAS makes, the autopilots will be rebooted twice.  

Results:
Every time the TAS runs, it will generate a dictionary of results which looks like this:
{'Timestamp': '2024-04-17 14:35:34.613423', 'AP Position': '1', 'Randomized Uptime': 229.26409771314852, 'Ping Check': 'True', 'Login Check': 'True', 'Document Source': 'SD', 'SD Corruption Check': 'None', 'Reformat Attempted': None, 'Uptime at Shutdown': 78}

The TAS logs these to a spreadsheet for later review which I have attached to this post.
[embedded: VXEP-236 Results.xlsx] 


Analysis:
There are a total of 2893 records in the spreadsheet above.  This corresponds to the TAS rebooting the batch of 8 autopilots a total of 361 times.  

Of the entries, there were a total of 12 records of autopilots not responding to ping after 30 seconds of uptime.  This is explained by Autopilot 4 which was experiencing unusual traffic from the TAS for unknown reasons.  This would likely not mean anything substantial for an aircraft.

Of the other checks performed, 100% of the autopilot samples had no failures in the login checks, document source checks, or SD corruption.  Based on this, there appears to be no connection between randomized power disconnection and SD corruption in the sample of 8 autopilots studied.  

The results of this study do not control for a larger population of autopilots.  It is possible that hardware differences between autopilots may make one autopilot more prone to SD corruption failure than the small sample of 8 AP’s studied here.  The autopilots chosen in this study were 8 random NCR scrap/retain autopilots that had other unrelated issues with their IMUs and other peripheral issues unrelated to SD card functionality.


Theories:
The results above suggest that failure of the SD cards is likely caused by a mechanism other than power being unexpectedly pulled.  There may be some effect where SD cards left unpowered for extended periods may lose their data.  This is supported by this StackExchange post where leakage is noted as a common failure mode of SD cards left unpowered for extended periods.  

If leakage is determined to be the main contributing factor, planes left unpowered for extended periods can be expected to experience SD corruption when powered on for the first time.  This will not affect planes in regular use as significantly since the SD card will be continuously recharging its NAND flash cells during use.

### Matt Philley, 2024-05-01

@David Grosher is this topic still being worked? It looks like the corrective actions summarized above do not take into account Ryan’s analysis below and suspicion that the issue may be an issue with the AC being unpowered for a long time and not with power being pulled.

### David Grosher, 2024-06-27

@Steve Stack Use this Jira ticket as the source of analysis regarding the issue. Ryan analysis below in the comments shows that the leakage (bit rot) issue is more likely than not the source of our problems, although it is not conclusive.  This is supported by the fact that all of the new related incidents are with birds being pulled out of storage. Low quality components or counterfeit components may complicate the issue further. As I have mentioned before, the root cause is not critical in this investigation because the proposed corrective action will address all of the potential root causes. The CA is https://jenaero.atlassian.net/browse/VXEP-413 and https://jenaero.atlassian.net/browse/FS2-1661. You will need to pull information from these sources for your report.

### Steve Stack, 2024-06-27

@David Grosher (Jira)<jira@jenaero.atlassian.net>
Those Jira pages are the same ones that I’ve been looking at where we don’t understand how or why the SD-Card became corrupted, so we have no root cause for the failure.  Because we don’t understand the root cause of the failure also means that we don’t know how to prevent it from happening in the first place.
To me this situation is like buying a car and the dealer tells you to that you will need to squirt ether into the intake to get it to start.  You’ve been taught how to start the car, but the problem is not fixed and most likely you’re going to buy a different brand of car.
This type of activity is called a correction, not a corrective action.  Is this really the best solution we can come up with?
S
@Marc Richardson<mrichardson@edgeautonomy.io>

### David Grosher, 2024-07-03

@Douglas Baker Additional context

### Cameron Chapman, 2024-09-05

9/5 meeting notes. Need to open and track subtasks.
4 issues. Evidence indicates likely not EA HW related. 
- Conterferfeit, less reliable.
- Two part numbers. ECN.
- SCO, verify logs.
- SDSQQVR-064G-GN6IA
- WDD064G1P0C
- Abel confirm these specific PNS
- Plan to test and approve. Confifgure, SCO, fly, review logs. Approve for all. Containment.
- Containment of current cards.
- May be more locations.
- Kingston cheap. Not recommended. https://jenaero.sharepoint.com/sites/JAI_Operations/Lists/Sharepoint%20Contact%20List/DispForm.aspx?ID=135&env=WebViewList&loadFormWithNucleus=1&id=*
- Better formatting. Should be field fixable with FW updates.
- Environmental 65C SD card current rating. Likely much higher in operation and storage. Plan to implement temp indicator stickers. Link to MAGNSS thermal testing.
- Configuration errors. SD card did not get formatted correctly. Reports formatted even if failed. SCO should catch this. Need to ensure they do.

### Cameron Chapman, 2024-10-21

Old 522 Status (since this issue has been repurposed as the systemic issue: 
- The PIC32 is not being reset by any reset pin
- The 3.3V regulator powering the PIC32 is working fine
- The PIC32 never loses power
- The 3 blue LEDs on the back of the XCOMM are resetting with the Red/Blue/Green LEDs that are usually associated with the PIC32 bootup.
- The ENABLE pins the the SERVO POWER regulators are being cycled when this happens.
- Which points to the PIC32 pulling those pins in some function again and again, in some state between bootload and firmware initialize

Last week, it seems like I was able to temporarily connect to 522 XCOMM over MPLABs and was able to push the bootloader onto it again. Most attempts and any attempts to do so of 529 would reject connection saying “this device is code protected” so we know the former flash is still on there.
After pushing the bootloader, the XCOMM was no londer in the loop but I haven’t been able to connect to 522 XCOMM over APBL. The firmware flash is probably still on it.
- Code is stuck waiting for a SD Card read in its initialization routine
- Removing the corrupted SD Card allows boot to succeed.

Next Action: Replace SD Card on 5-5306.

### Cameron Chapman, 2024-10-21

VXE-522 & 529 XCOM boards failed at LM Source inspection for TIQUILA program.
LM requesting root cause / corrective action / impact to over all fleet if any.for the XCOM issues. 
Links to associated NCR’s:
https://jenaero.sharepoint.com/sites/JAI_Operations/Lists/NCR%20List/DispForm.aspx?ID=1991&commentId=12&e=6b3UcE8VH0qiDcQneyB1gw&at=15 
https://jenaero.sharepoint.com/sites/JAI_Operations/Lists/NCR%20List/DispForm.aspx?ID=1971&commentId=10&e=4tE9kKI1R0etktOt2cOo5g&at=15 
@Sean Odell has the two XCOM boards and can pass off for investigation. 

Aircraft History Summary:
June/July - Aircraft Production Complete (AC completed SCO checkout and Test Flight)
July - Aircraft put in queue for Source Inspection
July - Aircraft complete Source Inspection Checkout by LM and Invoiced
Sept/Oct - Aircraft still in SLO & identified as needing Silvus Radio Replacement for Silvus Radio Containment. Radios Replaced & AC verified in SCO
Oct - Aircraft delivered back to LM Cage for Source Inspection
Dec - During LM Source Inspection LM unable to connect to Aircraft from Ground Station. 
- Carson helped troubleshoot, so we brought it back to SCO and verified we also cannot connect to Ground Station
- Both AC had same issue within 1 week from one another. We initially suspected faulty payload fried XCOMM, but payload checked out fine
- NCR dispo to replace XCOMM suspecting a dead network chip
- XCOMM boards replaced for both AC, pass Avi Box checkout in Electronics, and pass SCO checkouts
- AC re-flown, pass final checkout

Jan - Aircraft final checkout completed, squawks resolved, aircraft delivered back to LM for Source Inspection

3/19 Matt C (LM) email
Sorry if this was already covered (soo many emails), but can we get an explanation from Edge on what happened with the Xcomm boards?   How did these get thru Edge QA and SCO, and is there something we should be watching for?
 
We are trying to get ahead of this becoming a PTR with the airworthiness team.
 
Also, we would like to have copies of the flight SCO that occurred 12/22/23.  Ours are dated 6/30/2023.
Investigation Report: VXE-522 & VXE-529 XCOMM board failures at LM Source inspection.pptx
Found in: VXE-522 XCOMM board failures at LM Source inspection

### Christa Meck, 2025-04-17

Removed parent to prep for Incident hierarchy change.  Parent is linked as Linked issue.

### David Grosher, 2025-05-19

Closed with Containment delivered in v6.4 and Industrial SD card.

## Attachments (10)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [VXE-522 12-22-2023 FLight Paper Work and Rework.pdf](attachments/18306_VXE-522%2012-22-2023%20FLight%20Paper%20Work%20and%20Rework.pdf.md) | pdf | 1469 | 2024-01-12 | converted |
| [VXE-529 12-22-2023 FLight Paper Work and Rework.pdf](attachments/18305_VXE-529%2012-22-2023%20FLight%20Paper%20Work%20and%20Rework.pdf.md) | pdf | 1405 | 2024-01-12 | converted |
| image-20240403-180502.png | image | 137 | 2024-04-03 | listed only |
| image-20240404-023330.png | image | 95 | 2024-04-03 | listed only |
| image-20240404-024052.png | image | 67 | 2024-04-03 | listed only |
| SD Card Location on XCOM in Avionics Enclosure Assy.png | image | 788 | 2024-04-08 | listed only |
| [VXEP-236 Results.xlsx](attachments/20099_VXEP-236%20Results.xlsx.md) | xlsx | 131 | 2024-04-17 | converted |
| image001.png | image | 1 | 2024-06-27 | listed only |
| image002.png | image | 0 | 2024-06-27 | listed only |
| image003.png | image | 4 | 2024-06-27 | listed only |
