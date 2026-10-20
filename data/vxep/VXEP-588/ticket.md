# VXEP-588: Evaluate procuring pre-terminated harness legs from ODU.

- **Issue type:** Improvement
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Medium
- **Created:** 2023-02-21
- **Updated:** 2025-04-22
- **Resolved:** 2025-04-22
- **Reporter:** Cameron Chapman
- **Assignee:** Connor Peebles
- **Creator:** Cameron Chapman
- **Labels:** EE-Intern, Rate#
- **Production Stakeholder:** Ryan Ferguson
- **Supply Chain Stakeholder:** Victor Vandor
- **Key Stakeholder(s):** Ryan Ferguson

## Description

Start building a list of the easiest and highest gain legs/assemblies.

## Comments (8)

### Connor Peebles, 2023-02-22

[embedded: image-20230222-191907.png]
List by Ryan F. and Liam

One thing to note; ODU will only do these pre-terminated harnesses will all the solder cups terminated. They have jacket and shielding and molded boot options, or just discrete wire. I will contact Jeff Garvais from ODU and ask for clarification on these options. 
Questions I will ask:
- Options on twists per inch?
- Bundle ability?
- Wire vendors? → from in person Jeff said they could use our current wire ALPHA WIRE, PTFE 19 strand. there are other vendor options he mentioned for alternate wire
- Options on wire colors?
- Backshell potting? → from in person: Jeff said they would use DP100 most likely
- Could they pot our braiding in molded boot?

Other questions? @Ryan Ferguson @Kelly J Furlong @Liam Limon @Cameron Chapman 

We can narrow down which ones have all their cups terminated on our assemblies. Alternatively we can simply cut the extra wires we don’t need right at the boot (if we don’t have them add braid for us)

### Cameron Chapman, 2023-02-22

Technically we should not be working projects while in new state (have not been approved yet). In this case, I am pretty sure this will get approved due to large production gains and supporting rate. @Greg Fryer, is that ok? 
Additional questions
- Why do they need all solder cups terminated? Seems like they could build without, but they may have a good reason. Cutting at the book risks shorting or more complex builds, but can be doable.
- How do they test the cable. Continuity/isolation/hi-pot to flying leads?
- Compare dimensions of molded boots vs our heat shrunk boot.
- See twisted wire Jira project for our planned twist rates.

DP100 should be fine. They are already delivering cables that way.

### Connor Peebles, 2023-02-22

Ah understood thank you Cameron

### Greg Fryer, 2023-02-22

@Connor Peebles @Cameron Chapman I am putting this on hold because it has not risen to the top of the pile yet. However if anyone has available time, they are welcome to work on this (and should put it into “in progress”).
This is more beneficial for harnesses we will keep making internally, and only moderately beneficial for outsourced harnesses (lower cost expected).

### Connor Peebles, 2023-04-21

@Ben Norris @Victor Vandor @Stephanie Sacheen Hershey Here is a Jira that came from our last conversation with Jeff Garvais.
Attached is a list of relevant ODU connector assemblies, good candidates for acquiring pre-terminated ODU connectors. We will want to stick with our specific wire, so they will need to create drawings and have first articles.

Perhaps not all wires need to be PTFE? Could some be evaluated as just Teflon hook-up wires? Make a seperate Jira abould just using Teflon wires

### Cameron Chapman, 2023-04-21

“Could some be evaluated as just Teflon hook-up wires? Make a seperate Jira abould just using Teflon wires”
@Connor Peebles yes, they could be evaluated, but not ordered until approved. Separate Jira issue to track the evaluation would be best.

### Connor Peebles, 2023-05-11

ODU sent 4 samples of pre-terminated discrete wired CGK0YAR10000156, with potting around the terminals

### Connor Peebles, 2023-06-01

samples received and at my cubicle

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20230222-191907.png | image | 47 | 2023-02-22 | listed only |
