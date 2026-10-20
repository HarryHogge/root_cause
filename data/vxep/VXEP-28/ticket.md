# VXEP-28: TPTR-94 HLB reading incorrect percentage compared to measurement with checker

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2023-08-23
- **Updated:** 2025-06-09
- **Resolved:** 2025-06-09
- **Reporter:** Allen Gardner
- **Assignee:** Cameron Chapman
- **Creator:** Allen Gardner
- **Links:** causes ENG-2181 (EA Internal: VXE511 Aborted Launch at 2ft, VTOL ESCs stuck in initialization loop); is caused by VA-35 (511 CW Input power connector damaged); relates to VA-399 (TPTR-94 HLB reading incorrect-Record which center wing this was originally discovered on. Was it 511?); relates to VA-400 ( TPTR-94 HLB reading incorrect -Summarize C/CA); is blocked by ENG-2343 (Locate and Download TIQ AARs)
- **Customer:** TIQUILA
- **Plan:** - Find data where aircraft reads 80% SOC, but bms voltage reads ~100%.
- **Incident Type:** Squawk
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

Files: https://jenaero.sharepoint.com/:f:/r/sites/FlightSafety/Shared%20Documents/Incident%20Reports/TPTR-94%20HLB%20Incorrectly%20Reading%20Voltage?csf=1&web=1&e=ab7OMe 
Summary: TPTR-94 HLB reading incorrect - Investigation .pptx
During TO1 FAT, HLB serial number 1803 reading was observed to be incorrect. The Battery read around 80%, however when checked with the checker, the reading was observed to be 98%. Noting that all batteries were charged prior to FAT.
 AUGUST 2023 FAT RAW DATA

## Corrective Action

- CAR CA-07-23 Defective part delivered to customer
- See https://jenaero.atlassian.net/browse/VXEP-12

## Issue Status

- HLB 2-1803 had a low voltage issue reporting from GCS SW when this HLB was installed during earlier attempted flight. Battery checker showed appropriate voltage. This battery was set aside as not to be used, but was not marked as NFF (schedule pressure reported). This battery was then used on this incident. The battery shows a missing retention ring, and small amounts solder of the end of the socket (probably from the overheating pin mating to it). This is the contact that mates to the anti-spark contact on the wing.
- Post flight discharge test appears normal. Indicates no permanent failure in the battery. Issue is suspected to be due to CW511 damage.

## Root Cause

- HLB 2-1803 was used with a center wing that was previously damaged, in engineering for troubleshooting, and should not have been flown or delivered to the customer. The findings were reported in JIRA, but wing was not red tagged. 511 RMA was not updated to indicate connector damage.
- Initial damage https://jenaero.atlassian.net/browse/VA-35
- FAT incident https://jenaero.atlassian.net/browse/ENG-2181 .
- This damage to the connector likely caused the intermittent connection and lower voltage readings.

## Comments (14)

### Michael Berger, 2023-08-24

Was the “incorrect percentage” of the HLB observed in the GCS Software? Or some other place
Was the problem observed on just one HLB or all?

### Allen Gardner, 2023-08-24

@Cameron Chapman Please creat a task in VA (and link it here) to determine the root cause of this issue. Then, after the root cause is identified, please have the team create the corrective actions lists and link here.

### Cameron Chapman, 2023-08-29

CAR link here. CA-07-23 Defective part delivered to customer. 
Quality mostly works in sharepoint, not Jira currently.

### Cameron Chapman, 2023-09-05

@John Clark or @Nadia Brown do you have anyone available to help with the data review section of this? Please create a quick ppt summary like this one. Vehicle Investigation Example Template (1)-Cam Recommendations.pptx

### Nadia Brown, 2023-09-05

@Cameron Chapman I could help out on this. Would you like me to assign to myself?

### Cameron Chapman, 2023-09-05

Assigned to Nadia. Let us know if you have any questions on the data review or ppt template.

### Cody Smisek, 2023-09-06

Per my comment in this https://jenaero.atlassian.net/browse/VA-399  it is unclear where the data will be or when the initial issue exactly occurred. Estimated to have occurred on afternoon of 8/7 or on 8/8.

### Cody Smisek, 2023-09-07

I’ve reviewed the 4x AARs currently available to Edge (unknown where the numerous others have been stored). It appears that HLB 1803 was likely installed on 8/7 for flight #2 (this was only verified through a flight data log on a future flight as the actual AAR is unavailable at this time). However, it should be made clear that the launch wizard likely does not update the HLB # when the step has been passed and the HLB is replaced. This could have been what occurred for this specific flight. So, any actual flight data may not correspond to 1803 as it was removed during preflight. 
AAR file name is not listed within the spreadsheet. Possibly due to issues we were having with pulling AARs throughout testing.

### Cody Smisek, 2023-09-08

@Nadia Brown I attached the AAR. @Cameron Chapman FYI

### Nadia Brown, 2023-09-11

@Cody Smisek The place where the AARs were linked does not seem to work for me.

[embedded file]
[embedded file]

### Cody Smisek, 2023-09-11

@Nadia Brown  the only applicable AAR for this issue is already linked within the issue.

### Nadia Brown, 2023-09-11

@Cody Smisek I see it, thank you.

### Nadia Brown, 2023-09-12

I began the ppt for this investigation and included the readings from the HLB in it:
Vehicle Investigation HLB 2-1803.pptx

### Cameron Chapman, 2023-09-19

@Nadia Brown please continue investigation task here https://jenaero.atlassian.net/browse/VA-400

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V511_230807_143443_pack.zip | archive | 2708 | 2023-09-08 | listed only |
| image-20230911-161812.png | image | 69 | 2023-09-11 | listed only |
| image-20230911-161917.png | image | 68 | 2023-09-11 | listed only |
