# Prompt 02: Root cause for every incident

Runs in: Sandbox
Type: Analysis, in batches, over several sessions. Change nothing outside `reports/`, `results/` and `scripts/check_results.py`.
Output: `results/02/batch_NNN.jsonl`, `results/02_all.jsonl` and `reports/02_incident_run.md`.

Read `CLAUDE.md`, `docs/decisions.md` (both October 20 sections) and `reports/01_corpus_survey_and_pilot.md` first.

## Purpose

Work out the root cause of each of the 409 Incident (8D) tickets in `data/vxep/`, as specifically as the evidence allows, in the format agreed after report 01.

This prompt takes more than one session. Each session picks up where the last one stopped.

## What changed in the data since report 01

The export was run again after report 01, with these fixes:

- Long tickets now have all their comments, oldest first. Before, tickets with more than 20 comments were missing up to 20 of their oldest comments and repeated the newest ones (86 tickets). Eight pilot tickets were affected: VXEP-263, 512, 639, 720, 1630, 1661, 1778 and 1989.
- Jira headings inside fields and comments are written in bold, not with `#`. Every `##` and `###` line in `ticket.md` is now the exporter's own.
- Embedded files are named: `[embedded: <file name>]`, where the name matches the attachments table. `[embedded file, not matched to an attachment]` means Jira gave no way to match it.
- CSV summaries skip comment and settings lines above the header, and keep those lines as written ("Lines above the header"). They often hold the logger, serial number, firmware and settings.
- Converted emails no longer carry confidentiality or export control notices, external-sender banners, phone numbers or email addresses.
- Bookkeeping fields (Epic Color, Issue color and others) are gone.
- **New:** `data/linked/` holds the 561 tickets in other projects (VA, FS2, RMA, ENG, XKIT and others) that VXEP incidents point to, by Jira link or by key in the text. They are written the same way as VXEP tickets. `data/linked/index.jsonl` gives `referenced_by` for each.
- **Moved tickets.** 17 keys written in VXEP tickets now belong to tickets that were moved, for example VA-82, which is now VXEP-481. `data/linked/manifest.json`, under `moved`, gives each old key and the folder where the ticket is now. Nine of them moved into VXEP and are in `data/vxep/`. Look there before calling a linked ticket missing.

Check these against the data in Part A before relying on them.

## Part A: First session only

Do this only if `results/02_batches.json` does not exist yet.

1. Spot-check the fixes above on a few tickets each, for example VXEP-40 and VXEP-426 for comments, VXEP-1017 and VXEP-1290 for embeds, VXEP-1980 for the CSV, VXEP-55 for emails. Report anything that is not as described. If the comments are still duplicated or missing, stop and say so.
2. Write `results/02_batches.json`: every Incident (8D) key in `data/vxep/index.jsonl`, in key-number order, in numbered batches of 10. This list is fixed once written. Do not change it in later sessions.
3. Write `scripts/check_results.py`, the checks from report 01, D2, as a script:
   - every line parses and has every field;
   - every evidence quote is found word for word in the file it cites;
   - no em dashes;
   - each batch file has exactly one line per key in its batch.

   It reads `data/` and `results/` and writes nothing.

## Part B: Every session

1. List the batches that have no complete `results/02/batch_NNN.jsonl`. Work through them in order.
2. Analyze each ticket as in the pilot: read `ticket.md` and every converted attachment in full. In addition:
   - **Linked tickets.** When a ticket points to another ticket for its cause, investigation or repair, read that ticket too. Look in `data/vxep/` for VXEP tickets and in `data/linked/` for the rest, including their converted attachments. Cite them in `evidence` like any other file. A linked ticket that is not in the export goes in `would_settle_it` as `linked_ticket`.
   - **Several incidents on one ticket.** If one ticket covers more than one aircraft or event, give the main one and describe the others in `contributing` or `notes`.
3. Write one JSON line per ticket in the format below. Then run `scripts/check_results.py` on the batch and fix what it finds before moving on.
4. After every four batches, commit and push with the message "Prompt 02: batches NNN to NNN".
5. When a session has to stop, update the report (below) to show progress, commit and push. Reply with: "Prompt stopped: partial run, N of M batches done. Details in reports/02_incident_run.md."

## Result format

The format from report 01, Part C, which Scott accepted, with two changes for position:

- `position`: in the agreed convention, motor number plus words, for example `"motor 3 (rear right)"`. Numbering as in VXEP-272: 1 front left, 2 front right, 3 rear right, 4 rear left. For things that are not lift motors or ESCs (servos, wings, booms), use plain words: `"left aileron servo"`. Empty if the evidence does not say which one.
- `position_as_written`: the position exactly as the ticket writes it, for example `"RR"` or `"right aft"`. Empty if none.

If a ticket's wording cannot be mapped to a motor number with confidence, leave `position` as the words only and say why in `notes`. Do not guess the number. "CW" can mean center wing or clockwise (report 01, B3).

Also add:

- `linked_read`: the linked tickets read for this result, VXEP or other projects.

Meanings of `outcome` and `confidence`, and the rule for designed aborts, are as in report 01, Part C. They are settled (decisions, October 20).

## Part C: Last session, when every batch is done

1. Join the batches into `results/02_all.jsonl`, in key order, and run `scripts/check_results.py` on it.
2. Write the final report.

## Report

`reports/02_incident_run.md`, in plain language. While the run is partial, it shows progress only (items 1 and 2). When it is complete, it has all of these:

1. The branch, the commit each session started from, and the export date from `data/vxep/manifest.json`.
2. Progress: batches done, tickets done, and every ticket not done or not readable, with the reason. Part A findings, from the first session.
3. Outcomes: counts of `determined`, `narrowed`, `not_determined` and `no_fault_found`, by year and by incident type (the Incident Type field: Mission Failure/Abort, Aircraft Damage, Aircraft Loss and so on).
4. What fails: by `system`, then the most common components within each system, with counts and example tickets. Repeat failures of the same part are what Scott most needs to see. Call out any part or failure mode that appears on five or more incidents, and how many of those are `determined`.
5. Position: for propulsion results, counts by motor position, and whether any position fails more often than the others. Say how many propulsion results had no position.
6. Against the team: for incidents with a Root Cause field, counts of `yes`, `more_specific`, `differs` and `no_team_answer`. For every `differs`, one paragraph with quotes from both sides.
7. Against the pilot: for the 40 pilot tickets that are in this run, every result that changed from `results/01_pilot.jsonl`, and why. Say separately what changed on the eight tickets whose comments were incomplete in the pilot.
8. What the linked tickets added: how many results cite a ticket from `data/linked/`, and examples where it changed the result.
9. What would settle the open ones: counts by `would_settle_it` kind, as in report 01, D4. Then a list of the tickets where one named photo or plot attached to the ticket would most likely settle it, with the file name. This list is the input for the image step.
10. Problems in the data found during the run, by file path.
11. Questions for Scott, at least: whether the component names are consistent enough to group, or need the Confluence glossary step next.
