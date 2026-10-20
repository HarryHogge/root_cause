# TPTR-58_EAES 8D Failure Analysis_10.9.2023.pptx

Attachment 17406, pptx, 7568 KB, added 2023-11-07 by Sean Wendling.

## Slide 1

TPTR-58 – 8D Failure Analysis
Edge Autonomy Energy Systems

Last Updated: October 2023
[picture]
[picture]

## Slide 2

Executive Summary (Last Updated:10-09-23 )
| Problem Information |  | Containment Actions/Status | Root Cause Actions/Status | Corrective Actions/Status | Verification Actions/Status |
| Who | Observers at the Stalker FAT Testing (Cody Smisek, Glen Francis, Others?) | Customer LMUK – TIQUILA Customer | RC1 - COTs blower paired with PCA129 control board suffered Lock Rotor Failure on startup. | CA1 - PCA129 software protections added to protect system from lock rotor, and high current draw failure. | CA1 - Validation & Test Plan written to validate software yielded exceptional result. (1) Component failure amongst 75+ tests and 24 control boards. |
| What | D450 Fuel Cell (D4500510) failed during startup.  Fault code 17440 was observed.  Rebooting did not resolve the issue. | Internal Problem units isolated; additional identification added to units with CA applied. | RC2 - COTs blower paired with PCA129 control board arrived with damage inflicted by high current draw during QC testing in AA that did not propagate until after delivery. | CA2 - In conjunction with software correction, PCB outfitted with additional electrical components that are required to apply software corrections. | CA2 - Application of rework is validated by unique markings to board, and operational testing during System QC Testing |
| When | During Stalker FAT Testing (reported on 8/15/23).  Date of testing not communicated with RM. | Supplier Updated BOM and print provided to board supplier. | RC3 - Initial Validation and test plan failed to identify these failure modes, allowing them to enter production unnoticed. | CA3 - Test plan designed to apply comprehensive range of functional tests on Fuel Cell. | CA3 - Execution of Test plan yielded highly successful results. Leading to extremely low # of “Critical Failures”, all of which outside normal operational functionality. |
| Where | Stalker FAT Testing.  Location not communicated with RM. | Notes Systems with this failure never shipped to customer. Only observed during FAT. | Notes 3rd party software failed to protect against items protected by COTS control board. | Notes Corrective Actions have been applied and validated. | Notes Complete test plan validates both RC items and operational capacity outside of normal operation. |
| Actions for the coming week | Actions for the next few weeks |
| Complete 8D reporting. Apply re-work action to remaining boards in house. | Continue working with 3rd party software vendor to update print and BOM for future shipment.  Continued System testing that will further validate PCA129 software. |

## Slide 3

D1 – Team Overview
| ROLE | TITLE | NAME |
| INVESTIGATION LEAD: | Director of Operations | Rick Martin |
| TEAM MEMBERS: | VP of Technology | Tom Westrich |
|  | Engineering Technician | Robert Redfield |
|  | Sean Wendling | Product Engineer |
|  | Kyle Kooyers | Supply Chain Manager |

## Slide 4

D2 – 5W2H
| Who? (Who found the issue and Who was involved?) | Observers at the Stalker FAT Testing (Cody Smisek, Glen Francis, Others?) |
| What? (What happened and what makes it important?) | D450 Fuel Cell (D4500510) failed during startup.  Fault code 17440 was observed.  Rebooting did not resolve the issue. |
| When? (When did the event occur and when was is discovered?) | During Stalker FAT Testing (reported on 8/15/23).  Date of testing not communicated with RM. |
| Where? (Where did the event occur?) | Stalker FAT Testing.  Location not communicated with RM. |
| Why? (Any ideas on Why this happened? Potential causes?) | Fault Code 17440 reports a non-responsive Cathode Air Blower. Potential Causes: Blower stuck/locked/motor windings or wiring damaged are all primary causes. |
| How Many? (How many items were involved in the event?) | 1 |
| How was it Found? (Circumstances around the event? Testing? Takeoff? Landing?) | The fault was found during the Stalker FAT testing during the initial fuel cell startup while the aircraft was grounded. |

## Slide 5

D2 – NCR Summary
Non-Conformance Occurred during Fuel Cell Validation during FAT testing for LMUK – TIQUILA customer. Issue report was described as follows:
During STALKER FAT Testing, one of the D450+ Fuel Cells (SN:510) failed during start up. Fault code 17440 was observed and rebooting the fuel cell did not resolve the issue. This was observed during set up of system through operator's manual and prevented steps for SRD-6 in fuel cell configuration to be passed.
Fuel Cell SN 510 was sent to Ann Arbor for inspection:
After receipt of Fuel Cell, system was setup and cycle attempted by Product Engineer to confirm failure behavior. Comments are as follows: 
“Hello All, I received SN510 and was able to recreate the error here. Cathode Fan failed to operate during warm-up and during diagnostics. Once it was replaced with a new blower, the system functioned as intended. The cause is determined to be either lock-rotor failure or an unprotected high-power draw that damaged the blower motor. We have observed this failure in the past and are currently working with our developer’s software team and are expecting a software update to apply to all systems. I will continue to update this ticket as we apply updates and follow through with our validation plan implementing the correction. (updated by Sean Wendling)”. 
This error was further observed in the form of failures on production units during QC testing. In order to resolve the immediate term issues, a calibration update was created to limit the capability of the COTS blower/board pair to protect against current overdraw, which was shown to adequately eliminate the issue, but greatly reduces cooldown time and blower capabilities in operation. 
After this fix was applied as an immediate containment.

## Slide 6

D3 – Containment Actions
| Action # | Action Description | Action Owner | Est. Complete | Actual Complete | Notes |
| 1 | Identify all Part Numbers impacted | SW, RM, TW, RR | 8/15/2023 | 8/15/2023 | Complete |
| 2 | Check WIP | SW, RR | 8/29/2023 | 8/29/2023 | Complete |
| 3 | Check Inventory | SW, KK, RR | 8/29/2023 | 8/29/2023 | Complete |
| 4 | Determine if there is any Customer Impact | SW, RM, TW | 8/29/2023 | 8/29/2023 | ESOSOC (18) units delivered with “Calibration” fix, but not updated software. |

## Slide 7

D3 – Containment Actions - Details
| Action # | Action Description (Systems delivered with Calibration only) | Action Owner |
| 1 | Quarantine of all WIP boards on production line. | Robert R, Sean W |
| 2 | All assembled systems underwent calibration re-write during QC Testing (at varying stage) prior to shipment. | Robert Redfield |
| Action # | Action Description (Systems delivered with PCA122/129 Software Update) | Action Owner |
| 1 | Quarantine of all WIP boards on production line. | Robert R, Sean W |
| 2 | Inventory Cage boards isolated from production line and material re-routed to rework. | Sean W, Robert R, Kyle K |
| 3 | All Systems with Control Board Rework receive red paint dot to indicate rework. | Robert R |
| 4 | All Systems with Control Software update receive additional red paint dot indicating software load. | Robert R, Sean W |

## Slide 8

D4 – Root Cause Investigation Actions
| Action # | Action Description | Action Owner | Est. Complete | Actual Complete | Notes |
| 1 | Investigate Design & Requirements | TW, TreeTown | 9/04/2023 | 9/04/2023 | Investigation completed and Current draw & Lock rotor determined to be primary RCs |
| 2 | Evaluate COTS Blower Control Board | TW, TreeTown | 9/04/2023 | 9/04/2023 | In review of COTS control board, evidence of protections can be seen, though they had not been replicated in TTT software. |
| 3 | Investigate Blower/Board Assembly Process | SW, RR | 8/29/2023 | 8/29/2023 | Yielded potential issues, however, none related to observed failure behavior. |
| 4 | Investigate Data from other failures | SW, TW, RR | 9/04/2023 | 9/04/2023 | Investigation yields high current behavior in many failure occurrences. |
| 5 | Complete 3 Legged 5 Why | SW | 10/13/2023 | 10/09/2023 | Completed Retroactively |

## Slide 9

D4 – Root Cause Tools – 3 Legged 5 Why
PROBLEM
ESCAPE
SYSTEMIC
WHY?
WHY?
WHY?
WHY?
ROOT CAUSE 1
WHY?
WHY?
WHY?
WHY?
ROOT CAUSE 2
WHY?
WHY?
WHY?
WHY?
ROOT CAUSE 3
Problem/Occurrence –
[Focal: Prod Engr & Prod]
“How did the problem happen?”
Escape/Detection –
[Focal: Qual Engr & Insp]
“How come we did not catch it?”
Systemic –
[Focal: Investigation Team]
“Why did we not fix the Problem or Escape before this happened?”

Speaker notes:
were previously limited. Test plan for initial release of software did not account for the possibility of these failure modes.

## Slide 10

D4 – Root Cause Summary
| Root Cause Cat. # | Cause Type | Cause Description | Notes |
| RC1 | PCA122/129 Software | Blower software lacked necessary features to protect COTS blower from Lock Rotor and High Current Draw Failures. | In failures, Blower can be observed exceeding 2.0A current draw. This amount of current has been determined to increase risk of Blower Damage. |
| RC2 | Failure Behavior | Failure is intermittent, and can occur without warning leading to failure that escapes QC testing. | Because damage can occur without complete failure during cooldown, system can appear to pass QC, then fail to operate on following cycle. |
| RC3 | Insufficient Testing | Initial software validation failed to identify failure modes. | Rapid validation of Control Board and Software failed to identify these failures, resulting in systems beginning production without identifying issues with software. |

## Slide 11

D5 – Corrective Actions
| Root Cause # | Corrective Action # | Action Description | Action Owner | Est. Complete | Actual Complete | Notes |
| RC1 | CA1 | Update cathode control calibrations to limit the power requested from the cathode blower during use. | Tom Westrich | 9/01/23 | 9/01/23 | This option is a partial solution that would greatly reduce risk by reducing blower RPM range. |
| RC1 & RC2 | CA2 | Update cathode blower controller software to limit instantaneous blower power to less than 2.0A, and cycle phases during startup to eliminate failure with | Sean Wendling, TreeTown | 9/08/23 | 9/12/2023 | Complete solution would eliminate Lock Rotor failure as well as High Current Draw without compromising blower operational range. |
| RC3 | CA3 | Additional Validation through Comprehensive test plan for Blower/Board. | Sean Wendling | 9/18/2023 | 9/18/2023 | Additional Validation to identify any other failure modes and validate software correction properly addresses issue. |

## Slide 12

D6 – Verification Actions - Overview
| ID | Test Description | Acceptance Criteria | QTY | Pass/Fail | Comments |
| 1 | Lock rotor Resilience Test: Motor is energized, asked to immediately produce maximum RPM followed by immediate request for 0 RPM, and de-energized in repeating cycle for 10 cycles. | - Cathode Motor and board function properly. (Current Draw > 2.0A = partial failure) - Reasonable amount of heat is measured from the board not exceeding normal operational temp (observation of temp only) | 24 | Fail = any critical failures Pass < 10% partial failure | 1° Priority test All Articles tested in random order, paired with random WS7040 blowers. |
| 2 | Cyclical Test: Full Ramp-up to 250 LPM, operate at 250 LPM for 3 minutes and descend to 0 LPM. Repeated for 10 cycles. | - Cathode Motor and board function properly. (Current Draw > 2.0A = partial failure) - Reasonable amount of heat is measured from the board not exceeding normal operational temp (observation of temp only) | 24 | Fail = any critical failures Pass < 10% partial failure | 2° Priority test All Articles tested in random order, paired with random WS7040 blowers. |
| 3 | Endurance Test: Cathode function at peak RPM for 16-hour endurance cycle. | - Cathode Motor and board function properly. (Current Draw > 2.0A = partial failure) - Reasonable amount of heat is measured from the board not exceeding normal operational temp (observation of temp only) | 3 | Fail = any critical failures Pass < 1 partial failure | 3° Priority test 6 Articles randomly selected, paired with WS7040 blower for entire endurance cycle. |

## Slide 13

D6 – Evidence (Test ID#1)
Purpose:
Lock Rotor Protection was determined to be a leading cause of WS7040 blower failure during quality testing and was the result of the system’s inability to safely interpret and safely actuate rotors out of phase. This was observed on occasion during Quality Checkout at Ann Arbor Facility and in TIQUILA FAT program in SLO.

Procedure: 
Board connected to an energized PCA130 Main control board and WS7040 Wonsmart Blower. Using cyclical command software, blower is commanded to run at 36,000 RPM for 10 seconds, run 0 RPM for 10 seconds, and repeat this for a total of 5 & 10 cycles. Actuator and Output current are measured and recorded. 

Results:
Of (24) PCA129 boards tested, 100% of articles passed both 5 cycle and 10 cycle Lock Rotor Resilience testing and were able to safely drive the blower immediately to 32,000 – 36,000 RPM range without failure for all 10 start attempts across all 24 blowers. 32,000 RPM exceeds boundary operational conditions of the D450+ Fuel Cell. In all cases, software protected ramp-up RPM and current draw eliminating all occurrence of blower failure.
[chart: Cathode Current Draw]
[chart: Cathode Actuator Response]
| PCA129 Board Serial # | Lock Rotor 5 Cycle | Lock Rotor 10 Cycle |
| B120472-0034 | Pass | Pass |
| B120472-0036 | Pass | Pass |
| B120472-0038 | Pass | Pass |
| B120472-0040 | Pass | Pass |
| B120472-0046 | Pass | Pass |
| B120472-0048 | Pass | Pass |
| B120472-0049 | Pass | Pass |
| B120472-0055 | Pass | Pass |
| B120472-0056 | Pass | Pass |
| B120472-0058 | Pass | Pass |
| B120472-0061 | Pass | Pass |
| B120472-0063 | Pass | Pass |
| B120472-0065 | Pass | Pass |
| B120472-0071 | Pass | Pass |
| B120472-0072 | Pass | Pass |
| B120472-0075 | Pass | Pass |
| B120472-0077 | Pass | Pass |
| B120472-0078 | Pass | Pass |
| B120472-0083 | Pass | Pass |
| B120472-0086 | Pass | Pass |
| B120472-0089 | Pass | Pass |
| B120472-0091 | Pass | Pass |
| B120472-0094 | Pass | Pass |
| B120472-0095 | Pass | Pass |

## Slide 14

D6 – Evidence (Test ID#2)
Purpose:
Cyclical Test is created to identify failure of blower during transitions of Fuel Cell from “Warm-up” to “Operate”, and “Operate” to “Cooldown” and eventually FC “Off” State. Failure mode results in possible system failure and critical function risk of Fuel Cell. Observed (3) instances of failed Cathode Blower during cooldown in Quality Checkout at Ann Arbor Facility. 

Procedure: 
Board connected to an energized PCA130 Main control board and FLD0988 Wonsmart Blower. Using cyclical command software, blower is commanded to climb at standard functional ramp-rate to 250LPM (~110seconds), idle at 250LPM (60-80 seconds), and return to 0 LPM (~110 seconds) and repeat this for a total of 5 or 10 cycles. Actuator and Output current are measured and recorded. Total test time for 5 cycle - 25 min, 10 cycle - 50min

Results:
Of (24) PCA129 boards tested, 100% passed a 5-cycle rapid validation. Due to duration of testing cycle, all but (2) PCA129 articles completed 10-cycle test (as of 9/19/2023).  Of these, 100% pass-rate was also recorded among these articles. Climb rate, Actuator Response, and Output Current all met “Pass” conditions for the test.
| PCA129 Board Serial # | 5 Cycle | 10 Cycle |
| B120472-0034 | Pass | Pass |
| B120472-0036 | Pass | Pass |
| B120472-0038 | Pass | Pass |
| B120472-0040 | Pass | Pass |
| B120472-0046 | Pass | Pass |
| B120472-0048 | Pass | Pass |
| B120472-0049 | Pass | Pass |
| B120472-0055 | Pass | Pass |
| B120472-0056 | Pass | Pass |
| B120472-0058 | Pass | Pass |
| B120472-0061 | Pass | Pass |
| B120472-0063 | Pass | Pass |
| B120472-0065 | Pass | Pass |
| B120472-0071 | Pass | Pass |
| B120472-0072 | Pass | Pass |
| B120472-0075 | Pass | Pass |
| B120472-0077 | Pass | Pass |
| B120472-0078 | Pass | Pass |
| B120472-0083 | Pass | Pass |
| B120472-0086 | Pass | Pass |
| B120472-0089 | Pass | Pass |
| B120472-0091 | Pass | Pass |
| B120472-0094 | Pass | Pass |
| B120472-0095 | Pass | Pass |
[chart: Cathode Actuator Response]
[chart: Cathode Current Draw]

## Slide 15

D6 – Evidence (Test ID#3)
Purpose:
Endurance test is designed to validate blower function at maximum flow rate for sustained period of time without degradation of WS7040 Blower or PCA129 article. At Quality Control in Ann Arbor, blower failure after short term use was observed rarely, however endurance testing serves to additionally validate the sustainment of Cathode airflow beyond the Cyclic and Lock Rotor testing at a range well exceeding operational output. 

Procedure: 
Board connected to an energized PCA130 Main control board and FLD0988 Wonsmart Blower. Using FC Diagnostic (Force) software, commanding 36,000RPM from Cathode, allow blower to function overnight, upon return in the morning reconnect to system, and validate RPM and Current Draw still within accepted limits.

Results:
Of (5) PCA129 boards tested, 5 of 5 successfully completed Test #1, and of (5) boards tested, 4 of 5 successfully completed Test #2. 
NOTE: Failure of B120472_0038 did not occur during endurance operation, Article passed END Test #1 and previously listed testing. Observed failure consisted of lack of function during set-up/start of Test #2. Board has been returned to Software development 3rd party vendor for failure analysis, which determined the failed component to be “R23” Resistor. Temperature may have been a contributing cause, leading to additional testing shown on following page.
| PCA129 Board Serial # | Test #1 |  |  |  | Test #2 |  |  |  |
|  | Start | End | Total | Pass | Start | End | Total | Pass |
| B120472-0036 | 4:37pm | 8:46am | 16:09 | Pass | 5:36pm | 11:08am | 17:32 | Pass |
| B120472-0038 | 4:45pm | 9:35am | 16:50 | Pass | N/A | N/A | N/A | Fail |
| B120472-0072 | 4:47pm | 9:37am | 16:50 | Pass | 12:50pm | 8:47am | 19:57 | Pass |
| B120472-0077 | 4:40pm | 8:47pm | 16:07 | Pass | 5:36pm | 11:07am | 17:31 | Pass |
| B120472-0089 | 4:51pm | 9:37am | 16:46 | Pass | 12:51pm | 8:47am | 19:56 | Pass |

## Slide 16

D6 – Continued Investigation of single failure (Temperature Extrema)
Purpose:
Temperature Testing designed to investigate the maximum operational temperature of PCA129 Control Board. Conducted in response to failure analysis by Tree Town Tech of failed unit B120472_0038. Potential root cause determined by TTT indicated a potential for failure on “current sense” R23 Resistor unit. For further analysis, PCA129 with special consideration of R23 resistor is subjected to thermal testing.

Procedure: 
PCA129 connected to an energized PCA130 Main control board and FLD0998 Wonsmart Blower. PCA129 and FLD0998 are operating in thermal chamber to simulate high ambient temperatures. Using FC Diagnostic (Force) software, commanding 36,000RPM from Cathode, temperature is increased by 10C beginning at 50C (Maximum ambient operating temp for VXE-30) every 5 minutes. After each step, chamber is briefly opened, and temperature is manually measured by thermal camera. PCA129/FLD0998 is run in this configuration until failure.

Results:
PCA129/FLD0998 combination failed at approximately 130C Ambient (146C Board temperature). This failure occurred at the blower and not the PCA129 unit, beginning with a gradual decline of Cathode RPM from 34,000RPM to 18,000RPM before an eventual drop to 0RPM. After Temperature was reduced in chamber and board temperature read 90C, FLD0998 reverted to 36,000RPM for approximately 5-10 seconds before mechanically failing. 
Notable Observations: 
Noted that across entire temperature range, board temperature was approximately 12C over ambient. This can be further investigated as a possible indicator of Mid-Fuselage Ambient Temperature (potential accuracy increase from extrapolating data from Main Control MCU Temp).
PCA129 was paired with a new FLD0998 blower after test, blower functioned as normal and current protection functioned as intended.
R23 not determined to be cause, while Blower Failure occurred at output current >2.0A current limit, this could be a result of FLD0998 damage during testing at temperature.
[chart: Temperature Testing - PCA122/129]
[chart: Blower Current Draw v. Blower RPM (110-130C)]

## Slide 17

D6 – Additional Testing Considerations
Testing conducted 9/11-9/21 serves to validate the protections integrated into PCA122/129 software that were directly derived from failure modes observed during first deliveries and testing conducted at quality control step of SCO in Ann Arbor. Additional validation and failure mode exploration could be conducted to further mitigate associated risks with PCA122/129 Blower design and integration. These are summarized below. (Some items listed are included in D450+ Validation testing goals).

Continued Validation Considerations: 

WS7040 Blower Lifespan Testing
Constant Operation - Testing to investigate Blower/Board lifespan against the manufacturer specification.
6 HR Cyclical -  Testing Blower/Board integrated into the D450+ Fuel Cell operating in 6HR cycles.
Blower Temp Extrema - Temperature Related Degradation to Blower Lifespan.

Environmental Condition Testing
Ingress Protection – Validation of Ingress considerations (Dust, Water, etc).
D450 Integrated Cold Testing – Validation of Cold operation (at and above VXE max operational range).
D450 Integrated Hot Testing – Validation of Hot operation (at and above VXE max operational range).

Vibration and Altitude Testing 
Vibration Testing – Blower/Board integration into D450+ Fuel Cell and operation.
Altitude Testing – Blower/Board integration into D450+ Fuel Cell warm-up/air intake at high altitude.

VXE-30 Flight Operation Testing (Bend – Flight Ops Support)
D450/VXE Integrated Flight – Complete VXE system validation of D450+ fuel Cell with latest Blower/Board control.
D450/VXE Integrated Environmental Simulation – Heat/Cold/Rain complete system integration testing.

## Slide 18

[picture]
Section Goal:
Determine if there are any additional actions that could be taken on similar parts, products, processes, or anything else that could benefit from the information gained during this investigation

Section Content:
Outline of potential Preventative Actions
Status on any Actions taken 



Typical Deliverables:
Summary of Preventative Actions
D7 – PREVENTATIVE ACTIONS

## Slide 19

D7 – Preventative Actions
| Preventative Action # | Preventative Action Description | Action Owner | Est. Complete | Actual Complete | Notes |
| 1 | Update PCA122/129 Docs | Tom Westrich, TTT | 10/13/2023 |  | All Component BOM, Software, and Supplier Documentation to be updated prior to repeat orders. |
| 2 | Deliver Corrected Docs to Vendor | Tom Westrich, Kyle Kooyers | 10/13/2023 |  | Documents to be shared with Odessey & Custom Assembly to eliminate possibility of MFG error. |
| 3 | Continue to mark all systems with RW & SFT ID marks once correction or software is applied. | Sean Wendling, Robert Redfield | 11/04/2023 |  | Completion date indicated as anticipated close out of containment activity and elimination of all un-reworked materials in production facility. |

## Slide 20

D7 – BLANK SLIDE
TEXT

## Slide 21

[picture]
Section Goal:
Close the project and Celebrate the win

Section Content:
Acknowledgement of Project Completion



Typical Deliverables:
N/A
D8 – PROJECT CLOSURE

## Slide 22

[picture]
[picture]
