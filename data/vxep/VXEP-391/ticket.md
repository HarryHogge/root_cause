# VXEP-391: Develop Replacement for cable Signal Connectors

- **Issue type:** Initiative
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Medium
- **Created:** 2023-12-11
- **Updated:** 2026-03-30
- **Resolved:** 2026-03-30
- **Reporter:** Connor Peebles
- **Assignee:** Abel J. Markow
- **Creator:** Connor Peebles
- **Parent:** SP-206 Improve Power Connector, Contacts, and Signal Connectors
- **Links:** relates to XKIT-761 (Evaluate using crimped and locking signal connectors for new X-kit connectors); relates to ENG-2427 (Evaluate alternate connectors for production units); relates to VXEP-389 (Develop Replacement for Troublesome/Non Mil-Stnd Board Mount/PCB Connectors)

## Description

Current trade study sheet Connector Trade Study.xlsx

Objective Requirements
- locking features
- Crimp contacts or pre-wired
- Lighter or similar weight to ODU equivalent.
- Fully mated indicator (Ex lock visible or clicks)
- Stocked or Short lead times.
- Compare prices.

 
See similar effort here https://jenaero.atlassian.net/browse/ENG-2427
Tasks @Garrett O'Neill
- Perform market survey of options
- Glenair mighty mouse https://www.glenair.com/mighty-mouse/index.htm
- Amphenol 2M https://www.amphenol-aerospace.com/products/2m-hermetic#section=documents
- Start requirements spreadsheet and trade study.
- Identify best candidates and review with Cam.
- Review with other stakeholders.

## Comments (5)

### Cameron Chapman, 2024-01-31

@Ryan Ferguson @Liam Limon @Emalee Johnson we are trying to make progress on this, but progress has been slow due to other assignments. Do any of you have bandwidth and/or desire to help with this comparison? The draft comparison is here. https://jenaero.sharepoint.com/:x:/r/sites/IRAD/Shared%20Documents/General/Projects/VXE_CRPA_AntiJam/Architecture,%20Block%20Diagrams,%20Integration/Wire%20Harnesses/Milestone%202%20-%20Retrofit/Connector%20Trade%20Study.xlsx?d=w2b3edfa4f50a454480cc2cf273d953ad&csf=1&web=1&e=1RjNIN 
We could use help with many items, but especially an estimate of the production time, cost, and quality savings of switching to crimped connectors like Mighty Mouse vs ODU AMC.

### Ryan Ferguson, 2024-01-31

@Cameron Chapman I’ve added a couple rows with considerations from Production.  These are whether the connector allows for easy rework, estimated termination touch time, and estimated training time for a brand new tech to start building assemblies with the connector.
I also added an additional row for cycle time.  Every time a connector needs to bounce between Quality and the techs, we introduce a significant amount of time with the part waiting on a shelf.  The cycle time attempts to capture this.  In the case of the Odu connector specified, cycle times are approximately 10 hours per connector since the assembly has to bounce between Quality and the techs no less than 4 times to inspect each row of pins.  Crimp connectors will always be better in this regard since techs can terminate all connectors and have Quality inspect only twice - once after crimping all contacts, and once after fully terminated in the backshell.
Quality of the connector is difficult to pin down since we can only get actionable data once we have significant with two connectors to compare.  I can say from experience however that crimp connectors will almost always be better from a quality standpoint since we can inspect every part of the pin prior to installation and perform a pin retention test to verify the housing is working as expected.  Rework is also extremely easy since techs can simply depin the connector from the housing and swap it to the correct position.
If additional information is required, feel free to ask.  I only compared the Odu connectors and the 801 connector since those are currently our two best candidates to my knowledge.

### Cameron Chapman, 2024-01-31

Thanks @Ryan Ferguson I agree 801 seems like the best candidate. We are evaluating 804 and 803 as well in case stakeholders still want a QD option, or the quick connect of the bayonet.

### Cameron Chapman, 2024-02-01

Thanks @Ryan Ferguson for these estimates. Crimp contacts with gaskets separating the contacts certainly have benefits for inspection, rework, quality (lower shorting risk), etc.
Are you or anyone else able to estimate costs for the following? @Kelly J Furlong @Desiray Johnston 
- New technicians per year here, AA, and HSV (will factor into training hours).
- Is the estimate combined hours for trainee and trainer?
- Cost/hr avg.

### Cameron Chapman, 2024-12-05

Need to evaluate these recommendations from @Abel J. Markow  and organize : 
I can help with this.   Need a limit scope a little.  You do not want twist lock?
 
I have heavily used the LEMO connectors.  They are nice, like the mighty mouse and way less expensive.  We work aroudn their lead times by keeping our own stock.  
 
They are alos increadibly light.
 
And if you use them as a commone connector accross the entire aircraft, it will decreast the size of yoru BOM.
 
They are alos great for CRIMP Shields, and bond well.
 
I beleive they make a PCB and crimp interface type as well as a 90.
 Lemos look nice, but possibly too long for many applications compared to others (from eyeballing rather than detailed comparison) 
Let me get you some part numbers.
 
Many of them are only 1/2 in in length
Some are 3 in in length
And it depends on the backshell selection
https://www.mouser.com/ProductDetail/LEMO/HEP2M308XLNP?qs=BpQ5zMcxL3BnhQrNWNTE2Q%3D%3D&mgh=1&utm_id=17222215321&gad_source=1&gclid=Cj0KCQiAu8W6BhC-ARIsACEQoDCwZ1ugcVInBf9IVOL6zkVtBMIvN4xn2GEvTFwqQ1YMGQWZOaoo2vgaAuuTEALw_wcB 
HEP.2M.308.XLNP LEMO | Mouser
HEP.2M.308.XLNP LEMO Circular Push Pull Connectors datasheet, inventory, & pricing.
 Trying to sort out ideal mechanical and weight vs ideal low side bonding trades. 
 
The mate for the above that I coulf find quickly with the crimp shiel and crimp inserts is .9 in.
 
https://www.lemo.com/pdf/FMP.2M.308.XLC.pdf
 
This exact pari is used on the Apache
 
Another one wiht 30 pins
 
https://www.digikey.com/en/products/detail/lemo/FGN-3M-330-XLCT/3690109?gclsrc=aw.ds&&utm_adgroup=General&utm_source=google&utm_medium=cpc&utm_campaign=PMax%20Shopping_Product_Zombie%20SKUs&utm_term=&utm_content=General&utm_id=go_cmp-17815035045_adg-_ad-__dev-c_ext-_prd-_sig-Cj0KCQiAu8W6BhC-ARIsACEQoDDKD5RtEPQ8Glfk6rkh9whlI8LguG1zkf68v-WcCtT5XSbQfefF5aoaAn8zEALw_wcB&gad_source=1&gclid=Cj0KCQiAu8W6BhC-ARIsACEQoDDKD5RtEPQ8Glfk6rkh9whlI8LguG1zkf68v-WcCtT5XSbQfefF5aoaAn8zEALw_wcB&gclsrc=aw.ds 
 
And its panel mount.  https://www.digikey.com/en/products/detail/lemo/PEN-3M-330-XLMT/3806962?s=N4IgTCBcDaIAoFEByA6AzAWXWgDCgGgDIYAqIAugL5A 
PEN.3M.330.XLMT LEMO | Connectors, Interconnects | DigiKey
Order today, ships today. PEN.3M.330.XLMT – 30 Position Circular Connector Receptacle, Female Sockets Crimp from LEMO. Pricing and Availability on millions of electronic components from Digi-Key El...
 
Great for....say a wing.

## Attachments (0)
