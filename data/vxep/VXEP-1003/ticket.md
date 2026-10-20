# VXEP-1003: LEMB Test Plan and Execution

- **Issue type:** Epic
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2025-02-11
- **Updated:** 2025-06-12
- **Resolved:** 2025-06-12
- **Reporter:** Cameron Chapman
- **Assignee:** Stephen Peters
- **Creator:** Cameron Chapman
- **Parent:** VXEP-824 Prototype LEMB Project-Long Endurance Main Battery

## Plan

@Stephen Peters @Erik Hanson @Tom Westrich tracking test plans/concepts here. Many of these could be cell level tests rather than pack (or both)
- Model testing. 
- Account for:
- Temperature
- Cell life
- Wire loss in aircraft (cell taps may help with closer measurement, but need to update model if using that data)
- Ideally varying power demands, but if we have to, want to optimize for cruise loads and be conservative (model should say the battery is empty before it is actually empty).
- Flight profile testing
- Define and verify battery can meet appropriate requirements
- Climb rate  at defined SOCs. (power at max throttle will reduce as battery voltage sags/reduces).
- Payload and avionics voltage requirement

## Comments (0)

## Attachments (0)
