# VXEP-7: TPTR-89 Windows Hardening Build Implementation

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2023-08-23
- **Updated:** 2026-02-02
- **Resolved:** 2024-02-29
- **Reporter:** Allen Gardner
- **Assignee:** Craig Burton
- **Creator:** Allen Gardner
- **Links:** is caused by GCSS-79 (Ship Laptop or Hard Drive to LMUK); is caused by GCSS-80 (Hold CCB for Windows Hardening Solution and Release to Production); is blocked by GCSS-76 (Prepare UK Hardened SGCS1 for Pen Testing); is blocked by GCSS-88 (Receive Feedback Regarding UK MoD Hardening Mod Kit on SGCS1 Pen Testing); is blocked by GCSS-87 (Deliver SGCS1 Laptop to LMUK for Pen Testing); is blocked by GCSS-86 (Get Delivery Instructions From LMUK For Pen Testing); is blocked by GCSS-44 (Document Procedure for Applying UK MoD Hardening Mod Kit); is blocked by GCSS-47 (Train Production to Apply Windows Hardening Mod Kit); is blocked by VA-644 (Complete approval (fix AR), and deploy UK Windows hardening build); is blocked by GCSS-133 (Release the UK MoD Hardening Mod Kit for the SGCS1 Laptop)
- **Customer:** TIQUILA
- **Root Cause:** Engineering did not implement full scope of the guidance provided by LMUK
- **Severity:** 1 - Flight Critical
- **Impacted Disciplines:** Software, Hardware
- **Impacted Core Subsystems:** Ground Systems

## Description

Problem: During STALKER FAT in SLO, it was noted that some policies for the windows hardening build may not have been implemented fully, allowing operators to carry out certain functions that would not be allowed during the operation of the system based on the policies indicated by the NCSC.
Examples include: FIPS Mode in Silvus settings not enabled, No user notification that Encryption key is present in the encryption key box, Not secure observed on browser during SSH/HHTPs checks, Software can be run directly from USB, Ability to access USBs.  Note following further investigations into Windows Hardening build, this issue may need to be broken out into multiple PTRs.

Desired Behavior: Windows hardening build is implemented as per the guidance provided by LMUK and in accordance with the NCSC Guidelines

## Corrective Action

Engineering: 
- Implement new Window Hardened Build Image, deploy on SGCS1-109 -COMPLETE
- Generate evidence package -COMPLETE
- Send to LMUK for PEN testing – WAITING FOR DIRECTION FROM LM
- Need to ship laptop to LM for testing.
- CCB and implement

## Comments (7)

### Craig Burton, 2023-08-24

Tracking PEN testing readiness via https://jenaero.atlassian.net/browse/GCSS-76.

### Cameron Chapman, 2023-08-24

Awaiting approval from LM to CCB

### Greg Fryer, 2023-08-29

@Craig Burton is updating the linked issues to make sure they are a complete set of assigned tasks, that are in the current sprint. that includes “waiting” since part of waiting is getting status and pushing where possible. (Similar to a “wait for ordered parts to arrive”).
@Carl Graf @Cameron Chapman FYI.

### Wesley Reynolds, 2023-08-29

I have updated the is blocked by issues to include all of the blocking issues that I am aware of.
This set of issues assumes that pen testing will go well and will not raise more issues. If there are issues, https://jenaero.atlassian.net/browse/GCSS-87 and https://jenaero.atlassian.net/browse/GCSS-88 will need to be repeated after the newly raised issues are resolved.
The current status of this issue: We are waiting for LMUK to tell us when/where to ship their laptop, SGCS1-109. This laptop is ready for their pen tests.

### Matt Philley, 2023-09-25

Added link to NCR 1572 which is documenting approval to ship SGCS1 Kits SN 108, 109, 110 with MOD Kit 150-113727 as-is with the Windows Hardening not yet approved by the Customer. 
These are planned to ship today 9/25/23.

### Wesley Reynolds, 2023-10-24

I have created the following ticket:
https://jenaero.atlassian.net/browse/GCSS-133 
To better track the progress that has been made/needs to happen regarding this issue.

### Craig Burton, 2024-02-29

Resolved and approved by customer.  Closing.

## Attachments (0)
