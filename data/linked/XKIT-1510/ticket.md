# XKIT-1510: Troubleshoot Main Power Harness

- **Issue type:** Sub-task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-03-01
- **Updated:** 2024-04-01
- **Resolved:** 2024-03-04
- **Reporter:** Carl Graf
- **Assignee:** Garrett O'Neill
- **Creator:** Carl Graf
- **Parent:** XKIT-1714 Troubleshoot XKIT Issues found in flight testing / Prepare for Demos 2
- **Sprint:** XKIT Sprint 4/13-5/7, XKIT 3/23-4/13

## Description

- Main power harness when plugging in the power
- Could be related to contacts (AMASS, poor contact quality)
- Higher voltage of Xkit may be the difference between VXe30 and Xkit
- This connector has approx 10-15 installations
- Has anti spark resistor in male contact (susceptible to zortching)
- Requires investigation
- Is it asset specific or systemic?
- Want to look at blade-style connectors

## Issue Status

Replaced Fuse Power Harness (P/N: 107-102189-1) in V376 Fuse. Performed mating/de-mating of connector with battery ~10 times - no sparks were observed. Likely, this connector was faulty from the manufacturer and we did not observe sparking until we started using it as an Xkit asset with the higher voltage Battery bus. Will continue to monitor for sparking on Xkit vehicles.

## Comments (3)

### Garrett O'Neill, 2024-03-01

@Carl Graf @Hayden Jeanor Did a resistance check on the positive AS150 terminal of the Fuselage Power Harness, measured ~245 KOhms, should be about 5.6 Ohms. It looks like a very old harness that pre-dates our new quality control tests for the AS150 contacts. I recommend replacement.

### Carl Graf, 2024-03-04

@Hayden Jeanor

### Hayden Jeanor, 2024-03-04

Replaced Fuse Power Harness (P/N: 107-102189-1) in V376 Fuse. Performed mating/de-mating of connector with battery ~10 times - no sparks were observed. Likely, this connector was faulty from the manufacturer and we did not observe sparking until we started using it as an Xkit asset with the higher voltage Battery bus. Will continue to monitor for sparking on Xkit vehicles.

## Attachments (0)
