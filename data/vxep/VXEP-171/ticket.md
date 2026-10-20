# VXEP-171: Combine Foam Cores into single PN for Horizontal Stab

- **Issue type:** Improvement
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2023-10-26
- **Updated:** 2024-02-12
- **Resolved:** 2024-02-12
- **Reporter:** Luca Lauritzen
- **Assignee:** Hans Hershberger
- **Creator:** Luca Lauritzen
- **Parent:** VA-960 Composite updates to support workflow
- **Links:** relates to VXEP-210 (Engineering Requests to Enable Production Scheduling)
- **Epic Link:** VA-960
- **Issue color:** purple

## Description

The drawing for the Vertical Tail, Foam Core 107-102064 has a note detailing information about the rudder portion of the core (from 107-102064-1 hotwired stage) so that it is still captured in the overall drawing as one part number. This is not the case for the Horizontal Stab Core, as it loses view of the rudder portion once the core moves from 107-101870-1 (Hotwired stage) to the 107-101879-2 (Machined stage) drawings. Production is requesting that either a note and rudder image be added to drawing 107-102064-2 for the Horizontal Stab or a new drawing (107-102064) that captures both the main core and rudder core.
[embedded file]
[embedded file]
[embedded file]

## Comments (11)

### Hans Hershberger, 2024-01-31

@Luca Lauritzen @Trevor Gronner I am trying to understand this ticket.  Do we want a new 107-102064 drawing?  I thought 107-102064 was alluded to above as an example of what 107-101870 should become.

### Luca Lauritzen, 2024-02-01

@Hans Hershberger my apologies for the confusion, I accidentally put the PN for the Vertical Tail when I should have put the Horizontal Stab. 107-102064 is correct and what we want to do for 107-101870-2 (I mistakenly wrote 107-102064 instead)

### Hans Hershberger, 2024-02-01

Thanks for the clarification @Luca Lauritzen !

### Hans Hershberger, 2024-02-01

This is an interesting task, does the elevator not get machined after it is hotwired?  I am trying to figure out if there is a reason it has not been displayed in 107-101870-2  In CAD, the hotwired and machined elevator do look different.  I want to know if that is reflective of reality, however.

### Luca Lauritzen, 2024-02-02

@Hans Hershberger that would be correct, the elevator does not get any machining after hotwiring, the differences in CAD configurations for the elevator between hotwiring and machining are actually done by hand by the wet layups technicians

### Hans Hershberger, 2024-02-02

Awesome!  Thanks @Luca Lauritzen

### Hans Hershberger, 2024-02-02

@Luca Lauritzen do we have a part number for the attached note on 107-101870-2?
[embedded file]

### Luca Lauritzen, 2024-02-02

@Hans Hershberger it does not have a part number but if you’d like i could upload a phantom solidworks assy to the vault to give it a part number and then label jig out in production

### Hans Hershberger, 2024-02-02

@Luca Lauritzen I think we might as well and roll it into this release.

### Luca Lauritzen, 2024-02-02

@Hans Hershberger phantom assy 116177 has been uploaded to the vault and I’ll go label the production jig now

### Hans Hershberger, 2024-02-02

Has been submitted for release

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| Horizontal Stab Core Full.JPG | image | 86 | 2023-10-26 | listed only |
| Vert Foam Core Full.JPG | image | 144 | 2023-10-26 | listed only |
| Vert Foam Core Note.JPG | image | 15 | 2023-10-26 | listed only |
| Screenshot 2024-02-02 113652.png | image | 136 | 2024-02-02 | listed only |
