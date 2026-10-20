# HAVOC XCOM 5V Change.docx

Attachment 23769, docx, 580 KB, added 2024-10-02 by Jeremy Kostel.

|  |
|  |
| Document Number:  Revision:  Author: JEREMY KOSTEL Release Date: |
| CONFIDENTIAL AND PROPRIETARY DATA: Portions of this document contain proprietary technical data pertaining to items, or components, or processes, or other matter developed or acquired at the private expense of Edge Autonomy and is restricted to use only by Edge Autonomy employees or other persons authorized by Edge Autonomy in writing to use it. Neither said document nor said technical data shall be furnished or disclosed to, or copied or used by, persons outside Edge Autonomy, without the express written approval of Edge Autonomy. Markings on this page regarding confidentiality and proprietary information apply to this entire document.  EXPORT CONTROL WARNING NOTICE: WARNING – this document may contain technical data whose export is restricted by the Arms Export Control Act (Title 22, U.S.C. Sec 2751 et seq) or the Export Administration Act of 1979 (Title 50, U.S.C., App. 2401, et seq) as amended.  Violations of these export laws are subject to severe criminal penalties.  Disseminate in accordance with provisions of DoD Directive 5230.25.   Contains Export Controlled Information Not releasable to Foreign Persons unless authorized by 22 C.F.R. 120-130 or 15.C.F.R. 730-774. |

List of Figures

Figure 1: XCOM 5V Regulator

Figure 2: ESC Power Wiring Diagram

Figure 3: Video/SLA Wiring Diagram Pre-Changes

Figure 4: Video/SLA Wiring Diagram Post-Changes

Figure 5: Capture of 5V Signal on Startup Pre-Changes (Voltage-Yellow, Current-Blue)

Figure 6: Capture of 5V Signal on Startup Post-Changes (Voltage-Yellow, Current-Blue)

## Overview

## Problem Overview

The production Hargrave ESCs used in the HAVOC aircraft are currently incompatible with our system. This issue has been traced to the ESC startup sequence, specifically due to the 5V enable line. The 5V supply originates from the XCOM board, specifically from U4, which is a 5V regulator (LP2985-5, U4, datasheet).

Figure 1: XCOM 5V Regulator

A 100-ohm series resistor is placed on the ESC power line coming from U4. However, the ESC requires a minimum startup voltage of 3.1V and a transient startup current of approximately 30mA. The 100-ohm resistor introduces excessive resistance, causing the voltage to drop below the threshold necessary for ESC startup.

Figure 2: ESC Power Wiring Diagram

Additionally, the 5V regulator (U4) powers two other ICs on the XCOM board: U21 and U23. U23 is an inverting charge pump DC/DC converter (LTC1983-5, datasheet), while U21 is a switching multiplexer with an amplifier (AD8170ARZ, datasheet).

Figure 3: Video/SLA Wiring Diagram Pre-Changes

The largest power draw in this system is from U21, which amplifies a video signal, potentially drawing significant current. However, in our current configuration, the input (SA CAM VIDEO) and port J8 on the standard VXE30 are no longer in use. While the MAGNSS configuration has reintroduced the use of port J8, it does not rely on the SLA2k_VID_IN signal that U21 supplies.

To address these issues, the following changes have been proposed:

Removal of R142, R141, and R39 from the XCOM board.

Removing R141 and R142 will isolate U21, effectively cutting off power to the IC. While there is minimal risk in leaving U21 powered due to its lack of active input/output, it is preferable to remove these resistors as part of the current board modifications.

Removing R39 will resolve the voltage drop issue during ESC startup. The R39 pads should be connected via a solder bridge to maintain continuity.

These modifications are expected to enhance the compatibility and performance of the system, particularly in relation to the ESC startup.

Figure 4: Video/SLA Wiring Diagram Post-Changes

## Power Budget

The 5V regulator (U4) is capable of supplying up to 750mW (5V, 150mA). By removing R141 and R142, U21 is effectively isolated, leaving the ESC as the primary consumer of power from U4. Since U23 no longer has a load it draws an insignificant amount of power. The ESC draws approximately 150mW during startup (5V, 30mA) and 42mW during steady-state operation (5V, 8.4mA).

Even during the ESC’s startup phase, only 20% of the regulator’s total power capacity is utilized, ensuring there is sufficient headroom for reliable operation.

## Testing results

Initial benchtop testing revealed the voltage drop in our previous system (Figure 5), as well as the improved signal captured on an oscilloscope after implementing the proposed changes (Figure 6).

Figure 5: Capture of 5V Signal on Startup Pre-Changes (Voltage-Yellow, Current-Blue)

Figure 6: Capture of 5V Signal on Startup Post-Changes (Voltage-Yellow, Current-Blue)

Following these tests, the XCOM board was used to power the ESC during unloaded spin-up tests on the Iron Bird, as well as during loaded motor testing on the dynamometer. No issues were observed in any of the testing configurations.
