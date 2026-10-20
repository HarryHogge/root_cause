# VXEP-1583: EC: SB40 ADB without CAN resistor 2122481-02 cut over to VXE30

- **Issue type:** Engineering Change
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2025-10-29
- **Updated:** 2026-02-11
- **Resolved:** 2026-02-11
- **Reporter:** Nina Menon
- **Assignee:** Brendan Palmer
- **Creator:** Christa Meck
- **Parent:** VXEP-1552 SB40 ADB without CAN resistor 2122481-02 cut over to VXE30
- **Links:** relates to JA-853 (Release drawings from 10/30 CCB); relates to VA-2879 (2121756-02 Replaces 2121756-01 in Spares Package (107-103277) and 35X CW (2121856-01))
- **Epic Link:** VXEP-1552
- **Engineering Change Level:** Level 1 - Scope of change is clear but there is a choice of approaches
- **Link to Engineering Change Notice (ECN):** ECN #240 UPDATE ADB - NO CAN RESISTOR.xlsx

## Description

See Confluence for instructions and templates: https://jenaero.atlassian.net/l/cp/ztB58xvi 
Full details are in the parent epic https://jenaero.atlassian.net/browse/VXEP-1552 

Production will run out of Air Data Boards 2122839-01 in the next week and were directed to not order more, as VXE30 will begin using a standard board without the CAN resistor, 2122839-02.
Drawing Status:
:check_mark: 2122839-02 Air Data Board, CAN: Order files released, Qty 125 set to arrive in Oct, Qty 100 more due in Dec 
:check_mark: 2122481-02 Air Data Board Assembly: Drawing Number 2122481-01 needs to change to 2122481, see redlines 
:check_mark: 2121756-02 Air Data Pod Assembly: Drawing is clearly updated to have -01 and -02 
:check_mark: 107-100455 Centerwing Assembly: Drawing needs to be updated to replace 2121756-01 with 2121756-02

## Comments (11)

### Nina Menon, 2025-10-29

@Grant Goodman @Eric Rinell Christa made this ticket for the ADP change with the CCB flow. can we make an ECN so this can go to CCB tmrw? the cutover will be when production runs out of 2121756-01. (or is there an ECN already?)

### Eric Rinell, 2025-10-29

@Nina Menon @Grant Goodman I made the ECN and linked it above.

### Nina Menon, 2025-10-30

@Eric Rinell thank you!!

### Christa Meck, 2025-10-31

107-100455 drawing + assembly documents released.
2122481 drawing + assembly documents released.

### Trevor Gronner, 2025-10-31

@Catherine Wagner @Sandra Lopez @Kelly J Furlong @Natalie Lusk @Arunita Kashyap @Leslie Cital We are moving from an Air Data Board with a resistor to an Air Data Board with no resistor for VXE30. This will allow us to use the same board for both VXE30 and BLK40. Just a heads up that this is going to be implemented when we run out of the original air data boards.

### Trevor Gronner, 2025-11-03

@Grant Goodman @Eric Rinell Can I get confirmation that 2121756-02 should replace 2121756-01 in all assemblies? I don’t think the VXE30 spares package (107-103277) and the 35X Center Wing (2121856-01) were updated to call out the new -02 ADP. Having said that, I’m assuming we don’t want to have any 2121756-01 in the future. If I get confirmation, I can create a new ECN to track these changes.

### Grant Goodman, 2025-11-03

@Trevor Gronner confirmed that 2121756-02 should replace 2121756-01 in all assemblies.

### Trevor Gronner, 2025-11-03

@Grant Goodman I created https://jenaero.atlassian.net/browse/VA-2879 to capture the changes that still need to be made. I updated the Odoo BOMs at risk to try and avoid having procurement purchasing the -01 version of the air data board. Thanks for the confirmation!

### Trevor Gronner, 2025-11-03

@Brendan Palmer Do you mind helping to coordinate these subtasks? When all the subtasks are complete, please mark the overall ticket as Done.

### Christa Meck, 2026-02-11

@Brendan Palmer What’s the status of sub task https://jenaero.atlassian.net/browse/VXEP-1590  ?  This has been hanging out for a few months.

### Brendan Palmer, 2026-02-11

@Christa Meck Finished the subtask last week. Moving the subtask and this ticket to complete.

## Attachments (0)
