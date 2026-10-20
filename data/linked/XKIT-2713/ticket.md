# XKIT-2713: MAGNSS Thermal Testing

- **Issue type:** Epic
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2024-08-05
- **Updated:** 2025-09-19
- **Resolved:** 2025-08-12
- **Reporter:** Cameron Chapman
- **Assignee:** Steve Gonzales
- **Creator:** Cameron Chapman
- **Links:** relates to XKIT-2657 (Pre-MAGNSS Thermal Testing and Actions); relates to ENG-2707 (Define maximum vehicle temperatures and shade requirements, update manuals. ); relates to XKIT-2695 (Heat Sink on XCOMM); relates to XKIT-2706 (Thermal Test Planning for Production); relates to ENG-2649 (PreMAGNSS Avi Enclosure Fail Checkout #2 P-S100141); relates to FS2-2522 (B30+40: Implement 12V load shedding when vbatt gets too low or overcurrent detected. )
- **Production Stakeholder:** Matt Philley
- **Other Stakeholder (as required):** Wesley Lilienthal
- **Leadership Stakeholder:** Greg Fryer

## Description

Current plan is to have this due for production delivery. Nice to have for the initial 4, but unlikely we will be able to fit it in before the deadline. @Ryan Babigian can you please insert this into production schedule.
Rough outline
- Create test plan based on thermal requirements in CDR (or document requirements if not done)
- Able to idle indefinitely at max OAT.
- Execute test plan and verify requirements are met.
- Document test and record actions.

## Comments (3)

### Ryan Babigian, 2024-08-07

Issue captured on production list and ticket https://jenaero.atlassian.net/browse/XKIT-2706 previously created

### Matt Philley, 2024-08-22

When this task is being planned and executed please reach out to @Liam Limon we are concerned the added components and heat is causing weird new problems with the XCOMM. 
AC 517 (RMA/Engr Retro) - SCO - Aircraft Not Connecting to GCS
AC 509 (RMA/Engr Retro) - QA - SW Loading Issue
Potential issue on AC 704 will add NCR if confirmed

“Ok. That would be good to start tracking. Thermals would be good too but I think just time on with all the new electronics in the enclosure would be good. It seems to me like the xcomm failures we’re seeing are long term temperature exposure issues and they’re presenting as slow failures. I find it really similar to GoPros or DJI VTXs for quads. They have passive designs and they work great while everything’s moving but if you try to do long term bench work with them or park them in the sun they start to get weird.”

### Cameron Chapman, 2024-08-23

Below is the SSD temperature data that was collected on vehicle 691 on its flight test using OGCS/VCSi.  There were 3 flights that afternoon -- note the rapid temperature drop once the vehicle was aloft.  Note also the apparent decline in ambient temperature at the field between 3 PM and 8 PM.
[embedded: image-20240823-124212.png]
 Thanks Craig. Do you have ambient temps plotted or recorded for that time period? Along with launch and landing times? 140f is pretty concerning for some of the other avionics.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20240823-124212.png | image | 43 | 2024-08-23 | listed only |
