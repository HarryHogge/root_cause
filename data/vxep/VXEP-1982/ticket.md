# VXEP-1982: VXE 897Failure to launch same error each time

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Won't Do
- **Priority:** High
- **Created:** 2026-08-21
- **Updated:** 2026-08-27
- **Resolved:** 2026-08-27
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Ted Trowbridge
- **Creator:** Alexander Alan Arnold
- **Labels:** Software
- **Links:** relates to VXEP-1290 (VXE 528 aborted launch after 10 feet ); relates to MS-384 (VXE 691 Failed take off - 2 attempts during During PreMAGNSS Verification Test Flight)
- **Customer:** USSS
- **Vehicle Tail Number:** VXE 897
- **Vehicle Configuration:** VXE 30 adv nav Jennings GCS
- **Corrective Action:** rare altitude bug not often observed, closing due to aircraft being updated with ogcs and having a successful flight.
- **Executive Summary:** Issue believed to be rare

## Description

Aircraft aborted 3 times with same error each time.

## Comments (6)

### Alexander Alan Arnold, 2026-08-21

@Ted Trowbridge Similar issue I believe, this aircraft is being blocked from going back to the customer due the SCO flight not being to be able to be completed, we are also going to update the aircraft to OGCS since they just recieved theyre training. I Just need to know if its the same issue, why it reported 400 ft even though operator commanded 200 ft transition, and checking to make sure there is nothing else wrong with it other than the alt bug

### Ted Trowbridge, 2026-08-21

@Alexander Alan Arnold is there anything unusual about the DTED loaded on this laptop?  Has it been used for other launches OK?  Was the same GCS laptop used for each?

### Alexander Alan Arnold, 2026-08-21

@Ted Trowbridge same laptop for all three aborts, its the HSV SCO laptop there should not be anything wrong with it. do I need to retrieve the dted and provide it?

### Ted Trowbridge, 2026-08-21

@Alexander Alan Arnold I don’t need it to be retrieved, but just a quick confirmation that DTED is loaded.  If the laptop has been used for other flights then it’s unlikely to be the cause.

### Alexander Alan Arnold, 2026-08-21

@Ted Trowbridge Recent flights were done with 6.5.0 this is the first time they used it to fly with 6.6.1

### Alexander Alan Arnold, 2026-08-27

legacy bug rarely observed. updated aircraft to OGCS and did not experience issue

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T115_V897_260820_134827_pack.zip | archive | 1368 | 2026-08-21 | listed only |
| T115_V897_260820_143009_pack.zip | archive | 1038 | 2026-08-21 | listed only |
| T115_V897_260820_145349_pack.zip | archive | 1117 | 2026-08-21 | listed only |
| T115_V897_260820_151337_pack.zip | archive | 946 | 2026-08-21 | listed only |
| we.vmis | other | 4 | 2026-08-21 | listed only |
