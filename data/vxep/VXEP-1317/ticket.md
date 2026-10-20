# VXEP-1317: V666 & V551 standard VXE30 XCOMM WDT Resets 6/26/25

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2025-06-27
- **Updated:** 2025-08-15
- **Resolved:** 2025-08-15
- **Reporter:** Cameron Chapman
- **Assignee:** David Grosher
- **Creator:** Cameron Chapman
- **Links:** relates to VXEP-1039 (Test non-conductive plate and/or gimbal mounts to see if that resolved the issue and meets other requirements. Release and implement if so.)
- **Incident Type:** Near Miss
- **Severity:** 1 - Flight Critical

## Corrective Action

- Validate the message contents on FW AP and XCOMM [COMPLETE in v6.5]
- Fix the GCS root cause. Note: the issue is still present on v6.5 on the GCS side but the updated compiler tools make it less catastrophic.

## Plan

- Dave says this is not E140 related.
- SCO E140 does have 2 E140s with 1 conductive plate. Probably unrelated, but should still be resolved. Will create linked task. https://jenaero.atlassian.net/browse/VXEP-1318

## Root Cause

GCS sends corrupted imager message to XCOMM → FW AP → XCOMM. Because the FW AP holds the value it continues to send it to the XCOMM resulting in the boot loop cycle when the XCOMM tries to send the status response to the console debug. Note: this can be caused with CTRL+F prior to establishing a vehicle connection on v6.4.

## Comments (2)

### Cameron Chapman, 2025-06-27

Chat for standard VXE30 XCOMM WDT Resets 6/26/25, separating from MCM reset issue
 
Connor Peebles changed the group name to standard VXE30 XCOMM WDT Resets 6/26/25.
 
Ruysser Gabler can you post an NCR or the Veh tail #'s? + gimbal
 No NCR made Veh 666 and 551 
JIRA>>NCR IMO
 Both gimbals with the AC there in FLOPS No JIRA either If needed to make one please pull info from teams chats 
link to the MCM reset one
 
Jason Scherer added Dave Grosher to the chat and shared all chat history.
 
also the non-conductive plate swap. It seems like that containment was not fully processed
 
6096, and 6432
 
6096 is on 3.5.1.0 
6432 is on a new experimental one for a new EO sensor test
 
Dave was just asking me about a previous XComm WDT reset which he said was excatly the same to the one we fixed in 6.5. What firmware was this vehicle flying? 
 
Both used the same plate 
 
6.4 
 
Ok then this may be a known bug that we fixed already in 6.5
 
6.4 is a optional update for VXE30
 
Maybe we need to make it required 
 
Ruysser Gabler
Both used the same plate

Same conductive plate right? (which should be replaced with non-conductive, but has not yet. I'm working to get more)
 
Yes, we moved plate from gimbal to gimbal 
 
Dave Grosher Is this the incident you were asking about?
 
Ruysser Gabler
Maybe we need to make it required

Yes we are looking into this. 
 
Jason Scherer
DaveGrosher Is this the incident you were asking about?

yes
 
What version of the GCS was used during the incidents yesterday?
 
The 551 was on 6.5 GCS. and 666 was on 6.4 GCS
 
Connor Peebles changed the group name to V666 & V551 standard VXE30 XCOMM WDT Resets 6/26/25.
 
Connor Peebles added Ryan Smith and Logan Wright to the chat and shared all chat history.
 
Equipment in Engineering
 
FYA, there is an optional infra red laser pointer on the EZ140 model.  not sure if the one we have has it but it can cause permanent damage to the eye even for short durations.  Let's make sure it is well covered if powered.  Thank you. 
 
Connor Peebles added Cody Smisek to the chat and shared all chat history.
 
the laser requires a harness that provides power to a pin. don't think we've made any of those to date. so there is no way to power that laser
 
Cody Smisek
the laser requires a harness that provides power to a pin. don't think we've made any of those to date. so there is no way to power that laser

I think we have. A previous decision was to hard wire it enabled and rely on the SW disable. Agreed best to cover until needed. 
 
what is the PN for those harnesses
 
Is there labelling for the laser danger? That would be a good JIRA problem if not. 
 
here is one 
 
hard wired to converter output
 
yes
 
https://jenaero.atlassian.net/browse/VXEP-1317 
VXEP-1317: V666 &amp; V551 standard VXE30 XCOMM WDT Resets 6/26/25

### David Grosher, 2025-08-15

Fixed in v6.5

## Attachments (0)
