# FS2-1759: Fuel cell and HLB state of charge

- **Issue type:** Epic
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-04-18
- **Updated:** 2024-05-30
- **Resolved:** 2024-05-30
- **Reporter:** Scott Whitney
- **Assignee:** Jason Scherer
- **Creator:** Scott Whitney
- **Labels:** USASOC
- **Components:** Vehicle Incident Support 
- **Links:** clones VXEP-368 (VXE 523 multiple faults with HLB discharging while in fuel cell configuration); relates to FS2-1758 (v523 Investigation Fuel Cell and HLB issue seems to be Faulty Air Speed Data)
- **Vehicle Tail Number:** 523
- **Problem Type:** Other (explain in description)
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

Information received from customer:
Over the last 72 hours we have had several faults we believe relate to the fuel cell configuration. Upon launching the aircraft, the HLB will continue discharging. The fuel cell operation window was also reporting a battery current of "-10". We chose to immediately start the landing sequence 10 minutes after launch. At IP1 the HLB was reporting a 40% state of charge while still continuously discharging. The aircraft was reporting failure to maintain altitude.

AAR file attached

## Comments (3)

### Jason Scherer, 2024-04-19

@Scott Whitney I think this is the ticket you meant to assign to me. I added some charts to the other ticket before I realized it pertained to an X-Kit flight. I’ll move them to this ticket.

### Scott Whitney, 2024-04-20

@Jason Scherer this is the epic. https://jenaero.atlassian.net/browse/FS2-1758 is the task created from the incident findings task. Feel free to attach any finding here, they are both linked to https://jenaero.atlassian.net/browse/VXEP-368

### Scott Whitney, 2024-05-30

Investigation found that this was an air speed data issue relating. Investigation for air speed data being done in another task (https://jenaero.atlassian.net/browse/VXEP-368#icft=VXEP-368)

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V523_240418_174902_pack.zip | archive | 2997 | 2024-04-18 | listed only |
