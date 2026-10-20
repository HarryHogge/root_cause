# FS2-4701: VXE 996 Link Loss on landing

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2026-06-08
- **Updated:** 2026-10-15
- **Resolved:** 2026-08-31
- **Reporter:** Scott Whitney
- **Assignee:** Kurt Burian
- **Creator:** Scott Whitney
- **Links:** relates to VXEP-1903 (VXE 996 Link Loss on landing); relates to FS2-5264 (V996 Follow up - Landing Detect Bug)
- **Sprint:** FS2 Sprint 38

## Description

details in https://jenaero.atlassian.net/browse/VXEP-1903
[embedded: V996_FINAL_REPORT.pdf]
Executive Summary
The V996 incident investigation analyzed two flights where motors failed to shut off after false landing detection. This was NOT a communications hardware failure - the evidence conclusively shows the communication link was functioning, as the FW AP continued transmitting data ("local rx okay"). The root cause was the Fixed-Wing Autopilot CPU becoming blocked and unresponsive ("ap rx bad"), preventing it from processing incoming motor shutoff commands. The false landing was triggered by steady flight conditions (quiet gyro, quiet accelerometer, low GPS velocity) meeting the voting threshold while the laser altimeter was out of range, so no altitude confirmation was required. The XCOMM event log proves the landed-event task started but never reached the FDR capture step, and approximately 100 seconds later link faults were detected when XCOMM noticed the FW AP had stopped responding. All 14 watchdog boot markers found in the FDR files were traced to historical flights stored in the circular buffer - no watchdog reset occurred during the incident. The single WDE warning found was caused by mission upload processing during pre-flight on a previous flight and is unrelated to the incident. Recommended fixes include requiring altitude confirmation for landing detection, adding timeouts to blocking loops in the FW AP serial/SPI code, and implementing heartbeat monitoring between XCOMM and FW AP.
[embedded: V996_FISHBONE_DIAGRAM-20260901-053723.png]


[embedded: V996_FINAL_REPORT.md]
[embedded: V996_LANDING_DETECTION_ANALYSIS-20260901-043245.png]
[embedded: V996_INVESTIGATION_DIAGRAMS-20260901-032652.png]
[embedded: V996_FLIGHT_COMPARISON-20260901-033700.png]

## Comments (1)

### Kurt Burian, 2026-08-31

Created some scripts to generate plots. See file attached and summary above.

## Attachments (6)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [V996_FINAL_REPORT.md](attachments/64376_V996_FINAL_REPORT.md.md) | text | 40 | 2026-08-31 | converted |
| V996_FISHBONE_DIAGRAM-20260901-053723.png | image | 176 | 2026-08-31 | listed only |
| V996_FLIGHT_COMPARISON-20260901-033700.png | image | 199 | 2026-08-31 | listed only |
| V996_INVESTIGATION_DIAGRAMS-20260901-032652.png | image | 135 | 2026-08-31 | listed only |
| V996_LANDING_DETECTION_ANALYSIS-20260901-043245.png | image | 291 | 2026-08-31 | listed only |
| [V996_FINAL_REPORT.pdf](attachments/64382_V996_FINAL_REPORT.pdf.md) | pdf | 235 | 2026-09-01 | converted |
