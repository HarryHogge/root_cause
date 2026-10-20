# VXEP-372: Consider removing I2C comms from AIRCRAFT STATE LED / DISABLE BUTTON (107-102262)

- **Issue type:** Improvement
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2024-01-18
- **Updated:** 2025-04-25
- **Resolved:** 2025-04-25
- **Reporter:** Travis Storm
- **Creator:** Travis Storm
- **Issue color:** purple

## Description

AIRCRAFT STATE LED / DISABLE BUTTON (P/N 107-102262) appears to have a serial I2C comms line connected to the VTOL AP, but this data may be unused. This adds unnecessary serial traffic & processing requirements. Investigate to confirm if this data stream exists, and if so, consider removal.

## Comments (2)

### Christa Meck, 2024-04-18

@Greg Fryer What issue type should this be?  Not feeling like a Jira/Process Improvement.

### Christa Meck, 2025-03-05

@Greg Fryer Do you know if this still needs to be addressed?  I know Travis is no longer with the company.

## Attachments (0)
