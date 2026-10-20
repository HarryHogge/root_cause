# VXEP-1442: Handle off nominal time.

- **Issue type:** Task
- **Status:** New
- **Priority:** Low
- **Created:** 2025-07-21
- **Updated:** 2025-07-21
- **Reporter:** Eric Brewer
- **Creator:** Eric Brewer
- **Parent:** VXEP-1237 Apex Must Haves (VBN)
- **Epic Link:** VXEP-1237

## Description

For case with no time or spoofed time:
- Nothing explicitly should break but we'll need to test
- Operator log-in to OGCS should use laptop system time to set time on the OGCS.  The very act of logging in grabs the PC's system time and sends that time to the backend, where it is written out in the filesystem.
- If NovAtel sends a time that is wrong (in the case we can't use approxtime) then mcm/ogcs time will also need to the be same 'wrong' time for the system to work.
- Yes, depending.  If the timestamp's year is 2023 or earlier, for example, the set_system_time utility will reject it.  But there are lots of places where it would accept a "close" value that would not pass validation by the web browser's time-based security checks.  Again, lots of testing needed.  If the VSM accepts a time that is off by more than 24 hours from laptop time, you won’t be able to log in.

To keep everything in sync and talking, I believe we’ll need two main changes:
1.  In full GPS denial, the laptop time will become the ‘truth’.  When the user logs into the OGCS, the time will be updated on the backend automatically.  For GPS denied ops, this time needs to also be sent to the novatel using the ‘setapproxtime’ command.  NOTE: this command appears to break the receiver today so we need an update from NovAtel before we implement.
2. If the time on MCM or novatel drift too far from laptop time, they will need to be reset - similar to startup procedure.  We’ll also need to make sure each system component can handle this step jump in system time.

## Comments (0)

## Attachments (0)
