# MS-1669: VSM:  Require Landing Pattern Altitude to be 100 ft AGL or Higher

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2026-06-22
- **Updated:** 2026-06-24
- **Resolved:** 2026-06-24
- **Reporter:** Craig Burton
- **Assignee:** Craig Burton
- **Creator:** Craig Burton
- **Sprint:** MS Sprint 34

## Description

- Restrict landing pattern altitude to be specified between 100 and 500 feet inclusive.
- Ensure IP1 altitude is greater than or equal to pattern altitude so that the vehicle does not have to climb into IP2, which is a descending orbit.

## Comments (3)

### Cody Smisek, 2026-06-23

@Craig Burton @Ted Trowbridge Will this also impact land immediately? Personal opinion is that land immediately should be left as is and permit operator to activate at any altitude.

### Ted Trowbridge, 2026-06-23

@Cody Smisek I don’t plan to implement anything related to Land Immediately and I agree with you that it should be left as-is as a safety critical feature that can be used at any altitude (with a warning that you can override if the vehicle is too high)

### Craig Burton, 2026-06-24

Tested, reviewed and merged.

## Attachments (0)
