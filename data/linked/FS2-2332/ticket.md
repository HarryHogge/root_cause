# FS2-2332: Investigate AP Link Loss issues on FW AP

- **Issue type:** Story
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2024-09-26
- **Updated:** 2025-03-22
- **Resolved:** 2025-03-22
- **Reporter:** Jason Scherer
- **Assignee:** Jason Scherer
- **Creator:** Jason Scherer
- **Links:** relates to VXEP-220 (VXE 487 - GCS blocking resulting in multiple FWAP link losses ); relates to VXEP-608 (VXE 336 uncommanded aborted launch); relates to VXEP-284 (VXE-540 Crash after transition at training event); relates to VXEP-1047 (VXE-729 Aborted launch)
- **Sprint:** FS2 Sprint 24, FS2 Sprint 25, FS2 Sprint 32

## Description

Update (3-22-25): It has been confirmed that GCS mission simulation will cause this issue. The GCS is a single threaded application, and when the mission sim is run the uplink messages are not sent to the vehicle. As a result, the vehicle logs a link fault which shows up in the logs as a “ap link fault”. As you can see from the debug message log below, the fault is always proceeded by a GCS mission update.

**Background**

Sometimes, an ap link fault is recorded in the XComm log followed by a link restored message shortly after. This happens frequently in most VXE 30 flights. 
Example of ap link faults recorded in the XComm log below:
[embedded: image-20231212-222157.png]
**Source of the log message on XComm**

This message is logged from the following XComm function:
[embedded: image-20240927-004242.png]
In the above function, the tx value can be false, if (line# 1586) apGetSysState().LandingStatus contains the LSTAT_NOLINK bit value of 0x1000. This value is set on the fixed wing code in the HostInterface::DispatchSystemQuery() function below:
**Fixed Wing LSTAT_NOLINK logic**

[embedded: image-20240927-005143.png]
The fixed wing online boolean variable is set in the HostInterface::ServiceHostComm() function below: 
[embedded: image-20240927-005353.png]
The GetLinkStatus() function is defined in the HostInterface class below. The link status value returned is based on a variable called tlinkok.
[embedded: image-20240927-003430.png]
The tlinkok variable is updated in the HostInterface::MaintainLink() function below. When the function is called, the passed parameter sec (seconds) is added to the current clock value and stored in tlinkok.
[embedded: image-20240927-003402.png]
[embedded: image-20240927-010425.png]
The MaintainLink() function is called (with a value of ONLINE_TIME = 5) 13 times in the HostInterface class in the following functions.
- DispatchTaggedPacket() When receiving the following messages
- MISSION_DATASET_TAG
- MISSION_RECORD_TAG
- VTED_DATA_TAG
- DispatchSystemCommand() When receiving the following messages
- COMMAND_ALTWEAK
- COMMAND_LZ
- COMMAND_ALTMODE
- COMMAND_RTBMODE
- COMMAND_LOSTIMEOUT
- COMMAND_TERRCLEAR
- COMMAND_LOSTIME
- COMMAND_MUAVHOT
- COMMAND_STROBE
- RcvCommand() When receiving the following message
- RAW_UPLOAD

The MaintainLink() function is called (with a value of 0) one time in the RcvCommand() function when receiving a DISCONNECT message.
**Log Message Summary**

So, the message appears in the logs when the fixed wing processor doesn’t receive one of the above messages for ~5 seconds. 
**Root Cause Analysis**

Initially, it was thought that the datalink was dropping out, however, frequently this issue would be found in incidents that had launch aborts where the vehicle is very close to the ground station, and should not be losing link.
Further analysis shows that sometimes (example below) a large uptick in fixed wing serial traffic transmission occurs prior/during the link fault messages. At that point we became suspicious that the fixed wing processor might be delaying serial reads due to a large transmit queue which prevents processing of serial messages for some time. Because of a delay in serial reads the fixed wing ap acts like a data link outage has occurred, or so we think.

[embedded: image-20240927-001852.png]

## Comments (3)

### Jason Scherer, 2024-09-26

Also relates to NCR-240617 - 3540

### Jason Scherer, 2024-10-02

Note to self: fw serial spike anomaly on successful VTOL landing. For future reference. 
[embedded: image-20241002-183118.png]

### Jason Scherer, 2025-03-22

Root cause believed to be GCS mission sim preventing uplink messages which trigger link timeouts resulting in log messages.

## Attachments (9)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20231212-222157.png | image | 131 | 2024-09-26 | listed only |
| image-20240927-001852.png | image | 214 | 2024-09-26 | listed only |
| image-20240927-003402.png | image | 24 | 2024-09-26 | listed only |
| image-20240927-003430 (5a5bc102-954e-4cdf-a93f-ea2abd95bf4b).png | image | 10 | 2024-09-26 | listed only |
| image-20240927-004242.png | image | 86 | 2024-09-26 | listed only |
| image-20240927-005143.png | image | 4 | 2024-09-26 | listed only |
| image-20240927-005353.png | image | 4 | 2024-09-26 | listed only |
| image-20240927-010425.png | image | 2 | 2024-09-26 | listed only |
| image-20241002-183118.png | image | 242 | 2024-10-02 | listed only |
