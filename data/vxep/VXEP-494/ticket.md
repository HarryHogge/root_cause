# VXEP-494: Find out the burn-in profile

- **Issue type:** Sub-task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-04-10
- **Updated:** 2024-07-10
- **Resolved:** 2023-04-28
- **Reporter:** Connor Peebles
- **Assignee:** Ryan Ferguson
- **Creator:** Connor Peebles
- **Parent:** VXEP-484 0002P01G Green Autopilot Reliability Issues/Fallout Study
- **Links:** relates to VXEP-484 (0002P01G Green Autopilot Reliability Issues/Fallout Study)

## Description

What is the temperature and time profile of the burn-in?

## Comments (13)

### Ryan Ferguson, 2023-04-10

This is documented in the autopilot Burn-In Procedure, document # 110644.  Please see the below chart for the relevant info from that procedure:
[embedded file]

### Connor Peebles, 2023-04-10

easy task

### Connor Peebles, 2023-04-10

Initial impressions are that I would want to add another soak at 100C for awhile on the way up…

### Connor Peebles, 2023-04-10

https://resources.system-analysis.cadence.com/blog/msa2020-conduct-burn-in-testing-in-semiconductor-devices-to-ensure-reliability

### Connor Peebles, 2023-04-10

@Ryan Ferguson Would you agree that the burn-in we apply is a static burn-in? We simply power up the boards and do not apply input stimuli that isn’t part of the board’s power up sequence.

### Connor Peebles, 2023-04-10

Cannot change code during powered up, calibration and burn-in are the same?

### Connor Peebles, 2023-04-10

@Ryan Ferguson @John Clark Can we look into reasonings and re-workability of the burn-in process? 
Consider cooking w/out power
Consider lowering burn-in temp
Consider changing, looking into the necessity of calibration

### Connor Peebles, 2023-04-11

Update, the burn-in only goes to 65C, not 165C

### Cameron Chapman, 2023-04-27

@Maxime Jeanneau

### Ryan Ferguson, 2023-04-28

Reopening so I can attach updated burn-in profile graphs

### Ryan Ferguson, 2023-04-28

I have updated the graphs in the burn-in procedure with the correct temperatures and checked them back in to the Vault.  The updated profiles can be seen in the attachment list above.
@Maxime Jeanneau FYI.
Marking this closed now that all work in this ticket is complete.  If further work is required we’ll reopen this ticket again.

### Maxime Jeanneau, 2023-04-28

@Ryan Ferguson can you please post the file location or vault part number for the original file?

### Maxime Jeanneau, 2023-04-28

File information: 965-1-01-2004, document number 110644

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20230410-171409.png | image | 140 | 2023-04-10 | listed only |
| Green AP burn-in profile.PNG | image | 123 | 2023-04-28 | listed only |
