# Report 01: Corpus survey and pilot

- **Prompt:** `prompts/01_corpus_survey_and_pilot.md`
- **Branch:** `agent/wednesday`
- **Started from commit:** `7626ce1` (Export VXEP tickets; add working rules, decisions and prompt 01)
- **Data:** `data/vxep/`, exported 2026-10-20 15:50 UTC, 1,791 tickets (`data/vxep/manifest.json`)
- **Outputs:** this report and `results/01_pilot.jsonl` (40 lines)
- **Completeness:** all 1,791 `ticket.md` files were parsed for Part A. All 216 Root Cause entries were read for Part B. All 40 pilot tickets and every converted attachment on them were read for Part D. Nothing was skipped. No file under `data/` was changed.

Nothing here is the final answer for any ticket. The results in `results/01_pilot.jsonl` are a trial of the method and the format.

---

## Summary

1. **Only about a quarter of the 1,791 tickets are incidents.** There are 409 "Incident (8D)" tickets. The rest are tasks, sub-tasks, epics, projects, design reviews and BOM/drawing requests. The full run should cover the 409 incidents, not all 1,791 (question 4).
2. **The team has already written a root cause on 216 tickets**, almost all of them incidents (215 of 409). About 62% name a part, a board, a specific bug or a specific operator action. 20% name only a category, such as "software" or "operator error". Only 7% say *which* unit failed (for example motor position, side or pin).
3. **The pilot reached a specific component on 11 of 40 tickets and narrowed 26 more.** Where the team had an answer, I agreed 13 times, was more specific 4 times and differed once (VXEP-1524). On that one the engineer's own comment rules out the Root Cause field.
4. **The evidence that would settle most open tickets is the AAR log packages.** They are listed but not exported. The AAR packages were the deciding missing item on 24 of the 29 tickets the pilot left open. Photos and plots come second (16 tickets). CSVs mattered on only 1.
5. **The exporter has one real bug to fix before the full run.** On every ticket with more than 20 comments, the comments are written twice (86 tickets, 898 extra comments). Details are in Part A, item 5.

---

## Part A: What is in the data

### A1. Tickets by issue type, status and year

**By issue type** (1,791 total)

| Issue type | Tickets | | Issue type | Tickets |
| --- | --- | --- | --- | --- |
| Incident (8D) | 409 | | Corrective Action | 38 |
| Task | 394 | | Improvement | 37 |
| Sub-task | 278 | | Engineering Change | 29 |
| Epic | 202 | | Initiative | 28 |
| Major Project | 163 | | Story | 16 |
| Problem | 101 | | Bug | 15 |
| Design Review | 66 | | Minor Project | 15 |

"Problem" tickets are mostly production and drawing issues (for example VXEP-110 "Outdated PN in BOM", VXEP-158 "GCS Power Adapter, HS Diameter Too Large"), not flight failures.

**By status** (top entries): DONE 593, Canceled 561, D8 - Closed 235, New 216, D8 - Closed, but added to Bermuda Triangle List 39, D4 - Investigating Root Cause 33, In Process 31, On Hold 15, D2 - Gathering Information 13, To Do 12. There are 11 smaller statuses with 9 or fewer tickets each.

**By year created:**

| Year | All tickets | Incident (8D) |
| --- | --- | --- |
| 2022 | 50 | 0 |
| 2023 | 230 | 54 |
| 2024 | 469 | 104 |
| 2025 | 709 | 140 |
| 2026 | 333 | 111 |

Incident (8D) status: D8 - Closed 235, Canceled 63, Bermuda Triangle 39, D4 33, D2 13, New 11, D6 12, other 3.

### A2. Which tickets have which kinds of content

A note on how the exporter writes fields. A short field value goes in the bullet list at the top of `ticket.md` (`- **Root Cause:** ...`). A long or multi-line value becomes its own `## Root Cause` section. Root Cause, Corrective Action and Executive Summary each appear both ways, never both on one ticket. Any reader has to check both places. The counts below do.

| Content | All tickets (1,791) | Incident (8D) (409) |
| --- | --- | --- |
| Description | 1,109 | 403 |
| Root Cause field | 216 | 215 |
| Corrective Action field | 189 | 186 |
| Executive Summary | 71 | 71 |
| At least one comment | 1,009 | 394 |
| At least one converted attachment | 215 | 115 |
| None of the above (summary line only) | 489 | 0 |

Every incident ticket has at least a description or a comment. The 489 tickets with nothing beyond a summary are all non-incident types (for example VXEP-59, VXEP-92, VXEP-114, VXEP-123).

### A3. Custom fields

**Look useful for root cause** (count = tickets with a value):

| Field | All | Incidents | Comment |
| --- | --- | --- | --- |
| Severity | 406 | 386 | Clean 4-level scale (1 Flight Critical 161, 2 Degraded No Workaround 126, 3 With Workaround 89, 4 Annoyance 30) |
| Vehicle Tail Number | 326 | 309 | Useful but written many ways: "674", "VXE-622", "VXE 500", "522 & 529" |
| Customer | 321 | 304 | Useful for grouping; some values are lists ("25thID, LRR") |
| Incident Type | 244 | 240 | Mission Failure/Abort 83, Aircraft Damage 63, Aircraft Loss 28, Near Miss 26, Squawk 24, Other 20 |
| Vehicle Configuration | 170 | 166 | Free text, many spellings of the same thing ("VXE30", "VXE-30", "VXE 30 standard battery configuration") |
| Labels | 544 | 327 | Mixed: Crash, Hardware, Software, RCCA, customer names, Weekly-incident-tracker |
| Problem Type | 116 | | Mostly "Other" or "Discovered Issue" |
| Part Number(s) | 79 | 13 | Useful where filled, rarely filled on incidents |
| Components (EA Aircraft) | 55 | 44 | Weak: 31 of 55 say only "Aircraft, full assembly" |
| Impacted Core Subsystems | 25 | | Too coarse ("Aircraft", "Ground Systems") |
| Issue Status | 133 | | Free text progress notes, sometimes holds the real conclusion (for example VXEP-897) |

**Noise the exporter could drop:** Issue color (440), Epic Color (202, values like "ghx-label-7"), Epic Status (202), Epic Name (18), Current Sprint Priority (21), Story Points, Team, Company Priority, "Is this ticket a Design Project?" (48). The four tickets with a "Cause" field all hold the same sentence ("Need for better understanding of harshest conditions applied while deployed or stored..."), which is template text.

### A4. Attachments

From `manifest.json`: 540 converted, 4 converted but cut, 3 with no text found, 2 failed, 2,776 listed only.

| Kind | Converted | Listed only | Other result |
| --- | --- | --- | --- |
| image | | 1,931 | |
| archive (zip, gz; mostly AAR packages) | | 652 | |
| pdf | 171 | | 4 cut, 1 failed |
| csv (headers and row count only) | 150 | | |
| video | | 105 | |
| other (.t00, .vmis, .bin, .hex, .step, .pcapng ...) | | 88 | |
| text (.txt, .log, .json) | 85 | | |
| docx | 41 | | 1 no text |
| xlsx | 36 | | |
| pptx | 33 | | 1 failed |
| msg / eml | 24 | | |
| html | | | 2 no text |

On the 409 incidents: 335 have at least one attachment. 280 have an archive (623 zips, nearly all AAR packages), 259 have images and 16 have CSVs. **204 incidents have attachments but nothing converted.** All their attachments are images, archives or videos. 24 incidents have only images and 36 have only archives. Across all ticket types, 181 tickets have only images and 40 have only archives.

Failures: VXEP-99 `VIT2-448_VXE-482_Investigation[1].pptx` (not a valid pptx) and VXEP-706 `2118266[B].pdf` (damaged pdf). Cut: three standards documents on VXEP-183 (AC 21-99, AS50881) and a connector datasheet on VXEP-382, none of them incident evidence. No text: `timeline_722.html` and `visualization_722.html` on VXEP-1221 (these are plots, so the evidence is lost) and `672 arching (2).docx` on VXEP-1801.

### A5. Problems in the exported text

1. **Duplicated comments (exporter bug).** On every ticket with more than 20 comments, the comment list is written twice. The first copy is the newest 20 comments; the second is the complete list. Examples: `data/vxep/VXEP-40/ticket.md` says "Comments (42)" but has 22 real comments; `data/vxep/VXEP-282/ticket.md` is the same; `data/vxep/VXEP-426/ticket.md` is the worst (26 repeats). 86 tickets, 898 extra comments. Cause: in `scripts/export_jira.py`, `all_comments()` keeps the comments the search returned (the newest 20) and then fetches more starting at number 20. The second fetch came back as the full list, which was appended to the first. The fix is to discard the search's comments whenever there are more to fetch, and fetch the whole list from the start. This also puts the comments back in date order: today the first two comments of each long ticket appear after comment 22.
2. **Headings inside field text.** The exporter turns Jira headings into `#`, `##`, `###` lines. Inside a description or comment, these look the same as the ticket's own section and comment headers. 47 tickets have 148 such lines (for example `data/vxep/VXEP-1138/ticket.md` "#### 1. Investigate Root Cause of GPS Timestamp Issue"; `data/vxep/VXEP-1053/ticket.md` "## MOVED TO VA-2507"). A heading in a comment that starts with `###` cannot be told apart from a new comment. Suggest writing Jira headings as bold text, or indenting field bodies.
3. **Unnamed embedded images.** 1,323 `[embedded ...]` placeholders on 416 tickets. 902 name the file, but 421 just say `[embedded file]`, so a reader cannot tell which listed image was meant (for example `data/vxep/VXEP-1017/ticket.md`, in a comment from 2024-06-28, and the Root Cause field of `data/vxep/VXEP-1290/ticket.md`). If Jira gives the media id, writing the filename would help the image step later.
4. **Empty or near-empty conversions.** 26 converted attachments have under 200 characters of text. Most are scanned drawings ("no text on this page; probably an image or scan"), for example `data/vxep/VXEP-1048/attachments/27637_2121367-01.pdf.md` and `data/vxep/VXEP-910/attachments/25597_Stalker Loss of Link 26 Sep (3)(562).pdf.md`. The second one is a loss-of-link report and is real evidence. Others: `data/vxep/VXEP-1630/attachments/36681_Vt00027.docx.md` (title only), `data/vxep/VXEP-540/attachments/25312_proposedChange 114-106509.xlsx.md` (empty).
5. **CSV header detection.** `data/vxep/VXEP-1980/attachments/64333_2026-08-28_13-25-VH_CID-4-log.csv.md` reports one column named "# Hargrave Technologies Logs" because the file starts with a comment line. `data/vxep/VXEP-1291/attachments/30067_592-elevatorBoostBoardTest.csv.md` reports 0 columns. Skipping leading `#` lines before reading the header would fix both.
6. **Email boilerplate.** Converted emails carry the same confidentiality notice (13 tickets), export control notice (12) and signature blocks (5+). For example, `data/vxep/VXEP-55` and `data/vxep/VXEP-187` attachments. The signature blocks include a named employee's phone number and email address. The boilerplate filter works only on Jira fields, not on attachment text, so it missed these.
7. **Repeated text that is real.** "Operator attempted to connect with the aircraft and was unable to do so. Unknown if further troubleshooting was conducted due to lack of information." appears on 11 tickets (VXEP-1830 to VXEP-1834 and others). These look like batch-created tickets, not template text, so they should stay. Jira housekeeping comments ("Removed parent to prep for Incident hierarchy change", 6 tickets; "Closing this incident as it's from August 2023...", 4 tickets) are harmless.
8. **Garbled text.** Only one attachment had a notable number of unreadable characters: `data/vxep/VXEP-98/attachments/16871_Stalker XE25 Quicksheets Rev B_2021.05.06.pdf.md` (21). A pilot agent also found the text of the VXEP-263 risk assessment PDF jumbled in places, though still readable.
9. **Root Cause field misused.** Some Root Cause fields hold something other than a cause. On VXEP-720 it is the ticket's own Jira link title. On VXEP-275 it is interim operator guidance. On VXEP-11, 429, 1890 and 1956 it only points to another ticket. These need handling in the analysis, not the exporter.

---

## Part B: How people describe failures today

All 216 Root Cause entries were read. Each was given a primary system (where the failure started, by my reading), plus any other systems it mentions. This grouping is mine, not the team's.

### B1. Systems and components named

| System | Primary | Mentioned at all | Examples |
| --- | --- | --- | --- |
| Vehicle software and firmware (AP, XCOMM, watchdog, ESC firmware) | 30 | 38 | VXEP-146 (land immediately during abort leaves AP in attitude-only mode), VXEP-514 (Config Manager memory corruption), VXEP-1775 (XCOMM WDT, stale FWAP data) |
| Avionics hardware (FWAP, VTOL AP, XCOMM, MCM, SD card, CAN, sense boards) | 20 | 22 | VXEP-46 (capacitor C20, XCOM PCB), VXEP-236 (XCOM SD card corruption), VXEP-1608 (LEMB damaging CAN transceivers) |
| Sensors and air data (pitot, baro, LRF, magnetometer, IMU, gyro) | 20 | 23 | VXEP-292 (pitot calibration), VXEP-1302 (Garmin Lidar-Lite lens), VXEP-1484 (barometer, R97 to R99) |
| Operator and procedure (including outdated firmware, ADs not applied) | 19 | 33 | VXEP-512, VXEP-651 (transition to VTOL at altitude), VXEP-605 (firmware not up to date) |
| Ground software (GCS, OGCS, VSM) | 18 | 20 | VXEP-546 (MSL waypoint bug), VXEP-1473 (OGCS server crash), VXEP-1797 (gcs.ini LandOnError) |
| Propulsion (lift motor, ESC, rotor) | 16 | 17 | VXEP-384 (position 3 ESC soft-start), VXEP-811 (RF ESC), VXEP-900 (motor 4 bearing missing) |
| No answer (unknown, pending, points to another ticket) | 15 | 15 | VXEP-43 "Unknown", VXEP-1458 "Under Investigation", VXEP-429 "See VXEP-514" |
| Power connectors and contacts (AS150, battery mate) | 13 | 17 | VXEP-12, VXEP-101, VXEP-415 (AS150 contact resistance 435 uOhm) |
| Environment (wind, icing, interference) | 11 | 17 | VXEP-17 (winds 20 to 25 mph), VXEP-381 (snow in pitot), VXEP-1864 |
| Fuel cell | 10 | 12 | VXEP-306 (PCA0120 board short), VXEP-780 (reversed mass flow meter), VXEP-1948 |
| GPS / GNSS | 9 | 11 | VXEP-412 and VXEP-427 (reduced u-blox rate), VXEP-527 |
| No fault found / behaved as designed | 9 | 9 | VXEP-529, VXEP-1566, VXEP-1592 |
| Batteries (HLB cells, main battery, charge reading) | 9 | 11 | VXEP-1407, VXEP-1435, VXEP-1449 (HLB cell electrolyte loss) |
| Manufacturing, quality, supplier | 4 | 13 | VXEP-15 (conformal coating), VXEP-162 (XT-90 supplier), VXEP-258 (ODU potting) |
| Harness and wiring | 3 | 7 | VXEP-1314 (main system harness not mated), VXEP-999, VXEP-232 |
| Ground equipment (chargers, adapters, checkers) | 3 | 3 | VXEP-23, VXEP-27, VXEP-748 |
| Radio link | 3 | 4 | VXEP-1057, VXEP-1179, VXEP-1800 |
| Airframe and structure | 2 | 3 | VXEP-21 (glue in spar), VXEP-548 (wing bracket holes) |
| Payload (E140, gimbal) | 2 | 5 | VXEP-813, VXEP-1034 |

Patterns worth knowing:
- **AS150 power contacts** are the single most repeated hardware cause (VXEP-12, 13, 101, 231, 305, 415, 646, 761, 985, 1278, and systemic VXEP-628).
- **Lift ESC soft-start MOSFETs** recur on the propulsion side (VXEP-51, 272, 384, 628).
- **HLB cell dropout** clusters in 2025 and 2026 (VXEP-1407, 1435, 1485, 1974, systemic VXEP-1449).
- **Watchdog resets** on XCOMM or VTOL AP (VXEP-230, 1548, 1775, 1780, 1904) and **GPS rate or quality** (VXEP-412, 427, 453, 1066) are the common software and navigation themes.

### B2. How specific the entries are

| Level | Entries | Share |
| --- | --- | --- |
| No answer (unknown, pending, no fault, points elsewhere) | 22 | 10% |
| Category only ("software issue", "operator error", "winds out of limits") | 44 | 20% |
| Names a part, board, specific bug or specific action | 134 | 62% |
| Names a part and where it is (motor position, side, pin, reference designator) | 16 | 7% |

The 16 at the most specific level: VXEP-46, 51, 99, 160, 199, 232, 272, 306, 384, 791, 811, 900, 1484, 1654, 1933, 1948. Of these, 9 give a physical position on the aircraft (front left, left aft, RR, RF, position 3, motor 4, right wing, left servo). The rest give a reference designator or pin number on a board.

Category-only examples: VXEP-1047 "Believed to be software related", VXEP-2006 "Operator Error", VXEP-1774 "SW issues in 6.6.1 will be addressed in 6.7.1".

### B3. How people refer to positions

Searched across every ticket and converted attachment. Counts are matches, with the number of tickets in brackets.

| Convention | Matches | Examples |
| --- | --- | --- |
| Side then end: "left aft", "right forward", "right rear", "left front" | 191 (26) | VXEP-118 "Right aft prop strike"; VXEP-1464 "right rear lift motor" |
| End then side: "rear left", "front right", "aft left", "forward right" | 77 (24) | VXEP-140 "Rear left lift motor ESC fried"; VXEP-1293 "Forward Right (FR) motor" |
| Number: "motor 3", "motor #3", "ESC 4", "position 3" | 135 (11) | VXEP-384 "position 3 VTOL ESC"; VXEP-1630 "Motor/ESC position 1, Left Front" |
| Two-letter code: RR, RF, LF, FL, FR | 22 (13) | VXEP-791 "RR motor/ESC failure"; VXEP-811 "RF ESC"; VXEP-103 "The LF and RF motors" |
| M1 to M4 | 37 (11) | VXEP-1903 report "M1=45%, M2=17%" (most other M3/M4 hits are screw sizes) |
| Boom: "left boom", "right boom", "boom 1" | 32 (16) | VXEP-1802 "Testing performed on Right Boom"; VXEP-1478 "Left Boom and Tail Boom" |
| Pairs: "forward 2 motors", "aft 2" | 5 (3) | VXEP-101 "the forward 2 motors stop followed by the aft 2 motors" |
| Starboard / port | 2 (1) | VXEP-1802 (customer report, "Stbd side") |

The motor numbers line up with the log glossary quoted in `data/vxep/VXEP-272/ticket.md`: "vtThr1 ... motor 1 (front left)", "motor 2 (front right)", "motor 3 (rear right)", "motor 4 (rear left)". Engineers use the same numbering in VXEP-1464 ("motor 3 (right rear)"), VXEP-900 and VXEP-1980 ("Motor 4 (Rear Left)") and VXEP-1630 ("position 1, Left Front"). No ticket I read contradicts it.

One trap: **"CW" means both center wing and clockwise.** VXEP-1630 says "Left Front, CW S# C-S110569", meaning a clockwise motor. Elsewhere "CW" almost always means center wing (VXEP-101 "488CW", VXEP-1294 "Connection to CW appears lost").

I have not picked a convention. That is question 1.

---

## Part C: Proposed result format

The pilot used the format below. Every pilot line in `results/01_pilot.jsonl` follows it.

| Field | Meaning | Change from the prompt's starting point |
| --- | --- | --- |
| `key` | Ticket key | as proposed |
| `event` | One sentence on what happened | **added**: a result is hard to read without it |
| `tail` | Tail number(s), digits only, e.g. "487+488CW" | **added**: the Jira field is missing or inconsistent on many tickets |
| `outcome` | `determined`, `narrowed`, `not_determined`, `no_fault_found` | **added `no_fault_found`** (see below) |
| `system` | One of 17 provisional systems (the Part B list), where the failure started | as proposed, with a fixed list |
| `component` | As specific as the evidence allows, with part number or reference designator if given | as proposed |
| `position` | Which of several identical units, **written as the ticket writes it** | as proposed; normal form waits for question 1 |
| `failure_mode` | How it failed | as proposed |
| `initiating_cause` | Why it failed: design, manufacturing_quality, maintenance_or_assembly, operator_action, outdated_software_or_ads_not_applied, environment, wear_or_age, unknown | **added**: separates "what broke" from "why"; the team's fields mix the two |
| `contributing` | Other factors the evidence supports | **added**: many incidents are chains (VXEP-512, VXEP-1221) |
| `confidence` | `high`, `medium`, `low` (below) | as proposed |
| `evidence` | List of `{file, quote}`, each quote exact | as proposed; every quote was checked by machine against its file |
| `team_root_cause` | Root Cause field, copied as written (first 600 characters) | as proposed |
| `team_view_in_comments` | Exact quote when engineers state a conclusion in comments but the field is empty | **added**: keeps the team's words separate from mine on the 20 tickets with no field |
| `agrees_with_team` | `yes`, `more_specific`, `differs`, `no_team_answer` | as proposed |
| `disagreement` | For `differs`: why, with quotes from both sides | **added** |
| `would_settle_it` | List of `{file, kind, what}`; kind is image, csv, aar_or_archive, video, other_attachment, linked_ticket, external_document, physical_inspection | as proposed, with a `kind` so it can be counted |
| `attachments_read` | Converted attachments read | **added**: shows the reading was complete |
| `reasoning` | Two to four sentences from evidence to result | **added** |
| `notes` | Export problems seen, review changes | **added** |

**Proposed meanings** (question 2):

- **determined**: a specific component or specific mechanism is supported by direct evidence: a measurement, a teardown finding, a swap test, or a log channel that names it. Example: VXEP-1630, where swapping flight profiles between positions showed the fault followed the motor/ESC in position 1.
- **narrowed**: the evidence gets to one system, or a short list of candidates, but not to one part. Example: VXEP-1294, where everything on the center wing dropped out at once, but the ESC, battery, connector and XCOMM were never separated.
- **not_determined**: the evidence does not get past the symptom. Example: VXEP-30.
- **no_fault_found**: the report was unfounded, or the system behaved normally under normal inputs.

**A rule I applied at review, which needs your agreement.** Some aircraft abort as designed because an input degraded, such as GPS signal quality dropping below the abort threshold. In those cases I score the result on the degraded input, not on the abort. The abort working as designed does not make it `no_fault_found`. So VXEP-102, VXEP-451 and VXEP-527 were changed to `narrowed` (system `gps`): the GPS drop is shown, its cause is not. The agents had scored these three differently (one determined, two no_fault_found), which is why I brought them under one rule. Each line's `notes` records the change.

**Confidence:**

- **high**: direct evidence for the named part and nothing in the ticket contradicts it.
- **medium**: points to it by inference, or one credible alternative remains.
- **low**: best reading among several, or thin evidence.

**Fields I considered and left out:** a normalized position (waits on question 1), and a component vocabulary code (your decision, after the Confluence glossary).

---

## Part D: Pilot

### D1. How the 40 tickets were picked

- **Group A, with a team answer (20).** The pool was the 173 tickets that have a Root Cause field and a closed status (D8 - Closed, D8 Bermuda Triangle, or DONE).
- **Group B, without a team answer (20).** The pool was the 150 Incident (8D) tickets with no Root Cause field, a description, and a status other than Canceled. I first included "Problem" tickets, but they turned out to be BOM and drawing requests (VXEP-110, VXEP-190, VXEP-210), not failures, so I limited this group to incidents. Group B is not limited to closed tickets: it includes VXEP-1989, which is still in D2.
- **Spread.** Five tickets per year, 2023 to 2026, in each group. In each year, 2 tickets with converted attachments where possible and 3 without. The pick was random with a fixed seed (20261020) so it can be repeated. The 2023 pool for group B had only 6 tickets.

Group A: VXEP-102, 10, 27, 231, 7 (2023); 451, 512, 720, 723, 527 (2024); 1524, 1221, 1294, 1179, 897 (2025); 1906, 1778, 1800, 2006, 1948 (2026).

Group B: VXEP-149, 30, 39, 26, 35 (2023); 263, 790, 844, 639, 283 (2024); 1398, 1630, 1218, 1452, 1461 (2025); 1845, 1944, 1661, 1926, 1989 (2026).

15 of the 40 have converted attachments (38 attachment files read in total).

### D2. Method

Each ticket's `ticket.md` and every converted attachment were read in full. The analysis was split across four parallel Claude Code sub-agents, ten tickets each, all working to one written brief. I then checked every result:
- every line parses and has every field;
- every evidence quote was found word for word in the file it cites;
- there are no em dashes;
- I read each result's reasoning against the team's text.

Two limits:
- The VXEP-1524 and VXEP-1221 logs are large (up to 0.5 MB each). They were read with repeated TRACE, joystick and version lines filtered out, not line by line.
- The VXEP-1524 logs cannot be tied to the incident date, because the ticket never gives one.

### D3. One line per ticket

**Group A: tickets with a team Root Cause** (team text cut to fit; full text in the results file)

| Key | Team root cause (as written) | My result | Outcome | Confidence | vs team |
| --- | --- | --- | --- | --- | --- |
| VXEP-102 | Loss of GPS signal near transition altitude, system aborted launch per standard. | gps: GPS receiver signal quality (GPS Status Byte 0x2E, SNR) | narrowed | medium | more_specific |
| VXEP-10 | Quality issue. Excessive solder balls, F.O.D. and potential corrosion was found on the component side of the magacc2... | avionics_hw: MAGACC2 board (1710P01A) in the fixed wing autopilot, under the RF shield can | determined | high | more_specific |
| VXEP-27 | Because the Dell adapters were delayed, we ordered a couple from eBay. Unfortunately those turned out to be an older... | ground_equipment: Dell laptop power adapter (older model bought on eBay) used with SGCS1 Lind DC-DC converter and SGCS2 Lind PoE injector | determined | high | yes |
| VXEP-231 | Failure between VTOL battery and VTOL system (proven by large delta between BMS and VTOL measured voltage). Likely du... | power_connector: HLB to VTOL system power connection (AS150 contacts at the center wing) | narrowed | medium | yes |
| VXEP-7 | Engineering did not implement full scope of the guidance provided by LMUK | ground_software: SGCS1 laptop Windows hardening build image (UK MoD Hardening Mod Kit) | determined | high | yes |
| VXEP-451 | No Issue. The vehicle landed at the current location because GPS was lost and position control was no longer possible. | gps: GPS position solution (loss of GPS fix during landing sequence) | narrowed | medium | yes |
| VXEP-512 | Closed: Operator error @David Grosher this doesn’t seem like a total root cause. Yes, the operator should not have ex... | operator_procedure: GoTo IP4 command issued instead of RTB (skipped IP2 descending orbit) | determined | high | more_specific |
| VXEP-720 | [VXEP-720] VXE 490 main battery percentage reporting incorrectly during flight with MB's (S/N's 1967 and 1737) - Jira | ground_equipment: FSK battery checker SoC model (wrong chemistry for Amicell main battery) | narrowed | low | no_team_answer |
| VXEP-723 | SLA Breakout 128-117156-01 Rev B has the Over Voltage Protection pin of both E-Fuses set to ~35V. When plugging in th... | avionics_hw: SLA Breakout Board 128-117156-01 Rev B, E-Fuse feeding the MCM (over-voltage protection about 34.9 V) | determined | medium | yes |
| VXEP-527 | Degradation of GPS below threshold caused launch abort, per design. Likely cause is the listed extra equipment, some... | gps: GPS signal quality (CN0) during VTOL climb; customer-added HackRF One, Raspberry Pi and GPS antenna puck suspected | narrowed | medium | yes |
| VXEP-1524 | Possible: GetTickCount() rollover after 49.7 days system uptime causing map tool continuous timeout. | ground_software: GCS map tool handling for the Go To Waypoint command | not_determined | low | differs |
| VXEP-1221 | Operator Error - Commanded Vehicle to VTOL at altitude. v6.4 will have an interlock warning to help prevent this from... | vehicle_software: VTOL autopilot landing state machine (a second land immediately request while the lift system is active) | determined | medium | yes |
| VXEP-1294 | Connection to CW appears lost. Need more updates | (no single system): center wing power or network; VTOL AP, air data board, SA camera and HLB BMS data all lost at once | narrowed | low | yes |
| VXEP-1179 | Dropped Radio Link, possibly misconfigured radios | radio_link: GCS to aircraft command link during VTOL launch (radio configuration suspected, not shown) | narrowed | medium | yes |
| VXEP-897 | Fixed wing magnetometer interference due to E140ZG2 payload caused disagreement between FW and VTOL APs leading to la... | payload: E140ZG2 gimbal payload suspected of disturbing the fixed wing autopilot magnetometer | narrowed | low | yes |
| VXEP-1906 | exceeded GPS threshold on launch | gps: GNSS position solution (accuracy threshold exceeded during launch) | narrowed | medium | yes |
| VXEP-1778 | Cannot Reproduce | power_connector: main battery AS150 connector mating (leading candidate among main battery, battery internal fault and XCOMM microcontroller) | narrowed | low | no_team_answer |
| VXEP-1800 | Silvus was being stepped on due to freq in area | radio_link: Silvus datalink radio (operating frequency) | narrowed | low | yes |
| VXEP-2006 | Operator Error | operator_procedure: landing pattern definition and manual nudge during VTOL descent | narrowed | low | more_specific |
| VXEP-1948 | 508 suffered a sudden internal short. The weld between the chimney and heat exchanger failed, either from vibration o... | fuel_cell: SOFC heat exchanger chimney to flame extender weld, fuel cell 508 | determined | high | yes |

**Group B: tickets without a team Root Cause**

| Key | My result | Outcome | Confidence |
| --- | --- | --- | --- |
| VXEP-149 | power_connector: main battery AS150 anti-spark connector on the aft Fuselage Power Harness (107-102189-1) | narrowed | low |
| VXEP-30 | GCS user interface freeze, neither software nor laptop hardware singled out | not_determined | low |
| VXEP-39 | airframe: fuselage top cutout edge at the lift battery opening (hand strikes it when the connector breaks loose) | determined | medium |
| VXEP-26 | ground_software: GCS D450+ Fuel Cell Control dialog Fan RPM gauge (RPM exceeds gauge limit) | narrowed | medium |
| VXEP-35 | ground_software: SGCS1 laptop Windows user account names created without the kit number | determined | high |
| VXEP-263 | vehicle_software: VTOL AP magnetometer data path (high CPU load, suspected FPU context not saved) | narrowed | medium |
| VXEP-790 | ground_software: VXE SUAV GCS hang during mission sync (mission FTP upload) | narrowed | low |
| VXEP-844 | vehicle_software: VTOL AP firmware v1.55.03 (watchdog reset, simple_tlb_refill_exception) | narrowed | low |
| VXEP-639 | battery: HLB, or the center wing HLB voltage reference / ground isolation circuit | narrowed | low |
| VXEP-283 | propulsion: VTOL lift power failure (cause tracked in VXEP-282), plus VTOL AP abort mode logic | narrowed | low |
| VXEP-1398 | battery: hybrid lift battery (HLB) 2-3490 from Kit 124 (cell imbalance) | narrowed | medium |
| VXEP-1630 | propulsion: lift motor/ESC assembly S/N C-S110569, position 1 (left front) | determined | medium |
| VXEP-1218 | ground_software: VXE SUAV GCS 6.4 window focus handling during mission sync and simulation | narrowed | medium |
| VXEP-1452 | harness: new E140 regulated payload harness, Ethernet path (missing Ethernet magnetics suspected) | narrowed | low |
| VXEP-1461 | avionics_hw: MCM eamcm0881 resetting (incorrect partitioning configuration suspected) | narrowed | low |
| VXEP-1845 | right aft lift motor did not start on a HIL SIM rig; logs never analyzed | not_determined | low |
| VXEP-1944 | operator_procedure: mission plan PLZ set about 10 km away, lost comms set to RTB | determined | medium |
| VXEP-1661 | avionics_hw: fixed wing autopilot (FWAP) in the 674 avionics box (fault follows the box) | narrowed | medium |
| VXEP-1926 | payload: Epsilon E140Z G2 gimbal firmware before 4.0.1.4 | narrowed | medium |
| VXEP-1989 | sensors_air_data: airspeed measurement feeding fixed wing landed detection | narrowed | low |

### D4. Summary

**Outcomes**

| | Determined | Narrowed | Not determined | Total |
| --- | --- | --- | --- | --- |
| Group A (team answer) | 7 | 12 | 1 | 20 |
| Group B (no team answer) | 4 | 14 | 2 | 20 |
| All | 11 | 26 | 3 | 40 |

Confidence: 6 high, 17 medium, 17 low. No pilot ticket ended as `no_fault_found` after the review rule in Part C.

**Against the team, for the 20 with a Root Cause field:**

| | Count | Tickets |
| --- | --- | --- |
| yes | 13 | 27, 231, 7, 451, 723, 527, 1221, 1294, 1179, 897, 1906, 1800, 1948 |
| more_specific | 4 | 102 (SNR 36 against threshold 40), 10 (solder ball under the RF shield), 512 (GoTo IP4 instead of RTB), 2006 (landing plan and nudge) |
| differs | 1 | 1524 |
| no_team_answer | 2 | 720 (the field holds only the ticket's own link title), 1778 (the field says "Cannot Reproduce") |

"Agrees" often means agreeing with a narrow answer. Of the 13 "yes", 9 are `narrowed`: the team and I both stop at, for example, "radio link" or "GPS degraded", and the evidence does not go further.

**The one "differs": VXEP-1524.**
- The team's Root Cause field says: "Possible: GetTickCount() rollover after 49.7 days system uptime causing map tool continuous timeout."
- The same engineer later wrote in a comment (`data/vxep/VXEP-1524/ticket.md`): "I ruled this out via the logs, and it also would’ve only failed once every 49.7 days." Then: "We don’t have enough information in GCS debug/event logs to investigate further."
- My result is `not_determined`: the GoTo map tool did not stay active, and the cause was not found. The field was never updated after the comment.

**Which attachments made the difference.** 10 of the 15 tickets with converted attachments cite them as evidence:
- **Investigation reports (pptx and pdf)** were the most valuable:
  - VXEP-102 `Vehicle Investigation Report VXEP-102`: GPS status byte and SNR against threshold.
  - VXEP-10 `TPTR-85 ... Customer Summary`: the solder ball under the RF shield.
  - VXEP-512 `AC556_Investigation.pptx`: GoTo IP4 in the XComm log.
  - VXEP-1778 `VXE-512 Vehicle Investigation` PDF: avionics power lost all at once.
  - VXEP-1906 and VXEP-1944 `AIR PMO Multiple Vehicle Investigation Report`: Silvus frequency contention, PLZ 10 km away.
  - VXEP-263 risk assessment PDF: CPU loading and magnetometer.
- **Plain-text logs** decided VXEP-1221. `T95_V722_..._event.txt` and `..._debuglog.txt` show the VTOL state going into land abort and back into a second land command.
- **Operator statements (docx)** on VXEP-790.
- **CSV summaries** (headers and row counts only) added nothing on any pilot ticket. That is expected under the current CSV decision.

**What would settle the open tickets.** 29 of the 40 are not `determined`. Each result's `would_settle_it` lists what would settle it, and one ticket can list more than one thing:

| Would be settled by | Open tickets listing it | Listed first |
| --- | --- | --- |
| AAR package (zip) | 24 | 15 |
| Image (photo or plot) | 16 | 2 |
| Linked ticket (VXEP, VA, FS2, RMA ...) | 14 | 2 |
| External document (SharePoint report, test data) | 13 | 5 |
| Physical inspection or teardown | 13 | 4 |
| Video | 3 | 1 |
| CSV | 1 | 0 |

Only 2 open tickets (VXEP-26 and VXEP-1452) need nothing that is attached in Jira. Linked tickets are worth noting separately. Many VXEP tickets say "see VXEP-12" or "tracked in VXEP-1449". Those tickets are already in the export, so a full run can follow links inside VXEP at no extra export cost. Links to other projects (VA, FS2, RMA, XKIT) are not exported.

### D5. Time and the full run

**Pilot time.**
- The survey (Parts A and B) took about 20 minutes, mostly scripted.
- The 40-ticket analysis ran from 16:03 to 16:10 UTC: about 7 minutes wall clock, with four agents in parallel. The longest batch took 6 minutes because it held the two large log files.
- Checking and review took about 10 minutes.
- The agents used about 635,000 tokens for 40 tickets, about 16,000 per ticket. Log-heavy tickets cost several times more than short ones.

**Estimate.**

| Scope | Tickets | Batches of 10 | Wall time (4 in parallel) | Tokens |
| --- | --- | --- | --- | --- |
| Incident (8D) only (recommended) | 409 | 41 | about 1.5 to 2 hours, over 2 to 3 sessions | about 7 million |
| Incidents + Problem + Corrective Action | 548 | 55 | about 2 to 3 hours | about 9 million |
| All 1,791 | 1,791 | 180 | about 5 to 7 hours | about 20 million or more |

Running all 1,791 would mostly mean tasks, epics and project tickets that have no failure to explain.

**Plan for batches that can resume** (for a later prompt; nothing was set up in this one):
1. A fixed batch list, `results/02_batches.json`, assigning each ticket key to a numbered batch, oldest first.
2. Each batch writes `results/02/batch_NNN.jsonl`. A batch is done when its file exists and has one line per key. A session starts by listing the missing batches, so a run stopped halfway restarts at the next missing batch and redoes nothing.
3. After each round of four batches, run the same check used here: every line parses, every quote is found in its file, there are no em dashes. Commit and push after each round, so a lost session loses at most one round.
4. Follow VXEP links: when a ticket points to another VXEP ticket for its cause, read that ticket too, and record it in the evidence.
5. A final step joins the batches into `results/02_all.jsonl` and writes the report, listing any batch or ticket not done.

---

## Questions for Scott

1. **Position convention.** Which form should results use? Options seen in the data:
   - log numbering, "motor 1 to 4", matching the XCOMM glossary in VXEP-272 (1 front left, 2 front right, 3 rear right, 4 rear left);
   - words, "front left" or "left front";
   - two-letter codes, "FL" or "LF".

   I suggest storing the motor number and the words together, for example "motor 3 (rear right)", since both appear in the tickets and the logs use the number. Your call.
2. **Result format and meanings.**
   - Are the fields in Part C right?
   - Are the meanings of `determined` and `narrowed` right?
   - Do you agree with the rule that a designed abort caused by a degraded input (GPS) is scored on that input, so it is `narrowed`, not `no_fault_found`?
3. **Exporter changes before the full run**, in priority order:
   - (a) Fix the duplicated comments (A5 item 1). This matters most, because duplicated comments make tickets longer and make a single comment look like it was said twice.
   - (b) Write Jira headings inside fields so they cannot be mistaken for comment headers (A5 item 2).
   - (c) Give embedded images their file names where Jira allows (A5 item 3).
   - (d) Skip leading `#` lines when reading CSV headers (A5 item 5).
   - (e) Strip email confidentiality, export control and signature blocks from converted emails (A5 item 6). The signature blocks hold personal phone numbers.
   - (f) Drop the bookkeeping fields listed in A3.
4. **Scope of the full run.** Incidents only (409), incidents plus Problem and Corrective Action (548), or all 1,791?
5. **AAR packages.** They are the most common missing evidence (24 of 29 open pilot tickets), and 280 of 409 incidents have one. Should a later prompt look at what an AAR package contains and whether a text summary of its logs could be exported, the same way CSVs get a header summary?
6. **Linked tickets in other projects.** Many causes are tracked in VA, FS2, RMA or XKIT tickets (for example VXEP-101 points to VA-573, VXEP-1933 to AV-1370). Should those projects be exported too, or only the specific linked tickets?
