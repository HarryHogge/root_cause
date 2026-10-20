# Prompt 01: Corpus survey and pilot

Runs in: Sandbox
Type: Exploratory. Change nothing outside `reports/` and `results/`.
Output: `reports/01_corpus_survey_and_pilot.md` and `results/01_pilot.jsonl`, committed with the message "Prompt 01: corpus survey and pilot" and pushed.

Read `CLAUDE.md`, `docs/decisions.md` and `data/vxep/manifest.json` first.

## Purpose

Before analyzing all 1,791 VXEP tickets, find out what the data can support, agree on what a result looks like, and try it on a sample. Nothing in this prompt is the final answer for any ticket.

## Part A: What is in the data

Use `data/vxep/index.jsonl`, the ticket files and the manifest. Report:

1. Tickets by issue type, by status, and by year created.
2. How many tickets have each of: a Description, a Root Cause field, a Corrective Action field, an Executive Summary, at least one comment, at least one converted attachment. How many have none of these beyond a summary line.
3. Which custom fields appear, and on how many tickets. Flag the ones that look useful for root cause (for example Components, Incident Type, Vehicle Tail Number) and any that are noise the exporter should drop.
4. Attachments: converted, listed only, failed, by kind. How many tickets have only images or only AAR packages as their evidence.
5. Anything in the exported text that looks broken: conversion junk, cut-off files, empty attachments, repeated template text the exporter missed. Give examples by file path.

## Part B: How people describe failures today

1. Read the Root Cause field across every ticket that has one. Group what people wrote into a rough list of systems and components (propulsion: motor, ESC, propeller; power: battery, fuel cell, harness; avionics; comms; GPS; airframe; software; operator; environment; and whatever else appears). Give counts and two or three example tickets for each.
2. How specific are they? Count how many Root Cause entries name only a category ("hardware", "software", "operator error"), how many name a part, and how many name a part and where it is (position, side, motor number).
3. How do people refer to positions? List the conventions you find (for example "right front", "motor 3", "M3", "starboard aft", "boom 2"), with examples. Do not pick one: Scott will.

## Part C: Proposed result format

Propose the fields one result should have. As a starting point, consider:

- `key`
- `outcome`: `determined`, `narrowed`, or `not_determined`
- `system`, `component`, `position`, `failure_mode` (each as specific as the evidence allows, or empty)
- `confidence`: `high`, `medium`, `low`, with what each means
- `evidence`: a list of `{file, quote}`, each quote short and exact
- `team_root_cause`: what the Root Cause field says, copied as written, or empty
- `agrees_with_team`: `yes`, `more_specific`, `differs`, or `no_team_answer`
- `would_settle_it`: what data would settle an open question, naming the file (for example a photo listed on the ticket, a CSV, an AAR)

Change, add or drop fields as the data suggests, and explain why.

## Part D: Pilot

1. Pick 40 tickets: 20 closed tickets that have a Root Cause field, and 20 that do not. Within each group, spread them across years and include several with converted attachments. List the keys and how you picked them.
2. Analyze each one by reading its `ticket.md` and every converted attachment. Write one JSON line per ticket to `results/01_pilot.jsonl` in the Part C format.
3. In the report, for each ticket give one line: the key, the team's root cause (if any), your result, and the confidence.
4. Summarize:
   - how many came out `determined`, `narrowed` and `not_determined`;
   - for the 20 with a team answer, how often you agreed, were more specific, or differed. For every "differs", explain the disagreement and quote the evidence on both sides;
   - which attachments made the difference (kinds and examples);
   - how many would likely be settled by images, by CSVs or by AARs, according to `would_settle_it`.
5. About how long the pilot took, and an estimate of what the full 1,791 tickets would take, with a plan for running them in batches that can resume across sessions.

## Report

`reports/01_corpus_survey_and_pilot.md`, in plain language:

- The branch and the commit the work started from.
- Parts A to D as above.
- Questions for Scott, at least:
  - which position convention to standardize on;
  - whether the proposed result format and the meaning of `determined` and `narrowed` are right;
  - anything in the data the exporter should change before the full run.
