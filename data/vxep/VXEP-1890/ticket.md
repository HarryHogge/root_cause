# VXEP-1890: VXE 902 - user power cycled aux 1&2 simultaneously, and lost comms with the A/C for ~2 minutes. CHAOS payload

- **Issue type:** Incident (8D)
- **Status:** D4 - Investigating Root Cause
- **Priority:** High
- **Created:** 2026-05-14
- **Updated:** 2026-09-24
- **Reporter:** Stephan Johnson
- **Assignee:** Drew Hildreth
- **Creator:** Stephan Johnson
- **Labels:** GS_Closed, Precision, RCCA, Software, Weekly-incident-tracker
- **Links:** relates to VXEP-1315 (B30 Systemic MCM Resets due to payload power); relates to VXEP-1956 (VXE 880 MCM Reset inflight after gimbal power cycle); relates to MS-1684 (VSM: Accommodate MCM Restarts in Flight); relates to VXEP-2005 (VXE 966 MCM reset led to uncommanded climb )
- **Customer:** Precision
- **Vehicle Tail Number:** 902
- **Corrective Action:** See See https://jenaero.atlassian.net/browse/VXEP-1315
- **Root Cause:** See https://jenaero.atlassian.net/browse/VXEP-1315
- **Severity:** 2 - Degraded Performance - No Workaround
- **Executive Summary:** Currently linked to MCM reset investigation on 880. Probable cause; Software Issue.

## Description

Configuration: 902 Adv Nav VXE. E95 gimbal and clarity on the hood. Flight was in support of CHAOS dev team. E95 wasn't responding to commands so I took control back from CHAOS. I went to payload power and selected aux 1&2 off, waited a few seconds and powered back on. When I pushed the "both on" button my GCS control window went from "you have control" to "reconnecting". It stayed in this state for about 2 mins before I refreshed the browser page. During the "reconnecting" phase, I still had SA cam feed and verified my silvus network stil had a strong and functioning connection via the webpage. After refresh, I was back in control of the AC, however, I had no mission on the map. I also had "reference alt has not been set" error. I called Redwire support and tried synchornize mission which failed.
I tried and was unable to create any new mission legs of any kind, likely due to the system thinking it hadn't yet gotten its pitot cal or test yet. The only feature that was working was the loiter here. I used that to descend and head back to the airfield and set up for a "land immediately/ Nudge" landing. The landing was accomplished without issue. We debated trying to release the VSM from the autopilot and picking up with JAI sw, but we thought there was too much risk if we were unable to grab it back and the OGCS no longer having a lost comm mission to fall back on.

## Plan

See updated plan in this issue for containment and customer notification plan: [VXEP-1315] MCM Reset on E140 Connection - Jira
- Aircraft and Chaos payload will be in HSV for test 6/3. 
- Need to develop measurement option for HSV. 
- @John Gober has Agilent current probe. Look at bandwidth number on that. @Laszlo Juhasz to ship Rogoski measurement if not.
- The current probe I have is a Keysight 1146B. Keysight Medium Wide Template
- JG - Teledyne LeCroy T3RC0120-UM Rogowski current probe on order 6/2; should be here 6/3
- @Abel J. Markow  @Connor Peebles  do you know where the previous inrush measurements are located for E140? We will want to know if that helps prevent this issue for newer gimbals, future E95s, etc.
- Measure E140, E95, Chaos, and combined E95+chaos inrush current and voltage transient when on an aircraft with battery connected.
- Provide guidance C/CA based on measurement.
- See recommended guidance in linked issue. @Drew Hildreth
- What PN and rev Avionics box do you have? We can probably answer this internally. @Kyle England @Trevor Gronner do we have records of which avbox this 902 received?
- Are 12V RTN and Vbatt/28V rtn isolated on your payload? They should be and can exacerbate this and similar issues if not.
- Can you measure the inrush current of your payload when connected to the aircraft/battery power? Reducing it should reduce the occurrence of this issue.

## Comments (12)

### Stephan Johnson, 2026-05-14

@David Grosher can you please take a look at this? Thanks!

### David Grosher, 2026-05-14

@Drew Hildreth @Greg Fryer @Mike DeJesus After reevaluating the timing of the incident in the flight, I believe that the VSM restarted and that the ethernet network across the aircraft experienced outages when the event occurred. I believe this is because the MCM restarted based on the gap in the tegra stats history log at 9:22:26 - 9:24:30 local time, which is inline with what has been observed with the E140 during power up with inrush current. I believe the event is seen in the XCOMM log at ~162309 UTC / 4259 XCOMM CpuTime and is captured in XCL00289.csv. I think to return to flight they could handle this procedurally by not power cycling the E95. 
```
[16:22:46.044 4253.044] sw 1 port link reset 1
[16:22:46.045 4253.046] sw 1 port link reset 2
[16:22:55.847 4262.848] sw 2 port link reset 2
[16:23:00.566 4267.566] ap link fault: local rx okay ap rx bad
[16:23:00.567 4267.568] ap link fault during transition/fw flight
[16:23:23.024 4290.024] sw 2 port link reset 2
[16:23:54.659 4321.659] link timeout
[16:23:54.661 4321.661] uplink state was/is: ACTIVE TIMEOUT
[16:24:30.303 4357.303] ap dbg: LOS!
[16:24:31.299 4358.299] connection query from: 10.131.134.30:50103
[16:24:31.300 4358.300] connection state reply: 1
[16:24:31.301 4358.302] reply sent to: 10.131.134.30:50150
[16:24:31.313 4358.313] config paired with: 10.131.134.30:50100
[16:24:31.314 4358.314] link paired with: 10.131.134.30:50012
[16:24:31.395 4358.395] uplink state was/is: TIMEOUT ACTIVE
```

### Cody Smisek, 2026-05-14

@David Grosher FYI
I was asked the following last week
[embedded: image-20260515-031820.png]
I attempted to gather additional information regarding why the question was being asked but was never updated regarding the context. 
Seems we have the answer now.

### Jackson Riley Curvin, 2026-05-26

@David Grosher the customer reached out asking some questions can you please help us answer these?
We discussed with Precision pilot this morning, and understand Redwire has researched the issue. Do you have supporting documentation from the dissected flight data AAR and VSM log file that was sent by Curtis that shows a timeline where the MCM was reset or current was exceeded? Has Redwire seen a powercycle impact E95 gimbal or is this an isolated event? Can you provide a hardware interconnect diagram for the Adv Nav Stalker which we can verify configuration?
FYSA @Drew Hildreth

### David Grosher, 2026-05-26

@Jackson Riley Curvin You will need to follow up with @Greg Fryer and @Mike DeJesus to get that data. And, the data rate during this phase of flight is very unlikely to capture any dynamic electrical transients. The Engineering team at this point is saturated and does not have bandwidth to support non-flight critical investigations.  @Drew Hildreth FYSA

### Cameron Chapman, 2026-05-28

@Jackson Riley Curvin this seems like the same issue/cause as this one. I am tagging up with the team to see the containment status of that.

### Cameron Chapman, 2026-05-28

https://jenaero.atlassian.net/browse/VXEP-1315

### Anthony Hansen, 2026-07-09

D/R

### Alexander Alan Arnold, 2026-07-09

@Anthony Hansen 880 has its own ticket with data

### Craig Burton, 2026-07-09

@Anthony Hansen Linking comment from VXEP-1956:  https://jenaero.atlassian.net/browse/VXEP-1956?focusedCommentId=98731

### Cameron Chapman, 2026-09-23

@Drew Hildreth was this aircraft ever sent back to HSV as the plan indicates?

### Drew Hildreth, 2026-09-24

@Cameron Chapman They never sent it back.

## Attachments (8)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_V902_20260514T172045Z.zip | archive | 39943 | 2026-05-14 | listed only |
| DATALOG - 902 Precision.zip | archive | 332406 | 2026-05-14 | listed only |
| Recording 2026-05-14 132713.zip | archive | 574021 | 2026-05-14 | listed only |
| image-20260515-031820.png | image | 26 | 2026-05-14 | listed only |
| vsm-info.05.14.2026 | other | 123188 | 2026-05-14 | listed only |
| AAR_V880_B30N_20260709T135535Z In Air reset.zip | archive | 39233 | 2026-07-09 | listed only |
| frontend-native-0023-2026-07-09.bin | other | 25286 | 2026-07-09 | listed only |
| [frontend-native-0023-2026-07-09.jsonl](attachments/63372_frontend-native-0023-2026-07-09.jsonl.md) | text | 2 | 2026-07-09 | converted |
