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
