# VXEP-977: VXE 500 Fuel cell reports error of "-25568"

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2025-02-05
- **Updated:** 2026-01-06
- **Resolved:** 2026-01-06
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Craig Burton
- **Creator:** Alexander Alan Arnold
- **Labels:** Edge_Asset, Weekly-incident-tracker
- **Vehicle Tail Number:** VXE 500
- **Vehicle Configuration:** Fuel cell config, heated pitot prototype
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

EDGE ASSET
Ruysser: Before flight, during the warmup the fuel cell reported an error of "-25568". I am unaware of an error being negative. After confirming with the Ann Arbor team, it seemed to be an error indicating that the fuel cell temperature had dropped too low (this was while at idle on the ground). The AA team would like to run some tests when they can to try and replicate the issue. To clear the error, the fuel cell was stopped and restarted. After talking with Ann Arbor, it seems that it may have gone away after the fuel cell started making more power and warmed up, but that is unconfirmed.

## Corrective Action

Update to VSM to remove negative integers within the next release of VSM updates. Handled by Mission Systems IPT. 
@Craig Burton can you please link to what VSM version this will be resolved in? Is there a Jira issue you can link for it? We can then assign to Alex to verify the issue is fixed.

## Root Cause

VSM Fault Interpretation issue, Passthrough of high decimal fault values resulted in a negative reported erroneous fault message.

## Comments (8)

### Sean Wendling, 2025-02-05

@Alexander Alan Arnold Hey Alex, I see you reported this. Is this a “Highest” severity issue? If the system displayed the fault but it cleared, could it be lower priority while I work other issues? If it is high priority I can make time, but I just wanted to check.

### Alexander Alan Arnold, 2025-02-05

I just set them to highest when they first get reported. since its assigned to you I believe you should be able to determine priority. @Sean Wendling

### Sean Wendling, 2025-05-21

Hey @Pat Wells  & @Drew Hildreth , What type of report would you like for a ticket like this? I can just report findings on this item as a comment to this ticket, or PowerPoint. Because its not going to a customer, I don’t think we need the more formal reporting options. Either way just let me know! Thanks, Sean

### Drew Hildreth, 2025-05-21

@Sean Wendling I agree we don’t need a formal report on this since it is an internal asset. If you want to drop into the ticket and update the  root cause and corrective actions above I think that would be just fine.

### Sean Wendling, 2025-07-08

@Alexander Alan Arnold @Drew Hildreth Update to this ticket, Working with Mission Systems team, there was a VSM error causing values exceeding a specific fault to revert to negative numbers. It is currently being tracked and resolved on the engineering side with an estimated correction on the next GCS / VSM release. Not sure how you want to move forward with this ticket, but I would say it is closed pending that update. Thanks!

### Sean Wendling, 2025-12-30

Hey @Craig Burton, I know we were working on this back in the summer. I realized that the root issue wasn’t closed out. Just want to confirm this was fixed and inquire what software version the correction became active. Thank you!

### Craig Burton, 2025-12-30

Hi @Sean Wendling This was fixed in the VSM under [MS-725] VSM update to provide fault codes in FC messages to GCSs - Jira and recently revised under https://jenaero.atlassian.net/browse/MS-1261

### Craig Burton, 2026-01-06

I recommend closing this ticket @Alexander Alan Arnold

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [Mishap Reporting Odd FC Error.docx](attachments/25979_Mishap%20Reporting%20Odd%20FC%20Error.docx.md) | docx | 359 | 2025-02-05 | converted |
| T95_V500_250202_121303_pack.zip | archive | 6457 | 2025-02-05 | listed only |
