# GCSS-88: Receive Feedback Regarding UK MoD Hardening Mod Kit on SGCS1 Pen Testing

- **Issue type:** Story
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2023-08-29
- **Updated:** 2023-10-23
- **Resolved:** 2023-10-23
- **Reporter:** Wesley Reynolds
- **Assignee:** Wesley Reynolds
- **Creator:** Wesley Reynolds
- **Parent:** VA-644 Complete approval (fix AR), and deploy UK Windows hardening build
- **Links:** is blocked by GCSS-87 (Deliver SGCS1 Laptop to LMUK for Pen Testing); blocks GCSS-44 (Document Procedure for Applying UK MoD Hardening Mod Kit); blocks VXEP-7 (TPTR-89 Windows Hardening Build Implementation)
- **Epic Link:** VA-644
- **Sprint:** GCSS Sprint 6, GCSS Sprint 5, GCSS Sprint 7

## Description

LMUK is performing penetration tests to ensure the security of the SGCS1 laptops. After sending them an SGCS1 to preform the tests on, they will preform the tests and tell us about the results.

## Comments (3)

### Wesley Reynolds, 2023-10-05

There is one outstanding issue with the laptop:

”the autorun functionality is still present, however this time only from the Admin account. To fix this a change would be needed to one of the group policies”.

On these laptops, it should not be possible to run an executable directly from a USB device.

### Wesley Reynolds, 2023-10-05

Possible solution: enable the following Group Policy:
Computer Configuration/Administrative Templates/System/Removable Storage Access/Removable Disks: Deny execute access.

### Wesley Reynolds, 2023-10-23

There are 3 deliverables due by 10/27/23:
- Evidence that the suggested group policy disables software execution from removable media devices.
- A diagram of the network traffic.
- FIPS mode needs to be enabled on the Silvus radios.

## Attachments (0)
