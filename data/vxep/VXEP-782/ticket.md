# VXEP-782: Make HPMB compatible with payload ICD and/or specific payloads

- **Issue type:** Epic
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2024-11-19
- **Updated:** 2026-03-30
- **Resolved:** 2026-03-30
- **Reporter:** Cameron Chapman
- **Assignee:** Charles David Madewell
- **Creator:** Cameron Chapman
- **Parent:** VXEP-752 Integrate Amprius Heavy Payload Main Battery for Hatchet+AEWE demos and future use 
- **Epic Status:** To Do
- **Epic Color:** ghx-label-10
- **Issue color:** blue
- **Other Stakeholder (as required):** Tom Westrich
- **Leadership Stakeholder:** Jeremy White

## Description

HPMB voltage range is lower than standard (down to 17.5V). Many payloads have a higher voltage range (Epsilon ~20V min. SLO has not verified that with test).
Initial options in order of increasing scope. 
- Add a regulator to each payload to make voltage ranges compatible. Cam recommends for short term. 
- Already done on previous octopus payloads (less engineering development/support, but some required due to rushed initial design/documentation). [embedded file] [embedded file]
- More closely matches VXE30 architecture.
- Bulkier/heavier/less professional/rugged.
- This could be most efficient to build compatible payloads in Riga, with lots of review on our side to prevent previous oversights.
- Use the DCDC output of the current battery
- Payload power is not measured, which can add risk and lead to less accurate endurance estimates. May be minor depending on payload % of total power adds some risk of not being able to detect and shutoff a payload fault.
- Could be improved by getting current reading from the payload, but this would require Latvia and SLO SW development, which has been hard to get manpower and correct in the past.
- New harness design required.
- Does not match VXE30 architecture. Bad practice and risk for ground loops, transients, etc. but some LM payloads have operated with a similar method in the past. 
- This may be ok if we verify the ethernet isolation is compatible with all transients, and any other connections like 12V switching are isolated (ex: via SSR).
- Move current sensing to the battery, DCDC after the current sensing. Cam recommends for customer deliverable.
- Better power architecture, closer to havoc plan, less risk.
- Larger scope, but planned for Havoc already, which reduces standalone scope.
- More deviation from VXE architecture, but more industry standard, should reduce risk, and planned for Havoc.

## Plan

Need to decide short term plans for activities like Hatchet integration (Hatchet +E95 probably), AEWE (need to define configuration), and longer term VXE production.

## Comments (0)

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [101-106864 Input Power Assembly, Epsilon 14oz G2_P1.pdf](attachments/24608_101-106864%20Input%20Power%20Assembly,%20Epsilon%2014oz%20G2_P1.pdf.md) | pdf | 123 | 2024-11-19 | converted |
| [Old- 101-109034 Epsilon 140Z G2, WD.PDF](attachments/24609_Old-%20101-109034%20Epsilon%20140Z%20G2,%20WD.PDF.md) | pdf | 37 | 2024-11-19 | converted |
