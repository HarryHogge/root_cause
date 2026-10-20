# VXEP-1541: Integrate and Validate Sensor Inputs to Processor Board

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2025-10-07
- **Updated:** 2026-05-11
- **Resolved:** 2026-05-11
- **Reporter:** Tobi Ogunro
- **Assignee:** Adrian Garcia
- **Creator:** Tobi Ogunro
- **Parent:** VXEP-1189 Electrical - Wing Utility Pylon (FKA drop payload)
- **Epic Link:** VXEP-1189

## Description

Ensure proper electrical integration of sensor inputs (PN 100-117037) to the onboard processor for new pylon configuration.

## Plan

Deliverables / Action Items:
Define pinout and sensor wiring interface.Validate sensor input signals on processor (bench test).Document configuration and connection mapping.Upload updated schematic and wiring notes to SharePoint.

## Issue Status

Power: 
Since the sensors are rated to 24V and not 28V an fixed 24V 100mA LDO is used to power the sensor. The current consumption according the the datasheet is 15mA so the 100mA should be more than enough margin. 
System Integration: 
The GX-F8A is an NPN open collector proximity sensor, which means its output transistor can only connect the output wire to ground — it cannot drive it high.
- When the sensor detects something, it turns on that transistor → the output line is connected to ground (0 V).
- When it doesn’t detect anything, the transistor is off, and the output line is floating (not connected to anything).

Because it can’t drive the signal high by itself, you need an external resistor to pull the line up to a known logic level (like 3.3 V).
A pull-up resistor connects the sensor output line to 3.3 V.
- When the sensor output transistor is off (no object detected), the resistor gently pulls the signal up → the microcontroller sees a HIGH (3.3 V).
- When the sensor turns on (object detected), it pulls the output line down to LOW (0 V) by connecting it to ground.

Without the pull-up, the output line would “float” when the sensor is off — meaning the voltage could randomly drift high or low, causing unreliable readings.
The flying leads of the sensors are connected to molex microlock plus connectors. Since there are 2 sensors in the assembly, one of them is a 3pin connector and the other is a 4pin connector to avoid mismating. The pinout and pn for the connectors can be see below. 
[embedded image-20251013-210951.png]
[embedded image-20251013-211006.png]
[embedded image-20251013-211030.png]
[embedded image-20251013-211041.png]

## Comments (2)

### Tobi Ogunro, 2025-10-13

@Adrian Garcia checking in on the sensor integration.

### Connor Peebles, 2026-05-11

Sensor integration electrically and software sound, some mechanical hiccups. Closing

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20251013-210951.png | image | 49 | 2025-10-13 | listed only |
| image-20251013-211006.png | image | 203 | 2025-10-13 | listed only |
| image-20251013-211030.png | image | 38 | 2025-10-13 | listed only |
| image-20251013-211041.png | image | 8 | 2025-10-13 | listed only |
