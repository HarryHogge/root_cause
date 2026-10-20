# VXEP-540: Recent AS150 Connectors causing intermittency and difficulty to connect and disconnect correctly and safely (AS150 Socket Issues)

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-08-15
- **Updated:** 2026-02-02
- **Resolved:** 2025-05-21
- **Reporter:** Hayden Jeanor
- **Assignee:** Greg Fryer
- **Creator:** Hayden Jeanor
- **Parent:** VXEP-444 Sustainment: VXE-30 (inc'l minor issues and improvements)
- **Links:** relates to VXEP-539 (Main battery (s/n: 3-1976) connector heated up while plugged into V692); relates to VA-1903 (VXE695 - Main Battery Harness Connector Sparking when Main Battery Mate); relates to ENG-2655 (107-102189 Pin Depth Tolerance Issue); relates to VXEP-326 (AS150 pin connectors diagnosing the reason the parts are OOS when assembled (could be pin dimensions, threads too deep, etc).  Identify long term C/CAs and short term workarounds. Ex 107-102189 114-106508); relates to VXEP-473 (Replacement for AS150 Connections, VXE30); relates to JA-136 (Convert Problem to Major Problem - Link + data loss questions); relates to VXEP-621 (Overnight parts to HSV); relates to VXEP-834 (VXE 567 Low battery warning during mission and link loss during RTB resulted in crash ); relates to VXEP-985 (VXE 560 Main battery connector was extremely hot after software upgrades); relates to VXEP-999 (VXE 598 with VXE 596 Center Wing. Lost connection to VTOL AP and ADB and crashed. ); relates to VXEP-761 (VXE 557 Smoking Smell from Fuselage after connecting main battery); relates to VXEP-553 (AS150 Plug/Pin Connector Issue Systemic Collector)
- **Issue color:** purple
- **Production Stakeholder:** Trevor Gronner
- **Supply Chain Stakeholder:** Kenneth Weber
- **Other Stakeholder (as required):** Steve Stack
- **Leadership Stakeholder:** Greg Fryer
- **Severity:** 1 - Flight Critical

## Description

Incident https://jenaero.atlassian.net/browse/VXEP-539  discovered a defect in the AS150 contact of Main Battery S/n: 1976 where the AS150 contact can become intermittent if not fully mated - causing heating (potentially melting) of the connector and could cause a “brown out” in flight. Need to determine what exact manufacturing defect caused the behavior exhibited, how to contain that problem, and how to correct the defect for the future
Investigation summary of the incident: Main battery (sn 3-1976) overheating connector - JIRA VXEP-539.docx

## Plan

Markings have been placed on connectors, and notification provided to warn to verify full mating. More robust resolutions will be executed in next block upgrades/aircraft.

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Historic info follows:
3/14 Meeting about customer incidents tied to this issue. 
- Try to bound occurrence of this issue to harness mfg date, battery serial number, etc. @Jackson Riley Curvin  to coordinate with @Brad Crampton . Add mfr date of vehicle incidents to the tracker sheet for problem connectors observed in production. Compare mfr dates of production issues, customer issues, transfer of builds to HSV, etc.
- Determine plan for customer notification.
- AN to ensure back of connector flange connector mates flush to the battery?


The plan steps below are outdated. Jira has not kept up with this investigation, as it was managed via spreadsheet and meetings. Keeping the plan below since some of the steps are still relevant in case anyone wants to update them. 
11/18: Issue
Some batteries are failing pull tests. These seem to be the WIP batteries that missed containment to .275 ID sockets.  https://jenaero.sharepoint.com/sites/JAI_Operations/Lists/NCR%20List/Attachments/4789/HybridPullTest%2011-13-24.xlsx?web=1 
Actions. 
- Add .275 diameter requirement to socket drawings. @Gary Angelus can you please coordinate this with @Steve Stack ASAP?
- Disposition batteries. Check previously approved limits. See if FLOPs wants these. Mark appropriately.
- SLO containment.
- Inspection socket diameter all batteries until we can contain all batteries.


Earlier investigation
- Identify pass fail tests and values then implement. 
- Assembly level. @Hayden Jeanor is developing pass/fail criteria based on demating force and testing batteries. Will need to document.
- Contact dimensions. @Brad Crampton and @Sloan Payne
- Evaluate potential short term workarounds. @Matt Weber 
- Contact or housing grease? I think the team tried silicone grease on the housings, but not the contacts. We could evaluate if it is possible/helpful to lubricate the contacts with anything without reducing current capacity or increasing the amount of dirt they pickup.
- Expand socket diameter. I don’t believe this procedure could be done with assembled connectors. With the female contact assembled in the plug housing, there is little room between the wall of the housing and the contact (see attached photo).
- Determine if we need a service bulletin for operator testing. Depends on workaround and testing.
- further investigate root cause(s)
- Is this more on the pin, socket, or both connectors? Seems mostly socket based, but certain pin connectors are easier to mate than others. this issue is tracking the pin side. https://jenaero.atlassian.net/browse/VXEP-326
- Differences in manufacturing from SLO to HSV. Transfer and test all tribal knowledge practices.
- Housings not built to print. Currently tracking here, but should be broken out into separate tasks. https://jenaero.atlassian.net/browse/VXEP-569
- Is the potting compound too rigid? Was tough seal (original compound) more flexible?
- Contact dimension changes
- Quantify what dimensions have changed, when they seem to have changed, and if this correlates to the connector mating difficulties. Initial indications seem to indicate the socket ID and pin OD have changed and may be leading potential causes.
- From this NCR, the Amass pins coming in at ~.038" shorter than nominal seems like it could be the main cause of this issue and potentially the hard to mate batteries. I suggest investigating where these pins were acquired, if they are authentic, how they compare to previous ones, etc.
- implement a corrective action
- Short term
- strap for back of AS150D connector?
- Long term https://jenaero.atlassian.net/browse/VXEP-473
- https://jenaero.atlassian.net/browse/VXEP-561

## Issue Status

Files: VXEP-540 Manufacturing defect in AS150 Connectors from EAES causing intermittency and difficulty to connect and disconnect correctly and safely
Action Tracking: TaskAndPriority.xlsx
Connector Tests: AS150 Connector Screening Data.xlsx
8/27 status documented here https://jenaero.atlassian.net/browse/VXEP-540  (comments, questions, more detail welcome): 
- Proposed connector test determined (fully mate connector, test demating force). Refining test criteria. 
- HLB: Preliminary criteria shows a higher occurrence between 1/30/24 and 7/24/24. 26/34 passing current criteria. Flight ops. Ryan. SCO.
- Need to test the round HLB connectors and review criteria/force limit with flight ops and other stake holders.
- Main Battery: Less of a chronological trend. 17/27 tested passing  current criteria. 
- Need to review criteria/force limit with flight ops and other stake holders.
- Significant variation in socket and pin dimensions measured. Newer ones seem to differ to older ones consistently. This is likely a significant contributor. Need to investigate if source related, or changed by the manufacturer.
- Investigating housings not built to print, fully documenting and transferring SLO tribal, and other improvements.
- Investigating potential workarounds for failing connectors. (grease, opening battery seals for rework, etc).
- Many more actions and statuses in JIRA.
- Removed o-ring. It did not affect demate force.

Sam 9/26 
“Yes. To satisfy critical September deliveries, we are going to proceed with the shipment of HLBs from this batch that meets this criteria: 
 
a) both black and amber connectors can be fully engaged
b) have tested a pull force of 60 lbs and below on the black connector and 42 lbs and below on the oval amber connector.  
 
We will want to cherry-pick batteries with the lowest pull forces.  No change on our Main battery pull force criteria at this time.  
Just talked with Kyle.  We will rework the remaining batteries (that aren’t cherry picked for Sept deliveries“

  https://jenaero.atlassian.net/browse/VXEP-540 
- Identify pass fail tests and values then implement.
- Assembly level. @Hayden Jeanor is developing pass/fail criteria based on demating force and testing batteries. Will need to document.  >> Completed:  Hayden Jeanor completed the pass/fall criteria.  It is stored at “Files”.  The filename is:  107-101050, 114-106085 - Electronics - AS150 Force Testing - Procedure.pptx
- Contact dimensions. @Brad Crampton and @Sloan Payne  >> Completed:  Contact dimensions collected in files: 100-100804 VendorDrawing.png, 100-102571 OuterDiameter.png, 100-104254 OuterDiameter.png, 107-102613 20PcStudy.xlsx, AS150 Connector Screening Data.xlsx, DplugDiameterStudy.xlsx, PinDiameterStudy.xlsx . Also, https://jenaero.atlassian.net/browse/VXEP-326 was created to further investigate.
- Evaluate potential short term workarounds. @Matt Weber
- Contact or housing grease? I think the team tried silicone grease on the housings, but not the contacts. We could evaluate if it is possible/helpful to lubricate the contacts with anything without reducing current capacity or increasing the amount of dirt they pickup. >> Completed:  Lubricant has been tried before without success per Brad Crampton.
- Expand socket diameter. I don’t believe this procedure could be done with assembled connectors. With the female contact assembled in the plug housing, there is little room between the wall of the housing and the contact (see attached photo).
- Determine if we need a service bulletin for operator testing. Depends on workaround and testing.  >> Completed:  A Quality Alert was issued by Brad Crampton on 8/19/2024.  File:  Quality Alert 107-101050 Main Battery 3.xlsx .   Pull Test Procedure was also created.  File:  107-101050, 114-106085 - Electronics - AS150 Force Testing - Procedure.pptx .   Harness Level Testing Procedure created.  File:  114-106508, 114-106509, 107-102613 - Electronics - AS150 Socket Force Testing - Procedure.pptx .  Training occurred on Sept 10, 2024.
- further investigate root cause(s)
- Is this more on the pin, socket, or both connectors? Seems mostly socket based, but certain pin connectors are easier to mate than others. this issue is tracking the pin side.  >> New Jira task created to further investigate:  https://jenaero.atlassian.net/browse/VXEP-326
- Differences in manufacturing from SLO to HSV. Transfer and test all tribal knowledge practices.  >> HSV has sorted all pins and have 940 of 3000 that are within need.  HSV recommends SLO start sorting (Sept 12 2024).
- Housings not built to print. Currently tracking here, but should be broken out into separate tasks.  >> New Jira task created: https://jenaero.atlassian.net/browse/VXEP-569
- Is the potting compound too rigid? Was tough seal (original compound) more flexible?  >> Discussions about potting, waiting to pott after pin alignment, and using jigs to align pins before potting were discussed.
- Contact dimension changes >> This step was not done in this Jira task.   Would be more part of  https://jenaero.atlassian.net/browse/VXEP-326 Instead, pull tests are being done to determine pass/fail criteria for connector to battery.
- Quantify what dimensions have changed, when they seem to have changed, and if this correlates to the connector mating difficulties. Initial indications seem to indicate the socket ID and pin OD have changed and may be leading potential causes.
- From this NCR, the Amass pins coming in at ~.038" shorter than nominal seems like it could be the main cause of this issue and potentially the hard to mate batteries. I suggest investigating where these pins were acquired, if they are authentic, how they compare to previous ones, etc.
- implement a corrective action
- Short term
- strap for back of AS150D connector?  >> Completed:  Short term solution was to halt production and sort through all pins keeping only those deemed within required dimension.  Production was resumed after that using the procedures outlined in #3 above.  10 battery cables of part number 508, 10 of 509, and 10 of 613 are being produced and are due to be shipped on Monday Sept 16, 2024.  Pre-potting Pull tests are being conducted and recorded.  Once potted, final pul tests will be conducted.  Once all pull tests are completed, this step is complete/finished.  Until a long-term solution is created, all cables from here on must have this manual pull testing done before acceptance.
- Long term >> Completed:  Plan is to sort through batteries that are not within specification and repair/correct the issue then restock.  Pull tests are being done to determine pass/fail criteria for connector to battery.   https://jenaero.atlassian.net/browse/VXEP-473
- >> As part of the short term solution, this Jira task was created and is being worked:  https://jenaero.atlassian.net/browse/VXEP-561 Laszlo Juhasz started the battery dismantling process on Sept 10, 2024.  The steps in the process are being compiled and will become part of the method in https://jenaero.atlassian.net/browse/VXEP-561.  When this procedure is documented, this step is complete.
- Long term solution to be completed by Matt Philley in separate Jira task.
- When step #5 and step #6 are completed, this Jira task can be closed.  (Charles Madewell, 16 Sept 2024).
- Final Comment:  Steps #5 and #6 were completed.  Full pull testing went on for a long time in Huntsville.  Pull tests have shown that the connector and procedural fixes worked as no excessive force is being exhibited in the pull tests.  Thus, Huntsville site has stopped pull testing and resumed normal operation.
- Long term future fix/improvement Jira tasks are not included in these comments and is a separate task.

## Comments (43)

### Cameron Chapman, 2024-08-29

@Ryan Stafford @Brad Crampton could you please paste a link to the action tracker so that I can link it here?

### Cameron Chapman, 2024-08-29

8/29 Meeting Notes:
- Please record socket diameters in the same sheet as the pull force so we can correlate that information https://jenaero.sharepoint.com/:x:/r/sites/FlightSafety/Shared%20Documents/Incident%20Reports/VXEP-540%20%20%20%20Manufacturing%20defect%20in%20AS150%20Connectors%20from%20EAES%20causing%20intermittency%20and%20difficulty%20to%20connect%20and%20disconnect%20correctly%20and%20safely/AS150%20Connector%20Screening%20Data.xlsx?d=w22c23ca903634ca09795efcfd7f8b9bd&csf=1&web=1&e=zu4Sxw
- Need to confirm we are screening and checking diameter of every socket.

### Cameron Chapman, 2024-08-29

@John Gober helpful analysis thank you. @Matt Weber see below. 
- It makes sense stretching contacts in the housing may not be feasible. Thank you for the analysis.
- If the battery is dismantled, we would just replace the entire pigtail/connector. They are not serviceable.
- I think the team tried silicone grease on the housings, but not the contacts. We could evaluate if it is possible/helpful to lubricate the contacts with anything without reducing current capacity or increasing the amount of dirt they pickup.

### John Gober, 2024-08-29

I’ll take a look for some products to try and evaluate the risks.

### Brad Crampton, 2024-08-29

@Cameron Chapman I added a snapshot or correlation data we collected yesterday: ID CorrelationData-1    More to come.

### John Gober, 2024-08-29

NYOGEL 760G seems to be the gold standard.  Product Overview - NyoGel 760G_23(.indd (nyelubricants.com)
It is approved by Ford, GM, Toyota, Chrysler, Daimler, Freightliner, Trane, Black & Decker, Honeywell and others.
The manufacturer claims the product does not affect conductivity. Does Grease Affect Conductivity? | Nye Lubricants
Temp Range is -40 to 135 C
It is expensive and difficult to get. The factory will only accept orders over $750.  Small quantiles can be ordered here:
NYOGEL 760G 100 GRAM TUBE | Next Generation Services (nextgenstore.com)

They also have a product, UNIFLOR 8961MT, which is recommended for Aerospace connectors and meets MIL-PRF-27617, but the cost is $1,500 / 50 grams.  The only benefit I see is the temp range is extended to -80 to 200 C.

### Brad Crampton, 2024-08-29

@Matt Weber I don’t know if this is a crazy idea or not but a slight hydraulic expansion of the inner diameter while the connector is in the battery might offer a solution to rework batteries.  Looks like it comes with a 1/4” fitting.  
https://www.youtube.com/watch?v=0iZONUECpXA

### Cameron Chapman, 2024-08-29

Thanks @John Gober . 
- Do you have equipment in HSV to test contacts up to 200A and examples of hard to mate connectors, or are they all in SLO?
- Did you see the temp rating of NYOGEL 760G? @Laszlo Juhasz could be answer how hot our contacts get during discharge. It may be that hot.
- Do you think that grease would pickup a lot of dust and degrade the connector performance?

Please order to evaluate if either/both sounds like a good option to test. Here is our purchasing process. I am not sure if it is the same for HSV. https://jenaero.atlassian.net/wiki/spaces/EF/pages/7307274/Buying+Stuff?search_id=d4617e60-d0bf-48c9-96f1-2ae3bc449551

### John Gober, 2024-08-30

- Equipment: 
- I did find a wire terminal pull tester I believe can be adapted to measure contact removal force.  DataSheetWT3-201.pdf (mark-10.com)
- 200 Amp test in HSV is a no go.  The only bench supply we have here is a 10 Amp model and we have a 30 Amp electronic DC load.
- Eric has nine (9) 107-102189-1 assemblies in quarantine.  
- Contacts in stock @ HSV
- 100-100804 / Qty.  2,170
- 100-102571 / Qty.  292
- 100-104254 / Qty.  2,290
- Why would we test at 200 Amps? The cable assembly I’ve been looking at has an XT90 connector on the battery end which is rated for 90A instantaneous and 40 Amps continuous. The assembly uses a 10AWG, 200C wire which I would rate about 50A when bundled.  
- Unless the AS150 contacts are used elsewhere in a higher current application I’m not aware of, I would recommend test parameters more in line with how we are actually using the contacts. I think our actual maximum continuous and instantaneous currents plus say a 20% margin would be a sufficient test.  I need someone to confirm those max values, but based on the information I’ve seen, I would frame the test around 50A continuous / 100A instantaneous.
- Temperature Ranges
- NYOGEL 760G: -40 to 135 C
- UNIFLOR 8961MT:  -80 to 200 C.
- Performance with dielectric grease 
- Common sense is telling me if we apply any type of film, it will catch more dust than if we hadn’t. There are too many variables for a conversation on how much additional dust would collect and at what point accumulated dust would adversely affect performance to be anything more than speculation. I think we would be ok with normal use and care, but we have to consider extremes like desert dust storms as well as abuse, neglect, and untrained personnel. Obviously, with the potting and O-ring, these connections should be near IP6x (dust proof) when mated. Do we not supply dust covers to install when the connections are not in use?

### John Gober, 2024-09-05

I circled back with @Laszlo Juhasz on the temperatures seen by the AS150 contacts.
He reported applications where the AS150 contacts see in excess of 200 Amps and can see temperatures of 240C. 
240C is beyond the max temp of all the lubricants I surveyed.
Let’s recap…
- Three times the contact manufacturer’s rated continuous current of 70 Amps
- Double the contact manufacturer’s operating temperature range of 120C
- 40 degrees beyond the deflection temperature (200C) of the housing material (Ultem)
- 40 degrees beyond the melting point of PTFE wire insulation (200C)
- 25 degrees past the melting point of lead-free solder (215 to 240C)

I would not recommend introducing dielectric grease or any other compound into this situation.

### Cameron Chapman, 2024-09-13

@John Gober I think the 240C measurement was when subjected to a longer than realistic profile. The contacts do not reach 240C in the flight profiles they are exposed to (~30 sec max at that current)https://jenaero.atlassian.net/wiki/spaces/EE/pages/11272193/Power+and+Temperature+Profiles, but I agree they are being stressed beyond their designed limits and dielectric grease would add risk.

### Charles David Madewell, 2024-11-01

This effort is complete, and manufacturing has resumed.  The long term fix for the issue is being worked in another JIRA task.

### Cameron Chapman, 2024-11-18

Reopening. This is not done, but could use some cleanups

### Brad Crampton, 2025-01-08

@Cameron Chapman @Hayden Jeanor @Sloan Payne @Wayne Houston I have added a proposed drawing change for 114-106509 because we are still getting a high percentage of rejects due to this cable in the battery.

### Cameron Chapman, 2025-01-09

This looks good to me. @Gary Angelus can you please create a linked eng change task to update that drawing, and check Jira to see if needs any other updates?

### David Grosher, 2025-05-20

@Cameron Chapman What is the status of this investigation? It isn’t assigned to anyone.

### Cameron Chapman, 2025-05-20

@David Grosher The issue will be resolved for B35/40 aircraft. We will need to decide if it is a manpower priority to address remaining B30 issues. Assigning to @Greg Fryer  to determine if we should allocate manpower to resolve the B30 issues. Guessing no currently. Updated plan.

### Greg Fryer, 2025-05-21

@David Grosher @Cameron Chapman I’m going to close this after I write up what we’ve done, which is what we can do. Thanks for bringing it up.

### Greg Fryer, 2025-05-21

See linked incident

### Cameron Chapman, 2025-08-12

@Greg Fryer Which ticket? We have a linked one for pin issues, but I don’t see one for sockets. While it needs a lot of cleanup, this issue seems to have the most info for that.

### Cameron Chapman, 2024-08-28

Wed evening update.
 
- Hayden measured removal force of multiple finished goods, Main and HLB, using a pull force gauge and power harness connector.
- Flight ops reviewed and gave input on thresholds for connector fit (what is “too tight”)
- Brad then measured receptacle size using pin gauges and compared that to removal force for each battery. Correlation was seen between undersized pins and strong pull force needed
- @Hayden Jeanor will provide measurement method and @Brad Crampton will measure all finished goods batteries Thursday morning to determine how many shippable batteries we have
- @Brad Crampton will need mechanical engineering assistance (@Matt Weber) to determine a pass/fail criteria for receptacle components, then we can sort inventory

 
-----Original Appointment-----
From: Ryan Stafford

### Brad Crampton, 2024-08-29

Latest data from pull test has been posted as PinDiametStuy.xksx.  Old versions were removed but no data is missing. Seems like a pretty good bit of evidence to suggest receptacle I.D. as a major culprit. We are going to do sorting today so a great deal more data will be generated to confirm or deny the I.D. correlation to pull force. I plan on measuring pull force and I.D. of receptacles while recording serial numbers during the battery sorting. I think it can be stated with a good bit of certainty that receptacle pin  I.D.'s can be sorted using .275 as a criteria but group consensus is important on this issue.

### John Gober, 2024-08-29

Cameron, 

[embedded Plug Assembled.jpg]

On stretching the contacts… In theory, we could forcefully insert an oversized pin gauge into the female contact and then test the contact retention force. The process would be repeated with progressively larger pins until the retention force falls to an acceptable level.
However, I don’t believe this procedure could be done with assembled connectors. With the female contact assembled in the plug housing, there is little room between the wall of the housing and the contact (see attached photo).
Ryan and I examined this spacing earlier in the week. As I recall, on the article I measured the hole in the plug was 0.005” larger than the OD of the female contact. This would not be sufficient room to allow any meaningful “stretching” of the female contact in a completed assembly. 
Now, if we must dismantle an assembled workpiece to attempt a work around, wouldn’t a better solution be to replace the non-conforming contact – once we decide what “conforming” means and are able to obtain stock. 
On adding grease or dry lube… Someone in this conversation, I think it was Laszlo, stated that grease had already been tried without much success. We should circle back to see what was tried and if the results warrant further investigation. We also don’t seem to have a force gauge in the HSV office. We would need to order one to conduct any testing with quantifiable results.

### Cameron Chapman, 2024-08-29

@Ryan Stafford @Brad Crampton could you please paste a link to the action tracker so that I can link it here?

### Cameron Chapman, 2024-08-29

8/29 Meeting Notes:
- Please record socket diameters in the same sheet as the pull force so we can correlate that information https://jenaero.sharepoint.com/:x:/r/sites/FlightSafety/Shared%20Documents/Incident%20Reports/VXEP-540%20%20%20%20Manufacturing%20defect%20in%20AS150%20Connectors%20from%20EAES%20causing%20intermittency%20and%20difficulty%20to%20connect%20and%20disconnect%20correctly%20and%20safely/AS150%20Connector%20Screening%20Data.xlsx?d=w22c23ca903634ca09795efcfd7f8b9bd&csf=1&web=1&e=zu4Sxw
- Need to confirm we are screening and checking diameter of every socket.

### Cameron Chapman, 2024-08-29

@John Gober helpful analysis thank you. @Matt Weber see below. 
- It makes sense stretching contacts in the housing may not be feasible. Thank you for the analysis.
- If the battery is dismantled, we would just replace the entire pigtail/connector. They are not serviceable.
- I think the team tried silicone grease on the housings, but not the contacts. We could evaluate if it is possible/helpful to lubricate the contacts with anything without reducing current capacity or increasing the amount of dirt they pickup.

### John Gober, 2024-08-29

I’ll take a look for some products to try and evaluate the risks.

### Brad Crampton, 2024-08-29

@Cameron Chapman I added a snapshot or correlation data we collected yesterday: ID CorrelationData-1    More to come.

### John Gober, 2024-08-29

NYOGEL 760G seems to be the gold standard.  Product Overview - NyoGel 760G_23(.indd (nyelubricants.com)
It is approved by Ford, GM, Toyota, Chrysler, Daimler, Freightliner, Trane, Black & Decker, Honeywell and others.
The manufacturer claims the product does not affect conductivity. Does Grease Affect Conductivity? | Nye Lubricants
Temp Range is -40 to 135 C
It is expensive and difficult to get. The factory will only accept orders over $750.  Small quantiles can be ordered here:
NYOGEL 760G 100 GRAM TUBE | Next Generation Services (nextgenstore.com)

They also have a product, UNIFLOR 8961MT, which is recommended for Aerospace connectors and meets MIL-PRF-27617, but the cost is $1,500 / 50 grams.  The only benefit I see is the temp range is extended to -80 to 200 C.

### Brad Crampton, 2024-08-29

@Matt Weber I don’t know if this is a crazy idea or not but a slight hydraulic expansion of the inner diameter while the connector is in the battery might offer a solution to rework batteries.  Looks like it comes with a 1/4” fitting.  
https://www.youtube.com/watch?v=0iZONUECpXA

### Cameron Chapman, 2024-08-29

Thanks @John Gober . 
- Do you have equipment in HSV to test contacts up to 200A and examples of hard to mate connectors, or are they all in SLO?
- Did you see the temp rating of NYOGEL 760G? @Laszlo Juhasz could be answer how hot our contacts get during discharge. It may be that hot.
- Do you think that grease would pickup a lot of dust and degrade the connector performance?

Please order to evaluate if either/both sounds like a good option to test. Here is our purchasing process. I am not sure if it is the same for HSV. https://jenaero.atlassian.net/wiki/spaces/EF/pages/7307274/Buying+Stuff?search_id=d4617e60-d0bf-48c9-96f1-2ae3bc449551

### John Gober, 2024-08-30

- Equipment: 
- I did find a wire terminal pull tester I believe can be adapted to measure contact removal force.  DataSheetWT3-201.pdf (mark-10.com)
- 200 Amp test in HSV is a no go.  The only bench supply we have here is a 10 Amp model and we have a 30 Amp electronic DC load.
- Eric has nine (9) 107-102189-1 assemblies in quarantine.  
- Contacts in stock @ HSV
- 100-100804 / Qty.  2,170
- 100-102571 / Qty.  292
- 100-104254 / Qty.  2,290
- Why would we test at 200 Amps? The cable assembly I’ve been looking at has an XT90 connector on the battery end which is rated for 90A instantaneous and 40 Amps continuous. The assembly uses a 10AWG, 200C wire which I would rate about 50A when bundled.  
- Unless the AS150 contacts are used elsewhere in a higher current application I’m not aware of, I would recommend test parameters more in line with how we are actually using the contacts. I think our actual maximum continuous and instantaneous currents plus say a 20% margin would be a sufficient test.  I need someone to confirm those max values, but based on the information I’ve seen, I would frame the test around 50A continuous / 100A instantaneous.
- Temperature Ranges
- NYOGEL 760G: -40 to 135 C
- UNIFLOR 8961MT:  -80 to 200 C.
- Performance with dielectric grease 
- Common sense is telling me if we apply any type of film, it will catch more dust than if we hadn’t. There are too many variables for a conversation on how much additional dust would collect and at what point accumulated dust would adversely affect performance to be anything more than speculation. I think we would be ok with normal use and care, but we have to consider extremes like desert dust storms as well as abuse, neglect, and untrained personnel. Obviously, with the potting and O-ring, these connections should be near IP6x (dust proof) when mated. Do we not supply dust covers to install when the connections are not in use?

### John Gober, 2024-09-05

I circled back with @Laszlo Juhasz on the temperatures seen by the AS150 contacts.
He reported applications where the AS150 contacts see in excess of 200 Amps and can see temperatures of 240C. 
240C is beyond the max temp of all the lubricants I surveyed.
Let’s recap…
- Three times the contact manufacturer’s rated continuous current of 70 Amps
- Double the contact manufacturer’s operating temperature range of 120C
- 40 degrees beyond the deflection temperature (200C) of the housing material (Ultem)
- 40 degrees beyond the melting point of PTFE wire insulation (200C)
- 25 degrees past the melting point of lead-free solder (215 to 240C)

I would not recommend introducing dielectric grease or any other compound into this situation.

### Cameron Chapman, 2024-09-13

@John Gober I think the 240C measurement was when subjected to a longer than realistic profile. The contacts do not reach 240C in the flight profiles they are exposed to (~30 sec max at that current)https://jenaero.atlassian.net/wiki/spaces/EE/pages/11272193/Power+and+Temperature+Profiles, but I agree they are being stressed beyond their designed limits and dielectric grease would add risk.

### Charles David Madewell, 2024-11-01

This effort is complete, and manufacturing has resumed.  The long term fix for the issue is being worked in another JIRA task.

### Cameron Chapman, 2024-11-18

Reopening. This is not done, but could use some cleanups

### Brad Crampton, 2025-01-08

@Cameron Chapman @Hayden Jeanor @Sloan Payne @Wayne Houston I have added a proposed drawing change for 114-106509 because we are still getting a high percentage of rejects due to this cable in the battery.

### Cameron Chapman, 2025-01-09

This looks good to me. @Gary Angelus can you please create a linked eng change task to update that drawing, and check Jira to see if needs any other updates?

### David Grosher, 2025-05-20

@Cameron Chapman What is the status of this investigation? It isn’t assigned to anyone.

### Cameron Chapman, 2025-05-20

@David Grosher The issue will be resolved for B35/40 aircraft. We will need to decide if it is a manpower priority to address remaining B30 issues. Assigning to @Greg Fryer  to determine if we should allocate manpower to resolve the B30 issues. Guessing no currently. Updated plan.

### Greg Fryer, 2025-05-21

@David Grosher @Cameron Chapman I’m going to close this after I write up what we’ve done, which is what we can do. Thanks for bringing it up.

### Greg Fryer, 2025-05-21

See linked incident

### Cameron Chapman, 2025-08-12

@Greg Fryer Which ticket? We have a linked one for pin issues, but I don’t see one for sockets. While it needs a lot of cleanup, this issue seems to have the most info for that.

## Attachments (15)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20240815-225520.png | image | 953 | 2024-08-15 | listed only |
| image-20240816-153119.png | image | 1891 | 2024-08-16 | listed only |
| image-20240816-153403.png | image | 2156 | 2024-08-16 | listed only |
| image-20240816-153417.png | image | 2145 | 2024-08-16 | listed only |
| image-20240816-154900.png | image | 2011 | 2024-08-16 | listed only |
| image-20240816-155140.png | image | 1379 | 2024-08-16 | listed only |
| image-20240816-155145.png | image | 1478 | 2024-08-16 | listed only |
| ConnectorGap.png | image | 493 | 2024-08-22 | listed only |
| [ExperimentOne 8-22-24.docx](attachments/22566_ExperimentOne%208-22-24.docx.md) | docx | 16 | 2024-08-22 | converted |
| Vdrop.png | image | 380 | 2024-08-22 | listed only |
| MicrosoftTeams-video.mp4 | video | 1468 | 2024-08-23 | listed only |
| ID CorrelationData-1.png | image | 45 | 2024-08-29 | listed only |
| [PinDiameterStudy.xlsx](attachments/22795_PinDiameterStudy.xlsx.md) | xlsx | 96 | 2024-08-29 | converted |
| Plug Assembled.jpg | image | 156 | 2024-08-29 | listed only |
| [proposedChange 114-106509.xlsx](attachments/25312_proposedChange%20114-106509.xlsx.md) | xlsx | 142 | 2025-01-08 | converted |
