# VXEP-761: VXE 557 Smoking Smell from Fuselage after connecting main battery

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-11-01
- **Updated:** 2026-03-02
- **Resolved:** 2025-06-24
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Steve Gonzales
- **Creator:** Alexander Alan Arnold
- **Labels:** AS150, USASOC, Weekly-incident-tracker
- **Links:** relates to VA-573 (Poor Quality/higher impedance plating on AS150 power contacts - Containment and Corrective Action); relates to VXEP-762 (Check if VXE30 checker SOC is accurate for Main Batteries (I suspect no). Update manuals and charger+checker firmware to instruct not to use this feature and remove it if so.  ); relates to VXEP-326 (AS150 pin connectors diagnosing the reason the parts are OOS when assembled (could be pin dimensions, threads too deep, etc).  Identify long term C/CAs and short term workarounds. Ex 107-102189 114-106508); Linked issue cannot finish until this issue finishes. FS2-2521 (Log more data on the GCS in case aircraft is not recovered. ); relates to FS2-2521 (Log more data on the GCS in case aircraft is not recovered. ); relates to RMA-478 (VXE-557 USASOC 250127-1); relates to VXEP-540 (Recent AS150 Connectors causing intermittency and difficulty to connect and disconnect correctly and safely (AS150 Socket Issues)); relates to VXEP-553 (AS150 Plug/Pin Connector Issue Systemic Collector); split to VXEP-1136 (VXE 557 Inaccurate SoC Model Causing Battery State to Fluctuate (OCT 12th Incident) )
- **Customer:** USASOC
- **Vehicle Tail Number:** VXE 557
- **Vehicle Configuration:** Battery Configuration
- **Incident Type:** Aircraft Damage
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

Cam questions/comments in bold. 
 3rd SFG(A) Hagan
@Pat Wells Is this the 12 Oct flight. It was not stated clearly
Why: Unknown at this time. Battery passed all of its pre launch checks. It also passed its battery health check after the flight per the maintenance manual. After conducting a RTB at 32% the aircraft main battery percentage started fluctuating from 16-30% rapidly. This started happening after beginning IP 1 and didn’t end until passing into IP4. The aircraft was landed safely and the VXE software reported 30% main battery life on ground. After letting the battery cool off the main battery charger reported the battery at 12%.  
@Pat Wells please encourage customers to report issues like this ASAP and not fly the same equipment until they receive a response. The SOC on the battery charger is likely based on typical LiPo cells, so is inaccurate for our main battery. I opened a linked CA to correct this.https://jenaero.atlassian.net/browse/VXEP-762 
On 30 October 2024 the 3rd SFG(A) conducted an operational check on aircraft 557. This was the first operational check since the aircraft last flew on 12 October. We made sure to use a different main battery then what flew on the 12 October flight. Three minutes into the aircraft being turned on a strong burning smell came from the inside of the aircraft. After disconnecting and powering down the aircraft we noticed that the main power cable that plugs into the main battery had a corrosive substance on it. While out here we have made sure to pay extra attention to these ports to ensure there has been no carbon buildups and we can verify the port was clean prior to use. I believe this issue is what contributed to the rapid battery fluctuation for the flight on 12 October. 
FOR DATA Gathering: Operator reported incident dates are 12 OCT and 30 OCT. Due to the observed issue on OCT 30 operators were unable to pull data since they had to disconnect Main Battery
Sharepoint : https://jenaero.sharepoint.com/sites/FlightSafety/Shared%20Documents/Forms/AllItems.aspx?csf=1&web=1&e=aFOcRu&CID=097f044e%2Dac51%2D432f%2D96f4%2D90cbb7a76c3e&FolderCTID=0x012000D03119522A011A40817D7F0F59E3A7EF&id=%2Fsites%2FFlightSafety%2FShared%20Documents%2FIncident%20Reports%2FVXEP%2D761%20%2D%20VXE%20557%20Smoking%20Smell%20from%20Fuselage%20after%20connecting%20main%20battery&viewid=7181a7a2%2Dd286%2D47c9%2Dbdd3%2D9195ef18282c 
Investigation Report: VXEP-761 - VXE 557 Smoking Smell from Fuselage after connecting main battery.pptx

## Corrective Action

- https://jenaero.atlassian.net/browse/VXEP-762
- https://jenaero.atlassian.net/browse/FS2-2521
- Implement AS150 anti-spark measurements in Fuse power harness traveler
- Replace Fuselage Power Harness (PN: 107-102189-1 and 107-102189-2)

## Plan

Aircraft Hardware
- Aircraft in SLO. Replace power harness.  Run through production bench checkout after engineering performs HIL test with new harness. (complete by 3/21)
- (3/18/25) Provide advance replacement or otherwise replace customer main batteries that were used with this vehicle, TBD.

Investigation:
- Pull data from aircraft. Save to SharePoint.
- Inspect components for damage.
- Review data.
- Identify C/CA. 
- A likely cause for this issue could be the harness was not fully mated, possibly due to the connector issues recently experienced. Once we have the battery SN, we can see when and where it was made, and if it relates to this issue. https://jenaero.atlassian.net/browse/VXEP-540
- Did they log main battery SN in any of the logs?
- @Jeremy Kostel can you please compare the cell readings pictured to a typical main battery after charging. This could indicate damage. We could also monitor them over time to see if excess self discharge. 
- Cell 6 and 7 seem to be lagging, which could indicate weakness there and thermal damage, but we would have to compare to other batteries and possibly run a discharge test to confirm.
- Measure Anti-spark resistor
- Investigate when and where batteries were manufactured
- (3/18/25) Heat connector AS150 to find if PTC or NTC. (complete by 3/20).
- (3/18/25) Load AS150 to 2A at tip and measure/log voltage with HIL connected for 5 min or until signs of damage.  Take readings with the thermal camera every 20s or as deemed appropriate. (complete by 3/20).
- 3/25/25 Gave to Rodney to replace 2 connectors.  Rodney needs avionics box pending FW of SOC replacement, expected 3/28 .

## Issue Status

Aircraft OCONUS. Recommended grounding aircraft and battery until further notice. Need to confirm.
- Cell 6 and 7 seem to be lagging, which could indicate weakness there and thermal damage, but we would have to compare to other batteries and possibly run a discharge test to confirm.
- A likely cause for this issue could be the harness was not fully mated, possibly due to the connector issues recently experienced. Once we have the battery SN, we can see when and where it was made, and if it relates to this issue. https://jenaero.atlassian.net/browse/VXEP-540
- Nothing unusual has been found in the data involving Oct 12th incident other than low sampling rate and evidence of an inaccurate SoC model. I believe that the two incidents are unrelated and the Oct 12th incident would not have been presented to ENG if the fuselage did not smoke on Oct 30th
- Continuity from Fuse Power GND to the black alden connector GND was not broken
- Battery Info: 
- Both batteries were built in house in SLO - battery data 3-1351 and 3-1353.xlsx
- Main Battery SN : 3-1353 (oct 12th incident) and 3-1351 (oct 30th incident)
- 4/1/25 Has not moved forward; no resources allocated.

Next Steps: 
- Send back to RMA and replace Fuselage Power Harness (PN: 107-102189-1 and 107-102189-2)\
- @Pat Wells @Alexander Alan Arnold Are you able to advise the customer to quarantine the battery that was involved in the OCT 30th incident. The battery SN is 3-1351. The suspected cause of the incident is an unmated connection and may be a cause of out of spec sockets on the battery side. Can we get it sent back for testing?
- Create new incident - one tied to the oct 12th incident and another tied to the oct 30th

## Root Cause

- Poor Mating caused the incident OCT 30th 
- Melted anti-spark is a clear indication that a bad mate was made on the main battery. 
- When inserting the anti-spark pin into the socket the initial mate sees 6ohm to limit the inrush current and then once fully mated the connection should be around 2mohms. If the connection isn't completed quickly (i.e., the main contact isn't engaged in time), the small anti-spark contact may carry too much current for too long, causing it to overheat and melt.

## Comments (57)

### Jeremy White, 2025-03-05

@Adrian Garcia Thanks for the update. What is a typical or goal for RMA turn-arounds?

### Adrian Garcia, 2025-03-05

@Jeremy White I try my best to get them out 1-3 weeks but sometimes I that doesn't happen.

### Adrian Garcia, 2025-03-06

@Alexander Alan Arnold do you know the batteries used from both incidents. I see 1 battery photo attached that says it was manufactured in 2023, is that battery the one where the customer saw the battery state fluctuation (oct 12) or the one where the fuselage started to smoke (oct 30)

### Alexander Alan Arnold, 2025-03-07

Looking at the question for Pat  in the description that is the 12 October flight based on the description in the attached word document as far as batteries go Im not sure the main battery is the same for both incidents. We do not have the batteries. Does the FDR not have serial numbers logged in the spreadsheet? 

@Adrian Garcia

### Adrian Garcia, 2025-03-10

@Cameron Chapman @David Grosher Based off the evidence I have gathered, I believe the incident that occurred on OCT 12th does not relate the the OCT 30th incident. The fluctuation in the Battery State, as described in the customer’s report, can be attributed to an inaccurate SoC model that was modeled for loads of 400W and 30A. The investigation report highlights 2 other flights from Flight Ops that show Battery State fluctuating when the load is outside of the 400W and 30A range. I do think that the OCT 30th incident is due to a bad mate between the fuse power harness and battery. The anti-spark overheating/melting is a common symptom of a bad mate. 
Investigation Report: VXEP-761 - VXE 557 Smoking Smell from Fuselage after connecting main battery.pptx

### Cameron Chapman, 2025-03-12

@Adrian Garcia good findings. Please update fields above and recommend next steps.

### Adrian Garcia, 2025-03-13

@Cameron Chapman Is it okay to send back to RMA so that they are able to replace the Fuse Power Harness?

### Cameron Chapman, 2025-03-13

@Adrian Garcia please update fields above, separate linked incidents and ppts for the two issues described, and other actions described. I don’t think we have enough information in the ppt to prove that the issue is isolated to the harness. Please add more analysis.

### Jeremy White, 2025-03-13

I spoke with the operators today. They used multiple batteries. @Adrian Garcia @Alexander Alan Arnold

### Adrian Garcia, 2025-03-14

I was able to pull the logs from the oct 30th incident and noticed that the starting voltage is 13V with a 0.8A. I spoke to @Hayden Jeanor about this and he mentioned that if there is a bad initial mating the voltage should see a 10V-6V drop with about 1.5A of current. Between 50s and 60s the voltage increases to ~15V which is likely the time where the anti-spark melted. 
[embedded image-20250314-174427.png]
@Cameron Chapman @David Grosher

### Pat Wells, 2025-03-17

@Adrian Garcia @Cameron Chapman can we pull this back to RMA for repair or is there something else you need the aircraft for?

### Cameron Chapman, 2025-03-18

@Steve Gonzales can you please review this and determine what should be kept vs returned?

### Rodney Linch, 2025-03-31

@Steve Gonzales - can I return the cases to RMA and schedule work to replace power harness & SD cards?

### Steve Gonzales, 2025-03-31

@Rodney Linch pls replace the power harnesses.  Call me regarding the cases.  There is still an open question on the FW side, then we can give you back the avionics enclosure to replace the SD card.

### Rodney Linch, 2025-03-31

@Steve Gonzales - picked up both AC cases. Verified avionics box is not in the fuselage.

### Alexander Alan Arnold, 2025-04-08

@Steve Gonzales Any updates on this?

### Rodney Linch, 2025-04-16

@Steve Gonzales - may I take the avionics box to get the SD card swapped?

### Steve Gonzales, 2025-04-16

@Rodney Linch You can take back the Avionics box to replace the SD card.  We can still check the FW on the SOC issue apart from having the avionics box.

### Steve Gonzales, 2025-04-16

@Giovanni Gonzalez pls provide Rodney in RMA dept. with the avionics box for vehicle # 557.

### Rodney Linch, 2025-04-21

@Steve Gonzales would you please describe what work you did with the avionics box?  Depending on what y’all did with the box, SCO will need to tailor their checkout based on what was done. Thank you!

### Cameron Chapman, 2024-11-06

@Alexander Alan Arnold do we have a procedure to pull and send logs from a GCS? I think these may have some useful logs that could help with that last flight. See VXE-FCD-AAR Glossary.docx
@Eric Brewer can you please plot VTOL current and voltage on those flights for the same time period? It could be grounding issues causing that inaccuracy during VTOL descent.

### Eric Brewer, 2024-11-06

@Cameron Chapman 

[embedded image-20241106-210118.png]

### Cameron Chapman, 2024-11-06

Thanks @Eric Brewer this seems like pretty clear correlation that inaccuracy is due to VTOL current/grounding issues.

### Alexander Alan Arnold, 2024-11-07

- Can you please record SN of the battery used, post photos of the battery connector? -Is this not already in the information and pictures that have been added since opening the ticket or do you need additional pictures? (reference main battery image, main battery fuselage connector image) @Cameron Chapman
- I have added logs from the GCS connected to the VXE 557

### Cameron Chapman, 2024-11-07

Thanks @Alexander Alan Arnold . Good point. I added the SN.
@Eric Brewer can you review those GCS logs?

### Eric Brewer, 2024-11-07

@Cameron Chapman the logs contain mostly maintenance information, there is no current/voltage etc. data to analyze.

### Cameron Chapman, 2024-11-08

@Eric Brewer @Alexander Alan Arnold should this file be on the GCS? It seems so, but is not in the attached zip. 
log.csv
GCS csv log file of flight data. It has poor time resolution, but it can be useful for diagnosing a crash if the aircraft is not recovered.
I created this improvement task. https://jenaero.atlassian.net/browse/FS2-2521

### Eric Brewer, 2024-11-08

@Cameron Chapman that file is usually in the AAR’s but I didn’t see it in either of the attached folders.

### Cameron Chapman, 2024-11-12

@Michael Berger should GCS csv log file be on the GCS computer, or any other files with flight data? Which folders if so? @Alexander Alan Arnold can you please ask for that when Mike answers?

### Alexander Alan Arnold, 2024-11-12

@Cameron Chapman will do

### Michael Berger, 2024-11-12

The file which when included in the AAR is called log.csv is named logfile_241029_140349.csv or similar before being renamed when it is added to the AAR zip file.

### Rodney Linch, 2025-02-26

@Adrian Garcia - dropping off the Wing and Fuselage cases to the Engineering area.

### Adrian Garcia, 2025-03-04

@Rodney Linch are we able to get the battery that was used for investigating?

### Rodney Linch, 2025-03-04

@Adrian Garcia - battery was not shipped with V557.

### Jeremy White, 2025-03-05

@Rodney Linch Do we have an ECD?

### Rodney Linch, 2025-03-05

@Jeremy White I will defer to @Adrian Garcia as I believe he is the assigned engineer. And Adrian, if you’re not the assigned engineer, would you please send me the POC’s information?

### Adrian Garcia, 2025-03-05

@Jeremy White @Rodney Linch I am actively working on this ticket but I also have a higher priority investigation that is closing out soon. It is hard to say when the ECD is but I am shooting for next week.

### Jeremy White, 2025-03-05

@Adrian Garcia Thanks for the update. What is a typical or goal for RMA turn-arounds?

### Adrian Garcia, 2025-03-05

@Jeremy White I try my best to get them out 1-3 weeks but sometimes I that doesn't happen.

### Adrian Garcia, 2025-03-06

@Alexander Alan Arnold do you know the batteries used from both incidents. I see 1 battery photo attached that says it was manufactured in 2023, is that battery the one where the customer saw the battery state fluctuation (oct 12) or the one where the fuselage started to smoke (oct 30)

### Alexander Alan Arnold, 2025-03-07

Looking at the question for Pat  in the description that is the 12 October flight based on the description in the attached word document as far as batteries go Im not sure the main battery is the same for both incidents. We do not have the batteries. Does the FDR not have serial numbers logged in the spreadsheet? 

@Adrian Garcia

### Adrian Garcia, 2025-03-10

@Cameron Chapman @David Grosher Based off the evidence I have gathered, I believe the incident that occurred on OCT 12th does not relate the the OCT 30th incident. The fluctuation in the Battery State, as described in the customer’s report, can be attributed to an inaccurate SoC model that was modeled for loads of 400W and 30A. The investigation report highlights 2 other flights from Flight Ops that show Battery State fluctuating when the load is outside of the 400W and 30A range. I do think that the OCT 30th incident is due to a bad mate between the fuse power harness and battery. The anti-spark overheating/melting is a common symptom of a bad mate. 
Investigation Report: VXEP-761 - VXE 557 Smoking Smell from Fuselage after connecting main battery.pptx

### Cameron Chapman, 2025-03-12

@Adrian Garcia good findings. Please update fields above and recommend next steps.

### Adrian Garcia, 2025-03-13

@Cameron Chapman Is it okay to send back to RMA so that they are able to replace the Fuse Power Harness?

### Cameron Chapman, 2025-03-13

@Adrian Garcia please update fields above, separate linked incidents and ppts for the two issues described, and other actions described. I don’t think we have enough information in the ppt to prove that the issue is isolated to the harness. Please add more analysis.

### Jeremy White, 2025-03-13

I spoke with the operators today. They used multiple batteries. @Adrian Garcia @Alexander Alan Arnold

### Adrian Garcia, 2025-03-14

I was able to pull the logs from the oct 30th incident and noticed that the starting voltage is 13V with a 0.8A. I spoke to @Hayden Jeanor about this and he mentioned that if there is a bad initial mating the voltage should see a 10V-6V drop with about 1.5A of current. Between 50s and 60s the voltage increases to ~15V which is likely the time where the anti-spark melted. 
[embedded image-20250314-174427.png]
@Cameron Chapman @David Grosher

### Pat Wells, 2025-03-17

@Adrian Garcia @Cameron Chapman can we pull this back to RMA for repair or is there something else you need the aircraft for?

### Cameron Chapman, 2025-03-18

@Steve Gonzales can you please review this and determine what should be kept vs returned?

### Rodney Linch, 2025-03-31

@Steve Gonzales - can I return the cases to RMA and schedule work to replace power harness & SD cards?

### Steve Gonzales, 2025-03-31

@Rodney Linch pls replace the power harnesses.  Call me regarding the cases.  There is still an open question on the FW side, then we can give you back the avionics enclosure to replace the SD card.

### Rodney Linch, 2025-03-31

@Steve Gonzales - picked up both AC cases. Verified avionics box is not in the fuselage.

### Alexander Alan Arnold, 2025-04-08

@Steve Gonzales Any updates on this?

### Rodney Linch, 2025-04-16

@Steve Gonzales - may I take the avionics box to get the SD card swapped?

### Steve Gonzales, 2025-04-16

@Rodney Linch You can take back the Avionics box to replace the SD card.  We can still check the FW on the SOC issue apart from having the avionics box.

### Steve Gonzales, 2025-04-16

@Giovanni Gonzalez pls provide Rodney in RMA dept. with the avionics box for vehicle # 557.

### Rodney Linch, 2025-04-21

@Steve Gonzales would you please describe what work you did with the avionics box?  Depending on what y’all did with the box, SCO will need to tailor their checkout based on what was done. Thank you!

## Attachments (19)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 557 Main connector.jpeg | image | 237 | 2024-11-01 | listed only |
| 557 nose cone cable.jpeg | image | 198 | 2024-11-01 | listed only |
| 557 nose cone connector.jpeg | image | 464 | 2024-11-01 | listed only |
| [557 report.docx](attachments/24338_557%20report.docx.md) | docx | 13 | 2024-11-01 | converted |
| DATALOG - Copy (2).zip | archive | 26240 | 2024-11-01 | listed only |
| MaIn bAttery.jpeg | image | 290 | 2024-11-01 | listed only |
| battery connector.jpeg | image | 313 | 2024-11-01 | listed only |
| battery port bad.jpg | image | 339 | 2024-11-01 | listed only |
| image-20241101-212750.png | image | 147 | 2024-11-01 | listed only |
| main battery cell readout.jpeg | image | 251 | 2024-11-01 | listed only |
| image-20241104-231254.png | image | 45 | 2024-11-04 | listed only |
| image-20241105-000157.png | image | 134 | 2024-11-04 | listed only |
| image-20241105-163709.png | image | 41 | 2024-11-05 | listed only |
| image-20241106-184907.png | image | 1634 | 2024-11-06 | listed only |
| image-20241106-185047.png | image | 1583 | 2024-11-06 | listed only |
| image-20241106-185805.png | image | 1768 | 2024-11-06 | listed only |
| image-20241106-210118.png | image | 36 | 2024-11-06 | listed only |
| 557  datalogs.zip | archive | 18 | 2024-11-07 | listed only |
| image-20250314-174427.png | image | 38 | 2025-03-14 | listed only |
