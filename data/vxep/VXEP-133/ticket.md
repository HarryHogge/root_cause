# VXEP-133: 100-108995 Pasternack SMA F to SMP M missing procurement and inspection requirements

- **Issue type:** Improvement
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** High
- **Created:** 2023-10-04
- **Updated:** 2025-10-21
- **Resolved:** 2025-05-28
- **Reporter:** Catherine Wagner
- **Assignee:** Wesley Lilienthal
- **Creator:** Catherine Wagner
- **Labels:** COTs
- **Links:** is blocked by VXEP-134 (Revise 100-108995 to include label and inspection/test requirements.)
- **Part Number(s):** 100-108995
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

Engineering definition includes CAD drawing, MFG Part number and MFG (Pasternack). Historical COTS / Vendor PN does not include requirement for test data and traceability - it has to be requested when procurement places PO.
These cables are used inside 965-1-01-4900 Silvus Enclosure which is inside the VXE30 Fuselage. Qty 2 cables per aircraft. 
100-108995 (PE3C3937-3.7) is missing:
- Test data requirements
- Inspection requirements (could be satisfied by datasheet in Vault: https://www.pasternack.com/images/ProductPDF/PE3C3937.pdf)
- Traceability requirements (label method, content)

[embedded file]
In addition, description specifies 3 in. cable but ordered part number is 3.7 in.

## Comments (8)

### Catherine Wagner, 2023-10-04

@Brad Crampton @Matt Philley Resolution reached for linked NCR, but this is an ongoing issue for procurement and inspection. I would appreciate your help working with engineering to get the test data and marking requirements defined.
FYI @Stephanie Sacheen Hershey @Former user @Victor Vandor

### Matt Philley, 2023-10-05

@Marc Richardson potential topic for CCB. This is part of our ongoing need for all RF cables to be fully defined by Engineering.

### Catherine Wagner, 2023-10-20

Related issue: PO 231004-04 is classified as COTS so once received it moved straight to inventory without verification / pairing of test data. @Spenser Bracken noticed it in inventory and brought it to QC. This receipt was conforming but of course the risk is test data may be missed if it routes around inspection. @Matt Philley @Marc Richardson Ideally PO details would include whether inspection is required or not, independent of the COTS classification.

### Catherine Wagner, 2023-11-14

@Matt Philley @Marc Richardson @Stephanie Sacheen Hershey 
Received PO 231004-04, QTY 60, and realized we have open orders under 100-108995 for two Pasternack PNs: PE3C3947 & PE3C3937. 
PE3C3937 has a right angle connector and is correct per Vault; PE3C3947 has straight connectors. 
Last receipt (QTY 125) and this one match PO not Vault.
[embedded file]

### Matt Philley, 2023-11-15

@Catherine Wagner looks like these go into the 965-1-01-4900 Silvus Enclosure which show the right angle connector on the drawing, so any PE3C3947 with straight connector lets get on NCR.

[embedded file]

### Matt Philley, 2023-11-15

@Greg Fryer @Victor Vandor can we touch on this in CCB this week and get this caught up to the current standard? 
These cables are buried inside an assembly, so extremely difficult to fix if we find out they are bad, so its super important they come in correct with all the right documentation.

### Catherine Wagner, 2024-03-04

@Matt Philley @Wesley Lilienthal  Updated with links to recurring NCRs for cables missing test data. If lack of documentation isn’t a root cause I would be surprised.

### Catherine Wagner, 2024-04-26

@Irfan Sultan NCR history and request for procurement requirements.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20231004-181016.png | image | 72 | 2023-10-04 | listed only |
| Screenshot 2023-11-14 160213.jpg | image | 115 | 2023-11-14 | listed only |
| image-20231115-151738.png | image | 59 | 2023-11-15 | listed only |
