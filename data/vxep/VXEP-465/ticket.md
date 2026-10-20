# VXEP-465: Assign payload cases with a separate assembly PN for each configuration, with a BOM for each.

- **Issue type:** Improvement
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Medium
- **Created:** 2024-07-09
- **Updated:** 2025-11-14
- **Resolved:** 2025-11-14
- **Reporter:** Cameron Chapman
- **Assignee:** Greg Fryer
- **Creator:** Cameron Chapman

## Description

@Greg Fryer @Matt Weber @Gerrit Sperling this seems like a MechE or Latvia task since they are MechE drawings and BOMs?  Thoughts.
FYI @Cody Smisek 
Example
VXE30 E140 with relay
VXE30 E140 with regulator. 
VXE30 E140 with 1 GPS
VXE30 E140 requiring 2 GPS. 
E140 with no VXE30 equipment. 
Triclops
Single VXE30 E95.

## Comments (8)

### Cameron Chapman, 2024-07-09

Pasting below one of the numerous times a payload is shipped or installed without all required equipment, leading to critical test delays. 

[2:53 PM] Cody Smisek
If anyone is aware of any addition Epsilon GPSs please advise. I will ask Mike DJ if he has any
 
[3:05 PM] Cody Smisek
We had a dual GPS e140 that only had 1 gps connected....
 
[3:47 PM] Cameron Chapman
This seems to happen a lot. It seems like we should be assigning, labelling, and tracking payload cases with a separate assembly PN for each configuration, with a BOM for each. Any objections?

### Cameron Chapman, 2024-07-09

@Hans Hershberger do we have existing part numbers for these that we could start labelling cases with, or would we need BOMs created for each?

### Cody Smisek, 2024-07-09

Would be nice to know things like Laser Range Finder, Laser pointer or other internal hardware as well

### Hans Hershberger, 2024-07-11

@Cameron Chapman in relation to part numbers, are you referring to label part numbers or are you looking for the part numbers of the payload assemblies themselves?

### Cameron Chapman, 2024-07-22

@Hans Hershberger the part number on the label of the case. That part number should be the same as the BOM that lists what should be in the case for each assembly/case. A drawing is nice to have as well, but the BOM is higher priority. 
Ex case names/functions:
- E140G2 with VXE30 cables, relay version.
- E140G2 with VXE30 cables, regulator version
- E140G2 (standard, no VXE30 cables).

Each of the above should contain specific PNs to indicate the specific payload PN included. 
Thank you.

### Hans Hershberger, 2024-07-24

@Cameron Chapman It looks like the only situation where we have something close to this is 101-117557 (VXE30 PAYLOAD KIT, E140ZG2).  Would you look at that and let me know if this is what you’re looking for?  We can create new P/N’s for BOMs to capture the configurations you are looking for however, this is starting to feel more like a configuration control issue over an engineering issue.  @Greg Fryer do we have a configuration control person?  I remember hearing something about that but cannot quite recall.

### Cameron Chapman, 2024-07-24

@Hans Hershberger that BOM has most of what we need. I can’t see the entire indented BOM, but it should have items like the VXE harness, Epsilon ground harness, etc. on it to detail the entire case contents. @David R. Martin II is the CM lead, but I think he will need complete BOMs and PNs in order to effectively manage the configurations.  If Riga could provide a BOM, unique PN for each of the payload versions, and label the parts, we could more quickly list the parts we add to make a complete list of what is in a VXE case.

### Hans Hershberger, 2024-07-24

Alright.  This will be a project.  Once I am have some time, I can get on it.

## Attachments (0)
