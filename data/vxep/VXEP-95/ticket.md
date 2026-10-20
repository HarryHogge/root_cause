# VXEP-95: Rate30: PCB Production Improvement Batch 2

- **Issue type:** Major Project
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** High
- **Created:** 2023-02-24
- **Updated:** 2026-02-07
- **Resolved:** 2025-02-05
- **Due:** 2023-08-15
- **Reporter:** Former user
- **Assignee:** Cameron Chapman
- **Creator:** Former user
- **Labels:** Rate#
- **Parent:** ENG-368 IRAD: Optimize VXE Production
- **Links:** relates to ENG-92 (PCB Production Improvement Batch 1); relates to VXEP-97 (PCB Production Improvement Batch 3); relates to ENG-626 (PCB Production Improvement Batch 4); relates to ENG-627 (PCB Production Improvement Batch 5); relates to VXEP-96 (PCBs that need updating, but are obsolete or being obsoleted); blocks ENGPRJA-17 (Create Processed BOMs for all PCBs); relates to ENGPRJA-141 (1905P01B-1 & 1905P01B-2 Alternate Request); relates to VA-127 (Create outline and steps and hand off document updates to Belcan)
- **Start date:** 2022-12-19
- **Target end:** 2023-11-30
- **Production Stakeholder:** Emalee Johnson
- **Supply Chain Stakeholder:** Mike Jercich
- **Other Stakeholder (as required):** Marc Richardson

## Description

Weekly ppt update: Improvement Project Proposal - PCB outsource.pptx
This is Batch #2 of our effort to productionize PCBs. This batch is intended to cover:
Per Victor, We need to order everything now – since we need to be 12 months ahead! 5/24/2023 → PO for this first production order is PO# 230501-10

Order status (see child issues for more specific details):
| P/N | Name | Assigned | First Articles (Coated) | Production Order (Coated) | Current Status: Updated 11/8/23 | Production Priority |
| 1607P01A | XE240 Block 25 Power Comms & NHA | SUPPLY CHAIN | Waiting on CC FAs to arrive; ETA NOV 9th | Attempting to Pull in to January | (QTY 500) WAITING ON FA | High (shortage) |
| 1702P01B | Battery Protection Board | RECEIVING QA | CC boards arrived, waiting in receiving (shipping quantity dispute) | In receiving QA | Will stay w/ Advanced Circuits. Docs Updated, ordering from Advanced Circuits w/ CC. – FAs need approval | Med |
| 1710P01A | Mag Accel PCBA | SUPPLY CHAIN | Waiting on CC FAs to arrive; ETA NOV 9th |  | (QTY 500) board on order WAITING ON FA | Low |
| 1901P01B | AP VTOL Interface Board | SUPPLY CHAIN | CC FAs arrived 10/1 – approved 10/6 | JAN 25th | (QTY 500) CC board on order, in receiving - MassPro on the way | High (Huge time saver) |
| 1902P01E | VXE FOC-ESC | RECEIVING QA | FAs arrived 10/1 – needs approval (separate from NHA) |  | (QTY 500) Docs updated, but we will order the NHA from SPM - FAs need approval | High (Huge time saver) |
| 107-105730 | Processed VXE FOC-ESC Board | SUPPLY CHAIN | NHA Docs sent, waiting on FAs to arrive – no ETA yet |  | Orders for 1902P01E will fold into this NHA order at SPM – WAITING ON FA | High (Huge time saver) |
| 1904A01A | VTOL2 Current Sense Board & NHA | Connor Assigned - Not started yet | ETA NOV 9th (separate from NHA) |  | (QTY 500) board on order with no CC, working on updating docs | Med |
| Needs new PN to separate CC from harness | Processed VTOL2 Current Sense Board | Nadia Assigned – Not started yet | Need documents to complete order |  | Orders for 1904A01A will fold into this NHA order at SPM | Med |
| 0002P01G | PCBA, XE Autopilot | RECEIVING QA | Verify chip issue resolved, no coated articles yet |  | Need to verify chip issue is resolved, then proceed with conformal coating from board house.  QTY 42 coming from Sierra (no CC) with long baked chips. ETA 11/6. ARRIVED 11/8 See Green AP chip issue for more | High |
| 1409P01D | VTOL Autopilot Board | Supply Chain – Mike J. | Updated Docs sent, waiting for FAs to arrive; ETA NOV 27 |  | Updated docs sent | High (Huge time saver) |

Board QTY wise, we have enough stock going into 2024.

## Comments (30)

### Connor Peebles, 2023-03-08

@Former user Could we move 1607P01A from Batch 3 to Batch 2? Procurement is desperate to start the transfer process for that board.

### Connor Peebles, 2023-03-15

@Former user See cheat sheet added for targeted boards in this batch

### Connor Peebles, 2023-03-16

sent estimated timeframes to Tan Poh Li 
EAU = estimated annual usage, FA = first article, MP = manufacturing production
| Part Number | EAU | Qty Per Order | Request Date for FA | Request Date for MP |
| 1607P01A | 360 | 200 | June 1st 2023 | August 1st 2023 |
| 1702P01B | 1,080 | 600 | June 1st 2023 | August 1st 2023 |
| 1710P01A | 360 | 200 | June 1st 2023 | August 1st 2023 |
| 1901P01B | 360 | 200 | June 1st 2023 | August 1st 2023 |
| 1902P01E | 360 | 200 | June 1st 2023 | August 1st 2023 |
| 1904A01A | 360 | 200 | June 1st 2023 | August 1st 2023 |

@Former user @Victor Vandor let me know if these dates do not work and we can correct them as we progress with this batch with SPM

[embedded: RE RFQ for a new board 1710P01A.msg]

### Connor Peebles, 2023-03-22

overall progress update:
For all of the boards in this batch, current (old) Jennings Aero format order documents have been sent to SPM for a quote and so they can start sourcing parts.
Moving onto to creating new relevant or updated documents for conformal coat and/or NHA documents

### Cameron Chapman, 2023-05-24

@Connor Peebles , can you please update the order status here. See notes in the weekly ppt.

### Cameron Chapman, 2023-05-24

Thanks Connor for the update. Please add additional info to the table. 
Update to indicate states: first article has been ordered, received, approved, production ordered, received, approved. Coated or not for each.

### Cameron Chapman, 2023-06-06

Next step, Connor to create outline and steps to enable handing off document updates to Belcan.

### Cameron Chapman, 2023-06-19

@Madeleine Masiello , please meet with @Connor Peebles to start working on this project. Also @Nadia Brown if you have bandwidth. Depending on our bandwidth, we will probably involve Belcan as well.

### Nadia Brown, 2023-06-19

Alright, that should be no problem. @Cameron Chapman

### Greg Fryer, 2023-06-27

@Connor Peebles @Cameron Chapman Can you confirm we left the FW (Green) AP board out of the batches, since we thought we were obsoleting it? We still are, but it will last longer due to TIQUILA. Please put it in the soonest batch you can, because of the corosion issues the shop is having as part of masking for conformal coat.
Open to discussion!

### Connor Peebles, 2023-06-27

@Greg Fryer Confirmed that is what we did. see [ENG-628] Obsolete or being obsoleted - Jira (atlassian.net). We will throw it in the highest priority. Please tell the e-shop to stop using the supposedly corrosive masking agent (I’m sure they have but I’m putting it here anyway!).

### Cameron Chapman, 2023-06-28

@Kelly J Furlong @Liam Limon@Ben Hansen @Ryan Ferguson  please see Connor’s comment below.

### Cameron Chapman, 2023-06-28

@Connor Peebles added 0002P01G	PCBA, XE AUTOPILOT to this batch. Please add order status and add to weekly slides. Thank you. Is there a non-corrosive masking agent option in the short term?

### Connor Peebles, 2023-06-28

@Cameron Chapman This corrosion that we are seeing is only on the GPS connector pins of the Green AP, and on those only a few not all of them. I am not entirely convinced it is the masking material that is causing the corrosion/oxidation as we never had this problem before with any of the other contacts that touched the masking material. Looking more into the material of that specific connector, substitute, and masking right now.

### Connor Peebles, 2023-06-28

@Cameron Chapman Repasting from NCR 1142: 'This is my hypothesis: The tin & bismuth that is on the connector leads is mixing with the leaded solder to create a really low temp solder of SnPbBi + Ag. We may be able to confirm this by attempting to reflow the solder joints at as low as 90C as that, maybe a bit higher because of the Ag plating - but much lower than should be flowing at. They may be wetting abit during burn-in and that is why we see the oxidation “after applying conformal coat”. I am ordering some of these https://www.digikey.com/en/products/detail/gct/FFC3B11-08-T/10656947 to prototype as a drop in replacement and see if further ‘corrosion' occurs’

### Ryan Stafford, 2023-08-15

@Connor Peebles @Mike Jercich can we get an update on this effort in terms of expected delivery date of PCBs we’ve placed orders for? Specifically the ones we’ll be getting with the conformal coating applied.

### Connor Peebles, 2023-08-15

From the latest weekly meeting w/ SPM:

[embedded: image-20230816-015208.png]
[embedded: image-20230816-015243.png]
[embedded: image-20230816-015311.png]
@Ryan Stafford These are contingent on if we get them the documentation they need in time, so they may change. @Mike Jercich Is working on if we can expedite ones that we’ve already given them necessary documentation for. I’ll update the Improvement Project Proposal - PCB outsource.pptx tomorrow

### Ryan Stafford, 2023-08-16

@Connor Peebles @Mike Jercich thanks, there are four boards that look like we received first articles. Are we waiting on someone to inspect those? All the boards with first articles estimated in sep-nov , are those ordered already?

### Mike Jercich, 2023-08-16

@Ryan Stafford Yes, all the boards on this schedule are on order currently.

### Ryan Stafford, 2023-08-16

@Mike Jercich Any way to pull these in? Is the vendor waiting on us for anything?

### Connor Peebles, 2023-08-16

@Ryan Stafford To answer your first question they’re waiting on me to inspect them, which will be done before this week is over

### Mike Jercich, 2023-08-16

@Ryan Stafford As Connor said, they are waiting on FAI inspection but as soon as that is ready I will ask them for an updated ETA. I believe the actual delivery dates can be moved up, Jan 1 was an estimate when the orders were placed early this year.

### Cameron Chapman, 2023-08-24

Linking subtasks to parent

### Greg Fryer, 2023-09-19

Moved to VXEP board where projects and problems go. Epics and Tasks remain in VA where they already are.

### Cameron Chapman, 2023-09-21

@Connor Peebles , @Ryan Stafford and production would like to start making progress on these again. Can you please review and update the statuses.  Ex:This is the only remaining task for this board https://jenaero.atlassian.net/browse/VA-195 If it has been ordered, please add a delivery date. If not, or if we don;t have a date, please comment accordingly, and assign to procurement. 
@Greg Fryer can we put some of these into the current sprint? @Nadia Brown should be available for some of these. After that, we would be pulling people off other high priority incidents and projects.

### Connor Peebles, 2023-09-21

@Cameron Chapman Steady progress has been made on these, see recent ECN’s.
- I’ve been updating the individual Jiras and been forgoing majorly updating the spreadsheets (3 different places to update after every action seems excessive), but I’ll continue updating as had been before (the summary spreadsheet and Jira projects).
- I will update any delivery dates.
- People outside of engineering don’t generally check Jira when Jiras are assigned to them. This becomes a blocker until I recognize later that their task was done and I close it.
- Nadia help will be greatly appreciated with the [VA-173] 1902P01E VXE FOC-ESC & NHA (107-105730) - Jira (atlassian.net) and [VA-168] 1904A01A VTOL2 Current Sense Board & NHA (PN Creation Needed) - Jira (atlassian.net) updating.
- After that and all the FA’s are received, this project is getting close to done.

### Greg Fryer, 2023-10-04

@Cameron Chapman Per discussion I reassigned this project to you. If you want to discuss, ping me.

### Cameron Chapman, 2023-10-05

@Greg Fryer I see you have Nadia allocated 100% to your upcoming sprint. Can she work on these updates? She is the only one available without impacting other urgent projects (Connor incidents, Hayden+Jeremy Xkit, Adrian-incidents+as150). We may be able to get some time from Adrian and Jeremy too.  
FYI @Connor Peebles

### Connor Peebles, 2023-10-05

@Greg Fryer Nadia has been very valuable for this project

### Greg Fryer, 2023-10-05

@Cameron Chapman@Connor Peebles I think that Nadia allocation is just a carry over from last period, please edit appropriately. I will need some amount of her time to address electrical drawing updates for production. So please leave me some!

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [PCB Production Improvement Batch 2 cheat sheet.pdf](attachments/13085_PCB%20Production%20Improvement%20Batch%202%20cheat%20sheet.pdf.md) | pdf | 9142 | 2023-03-15 | converted |
| [RE RFQ for a new board 1710P01A.msg](attachments/13132_RE%20RFQ%20for%20a%20new%20board%201710P01A.msg.md) | msg | 212 | 2023-03-16 | converted |
| image-20230816-015208.png | image | 274 | 2023-08-15 | listed only |
| image-20230816-015243.png | image | 251 | 2023-08-15 | listed only |
| image-20230816-015311.png | image | 131 | 2023-08-15 | listed only |
