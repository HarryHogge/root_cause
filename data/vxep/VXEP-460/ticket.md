# VXEP-460: Ethernet dropout with load transient.

- **Issue type:** Bug
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2024-07-02
- **Updated:** 2026-03-30
- **Resolved:** 2026-03-30
- **Reporter:** Cameron Chapman
- **Creator:** Cameron Chapman
- **Parent:** VXEP-456 Create list of issues discovered, improvement ideas, tests recommended. Prioritize the list and determine implementation plan
- **Epic Link:** VXEP-456
- **Issue color:** purple
- **Plan:** Maybe fixable with Grey wire removed and bonding wire between batteries (I used a banana cable @ 12 gauge)

## Description

- This is voltage readings / ethernet flow in the nominal configuration when I apply a 2 volt droop to simulate engine load.  Recording 2024-06-20 181819-greysintalledtransient.mp4
- Note 1:  2 volts may be a large droop for this system.  That battery is very capable.  It may be a rare case that the battery system droops that far. It also could be a common occurrence and because it recovers people don’t care.
- The dropout of the ethernet is easy to see.  It is possible the CAN bus and other devices are being knocked out too.
- The security context stays active (The credentials I passed the autopilot), so I don’t believe we had an autopilot reboot.
- The voltage in this configuration is off by several 100 millivolts and the current bounces a lot. When the grey wire is removed and a ground wire installed the values are off by a few millivolts, current is even more bouncy.

## Comments (1)

### Garrett O'Neill, 2024-07-02

AAR logs from Abel’s test:
[embedded file]

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| V455 Data.zip | archive | 33955 | 2024-07-02 | listed only |
