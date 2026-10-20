# VXEP-237: VXE-529 XCOM board failures at LM Source inspection

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-01-16
- **Updated:** 2025-05-19
- **Resolved:** 2025-05-19
- **Reporter:** Cameron Chapman
- **Assignee:** David Grosher
- **Creator:** Cameron Chapman
- **Labels:** FlightSystems
- **Links:** clones VXEP-236 (Systemic SD card Investigation VXE-522 XCOM board failures at LM Source inspection); relates to FS2-1661 (XCOM board failures at LM Source inspection); relates to FS2-310 (VXEP - SD Card file corruption (VXEP-236,237,414)); relates to RMA-276 (VXE-499 Center Wing 240625 Edge Riga FLOPS); relates to RMA-300 (VXE 590 Center Wing 240731-1  MOLSON); relates to RMA-301 (VXE 635 Center Wing 240731-2 MOLSON); relates to RMA-307 (240812-1 Center Wing VXE-595); relates to RMA-236 (VXE 532 Center Wing 240418-1); relates to RMA-286 (VXE-623 TIQ MOD 240703-1); relates to RMA-248 (VXE-548 240516  ); relates to RMA-323 (240823-4 PMA263 VXE-503 Center Wing); relates to RMA-322 (240823-3 Center Wing Tail # 4019 Spare); relates to RMA-321 (240823-2 Center Wing VXE-628); relates to RMA-320 (240823-1 Center Wing VXE-596); relates to RMA-309 (VXE-529  Avionics box 240819); relates to RMA-355 (VXE-540 Center Wing 240923-2); relates to RMA-340 (RMA 240911 VXE-685); relates to RMA-364 (VXE-706 241001); relates to RMA-362 (VXE-633 240926-1)
- **Issue color:** purple
- **Customer:** TIQUILA
- **Vehicle Tail Number:** 522 & 529
- **Other Stakeholder (as required):** Marc Richardson
- **Severity:** 2 - Degraded Performance - No Workaround
- **Impacted Disciplines:** Hardware
- **Impacted Core Subsystems:** Comms Systems

## Description

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
Investigation report: VXE-522 & VXE-529 XCOMM board failures at LM Source inspection.pptx

## Corrective Action

- Provide instructions to customers to identify SD Card as problem, replace, and re-format SD Cards on their own or ship Avionics Box back to Edge Autonomy RMA to do so.
- https://jenaero.atlassian.net/browse/VXEP-319


- To have this error fix itself, low level driver would need a rewrite to timeout and upper layer code would need to be modified to trigger a reformat
- a significant amount of SW work.
- https://jenaero.atlassian.net/browse/VXEP-320


- To attempt to prevent SD Card corruption: add a super-cap to power the XCOMM while the last write operations are completed after power has been disconnected
- XCOMM will need to understand that it has lost main power and is booting down
- During this, tell PIC32 to not read or write from SD Card
- https://jenaero.atlassian.net/browse/VXEP-321
- @Ryan Ferguson do you have any information or tracking of SD card issues, bad batches, ways to identify them, etc?

## Plan

@Ryan Ferguson do you have any information or tracking of SD card issues, bad batches, ways to identify them, etc? 
Determine how this relates to https://jenaero.atlassian.net/browse/RMA-230. These should get a Jira incident if engineering is involved in troubleshooting. 
Quick research if long term storage increases the odds of SD card corruption. 
Review for additional actions.

## Issue Status

- The PIC32 is not being reset by any reset pin
- The 3.3V regulator powering the PIC32 is working fine
- The PIC32 never loses power
- The 3 blue LEDs on the back of the XCOMM are resetting with the Red/Blue/Green LEDs that are usually associated with the PIC32 bootup.
- The ENABLE pins the the SERVO POWER regulators are being cycled when this happens.
- Which points to the PIC32 pulling those pins in some function again and again, in some state between bootload and firmware initialize

529 XCOMM we removed the SD Card and the XCOMM was able to fully boot and make it to the XCOMM webpage:
We put the SD card back into the XCOMM and could see that some files were corrupted. The SD card was reformatted and it now works again with the SD Card installed.

## Root Cause

- SD Card became corrupted. There are many different reasons an SD Card can become corrupted. We know the SD card write operation occurs in blocks every few seconds, if a power event occurred mid-write it could have corrupted the data or the card may have been faulty from the factory.
- Code is stuck waiting for a SD Card read in its initialization routine
- Removing the corrupted SD Card allows boot to succeed.

## Comments (14)

### Marc Richardson, 2024-03-20

@Cameron Chapman @Connor Peebles Was there any troubleshooting performed on the XCOM board? @Steve Stack @Douglas Baker

### Connor Peebles, 2024-03-20

Electrically these boards are OK.
 
They both had the same problem upon start-up where the micro-controller goes from calling the bootloader to initializing the HEX file and then it would get stuck in a loop here where it continuously resets every 5 seconds or so in an attempt to properly initialize the HEX file. This is probably due to some corruption in the HEX file as stored on these XCOMMs.
 
Attempts to re-flash one of the XCOMMs leads to the expected “the device is code protected” error, as normally an XCOMM update is done through the webpage and not the initial programming software. Maybe we can get them re-flashed, but it just goes to show that it is something wrong with the code and not with the hardware.
 
This is from my observations and rudimentary understanding of the code.

### Cameron Chapman, 2024-03-20

Currently being troubleshot with 522 XCOM. Tracking there. We can separate if the investigations separate later https://jenaero.atlassian.net/browse/VXEP-236

### Connor Peebles, 2024-04-03

522:
Last week, it seems like I was able to temporarily connect to 522 XCOMM over MPLABs and was able to push the bootloader onto it again. Most attempts and any attempts to do so of 529 would reject connection saying “this device is code protected” so we know the former flash is still on there.
After pushing the bootloader, the XCOMM was no londer in the loop but I haven’t been able to connect to 522 XCOMM over APBL. The firmware flash is probably still on it.
529:
529 XCOMM we removed the SD Card and the XCOMM was able to fully boot and make it to the XCOMM webpage:
We put the SD card back into the XCOMM and could see that some files were corrupted. The SD card was reformatted and it now works again with the SD Card installed.
[embedded image-20240403-180502.png]

### Connor Peebles, 2024-04-03

assigning to @Scott Whitney, ready to handoff for software troubleshooting. The XCOMMs for 522 and 529 are on my workbench, same SD Cards are still installed. The investigation report in the description is update to current status.

### Connor Peebles, 2024-04-04

Updated RCCA
moving tickets to D5

### Connor Peebles, 2024-04-04

@Cameron Chapman For review.
I updated the combined Investigation Report, as well as all the fields. I also created linked subtasks for the corrective actions.

### Cameron Chapman, 2024-04-05

Hi @Kat Gulstad we have identified cause and potential corrective actions. Since this issue will not happen during flight (unless the XCOM rebooted, which would already likely cause a crash), no containment should be required, just directions to the customer for how to verify and remedy this issue.
Let us know what else we can help with for this. Assigning to you.

### Rodney Linch, 2025-04-07

@Cameron Chapman @Jason Scherer I placed a529’s avionics box on the Engineering work table. This is the original  avionics box that the customer received. We then sent a replacement avionics box which is here in SLO for an SD card swap. Let me know if you want/don’t want the avionics box because Huntsville does want it if y’all don’t!

### Cameron Chapman, 2025-04-08

@Rodney Linch did the customer receive a replacement, and is this box now ours? Is it flight worthy, or does it have any issues. HSV can likely have it pending those details.

### Rodney Linch, 2025-04-09

@Cameron Chapman - the customer did receive a replacement avionics box and AC returned (with the replacement box) to EA for SD card swaps in fuse and center wing. I do not know if its flight worthy. Should I ask final assembly to perform a functions check?  If not, I’ll recover the box and ship it to HSV.

### Cameron Chapman, 2025-04-16

@Rodney Linch I recommend asking @Desiray Johnston if these could/should be used for any planned internal asset builds. There seems to be nothing wrong other than corrupt SD cards. If she doesn’t want them, shipping them to HSV sounds good.

### Rodney Linch, 2025-04-23

@Cameron Chapman - I confirmed with Production that they do want this part. I’ll take a look in the Engineering area to pick it up.

### David Grosher, 2025-05-19

Closing with containments in v6.4 and the Industrial SD card.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [VXE-522 12-22-2023 FLight Paper Work and Rework.pdf](attachments/18323_VXE-522%2012-22-2023%20FLight%20Paper%20Work%20and%20Rework.pdf.md) | pdf | 1469 | 2024-01-16 | converted |
| [VXE-529 12-22-2023 FLight Paper Work and Rework.pdf](attachments/18324_VXE-529%2012-22-2023%20FLight%20Paper%20Work%20and%20Rework.pdf.md) | pdf | 1405 | 2024-01-16 | converted |
| image-20240403-180502.png | image | 137 | 2024-04-03 | listed only |
