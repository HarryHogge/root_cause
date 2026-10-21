# Report 02: Root cause for every incident

- **Prompt:** `prompts/02_incident_run.md`
- **Branch:** `agent/wednesday`
- **Sessions:** one session, started from commit `cd9b67a` (Re-export VXEP with exporter fixes from report 01; add linked tickets and prompt 02). Usage limits paused it twice; the same session resumed each time from the batch files already written.
- **Export:** `data/vxep/manifest.json` exported_at 2026-10-20 17:40 UTC (1,791 tickets). `data/linked/manifest.json` exported_at 2026-10-20 17:50 UTC.
- **Outputs:** `results/02_batches.json`, `results/02/batch_001.jsonl` to `batch_041.jsonl`, `results/02_all.jsonl` (409 lines), `scripts/check_results.py`, this report.
- **Status:** COMPLETE. All 409 Incident (8D) tickets have a result. `python scripts/check_results.py` passes on all 41 batch files and on `results/02_all.jsonl`.

All conclusions here are mine, drawn from the ticket text. Where the engineers' own words are quoted, they are marked as theirs.

---

## Summary

1. **Outcomes.**
   - **166 of 409 incidents (41%) are `determined`.** A specific part or mechanism is shown by a measurement, teardown, swap test or log channel.
   - **194 (47%) are `narrowed`** to a system or a short list.
   - **41 (10%) are `not_determined`.**
   - **8 (2%) are `no_fault_found`.**
2. **Two parts fail far more often than anything else:**
   - **AS150 power contacts:** 22 incidents, 13 determined. These are the battery and HLB power connectors, including the anti-spark contact.
   - **HLB cells:** 20 incidents, 12 determined. Five of the incidents that name a cell name cell 6.
   - After those come magnetometer problems (17), lift ESCs (9 plus 6 where motor and ESC were not separated), autopilot and XCOMM watchdog resets (14), land abort logic (9) and FWAP IMU boards (7, 6 determined).
3. **Against the team.** Where the team wrote a Root Cause (215 incidents), I agreed on 148, was more specific on 30, and differed on 16. On the other 21, the field holds no usable cause.
4. **What would settle the open ones.** The 235 open results most often need the AAR packages (listed on 158, listed first on 76). Next come a single photo or plot attached to the ticket (listed first on 75) and physical inspection (113). Section 9 lists the 75 images by file name.
5. **Linked tickets mattered.** 304 results read at least one linked ticket and 159 cite one as evidence. On 29 `determined` results, the deciding evidence (teardown, measurement or code finding) comes mainly from a linked RMA, ENG, VA, FS2 or BAT ticket.

---

## 1. Progress

All 41 batches are done: 409 of 409 tickets. Every ticket's `ticket.md` was read. Every converted attachment was read, with these limits, each recorded in that result's `notes`:

- **Large logs searched rather than read line by line.** Plain-text logs over about 300 KB were read by searching for faults, state changes, watchdog boots and link events, with repeated TRACE, ISR and status lines skipped. Examples: VXEP-1221, 1524, 1797, 1314, 1617, 146, 608, 1149, 530; fuel cell QC logs on RMA-242, 257 and 336.
- **Long documents searched by keyword.** Some long linked-ticket documents with no bearing on cause were searched rather than read in full: the two Airworthiness Directive PDFs on FS2-2321, RMA-331 quote terms, RMA bailment forms, and the later pages of the RMA-1082 OCR.

**Tickets not readable:** none. Some attachments had no usable text (section 10), so a few results rest on `ticket.md` alone.

**Review after the batches**, recorded in each affected line's `notes`:
- 7 results listed a linked ticket as missing when it was in the export (VXEP-41, 275, 811, 1317, 1452, 1464, 1495). Those tickets were read and the results updated. Two changed in detail (VXEP-1317, VXEP-1495); none changed outcome.
- 20 results had compared themselves with the engineers' comments on tickets that have no Root Cause field. They were set to `no_team_answer`, as the format requires; the comparison is kept in `notes`. VXEP-720 was set the same way, because its Root Cause field is only its own link title.
- VXEP-748 changed from `no_fault_found` to `determined` to match VXEP-720, which has the same battery checker cause.

### Part A findings (first session)

Every exporter fix listed in the prompt was checked against the data. All are as described, with the small exceptions noted. Nothing stopped the run.

1. **Comments: fixed.** VXEP-40, 426, 282 and 101 now have as many comments as their header says (42, 84, 42 and 25), each comment different, in date order. Across all 1,791 tickets, only VXEP-1491 has two identical comments: two separate image-only comments, which is real.
   - **Correction to report 01.** Report 01 (A5, item 1) said the second copy of the comments was the complete list, so VXEP-40 had 22 real comments. That was wrong. The oldest comments were missing, and VXEP-40 has 42.
2. **Headings: fixed.** Every `##` line is now an exporter section and every `###` line a comment header. Nine lines in four tickets start with `#` but are ordinary text (for example `data/vxep/VXEP-880/ticket.md` "#2-> 881").
3. **Embedded files: fixed, two small leftovers.** There are 1,392 named embeds and 7 unmatched.
   - 10 named embeds are not in their ticket's attachment table: VXEP-272, 426, 944, 1016 (2) and 1880 (3 battery screenshots). These are probably images deleted from Jira.
   - Email signature graphics appear as embeds on VXEP-1907 and VXEP-1967.
4. **CSV headers: fixed.** `data/vxep/VXEP-1980/attachments/64333_2026-08-28_13-25-VH_CID-4-log.csv.md` now shows the logger lines. VXEP-1291's boost board test shows 8 columns.
5. **Emails: fixed.** No notices, addresses or phone numbers remain in the 32 converted emails. Four subjects start "EXTERNAL:" as part of the subject.
6. **Bookkeeping fields: gone.**
7. **Linked tickets.** `data/linked/` has 558 folders, matching the 558 keys in its `index.jsonl`. Its `manifest.json` says 561 tickets; the gap of 3 is not explained there.
8. **Moved tickets: as described.** All 17 `moved` targets exist, and 9 point into `data/vxep/`.

---

## 2. Outcomes

| Outcome | Count | Share |
| --- | --- | --- |
| determined | 166 | 41% |
| narrowed | 194 | 47% |
| not_determined | 41 | 10% |
| no_fault_found | 8 | 2% |

Confidence: 56 high, 204 medium, 149 low.

**By year created**

| Year | Determined | Narrowed | Not determined | No fault found | Total |
| --- | --- | --- | --- | --- | --- |
| 2023 | 26 | 20 | 5 | 3 | 54 |
| 2024 | 44 | 50 | 9 | 1 | 104 |
| 2025 | 61 | 67 | 12 | 0 | 140 |
| 2026 | 35 | 57 | 15 | 4 | 111 |

2026 has the lowest share determined (32%). Many of those tickets are still open (D2 or D4), or closed without a teardown.

**By Incident Type field**

| Incident Type | Determined | Narrowed | Not determined | No fault found | Total |
| --- | --- | --- | --- | --- | --- |
| Mission Failure/Abort | 28 | 51 | 4 | 0 | 83 |
| Aircraft Damage | 32 | 25 | 6 | 0 | 63 |
| Aircraft Loss | 10 | 11 | 7 | 0 | 28 |
| Near Miss | 13 | 11 | 1 | 1 | 26 |
| Squawk | 7 | 8 | 5 | 2 | 22 |
| Other | 11 | 5 | 2 | 0 | 18 |
| (field blank) | 65 | 83 | 16 | 5 | 169 |

Aircraft Loss has the highest share not determined (7 of 28), usually because the aircraft was not recovered. Mission Failure/Abort is mostly `narrowed`, because many aborts are designed responses to a degraded input whose cause is not shown (the settled rule).

**By ticket status:**
- D8 Closed: 113 determined of 235.
- Bermuda Triangle: 5 determined of 39.
- Canceled: 25 determined of 63.

---

## 3. What fails

### By system (where the failure started)

| System | Determined | Narrowed | Not det. | No fault | Total |
| --- | --- | --- | --- | --- | --- |
| vehicle_software (VTOL AP, FWAP, XCOMM, MCM firmware) | 30 | 28 | 0 | 0 | 58 |
| avionics_hw (FWAP, VTOL AP, XCOMM, MCM boards) | 21 | 28 | 0 | 0 | 49 |
| ground_software (GCS, OGCS, VSM) | 17 | 24 | 0 | 1 | 42 |
| (no system: not determined) | 0 | 0 | 34 | 1 | 35 |
| battery (HLB, main battery, LEMB BMS) | 15 | 14 | 2 | 0 | 31 |
| propulsion (lift and cruise motors, ESCs, rotors) | 8 | 15 | 0 | 1 | 24 |
| power_connector | 13 | 8 | 0 | 1 | 22 |
| payload | 5 | 16 | 0 | 0 | 21 |
| gps | 3 | 17 | 0 | 0 | 20 |
| operator_procedure | 13 | 4 | 0 | 1 | 18 |
| fuel_cell | 8 | 5 | 2 | 1 | 16 |
| environment | 4 | 11 | 0 | 0 | 15 |
| sensors_air_data | 8 | 5 | 0 | 1 | 14 |
| ground_equipment | 8 | 2 | 3 | 0 | 13 |
| radio_link | 2 | 9 | 0 | 1 | 12 |
| harness | 3 | 5 | 0 | 0 | 8 |
| manufacturing_quality | 7 | 1 | 0 | 0 | 8 |
| airframe | 1 | 2 | 0 | 0 | 3 |

Why it failed (`initiating_cause`): unknown 209, design 93, operator_action 36, manufacturing_quality 31, environment 19, maintenance_or_assembly 11, outdated_software_or_ads_not_applied 9, wear_or_age 1.

### Repeat failures (five or more incidents)

Grouped by me from the `component` and `failure_mode` fields. The groups cut across systems. "Det." is the number `determined`. Ticket numbers are VXEP keys.

| Part or failure mode | Incidents | Det. | Tickets (determined in bold) |
| --- | --- | --- | --- |
| **AS150 power contact** (HLB and main battery connectors, anti-spark contact) | 22 | 13 | **12, 13, 101, 293, 305, 415, 539, 540, 646, 761, 985, 999, 1278**, 28, 149, 231, 834, 1489, 1778, 1801, 1967, 2007 |
| **HLB cells** (cell sag or dropout under lift load, self-discharge, electrolyte loss) | 20 | 12 | **1293, 1398, 1407, 1417, 1418, 1435, 1449, 1485, 1492, 1622, 1696, 1976**, 1408, 1412, 1413, 1488, 1495, 1499, 1965, 1974 |
| Magnetometer (FWAP or VTOL AP mag data, checks, interference) | 17 | 5 | **579, 896, 1056, 1219, 1443**, 118, 263, 275, 342, 500, 529, 530, 605, 897, 966, 967, 1554 |
| GNSS quality causing a designed abort or land-in-place | 11 | 0 | 102, 431, 451, 527, 1066, 1465, 1592, 1906, 1912, 1913, 1929 |
| Lift ESC | 9 | 4 | **44, 51, 384, 1464**, 272, 274, 628, 811, 1294 |
| Land abort / land immediately logic | 9 | 7 | **146, 283, 453, 1221, 1471, 1476, 1797**, 233, 598 |
| VTOL AP watchdog reset or task lockup | 8 | 2 | **835, 1904**, 9, 11, 41, 161, 230, 844 |
| FWAP IMU board (MPU-9250, MAGACC2, gyro) | 7 | 6 | **10, 619, 1776, 1838, 1840, 1971**, 637 |
| XCOMM microSD card corruption | 7 | 3 | **236, 237, 1149**, 1069, 1292, 1309, 1943 |
| NovAtel GNSS receiver dropouts | 7 | 0 | 1222, 1462, 1882, 1883, 1891, 2013, 2019 |
| Silvus radio link (frequency, configuration) | 7 | 2 | **1310, 1686**, 1593, 1691, 1800, 1866, 1944 |
| Airspeed / pitot (calibration, blockage, erratic) | 7 | 2 | **368, 1491**, 292, 381, 1774, 1970, 1989 |
| XCOMM watchdog, exception or lockup | 6 | 5 | **1548, 1775, 1780, 1978, 2014**, 1692 |
| Lift motor or ESC, not separated | 6 | 1 | **1630**, 791, 1802, 1845, 1881, 1977 |
| GCS mission simulation blocking the uplink | 6 | 1 | **220**, 555, 600, 608, 1047, 1061 |
| Operator altitude or Go To entry | 6 | 5 | **512, 651, 652, 1858, 1928**, 1988 |
| MCM power via TPS16630 eFuse on the payload bus | 5 | 3 | **723, 1315, 2005**, 1890, 1956 |
| Gimbal ground loop or magnetic interference (E140) | 5 | 2 | **813, 1034**, 500, 530, 897 |
| Fuel cell cathode blower or cooling fan | 5 | 4 | **14, 1513, 1799, 1803**, 570 |
| Wind, thermals, updrafts | 15 | 4 | **842, 1480, 1570, 2023**, 17, 160, 524, 532, 832, 1289, 1482, 1562, 1863, 1864, 1987 |

What stands out inside the groups:

- **AS150 contacts fail in three ways**, all shown by measurement or teardown:
  - High contact resistance from poor plating: VXEP-101 (305 and 253 uOhm), VXEP-305 (480 uOhm), VXEP-415 (435 uOhm against a 235 uOhm limit), VXEP-646.
  - Incomplete mate, leaving the 6 ohm anti-spark contact carrying load current: VXEP-761, 985, 1278, 539.
  - Undersized sockets that stop a full mate: VXEP-540 and 999 (0.272 to 0.273 in against a 0.275 in pin).
- **HLB cells.** The fleet investigation (VXEP-1449, with BAT-223 and BAT-367) found electrolyte leaking or evaporating, and a pouch seal defect, in the Advanced Energy 3300 mAh cells. Where a cell number is named, it is **cell 6 on five incidents** (VXEP-1435, 1492, 1495, 1696 with cell 7, 1976), cell 5 on one (1407) and cell 2 on one (1485). I do not know how cells are numbered in the pack, or whether cell 6 sits in a hotter or more loaded spot. That would be worth checking.
- **Lift ESC soft-start MOSFETs** recur: VXEP-44/51 (Q20, same event), 384 (Q20 to Q23), 272 (suspected), and the systemic tracker VXEP-628.
- **FWAP MAGACC2 / IMU boards** show a workmanship pattern: a solder ball under the RF shield (VXEP-10) and burned flux under the RF shield (VXEP-1971). Two other units failed MPU-9250 initialization (VXEP-1838, 1840).
- **XCOMM.** Five of six XCOMM firmware lockups are determined: watchdog after dynamic memory allocation (1548), a critical exception (1775, 1780, with identical report timelines), an infinite network wait in CycloneTCP (1978), and a bootloop after an update (2014). The SD card corruption cases (236, 237, 1149) are a separate, hardware-side group.

---

## 4. Position (propulsion)

24 results have `system` propulsion:

| Position | Results | Tickets |
| --- | --- | --- |
| motor 1 (front left) | 5 | 199, 1294, 1630, 1881, 1933 |
| motor 2 (front right) | 5 | 44, 51, 274, 409, 811 |
| motor 3 (rear right) | 7 | 384, 791, 1464, 1802, 1845, 1951, 1977 |
| motor 4 (rear left) | 2 | 272, 900 |
| nose cruise motor | 1 | 99 |
| no position | 4 | 103 (all lift motors), 279 (XE25 nose ESC), 628 (fleet tracker), 1889 (cruise propeller) |

Results in other systems also name lift motors: VXEP-426 (motor 3), 1566 and 1980 (motor 4), and 8 (motors 1 and 2).

**Does any position fail more often?** Motor 3 (rear right) has the most: 7 propulsion results, 8 counting all systems. That is not enough to call it a pattern:
- **The counts are small.** VXEP-44 and 51 are the same event, so motor 2 has 4 distinct events.
- **Some positions rest on thin evidence:**
  - VXEP-1294 takes "front left" from the Plan field, not a measurement.
  - VXEP-1845 is a HIL rig.
  - VXEP-1630 has a conflict between the log (read as motor 3) and the dyno swap test (position 1). The dyno result was used.
  - VXEP-274 has a witness saying front left and a log pointing to front right.

  Each is explained in that result's `notes`.

Two results kept words without a number, as the convention requires, because their wording could not be mapped safely: VXEP-1902 and VXEP-1905 ("left lift boom", which carries two motors).

---

## 5. Against the team

For the 215 incidents with a Root Cause field:

| agrees_with_team | Count |
| --- | --- |
| yes | 148 |
| more_specific | 30 |
| differs | 16 |
| no_team_answer (field says unknown, cannot reproduce, or only points elsewhere) | 21 |

Every `differs` case, with the conflicting words. The Root Cause text is the team's; the rest is my reading.

- **VXEP-36.**
  - Root Cause: "Incorrect interpretation of information."
  - The same ticket's Issue Status says "this behavior was a result of PTR-85 autopilot hardware failure."
  - I scored it as an autopilot hardware fault, narrowed, low confidence. PTR-85 is not in the export.
- **VXEP-265.**
  - Root Cause: "Unstable flow of rotor wake causes inaccuracies in baro altimeter measurements".
  - The comments say the problem stopped when only the VTOL AP was swapped ("ADP did not get replaced"), and the linked task says "VTOL AP was replaced and issue was resolved."
  - I narrowed it to the removed VTOL AP, with rotor wake at most a contributor.
- **VXEP-342.**
  - Root Cause: "Believed to be an operating procedure that needs to be updated to include restarting the wizard".
  - The customer wrote "We have tried separate aircraft, separate GCS, power cycles and Mag Checks and the error is still occurring", and the only engineering review says "the FW AP IMU error checks failed".
  - I narrowed it to the FWAP IMU checks, not procedure.
- **VXEP-529.**
  - Root Cause: "Not an issue... Goto was ignored because it was too far along in the landing sequence."
  - I accept that for the Go To. But the trigger was "the heading from the fixed-wing ap was erroneous for some reason", which was never resolved.
- **VXEP-571.**
  - Root Cause: "It is believed to be a software issue".
  - The only log line is "vt lost link during lch, aborting", and the closing comment says "Loss of link".
  - I scored it on the radio link (a designed abort).
- **VXEP-597.**
  - Root Cause: a partial battery disconnect by the operator.
  - The customer later wrote "He notes and acknowledges that the batteries were connected during this anomaly."
  - Not determined.
- **VXEP-611.**
  - Root Cause: "Operator Error: Did not follow ADs".
  - The consolidated report says the crash flight was "Not investigated due to outdated firmware".
  - Not determined, because nothing ties a firmware fault to the crash.
- **VXEP-944.**
  - Root Cause: a "VTOL or VTOL ESC or in circuit wiring intermittent low resistance short".
  - Teardown and failure analysis found the XCOMM Ethernet switch U11 failed from "an overvoltage condition on the 3.3V rail".
  - I narrowed it to the XCOMM power circuit.
- **VXEP-967.**
  - Root Cause: "Faulty SD Card".
  - The data review found "erroneous fixed-wing mag" with "a huge delta in the offsets and the z span", and the returned card "read like normal".
  - I narrowed it to the FWAP magnetometer.
- **VXEP-1509.**
  - Root Cause: "intermittently degraded environmental conditions".
  - The customer said "GPS in the area on other devices was not effected. Only the gimbal", and an engineer read "the VN board is not initializing".
  - I narrowed it to the gimbal GNSS.
- **VXEP-1524.**
  - Root Cause: the "GetTickCount() rollover after 49.7 days".
  - The same engineer later wrote "I ruled this out via the logs, and it also would’ve only failed once every 49.7 days."
  - I narrowed it to the GCS map tool. (In the pilot this was `not_determined`; see section 6.)
- **VXEP-1554.**
  - Root Cause: "rebar or some type of metal in the concrete pad".
  - An engineer found the disturbance "follows the vehicle up 100'" after throttle-up, and wrote "That likely points to the issue with the fuel cell being related to the mag disturbance."
  - I narrowed it to an external magnetic disturbance, source unsettled.
- **VXEP-1566.**
  - Root Cause: "None. Aircraft behaved as expected."
  - Engineers wrote "This looks like a case of the motor delay after the LR throttle was low on transition" and linked it to the VXEP-426 motor start delay.
  - I narrowed it to that delay plus wind.
- **VXEP-1774.**
  - Root Cause: "SW issues in 6.6.1 will be addressed in 6.7.1".
  - The 933 AAR shows "Abnormal airspeed indications preflight and during launch", the same as the VXE 932 crash flown with the 933 center wing.
  - I narrowed it to the air data on that center wing.
- **VXEP-1797.**
  - Root Cause: deleting gcs.ini reverted to an unsafe LandOnError=1.
  - The engineer's later test says "this does not appear to be a plausible explanation" and "the file must have been changed by someone".
  - The LandOnError mechanism is determined; how it got into the file is not.
- **VXEP-1988.**
  - Root Cause: an "altitude estimation error", possibly the airdata board.
  - The software lead later wrote "The most likely workflow that caused this was probably an attempt to edit 300 and make it 200", which the OGCS 1.4.2 field turns into 2 ft.
  - I narrowed it to the OGCS altitude entry field.

---

## 6. Against the pilot

The 40 pilot tickets were all in this run. Their outcome, system, confidence or agreement changed as follows. Only the component wording changed on the others.

| Key | Change | Why |
| --- | --- | --- |
| VXEP-720 * | narrowed to determined; low to medium confidence | The complete comments and linked VA-2115 and VXEP-759 show flight data integration agreeing with the aircraft estimate (about 45%), so the checker model is shown to be wrong, not just suspected. |
| VXEP-1524 | not_determined to narrowed | The XCOMM log of the 18 Sep flight shows no Go To leaving the GCS after the last mission upload, placing the fault in the GCS map tool. |
| VXEP-1294 | (no system) to propulsion, motor 1 (front left); yes to more_specific | The Plan field names a likely front left ESC failure. It stays narrowed with low confidence, because that comes from discussion, not a measurement. |
| VXEP-2006 | narrowed to no_fault_found; more_specific to yes | Engineers found the patterns set correctly at 200 ft and wrote "this does not match what I see in the data": the reported altitude drop is not in the logs. |
| VXEP-26 | narrowed to determined | Linked GCSS-77 explains the gauge limit and the firmware change, and was released as the fix. |
| VXEP-283 | narrowed to determined; propulsion to vehicle_software | Read as the clone covering only the abort logic, which FS2-1512 ties to a race condition seen in HIL and fixed in 6.3.4. The power fault is VXEP-282's. |
| VXEP-1398 | narrowed to determined | The battery balance warning right after launch, then the hard landing, was judged direct evidence of an HLB cell imbalance. The cell and its mechanism are still not shown for this pack. |
| VXEP-1926 | narrowed to determined | The fault followed the gimbal across two aircraft and cleared after firmware 4.0.1.4. |
| VXEP-1944 | determined to narrowed; operator_procedure to radio_link | Under the settled designed-abort rule, the result is scored on the degraded input (link loss from frequency contention), not on the lost comms behavior. |
| VXEP-1845 | not_determined to narrowed, motor 3 (rear right) | The abort is designed, so it is scored on the rear right motor that did not start. It is a HIL rig, flagged in notes. |
| VXEP-30, 35, 639, 1452, 1461 | system changed only | VXEP-30 and 35 to ground_equipment, 639 to harness (repeats on the same center wing), 1452 to payload, 1461 to vehicle_software. |
| VXEP-7, 39, 897, 1179, 1800 | confidence only | 7: high to medium. 39: medium to high. 897: low to medium. 1179: medium to low. 1800: low to medium. |
| VXEP-102, 10 | more_specific to yes | Same finding as the pilot. This run judged the team's text already named the same mechanism. |

**The eight tickets whose comments were incomplete in the pilot** (marked * where the result changed):
- **VXEP-720** changed (above).
- **VXEP-639** moved from battery to harness. The full comments show the fluctuation repeating on the same center wing with different HLBs.
- **VXEP-512, 263, 1630, 1661, 1778 and 1989** kept the same outcome and system. The fuller comments added detail:
  - VXEP-1630: the conflict between the log reading (motor 3) and the dyno result (position 1).
  - VXEP-1661: the RMA technician's finding that an XCOMM swap restored the connection, which keeps it narrowed between two boards.
  - VXEP-1778: the report contradicting itself on the anti-spark resistor.

---

## 7. What the linked tickets added

- 304 of 409 results read at least one linked ticket (VXEP or other projects).
- 159 cite a ticket in `data/linked/` as evidence. By project: FS2 74 citations, RMA 62, ENG 59, VA 43, GCSS 16, XKIT 12, BAT 9, PLD 7, SMUP 4, MS 4, OGCS 2, AV 1.
- On 29 `determined` results, half or more of the evidence comes from linked tickets. Examples where the linked ticket supplied the deciding finding:
  - **VXEP-12** (ENG-2181, VA-35) and **VXEP-101** (ENG-3042): AS150 contact measurements and damage.
  - **VXEP-44 / 51** (ENG-3034, VA-851): the ESC teardown finding MOSFET Q20 detached and U1 destroyed.
  - **VXEP-46** (ENG-2992): capacitor C20 measured at 0.015 nF instead of about 3.3 nF.
  - **VXEP-514** (FS2-2114) and **VXEP-579** (FS2-2097): the software defects (Config Manager memory corruption; FPU context not saved in taskOneHz).
  - **VXEP-1449** (BAT-223, BAT-367): HLB cell dissections.
  - **VXEP-1933** (AV-1370, XKIT-5529, XKIT-5550): the front left motor phase lead insulation failure.
  - **VXEP-1840** (RMA-960, FS2-4500) and **VXEP-1072** (RMA-511, FS2-3022): board-level findings from the RMA.
- 24 open results still list a linked ticket that is not in the export (for example FS2-1426, FS2-1568, PTR-85, VIT2-227, RMA-563, RMA-946, NCC-161, NCC-168, NCC-174, XKIT-4742).

---

## 8. What would settle the open ones

235 results are `narrowed` or `not_determined`. Each lists what would settle it, and a result can list several things.

| Would be settled by | Open results listing it | Listed first |
| --- | --- | --- |
| AAR package (zip) | 158 | 76 |
| Image (photo or plot attached to the ticket) | 87 | 75 |
| Physical inspection or teardown | 113 | 28 |
| External document (SharePoint report, test data) | 92 | 37 |
| Linked ticket not in the export | 24 | 8 |
| Other attachment (.vmis, .t00, .pcapng ...) | 21 | 5 |
| Video | 11 | 3 |
| CSV | 1 | 1 |

Two open results list nothing (VXEP-1562 and 1987). Both are wind cases with no data left to examine.

### 9. Images that would most likely settle a ticket (input for the image step)

These 75 open tickets each list one named image first. Every file name was checked against the ticket's attachment table. Two images sit on a linked ticket instead (VXEP-1506's is on RMA-745, VXEP-1509's on PLD-54).

| Ticket | Image | What to look for |
| --- | --- | --- |
| VXEP-160 | image-20240125-000050.png | pitch, estimated AoA and wingtip AoA at the roll |
| VXEP-161 | Landing Power_Motors.png | motor power dropping to zero at the watchdog reset |
| VXEP-231 | image-20231220-231347.png | BMS voltage against VTOL measured voltage |
| VXEP-239 | image-20240122-230847.png | main battery voltage drop, size and timing |
| VXEP-265 | image-20240213-201044.png | baro altitude against GPS before the VTOL AP swap |
| VXEP-279 | image-20240217-054529.png | fire damage: burn origin in ESC or current sense board |
| VXEP-426 | image-20250919-190452 (9c8ca7cf-53e2-4748-af48-6cafbe1da696).png | VTOL FW flag forcing motor 3 to idle against motor 3 current |
| VXEP-452 | image-20240628-205312.png | crash dump: which task or address faulted |
| VXEP-527 | Image.jfif | GCS VTOL Control fault message from the 8/7 abort |
| VXEP-530 | image-20240905-173137.png | FW vs VTOL heading disagreement timeline |
| VXEP-532 | image-20241210-202509.png | power integral and battery state over the drain |
| VXEP-538 | QORASWCAWE-744NAS2024002 Tile 2 - Broken snips - break.jpg | fracture location and surface |
| VXEP-570 | TemperatureGraph_VXE-514.png | fuselage temperature against fan enable and 12 V current |
| VXEP-639 | image-20241113-195006.png | VREF against HLB voltage |
| VXEP-645 | GPS no fix 6.3.4.jpg | GPS status screen and selected COM port |
| VXEP-732 | image-20250218-180656.png | which of payload voltage, retract current, Ethernet dropped first |
| VXEP-760 | image-20241107-193321.png | power fault list after the 6 s gap |
| VXEP-790 | Picture 2.png | system load at the time of reduced responsiveness |
| VXEP-832 | image-20241212-202843.png | extent of leading edge and prop icing |
| VXEP-897 | image-20250113-230009.png | FWAP vs VTOL heading and mag field during launch |
| VXEP-979 | image-20250205-220215.png | labels of the two adapters |
| VXEP-1057 | 398.png | which side of the link dropped at the abort |
| VXEP-1066 | image-20250320-225059.png | GPS accuracy and C/N0 against the abort thresholds |
| VXEP-1137 | image (9).png | SoC against pack voltage through landing |
| VXEP-1230 | image-20250429-203913.png | XCOMM traffic per port at the drop |
| VXEP-1289 | image-20250519-165805.png | throttle and altitude, climb at zero throttle |
| VXEP-1292 | image-20250603-154610.png | the corrupted XCOMM event log |
| VXEP-1313 | image-20250625-015403.png | link status against RTC update timing |
| VXEP-1396 | Fuel Cell Hot.PNG | fuel cell temperature, power and state |
| VXEP-1413 | HLB issues with chart.png | which battery flew which flight, with which issue |
| VXEP-1451 | Error Message final.PNG | which message blocked takeoff |
| VXEP-1458 | MAIN fire (1).jpeg | where the fire started |
| VXEP-1461 | image-20250818-161634.png | PMC reset lines and timing against the reported instances |
| VXEP-1462 | image-20250806-160037.png | NovAtel heartbeat timeouts, which dropped first |
| VXEP-1465 | image-20250811-191136.png | GPS uncertainty against the abort threshold |
| VXEP-1474 | download.png | spiral RTB simulation against the flown track |
| VXEP-1475 | charger1.jpg | charger and aircraft SOC for the same battery |
| VXEP-1488 | vxe-499takeoff.png | cell voltages at takeoff, which cell |
| VXEP-1489 | image-20250828-155107.png | HLB voltage and current at transition |
| VXEP-1496 | image-20260113-182223.png | update error or successful version at closure |
| VXEP-1499 | image-20250905-124002.png | plot tying the flight to the HLB cell dropout |
| VXEP-1506 | 471Nose.jpg (on RMA-745) | burn pattern at the 16-pin nose ODU |
| VXEP-1509 | image-20250915-224720.png (on PLD-54) | E140 GPS diagnostic error window |
| VXEP-1554 | image-20251017-150806.png | mag magnitude against throttle and altitude |
| VXEP-1557 | image-20260708-213739.png | main battery voltage against forward throttle |
| VXEP-1561 | Image (11).jpg | burnt components or connector damage on the charger |
| VXEP-1566 | image-20260115-161623.png | which motor lagged on transition, and by how much |
| VXEP-1569 | image-20251030-192219.png | CAN message timing and air data at the fault |
| VXEP-1593 | image-20251111-175551.png | Silvus link and noise readings at the dropout |
| VXEP-1637 | Error list.jpg | Epsilon error list (tilt encoder vs GPS faults) |
| VXEP-1687 | image-20260202-141247.png | lift motor loading and pitch command against elevator |
| VXEP-1691 | IPCOMM.jpg | tail number and IPs shown by IPCOMM |
| VXEP-1774 | image-20260923-151314.png | 933 airspeed trace against the 932 crash |
| VXEP-1844 | 23e3ee71-f5e5-434c-9436-a077878115a7.png | reported route against the flown path |
| VXEP-1846 | download.png | warnings and flight state at 36 minutes |
| VXEP-1864 | image-20260423-211842.png | vibration of the aborted launch against the reference |
| VXEP-1881 | image-20260602-161554.png | motor 1 throttle saturating at the pitch down |
| VXEP-1883 | image-20261005-221821.png | XCOMM event log lines that mark the fault |
| VXEP-1889 | image-20260527-175256.png | IMU accelerations: blade loss before nose cone separation? |
| VXEP-1902 | 20260817_160016.jpg | left lift boom motors, mounts, wing shift bracket |
| VXEP-1905 | image-20260605-160220.png | left vs right lift motor response at transition |
| VXEP-1906 | image-20260605-165654.png | GPS accuracy and satellites against the abort threshold |
| VXEP-1925 | pitch down for 942.jpg | attitude just before link loss |
| VXEP-1927 | GPS fault VXE1016 resolved in flight.jpg | fault message and GPS quality values |
| VXEP-1929 | image-20260623-191458.png | CN0 against heading in the orbit (directional jamming) |
| VXEP-1962 | Release notes.jpg | which MWIR firmware fixes the FFC/NUC freeze |
| VXEP-1965 | image-20260717-025312.png | HLB cell voltages during landing |
| VXEP-1966 | image-20260810-184843.png | bus voltage and motor commands in the low voltage launch |
| VXEP-1970 | image-20260728-184134.png | airspeed against ground speed through transition |
| VXEP-1974 | image (1).png | HLB per-cell voltages, which cell dropped |
| VXEP-1977 | image-20260806-161340.png | lift throttles, motor 3 saturated at the upset |
| VXEP-1989 | image-20260917-165948.png | airspeed before takeoff and its drop to 0 |
| VXEP-2018 | image-20261009-194437.png | pitch command against response and elevator |
| VXEP-2022 | Ping200 Settings.jpg | Baro Altitude Source setting |
| VXEP-2024 | image (62).jpg | location and extent of fire damage on the HLB |

---

## 10. Problems in the data found during the run

**Attachments with no usable text**
- **Scanned RMA intake, induction and quote PDFs with no text.** These are the most common case. Examples: RMA-122, 128, 129, 181, 184, 208, 247, 242, 253, 299, 358, 363, 365, 366, 438, 528, 704, 705, 721, 722, 745, 796, 820, 933, 970, 971, 972, 1070, 1102, 1103, 1112, 1114, 1116. Also `data/vxep/VXEP-910/attachments/25597_Stalker Loss of Link 26 Sep (3)(562).pdf.md` and VXEP-1479's two PDFs.
- **Text that converted as font glyph codes** (unreadable): VXEP-274 attachment 26799, five of six PDFs on VXEP-1474, and the VXE-568 Incident Investigation PDF on RMA-435.
- **Text with reversed characters:** the drawing PDF on VXEP-258.
- **Mishap report forms that converted as the blank template** (operator statements lost): VXEP-1397, 1398, 1418, 1485, 1489, 1568.
- **Title only:** `data/vxep/VXEP-1630/attachments/36681_Vt00027.docx.md`. Empty: VXEP-540's proposedChange xlsx.

**Cut files**
- The VXEP-236 results spreadsheet holds 300 of 2,894 rows (the 300-row sheet limit).
- The four VTL and XCOMM xlsx logs on VA-400, and the xlsx logs on ENG-2992, are cut at 150,000 characters and cover only pre-flight data.

**Fields that disagree with the text**
- Tail numbers:
  - VXEP-265: field 604, text 606 (cloned ticket).
  - VXEP-533: field 591, text and AAR 551.
  - VXEP-1482: title 790, field 709.
  - VXEP-916: text V478, pack V748.
- Serial numbers:
  - VXEP-1398: HLB 2-3490 in a comment, 4115 in the VXEP-1449 table.
  - VXEP-1948: second fuel cell 998 and 988.
- Other text:
  - VXEP-1492: title 2.5 V, description 2.95 V.
  - VXEP-651: Root Cause says IP4, comments say IP5.

**Attachments from another aircraft or event**
- VXEP-608's only log is from tail 337, not 336.
- VXEP-1890's frontend log is from VXE 880.
- VXEP-2013 carries the 918 AAR.
- VXEP-2015's pack is named V967.
- VXEP-1570's AAR has the same file name as the August AAR on VXEP-1480.
- FS2-4161 is labelled AC 467/V647 but is about 674.
- The VXEP-780 report header says VXEP-732.
- The FS2-2825 title cites VXEP-556 but concerns VXEP-512/546.

**Text copied between tickets**
- VXEP-1775 and 1780 have identical report timelines.
- VXEP-1838 and 1840 have the same Issue Status.
- The RMA-971 finding is word for word the RMA-972 comment.

**Self-contradiction**
- The VXEP-1778 investigation report gives the anti-spark resistor as open circuit on page 7 and 6.0 ohm on page 10.

**Keys cited in tickets but absent from the export**
- VXEP-322, VXEP-542 (its content appears as ENG-2944), PTR-85, VIT2-227, VIT2-291, VA-1300, SMU-136, FS2-1426, FS2-1568, FS2-3188, FS2-3923, FS2-3934, ENG-3477, RMA-563, RMA-861, RMA-862, RMA-946, RMA-973, NCC-161, NCC-168, NCC-174, XKIT-4742.
- VXEP keys run to VXEP-2024 but the export has 1,791 tickets, so some VXEP keys no longer exist.

**Duplicate and clone tickets** are each counted as their own incident. The affected pairs:
- 44 and 51
- 429 and 514
- 526 and 525
- 966 and 967
- 1408 and 1407
- 1418 and 1417
- 1476 and 1471
- 1617 and 1314
- 11 and 41
- 282 and 283 (clone split into power fault and abort logic)

Outcomes differ inside some pairs, because the duplicate carries less evidence of its own. 429 is narrowed while 514 is determined, and 1408 is narrowed while 1407 is determined. Whether duplicates should be counted once is a question below.

---

## 11. Questions for Scott

1. **Component names: group as is, or glossary first?**
   - The `system` field is consistent, because it comes from a fixed list.
   - `component` is free text and only partly consistent:
     - Common parts are named the same way: "AS150 power contact", "HLB", "lift ESC", "XCOMM", "FWAP".
     - The same thing can still appear several ways. For example, "FWAP IMU roll gyro", "FWAP MPU-9250 IMU (MAGACC2 board)" and "fixed wing autopilot microcontroller" are all FWAP hardware at different levels of detail.
     - Software names mix module names with version numbers.
   - The repeat-failure table in section 3 needed hand grouping.
   - My recommendation: run the Confluence glossary step next and add a `component_code` field from it, rather than trusting text grouping for counts.
2. **Duplicates and clones.** Count each incident ticket once, as now, or merge duplicates into their main ticket for the statistics? Merging would remove about 10 tickets from the counts.
3. **HLB cell 6.** Five incidents name cell 6. Is it worth asking the battery team how cells are numbered, and whether cell 6 has a thermal or load reason to fail first?
4. **Image step.** Section 9 lists 75 tickets where one named image would most likely settle the result. Is that list the right input, or should the image step also cover the 12 open tickets that list an image second or later?
5. **AAR step.** AAR packages are the top missing evidence (158 open results). The decision log puts AAR after the full text run. Is this the time?
6. **Linked tickets not exported.** 24 open results list a linked ticket that Jira did not return or that is not linked by key (section 10). Can these be exported in a top-up run, and can the 3-ticket gap in `data/linked/manifest.json` (561 against 558 folders) be checked?
7. **Designed aborts.** Under the settled rule, 11 GNSS-quality aborts and the link-loss aborts are `narrowed` with no cause for the degraded input. Should the report treat these as their own category ("protection worked; input cause unknown"), so they are not read as unsolved failures?
