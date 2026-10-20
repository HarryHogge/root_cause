# VXEP-726: 2119719-01, Servo Assy - Engineering Drawing

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2024-10-16
- **Updated:** 2025-03-17
- **Resolved:** 2025-03-17
- **Reporter:** Matt Philley
- **Assignee:** Camron Richardson
- **Creator:** Matt Philley
- **Labels:** Gen1-Utility-Dropper
- **Parent:** VXEP-724 Practice Build - 2119719-01, Servo Assy Wing Drop
- **Epic Link:** VXEP-724
- **Issue color:** purple

## Description

Update: New redlines added 2/13/2025 based on First Article Pylon Build 
- 16 mm Heatshrink 100-106701: 
- location depicted is correct
- length should be .75” +/- .125”
- 3/8 HS 100-106125: 
- starting location is where the wires enter the back of the connector (we could add dashed lines to depict this)
- length should be .75 +/- .125”

## Comments (16)

### Gary Angelus, 2024-11-14

Sensors S1 and S2, will labels be required to tell them apart?  If so, what should the nomenclature be?
@Matt Philley @Nina Menon

### Nina Menon, 2024-11-14

@Gary Angelus Hi Gary, the designators S1 and S2 will work for the label nomenclature. We will be labelling the sensor itself, the wires get routed so tightly that there is no room for a heat shrink label.

### Nina Menon, 2024-11-22

@Gary Angelus hi Gary, can you put the drawing pdf in the Vault when you have time? Thanks!

### Nina Menon, 2025-02-13

@Brendan Palmer @Matt Philley @Michelle Greenwald Ticket updated with heat shrink redlines

### Connor Peebles, 2025-02-17

Assigning to @Camron Richardson to follow through after Gary’s departure.

### Camron Richardson, 2025-02-17

Redlines have been implemented and is waiting for review @Matt Philley

### Matt Philley, 2025-02-18

@Camron Richardson awesome!! can @Nina Menon and/or @Brendan Palmer get a chance to review this too?

### Nina Menon, 2025-02-18

@Camron Richardson thanks for jumping on this! a couple of notes:
- can we adjust the bom HS lengths from 1” to .75”?
- the heat shrink segments do have some overlap, so is it possible to show that somehow? Here’s 1 potential way that I could think of:

[embedded image-20250218-160009.png]
- I didn’t catch this before, but the label spec in Note 1 has an extra 5 - should be 110-111957

@Brendan Palmer can you attach a pic of the finished servo for Camron’s reference?

### Brendan Palmer, 2025-02-18

@Camron Richardson Here’s the actual servo, the scale might be a little off but I think it shows the overlap / offset between the two heatshrink pieces that @Nina Menon is talking about.

[embedded image-20250218-161525.png]
[embedded image-20250218-161552.png]

### Camron Richardson, 2025-02-18

@Brendan Palmer @Nina Menon @Matt Philley  Changes have been implemented. Document is now up to date. Note 1 was a duplicate, consolidated with Note 2 and fixed document number

[embedded image-20250218-204910.png]
[embedded image-20250218-204934.png]
[embedded image-20250218-205235.png]

### Nina Menon, 2025-02-18

@Camron Richardson looks good to me, thank you!

### Hayden Jeanor, 2025-02-19

@Camron Richardson please ensure FA build installation does not exceed wire bend radius specs outlined in IPC 620 and report results on this ticket. Also, redlines have been passed back to you

### Hayden Jeanor, 2025-02-20

Are there FA builds that EE can get our hands on to confirm dimensions, fit check, etc @Nina Menon 

Also, on the inspection sheet, might be worth specifying the orgin of each color on the pinout. The drawing specifies it, so maybe not necessary - up to yall. @Brad Crampton 
[embedded image-20250220-203232.png]

### Brad Crampton, 2025-02-20

@Hayden Jeanor I cannot find the drawing for this part in the vault. Do you know where it might be?

### Hayden Jeanor, 2025-02-21

@Brad Crampton the drawing isnt released to the vault yet. you should be able to view here https://jennings-aeronautics-2.365.altium.com/designs/AD3E6E91-0ED0-4643-8847-3CE42B9CCC6B?OpenedFrom=AD&activeDocumentId=211971920WING20DROP20SERVO.WirDoc&activeView=Wiring#design - will have to request permissions

### Hayden Jeanor, 2025-03-17

Drawing released to vault

## Attachments (9)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| Image (1).jpg | image | 3922 | 2025-02-13 | listed only |
| Image.jpg | image | 1117 | 2025-02-13 | listed only |
| image-20250218-160009.png | image | 86 | 2025-02-18 | listed only |
| image-20250218-161525.png | image | 907 | 2025-02-18 | listed only |
| image-20250218-161552.png | image | 4400 | 2025-02-18 | listed only |
| image-20250218-204910.png | image | 25 | 2025-02-18 | listed only |
| image-20250218-204934.png | image | 56 | 2025-02-18 | listed only |
| image-20250218-205235.png | image | 16 | 2025-02-18 | listed only |
| image-20250220-203232.png | image | 127 | 2025-02-20 | listed only |
