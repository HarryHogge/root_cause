# VXEP-895: Thermal Protection

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2025-01-09
- **Updated:** 2025-05-13
- **Resolved:** 2025-05-13
- **Reporter:** Grant Goodman
- **Assignee:** Grant Goodman
- **Creator:** Grant Goodman
- **Parent:** VXEP-854 SA Camera Pod Proof of Concept ADP
- **Links:** relates to VXEP-917 (Investigate thermal control of Sightline and camera system through ethernet)
- **Epic Link:** VXEP-854

## Description

Determine if thermal protection of the Sightline board itself adequate to protect hardware in the case that mechanical thermal management is not possible at the edge case of extended time on hot runway.
Sightline doc reference thermal management:
https://sightlineapplications.com/wp-content/uploads/ICD-1750-OEM.pdf
Also makes mention of “Low power mode”. If commanded, no video is output for low power consumption:
https://sightlineapplications.com/wp-content/uploads/EAN-Performance-and-Latency.pdf

## Comments (2)

### Grant Goodman, 2025-02-07

From a chat, “Power from the XCOM U5 and Q5 relay.” Not sure which one or both would we cut power to which parts of the ADP.

### Grant Goodman, 2025-02-19

Meeting with Sightline https://jenaero.atlassian.net/wiki/spaces/PDAO/pages/609845253/Thermal+Handling+Meeting+w+Sightline+-+2+10

## Attachments (0)
