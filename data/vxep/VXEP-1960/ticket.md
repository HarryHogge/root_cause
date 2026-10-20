# VXEP-1960: VXE HIL-102 6.7.1 Operator commanded RTB, but aircraft executed land Immediatley

- **Issue type:** Bug
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2026-07-15
- **Updated:** 2026-08-11
- **Resolved:** 2026-08-11
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Melika Dabiri
- **Creator:** Alexander Alan Arnold
- **Links:** relates to MS-1704 (VXEP-1960 - Investigation - Vehicle landed Immediately after RTB command); relates to RMA-1071 (HIL-102      RMA-260729-1 )

## Description

During the first HIL flight with the 6.7.1 software the HIL aircraft was commanded to RTB but instead performed a Land Immediately. AAR attached without FDR. FDR download repeatedly failed.
 
The HIL flight was with the 6.7.1 software on the “Jennings” GCS. No MCM/VSM, VCSi.
 
The 6.7.1 HIL firmware was used; AP 6.05W / 0x8386, XCOMM 4.76 / 0x4A8B, VTOL 1.60 / 0x28EA.

As you probably noticed the GCS.ini file shows LandOnError=0, also there were no symptoms in the GCS software similar to those described in AN 26-001. I did notice that IP1 of the PLZ was the active waypoint (orange) even though the aircraft was landing somewhere else.

## Comments (2)

### Alexander Alan Arnold, 2026-07-15

not sure who you guys assign these to. last time LM reached out to us Dave said hed have someone on the team work with LM as 6.7.1 wasn't released so the FSR team didn't need to work the issue @Ted Trowbridge @Scott Whitney

### Alexander Alan Arnold, 2026-07-20

added more screenshots and updated issue statement

## Attachments (6)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 6.7.1 HIL.vmis | other | 4 | 2026-07-15 | listed only |
| T95_V102_260714_163608_pack.zip | archive | 435 | 2026-07-15 | listed only |
| processed-126DE237-2810-470A-8D55-399AA7294D66.jpeg | image | 1025 | 2026-07-20 | listed only |
| processed-8159A2DF-279B-47FD-ADE3-F3F5F8A9F38E.jpeg | image | 1323 | 2026-07-20 | listed only |
| processed-D56665B6-781F-4B16-B3EB-A55CA80B0BF7.jpeg | image | 1072 | 2026-07-20 | listed only |
| processed-E8C73D98-88FA-4B96-8CD1-8633A758FD4B.jpeg | image | 1403 | 2026-07-20 | listed only |
