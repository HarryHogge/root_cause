# FS2-4057: VXE-894 VXE-897 Did not Auto RTB after mission was complete

- **Issue type:** Task
- **Status:** In Review
- **Priority:** High
- **Created:** 2025-12-09
- **Updated:** 2026-09-04
- **Reporter:** Scott Whitney
- **Assignee:** Brandon Slater
- **Creator:** Scott Whitney
- **Links:** relates to VXEP-1611 (VXE-894 VXE-897 Did not Auto RTB after mission was complete)
- **Sprint:** FS2 Sprint 37, FS2 Sprint 36, FS2 Sprint 35, FS2 Sprint 39, FS2 Sprint 38

## Description

Fly mission attached to VXEP and verify the final orbit is either captured and that it transitions to the LZ or that the issue is replicated

## Comments (4)

### Scott Whitney, 2026-01-20

Reassigning to @Brandon Slater. Could you take a look at https://jenaero.atlassian.net/browse/VXEP-1611 - fly the attached mission and confirm that the final orbit is either captured and that it transitions to the LZ or that the issue is replicated

### Brandon Slater, 2026-01-20

@Scott Whitney have not reproduced issue, attached is the flight with the same mission as USDA. I’ll take a look at their AAR as well to see if they did anything different

### Brandon Slater, 2026-01-20

Flew mission with GCS 6.5.1 with BLK30 Adv Nav (type 115). Expected behavior (based on investigation): Vehicle continues last racetrack and does not RTB. Actual behavior: vehicle continues successfully RTBs after finishing the last racetrack

### Brandon Slater, 2026-01-29

Note: customer HIL had these faults:
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
Time: 057:24.890  Fault Status Changed: 0x00114000
```

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T115_V110_260120_150440_pack.zip | archive | 1773 | 2026-01-20 | listed only |
