# VXEP-336: 107-102238 Servo Boost Wingtip needs dimensions updated because they do not add up.

- **Issue type:** Problem
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** High
- **Created:** 2024-03-28
- **Updated:** 2026-03-30
- **Resolved:** 2026-03-30
- **Reporter:** Liam Limon
- **Assignee:** Greg Fryer
- **Creator:** Liam Limon
- **Issue color:** purple
- **Part Number(s):** 107-102238
- **Production Stakeholder:** Emalee Johnson

## Description

107-102238 Wingtip Servo Boost assembly dimensions don’t add up on the drawing. The location that is being called out for the placement of the label and underlying heat shrink is not achievable based on the dimensions given. Suspect that the location of the heatshrink encapsulating the board is called out incorrectly leading to the other dimensions being incorrect. 
A deviation is needed until the drawing is updated to allow either the total length to be incorrect or to adjust the location of the label. 
NCR-2834

## Comments (10)

### Emalee Johnson, 2024-03-28

@Garrett O'Neill Please support when available, if you have questions Liam has looked into this the most. The NCR-2384 also has additional information.

### Garrett O'Neill, 2024-04-02

@Emalee Johnson @Liam Limon Is the issue that the heat shrink the label goes over is overlapping the heat shrink that goes over the boost board?

### Liam Limon, 2024-04-02

@Garrett O'Neill The issue is that when you place the heatshrink over the boost board where it is called out, and you cut and terminate your wires according to the procedure, the placement of the heatshrink that goes under the label gets moved a quarter inch too close to the ODU side. If you add up the dimensions, from the ODU 7.5+1+1.75-.25+2.1=12.1 but the drawing calls out the total length as 11.95. That’s also assuming that the .25” that is being subtracted is equal on both sides, because it’s not called out on the 2.1” side. The drawing also shows a small gap that is unmeasured between the label heatshrink and the board heatshrink, but there isn’t room in the dimensions for that gap. It also calls for an 8.5” piece of nylon but the total dimension from the end of the odu to the board is 8.75”. Once the ODU is added then the nylon is excessively long.

### Emalee Johnson, 2024-04-09

@Garrett O'Neill @Liam Limon Have we come up with a solution yet? This issue is causing a shortage in production right now.

### Emalee Johnson, 2024-04-09

@Cameron Chapman @Greg Fryer

### Liam Limon, 2024-04-09

@Emalee Johnson I spoke with Garrett and we have a solution if necessary but Leshawn and I are building a batch. I think that the error was due the the tech missunderstanding the measurement distances. While there is a tolerance stackup problem, at this time we can build them as is.

### Greg Fryer, 2024-04-09

@Emalee Johnson This feels like one where I would like you (Prod Eng) to be able to issue a revision (we’d still review like any other), but I’m not sure we have the tools in place.
@Garrett O'Neill Could we pass to @Nadia Brown with a proposed simplification? Maybe just locate the label off of the board shrink (0.25), and remove the 7.50? Feels like we put too much control on the label location back when. (0.25 so in-contact is ok, and a gap up to 0.5 is ok) Otherwise make it 0.100 (but that tightens the tolerance whichfeels unnecessary).
If you agree, just ping me and I’ll set the task to Nadia.
[embedded image-20240409-170506.png]

### Emalee Johnson, 2024-04-09

My understanding is that the heat shrink label acts as a strain relief once installed in the wing tip servo pocket which is why it has the higher location control. 
@Greg Fryer

### Matt Philley, 2024-04-09

Any dimension updates to this I strongly recommend test fit in wings. 
There are required dimensions at the Wing Tip level that are influenced by the position of the heat shrink-ish at the servo boost cable level since the zip tie in the pocket is supposed to act as a hard-stop with the heat shrink because folks tend to just yank the whole wing to disconnect the break-away ODU connector when disassembling the wing from the lift boom. 
[embedded image-20240409-180230.png]
Wing Tip Drawing 107-100549
[embedded image-20240409-180109.png]

### Liam Limon, 2024-04-11

@Matt Philley I’m building a batch based off of Garretts suggested revisions. I will be able to adjust the placement of the heathrink under the label as necessary to make sure that they will accommodate the wing and not be scraped if it turns out the suggested changes make the fitment an issue.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20240409-170506.png | image | 42 | 2024-04-09 | listed only |
| image-20240409-180109.png | image | 18 | 2024-04-09 | listed only |
| image-20240409-180230.png | image | 228 | 2024-04-09 | listed only |
