# Report 02: Root cause for every incident

- **Prompt:** `prompts/02_incident_run.md`
- **Branch:** `agent/wednesday`
- **Session 1 started from commit:** `cd9b67a` (Re-export VXEP with exporter fixes from report 01; add linked tickets and prompt 02)
- **Export:** `data/vxep/manifest.json` exported_at 2026-10-20 17:40 UTC (1,791 tickets); `data/linked/manifest.json` exported_at 2026-10-20 17:50 UTC
- **Status:** PARTIAL. See Progress.

## 1. Progress

<!-- PROGRESS -->
Batches done: 20 of 41 (200 of 409 tickets). Batch list: `results/02_batches.json`. Results: `results/02/batch_NNN.jsonl`. Every finished batch passes `scripts/check_results.py`.

Tickets not done or not readable: none so far, apart from the batches not yet run.
<!-- /PROGRESS -->

## 2. Part A findings (session 1)

Every fix listed in the prompt was checked against the data. All are as described, with the small exceptions below. Nothing stopped the run.

1. **Comments: fixed.** VXEP-40, VXEP-426, VXEP-282 and VXEP-101 now have as many comments as their header says (42, 84, 42 and 25), every comment different, in date order. VXEP-40's first comment is now 2022-03-25. Across all 1,791 tickets, only VXEP-1491 has two identical comments: two separate comments by the same person on 2025-08-28 that each contain only an unmatched image. That is real, not an export fault.
   - **Correction to report 01.** Report 01 (Part A, item 5) said the second copy of the comments was the complete list, so VXEP-40 had 22 real comments. That was wrong. As the prompt says, the oldest comments were missing, and VXEP-40 has 42. Pilot results on the eight affected tickets were made on incomplete comments (item 7 of the final report will cover what changed).
2. **Headings: fixed.** Every `##` line in every `ticket.md` is now one of the exporter's own sections, and every `###` line is a comment header. Nine lines in four tickets start with `#` but are ordinary text, not headings (for example `data/vxep/VXEP-880/ticket.md` "#2-> 881", `data/vxep/VXEP-652/ticket.md` "#ifdef VTED_BYTE").
3. **Embedded files: fixed, two small leftovers.** VXEP-1017 and VXEP-1290 now name their images (for example `[embedded: slightly-negative-agl.png]`). There are 1,392 named embeds and 7 `[embedded file, not matched to an attachment]` across the export. Leftovers:
   - 10 named embeds are not in their ticket's attachments table, probably images deleted from Jira after they were pasted: VXEP-272 `image-20240827-153642.png`, VXEP-426 `image-20250919-190452.png`, VXEP-944 `image-20250206-233902.png`, VXEP-1016 (2), VXEP-1880 (3 battery screenshots).
   - Email signature graphics appear as embeds on VXEP-1907 and VXEP-1967 ("Redwire", "linkedin icon", "X icon" and similar, 40 in all). Harmless noise.
4. **CSV headers: fixed.** `data/vxep/VXEP-1980/attachments/64333_2026-08-28_13-25-VH_CID-4-log.csv.md` now shows the logger lines (serial, firmware 3.1.4, running hours, settings) under "Lines above the header". `data/vxep/VXEP-1291/attachments/30067_592-elevatorBoostBoardTest.csv.md` now shows 8 columns and 32 rows.
5. **Emails: fixed.** No confidentiality or export control notices, email addresses or phone numbers remain in the 32 converted emails. Four subject lines still start "EXTERNAL:", which is part of the subject, not a banner (for example VXEP-232 `18021_FW 2-1619 .msg.md`).
6. **Bookkeeping fields: gone.** Issue color, Epic Color and Epic Status no longer appear.
7. **Linked tickets.** `data/linked/` holds 558 ticket folders, matching the 558 keys in `data/linked/index.jsonl` (RMA 157, FS2 143, VA 109, ENG 52, GCSS 31, XKIT 27, MS 11, SMUP 9, OGCS 6, BAT 5, PLD 5, AV 3, JA 2, SP 1). `data/linked/manifest.json` says 561 tickets; the difference of 3 is not explained in the manifest and should be checked on the local machine. One linked attachment failed to convert: ENG-3034 `Vehicle%20450%20incident%20report[1].pptx` (not a valid pptx).
8. **Moved tickets: as described.** `moved` lists 17 old keys. All 17 target folders exist; 9 point into `data/vxep/` (VXEP-51, 68, 130, 162, 389, 440, 480, 481, 1315).

Also written in this session: `results/02_batches.json` (409 Incident (8D) keys, key-number order, 41 batches of 10, the last of 9) and `scripts/check_results.py` (the report 01 checks, plus fixed-value fields, position wording and batch key lists).
