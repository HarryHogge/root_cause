# VA-445: 371 mis-configured -Record procedure used to land aircraft flying with wrong DTED.

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-09-05
- **Updated:** 2023-11-09
- **Resolved:** 2023-09-13
- **Reporter:** Cameron Chapman
- **Assignee:** Artis Bertulis
- **Creator:** Cameron Chapman
- **Links:** relates to VXEP-45 (371 mis-configured (ready for flight then DTED loaded))

## Description

Please reassign if someone else could better perform this task.

## Comments (2)

### Artis Bertulis, 2023-09-11

@Cameron Chapman do we really think this needs to be documented? The scenario is highly unlikely. All customer GCSs already have all DTED uploaded on them, the fact that this one didn’t have the DTED is weird.
I’m not opposed to adding info, but I’m not sure we should be documenting all corner cases. We could add a warning in DTED section to say something like “If new DTED is uploaded, restart the GCS software before performing a flight”.

### Cameron Chapman, 2023-09-11

I trust your judgement on how possible a reoccurrence is, and if updating manuals would help.  
For the sake of record keeping, the information in this ticket counts as recording what happened and how you fixed it. https://jenaero.atlassian.net/browse/VA-439 
It sounds like the best prevention for re-occurence will be done here https://jenaero.atlassian.net/browse/GCSS-99 
I think you can close this task if you agree

## Attachments (0)
