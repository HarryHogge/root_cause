# VXEP-30: TPTR-57 Jennings GCS stopped responding to the user

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed, but added to Bermuda Triangle List
- **Resolution:** Cannot Reproduce
- **Priority:** Low
- **Created:** 2023-08-23
- **Updated:** 2025-02-14
- **Resolved:** 2025-02-14
- **Reporter:** Allen Gardner
- **Assignee:** David Grosher
- **Creator:** Allen Gardner
- **Customer:** TIQUILA
- **Incident Type:** Squawk
- **Severity:** 3 - Degraded Performance - With Workaround
- **Impacted Core Subsystems:** Ground Systems

## Description

Jennings GCS stopped responding to user inputs but continued to display aircraft data, it was suspected that this was due to the heat in the area and after a reboot the system worked. This only deserved a DASOR due to the fact that during the reset the aircraft was no longer in comms with any GCS.

## Issue Status

Unable to replicate issue. GCS laptop has since changed to a newer, completely different model.  The new laptop is MIL-STD-810H compliant.  

Masters, Alexander J (UK) - Tue Jul 11 11:09:32 BST 2023 : DASOR reference - asor\ASWC - DHF\744 NAS\RPAS Specific S2\23\6811
Latest report attached [^20230711-DASOR-23-6811.pdf]

## Comments (7)

### Allen Gardner, 2023-08-24

@Craig Burton Please discuss with @Sam Miller to determine next steps. Do we need to fix a problem here, or is this just an unsolvable mystery that needs to be closed?

### Craig Burton, 2023-08-29

Reached out to Sam via email to discuss this and https://jenaero.atlassian.net/browse/VXEP-34.

### Sam Miller, 2023-09-01

Recommended closure due to GCS laptop hardware change from the Dell 7424 used in training to the Dell 7330 being delivered with the program.  It is possible that the processor went into low power mode due to running on battery power or due to heat.  We will monitor on the new laptop.

### Carl Denslow, 2024-02-16

@Craig Burton what is next step with this issue? It appears to be functionally resolved. I don’t think this should be included in the “limitations” section of the tiqila DDP, but checking if the ticket can be closed or if I should include this behavior in the limitations document.

### Craig Burton, 2024-02-16

I concur with Sam’s comment from 9/1/23 in which he recommends closing this issue.

### David Grosher, 2024-09-05

@Pat Wells This issue can’t be resolved with the data that we have. It has been suggested that we close it. The new GCS versions have Windows Error Reporting to catch when the GCS crashes although Freezing might not generate an error. I’m not sure if TIQUILA is still tracking this TPTR.

### David Grosher, 2025-02-14

We can’t resolve the issue with the available data. The customer’s needs have been addressed with a new laptop computer which is a MIL SPEC’d model.

## Attachments (0)
