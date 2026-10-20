# MS-1261: VSM:  Clearable versus Non-Clearable Fuel Cell Faults

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2025-12-23
- **Updated:** 2025-12-29
- **Resolved:** 2025-12-29
- **Reporter:** Craig Burton
- **Assignee:** Craig Burton
- **Creator:** Craig Burton
- **Sprint:** MS Sprint 31

## Description

Subsystem Status Alerts Type field must adhere to the following table for FC faults.
| Fault | Clearable* |
| mFaultMap[5248] = kCoolingSystemSignalFailure; | Y |
|  |  |
| mFaultMap[9232] = kTemperatureInFuselageTooHigh; | Y |
| mFaultMap[9280] = kTemperatureInFuselageTooHigh; | Y |
| mFaultMap[9296] = kTemperatureInFuselageTooHigh; | Y |
| mFaultMap[9344] = kTemperatureInFuselageTooHigh; | Y |
| mFaultMap[9360] = kTemperatureInFuselageTooHigh; | Y |
| mFaultMap[9408] = kTemperatureInFuselageTooHigh; | Y |
| mFaultMap[9424] = kTemperatureInFuselageTooHigh; | Y |
|  |  |
| mFaultMap[15376] = kAnodeFlowExceedsTarget; | N |
| mFaultMap[15392] = kAnodeFlowBelowTarget; | N |
| mFaultMap[17424] = kCathodeFlowExceedsTarget; | N |
| mFaultMap[17440] = kCathodeFlowBelowTarget; | N |
|  |  |
| mFaultMap[19472] = kTemperatureInsideFCExceeds; | N |
| mFaultMap[19488] = kTemperatureInsideFCBelow; | Y |
| mFaultMap[21520] = kTemperatureInsideFCExceeds; | N |
| mFaultMap[21536] = kTemperatureInsideFCBelow; | Y |
| mFaultMap[23568] = kTemperatureInsideFCExceeds; | N |
| mFaultMap[23584] = kTemperatureInsideFCBelow; | Y |
| mFaultMap[25616] = kTemperatureInsideFCExceeds; | N |
| mFaultMap[25632] = kTemperatureInsideFCBelow; | Y |
|  |  |
| mFaultMap[27664] = kIgnitionTimeout; | Y |
| mFaultMap[27680] = kWarmupTimeout; | N |
| mFaultMap[27712] = kExcessiveCooldownTime; | N |
| mFaultMap[39968] = kInsufficientFuelFlow; | Y |
|  |  |
| - Clearable == can be addressed by operator without power-cycling vehicle. |  |

## Comments (1)

### Craig Burton, 2025-12-29

Tested, reviewed and merged.

## Attachments (0)
