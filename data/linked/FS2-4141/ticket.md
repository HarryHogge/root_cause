# FS2-4141: B40 WDT reset during RC fwd power check

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2025-12-31
- **Updated:** 2026-02-24
- **Resolved:** 2026-02-24
- **Reporter:** Scott Whitney
- **Assignee:** Scott Whitney
- **Creator:** Scott Whitney
- **Parent:** FS2-4309 B40 WD Investigation
- **Links:** relates to VXEP-1692 (B40/30 XCOM WDT resets )
- **Epic Link:** FS2-4309
- **Sprint:** FS2 Sprint 35, FS2 Sprint 37, FS2 Sprint 36

## Description

- Multiple WDs seen on 882 only. Replaced avionics and retesting.
- removed avionics to be red tagged or labelled. Will install into a HIL for further testing. @Scott Whitney  will record PN and SN of the parts removed, and what HIL it ends up in.


20251231-Ground Testing - Note: the reset happens in the 4P run
A very similar exception happened in the field on 12/30 - Flight 1 - 4P Main 2.0
**documented here https://jenaero.atlassian.net/wiki/spaces/VXEA/pages/1012137991/B40+Release+Candidate+2**

**Old Plan 1: (Est. ~1 week)-Needs an update**

- Go back to the known ‘good’ xcomm version.
- Identify and pull in critical changes from the 6.6.1 release and create Release Candidate 2 (1 day)
- It is assumed that the File I/O changes from 6.6.1 caused the wd boot
- Endurance test RelCan2 on vehicle 882 (1 day)
- Progression Test Release Candidate 2 (2 days)
- Safety of Flight Release Candidate 2 (1 day)

## Comments (1)

### Scott Hunter, 2026-01-02

The Ground Testing episode was spinning the fwd motor from RC control.
The reset in the field, per Cody’s notes/memory “was probably just sitting for the period of time i was going back and forth getting things prepped”

Initial questions:
What .hex file is loaded in XC?  Verify B40 build not B35What configuration was the vehicleWhat is happening with power
“Flight 1”
```
[19:58:35.143 1.143] WD BOOT 16
[19:58:35.143 1.143] Index 0
[19:58:35.143 1.143] diag0 153
[19:58:35.144 1.144] diag1 0
[19:58:35.145 1.145] diag2 0
[19:58:35.145 1.145] diag3 0
[19:58:35.145 1.146] diag4 0
[19:58:35.146 1.146] diag5 0
[19:58:35.146 1.146] diag6 0
[19:58:35.147 1.147] diag7 0
** crash restart dump **
Crash@: 8003201c 0000ffff
reset reason: 00000010 : WDT
nmi reason: 00000000
crash addr: 9d0b0aa8
crash diag[0]: 00000000
crash diag[1]: 00000000
crash diag[2]: 00000000
crash diag[3]: 00000000
crash diag[4]: 00000099
crash diag[5]: 00000000
crash diag[6]: 00000000

```
“4P Run WDT”
```
[22:40:25.144 1.144] WD BOOT 16
[22:40:25.144 1.144] Index 0
[22:40:25.144 1.145] diag0 153
[22:40:25.145 1.145] diag1 0
[22:40:25.146 1.146] diag2 0
[22:40:25.146 1.146] diag3 0
[22:40:25.147 1.147] diag4 0
[22:40:25.147 1.147] diag5 0
[22:40:25.147 1.147] diag6 0
[22:40:25.148 1.148] diag7 0
** crash restart dump **
Crash@: 8003201c 0000ffff
reset reason: 00000010 : WDT
nmi reason: 00000000
crash addr: 9d0b0aa8
crash diag[0]: 00000000
crash diag[1]: 00000000
crash diag[2]: 00000000
crash diag[3]: 00000000
crash diag[4]: 00000099
crash diag[5]: 00000000
crash diag[6]: 00000000

```

## Attachments (0)
