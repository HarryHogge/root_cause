# VXEP-1611: VXE-894 VXE-897 Did not Auto RTB after mission was complete

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed, but added to Bermuda Triangle List
- **Resolution:** Cannot Reproduce
- **Priority:** Highest
- **Created:** 2025-11-18
- **Updated:** 2026-09-23
- **Resolved:** 2026-09-23
- **Reporter:** Jackson Riley Curvin
- **Assignee:** Scott Whitney
- **Creator:** Jackson Riley Curvin
- **Labels:** RCCA, Software, USSS, Weekly-incident-tracker
- **Links:** relates to FS2-4057 (VXE-894 VXE-897 Did not Auto RTB after mission was complete)
- **Customer:** USSS
- **Vehicle Tail Number:** VXE-894
- **Vehicle Configuration:** ADV NAV Main Battery
- **Severity:** 3 - Degraded Performance - With Workaround
- **Components (EA Aircraft):** Aircraft, full assembly
- **Contract/Customer First Need:** USSS
- **Executive Summary:** Issue unclear. unable to reproduce. Customer has not reported issue again. Probabale cause; Software Issue.

## Description

While conducting flights with USSS, we observed an issue with the aircraft not initiating its automatic RTB sequence. After the aircraft completed its final racetrack, it did not RTB on its own. After approximately four minutes with no action, I instructed the operator to manually command RTB.
On Day 2, the same issue occurred on the second flight of the day. Once the aircraft landed, I asked whether SUAV had been closed following the previous flight, and it had not. After fully closing and reopening SUAV, we launched the aircraft again with no issues. Upon mission completion, the aircraft auto-RTB’d as expected, with a delay of roughly two minutes.

## Comments (17)

### David Grosher, 2025-11-18

@Scott Whitney can you have someone fly the attached mission and confirm that the final orbit is either captured and that it transitions to the LZ or that the issue is replicated.

### Jackson Riley Curvin, 2026-01-20

@Anthony Hansen did you run this mission on our HIL sim in HSV?

### David Grosher, 2026-01-20

@Scott Whitney It was requested by global support that this ticket be prioritized.

### Anthony Hansen, 2026-01-20

@Jackson Riley Curvin Yes I did. The aircraft did not RTB after the expiration of the last primary mission element. It did RTB eventually to the PLZ, and before Auto Low Battery RTB would have done it.

### Jackson Riley Curvin, 2026-01-21

@David Grosher

### Scott Whitney, 2026-01-22

@Jackson Riley Curvin @Anthony Hansen  - were you able to recreate this issue?

### Jackson Riley Curvin, 2026-01-23

@Scott Whitney

### Brandon Slater, 2026-01-29

@Scott Whitney after completing the final racetrack did the customer explain what the vehicle did? Such as did it keep doing the race track, fly straight forever, etc. Noticed that it is only mentioned that “no action” occurred

### Brandon Slater, 2026-01-29

@Anthony Hansen after completing the race track did the vehicle keep orbiting around the race track?

### Anthony Hansen, 2026-01-30

@Brandon Slater I would like to say the first test in our HIL had similar results as my test flight today. 
When I ran their mission today (no wind and without ever re-tasking the aircraft in flight), the aircraft would have left the racetrack for IP1 at around the 14:20 elapsed time mark. The aircraft kept flying the racetrack through the timer expiration, and eventually RTB’d to IP1 at around the 16:57 elapsed time mark.

### Scott Lovett, 2026-02-02

Adding this to Tuesday meeting agenda.

### Jackson Riley Curvin, 2026-06-30

@Brandon Slater @Scott Whitney  Can we get a status update please? What are the recommended next steps?

### Alexander Alan Arnold, 2026-07-20

@Scott Whitney @Ted Trowbridge Are we going to be able to recreate this? If not, what is the recommended next steps?

### Scott Whitney, 2026-07-27

@Alexander Alan Arnold - we have note been able to recreate this issue.
 
Flew mission with GCS 6.5.1 with BLK30 Adv Nav (type 115). Expected behavior (based on investigation): Vehicle continues last racetrack and does not RTB. Actual behavior: vehicle continues successfully RTBs after finishing the last racetrack

### Scott Whitney, 2026-07-27

@Ted Trowbridge -  brandon did call out that the GCS Event log from the HIL Flight had the following

```
Time: 004:27.859  Fault Status Changed: 0x00014000
Time: 024:04.437  Launch wizard started
Time: 024:45.078  Fault Status Changed: 0x00034080
Time: 025:08.421  Fault Status Changed: 0x00014000
Time: 027:39.937  Launch wizard canceled
Time: 027:54.671  Launch wizard started
Time: 028:02.843  Fault Status Changed: 0x00034080
Time: 028:28.718  Fault Status Changed: 0x00014000
Time: 029:48.937  Mission save: C:\Users\Public\Documents\My GCS\Missions\USDA Test Field mission 1.vmis
Time: 040:10.531  Vehicle AZ: : 0.000000  0.000000
Time: 040:10.531  Ref Elev: : 144  0
Time: 040:55.562  Mission save: mission.txt
Time: 041:34.843  Vehicle AZ: : 0.000000  0.000000
Time: 041:34.843  Ref Elev: : 144  0
Time: 041:57.468  Auto mode automatically activated
Time: 042:15.781  Launch wizard complete
Time: 042:15.781  Auto mode automatically activated
Time: 042:15.796  Launch detected: 0.000000  0.000000
Time: 042:50.140  Auto mode automatically activated
Time: 042:50.140  Auto mode automatically activated
Time: 043:06.140  Fault Status Changed: 0x24014000
Time: 043:09.328  Fault Status Changed: 0x00014000
Time: 043:31.187  Fault Status Changed: 0x00114000
Time: 043:41.203  Fault Status Changed: 0x00014000
Time: 046:29.703  Fault Status Changed: 0x00114000
Time: 046:39.609  Fault Status Changed: 0x00014000
Time: 054:52.093  Fault Status Changed: 0x00114000
Time: 055:00.703  Fault Status Changed: 0x00014000

```

### Pat Wells, 2026-08-12

@Scott Whitney any update on this?
@Alexander Alan Arnold  @Drew Hildreth  FYSA

### Alexander Alan Arnold, 2026-09-23

Customer has not reported issue again and has been swapped to OGCS capable aircraft. closing and adding to Bermuda triangle

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T115_V894_251118_111723_pack.zip | archive | 2018 | 2025-11-18 | listed only |
| T115_V897_251117_121101_pack.zip | archive | 2727 | 2025-11-18 | listed only |
| USDA Test Field mission 1.vmis | other | 4 | 2025-11-18 | listed only |
