# VXEP-730: 128-117156-01 Rev B SLA Breakout Board - Increment to Rev C

- **Issue type:** Engineering Change
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-10-18
- **Updated:** 2025-09-17
- **Resolved:** 2025-09-17
- **Reporter:** Connor Peebles
- **Assignee:** Trevor Gronner
- **Creator:** Connor Peebles
- **Links:** is caused by VXEP-723 (VXE 724 MCM reset when changing HLB, other potential issues); is duplicated by VXEP-729 (128-117156-01 SLA Breakout improvements for next revision (Rev C to Rev D))
- **Production Stakeholder:** Kelly J Furlong
- **Supply Chain Stakeholder:** Perry Richardson
- **Other Stakeholder (as required):** Desiray Johnston
- **Engineering Change Level:** Level 1 - Scope of change is clear but there is a choice of approaches
- **Issue Status:** ECN #150, 128-117156-01 Rev B SLA Breakout Board - Increment to Rev C.xlsx
- **Link to Engineering Change Notice (ECN):** ECN #150, 128-117156-01 Rev B SLA Breakout Board - Increment to Rev C.xlsx

## Description

Changing values of some of the components of 128-117156-01 so that the E-Fuse is not tripping Over Voltage Protection upon common voltage transient.
Data collection here: 128-117156-01 Rev B SLA Breakout Board - Increment to Rev C (VXEP 730)
PPT here: VXEP 730 - 128-117156-01 Rev B SLA Breakout Board - Increment to Rev C.pptx
Rev C found here: Project 128-117156-01 Revision C

## Plan

- 128-117156-01 Rev B SLA Breakout Board - Increment to Rev C
- see redline for changes
- [embedded: 128-117156-01-Power Switching_REDLINE_11-25-2024.pdf]
- Once Rev C FAI are accepted, cut that into production and scrap any remaining Rev B boards
- Determine feasibility of rework for Rev B boards
- Re-work considered very arduous
- Determine customer impact of possibility of Mission Profile reset on OGCS between flights
- Customer impact determined low
- We will not be re-working Rev B boards

## Comments (21)

### Desiray Johnston, 2024-10-18

@Liam Limon Hello Liam, as discussed, this is the change for the SLA breakout board based on the NCR for 724.

### Connor Peebles, 2024-11-25

Stakeholder meeting completed, some lingering questions below:

@Craig Burton @Ted Trowbridge @Artis Bertulis Can you comment on how disruptive to mission success it is to lose a Mission Profile from the OGCS between flights? Answer may influence production rework requirement.

@Desiray Johnston @Luca Lauritzen @Catherine Wagner Can you comment on how disruptive a rework would be to production of ~100 PCBs of x2 0402 resistors, and x2 0603 capacitor + conformal coat + inspection

### Catherine Wagner, 2024-11-26

@Connor Peebles Repair will likely result in fallout at inspection (defects per IPC 610, Class 2) due to the component size, technical skill required, and internal conformal coat processes. FYA @Kevin Aban @Steve Stack

### Artis Bertulis, 2024-11-27

@Connor Peebles If I’m understanding the question right I think that’s how we’ve been operating OGCS until this point (resending the missions after each vehicle reset). I’d prefer that that wouldn’t be the case, but it’s not critical, we have been flying like that. @Craig Burton @Ted Trowbridge

### Connor Peebles, 2024-12-03

Thanks to the feedback, I am going to call not re-working the Rev B versions of the board and continue with the plan to cut in the Rev C versions

### Connor Peebles, 2024-12-03

Assigning to @Gary Angelus  just to officially track his work!

### Connor Peebles, 2024-12-11

@Gary Angelus You said this was ready to be reviewed, correct?

### Gary Angelus, 2024-12-11

@Connor Peebles  Corrent, ready for review on AD365

### Connor Peebles, 2024-12-11

I am approving the changes for rev C from my end.
@Cameron Chapman would you 1) a more formal review, and/or 2) to review the changes yourself, before we order first articles?

### Connor Peebles, 2024-12-12

@Mark Squillante Can you do a quick peer review of the changes here? See the description of this ticket for link to the Rev C board

### Connor Peebles, 2024-12-12

@Gary Angelus Can you change R2 and R7 to 845K Ohm 1% resistors, please? Better procurability.
Can you also change C7 and C8 to 1uF, 100V caps?
OVP note can stay the same. Thanks! @Mark Squillante

### Gary Angelus, 2024-12-13

@Connor Peebles @Mark Squillante Schematic and board updated.

### Connor Peebles, 2024-12-13

@Gary Angelus It looks good to me, please prepare Fabrication and Assembly files for first articles!

### Cameron Chapman, 2024-12-17

@Connor Peebles as discussed last week, I am good for you to order after Gary and Mark have approved. Thanks for asking.

### Connor Peebles, 2025-01-06

Requesting quote for QTY 10 and QTY 100 from Sierra Circuits

### Matt Philley, 2025-01-07

@Connor Peebles is Rev C required for MAGNSS?
I wanna capture that in my notes if thats the case.

### Connor Peebles, 2025-01-07

@Matt Philley It is not necessarily required but once rev C comes in and is approved, we will be scrapping any remaining rev B’s.

### Matt Philley, 2025-01-07

@Connor Peebles OK sounds good. We will try to hold off for Rev C since its an improvement, but if push comes to shove rev B will be an option.

### Connor Peebles, 2025-04-30

Board was released, is in advanced nav planes and will be the go to part going forward @Luca Lauritzen

### Trevor Gronner, 2025-05-01

@Luca Lauritzen Are there implementation actions still needed for this to roll into production?

### Christa Meck, 2025-09-16

@Trevor Gronner

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [128-117156-01-Power Switching_REDLINE_11-25-2024.pdf](attachments/24695_128-117156-01-Power%20Switching_REDLINE_11-25-2024.pdf.md) | pdf | 196 | 2024-11-25 | converted |
