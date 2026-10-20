# VXEP-319: VXE-522 / VXE-529 Corrective Action: Provide instructions to customers to identify and replace SD Card, or RMA to Edge

- **Issue type:** Sub-task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2024-04-04
- **Updated:** 2025-02-28
- **Resolved:** 2024-12-10
- **Reporter:** Connor Peebles
- **Assignee:** Pat Wells
- **Creator:** Connor Peebles
- **Parent:** VXEP-236 Systemic SD card Investigation VXE-522 XCOM board failures at LM Source inspection
- **Links:** relates to RMA-230 (VXE 508 240325-2)
- **Job Number:** J100084 - VXE Incident Investigation

## Comments (8)

### Cameron Chapman, 2024-04-05

@Connor Peebles what is the best way for a user to determine SD card corruption at the vehicle level? Just unable to connect? Confirm by replacing avionics box and confirming the issue is fixed? I do not think we want operators opening avionics boxes in the field. Please reassign to @Dana Holley once we have outlined the process recommended.

### Connor Peebles, 2024-04-05

@Cameron Chapman There are, ofcourse, many reasons an Avionics Box might not be able to connect.
A possible way of having the customer check for this error (only if they REALLY don’t want to or can’t send the avionics box back to Edge RMA):
- Can’t connect
- Open up Avioncs Box
- Power Avionics Box
- Watch Heartbeat LEDs near SD Card
- Watch for looping action where all heartbeat LEDs blink on and off every 5 seconds together
- Remove SD Card (while still powered)
- If boot succeeds, then SD Card was the problem
- Can attempt to re-install the SD Card (while powered) and reformat SD Card from XCOMM Webpage
- If failed, they would need a new SD Card installed and reformatted


In terms of powering the avionics box while open in order to debug it, that could be complicated if they do not have a bench set-up with a Black Alden debug cable to power the Avi Box
- Remove Avi-box from fuse
- Flip fuse over (in stand)
- install main battery
- unclip and pull main system harness out enough to connect to Avi box while placed on the upside down fuselage as a table


In this same regard, I propose the assembly of a debug kit to sell (or give) to customers. I am in no way considering the bad optics impact of giving debug kits, so don’t ask, I am merely stating that factually it would be beneficial for customers to have debug kits if they will not always send in problems.
- Avi box breakout harnesses
- Center Wing breakout harnesses
- Other breakout harnesses?

@Dana Holley

### Cameron Chapman, 2024-04-05

@Connor Peebles I think the answer is no, but want to confirm. Is there any way to confirm this issue without opening the avionics box (using a debug cable to some of the alden pins for example)? If not, I think we would be better off having a procedure for attempting to address the other reasons an Avbox could not connect that can be fixed externally, then send for RMA is those are not successful. I don’t think we want customers opening avionics boxes. @Pat Wells any thoughts on this?

### Connor Peebles, 2024-04-05

@Cameron Chapman @Pat Wells @Dana Holley I agree, but I know Sam has had customers open Avi boxes before. Other than maybe being able to identify a short inside the avionics box, there is not any external way of identifying why an Avionics Box may not be connecting.
- Dead network chip
- Dead processor
- Dead SD Card apparently
- random resistor or capacitor failure

### Cameron Chapman, 2024-04-05

@Pat Wells and @Sam Miller have a lot more familiarity with customer skill and willingness to open avionics boxes in the field. What do you two recommend? I would think we would not want this, but also understand the hardship of shipping equipment back from remote locations.

### Pat Wells, 2024-04-05

@Cameron Chapman I would not recommend having the operators open the avionics boxes in the field.  Standard practice at SLO when an avionics box is opened during the course of an RMA repair we require a full SCO and flight test. @Sean Odell

### Matt Philley, 2024-04-08

@Cameron Chapman @Connor Peebles I believe we separated this issue from others by connecting to the AC using the diagnostic cable… based on what pages we could see or not see as well as where power was going (i.e. with power on and servos home…) helped determine if this was a radio issue, an XCOM network issue, or something else. Carson would be a good person to provide the actual diagnosis method since it has happened multiple times in SCO.

### Matt Philley, 2024-12-10

we have drafted a formal letter to customers on this issue that Doug B and Pat W were a part of which covers the Customer comms for this topic and we have field replacement procedures as well. This topic is complete.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| SD Card Location on XCOM in Avionics Enclosure Assy.png | image | 788 | 2024-04-08 | listed only |
