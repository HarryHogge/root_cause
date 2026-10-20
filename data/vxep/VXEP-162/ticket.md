# VXEP-162: inconsistent plating of XT-90 connectors used on 107-102613

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-10-31
- **Updated:** 2025-06-10
- **Resolved:** 2025-06-10
- **Reporter:** Hayden Jeanor
- **Assignee:** Cameron Chapman
- **Creator:** Hayden Jeanor
- **Links:** relates to VA-750 (VA-744   inconsistent plating of XT-90 connectors used on 107-102613 - Identify C/CA); relates to VA-753 ( hold all WIP with XT90s and quarantine all inventory in SLO, in HSV, and AA.); relates to VA-752 (XT90 What is the ordering history of these parts (qty ordered and vendor)? Can we separate inventory by source? ); relates to VXEP-165 (XT60 Quality Concerns); relates to VXEP-181 (4mm Bullet Connector Quality Concerns); relates to VA-774 (Poor quality power contacts seem to originate from the same source. Need to confirm.)
- **Part Number(s):** 100-100899
- **Production Stakeholder:** Ben Hansen
- **Supply Chain Stakeholder:** Former user
- **Other Stakeholder (as required):** Matt Philley
- **Problem Type:** Production Issue
- **Plan:** - Done
- **Root Cause:** Fraudulent/Low quality supplier without COCs.
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

Files: https://jenaero.sharepoint.com/:f:/r/sites/EngineeringTeam/Shared%20Documents/Investigations/VXEP-162%20inconsistent%20plating%20of%20XT-90%20connectors%20used%20on%20107-102613?csf=1&web=1&e=M5I9u4 

https://jenaero.sharepoint.com/sites/JAI_Operations/Lists/NCR%20List/DispForm.aspx?ID=1785&commentId=3&e=geSRVvgspkSRp07Nfmpj6Q&at=15 
Tech description: There are very different, and easily visible differences in the plating of the connectors. Some are missing plating completely and some are missing parts of plating on the contact. There is a bag in production and we do not have a full count on how many are affected but it seems around 50%. There are 50 assemblies in production that are red tagged and will be routed for final inspection soon then we will require an engineering dispo. 

PNs:
Edge PN/Descrip: 100-100899 / XT90 Male Connector
Vendor: AMASS
Vendor PN: XT90H-M

XT90 current ratings
- cont = 40A
- max = 90A

Current drawn from MB
- cont cruise current ~ 450W/23V = 20A
- max climb power ~ 1500W/23V = 65A


Where-Used:
107-102613 - VXE BATTERY ADAPTER CABLE [used in FCR “Main” Battery]

## Corrective Action

- Process inventory according to quality alert and investigation plan.
- Establish new vendor and remove old vendor from purchasing system. See https://jenaero.atlassian.net/browse/VA-774

## Issue Status

https://jenaero.atlassian.net/browse/VA-774 
Inventory: Please scrap all connectors failing the attached quality alert. Connectors that pass are ok to use as is. 
WIP: Please quarantine any failing assemblies with connectors failing the attached quality alert for further disposition. Connectors that pass are ok to use as is. 
Finished Assemblies: If visible please quarantine any failing assemblies with connectors failing the attached quality alertfor further disposition. Connectors that pass are ok to use as is. These are used in Main Batteries, which are sealed after assembly. The lack of plating does not seem to affect electrical performance, the corrosion risk is very low in a sealed battery, the connector is never demated after initial connection, and the aircraft would detect a slowly corroding connector. No need to quarantine any sealed batteries.

## Comments (12)

### Hayden Jeanor, 2023-10-31

Initial measurements:
- visibly plated connector = 80uOhms
- visibly lacking plating connector = 110uOhms

### Hayden Jeanor, 2023-10-31

@Cameron Chapman FYI. threw some info in here, not sure who it should be assigned to based on priority.

### Cameron Chapman, 2023-10-31

@Matt Philley can we please start a containment for this? We should be able to disposition soon. 
Please hold all WIP with XT90s and quarantine all inventory in SLO and in HSV.  
Given the impedance measured is lower than the passing point of the much higher current AS150 limit, connectors with similar impedance shouldn’t be an overheating risk, but may be a degradation risk. 
@Hayden Jeanor 
- Can we sort good from bad easily?
- Can you please upload photos?

@Former user 
- What is the ordering history of these parts (qty ordered and vendor)? Can we separate inventory by source?

​FYI @Greg Fryer

### Cameron Chapman, 2023-10-31

@Laszlo Juhasz can you please help investigate first thing tomorrow morning?

### Matt Philley, 2023-11-01

@Marc Richardson FYSA. I will look into this further this morning.

### Matt Philley, 2023-11-01

Looks like latest batch was a direct from China…? We have ~4500 left in inventory.
[embedded file]
[embedded file]
[embedded file]

### Hayden Jeanor, 2023-11-01

resistance of left contact = 81uOhms
resistance of right contact = 110uOhms
[embedded file]

### Cameron Chapman, 2023-11-01

First steps:
- identify how many defective are present in WIP and inventory
- if we think they will be not acceptable
- Does the non-standard plating increase the risk of corrosion, solder, or other issues?
- Run sustained 65A through highest impedance connector. Log temps to see if any heat issues. (save files here https://jenaero.sharepoint.com/:f:/r/sites/EngineeringTeam/Shared%20Documents/Investigations/VXEP-162%20inconsistent%20plating%20of%20XT-90%20connectors%20used%20on%20107-102613?csf=1&web=1&e=M5I9u4 )
- If we can determine a process to sort them.

### Laszlo Juhasz, 2023-11-01

I’ve done the comparison 65A continuous power test, and the report was compiled. https://jenaero.sharepoint.com/:w:/r/sites/EngineeringTeam/Shared%20Documents/Electrical/XT-90%20Testing/Test%20Report_11_01_2023.docx?d=web648aeaa046421f84b95dc6e5d2b282&csf=1&web=1&e=0VMdRj

### Cameron Chapman, 2023-11-01

Thanks @Laszlo Juhasz for the detailed test report. It is also helpful to copy the conclusion here for quick viewing. Ex “Conclusion: There is no indication of any immediate defect that might affect the performance of the XT-90 connectors and I’m recommending continuing to use them in production. “

Do you predict any long term concerns due to these issues, like corrosion, solder issues, etc. or are they ok to use? The XT90s are pretty sealed in the main battery. The XT60s in the liked issue are not.

### Matt Philley, 2023-11-06

@Cameron Chapman @Laszlo Juhasz can yall take a quick look at the Inspection Sheet I drafted for XT90? I tried to capture reference images for the various defects we have found and wanna make sure it aligns with what you guys agree is not desirable. 
The XT60 Inspection Sheet will likely look almost the same.

I will call this out on the Quality Alert and by capturing it on an Inspection Sheet that means Inspection and Production will be able to reference this sheet when performing inspections in the future as well. We will also share with with AA and HSV.

Vault Doc# 115123, 100-100899 - XT90 Male Anti Spark Connector - Inspection Sheet

### Matt Philley, 2023-11-06

Updated Quality Alert has been attached here.
I will send Marc a copy to distribute to HSV and AA.
I went over the Inspection Sheet with Laszlo and it looks like the things we are higlighting in that align with what Engineering saw as well so if we inspect per that instruction we should have our bases covered.

## Attachments (6)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20231101-150027.png | image | 32 | 2023-11-01 | listed only |
| image-20231101-150125.png | image | 97 | 2023-11-01 | listed only |
| image-20231101-150234.png | image | 18 | 2023-11-01 | listed only |
| image-20231101-151211.png | image | 20372 | 2023-11-01 | listed only |
| [QA - XT-90 FCR Battery Plating Issue.xlsx](attachments/17375_QA%20-%20XT-90%20FCR%20Battery%20Plating%20Issue.xlsx.md) | xlsx | 881 | 2023-11-03 | converted |
| [QA - XT-90 FCR Battery Plating Issue - Updated 23.11.06.xlsx](attachments/17388_QA%20-%20XT-90%20FCR%20Battery%20Plating%20Issue%20-%20Updated%2023.11.06.xlsx.md) | xlsx | 884 | 2023-11-06 | converted |
