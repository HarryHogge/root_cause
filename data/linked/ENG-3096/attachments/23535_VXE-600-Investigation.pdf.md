# VXE-600-Investigation.pdf

Attachment 23535, pdf, 878 KB, added 2024-09-27 by Pat Wells.

## Page 1

1
Investigation Report
VXE 600
W1 Disappearance after Mission Checkout in LW
Author: Ted Trowbridge
25 Sep 2024

## Page 2

2
Summary & Findings
Edge Autonomy Proprietary Information
• Mission from previous day was opened, edited, and saved as today’s mission. Simulation was run and passed. Launch Wizard was 
run. Mission Check passed. A few screens later mission (and DTED) was uploaded to V600. GCS was disconnected from the aircraft.
• To have a backup GCS on standby, a second GCS was connected to V600 and the mission was Saved from Vehicle. Simulation was 
run and failed. Error: Less than 2 Waypoints in Launch Segment.
• Upon inspection, there was no W1 on either GCS. Dotted green line went from L to R2. There was no waypoint 1 on either GCS.
• Q: What would have happened if they had not downloaded the mission to a 2nd GCS, run a sim, and caught this? 
• Q: What would the aircraft do if launched with no W1?
Report:
1. Mission checkout will not pass without two waypoints (L & W1) in the Launch Route but it is possible to launch 
the vehicle without W1 if the mission is modified after checkout.
2. If launched without W1, HIL testing shows the vehicle safely launches but the departure/transition heading is 
unpredictable.  Code inspection backs up this observation.
 Operators should not launch if W1 is missing.  Vehicle behavior has not been fully tested and verified.
Findings:
Workaround: • Do not launch if W1 is observed to be missing from the Launch Route.
• Perform mission simulation prior to transferring any mission to the vehicle.
Corrective Actions: • GCS updates to prevent launch in all cases where W1 is missing.

## Page 3

3
VXE600 passed mission checkout and mission simulation on GCS1 launch wizard.
• Mission checkout and/or mission simulation will not pass if the mission has a Launch Route with less than two 
waypoints.
• The mission must have had two waypoints (L and W1) during mission checkout/simulation.
Mission Checkout Mission Simulation
Edge Autonomy Proprietary Information
Detailed Findings

## Page 4

4
A few screens later mission (and DTED) was uploaded to V600. GCS was disconnected from the aircraft. 
A second GCS was connected to V600 and the mission was Saved from Vehicle. Simulation was run and
failed. Error: Less than 2 Waypoints in Launch Segment.
Edge Autonomy Proprietary Information
Detailed Findings 
• Could not determine exact root cause for loss of W1 on GCS2 and later GCS1.  Possible explanations include:
1. Mission Modification after mission checkout and before mission transfer with LW remaining open:
– The operator could have deleted W1 between mission checkout and transfer.
– The operator could have loaded a different mission file that did not have W1 between mission checkout and transfer.
In both cases the GCS does not require the operator to re-run mission checkout or mission simulation (CA #1).
2. Mission Transfer Error
– Mission uploads to the autopilot have an integrity check that prevent failed transfers.  It  is not possible that W1 was lost 
during upload to the autopilot.
– To support downloading the mission from another GCS, the mission is also uploaded via a side channel which does not 
have integrity checks (CA #2).  It is possible that the mission could be corrupted during this transfer.
» There is some evidence of a link fault during transfer of the side channel mission in the logs.
– GCS2 may have downloaded a corrupt mission file causing W1 to be lost.

## Page 5

5
What would have happened if they had not downloaded the mission to a 2nd GCS, run a sim, and
caught this? What would the aircraft do if launched with no W1?
Edge Autonomy Proprietary Information
Observations 
• The autopilot uses W1 to calculate a launch departure heading for transition from VTOL to Fixed Wing flight.  If W1 is missing the 
launch departure heading will be unpredictable.
• Lack of W1 does not directly affect safety of flight, the vehicle continues to launch safely and proceed to the primary mission.
– Confirmed in HIL testing, screenshots of various departure headings below.
– Code inspection backs up HIL findings on unpredictable departure heading.
• Lack of W1 does indirectly affect safety of flight if there are restrictions on launch heading due to wind, obstacles, terrain, or 
other factors.

## Page 6

6
Corrective Actions 
• The GCS will be updated to prevent launch in edge cases 
where the mission was modified and became invalid after 
the mission checkout step.
#1  Prevent Launch w/ Invalid Mission #2 Add Integrity Checks for Mission Download from Vehicle
Edge Autonomy Proprietary Information
• The GCS will be updated to add integrity checks so the 
mission upload/download from a secondary GCS cannot 
introduce errors.

## Page 7

7
BACKUP
