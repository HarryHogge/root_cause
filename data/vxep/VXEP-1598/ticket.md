# VXEP-1598: VXE-674 Auto RTB Low energy Main Battery percentage 57% 26.6V

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed, but added to Bermuda Triangle List
- **Resolution:** Cannot Reproduce
- **Priority:** Highest
- **Created:** 2025-11-12
- **Updated:** 2026-07-07
- **Resolved:** 2026-07-07
- **Reporter:** Jackson Riley Curvin
- **Assignee:** David Grosher
- **Creator:** Jackson Riley Curvin
- **Labels:** Edge_Asset, GS_Closed, Weekly-incident-tracker
- **Links:** relates to FS2-4161 (VXE-674 Auto RTB Low energy Main Battery percentage 57% 26.6V)
- **Customer:** Edge_Asset
- **Vehicle Tail Number:** VXE-674
- **Vehicle Configuration:** https://jenaero.atlassian.net/browse/VXE-30#icft=VXE-30 Main Battery
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

While conducting U-drive, the aircraft experienced a warning that displayed a "Low energy/low endurance" message. The aircraft immediately RTB'd and began its landing pattern. When the message was displayed the main battery was reading 57% charge and a voltage of 26.6V in the aircraft display window. I have flown aircraft with a lower charge and voltage reading and never seen this warning in previous firmware.

## Comments (4)

### David Grosher, 2026-01-06

@Scott Whitney This might be a good issue to get someone some experience with investigations.

### David Grosher, 2026-01-14

Initial look: I see that the event occurred in the GCS debug log, but there is no indication of a low power RTB in the XCOMM event log or the datalog. I reached out to Ted regarding the GCS logic.

### Jackson Riley Curvin, 2026-06-30

@David Grosher @Ted Trowbridge  Can we get a status on this?

### Jackson Riley Curvin, 2026-07-07

Unable to determine root cause

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V674_251112_150801_pack.zip | archive | 2465 | 2025-11-12 | listed only |
