# VXEP-742: NASA Proposed 5W S-Band Transmit Power Limit

- **Issue type:** Task
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Medium
- **Created:** 2024-10-24
- **Updated:** 2026-03-30
- **Resolved:** 2026-03-30
- **Reporter:** Wesley Lilienthal
- **Assignee:** Jeremy White
- **Creator:** Wesley Lilienthal

## Description

Threat: 
We have heard rumblings that NASA is lobbying to have S-Band transmissions restricted to 5 Watts within CONUS due to the potential interruption of NASA Space Systems by transmissions of higher power. Implementation date unknown, but there was a data call date of 31 October 2024.
Impact:
Depending upon the nature of the limit, the prospective impact is either meaningful or very meaningful.
Note that the means of compliance would be a simple configuration change in the settings of a given Silvus radio, limiting that maximum transmission power for a given radio + antenna pairing. A unique setting would be required for each of VXE30, SGCS1, SGCS2, and SGCS3. 
@Abel J. Markowhas advised that he has not heard word of this restriction and it may very likely be posturing by NASA and have no real substance, especially in light of enforceability being an entirely separate matter from law and particularly from hearsay. Abel indicated that neither the missile folks at WSMR nor Vandenburg would ever agree to such a restriction. 
Open Questions:
- Need to know to which metric the 5 W limit applies: EIRP? ERP? Conducted transmit power? The former two account for antenna gain. The latter does not. If designed well, the limitation would capture antenna gain such that it limits field strength at the victim receiver, rather than just blindly limiting a given aggressor radio's conducted transmit power at its output port.
- Need to know how real the proposed restriction by NASA is.
- If real, need to know how likely the proposed restriction is to be enacted.
- Need to know how enforceable the restriction would be if enacted.
- Need to know what caveats would be present along with the restriction that we and our CONUS customers might leverage.

Sources: 
Per @Greg Fryer and @Jeremy White , @Gregory Nichols  has spent time with the PPT slide. Oleg Filipov (SOCOM SUMS Lead System engineer) received a slide this morning while we started training and talked with Greg briefly about its potential impact on Stalker and the upcoming operational testing.
We can’t have the slide, but AFSOC highlighted it to SOCOM. The slide doesn’t have any technical specs, but does mentions the Silvus 4400e since it is not “spectrum certified.” 
NASA is reportedly pushing for this restriction and AFSOC/SOCOM owe operational impacts by EOM October.

## Comments (1)

### Wesley Lilienthal, 2024-10-24

Current status: On hold until situation evolves. @Jeremy White monitoring.

## Attachments (0)
