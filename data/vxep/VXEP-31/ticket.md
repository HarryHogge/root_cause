# VXEP-31: TPTR-58 Fuel Cell error during launch wizard

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2023-08-23
- **Updated:** 2025-06-09
- **Resolved:** 2025-06-09
- **Reporter:** Allen Gardner
- **Assignee:** Cameron Chapman
- **Creator:** Allen Gardner
- **Links:** relates to VA-395 (TPTR-58 Resolution Fuel Cell error during climb); relates to VA-396 (TPTR-58 Fuel Cell error during climb, identify C/CA. ); relates to VA-441 (TPTR-58-Get more information from operators (LM?)); is blocked by VA-615 (Create report on root cause, and CAs (some are compelted))
- **Customer:** TIQUILA
- **Incident Type:** Mission Failure/Abort
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

From PTR Export Sheet. 
Fuel Cell error during climb
just after take off and into the climb for WP 1 the fuel cell gave an error on the GCS, as the HLB was being used to climb the aircraft and with no reasonable expectation of restoring the fuel cell to normal flight, the decision was taken to recover the AV immediately. The fuel cell was sent for testing I believe.
Shah, Dhruti (UK) - Mon Jul 10 21:30:18 BST 2023 : Vendor PTR-B 10/7/23: Confirm Fuel Cell Number 242 or 249 - Ask Dan Lloyd. Is this covered by VIT2-320 or considered a different issue. 
Old description from another incident below (I didn’t want to delete until we sorted out). 
Fuel Cell S/N 510 w/Aircraft 510 (note, there is a separate issue that involves AIRCRAFT 510 and Fuel Cell 249, DO NOT CONFUSE THEM).
Fuel Cell did not start during launch wizard.
File location for closure report and any supporting files: VXEP-0031 Fuel Cell error (TIQUILA TPTR-58)
(Quick files can be attached to the ticket too, but please ensure the final report and such are in this SharePoint folder.)

## Comments (10)

### Allen Gardner, 2023-08-24

@Cameron Chapman Please add a task within VA to determine the root cause and link back here. Then add corrective action steps.

### Cameron Chapman, 2023-08-29

Shah, Dhruti (UK) - Mon Jul 10 21:30:18 BST 2023 : Vendor PTR-B 10/7/23: Confirm Fuel Cell Number 242 or 249 - Ask Dan Lloyd. Is this covered by VIT2-320 or considered a different issue.

### Cameron Chapman, 2023-09-03

Email from Greg. 
Sam – We need some help to untangle what is either one or two fuel cell incidents (If anyone else has already resolved this, please chime in!)
 
We have a ticket [VIT2-320] Fuel Cell Fault SN D4500249 /247 - Jira (atlassian.net) for an incident in June.
 
We also have a ticket [VXEP-31] TPTR-58 Fuel Cell error during climb - Jira (atlassian.net) for an incident that occurred during TIQUILA FAT – or alternatively this is just TIQUILA tracking of the prior incident.
 
 
There are two fuel cells as Robert issued an RMA for both, but I can’t tell from my look how many issues there are. That may not indicate there were two incidents though.
 
If we can confirm this is one or two separate issues, I will clean up the tickets so we have tracking correctly. The last status in early August was that it was low priority, so while it is SEV3 (workaround by not using those fuel cells) it is being tracked by TIQUILA to closure.
 
Meaning: We need to sort out the bookkeeping at a minimum, so status can be given, and we can give status.
 
Thanks!
 
image001.png
Greg Fryer
Engineering Manager
Edge Autonomy – SLO
Phone: +1-805-592-1997
Email: gfryer@edgeautonomy.io
 
Confidentiality Notice
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.

### Pat Wells, 2023-09-05

@Cameron Chapman I don’t believe VIT-320 is related to TPTR-58
@Sam Miller do you recall a fuel cell incident during August FAT?

### Cameron Chapman, 2023-09-19

@Pat Wells Dan Lloyd does not recognize the wording in this issue. Do you know who reported it? 
@Tom Westrich @Sean Wendling do you have any more information on this incident (fuel cell SN, status, C/CA, etc)?

### Greg Fryer, 2023-09-20

@Former user @Former user While @Pat Wells offered to go find information, you may have the original TPTR files from LM. We believe in the record keeping confusion developed between TPTR-55 https://jenaero.atlassian.net/browse/VXEP-22  and TPTR 58 (this issue). Can you please check those source files and help us separate these two issues.

### Former user, 2023-09-20

@Greg Fryer    This event was on 10 July during training prior to Tiquila FAT (7 - 11 August).  It was using a D450XR  fuel cell which was returned to Ann Arbor where we have not been able to replicate the failure.  The S/N for this D450XR is 249.  [For Reference, the fuel cell in use for FAT was a D450+ S/N 510 and the failure is documented in TPTR-58.  Fuel cell 510 has had the calibration changes and replaced the fan speed controller.]  

It appears that A/C 510 was the A/C on both occasions.

### Greg Fryer, 2023-09-28

@Sean Wendling and I updated the description to clearly include the aircraft tail (listed as unknown right now) and the Fuel Cell s/n (249) for this incident.
Currently problem has not been replicated. Will provide the possible explanations, and close (barring any new info).

### Greg Fryer, 2023-09-28

All, be careful viewing past comments as they are confused because of duplicate descriptions. Be sure to read the actual issue description to know which event this is.

### Cameron Chapman, 2023-11-07

@Greg Fryerthis one seems to have been mixed up with another fuel cell incident. I checked with the TPTR export from august and corrected the description. 
@Former user can you point us to the latest TPTR source/log?

## Attachments (0)
