# AV-717: 2135413-01 - XCOMM UAP - REV A01

- **Issue type:** Story
- **Status:** In Progress
- **Priority:** Highest
- **Created:** 2026-04-07
- **Updated:** 2026-10-09
- **Reporter:** Connor Peebles
- **Assignee:** Connor Peebles
- **Creator:** Connor Peebles
- **Parent:** AV-716 2135413-01 - XCOMM UAP - REV A
- **Links:** relates to VXEP-1786 (UAP Block 30 Adv Nav Hardware); relates to VXEP-1695 (Add JTAG debugging to future boards like XCOM with processors. ); relates to ENG-346 (1607P01A Improvements. XCOM / XE240 PWR COMMS BD)
- **Epic Link:** AV-716

## Description

Tracker for rev A01 of 2135413-01

## Plan

Current Design Restrictions:
- Cannot change shape of the board
- Cannot change external NHA (avibox) connections
- Cannot change software, except for what is targeted below


Threshold:
Update all parts to pull from the RedWire Defense Tech Altium 365 Workspace parts LibraryUpdate all MLCC’s to X7R or C0GUpdate CAN Transceiver to higher temp rated ‘ATA6561-GAQW-N’ or 'MAX33040E'Updated U10, delete 85C max version leaving 105C max versionGive R162 official placement see below “Use LDO for ethernet switches 1.2V“Replace all SK56B Schottky diodes with CDBB545LR-HFIncrease C73 by %5-%10Insert bleed down resistor to SD card powerReplace coincell battery with higher temp rated coincell batteryadd 2 pin connector for potential external battery powerAdd ethernet magnetics to external-to-board ethernet portsAdd differential impedance for Ethernet and CANRemove U21 and U23, SLA Video no longer supportedIncorporate SLA Breakout Board into XCOMMEnsure MCM power is not fused. Consider removing FET. Connect Pin61 (AN9/RPB14/SCK3/RB14) of CPU U24 to J2-46Fix J5-10 silkscreen marking errorReplace X5R 6.3V 22uF 0805 caps with x2 X7R 10V 10uF for better procurability and performanceReplace CAP CER 100UF 16V 20% X5R 1210 caps with 50V caps (& X7R)Use LDO for ethernet switches 1.2V
Reason: EMI caused WDT correction procedure 1.docx
Suppl: KSZ8895 LDO Design Considerationschange LED resistors to 499Add esd protection to external connections (TVS Diodes) that do not have internal protection on the ICsSN65C3232D obsolete, replaced w/ MAX3232-EPU2, U6, U20: remove part options that have max temp range below 125CU22 VRef, change part to high temp range part, up to 125CU24, upgrade to extended temp range version ('E')Layer stack change to 8 layers, adding 2 new GND layers sandwiching current layer 3
Objective
Add thermistorAdd JTAG debugging connector, U24 pins 56, 57, 58Add reverse polarity protection with an ideal diode mosfetadd 1-wire hardware identity IC, for Contract Manufacturer (CM) to flash to our specsoptions: Microchip 24AA02/24LC02/24C02Secure options: Microchip ATECC608/ATECC508, NXP SE050Get the SCM lowdown when needed

## Comments (0)

## Attachments (0)
