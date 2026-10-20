# VXEP-32: TPTR-32 Launch from Waterborne Vessel (SRD-691)

- **Issue type:** Major Project
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2023-08-23
- **Updated:** 2026-03-30
- **Resolved:** 2026-03-30
- **Reporter:** Allen Gardner
- **Assignee:** Kat Gulstad
- **Creator:** Allen Gardner
- **Links:** relates to VA-404 (TPTR-32 Launch from Waterborne Vessel (SRD-691)-define requirements, ); relates to VA-405 (TPTR-32 Launch from Waterborne Vessel (SRD-691)-perform ground and flight tests)
- **Customer:** TIQUILA
- **Corrective Action:** Put together tasks and schedule for implementation
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

Failure of SRD-691
The current requirement and Acceptance Criteria require the STALKER Air Platform to be launched from a waterborne vessel or a simulated equivalent deck in a launch area of 10m radius. The changes required to support this requirement, require a software change to enable the magnetometer impacts to be assessed.

## Comments (8)

### Allen Gardner, 2023-08-24

@Cameron Chapman can you provide a list of actions that we would need to do to close this PTR? Please coordinate with @Sam Miller and @David Grosher

### Cameron Chapman, 2023-08-29

@Allen Gardner@Sam Miller@Greg Fryer or @Kat Gulstad , are there more details to this requirement? 
What counts as a simulated equivalent deck? Would on top of a steel plate count? Do we need to simulate issues that may occur on a real ship (antennas, radar, moving deck, etc).
Creating a task to define requirements.

### Kat Gulstad, 2023-09-05

@Cameron Chapman Confirming with Sam, this requirement may be accepted as noncompliant

### Cameron Chapman, 2023-09-06

It still seems required:

[Yesterday 3:25 PM] Kat Gulstad
Sam, confirming from our conversation earlier we anticipate not meeting this requirement and contesting it considering the VXE30 is a COTS product and the modification it would require implies an increase in cost to the customer for labor, time, and resources + we are already into TO2. Is this correct? 
 
| SRD-691 | ISF | Requirement | 3.2.0-5 The [Air Platform] shall be able to be hand launched from a water borne vessel |

 
[Yesterday 6:00 PM] Sam Miller
The customer is not able to withdraw this requirement and we are on the hook to put together a plan and schedule to meet just takeoff from a waterbourne vessel.  There is a PTR for this as well.  PTRs are tracked in Jira here: https://jenaero.atlassian.net/jira/software/c/projects/VXEP/boards/50 
 
And there is a customer dashboard here:  STALKER PTRs Export 15-Aug-23.xlsx
STALKER PTRs Export 15-Aug-23.xlsx
[Yesterday 6:03 PM] Cameron Chapman
Are there requirements for water borne vessel? Guessing something more than costco blow up mattress.
[Yesterday 6:33 PM] Kat Gulstad
There is the one I pulled. We can work together to decompose it into functional specification and tasks
like 1
[Yesterday 6:48 PM] Kat Gulstad
Sam Miller when you have a moment, could you point me to the spreadsheet that outlined the requirements that we are not compliant with that also had the costs listed? I wasn't able to find it on the SharePoint after our meeting

### Cameron Chapman, 2023-09-06

From spreadsheet: “
| Colhoun, Siobhan (UK) - Tue Jul 04 14:52:03 BST 2023 : PTRA/PTRB: Technical solution can be achieved with Edge; [~e317687@uk.lmco.com] to raise concession to move to TO2. Agreed with Frankie.  Sev changed to 3. |

### Kat Gulstad, 2023-09-11

Current risk assessment on this requirement:

| RSK-001​ | 691​ | Launch from water borne vessel​ | Vehicle prep and calibration in sea state 3​ | VXE30 may not be able to prep and launch from a smaller boat in sea state 3.  Schedule impacts for coding and testing. Medium-low risk for loss of vehicle(s) during testing.​ | Prep/launch from a larger stationary boat.  Update code to average vehicle motion during calibration, check IMU status​ |
| RSK-002​ | 691​ | Launch from water borne vessel​ | Magnetometer impacts from boat deck​ | VXE30 may not be able to prep and launch due to magnetometer misalignment.  Schedule impacts for coding and testing. Low risk for loss of vehicle(s) during testing.​ | Update code to ignore magnetometer during launch prep and initial takeoff through transition.  ​ |
| RSK-003​ | 691​ | Launch from water borne vessel​ | Launching in 20kt winds exceeds the current threshold for a safe launch​ | Launching above 17kt winds may result in loss of control​ | Reduce acceptable launch criteria to align with current capability.  ​ |
| RSK-004​ | 691​ | Launch from water borne vessel​ | Launching a VXE30 from small size of boat "To include a Medium Inflatable Boat, a Rigid Hard Inflatable Boat."  ​ | VXE30's size may not allow for safe launch from a small boat​ | "You're gonna need a bigger boat"​ |
| RSK-005​ | 691​ | Launch from water borne vessel​ | Aborted launch from a small water bourne vessel​ | VXE30's size may not allow for safe abort onto a small boat​ | Get a bigger boat, or ditch in the water​. Remove 10ft offset from code (or have option to select removing 10ft backup on abort) |
| RSK-006​ | N/A​ | Landing on water borne vessel​ | Edge did not propose landing on a water borne vessel.  The original JAI proposal assumed recovering on land.​ | Significant development will be required to support recovery onto a boat.  ​ | May be able to specify minimum ship size and land via attitude mode.  ​ |

Proposed mitigations out of Edge’s scope, in negotiation with customer:
- vehicle is only intended to launch from stationary boats → less impact to calibration
- Vehicle is not launched in winds > 17 kts
- Vehicle is only launched from large boats
- Vehicle is either landed on land or ditched in water 
- If we need to land on a ship, we can specify minimum boat dimensions, but boat must be stationary for landing

Edge feature implementations:
- Integrate a “sea” feature
- Turn magnetometer off while launching from a boat. The reason being that most decks are made of steel, which skews magnetometer data
- Remove “back up 10 ft” command in “Aborted Launch”
- When launching from a stationary boat, software, vehicle motion data from the IMU is averaged for calibration
- If we do need to land on a boat, specify minimum ship size needed to safety land and recover vehicle

Current time estimate = 3 months to implement software features
I will create subtasks to specify edge features + time to complete with consideration of other work going on

### Greg Fryer, 2023-09-11

@Kat Gulstad I changed this over to a Project instead of a Problem, since it is new scope/functionality not a failure. It will have a different workflow (whcih I think we discussed? 🙂) based on design and design review vs. root cause.

### Kat Gulstad, 2023-09-11

@Greg Fryer sounds good to me, I will also continue capturing the specification from this in the requirements

## Attachments (0)
