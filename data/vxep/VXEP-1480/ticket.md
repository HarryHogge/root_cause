# VXEP-1480: VXE-815 Failed to descend

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-08-20
- **Updated:** 2026-03-02
- **Resolved:** 2026-01-13
- **Reporter:** Jackson Riley Curvin
- **Assignee:** David Grosher
- **Creator:** Jackson Riley Curvin
- **Labels:** TIQUILA
- **Links:** relates to VXEP-1570 (VXE-815 Failed to descend )
- **Customer:** TIQUILA
- **Vehicle Tail Number:** VXE-815
- **Vehicle Configuration:** VXE-30 Battery Configuration
- **Problem Type:** Discovered Issue
- **Issue Status:** Complete.
- **Root Cause:** Operating outside wind limits.
- **Severity:** 3 - Degraded Performance - With Workaround
- **Components (EA Aircraft):** Aircraft, full assembly

## Description

While on a meeting with TIQ operator stated that they had an aircraft that transitioned but did not descend.

## Corrective Action

@Josh Burrell Is this phenomenon captured in the documentation? If you are descending outside of windlimits the lift may prevent the aircraft from descending, and there will be limited power draw from the HLB.

## Comments (5)

### David Grosher, 2025-08-20

This appears to have been actively landing in VTOL for about 18 minutes. Additionally, there appears to be a significant amount of wind, which may have generated a lot of lift preventing the system from descending and reducing the energy draw during this time.

### David Grosher, 2025-08-20

@Eric Brewer @Ben Triplett This isn’t a current priority but it is something we will need to look into. See below.

### Eric Brewer, 2025-08-22

@David Grosher this looks like it was outside the wind limits and just couldn’t descend.  It is holding station in VTOL with motors bouncing off the rails low
[embedded image-20250822-164651.png]
[embedded image-20250822-164803.png]
Also do you know if this was in theater? The altitude estimate above takeoff point goes negative - so either they took off from a hill and flew into a valley or the GPS altitude was not right:

[embedded image-20250822-164923.png]

### David Grosher, 2025-10-28

@Jackson Riley Curvin Was the analysis below provided to the customer. I know that I informally discussed it with them.  I’m wondering why we would even accept the same issue from TIQ on the same bird.

### Jackson Riley Curvin, 2026-01-13

Aircraft performed as expected.

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_V815_20250819T160210Z.zip | archive | 73549 | 2025-08-20 | listed only |
| image-20250822-164651.png | image | 33 | 2025-08-22 | listed only |
| image-20250822-164803.png | image | 59 | 2025-08-22 | listed only |
| image-20250822-164923.png | image | 41 | 2025-08-22 | listed only |
