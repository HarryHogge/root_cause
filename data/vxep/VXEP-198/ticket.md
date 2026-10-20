# VXEP-198: VXE450 Implement CA: Procurement Evaluate/Order new datecode FDMS86540 MOSFETs (IPN: 100-110341)

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-11-21
- **Updated:** 2025-11-10
- **Resolved:** 2025-08-08
- **Reporter:** Connor Peebles
- **Assignee:** Christa Meck
- **Creator:** Connor Peebles
- **Fix versions:** 11/10/2025
- **Links:** blocks VXEP-51 (Internal - Aircraft 450 VTOL Landing Crash - ESC soft start); relates to VXEP-272 (VXE-425 Crash on VTOL landing-ESC Damage); relates to VXEP-384 (VXE 545 Commanded aborted launch due to unusual behavior on ascent)

## Description

The FETs are available and active, see here: https://www.onsemi.com/products/discrete-power-modules/mosfets/FDMS86540
- We have ~1,400 boards-worth of them in our stock now. (we would be effectively scrapping that many?)
- I recall Procurement had some trouble with this chip, don’t recall the trouble. Probably Chip Shortage related.
- It is probably worth it to have procurement contact Onsemi directly and ask for newest datecode chips, and get procurement's past perspective on these.

## Comments (8)

### Connor Peebles, 2023-11-21

@Mike Jercich @Victor Vandor Victor, I recall we had ordering trouble with these chips for the 1711 boards. Now we have quite a few in stock.
- Did we order these from a reputable source recently?
- Could you check with Onsemi directly and see if we can order with newest possible datecodes?
- SPM mentioned that the datecodes were old, I believe we consigned them for the most part, correct?

Please respond to these questions and the give perspective to the ones in the description as well.
Thanks!

### Cameron Chapman, 2023-11-21

@Connor Peebles responding to the message below in bold. 
- The FETs are available and active, see here: https://www.onsemi.com/products/discrete-power-modules/mosfets/FDMS86540
- We have ~1,400 boards-worth of them in our stock now. (we would be effectively scrapping that many?) No, I don’t think we should scrap them. You mentioned the old date codes in the ppt. How old? Do you think soldering or other related issues could be caught with close attention? If not, how hard are these components to remove?

### Connor Peebles, 2023-11-22

@Cameron Chapman 
- “You mentioned the old date codes in the ppt. How old?
- Most of the date codes are “1809” or so, which is 2018, Week 9. 5 years old.
- Do you think soldering or other related issues could be caught with close attention? 
- Yes, see the Inspection Sheet Quality made as a CA for this incident.
- If not, how hard are these components to remove?“
- Very hard

### Mark Squillante, 2024-09-17

@Connor Peebles I see this issue has been around for a while and is currently assigned to Victor Vandor. Should it get assigned to someone else perhaps?

### Connor Peebles, 2024-09-17

@Mark Squillante Yeah, probably. We should re-evaluate where we stand with these components today though, as perhaps there was procurement action on this but it just wasn’t recorded here

### Perry Richardson, 2025-08-08

@Christa Meck Nothing to add here. This as Cameron said an active part and there is plenty of stock out there with distributors to last awhile. There is currently no EOL or LTB notice for this part.

### Christa Meck, 2025-08-08

Cool.  Thank you everyone for taking a moment to double check this item with current state.
The issue has been remediated via an Inspection Sheet Quality made as a CA for this incident.
Closing this item.

### Perry Richardson, 2025-08-08

If you need anything else on this please let me know.
[A picture containing icon  Description automatically generated]
Perry Richardson
Procurement Specialist III
Edge Autonomy - San Luis Obispo, CA
Phone: +1-805-592-1163 x123
Email : prichardson@edgeautonomy.io
831 Buckley Road, San Luis Obispo, CA 93401

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image001.png | image | 9 | 2025-08-08 | listed only |
