# VXEP-34: TPTR-98 Platform outputs onto GCS (SRD-309)

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2023-08-23
- **Updated:** 2025-02-14
- **Resolved:** 2025-02-14
- **Reporter:** Allen Gardner
- **Assignee:** David Grosher
- **Creator:** Allen Gardner
- **Customer:** TIQUILA
- **Plan:** May require adjustment to requirement
- **Incident Type:** Squawk
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

During TO1 STALKER FAT, connection to radio and aircraft was tested to determine the reaction time of the platform outputs to the GCS. The expected lag time was 5 seconds however after disabling encryption, the platform status output change was observed after 12 seconds

## Comments (8)

### Allen Gardner, 2023-08-24

@Craig Burton please add a task to GCSS to determine root cause, connect with @Sam Miller determine a good course of action, and create a set of corrective actions.

### Craig Burton, 2023-08-25

GCSS task https://jenaero.atlassian.net/browse/GCSS-83 has been created to track resolution during this upcoming sprint.

### Craig Burton, 2023-08-29

Reached out to Sam via email to discuss this and https://jenaero.atlassian.net/browse/VXEP-30.

### Sam Miller, 2023-09-01

Hi Craig, this was discussed at the LM Vendor PTR-B on Wednesday.  They now understand that the 12 seconds is the standard operational time required for the Silvus radio to reconfigure the network from encrypted to non-encrypted communications.  This isn’t something that can be changed.  Some operations like changing frequencies may occur much more quickly.  They are recommending closure of the PTR, pending concurrence from the UK Authority.

### Carl Denslow, 2024-05-22

@Craig Burton @Sam Miller has the appropriate UK Authority concurred on this request to close?  This particular TPTR is receiving comments and questions in the TIQ ddp.  If we can close the TPTR, then we can remove it from that document entirely as it will no longer be considered abnormal limitation.

### Craig Burton, 2024-05-23

@Carl Denslow @Sam Miller I have not heard anything from the authority on this.

### David Grosher, 2024-09-05

@Pat Wells Can you confirm this issue can be closed? There is no action to be taken per the comments.

### David Grosher, 2025-02-14

THis can’t be addressed it is inherent in the Silvus design.

## Attachments (0)
