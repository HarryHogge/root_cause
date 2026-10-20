# GCSS-82: Append kit number to each Windows account created for SGCS1 laptops with UK MoD Hardeneing Mod Kit Applied

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2023-08-25
- **Updated:** 2023-10-03
- **Resolved:** 2023-10-03
- **Reporter:** Craig Burton
- **Assignee:** Wesley Reynolds
- **Creator:** Craig Burton
- **Components:** GCS Application
- **Links:** relates to VXEP-35 (TPTR-102 Windows user account does not show a unique GCS ID); blocks GCSS-44 (Document Procedure for Applying UK MoD Hardening Mod Kit)
- **Sprint:** GCSS Sprint 6, GCSS Sprint 5

## Description

- In the past, the one (admin) account on the SGCS1 laptops had the same name as the laptop itself: SGCS1-XX (XX is the kit number, unique to each laptop).
- For the TIQ program, I was explicitly asked to make 3 accounts: Admin, APC (Air Platform Controller, I think?), and Payload Operator.
- For VXEP-35, it seems like the name of the accounts should be suffixed with -XX just as we have done in the past.

## Comments (4)

### Michael Berger, 2023-08-26

Are we going to ship more than 99 Ground stations UK MOD? might need more than 2 digits

### Wesley Reynolds, 2023-08-28

XX was just meant to represent an arbitrary integer. The first three kits going to the customer are 108, 109, and 110.

### Michael Berger, 2023-08-28

Is that number used in the IP address? Would it be limited to 255?

### Wesley Reynolds, 2023-08-30

It is the number used in the IP address. I believe it would be limited to (2^15) ~= 32,000.

## Attachments (0)
