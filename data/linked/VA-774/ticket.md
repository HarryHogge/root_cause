# VA-774: Poor quality power contacts seem to originate from the same source. Need to confirm.

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-11-03
- **Updated:** 2025-06-10
- **Resolved:** 2025-06-10
- **Reporter:** Cameron Chapman
- **Assignee:** Cameron Chapman
- **Creator:** Cameron Chapman
- **Links:** relates to VA-573 (Poor Quality/higher impedance plating on AS150 power contacts - Containment and Corrective Action); relates to VXEP-162 (inconsistent plating of XT-90 connectors used on 107-102613); relates to VXEP-165 (XT60 Quality Concerns); relates to VXEP-181 (4mm Bullet Connector Quality Concerns); relates to VA-779 (VA-774   Poor quality power contacts seem to originate from the same source. C/CA); relates to VA-619 (Record order history of AS150 contacts. Determine what time period has defective parts and field test requirements (which vehicles to test).); relates to VA-613 (Ensure all AMASS contacts and connectors are only ordered from authorized suppliers. Not amazon.); relates to VA-997 (XT60 Non-AMASS Connectors Specified on VXE30 Fuel Cells); relates to VA-998 (XT60 AMASS Connector not clearly specified - 116-106349 Power Input Cable [Progressive RC])
- **Production Stakeholder:** Desiray Johnston
- **Supply Chain Stakeholder:** Victor Vandor
- **Other Stakeholder (as required):** Matt Philley
- **Plan:** list all of the orders we placed with that supplier. PN, qty, date, etc

## Description

https://jenaero.sharepoint.com/:x:/r/sites/EngineeringTeam/Shared%20Documents/Investigations/Anti-spark%20pin%20issue/AMASS%20New%20Supplier%20Status.xlsx?d=w0c556183578848e5b6bfb6c84a2a61bd&csf=1&web=1&e=1MDvG6 
Outsourcing Status
See linked issues and attached email. The seller was found using the AMASS website, but the gmail address, paypal payment, and defective contacts cast a lot more suspcion on this seller. We should not purchase from them again. Will determine in linked tickets what to do with existing inventory, WIP, and parts.  
Purchasing from that supplier started ~January 25, 2022
FYI @Greg Fryer 
AMASS Contacts
| AS150 PIN (-) | AS150-M |
| AS150 PIN, ANTI-SPARK (+) | AS150-M |
| AS150 SOCKET | AS150-F |
| PIN, EC3 | EC3-M |
| SOCKET, EC3 | EC3-F |
| EC5-PIN | EC5-M |
| EC5 SOCKET | EC5-F |
| RECPT, INLINE, XT90P | XT90H-M |
| XT90S ANTI-SPARK | XT90S-F |
| XT60 SOCKET CONNECTOR | XT60-F |
| XT60M | XT60-M |

Example order 
[embedded: image-20231107-232719.png]

## Comments (13)

### Cameron Chapman, 2023-11-03

Repeat of teams message for tracking: @Former user , Are you able to list all of the orders we placed with that supplier? PN, qty, date, etc?

### Matt Philley, 2023-11-06

@Marc Richardson how do you wanna handle this?

### Cameron Chapman, 2023-11-06

@Former user where is the best place to record which of these contacts we have purchased and their evaluation status? Do you have an existing tracker, or would it help if I created one?

### Former user, 2023-11-07

@Cameron Chapman As I am bringing these in from a reliable source, I am populating the FAI sheet, with a pass/fail from Lazlo.  I do not have a tracker made for these.  AS-150 has been entered.  EC3 & EC5 will get the same treatment when they arrive in about a week.  After that I have not purchased any other first articles at this time.  If any of these connectors are potential suspects, we should make a tracker to recall the data we are collecting now.  If you are able to do that, I will populate data on it as these connectors get brought in through FAI vendor change.

### Cameron Chapman, 2023-11-07

@Former user I created a tracker sheet here https://jenaero.sharepoint.com/:x:/r/sites/EngineeringTeam/Shared%20Documents/Investigations/Anti-spark%20pin%20issue/AMASS%20New%20Supplier%20Status.xlsx?d=w0c556183578848e5b6bfb6c84a2a61bd&csf=1&web=1&e=1MDvG6 taking data from the outsourcing status sheet. 
Thanks for your help with this. Can you please order first articles of the following from JAMECO? has the AMASS gmail address been removed as the supplier for all of those contacts listed?
 
| RECPT, INLINE, XT90P | XT90H-M |
| XT90S ANTI-SPARK | XT90S-F |
| XT60 SOCKET CONNECTOR | XT60-F |
| XT60M | XT60-M |

### Former user, 2023-11-07

@Cameron Chapman working to order the first articles with Jameco now, I believe they have all this in stock.  We could see this by this Friday.

### Matt Philley, 2023-11-14

@Victor Vandor FYSA

### Matt Philley, 2023-11-16

@Cameron Chapman @Laszlo Juhasz  more parts from JAMECO arrived. I updated the spreadsheet in the description of this Jira as well as the Outsourcing Status spreadsheet. 
Qty 2000 arrive for each of these. There are notes that FAI is Complete already. Are we OK just going into inventory or were we expecting specs or any form of certification paperwork?
| 100-104254 | A | CTRM AS150 Male Without Resistance 7mm Barrel |
| 100-102571 | A | CRTM AS150 Male with Resistance 7mm Barrel |
| 100-100804 | A | CRTM AS150 Female connector |


Qty 100 arrived for each of these. Notes say FAI is needed, so I will coordinate with Laszlo as long as you are still the point of contact for that. They are currently in QA.
| 100-102809 | A | CTRM EC5 5mm Male |
| 100-100834 | A | CTRM EC5 5mm Female |
| 100-100832 | A | CTRM EC3 3mm Male |
| 100-100831 | A | CTRM EC3 3mm Female |

@Catherine Wagner FYSA

### Matt Philley, 2023-11-20

For the Qty 7 PNs in the previous message I have setup Inspection Sheets for QA and asked Purchasing to flag them to go through Receiving Inspection upon arrival.
Additionally the Inventory and Production teams will work to keep parts in the original manufacturer packaging where possible to try and maintain traceability to batches and date of manufacturer for future reference.

### Matt Philley, 2023-11-28

@Cameron Chapman @Laszlo Juhasz 
Qty 4 more Part Numbers of JAMECO FAIs have arrived. They are labeled on the QA FAI Rack with Laszlo’s name along with the EC3 and EC5 pins mentioned a couple comments ago. I am not sure who from Procurement is the point of contact since Randy left. I will ping Victor. 
| 100-100899 |  | XT90 Male Anti Spark Connector, Receptacle [XT90H-M (JAMECO: BC-XT90M) ] |
| 100-100898 |  | XT90 Female Anti Spark Connector, Plug [XT90S-F (JAMECO: BC-XT90F)] |
| 100-105270 |  | CONNECTOR, XT60 FEMALE [XT60-F (JAMECO: BC-XT60F-H)] |
| 100-109065 |  | XT60M NO BACKSHELL [XT60-M (JAMECO: BC-XT60M-H)] |

### Matt Philley, 2023-11-29

@Cameron Chapman turns out we are out of 100-105270 (XT60-F) can I get your help to review the JAMECO FAI for this PN? If its easy to do the XT60-M at the same time too we can do that.
I performed a visual check per our latest criteria and they pass. Ben Hansen performed a check for Production and has approved, so I would like Engineering to take a quick look if we can…?

### Cameron Chapman, 2023-11-29

@Matt Philley I had to run home and wfh today due to a sick child, but should be in tomorrow. I think it will be more efficient to inspect and approve all JAMECO contacts at once. Can you either dropoff one of each new vs old on my desk, or I can pickup somewhere tomorrow? 
Thank you

### Cameron Chapman, 2023-12-01

@Matt Philley these are approved in FAI sheet. 
| 100-100899 |  | XT90 Male Anti Spark Connector, Receptacle [XT90H-M (JAMECO: BC-XT90M) ] |
| 100-100898 |  | XT90 Female Anti Spark Connector, Plug [XT90S-F (JAMECO: BC-XT90F)] |
| 100-105270 |  | CONNECTOR, XT60 FEMALE [XT60-F (JAMECO: BC-XT60F-H)] |
| 100-109065 | Existing inventory needs a scrub. See  https://jenaero.sharepoint.com/:x:/r/sites/EngineeringTeam/Shared%20Documents/Investigations/Anti-spark%20pin%20issue/AMASS%20New%20Supplier%20Status.xlsx?d=w0c556183578848e5b6bfb6c84a2a61bd&csf=1&web=1&e=MLACct | XT60M NO BACKSHELL [XT60-M (JAMECO: BC-XT60M-H)] |

@Laszlo Juhaszpreviously approved these.  
| FAI Received | 100-102809 | A | CTRM EC5 5mm Male |
| FAI Received | 100-100834 | A | CTRM EC5 5mm Female |
| FAI Received | 100-100832 | A | CTRM EC3 3mm Male |
| FAI Received | 100-100831 | A | CTRM EC3 3mm Female |

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [FW_ AS150-F & AS150-M.msg](attachments/17372_FW_%20AS150-F%20&%20AS150-M.msg.md) | msg | 224 | 2023-11-03 | converted |
| [RE_ RFQ - AS150-F.msg](attachments/17371_RE_%20RFQ%20-%20AS150-F.msg.md) | msg | 628 | 2023-11-03 | converted |
| image-20231107-232719.png | image | 268 | 2023-11-07 | listed only |
