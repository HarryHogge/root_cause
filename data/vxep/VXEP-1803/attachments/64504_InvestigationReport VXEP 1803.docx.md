# InvestigationReport VXEP 1803.docx

Attachment 64504, docx, 127 KB, added 2026-09-11 by Charles Sweet.

|  |
|  |
| Incident Number:  Revision:  Author: C. Sweet Approver:  Date: |
| CONFIDENTIAL AND PROPRIETARY DATA: Portions of this document contain proprietary technical data pertaining to items, or components, or processes, or other matter developed or acquired at the private expense of RedWire Defense Tech and is restricted to use only by RedWire Defense Tech employees or other persons authorized by RedWire Defense Tech in writing to use it. Neither said document nor said technical data shall be furnished or disclosed to, or copied or used by, persons outside RedWire Defense Tech, without the express written approval of RedWire Defense Tech. Markings on this page regarding confidentiality and proprietary information apply to this entire document.  EXPORT CONTROL WARNING NOTICE:  WARNING – this document may contain technical data whose export is restricted by the Arms Export Control Act (Title 22, U.S.C. Sec 2751 et seq) or the Export Administration Act of 1979 (Title 50, U.S.C., App. 2401, et seq) as amended.  Violations of these export laws are subject to severe criminal penalties.  Disseminate in accordance with provisions of DoD Directive 5230.25.   Contains Export Controlled Information Not releasable to Foreign Persons unless authorized by 22 C.F.R. 120-130 or 15.C.F.R. 730-774. |

## Introduction and Executive Summary

## High Level Summary

On 3/30/2026, A flight was attempted with VTN VXE-658. Shortly after takeoff, the fuel cell cut out, forcing the aircraft to return using only power from the HLB.

Investigating the data shows that the vehicle’s nose cone fan was not initialized during the period of this flight. The ambient temperature read in the fuselage exceeded 85C for duration of the flight, compromising fuel cell electronics causing the eventual failure of the stack.

The reason for the nose cone fan not initializing appears to be the state in which the fuel cell was initialized.

## Root Cause

The primary root cause of the failure is identified as an unconcluded cooldown cycle prior to initialization of the fuel cell. Cooldown logic for the fuel cell identifies at what point the highest reading of the four thermocouples reaches a threshold of <150C before returning to an idle state awaiting next initialization. Seen in this case, initialization state is activated while the stack is cooling down – leading to a critical fault that sends the fuel cell into idle state after which it is re-initialized a second time. Not following the proper procedure in this case led to the aircraft launching without the appropriate support systems active (Nose Cone Fan).

## Root Cause Investigation Details

## XCL0042 Preliminary Data Review

Users provided the following:

| AAR Data File | FC Serial Number |
| XCOMM_658 | D4500563 |

Fig. 1 Temperatures vs. Stack State XCL0042

Seen in Fig. 1, The stack state changes directly from 6 to 2, at temperatures greater than 150C.

Fig. 2 Fan Rates vs Stack State XCL0042

The direct change from cooldown to initialization presents several problems. In cooldown, the cathode fans are running at maximum setpoints to remove excess heat from the system while the anode fans are not active. The direct transition into initialization activates the anode fans while the cathode fans are still producing a high amount of flow and backpressure inside of the system. This resistance to flow prevents the anode setpoints from being achieved, causing a critical fault and thus the system to shutdown again. The second instance of the stack entering cooldown is immediately ended as the systems temperatures are now <150, setting the stack into idle from which it initializes again. This final initialization works, but as this restart was completed outside of written operating procedure the fuel cell did not send the proper command to the aircraft to initialize the nose cone fan, causing the eventual over temp failure to the fuel cell electronics.
