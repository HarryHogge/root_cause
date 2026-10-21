# Decisions

Scott's decisions for root_cause, with reasons where given. Newest sections at the bottom. Claude Code must treat these as settled and must not change this file.

## October 20, 2026: scope and data

| Topic | Decision |
| --- | --- |
| Goal | Use Claude to narrow each incident's root cause from the Jira ticket and its attachments, as specifically as the evidence allows ("right front ESC", not "hardware"). Not every ticket will have the data; try anyway. |
| Who analyzes | Claude Code in the sandbox, working through numbered prompts. No AI model is called from code. |
| Jira data in GitHub | Allowed. It is already done in other repos. |
| Moving the data | The sandbox cannot reach Jira. Tickets are exported on the local machine with `scripts/export_jira.py` and committed as text under `data/`. |
| Scope | VXEP first. RMA tickets were judged low value by the team; Scott will take a second look after the VXEP results. |
| Output | Reports, for now. |
| Attachments: documents and emails | pdf, docx, pptx, xlsx, txt, md, msg, eml and similar are converted to text and committed. |
| Attachments: images | Not in the first pass. Each ticket lists its images by name and size. After the first results, shrunk copies are added only for tickets where the text points to photos or plots as the evidence. |
| Attachments: CSV | Column headers and row count only, not the data. Specific ones can be asked for later. |
| Attachments: skipped | AAR packages and other archives, and videos: listed, not downloaded. |
| Vocabulary | The first results come before any fixed component list. Scott may find a Confluence glossary; that is a step after the initial results. |

## October 20, 2026: after report 01

| Topic | Decision |
| --- | --- |
| Position convention | Motor number plus words, for example "motor 3 (rear right)". Numbering as in the log glossary on VXEP-272: 1 front left, 2 front right, 3 rear right, 4 rear left. |
| Result format | As proposed in report 01, Part C, including `event`, `tail`, `initiating_cause`, `contributing`, `team_view_in_comments`, `disagreement`, `attachments_read`, `reasoning` and `notes`. |
| `determined`, `narrowed`, `not_determined`, `no_fault_found` | Meanings as proposed in report 01, Part C. |
| Designed aborts | An abort that worked as designed because an input degraded (for example GPS quality) is scored on that input: `narrowed`, not `no_fault_found`. |
| Exporter changes | All six from report 01, question 3: the duplicated and missing comments, headings inside fields, embedded image names, CSV headers below comment lines, email notices and signature phone numbers, bookkeeping fields. |
| Scope of the full run | The 409 Incident (8D) tickets only. |
| AAR packages | A later step, after the full text run: look at what a few packages hold, then decide whether a text summary of their logs is worth exporting. |
| Linked tickets in other projects | Export only the specific tickets that VXEP incidents point to (VA, FS2, RMA, ENG, XKIT and others), not whole projects. They go in `data/linked/`. |

## October 21, 2026: after report 02

| Topic | Decision |
| --- | --- |
| Sandbox budget | The sandbox account hits session limits. Prompts are kept small, and larger steps start with a trial. |
| Images | Start with a trial of 10 tickets from report 02, section 9. Expand only if the trial shows the images change results. |
| AAR packages | Out of scope for now. AAR data lives in a separate database, and bringing it in is too large a step at present. |
| Glossary | Scott is looking for a Confluence glossary. The component grouping step waits on it. |
| HLB | HLB failures have their own investigation. For root_cause, "HLB" is an acceptable finding: do not go further into HLB cells (which cell, cell mechanism) and leave HLB tickets out of the image step. Connectors in the HLB power path (AS150) are not HLB and stay in scope. |
