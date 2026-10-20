# Servo shaft position error.docx

Attachment 47011, docx, 16 KB, added 2026-03-05 by Ben Norris.

Servo shaft position error.

Initial detection of error: Servos arrived with physical offset of shaft in reference to body of servo when commanded to the 0 position.

Initial correction of error: Correcting the CAN sdo values listed in the Pegasus reference document of [0x2108][0x01] for the Neutral value or [0x607C] for the home position would result in either insufficient correction to align the shaft to the body and there would be a persistent offset between the commanded and detected shaft position.

Pegasus recommended correction of error: After a back and forth with a Pegasus representative the shaft offset was checked and corrected on the sdo address [0x212C][0x01] which appeared to fix the offset issue. However it was noted as being strange that the value was non zero and unique for each servo indicating technicians at Pegasus had set the value correctly during production.

Persistence of error: The corrected servos were found to have returned to their individual shaft offset after being processed and verified to have the correct home position. It was communicated to Pegasus and we were asked to keep an eye on this issue since it only seemed to affect servos that initially presented as having incorrect home position. Also every time a shaft offset was changed and then returned to original offset were found to have the same value in the [0x212C][0x01] address even though the physical position was reset.

Review: Shaft position offset is controlled by [0x212C][0x01] this position offset appears to be getting physically rest while the stored value stays the same.

Notes:

CANopen: A standardized application-layer protocol built on top of CAN bus, defining how devices discover, configure, and exchange data with one another.

Node: Any device participating on the CANopen network (e.g., a servo drive, controller, or sensor).

Object Dictionary (OD): A structured table of parameters internal to each CANopen device, analogous to a register map. Each entry is identified by an index (e.g., 0x212C) and an optional subindex (e.g., [0x212C][0x01]).

SDO (Service Data Object): A CANopen messaging service used to read or write individual Object Dictionary entries — effectively reading/writing device registers for configuration, calibration, or diagnostics.

PDO (Process Data Object): A CANopen messaging service for real-time, cyclic exchange of process data (e.g., position feedback, torque commands) without the request/response overhead of SDOs.
