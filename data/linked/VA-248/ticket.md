# VA-248: Review/ evaluate addition of anomalous value flags during initial ADB calibration and assembly

- **Issue type:** Task
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Medium
- **Created:** 2023-03-28
- **Updated:** 2026-07-13
- **Resolved:** 2026-07-13
- **Reporter:** Connor Peebles
- **Assignee:** Scott Whitney
- **Creator:** Connor Peebles
- **Links:** relates to ENG-2982 (VXE 339 Mishap. Abnormal readings, behavior, and slow descent led to HLB empty and crash)

## Description

Does or can the Air Data Board flag temps that are outside expected range during temperature calibration?

[embedded: TempCalFlag.pdf]

## Plan

@Scott Whitney  determine if we have programmers available to address this. @Trevor Gronner or @Daniel Ceja can anyone on your team update the ADB calibration script programming? please see https://jenaero.atlassian.net/browse/VXEP-1484  for more info
- If the VTOL baro issues can lead to aborted launches, it seems like we should do one of the following
- test and/or calibrate at some point during production
- AP ignore data if not useful.
- For the ADB issue below, does the ADB calibration happen in a temp chamber currently? Would it be easy to see erroneous data, or would we need FW updates to read and flag it?  I think we should open and link a separate issue to track this if not related to this incident

## Comments (4)

### John Clark, 2023-05-18

I need further review to comment. @Greg Fryer

### Greg Fryer, 2023-06-30

@John Clark Please look at this incident “next” since I think it just needs clean up. Given our recent experience on red board calibration, this could be as simple as sending an Engineering Change to production to check values and provide them simple thresholds. Automating it can come later.

### Cameron Chapman, 2023-08-24

Linking subtasks to parent

### Christa Meck, 2026-07-13

No work done in over a year.  Canceling.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [TempCalFlag.pdf](attachments/13322_TempCalFlag.pdf.md) | pdf | 152 | 2023-03-29 | converted |
