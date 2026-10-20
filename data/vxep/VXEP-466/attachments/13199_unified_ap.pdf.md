# unified_ap.pdf

Attachment 13199, pdf, 528 KB, added 2023-03-22 by Cameron Chapman.

## Page 1

Unified Autopilot v1.0Kurt Burian3/8/2023Edge Autonomy - Propritary and Confidential

## Page 2

VXE EXISTINGXCOMMVTOL INTERFACE BOARDVTOL APFIXED WING APCirc ConnPWM TO VTOL MOTORSPWM TO SERVOSCANBUSETHERNETUART TO FUEL CELLVMS CPUETH SWITCHMessage HanderUARTSPIETHCANPWM TO FWD MOTORUART TO PAYLOADSMART BATTAIR DATAIMUIMUAP LINK
WINGFUSELAGEETH SWITCHGPS
GPS
Edge Autonomy - Propritary and ConfidentialVTOL ModuleFixed Wing Module

## Page 3

VXE UNIFIEDXCOMMVTOL INTERFACE BOARDUNIFIED APREMOTE MODULE(VTOL AP PCB)Circ ConnPWM TO VTOL MOTORSPWM TO SERVOSCANBUSETHERNETUART TO FUEL CELLVMS CPUETH SWITCHMessage HandlerUARTSPIETHCANPWM TO FWD MOTORUART TO PAYLOADSMART BATTAIR DATAIMUIMUWINGFUSELAGEETH SWITCHGPS
GPS
Edge Autonomy - Propritary and Confidential
VTOL ModuleFixed Wing ModuleMessage HandlerPWM

## Page 4

Embedded Tasks1. Get GNC group a HIL to understand flight characteristics, behavior, and operation. Recommend practice tuning on the HIL and test flying changes to see how real world compares to X-Plane and learn where the simulation is deficient. – HIL Delivery By ~3/10/23?2. Interprocess Communication Phase 1 – Redirect messaging. HIL Support.1. “Record” messaging between XCOMM, Fixed Wing AP , and VTOL AP during launch, landing, etc.2. Redirect the messaging internally. Enable fixed wing code in VTOL controller. 3. Redirect XCOMM to Fixed Wing AP traffic to Unified AP .4. Verify messaging is identical to recorded processes. Fix where it is not.5. HIL support for Unified AP Output3. Interprocess Communication Phase 2 – Remote Board Basic Functionality.1. Implement servo command messages to remote board. 2. Remote board servo pulse generation3. Hardware Design Kickoff4. Interprocess Communication Phase 3 – Redundancy and GCS Support.1. Publish GPS state/health from remote board to Unified AP .2. Publish IMU state/health from remote board to Unified AP3. Unified AP fallback to remote board IMU4. Unified AP fallback to remote board GPS5. GCS Feature support(Maint. Log, Calibration, True/Mag reporting, etc) 6. Port any flight code from XCOMM to Unified AP .5. Flight TestingEdge Autonomy - Proprietary and Confidential

## Page 5

Embedded Tasks Cont.6. GNC API Interface. 1. Implement API for testing new flight code. 1. Ideally should allow runtime switching between production and development code via a GCS switch2. Work together with GCS group to safely implement their initial code/psudocode.7. Windows SIL.1. Implement Unified AP emulator – Windows FreeRTOS?Edge Autonomy - Propritary and Confidential

## Page 6

Appendix: VXE30 System Diagram
Edge Autonomy - Propritary and Confidential
