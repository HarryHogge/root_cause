# VXEP-1406: Implement OGCS interface method to adjust altimeter setting based upon local atmospheric conditions.  See companion ticket 1405 for flight software.

- **Issue type:** Task
- **Status:** New
- **Priority:** Low
- **Created:** 2025-07-14
- **Updated:** 2025-07-21
- **Reporter:** Eric Brewer
- **Creator:** Eric Brewer
- **Parent:** VXEP-1237 Apex Must Haves (VBN)
- **Epic Link:** VXEP-1237

## Description

When GPS is denied, altitude information is based upon VBN or Baro which can be inaccurate or change over time.  In the event the errors are large enough, we may need a way to adjust the vehicle altitude estimate to allow it to climb or descend to a safe altitude.

## Comments (3)

### Eric Brewer, 2025-07-21

@Craig Burton @Ted Trowbridge not sure if this would be OGCS, VSM or both.

### Ted Trowbridge, 2025-07-21

@Eric Brewer It would be both.  I’d like to meet to discuss - I didn’t think we flew a pure pressure altitude, do we in VBN mode?

### Eric Brewer, 2025-07-21

@Ted Trowbridge when VBN is active we treat it like GPS updates so it should look the same as GPS available provided that VBN is accurate.  The updates here are more for the case where we lose both VBN and GPS, in that case it’s all based upon pressure so if it happens to drift over time (or if somehow vbn or gps was inaccurate for some reason) we may need to adjust.

## Attachments (0)
