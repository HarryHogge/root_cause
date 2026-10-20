# VXEP-35: TPTR-102 Windows user account does not show a unique GCS ID

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2023-08-23
- **Updated:** 2024-09-06
- **Resolved:** 2024-09-06
- **Reporter:** Allen Gardner
- **Assignee:** David Grosher
- **Creator:** Allen Gardner
- **Links:** relates to GCSS-82 (Append kit number to each Windows account created for SGCS1 laptops with UK MoD Hardeneing Mod Kit Applied)
- **Customer:** TIQUILA
- **Incident Type:** Squawk
- **Severity:** 4 - Annoyance
- **Impacted Core Subsystems:** Ground Systems

## Description

During TO1 STALKER FAT, a test was conducted to identify is the GCS generated a unique ID. The Test failed and instead APC was observed.

## Comments (7)

### Michael Berger, 2023-08-24

Need feedback on what this really means. What is APC?

### Craig Burton, 2023-08-24

@Wesley Reynolds provided some clarification:
- In the past, the one (admin) account on the SGCS1 laptops had the same name as the laptop itself: SGCS1-XX (XX is the kit number, unique to each laptop).
- For the TIQ program, I was explicitly asked to make 3 accounts: Admin, APC (Air Platform Controller, I think?), and Payload Operator.
- For VXEP-35, it seems like the name of the accounts should be suffixed with -XX just as we have done in the past.

### Allen Gardner, 2023-08-24

@Craig Burton can you create corrective action task(s) within the GCSS project to resolve this issue and add to the corrective action plan.

### Allen Gardner, 2023-08-24

@Craig Burton Let’s see if we can add this to the upcoming sprint for an easy win.

### Craig Burton, 2023-08-25

Created https://jenaero.atlassian.net/browse/GCSS-82 to track.  Will be scheduled in the next sprint.

### David Grosher, 2024-09-05

@Michael Berger Has the task below been included in previous releases? I suspect this ticket should be closed.

### Michael Berger, 2024-09-05

@David Grosher This is not connected to any release or the GCS Software, it is part of the GCS hardware setup process. It appears to be done.

## Attachments (0)
