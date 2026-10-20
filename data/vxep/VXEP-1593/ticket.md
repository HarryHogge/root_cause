# VXEP-1593: VXE-886 Lost link upon Transition to FW

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-11-11
- **Updated:** 2025-11-25
- **Resolved:** 2025-11-25
- **Reporter:** Jackson Riley Curvin
- **Assignee:** John Molina
- **Creator:** Jackson Riley Curvin
- **Labels:** Edge_Asset
- **Sprint:** NCC Sprint 10
- **Vehicle Tail Number:** VXE-886
- **Vehicle Configuration:** ADV NAV Standard Main Battery
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

After the aircraft launched, transitioned, and flew through WP1, the aircraft immediately lost comms. The aircaft node in the Silvus GUI completely disappeared. Through troubleshooting on Silvus the aircraft communications were very spotty. I ws able to get just enough link to send an updated PLZ and RTB command. The aircraft then completely its landing with comms being very intermittent throughout the entire landing plan.

## Comments (9)

### Jackson Riley Curvin, 2025-11-11

[embedded image-20251111-175551.png]

### Jackson Riley Curvin, 2025-11-11

[embedded image-20251111-175642.png]

### David Grosher, 2025-11-11

@Jackson Riley Curvin I assigned this to @John Molina given that the Silvus lost connection between the two radios.

### Jackson Riley Curvin, 2025-11-11

[embedded image-20251111-175731.png]

### Greg Fryer, 2025-11-11

@Jo Brown John is out today, can you take a quick look and see if anything is obviously wrong?

### Jo Brown, 2025-11-11

@Jackson Riley Curvin a few questions on this to try and get a better picture.
- What was the ground setup like? How many radios were on, and what models were they?
- Were other aircraft flown on the same setup, or just 1?
- Did you have connectivity issues once you were on the ground?

### Jackson Riley Curvin, 2025-11-11

@Jo Brown I think I got it sorted they ran a spectrum scan and there was significant noise on the frequency they were using so they switched frequencies, and I am waiting to hear back to see if that resolved their issue.

### Jackson Riley Curvin, 2025-11-11

@Jo Brown  they had 2 different flights first flight SGCS2 wired into the GCS
second flight SGCS1 with MAG Mounts. aircraft was good on the ground.

### Jackson Riley Curvin, 2025-11-25

Aircraft performed as expected

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T115_V886_251111_100747_pack.zip | archive | 2602 | 2025-11-11 | listed only |
| image-20251111-175551.png | image | 60 | 2025-11-11 | listed only |
| image-20251111-175642.png | image | 54 | 2025-11-11 | listed only |
| image-20251111-175731.png | image | 37 | 2025-11-11 | listed only |
