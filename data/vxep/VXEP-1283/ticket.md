# VXEP-1283: B30 300 - 5/14 MCM failure - had been set to be able to auto DHCP which let it randomly drop the 10 network

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** High
- **Created:** 2025-05-16
- **Updated:** 2025-05-19
- **Resolved:** 2025-05-19
- **Reporter:** Cameron Chapman
- **Assignee:** Ted Trowbridge
- **Creator:** Cameron Chapman
- **Labels:** MCM-Issue
- **Links:** clones VXEP-1282 (B30 689 - MCM failure after return from HSV-Nose fuse blown); is cloned by VXEP-1284 ([REMOVE FROM VXEP] B30 757 - unexplained reset at the flight line)
- **Issue Status:** Issue fixed. Identifying CAs
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

Need to populate issue summary and plan. 
Dave 5/14  “lost an MCM on v689 after its return from HSV. I understand it hasn't been looked into. Today (5/14) we lost one on v300 and v757 had an unexplained reset at the flight line. It sounds like we have a very serious issue on our hands that will require hardware support”

## Corrective Action

- @Ted Trowbridge @Craig Burton @Jo Brown do you think additional processes or documentation for MCM troubleshooting and/or how to reset it to defaults would help prevent and fix issues like this? 
- Jo B After talking with craig, my guess is that OKSI changed something themselves. They have run a lot of scripts on that vehicle that they did not write themselves. My suspicion is that one of them reset the ethernet interface settings. The new developers from OKSI were made aware of the issue. I don't have reason to believe that it will happen again doing forward

## Root Cause

had been set to be able to auto DHCP which let it randomly drop the 10. network, explanation from Jo B.:
"Issue was that the device field on the DHCP connection profile was blank. This means the DHCP connection profile could be (and was) applied to all network adapters.
To oversimplify a bit, it was luck of the draw whether the aircraft Ethernet connection would get a static IP address or a dynamic one."
300 has been played around with a bunch, reflashed to Jetpack
if 300 was configured like a production vehicle, it would not have had that issue

## Comments (2)

### David Grosher, 2025-05-19

This is an integration issue on non-released components, it should not be an incident in the VXEP project.

### David Grosher, 2025-05-19

Will not do 8D process on unreleased components.

## Attachments (0)
