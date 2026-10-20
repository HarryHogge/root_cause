# ENG-2978: VXE 515 XComm Watchdog Triggering

- **Issue type:** Problem
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** High
- **Created:** 2023-06-07
- **Updated:** 2026-04-17
- **Resolved:** 2026-04-17
- **Reporter:** Cameron Chapman
- **Assignee:** John Clark
- **Creator:** Cameron Chapman
- **Links:** relates to VXEP-41 (TPTR-74 VXE 510: (VTOL AP WD) Consolidated Watch Dog tracking); is blocked by FS2-708 (VIT2-309 v515 XCOMM WDT); relates to VA-123 (Modify HIL set 105 to include 515's XCOM, add GPS, magnetometer, ADP, and current sense)

## Description

From NCR-230601 - 1085 https://jenaero.sharepoint.com/sites/JAI_Operations/Lists/NCR%20List/DispForm.aspx?ID=1085 
VXE 515 is having WDT resets. Have not been able to reproduce a cause, but it happens frequently enough to show up in the log. It happened once during flight which caused a loss of comms for ~1 minute.
FDR added for flight with the lost comms.
Vehicle will WDT while sitting idle, no interaction needed to cause reset.

## Comments (9)

### Cameron Chapman, 2023-06-07

@John Clark please report your findings from troubleshooting and what you recommend swapping/further troubleshooting recommendations.

### Cameron Chapman, 2023-06-07

Notes from conversation with John. 
- Does it happen without battery? Don't know. Do know Carson demonstrated without CW plugged in, was able to generate WD without center wing plugged in, but less frequent.
- When cold, reboot happened after a while. When sitting for 2 days, never reset fuselage by itself.

### John Clark, 2023-08-14

@Cameron Chapman is the replaced (failed) avionics box available for use in HIL testing?

### Cameron Chapman, 2023-08-14

@Matt Philley I think we have not received this XCOM. Do you have it or know where it is?

### Matt Philley, 2023-08-14

@Cameron Chapman I have it. Its been hiding at my desk waiting for me to hand it off. I will swing by. It is just the XCOMM only.

### Matt Philley, 2023-08-14

Dropped off to @John Clark

### Cameron Chapman, 2023-08-24

Linking subtasks to parent.

### Christa Meck, 2026-04-17

@Cameron Chapman @John Clark @Matt Philley 
Is this still an item that needs investigation or are we beyond this at this point?

### Matt Philley, 2026-04-17

@Cameron Chapman your call since you are more knowledgeable on current stuff for WDT investigation, but this was from 2023 so I think we could safely close this out given how much is already going on related to WDT investigations if this isnt likely to help the current investigation(s).

## Attachments (0)
