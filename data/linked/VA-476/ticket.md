# VA-476: Investigate if autopilot was reused from previous incident and could have contributed to latest crash.

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-09-07
- **Updated:** 2023-11-09
- **Resolved:** 2023-09-20
- **Reporter:** Cameron Chapman
- **Assignee:** Hayden Jeanor
- **Creator:** Cameron Chapman
- **Links:** relates to VA-391 (Address loose bus bar on VTOL AP board. Determine if service bulletin or AD are recommended. Create tasks for that if so. ); blocks VXEP-8 (TPTR-6 VXE 489 fuse 408 CW VTOL Motor delayed start)
- **Sprint:** VXE-2 Greg's Team 9-17

## Description

First incident: 
- Probably not this one. Likely had 489CW. Could verify via data logs. https://jenaero.atlassian.net/browse/VIT2-217 
- 408CW was NOT involved in this incident, so did not cause the ballast bar issue.
- https://jenaero.atlassian.net/browse/VIT2-193 May have been damaged in this incident. We could check if parts were ever replaced.  
- if 408CW was on during this incident:
- determine if 408CW avionic was ever checked or replaced - check with RMA?
- Vehicle was not RMA’d after event, so no inspect or repair occured.
- determine the amount of deceleration the vehicle experienced
- No log exists that records the g forces, VTOL logs corrupted, and IMU data in the XCOMM were not turned on.

Second incident: https://jenaero.atlassian.net/browse/VIT2-272 
Investigate if we have RMA information for either. 

Conclusion: CW408 was found to be uninvolved in the crashed flight (https://jenaero.atlassian.net/browse/VIT2-217  ), but it was found to be involved in an incident where the aircraft had a hard landing (https://jenaero.atlassian.net/browse/VIT2-193 ). After its hard landing, V408 was never RMA’ed or inspected for sustained damage during that landing. We are unable to quantify the amount of g-force the aircraft sustained during the landing because VTOL logs were lost and Xcomm imu data was not enabled during the flight.

## Comments (7)

### Hayden Jeanor, 2023-09-08

confirmed incident https://jenaero.atlassian.net/browse/VIT2-217  had 489CW attached 
[embedded: image-20230908-223647.png]

### Hayden Jeanor, 2023-09-11

Confirmed that https://jenaero.atlassian.net/browse/VIT2-193  did have 408CW during the hard landing. 
[embedded: image-20230911-180041.png]

### Hayden Jeanor, 2023-09-11

No VTOL logs present in https://jenaero.atlassian.net/browse/VIT2-193  incident. And the Xcomm imu data was not enabled and logging during the flight. Looking into other ways that i can determine the acceleration from the landing

### Hayden Jeanor, 2023-09-19

Was not able to quantify the amount of G’s sustained from anywhere in the logs. @Sean Odell do are there records on all replacements/fixes done to any aircraft that has gone through RMA? We are interested to know if any repairs were done to 408CW after this incident: https://jenaero.atlassian.net/browse/VIT2-193

### Sean Odell, 2023-09-19

@Hayden Jeanor I only have information on the RMA’s from the last 12 months, but most of that information is here in Jira.  We only recently (Last week) start working on gathering all the aircrafts AAR files that I get into RMA’s.  We have not stored that information historically.

As far as VXE-408 - 408 Wing Case has been associated with incident https://jenaero.atlassian.net/browse/RMA-114 .  This is the only incident I am aware of that happened after https://jenaero.atlassian.net/browse/VIT2-193 .

@Pat Wells FYI

### Pat Wells, 2023-09-20

@Hayden Jeanor 408CW was never returned on an RMA for evaluation or repair after the hard landing incident.

### Hayden Jeanor, 2023-09-20

Thank you @Pat Wells @Sean Odell

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20230908-223647.png | image | 179 | 2023-09-08 | listed only |
| image-20230911-180041.png | image | 67 | 2023-09-11 | listed only |
