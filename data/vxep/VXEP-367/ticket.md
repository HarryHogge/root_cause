# VXEP-367: 12.8V Bus Current Limiting Issue (U5 X COM)

- **Issue type:** Improvement
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2024-04-17
- **Updated:** 2024-08-30
- **Resolved:** 2024-08-30
- **Reporter:** Maxime Jeanneau
- **Assignee:** Maxime Jeanneau
- **Creator:** Maxime Jeanneau
- **Parent:** XKIT-828 AGNSS: Perform Detailed Design Work
- **Links:** relates to VA-1343 (Heated Pitot V1 Electrical Design); relates to VA-1347 (Summarize power available for heated pitot. ); relates to ENG-346 (1607P01A Improvements. XCOM / XE240 PWR COMMS BD)
- **Epic Link:** XKIT-828
- **Issue color:** purple
- **Other Stakeholder (as required):** David Grosher
- **Leadership Stakeholder:** Greg Fryer

## Description

On testing of the 12.8V regulator (U5) on the XCOM board, it was noticed that a sustained overcurrent of the regulator (rated to 5A) did not trigger the over current protection of the chip and caused permanent damage to the regulator.
This power source is used by multiple devices including customer payloads. 
This ticket tracks a solution to prevent damage of this regulator when this bus exceeds it’s current limit. In the meantime, when powering devices from this bus, it must be estimated how much total current is being asked for, and made sure that it does not exceed the capacity of the bus.

## Comments (3)

### Maxime Jeanneau, 2024-04-17

@Cameron Chapman Here is the Jira ticket requested related to U5 on the XCOM board. Feel free to move it somewhere more appropriate or assign it to someone else.

### Maxime Jeanneau, 2024-04-17

@Rajesh Budhabhatti FYI

### Cameron Chapman, 2024-04-17

Thanks for tracking this @Maxime Jeanneauand @Rajesh Budhabhatti  . Here is where previous testing was logged. https://jenaero.atlassian.net/browse/VA-1347

## Attachments (0)
