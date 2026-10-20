# EC Checklist VXEP-1814.docx

Attachment 53712, docx, 36 KB, added 2026-04-15 by Christa Meck.

## Pre-CCB Checks:

https://jenaero.atlassian.net/browse/VXEP-1814

Icons:

✔ = Reviewed and all is well

✗ = This check does not apply to the Jira work item in review.

? = The reviewer has questions about this check.

✕ = The criteria for this check are NOT satisfied.  This work item is not ready for CCB.

## 1. Change Level Determination

✗All Software Changes require an SCN.  Level does not matter.

✔Determine change level (0, 1, 2, etc.).

✗If Level 0 or Level 4: no ECN required — ensure rationale for Level 0 classification is stated and documented.

✔If Level 1, 2 or 3: ECN must be initiated and linked to EC Jira work item.

✔Verify the ECN number or Jira work item is referenced in the EC and all affected drawings.

## 2. Documentation Completeness

✔Verify Completeness:

✔Jira Engineering Change work item is filled out completely (Reason for Change, Description of Change, Affected Item(s), Revisioning)

✔ECN form is filled out completely (Description of Change, Impact, Effectivity, PoC and Material Disposition).

✔Verify “Reason for Change” and “Description of Change” are clearly defined and unambiguous.

✔Confirm affected items (part number and respective parents) are included and properly referenced.  Was the correct configuration referenced on the Jira work item?

✔Verify part numbers queued for production release on Jira match those in Vault.

✔Confirm the drawing changes have an approver.  When drawings are updated, the approver should be an Engineer.

## 3. Technical and Configuration Review

✔Evaluate whether the change affects form, fit, or function (FFF).

NOTE:  If this is a preprod part that has not yet been ordered or is in production, we do NOT need to update the part number.

✗If FFF impacted, ensure a new part number has been generated.

✔If FFF not impacted, confirm revision only is appropriate.

✔Check with Jira work item Reporter and/or Assignee to see if interface has been updated and/or if interchangeability with other assemblies has been impacted by this change.

✔Confirm the revision block accurately states what changed and references the ECN number or Jira work item.

✔Validate Vault Data Card information matches Jira Engineering Change and ECN (if applicable).

✔Confirm drawing is in one of the PENDING CCB statuses.

✔Sanity check the vault folder location (no bolts stored in 400 – Electrical, etc)

## 4. Effectivity and Timing

✗Check if a CCN (Configuration Change Notice) or CR (Change Request) is required — if not, confirm justification is documented.

✔If the work item has an ECN:

✔Verify Effectivity Date on ECN matches planned implementation

✔Sanity check dispositioning vs quantities/cost/etc.

✔Ensure “Effectivity Values” on ECN clearly identify which units, aircraft serial numbers, or builds are affected.

✔Validate that production and supply chain are aware of effectivity timing.

## 5. Impact and Traceability Review

✔Run Where-Used Report in Solidworks and Odoo for affected PN(s) to  all Next Higher Assemblies (NHA).

✔List all programs / aircraft builds impacted.  See if this page can be used as a resource to answer this question while we wait for this information to be moved into Odoo.  https://jenaero.sharepoint.com/sites/JAI_Operations/Lists/Production%20Orders%20List/All%20Columns%20Including%20Shipped.aspx?viewid=29258d4b%2D3164%2D4323%2D8066%2Dbf27d76115a5

✔Review for system-level impacts (wiring diagrams, schematics, manuals, test plans).

✔Confirm no duplicate or conflicting ECNs exist for same PN/revision.

✔Validate supersession logic if this EC replaces prior ECs.

## 6. Quality and Compliance Check

✔Confirm no open deviations or temporary rework authorizations are in place for this PN.

## 7. Pre-CCB Readiness

✔EC and ECN have passed peer/engineering review and are ready for CM review.

✔No missing information remains; ECN is ready for formal CCB evaluation.

✔CM reviewer has verified that change package is CCB-ready and can be included in the next agenda.

## When CCB Starts:

Do we have attendance quorum https://jenaero.atlassian.net/wiki/spaces/CM1/pages/1060077578/How+To+Take+Attendance+for+the+CCB+Meeting

## Post-CCB:

Verify Vault “Released Revision” and EGG version control reflect same revision.

If applicable, ensure affected specifications or work instructions revisions are planned.
