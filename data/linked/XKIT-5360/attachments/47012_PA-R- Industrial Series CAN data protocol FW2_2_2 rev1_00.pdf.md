# PA-R- Industrial Series CAN data protocol FW2_2_2 rev1_00.pdf

Attachment 47012, pdf, 354 KB, added 2026-03-05 by Ben Norris.

## Page 1

CANopen Data Protocol for Industrial Actuators
Firmware 2.2.2
Document Revision:
1.0
Released
2025-05-13

## Page 2

CANopen Data Protocol for Industrial Actuators
This document is intended to be used by Pegasus Actuators GmbH customers and personnel
as an aid to understand the Pegasus Actuators data protocol interface for the Actuator series.
The interface data contained herein have been compiled from design specifications, simulation
results and testing. Due to the ongoing nature of the program, data contained herein are subject
to change without notice.
Unauthorized distribution of this document to third parties, or use of this document for any
purpose other than that stated above is strictly prohibited.
Firmware 2.2.2, Rev.1.0 www.pegasus-actuators.com 2

## Page 3

CANopen Data Protocol for Industrial Actuators
Contents
1 Available Object Dictionary Entries (apart from CANopen standardized entries) 2
1.1 Communication Profile . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.2 Manufacturer defined entries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.3 CiA 402 entries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
2 Possible EMCY messages (apart from CANopen standardized messages) 6
3 Quick Start 6
4 Commands with special timing requirements 7
5 Setting the Node ID and CAN bitrate 7
Firmware 2.2.2, Rev.1.0 www.pegasus-actuators.com 1

## Page 4

CANopen Data Protocol for Industrial Actuators
1 Available Object Dictionary Entries (apart from CANopen
standardized entries)
Selected entries are included here for better understanding even though they are technically
part of the CANopen base specification or CiA 402.
1.1 Communication Profile
 Entirely defined by the CANopen base standard, see standard for all details. Noteworthy
entries:
 0x1017, 0x00 – Producer Heartbeat Time [ms] (UInt16, R/W)
◦ If > 0, the actuator will send a heartbeat message every X milliseconds
 0x1018, 0x02 – Product Code (UInt32, R)
◦ Contains the first digits of the actuator model number
◦ e.g. PA-R-340-7-C-24-N-315-00 becomes 340724315 (0x144F0A5B)
 0x1018, 0x03 – Revision Number (UInt32, R)
◦ Software revision number in the format 0x00MMmmPP
◦ MM = Major version, mm = minor version, PP = patch version
◦ e.g. 2.1.4 becomes 0x00020104
 0x1018, 0x04 – Serial Number (UInt32, R)
◦ Actuator serial number in integer form
◦ e.g. 2407023 becomes 0x24BA6F
1.2 Manufacturer defined entries
 0x2002, 0x00 – Motor Temperature [°C] (Int8, R)
◦ Measured temperature at the outside of the motor inside the actuator
 0x2003, 0x00 – Motor Current [mA] (UInt16, R)
◦ Measured current draw of the motor in mA
 0x2004, 0x00 – Signed Motor Current [mA x10] (Int16, R)
◦ Measured current draw of the motor in mA with the sign depending on rotation di-
rection
 0x2200, 0x00 – Recall Factory Settings (Bool, W)
◦ Resets all parameters related to the movement to factory values if True is written
Firmware 2.2.2, Rev.1.0 www.pegasus-actuators.com 2

## Page 5

CANopen Data Protocol for Industrial Actuators
 0x2E00, 0x00 – Overload Counter (UInt8, R)
◦ Number of encountered overload events where the motor saver was activated
 0x2E01, 0x00 – Motor Overtemperature Counter (UInt8, R)
◦ Number of encountered motor overtemperature events
 0x2E02, 0x01 to 0x03 – Hour Meter 1 to 3 [min] (UInt32, R)
◦ Three copies of the total powered time counter in minutes
1.3 CiA 402 entries
 0x6040, 0x00 – Controlword (UInt16, R/W)
◦ Bit explanations:
• Bits 0 to 3 and 7: Used to represent the various CiA 402 state machine commands
• Bit 4 / New set-point: If set, new target positions will be processed. If not set, they
will be ignored.
• Bit 5 / Change set immediately: If set, new target position will take effect imme-
diately. If cleared, New target position will only take effect once the criteria for
Statusword bit 10 (“Target reached”) have been met, which means this can be
used tu “queue up” several target positions.
• Bit 6 / abs/rel: If cleared, target positions are treated as absolute positions, i.e.
target position -45° means “move to -45°. If set, target positions are treated as
relative offsets to the current target position. If there is no previous target position,
the relative movement will be based on the current output shaft position instead.
Firmware 2.2.2, Rev.1.0 www.pegasus-actuators.com 3

## Page 6

CANopen Data Protocol for Industrial Actuators
• Bit 7 / Fault reset: Used to exit from a “Fault” state (on rising edge of this bit)
• Bit 8 / Halt: If set, motor will be disabled immediately
• Bits 9 to 15: Unused
 0x6041, 0x00 – Statusword (UInt16, R)
Firmware 2.2.2, Rev.1.0 www.pegasus-actuators.com 4

## Page 7

CANopen Data Protocol for Industrial Actuators
◦ Bit explanations:
• Bits 0 to 3, 5 and 6: Used to represent the various CiA 402 state machine states
• Bit 4 / Voltage enabled: unused
• Bit 7 / Warning = Overtemperature Error as defined in RS485 protocol datasheet
• Bit 8 = Overload Error as defined in RS485 protocol datasheet
• Bit 9 / Remote: Always set
• Bit 10 / Target reached: Set if the output shaft position is within 0.5 degrees of the
setpoint, cleared otherwise. Also set after the Halt bit in the Controlword has been
set and the motor has been disabled.
• Bit 11 / Internal limit active = Angle Limit Error as defined in RS485 protocol
datasheet
• Bit 12 / Set-point acknowledge: Set if Bit “New set-point” in the Controlword is set
and the most recent setpoint is valid. Cleared otherwise.
• Bit 14 = Power Stage Error as defined in RS485 protocol datasheet
 0x6064, 0x00 – Position actual value [1/1000 °] (Int32, R)
◦ Current output shaft position in 1/1000 degrees
 0x607A, 0x00 – Target position [1/1000 °] (Int32, R/W)
◦ Target position in 1/1000 degrees
 0x607B, 0x01 – Min position range limit [1/1000 °] (Int32, R/W)
◦ Hard position range limit. If exceeded, will wrap around. Should not normally be
changed.
Firmware 2.2.2, Rev.1.0 www.pegasus-actuators.com 5

## Page 8

CANopen Data Protocol for Industrial Actuators
 0x607B, 0x02 – Max position range limit [1/1000 °] (Int32, R/W)
◦ Hard position range limit. If exceeded, will wrap around. Should not normally be
changed.
 0x607C, 0x00 – Home offset [1/1000 °] (Int32, R/W)
◦ Neutral position offset in 1/1000 degrees
 0x607D, 0x01 – Min position limit [1/1000 °] (Int32, R/W)
◦ Soft position limit in 1/1000 degrees. If exceeded, will stop at limit and set “Internal
limit active” in Statusword.
 0x607D, 0x02 – Max position limit [1/1000 °] (Int32, R/W)
◦ Soft position limit in 1/1000 degrees. If exceeded, will stop at limit and set “Internal
limit active” in Statusword.
 0x607E, 0x00 – Polarity (UInt8, R/W)
◦ If set to 0x00, actuator operates normally. If set to 0x80, output shaft movement will
be mirrored.
2 Possible EMCY messages (apart from CANopen
standardized messages)
Selected messages are included here for better understanding even though they are technically
part of the CANopen base specification or CiA 402.
 0x4310 – Motor overtemperature
 0x5410 – Motor driver (“power stage”) error
 0x6320 – Parameter error
 0x90E0 – Overload
3 Quick Start
To quickly get started without much prior CANopen knowledge, here are some standard com-
munication flows to initialize an actuator and command it to move.
1. Power up actuator, wait for “Bootup” message sent by actuator (ID 0x700 + Node ID)
2. Set NMT state “Operational” (ID 0x000, NMT state 0x01)
Firmware 2.2.2, Rev.1.0 www.pegasus-actuators.com 6

## Page 9

CANopen Data Protocol for Industrial Actuators
3. Set Controlword “Shutdown” 1 consisting of Controlword bits “Quick stop” 2 and “Enable
voltage” (RPDO 1, Controlword 0x0006)
4. Set Controlword “Switch On” consisting of Controlword bits “Quick stop”, “Enable voltage”
and “Switch on” (RPDO 1, Controlword 0x0007)
5. To command a position, set Controlword “Enable operation” consisting of Controlword bits
“Enable operation”, “Quick stop”, “Enable voltage” and “Switch on” as well as Controlword
bits “New set-point” and “Change set immediately” and set Target position according to
your needs (RPDO 2, Controlword 0x003F , Target Position user-defined)
6. The actuator should now move to the target position. To read the current position, send
SYNC (ID 0x080), to which the actuator will respond with TPDO 2 (Statusword + Current
position)
4 Commands with special timing requirements
The following CANopen commands require synchronicity between channels 1 and 2 (The same
command needs to be sent on both channels within a certain time, without other commands
interfering) to avoid triggering a redundancy error:
 Setting NMT state to “Stopped”
 Setting NMT state to “Pre-Operational”
 Executing the “Quick Stop” action via the Controlword
 Executing the “Halt” action via the Controlword
 Executing the “Clear Fault” action via the Controlword
 Entering the “Switched on”, “Ready to switch on” or “Switch on disabled” states via the
Controlword
 Sending target positions via RPDO 2
5 Setting the Node ID and CAN bitrate
The node ID and bitrate can be set via the CANopen standardized LSS protocol.
1Even though it is called „Shutdown“ and can be used for that purpose, it is also used during initialization.
2The „Quick stop“ bit is active-low, so it is usually set to 1.
Firmware 2.2.2, Rev.1.0 www.pegasus-actuators.com 7

## Page 10

CANopen Data Protocol for Industrial Actuators
This document is intended to be used by Pegasus Actuators GmbH customers and personnel
as an aid to understand the Pegasus Actuators data protocol interface for the Actuator series.
The interface data contained herein have been compiled from design specifications, simulation
results and testing. Due to the ongoing nature of the program, data contained herein are subject
to change without notice.
Unauthorized distribution of this document to third parties, or use of this document for any
purpose other than that stated above is strictly prohibited.
Pegasus Actuators GmbH
Am Kalkofen 8
D - 61206 Wöllstadt
Germany
Tel: +49 6034 / 93 99 699
Fax: +49 6034 / 93 99 701
http://www.pegasus-actuators.com
Firmware 2.2.2, Rev.1.0 www.pegasus-actuators.com 8
