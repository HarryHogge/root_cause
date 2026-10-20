# VXEP-1597: Current and overtemp limit non-crit 28V hood switch, CW non critical, and lower payload

- **Issue type:** Sub-task
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Medium
- **Created:** 2025-11-12
- **Updated:** 2026-10-08
- **Resolved:** 2026-10-08
- **Reporter:** Cameron Chapman
- **Assignee:** Jacob Troyer
- **Creator:** Cameron Chapman
- **Parent:** VXEP-1575 Sort subtasks by MVP-Aircraft Firmware development required for MB Interface to aircraft
- **Links:** relates to FS2-3794 ( BLK 40 Fuel Cell Support); relates to BAT-953 (Define operational temperature range of B40 batteries and 28V converter (power limits over expected temp range, CAWs, automatic behavior, etc). ); relates to BAT-1411 (Document, test, and release DCDC FW 2.0.0 (load shedding)  )

## Plan

- Document hardware current limits (each output and DCDC total).
- Recommend BMS or flight firmware limiting logic and urgency. @Frank Sundell has latest 28V budget.
- Asking @Scott Whitney implementation timeline.
- Implement according to plan.

## Comments (1)

### Cameron Chapman, 2025-11-12

Cameron Chapman
Abel Markow I am predicting that aircraft controlling non-critical current limiting will be out of scope for initial deliveries. So I think it will be hardware limit (need to lookup/document, i think 7.5A per non-crit output), BMS firmware, or nothing until flight FW gets updated in the future. Tho…

"need to lookup/document, i think 7.5A per non-crit output"
Yeah we wanted 7.5A for the switch going to the SSR board and lower payload (rating of MB output connector) and 7A to hood (rating of ODU). Also documented in Block 40 Compliance Matrix.xlsx

[embedded image-20251112-215659.png]

 
[embedded image-20251112-215654.png]
7.5A makes sense for pin and wire ratings. 3x7.5A*28=630W, so I think we will want additional limiting when available
 
Personally, I think a temporary basic non-crit limit in BMS FW is better than none until aircraft FW is ready (might be various points next year)
 
I guess we should start by asking FS. I'll do that

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20251112-215654.png | image | 158 | 2025-11-12 | listed only |
| image-20251112-215659.png | image | 122 | 2025-11-12 | listed only |
