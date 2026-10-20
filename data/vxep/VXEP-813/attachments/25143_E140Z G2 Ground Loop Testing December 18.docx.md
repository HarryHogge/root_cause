# E140Z G2 Ground Loop Testing December 18.docx

Attachment 25143, docx, 15 KB, added 2024-12-24 by Charles David Madewell.

December 18, 2024

Test 1

Aircraft: 734

Gimbal: E140ZG2 KIT  /  Serial: EPS6172

Power Supply: Brick

Gimbal Location for Test: Harness connected, Mount plate sitting on aircraft (no hardware)

Gimbal bounced and jerked (violently) during BIT and reported Tilt Encoder fault

Post BIT, the Gimbal would not move when commanded by GCS hand controller

This behavior was consistent through several power cycles.

This behavior matched GS team’s earlier observations

Instrument: Fluke 289 DMM / Serial: 65740008

Reading location between screws on top of gimbal mounting plate to screws on fuse (the ones that hold AV box) – Positive probe on gimbal, negative probe on aircraft

25.373VDC from power up until gimbal starts BIT

0.75VDC after BIT

These readings are comparable to values obtained by GS in their initial investigation

December 18, 2024

Test 2

Aircraft: 734

Gimbal: E140ZG2 KIT  /  Serial: EPS6172

Power Supply: Brick

Gimbal Location for Test: Harness connected, Gimbal on stand adjacent to (not touching aircraft)

Gimbal completed BIT and moved to home position

Post BIT, the Gimbal responded to operator commands as expected

Reading location between screws on top of gimbal mounting plate to screws on fuse (the ones that hold AV box) Positive probe on gimbal, negative probe on aircraft

Gimbal cable connected and power off: 0.5 to 0.75 MΩ

Power on during bit: 1.2 MΩ

Power on post bit: 0.75 MΩ

Power on until BIT: 25.427VDC

Power on during BIT: 0.75 to 1.2VDC

Power on after BIT: 0.75VDC

Power on after BIT: (meter and probes configured for DC current): Reading ~32 mA flowing from Gimbal to plane

December 18, 2024

Test 3

Aircraft: 734

Gimbal: E140ZG2 KIT  /  Serial: EPSXXXX (The one causing problems in AK)

Power Supply: Brick

Gimbal seems to complete BIT and move to home position.

Gimbal does not respond to operator commands

Gimbal moving counter clockwise very slowly uncommanded

No errors reported on BIT
