# GCS-253: Launch Wizard, surface check, Landing test

- **Issue type:** Bug
- **Status:** Canceled
- **Resolution:** Cannot Reproduce
- **Priority:** Medium
- **Created:** 2020-09-23
- **Updated:** 2024-03-12
- **Resolved:** 2024-02-29
- **Reporter:** Dustin Gamble
- **Assignee:** Dustin Gamble
- **Creator:** Dustin Gamble

## Description

If the landing test is pressed while an alerion is still sweeping then you only see partial spoiler deflection. To work around this you need to wait until the alerion test is complete. To make this cleaner, there might need to be a delay between when the alerion test is pressed and when landing test is sent.

## Comments (5)

### Michael Berger, 2020-09-23

I believe this is fixed wing only.

### Dustin Gamble, 2021-03-01

This issue is related to VXE30 when testing the fixed wing system. The landing test command should be delayed if another other surfaces tests have been command with in xx seconds.

### Michael Berger, 2021-03-01

Not sure what you are referring to “Fixed Wing System”. VXE 30 is only VTOL as I understand it. The issue described refers to not seeing partial spoiler deflection. There are not spoilers on VXE.

### Dustin Gamble, 2021-03-01

VXE30 landing surface test makes the alerions go up and act as spoilers.

### Michael Berger, 2021-03-01

Allowing the user to press a button (Landing test), but not having it do anything would not be a good user interface. 
We could disable the landing test button for a period after any surface test button is clicked.

## Attachments (0)
