# VXEP-1528: Implement Req/Resp Protocol FW-AP <=> Dropper <=> GCS

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2025-10-06
- **Updated:** 2026-01-07
- **Resolved:** 2026-01-07
- **Reporter:** Tobi Ogunro
- **Assignee:** John Clark
- **Creator:** Tobi Ogunro
- **Parent:** VXEP-1190 Software - Wing Utility Pylon (FKA drop payload)
- **Epic Link:** VXEP-1190
- **Other Stakeholder (as required):** Ted Trowbridge

## Description

Develop and implement a deterministic Request/Response protocol between FW-AP, Pylon Dropper, and GCS to eliminate data loss observed in legacy serial and Ethernet implementations.
This replaces ad-hoc polling with a structured message exchange model.

## Plan

Deliverables / Action Items:
Define Req/Resp message flow and timing sequence.Implement protocol handlers in FW-AP and Dropper firmware.Validate recovery from packet loss and ensure synchronization across all devices.Conduct bench test logging for packet continuity and latency.

## Comments (0)

## Attachments (0)
