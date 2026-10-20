# VXEP-1839: VXE 648 unable to connect to VTOL due to damaged CAN transceiver

- **Issue type:** Incident (8D)
- **Status:** D4 - Investigating Root Cause
- **Priority:** Medium
- **Created:** 2026-04-14
- **Updated:** 2026-10-09
- **Reporter:** Stephan Johnson
- **Assignee:** Drew Hildreth
- **Creator:** Stephan Johnson
- **Labels:** Hardware, RCCA, TIQUILA, Weekly-incident-tracker
- **Links:** relates to RMA-959 (A648 RMA 260407-2); relates to FS2-4500 (Investigation of TIQ Aviboxes); relates to RMA-779 (VXE-648 250814-11)
- **Customer:** TIQUILA
- **Part Number(s):** 107-111718
- **Vehicle Tail Number:** VXE-648
- **Incident Type:** Other (Record"Event Type: XXXXXX" in the description)
- **Severity:** 2 - Degraded Performance - No Workaround
- **Executive Summary:** Awaiting engineering resource to investigate, replacing x comm/avionics box; probable cause hardware failure.

## Description

Operator attempted to connect with the aircraft and was unable to do so. Unknown if further troubleshooting was conducted due to lack of information.

## Plan

- Replace XCOM and test through normal processes. Report results. @Drew Hildreth @Lauren Velasquez  are you able to coordinate this?
- Tag damaged XCOM for evaluation. Evaluate potential cause of damage. 
- Link to other CAN tranceiver damaged issues, see if C/CA can be linked
- Link to improvements like isolated CAN transceivers.

## Comments (14)

### Scott Whitney, 2026-04-21

I was able to successfully connect to Avibox 648 on an Ironbird. AAR attached. I will sign off on RMA traveler and return to @Lauren Velasquez 
Notes from connecting to all TIQ avionics are in https://jenaero.atlassian.net/browse/FS2-4500

 [embedded: T95_V648_260414_110442_pack.zip]

### Jeremy Kostel, 2026-04-23

[embedded: image-20260423-155250.png]
VTOL AP data not populated on the XCOM VTOL page. Usually indicates CAN issue. I isolated the avionics box to a bench and took a look at the CAN messages. Appears that the CAN chip has been damaged somehow. Shown above is a comparison between a known good board (left) and bad V648 board (right). Recommend opening the avionics box and inspecting

### Scott Whitney, 2026-04-23

After additional testing, connecting to the GCS does not seem to be the issue. It seems like there is an issue with CAN and downloading AARs

### Drew Hildreth, 2026-05-12

@Jeremy Kostel have you opened this Avionics to inspect?

What are the next steps for this one? Can we get disposition to replace a board within the avionics and continue investigation of root cause of why the CAN transceiver failed (or is it even worth it).

### Drew Hildreth, 2026-06-02

@Jeremy Kostel Reaching back on this one. Aware that everybody is busy. If you could give me an update so I could provide any additional information to the customer tomorrow that would be greatly appreciated.

### Jeremy Kostel, 2026-06-02

@Drew Hildreth Sorry I missed your initial ping, I have not opened this avionics box. It still needs an evaluation before we can determine if anything else is damaged. At minimum it will need a new XCOM board.

### Jackson Riley Curvin, 2026-07-07

@Jeremy Kostel  Have you had a chance to look at the avionics box?

### Jackson Riley Curvin, 2026-07-20

@Jeremy Kostel  Can we get a status on this please?

### Jeremy Kostel, 2026-07-27

@Jackson Riley Curvin Hey Jackson, I’m not actively working this. What is priority here? Root cause or getting this vehicle back to the customer? If its just getting the vehicle back out I would just recommend a new avionics box

### Mathew Papaleo, 2026-08-17

@Jeremy Kostel hey we have the avionics box open in rma, if you'd like to take a visual.

### Mathew Papaleo, 2026-08-26

@Lauren Velasquez @Jeremy Kostel @Jackson Riley Curvin if the failure was isolated to the xcom, can we maybe just get a quote and replace it so we can get this thing out of here?

### Jeremy Kostel, 2026-09-23

@Mathew Papaleo Recommend just replacing AV box and pushing back through SCO checkouts. Unclear if damaged XCOM lead to additional issues in the AV box. 

AV box replacement would be much quicker than swapping XCOM and pushing box back through EShop or ENG checkouts

### Stephan Johnson, 2026-10-05

@Jeremy Kostel does someone from your team have the report for this by chance?

### Jeremy Kostel, 2026-10-05

@Stephan Johnson No formal report was generated from this one. Do you need a full investigation report - or just an engineering write up?

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V648_260414_110442_pack.zip | archive | 14281 | 2026-04-21 | listed only |
| image-20260423-155250.png | image | 302 | 2026-04-23 | listed only |
| [V648 Report.pptx](attachments/65240_V648%20Report.pptx.md) | pptx | 696 | 2026-10-09 | converted |
