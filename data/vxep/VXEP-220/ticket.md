# VXEP-220: VXE 487 - GCS blocking resulting in multiple FWAP link losses

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2023-12-12
- **Updated:** 2025-08-12
- **Resolved:** 2025-08-12
- **Reporter:** Cameron Chapman
- **Assignee:** Ted Trowbridge
- **Creator:** Cameron Chapman
- **Labels:** FlightSystems
- **Links:** relates to VXEP-101 (VXE-487 488CW Damage to Center Wing power connector -Motors stopped at 90ft during VTOL landing); relates to FS2-2332 (Investigate AP Link Loss issues on FW AP); is caused by GCSS-434 (Mission simulation blocks UI thread)
- **Corrective Action:** GCS should be updated to not block uplink messaging during mission simulation.
- **Other Stakeholder (as required):** Jason Scherer
- **Root Cause:** GCS mission simulation prevents GCS from servicing uplink resulting in vehicle reported link timeouts.
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

[embedded: image-20231212-222157.png]

## Plan

@Jason Scherer @David Grosher I know this is not to priority. When you have time. I have this avionics box on my desk. Do you anticipate it being helpful for any HIL or other investigation? If not, I can see if it is useful for an ironbird or other use. We have provided another to the customer.

Adding @David Grosher for SA
Answers below each question. -JS
@Jason Scherer What are the potential impacts of this issue? Aircraft crashes because it loses servos?
Answer: This message indicates the primary (and only) data link between the fixed wing autopilot and the XComm is sometimes in a degraded state which would prevent the Fixed Wing AP from receiving new commands such as new waypoint, RTB, Land now, etc. I don’t believe this would cause any servo issues. The FW AP should still continue to fly the vehicle per the previously uploaded mission. The effect this issue would have is more like a datalink dropout. Cam: I think it is a flight safety issue, losing this link would lose air data to the FWAP.; Jason: Yes I agree. The air data updates would stop which is a flight safety issue.

Could/should we go back in that boxes logs (A487) to see if it always had that issue or developed it?
Answer: Yes. We can do this to see how long the message has been recorded. I did find this message reported a single time in an NCR AAR file for air vehicle 537 after I went back into my incident archives to see how prevalent this issue is. Perhaps this is more common than we would like, but I only found the one other case so far. To be fair the issue on 487 seems to resolve itself quickly. 

Can you document steps of where to check it? We could have Sam o put them in the checkout procedure?
Answer: The XComm debug message log can be viewed on the XComm website. I added screenshots to navigate to it in the comment below. To recreate the issue simply connect the GCS software while monitoring the log. I was able to create the link fault reporting every time I connected the GCS software for the first time on boot up.

Additional considerations. The more I look into this issue I’m starting to have doubts that it isn’t software. I still think it is, but I’m more open minded since I had to restart the hardware to recreate the message using the GCS each time. It also doesn’t seem to occur when I shook the avionics around vigorously which isn’t what I expected. I’d really like to have someone test the 40-pin ribbon cable that connects the XComm board to the FW-AP to see if we can identify any continuity issues. At least try to isolate this best we can to a hardware or software issue. The cable test seems like low hanging fruit. It the cable checks out ok we may want to dig more into what this fault message actually means and what would cause it to be reported.

## Comments (12)

### Cameron Chapman, 2023-12-12

[Yesterday 7:10 PM] Cameron Chapman
yes, seems like a pretty clear connector failure
[Yesterday 7:11 PM] Cameron Chapman
were there any indications of abnormal voltages during launch?
[Yesterday 7:16 PM] Cameron Chapman
This page seems concerning. how common are those on other aircraft? Is that a near miss that could be covered up by the actual crash?  
 
[8:45 AM] Jason Scherer
From what I saw the voltage levels seemed ok until the end. I'll relook to verify. The ap link failures scare me as well. I would most likely suspect a bad cable, connector something along those lines rather than a software issue simply due to the fact that I don't typically see this error. In fact this is the first time I have seen it.
[8:46 AM] Jason Scherer
But on the other hand this is old firmware, so I guess it could be an old issue too
[9:15 AM] Cameron Chapman
It seems worth testing to see if we can recreate/find a cable failure. We wouldn't want to return it with the cable. May be easiest to recreate, update FW, then see if it goes away
[9:16 AM] Cameron Chapman
It seems like we are ok to return everything to RMA except the fuselage and CW. Do you agree?
[9:16 AM] Cameron Chapman
might not need CW, since the dropouts were to the FWAP. Is the CW helpful to recreate this issue?
[9:52 AM] Jason Scherer
Most likely would be a 40 pin ribbon cable issue
[9:55 AM] Cameron Chapman
good point. In that case, do you recommend testing with the whole fuselage, or just pull the avionics box out and return the rest?
[10:10 AM] Jason Scherer
So I have the avionics for 487 at my desk right now. I say we attempt to recreate the errors. Then swap the ribbon cable and see if they go away. Also we could run continuity tests (sounds not fun) on the 40 pin. If a new ribbon doesn't fix it then we have to keep looking. I don't see how it could be something outside the avionics enclosure, but it's probably best to confirm before we send the aircraft back.
[10:10 AM] Jason Scherer
I'll turn on the avionics and see if the link errors are still occurring.
[10:24 AM] Cameron Chapman
thank you. you could wiggle/shake the cable while testing to see if that creates an issue 
[10:28 AM] Jason Scherer
I can shake the avionics if I don't see the issue for a bit. I'm using a different harness to power the avionics. I haven't cracked open the case yet. Do you want anyone specifically to do that part? Document configuration, look at the connectors, rtb applied, validate cable, etc. ?
[10:29 AM] Cameron Chapman
lets check in after the boot, shake, and check for errors test
like 1
[10:33 AM] Jason Scherer
Ok shake didn't do it, but as soon as I connected using the GCS I got it to happen
[10:34 AM] Cameron Chapman
Good find. Update firmware and see if it goes away?
[10:36 AM] Jason Scherer
Let me check with Dave and make sure we are ready to update firmware. Then I'll do that and re-test.
like 1
[12:28 PM] Jason Scherer
Firmware update on XComm and FW AP was successful, but did not resolve the ap link fault issue
[12:31 PM] Jason Scherer
Also I went back and looked for this error in the past incidents I have reviewed. I found it in one of the NCR birds one time. Tail number 537
[12:32 PM] Jason Scherer
Might be worth adding this as something to look for when checking out avionics in the production sub assembly process
[12:41 PM] Jason Scherer
I red tagged the avionics and put it on your desk.
[1:02 PM] Cameron Chapman
That sounds good. What are the potential impacts of this issue? Aircraft crashes because it loses servos?
Could we go back in that boxes logs to see if it always had that issue or developed it?
Can you document steps of where to check it? We could have Sam o put them in the checkout procedure
[1:20 PM] Jason Scherer
Sounds like we should create a Jira ticket to track. What is the best project create this ticket in? The process to see the fault in the log is simply to connect the GCS software. This has caused one link fault to be reported each time I have done so on the 487 avionics.
[2:10 PM] Cameron Chapman
Linked incident issue type. 
Where does one see the fault? In the gcs software message log? We could attach a screenshot.
[2:18 PM] Jason Scherer
It's a message found in the XComm debug message log, which can viewed on the webpage, but it might also show up in the GCS debug message log.

### Jason Scherer, 2023-12-12

Here is where to find the messages. The fault link should show up after connecting the GCS software (VXE SUAV) the first time to the avionics.
[embedded: image-20231212-225458.png]

### Cameron Chapman, 2024-02-27

@Jason Scherer @David Grosher I know this is not to priority. When you have time. I have this avionics box on my desk. Do you anticipate it being helpful for any HIL or other investigation? If not, I can see if it is useful for an ironbird or other use. We have provided another to the customer.

### David Grosher, 2024-02-27

Yes, since it is potentially flight critical we will investigate this.

### David Grosher, 2024-09-24

@Jason Scherer to revisit this with new info

### Jason Scherer, 2024-09-25

This is related to my ongoing investigation into some launch aborts due to link failure (VXEP-608, NCR-240617 - 3540). I believe we have a more systemic issue with the fixed wing ap serial link to XComm. The launch aborts seem to have a big uptick in fixed wing ap transmit traffic prior to declaring a link dropout. One of the current working theories is that the fixed wing microcontroller gets too busy to receive the data resulting in a logged link dropout.

### Jason Scherer, 2025-03-22

@David Grosher I’m starting to think all the FW link losses are due to GCS running mission simulations which briefly prevent the GCS from sending any messages to the fixed wing. This in turn causes the fixed wing to think the link has been lost. Looking back at the event log in the description, the link loss messages always seem to occur after mission related messages.

### Jason Scherer, 2025-03-22

GCS mission sim appears to be the root cause and has been confirmed to cause this issue.

### David Grosher, 2025-03-24

@Ted Trowbridge See Jason’s comments below. We should look at adding the mission simulation to a separate thread as a targeted solution for the legacy GCS. Let’s add it to the backlog. 
@Jason Scherer @Scott Whitney FYSA.

### Ted Trowbridge, 2025-03-24

Added https://jenaero.atlassian.net/browse/GCSS-434 to the backlog.

### Christa Meck, 2025-08-05

@Ted Trowbridge and/or @Cameron Chapman What is the status of this investigation?
Leaving open until 12 Aug for feedback.

### Christa Meck, 2025-08-12

No additional feedback on this one.  Closing

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20231212-222157.png | image | 131 | 2023-12-12 | listed only |
| image-20231212-225458.png | image | 656 | 2023-12-12 | listed only |
