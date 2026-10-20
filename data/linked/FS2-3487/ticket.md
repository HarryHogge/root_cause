# FS2-3487: Implement buffering to prevent loss of xcomm log data on error.

- **Issue type:** Task
- **Status:** To Do
- **Priority:** Low
- **Created:** 2025-07-17
- **Updated:** 2025-10-08
- **Reporter:** Eric Brewer
- **Creator:** Eric Brewer

## Description

See [VXEP-1291] VXE 592 Crash - Jira
This has happened on other incidents as well - but basically if the aircraft crashes and loses power, the xcomm log will have been buffering for awhile so we lose quite a bit of data making investigations difficult.  FDRRecover is implemented on fixed-wing which handles this type of situation, but xcomm does not have something similar.
To be more specific, we need to buffer data at 10Hz during FW flight so that if an error is detected we can log the data along with high rate data for the next ~30 seconds so that the issue can be properly debugged. Once an error is detected it needs to start writing to an error log file. The risk of data loss during an actual crash is something we will always have to live with unless we are buffering to non-volatile memory.

## Comments (3)

### Scott Whitney, 2025-10-08

@Eric Brewer  - does this CA need to be implemented in an upcoming release?

### Eric Brewer, 2025-10-08

@Scott Whitney it would be really nice. We have had a few crashes where the log data is lost and it makes the investigation quite difficult.  
I do not know how difficult it would be to implement.

### Scott Whitney, 2025-10-08

@Eric Brewer  - we should discuss the implementation of this or even just re-evaluate how logging should work. It won’t make it into the 6.6 release, but we can start building out a plan to get it into future releases.

One recommendation from Dave is to buffer data at 10Hz and if an error is detected, save the buffer and the next 30 seconds in an error log or at a higher rate in the data log. Because in FW flight we only get 1 sample every 10 seconds.

## Attachments (0)
