# VXEP-1137: B30 MB? HLB SOC Model Not Working

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** High
- **Created:** 2025-03-13
- **Updated:** 2026-01-15
- **Resolved:** 2025-11-24
- **Reporter:** Ruysser Gabler
- **Assignee:** Adrian Garcia
- **Creator:** Ruysser Gabler
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

From Hayden Jeanor 
”So i think the battery was at the end of its life because there was a total energy consumption of 4.82Ah when the pack is rated to 6.6Ah (73% pack degradation - 80% is usually the threshold to be considered at the end of its life)
 
[embedded image (8).png]
However, our SoC model should account for this degradation (its the whole reason we base SoC on pack voltage), but it did not react as we would hope. The vehicle was reading <21V (min cutoff voltage), but still reporting >25% SoC - this should never happen if the model was working. Also, SoC continues to drop at the same rate after the vehicle landed indicating something is wrong with the model 
 
[embedded image (9).png]
 
In summary - yes the pack is degraded (as expected after 44 flights), but the vehicle is designed to accommodate for this degradation in its SoC model, but the model is failing to do so for whatever reason. The model might have some dependence on coulomb counting, which might be taking too much precedence on the SoC determination”

AAR for this flight is attached

## Comments (2)

### Ruysser Gabler, 2025-03-13

@Hayden Jeanor Made this Jira ticket for that battery. Not sure if this is the right place for it or not

### Cameron Chapman, 2025-11-24

Not enough info/priority to work on this.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_V689_20250311T171122Z 1.zip | archive | 210590 | 2025-03-13 | listed only |
| image (8).png | image | 50 | 2025-03-13 | listed only |
| image (9).png | image | 66 | 2025-03-13 | listed only |
