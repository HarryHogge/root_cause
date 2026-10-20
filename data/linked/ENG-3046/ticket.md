# ENG-3046: 489 Erratic Landing Behavior

- **Issue type:** Problem
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2024-06-06
- **Updated:** 2026-06-16
- **Resolved:** 2026-06-16
- **Reporter:** Daniel Lloyd
- **Assignee:** Pat Wells
- **Creator:** Daniel Lloyd
- **Labels:** LM_asset
- **Links:** relates to VXEP-426 (VXE 489 Erratic Landing Behavior); relates to RMA-299 (VXE-489 RMA 240726 (LM))

## Description

On two successive flights, following the landing transition, the aircraft swapped directions, rapidly lost altitude, and then recovered to a nominal landing. Constraints of the landing zone necessitated landing with a tailwind so weathervaning was expected. Landing on 4 June winds were 7 mph and winds on 5 June were 2.5 mph. The aircraft’s behavior was the same even with lighter winds. Would like an analysis of this behavior to determine if the aircraft is safe to continue flight operations.
This is an LM asset not associated with the Tiquila program.
@Pat Wells

## Comments (16)

### Pat Wells, 2024-06-06

@Daniel Lloyd received. 
Do you have AAR’s to go along with the two flight anomalies?

### Pat Wells, 2024-06-20

@Daniel Lloyd 
Received some guidance from the engineering team.  Please let me know how you’d like to proceed.
- Using the motor test page,  test each motor sequentially, paying close attention to motor 3 to see if there is a lag from the command to the activation, or any other issues. If observed, replace motor assy 3 and see if fixed. If not, see below.
- Return whole aircraft for inspection and troubleshooting.
- Return just motor assembly 3. Ground that center wing and boom until investigation has more information. I don’t think we have yet proved it is isolated to the motor assembly.

### Pat Wells, 2024-06-25

@Daniel Lloyd following up on my request in the previous comment.
Thanks

### Daniel Lloyd, 2024-06-25

@Pat Wells I performed some motor checks and was not comfortable with the results. Will likely ask to return the wing set.
All “motor tests” (except launch wizard checks) were performed using the VTOL controller website Motor Test page. Tests were performed with default settings; Test Throttle = 1150uS and Duration = 1000mS.
- Motor test 1. Motor #1 started immediately, #2 immediately, #3 2-second delay, #4 immediately.
- Motor test 2. Motor #1 started immediately, #2 didn’t start. Wing no longer responding to commands. Safed system by depressing the flashing red light on the center wing. Cycled power to the center wing.
- Launch Wizard test 1. All motors worked normally.
- Launch Wizard test  2. All motors worked normally. When safing the system I heard it annunciate twice. The normal beep-beep was followed quickly by another beep-beep as though the ESC’s didn’t all get the safe command at the same time. I have also heard this happen when plugging in the HLB.
- Motor test 4. Motor #1 started immediately, #2 immediately, #3 2-second delay, #4 immediately. The web page stopped responding. Page went blank, Safed system by depressing the flashing red light on the center wing. Cycled power to the center wing. Had problems getting the web page to load, probably due to the power cycle. Closed browser and restarted.
- Motor test 5. Motor #1 started immediately, #2 immediately, #3 didn’t start. #4 didn’t start. The web page stopped responding. Page went blank, Safed system by depressing the flashing red light on the center wing.
- Motor test 6. Tried a different sequence. Motor #3 started immediately, #4 immediately, #1 didn’t start, #2 started immediately along with #1 which may have started after a delay. When safing the system I heard it annunciate twice.

Forgot to produce the AAR until after I disconnected and closed the software. Reopened, reconnected, downloaded the FDR. The files should be there. I won’t be able to post them today.
I have little confidence in this wing set.

### Pat Wells, 2024-06-25

@Daniel Lloyd all received and thank you.
I will pass along your findings to the team that investigating this issue.  More to follow soon.

### Daniel Lloyd, 2024-06-26

@Pat Wells I uploaded the AAR from my motor testing.

### Pat Wells, 2024-06-27

@Daniel Lloyd received and passed to engineering.

### Pat Wells, 2024-07-22

@Daniel Lloyd would it be possible for you to return this aircraft on an RMA?  The engineering team would like to take a deep look into the issues you’re experiencing.
@Sean Odell FYSA

### Daniel Lloyd, 2024-07-22

@Pat Wells My concern is that I won’t see it again for 6-9 months. I will check our need for it. It fly's fine using 493’s wing set. We can’t fly 493 because we sent it’s AP box in 3 months ago for an SD card swap. 489 using 493’s wings is the only LM asset we have working right now.

### Pat Wells, 2024-07-22

@Daniel Lloyd understood.  I just asked about 493 AP box for an updated status.

### Daniel Lloyd, 2024-07-25

@Pat Wells Shipped to SLO today

### Pat Wells, 2024-07-25

@Sean Odell FYSA see below.  Are you tracking this incoming?
@Daniel Lloyd acknowledged

### Sean Odell, 2024-07-25

@Pat Wells I heard an aircraft was coming but did not know the tail #. 
Jeff told me, he will request an RMA once he gets it in his hands.

### Pat Wells, 2024-07-26

@Daniel Lloyd aircraft arrived at SLO today 7/26

### Daniel Lloyd, 2024-08-07

@Pat Wells Thanks, please let me know when you find out anything.

### Christa Meck, 2026-06-16

Incident is closed.  Closing this as well.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V489_240604_094404_pack.zip | archive | 2281 | 2024-06-06 | listed only |
| T95_V489_240605_084654_pack.zip | archive | 1727 | 2024-06-06 | listed only |
| T95_V489_240625_113334_pack.zip | archive | 1870 | 2024-06-26 | listed only |
