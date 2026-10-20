# VXEP-648: Increase VXE30 HLB lifespan

- **Issue type:** Major Project
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Medium
- **Created:** 2024-09-20
- **Updated:** 2026-03-30
- **Resolved:** 2026-03-30
- **Reporter:** Cameron Chapman
- **Assignee:** Tom Westrich
- **Creator:** Cameron Chapman

## Description

Idea for a project to save a lot of money for our customers and work for us: 
Now that we have cell voltage monitor of the HLB cells, we could extend the lifespan. Possibly from 50 to ~100 cycles.  
- Using cell voltages, SOC, and current, calculate SOH of each cell. 
- Determine minimum SOH to operate in worst case scenario.
- Abort launch if a battery cell is performing below minimum limits.
- Have aircraft notify GCS and operator when a battery is approaching the end of its life.
- Ensure a battery past the end of its life will not launch.

## Comments (0)

## Attachments (0)
