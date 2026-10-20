# VXEP-389: Develop Replacement for Troublesome/Non Mil-Stnd Board Mount/PCB Connectors

- **Issue type:** Initiative
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Medium
- **Created:** 2023-12-07
- **Updated:** 2026-03-30
- **Resolved:** 2026-03-30
- **Reporter:** Cameron Chapman
- **Assignee:** Abel J. Markow
- **Creator:** Cameron Chapman
- **Parent:** SP-206 Improve Power Connector, Contacts, and Signal Connectors
- **Links:** relates to VXEP-232 (Overheating Battery/Cable (Fuel Cell Support Kit SCO Test Config) -); relates to VXEP-391 (Develop Replacement for cable Signal Connectors); relates to XKIT-3487 (Design SB40 Center Wing Distribution Board (Ethernet plus power switching))
- **Other Stakeholder (as required):** Connor Peebles

## Description

See here for latest recommendations: EE Design Guides.xlsx
We probably want to have multiple optons. Ex: smallest, default, power, etc. 
Need to have
- Crimp contacts. (no glue on VXE2024?) or easy repeatable install, like IDC.
- Locking hardware
- Various current ratings.
- May want shield connections for each connector (discuss with Cam).

Nice to have
- Ribbon cable. Minimize mfg time.
- Ribbon to wire option where needing to connect to an existing wired connector.
- Able to outsource easily.
- options for sealed (JST, Hirose DFW, micro-d, others?)

Ideas
- Harwin (see below)
- https://www.molex.com/en-us/products/connectors/wire-to-board-connectors/pico-lock-connectors
- Ribbon cables.
- Flex PCBs

Electrical Engineering (@Cameron Chapman @Adrian Garcia @Connor Peebles @Garrett O'Neill @Hayden Jeanor @Jeremy Kostel @Laszlo Juhasz @Madeleine Masiello @Mark Squillante @Maxime Jeanneau @Nadia Brown @Wesley Lilienthal) @Ryan Ferguson @Liam Limon 
Process
- Start design guide in confluence or similar.
- Identify currently used options, ones to consider, tradeoffs, etc.
- Down select.
- Purchase and evaluate best options.
- Update design guide. Primary selections for different applications (ex: right angle, most compact, higher current rating, etc).

## Comments (14)

### Connor Peebles, 2023-12-07

one thing to note down; We have to glue down the DF13’s because the DF13 terminals are not ‘Mil-spec’ and thus don’t crimp well with our ‘Mil-spec’ PTFE Wire. So, when evaluating crimps obviously look for that meshing.

### Connor Peebles, 2023-12-14

I changed this issue type to initiative and put it under the marquee of [VA-1004] Improve Power Connector, Contacts, and Signal Connectors - VXE2024 - Jira (atlassian.net)

### Liam Limon, 2023-12-17

@Connor Peebles @Cameron Chapman can I recommend we identify the Milspec or J-std or SAE identifier (such as SAE AS-39029 which encompasses the D369 contacts that we use). That would point us to qualified connectors that are rated for the use cases we are looking for. These specs will tell use the tooling, contacts, and housing that will all work together for the different use cases. 39029 is for crimped circular contacts, but there are others for board headers and that type of thing. The thing we need to identify is which spec incorporates the type of connector that will work for our use case and require the minimal amount of engineering effort to implement.

### Cameron Chapman, 2024-10-17

@Liam Limon yes, but those may be much bigger than many of our ideal PCB connectors. Those may be better options for cable/panel mount connectors https://jenaero.atlassian.net/browse/VXEP-391 
Recommendations for specific part numbers or series for each type are welcome.

### Cameron Chapman, 2025-02-25

@Connor Peebles @Liam Limon what are your thoughts on harwin connectors? Better or worse than Df13s? Any alternate recommendations? We need to select some for the havoc distribution board in the center wing.

### Connor Peebles, 2025-02-25

@Cameron Chapman Harwin has higher density, current capacity, better isolation, and somewhat better retention. DF13s are cheaper, more procurable, and easier to crimp.
Crimping the contacts is not as production friendly as DF13’s, but we have been using the pre-terminated Harwins, which internal production seems to like. The wires on the pre-terminated are not as sturdy as our standard wire so I wouldn’t use them somewhere that gets repeated bending during customer use.

### Cameron Chapman, 2025-02-25

Thanks @Connor Peebles I added those comments to the design guide.

### Liam Limon, 2025-02-25

@Cameron Chapman are you referring to Harwin M22’s or the Harwin Gecko’s. Crimping the Gecko’s is not viable for doing in production which is why we’ve been buying the pre terminated Harwin assebmlies. Working with the pre-terminated ones is pretty easy and like Connor pointed out they have better properties than the DF13’s. What types of signals is the Distribution board carrying, where is it going, and how often will connectors be connected to it? I think knowing those answers would help to pick the best option possible.

### Cameron Chapman, 2025-02-25

@Liam Limon We are trying to build a basic design guide for when we should select specific connectors, so any recommendations are welcome. 
In this case, I was referring to Geckos. Have we used M22s? Where, and how would you compare them to other options. 
For the CW board, it would be carrying payload power and 100mbps ethernet. Hopefully not often (like our AP int board). 
See here and the havoc diagram. https://jenaero.atlassian.net/browse/XKIT-3487

### Cameron Chapman, 2025-02-26

@Connor Peebles @Liam Limon AA has been using these recently on their BMS boards. Do you think they look like a decent option for us to try? I have not compared sizing and specs yet.https://www.molex.com/en-us/products/connectors/wire-to-board-connectors/pico-lock-connectors

### Liam Limon, 2025-02-27

@Cameron Chapman I like the look of those Pico-Lock connectors. They look very similar to picoblades. In response to your other questions we’re using the M22’s just for the reset pins on the MCM and I do not think they’d be good for this use case. They’re like a tiny c-grid. If you’re just carrying payload power, GPIO, and Ethernet then I think the pico locks are a good candidate. I think that would be preferable over Harwins because we would be able to manufacture them ourselves instead of having to buy pre-terminated connectors. Would they need to be weathersealed? The Harwins are potted at the back. The Pico Locks could probably be sealed at the rear of the housing with E-20 if necessary.

### Cameron Chapman, 2025-02-27

Thanks @Liam Limon. Like Gecko and DF13s, we would not use these in a sealed location. I think the Harwins are potted more for isolating the wires from each other and strain relief rather than sealing. Sealing would require a gasket or similar on the front side of the connector as well.

### Cameron Chapman, 2025-03-19

@Jason Colbourne is recommending these for the dist board. Could be a good option in the future. I have not reviewed yet. Thoughts? https://www.molex.com/en-us/products/connectors/wire-to-board-connectors/clik-mate-connectors  @Connor Peebles @Liam Limon

### Liam Limon, 2025-03-31

Currently selected for prototype boards for the Power Relay board of the Distribution board assembly for Havoc DuraClik Connectors | Molex

## Attachments (0)
