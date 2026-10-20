# FS2-749: Embedded SW Robustness Initiative

- **Issue type:** Epic
- **Status:** In Process
- **Priority:** High
- **Created:** 2023-08-22
- **Updated:** 2025-10-13
- **Reporter:** David Grosher
- **Creator:** David Grosher
- **Components:** Emb SW Robustness, WDT Investigation
- **Links:** blocks VXEP-9 ((Duplicate) TPTR-74 VXE 510 Watchdog Software Fault); blocks VXEP-11 (TPTR-5 VXE 407: (VTOL-AP-WD) Unexpected Behavior Seen During Vertical Landing)

## Description

Split this Epic into the following Epics. Create a Component or Label to add to link to the Embedded SW Robustness effort. 
- fix for UDP initialization (1080) https://jenaero.atlassian.net/browse/FS2-1080
- FreeRTOS v10 Upgrade (881, 891, 597, 811, https://jenaero.atlassian.net/browse/FS2-1708
- Eliminate Compiler Warnings (1126, 1222, 961, https://jenaero.atlassian.net/browse/FS2-1709
- I2C driver fix (1378) https://jenaero.atlassian.net/browse/FS2-1378
- Static Memory Allocation (598,1221, 748, 746, 1344, 1624, 1625, 1589, 1590, 1622, 1621, 1620, 1645, 1623, https://jenaero.atlassian.net/browse/FS2-1710
- X32 Compiler https://jenaero.atlassian.net/browse/FS2-1509
- Watchdog Task Monitoring (1226, 1422 (Close will not do), 917, 1304, https://jenaero.atlassian.net/browse/FS2-1711
- Clean up Dev Environment (812, 601 https://jenaero.atlassian.net/browse/FS2-1712
- Disable unused peripherals (1167, 1153, 1280, 1242, 1608, https://jenaero.atlassian.net/browse/FS2-1713
- Disable Webserver in Flight (1263, 1435, 1548, 1549, https://jenaero.atlassian.net/browse/FS2-1714
- Common XCOMM/AutoPilot sub Module (963) https://jenaero.atlassian.net/browse/FS2-963
- Task Frequency Reduction (993, 995) https://jenaero.atlassian.net/browse/FS2-1715
- Semaphore Robustness (921, 915, 969)https://jenaero.atlassian.net/browse/FS2-1716
- bootloader robustness (906, 868, 865, 862, 861, 896) https://jenaero.atlassian.net/browse/FS2-1717
- data integrity across task boundaries (910) https://jenaero.atlassian.net/browse/FS2-910
- i2c driver common code across busses (860, 1546) https://jenaero.atlassian.net/browse/FS2-1718
- Update compiler (626) https://jenaero.atlassian.net/browse/FS2-626
- Sensor Consolidation (607, 1038, 1260) https://jenaero.atlassian.net/browse/FS2-1719
- Debug logging robustness (610, 1002)https://jenaero.atlassian.net/browse/FS2-1720
- RTC handling (1371, 1396, 1389) https://jenaero.atlassian.net/browse/FS2-1721
- Consolidate File I/O (1084 1545, 1566,) https://jenaero.atlassian.net/browse/FS2-1722
- Consolidate UDPService tasks (1087) https://jenaero.atlassian.net/browse/FS2-1087
- Core Time Rollover (1353) https://jenaero.atlassian.net/browse/FS2-1353
- Bad Mag data (1604, 1605, 1606 move to bad mag epic) https://jenaero.atlassian.net/browse/FS2-1674


*All of the above that have struckthrough are done/canceled.
All epics have component= Emb SW Robustness


Moved out of Robustness 
- Universal Autopilot (869) - https://jenaero.atlassian.net/browse/FS2-250

## Comments (2)

### Christa Meck, 2025-10-13

@David Grosher Is all this stuff still a thing or are we past it all at this point?

### David Grosher, 2025-10-13

@Christa Meck This was the original Epic that we used to capture tasks and learnings while trying to increase the robustness of the system.  Scott has split the epic into smaller epics per the description but I’m not sure why there would still be child items here unless they were duplicated for documentation purposes. @Scott Whitney can you provide some insight here?

## Attachments (0)
