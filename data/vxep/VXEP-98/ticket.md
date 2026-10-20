# VXEP-98: TPTR-99 Launch wizard does not specifically indicate GPS issue

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2023-08-23
- **Updated:** 2025-08-05
- **Resolved:** 2025-08-05
- **Reporter:** Allen Gardner
- **Assignee:** Ted Trowbridge
- **Creator:** Allen Gardner
- **Customer:** TIQUILA
- **Corrective Action:** Possible: Update message with more clear exit criteria and instruction (push cancel).
- **Plan:** Review messages shown to user and status of Troubleshooting Quicksheet
- **Incident Type:** Squawk
- **Severity:** 3 - Degraded Performance - With Workaround
- **Impacted Disciplines:** Software
- **Impacted Core Subsystems:** Ground Systems

## Description

Failure of SRD-309
During TO1 STALKER FAT, a test was conducted to trigger a degrading GPS signal. and launch wizard process was followed. It was expected that the Launch wizard would indicate the GPS issue and could not be completed, however the LW does not specifically indicate the GPS issue and instead GCS calibration window does not go past its window

## Root Cause

User expected more explicit instructions or may not have access to troubleshooting sheet.
(Original text: Misalignment between aircraft specs and acceptance criteria; likely based on expectation that the system should time-out in this stage, which we do not want to include to allow user to try adressing the issue.)

## Comments (8)

### Allen Gardner, 2023-08-24

@Sam Miller What is the next action here?

### Greg Fryer, 2023-10-05

@Craig Burton I believe this improvement is in the GCSS project. Can you please make that issue a blocker of this VXEP problem? If it is more complicated than one bug, please make an epic to parent the tasks. Happy to discuss and go through mechanism.

### Craig Burton, 2023-10-05

@Greg Fryer While we do have a more generalized messaging enhancement documented in GCSS (GCSS-34), the “GPS Fix Check” dialog within the Launch Wizard already indicates why the LW does not allow a user to proceed.
In the event of no GPS fix on the vehicle, the user is presented with Status of “Waiting for GPS Fix” in the lower left hand portion of the dialog.  The “Next>” button is disabled in this condition:
[embedded file]
When the fix is valid (as reported by the vehicle to GCS), the “Next>” button is enabled and the Status message changes to “GPS Fix Valid“:
[embedded file]

### Greg Fryer, 2023-10-06

@Craig Burton A couple notes on this one. I think your description matches what was experienced during test. I think the issue might be better phrased: The pilot is trapped at this step if GPS doesn’t get a fix. A couple possibilities:
- Does the “Troubleshooting Quicksheet” mentioned in the message exist? Is it a file on the GCS? Should we alter the message with a pointer to it, if it is located on the GCS?
- Should we add a third bullet to the sheet to indicate “if troubleshooting does not work, most likely there is insufficient GPS signal to support system operation. Select Cancel and try another location or time.” This defines a clear exit of what to do, which may be what is missing.

Either way, you are right this is distinct from the “aircraft aborts after launch due to poor GPS at altitude” message fix we have planned.

@Wesley Lilienthal Maybe comment on my “insufficient GPS signal” - is that a normal phrasing? Keeping in mind this if or users and not radio/GPS technicians. 🙂

### Craig Burton, 2023-10-06

@Greg Fryer The “Troubleshooting Quicksheet” is a section within a PDF manual (“Stalker XE25 Quicksheets Rev B_2021.05.06”) that is installed by the GCS installer:
[embedded file]
The specific section is this:
[embedded file]

### Michael Berger, 2023-10-09

I don’t think link to this Quicksheet would be a good idea. This is a Block 25 Quicksheet (XE25 in the title) and will likely go away when support for Block 25 is phased out.
Training should direct users to where manuals etc are located on the GCS.
Operators should not be expected to be able to operate the vehicle without training.
Possibly an update to the Operators Manual would be appropriate.

### Wesley Lilienthal, 2023-10-09

@Greg Fryer Yes, “insufficient GPS signal” is appropriate phrasing for end users.

### Christa Meck, 2025-08-05

Closing this incident as it’s from August 2023 and any investigation is likely done at this point.

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| gps-fix-valid.png | image | 28 | 2023-10-05 | listed only |
| waiting-for-gps-fix.png | image | 29 | 2023-10-05 | listed only |
| [Stalker XE25 Quicksheets Rev B_2021.05.06.pdf](attachments/16871_Stalker%20XE25%20Quicksheets%20Rev%20B_2021.05.06.pdf.md) | pdf | 26916 | 2023-10-06 | converted |
| troubleshooting.png | image | 83 | 2023-10-06 | listed only |
