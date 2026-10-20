# VXEP-1655: Update E95 cable to remove unplanned connections. Add part marking. Ensure Latvia drawing is updated to include these changes and part marking.

- **Issue type:** Epic
- **Status:** New
- **Priority:** High
- **Created:** 2025-12-23
- **Updated:** 2026-04-28
- **Reporter:** Cameron Chapman
- **Assignee:** Mike DeJesus
- **Creator:** Cameron Chapman

## Description

Reference NCR here: EPS.95 Functional Discrepancies

## Comments (8)

### William Dresser, 2025-12-23

@Cameron Chapman I want to confirm drawing/part numbers because they aren’t listed on this ticket. The drawing for an E95 cable that I have source files for is the 101-111082 PAYLOAD CABLE SHIELDED, E95. That harness already does not have the unplanned connections so it should be fine, though it is also missing some other connections compared to 91-012 (see below) beyond just the unplanned connections.

EH-0091-012-00 Octopus E95 payload cable for VXE30 is the Latvia harness drawing which has the unplanned connections, but I don’t believe I have the power to edit that without Latvia sharing source files (looks like Visio?). Is that an option? Alternatively, I can remake a version of 101-111082 to match what we want 91-012 to look like.

### Cameron Chapman, 2025-12-23

@William Dresser I think that is part of this series of tickets. To sort out what is latest, ensure all sites are using latest, and mark others as obsolete. @Grant Goodman @Connor Peebles @John Gober @Mike DeJesus  should have more info than I do about that. 
That is better captured in https://jenaero.atlassian.net/browse/VXEP-1657 
I think the best current way to get the Latvia drawing changed is to release our latest/planned version, then ask them to update theirs accordingly, and ask to be part of the peer review before they release and build to it.

### Connor Peebles, 2025-12-23

@William Dresser Here is the redline that represents what I did to the harness for the 4 E95 gimbals from this NCR: EPS.95 Functional Discrepancies

This redline is in the vault, file name 101-111082-02. Functionally it is the same as 101-111082, but it does have 4 pig tails wires encapsulated in epoxy now (two wires cut in half), so this redline captures that configuration. I recommend that we DO NOT make a whole new drawing just for this configuration, and simply get Latvia to remove J1-10 and J1-51 wires from their drawing # EH-0091-012-00. Let this 101-111082-02 redline live in the vault as proof of that configuration, for now.[embedded: 101-111082-02.pdf] 
@Mike DeJesus Can you help us get Latvia to change their drawing as to how I describe above.
FYI @Cameron Chapman

### Cameron Chapman, 2025-12-23

@Connor Peebles @William Dresser@Mike DeJesus   if we do go that route, I think we should request Latvia does the following. 
- Make a different PN or config number for the updated drawing to separate it from the one that damages payloads 
- Do we have an idea of how many EH-0091-012-00 were built? Can we quarantine and rework all to 101-111082-02?
- Part mark all cables and other electronic assemblies on the part itself (not the bag). Including rev.
- Did you relabel all reworked cables as 101-111082? Thank you for doing that.

### Connor Peebles, 2025-12-23

@Cameron Chapman 3. yes, all 4 cables I reworked to 101-111082-02 were labeled as 101-111082-02

### William Dresser, 2026-01-05

@Cameron Chapman Can you please confirm that SLO will not be remaking the 101-111082 drawings, and that we will pass the redline from Connor on to Latvia for them to pull a new PN and generate a new drawing?

### Cameron Chapman, 2026-01-05

@William Dresser I am unable to confirm that. I do not control what Latvia does, receiving inspections in HSV and SLO, etc. I recommend short term adding to the traveler or receiving inspection that the cable has been verified reworked/built to 101-111082-02 and tested as functional. Medium term, we need to have a system to verify they send the same product every time and communicate/get approval for changes. 
The traveler has other issues. 
- Ex: “Perform functional checkout per (###).”
- This is not on the vault E95 PAYLOAD KIT, MOD KIT        2122187-01        1        EA        FOR EACH ORDER, REVIEW MOD KIT WITH ENGINEERING

### Cameron Chapman, 2026-01-05

@William Dresser reassigning to @Mike DeJesus

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [101-111082-02.pdf](attachments/38350_101-111082-02.pdf.md) | pdf | 399 | 2025-12-23 | converted |
