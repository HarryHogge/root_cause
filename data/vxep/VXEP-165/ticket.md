# VXEP-165: XT60 Quality Concerns

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-11-01
- **Updated:** 2025-06-10
- **Resolved:** 2025-06-10
- **Reporter:** Cameron Chapman
- **Assignee:** Cameron Chapman
- **Creator:** Cameron Chapman
- **Links:** relates to VXEP-162 (inconsistent plating of XT-90 connectors used on 107-102613); relates to VA-774 (Poor quality power contacts seem to originate from the same source. Need to confirm.); relates to VA-763 (VXEP-165   XT60 Quality Concerns - Identify C/CA)
- **Root Cause:** Fraudulent/Low quality supplier without COCs.
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

NCR XT60-F contacts on 107-102189-2 with suspect workmanship

t looks like we found JAMECO PNs for them, but stuff in Inventory and WIP is from questionable AMASS source. Hayden took a look at some of the bad ones that Production found and is of the opinion we should quarantine all of them until Engineering can do some testing.
 
I will go ahead and generate a JIRA ticket here in a few. Let me know your thoughts before I go ahead and pause Production. 
 
Here are some of the defects:
 
Contact Height:
 
Different color housings seem to correspond to a more shallow pin depth:
 
[embedded file, not matched to an attachment]
[embedded file, not matched to an attachment]
[embedded file, not matched to an attachment]
 
Some with very poor machining quality & discoloration at the base of pins some on "solder" side and some on "mating" side:

## Corrective Action

- Process inventory according to quality alert and investigation plan.
- Establish new vendor and remove old vendor from purchasing system. See https://jenaero.atlassian.net/browse/VA-774

## Plan

- Process inventory according to quality alert.
- Establish new vendor and remove old vendor from purchasing system.

## Issue Status

Inventory: Please scrap all connectors failing the attached quality alert. Connectors that pass are ok to use as is.
WIP: Please quarantine any failing assemblies with connectors failing the attached quality alert for further disposition. Connectors that pass are ok to use as is.
Finished Assemblies: If visible please quarantine any failing assemblies with connectors failing the attached quality alertfor further disposition. Connectors that pass are ok to use as is. Finished assemblies will not have any of the defect pictured visible. The do not seem like they will impact performance. Please flag any newly discovered issues.

## Comments (8)

### Cameron Chapman, 2023-11-01

@Garrett O'Neill can you please report max current for this connector in VXE30 and Xkit (D450 and 750 fuel cells)? 
@Laszlo Juhasz can you please report max impedance measured from an initial batch and perform a sustained current test on these.

### Garrett O'Neill, 2023-11-01

@Cameron Chapman @Laszlo Juhasz Per the respective fuel cell ICDs, worst-case currents are:
VXE30 (D450)
450W/19V = 23.7A
X-Kit (D750)
916W/38V = 24.1A

### Connor Peebles, 2023-11-02

@Laszlo Juhasz We put some XT60’s from NCR 1796 on your workbench. @Ben Hansen Helped me understand that these are a slightly different concern than the XT90’s:
Basic quality and build concerns
- Plating issue isn’t the same, it doesn’t look silverish
- Charring inside some contacts (black soot?)
- inconsistent size contacts
- cup at the edge of housing and leading to melted connector housings
- bought on the same PO as the counterfeit AS150’s

@Matt Philley @Brad Crampton  If you can find some XT60s with the same plating issues as we saw on the XT90s we would like to test those especially.

### Brad Crampton, 2023-11-02

@Laszlo Juhasz @Matt Philley From my understanding the issue with the XT 60’s are mostly poor assembly and machining. If I become aware of a plating issue, I will let you know.

### Cameron Chapman, 2023-11-03

@Laszlo Juhasz can you please enter your XT60 findings and recommendation here?

### Laszlo Juhasz, 2023-11-03

@Cameron Chapman @Matt Philley  The test for the XT-60 connector was competed and the report was saved at: https://jenaero.sharepoint.com/:w:/r/sites/EngineeringTeam/Shared%20Documents/Electrical/XT-60%20Testing/XT60_Test%20Report_11_02_2023.docx?d=wcaf36c3b75fd4453887c3674e5eefeba&csf=1&web=1&e=X50vHm
“Conclusion: There is no indication of any immediate defect that might affect the performance of the XT-60 connectors and passes the overall high current thermal connection test.”

### Cameron Chapman, 2023-11-03

@Laszlo Juhasz do you predict any other long term issues caused by these defects (solder bonding quality, increased corrosion, etc.)? That evaluation will help us determine what to do with affected parts.

### Matt Philley, 2023-11-06

Updated Quality Alert has been attached here and I will start distributing. 
I will send Marc a copy to distribute to HSV and AA.

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [QA - XT-60 FCR Battery Various Issues.xlsx](attachments/17374_QA%20-%20XT-60%20FCR%20Battery%20Various%20Issues.xlsx.md) | xlsx | 441 | 2023-11-03 | converted |
| [QA - XT-90 FCR Battery Plating Issue - Updated 23.11.06.xlsx](attachments/17389_QA%20-%20XT-90%20FCR%20Battery%20Plating%20Issue%20-%20Updated%2023.11.06.xlsx.md) | xlsx | 884 | 2023-11-06 | converted |
