# FS2-4161: VXE-674 Auto RTB Low energy Main Battery percentage 57% 26.6V

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2026-01-06
- **Updated:** 2026-02-27
- **Resolved:** 2026-02-27
- **Reporter:** Scott Whitney
- **Assignee:** Ryan Christino
- **Creator:** Scott Whitney
- **Links:** relates to VXEP-1598 (VXE-674 Auto RTB Low energy Main Battery percentage 57% 26.6V)
- **Sprint:** FS2 Sprint 37, FS2 Sprint 36

## Description

Added an Incident Investigation Report for this Below but Essentially:
- Aircraft should not have RTB’d and should be fairly robust to erroneous measurements used in the RTB calculation.
- Shortly beforehand, a roll fault was tripped. There is no logical flow that would cause a low energy RTB from that, but this could have contributed to some sort of corruption event around the calculation?
- Logged sensor values appear correct with no corrupted data present at the logging rate that was applied.

I did not discover the root cause of this issue beyond this theory and don’t have any recommendations for further testing.

## Comments (1)

### Scott Whitney, 2026-01-06

@Logan Wright  - can you take a look at this VXEP when you get some down time from B40?

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [VIT_V647_RTB_Investigation.pptx](attachments/39760_VIT_V647_RTB_Investigation.pptx.md) | pptx | 1510 | 2026-01-16 | converted |
