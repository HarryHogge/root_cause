# VXEP-616: Obsolete 1502P01 rev C . mark it as obsolete in the vault, on the PCBA sheet, and consider purging inventory

- **Issue type:** Epic
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2024-09-06
- **Updated:** 2025-11-14
- **Resolved:** 2025-11-14
- **Reporter:** Cameron Chapman
- **Assignee:** Scott Stuckey
- **Creator:** Cameron Chapman
- **Parent:** VXEP-266 VXE (all) ADP: Heated Pitot/New SA CAM/Remove other obsolete components
- **Links:** is cloned by XKIT-2881 (Obsolete rev C of air data board or evaluate if it can be updated to 1Mbps CAN.)
- **Epic Status:** To Do
- **Epic Color:** ghx-label-6
- **Issue color:** green
- **Supply Chain Stakeholder:** Perry Richardson
- **Other Stakeholder (as required):** Catherine Wagner
- **Issue Status:** Inventory purged of 1502P01C boards
- **Job Number:** J100078 - Sustainment: VXE-30

## Description

Improves the reliability/reduces risk of operating with MAGNSS. Coordinate with @Ryan Babigian how to link these efforts. We should also determine if it is worth it to retrofit/reprogram existing rev C ADBs during RMA or other action.

## Plan

- Ask Procurement & Production on their status of the Air Data Boards
- Confirm obsolescence of Rev C will not cause supply problems
- Obsolete files in Vault

## Comments (5)

### Connor Peebles, 2024-09-06

@Perry Richardson We want to obsolete the 1502P01C boards and only continue with the 1502P01D boards. 
1502P01C uses the chip DSPIC30F6015-30I/PT
1502P01D uses the chip DSPIC30F6014-30I/PF

These chips are shared with some of the 2005P01A, 2005P02A, 2005P03B battery boards.
2005P01A uses the chip DSPIC30F6014-30I/PF
2005P02A uses the chip DSPIC30F6014A-30I/PF
2005P03B  uses the chip DSPIC30F6015-30I/PT
@Perry Richardson Can you review our supply of those chips and give an OKAY as to if it will be okay to obsolete 1502P01C at this time? FYSA @Emalee Johnson @Luca Lauritzen

### Perry Richardson, 2024-09-06

There are only 10 pcs left in stock. Having REV C. boards purged from stock.

### Perry Richardson, 2024-09-06

Rev C. 1501P01C boards have been purged. For tracking purposes asked catherine to create an NCR for these boards. Then we will have them scrapped.

### Connor Peebles, 2024-09-09

@Perry Richardson I suppose it is Ann Arbor that has to worry about the 2005P01/2A/3B battery boards now. I just wanted to make sure we aren’t competing with ourselves for chip stocks.

### Perry Richardson, 2024-09-09

I Agree. Right now, we have enough built 1502P01D’s in stock to cover demand until April-May 2025 with 1400 pcs of the DSPIC30F6015-30I/PT available.  
DSPIC30F6014-30I/PF for the 2005P01A              3351 pcs in stock. 
DSPIC30F6014A-30I/PF for the 2005P02A           4854 pcs in stock

## Attachments (0)
