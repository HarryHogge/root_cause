# VXEP-512: VXE 556 vehicle transitioned to VTOL at 1200ft, operator unable to abort. HLB depleted and crashed

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-07-19
- **Updated:** 2026-03-02
- **Resolved:** 2025-02-25
- **Reporter:** Pat Wells
- **Assignee:** Ted Trowbridge
- **Creator:** Pat Wells
- **Labels:** 3rdSFG, GCS, USASOC, Weekly-incident-tracker
- **Links:** Linked issue cannot finish until this issue finishes. GCSS-362 (Implement lockouts or significant warnings to prevent operators starting VTOL landing at too high of an altitude. ); relates to FS2-2318 (Firmware Update: Check for enough energy before allowing transition to VTOL based on current altitude); relates to FS2-2342 (VXEP-512 - Investigation and GCS CAs for Transition to VTOL above 2000ft); relates to FS2-2825 (Firmware CAs (VXEP-556) for Transition to VTOL above 2000ft)
- **Customer:** USASOC
- **Vehicle Tail Number:** 556
- **Issue Status:** Closed: Operator error
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical

## Description

Verbal report from operator:  Vehicle transitioned to VTOL landing at 2500ft AGL.  Operator unable to abort.  HLB depleted and vehicle crashed.  

Still waiting on formal written narrative from operator.  Will add when it’s received. 

XCOMM and VTOL downloads attached.  Operator retrieved data using the post incident data recovery procedure.  No AAR file available. 

Written statement from customer, note they reference VTOL transition at 1200 feet, verbally they stated 2500 feet. Received 7/22


BLUF: During a test flight at Ft. Liberty, NC, a Stalker VXE-30 (Group 2 sUAS) appeared to suffer a failure in the battery system that led to vertical takeoff/landing (VTOL) propulsion failure during the landing phase of flight.  The propulsion failure resulted in the aircraft losing lift and crashing from approximately 1200 ft in altitude and 200m away from the intended landing point.
 
Who: SM (15W) and SM (15W) [both Service Members assigned to Special Operations Robotics Detachment (SORD)/TISC/4/3rd SFG(A)]
What: Stalker VXE-30 Crash
Where: OP 13 Ft. Liberty, NC
When: Approx. 1331 EDT, 15JULY2024
Why:  1st report: Aircraft lost propulsion due to a suspected battery failure.  The Crew was unable to recover control of the aircraft as it spiraled down from altitude where it eventually impacted standing foliage at the training area.
 
Amplifying Information:
- When the Operator commanded the Stalker to RTB, the crew said it went to its preplanned mission points and started to descend at around 2500 ft AGL. The Stalker VXE-30 should transition into its vertical take-off/ landing (VTOL) at around 100-300 ft AGL. Once the Operators saw the Stalker transition into VTOL at a higher altitude (1200 ft AGL), they immediately tried to abort the landing but were unable to due to the software ghosting out the option. Before crashing, the crew tried everything they could to put the Stalker into fixed wing flight but were unsuccessful.
- The SORD has 3 Stalker VXE-30s (it had 4x before the loss of this A/C) – these are the only Group II UAS currently in the SORD.
- Both Service Members s are current and qualified on the Stalker.
- SM  – MAY 24 NET on the Stalker VXE-30
- SM Scott – APR 24 NET on the Stalker VXE-30
- Currencies are maintained by flying the system every 60 days.
- Both SMs have flown the system since their respective NET dates.
- Both SMs are under 25 hours on the system (as most operators are due to the recent fielding of the equipment), so this was considered a MEDIUM risk training event.
- The Crew recovered 85% of the aircraft.  15% of the aircraft (a wing and a boom) are stuck in a tree.  The SORD is attempting to recover those pieces.  The high-dollar items are secured.
- The SORD took pictures (100+) and will get witness statements (2x C/1/3 SFOD-A Service Members + 2x Crew Service Members).

## Corrective Action

- https://jenaero.atlassian.net/browse/FS2-2102
- https://jenaero.atlassian.net/browse/FS2-2318

## Root Cause

Closed: Operator error
@David Grosher this doesn’t seem like a total root cause. Yes, the operator should not have executed a VTOL landing at 2500ft, but robust software should also warn/not allow a VTOL landing to start that high.  Seems like that is acknowledged in the CA. More info on what the operator error was would also be useful in that field.

## Comments (27)

### Pat Wells, 2024-07-19

@David Grosher @Cameron Chapman FYSA, received data files today.  Attached.

### David Grosher, 2024-07-19

@Pat Wells Initial look at the XCOMM log shows that a goto was commanded to IP4 about 30 seconds prior to VTOL transition starting. Can you request the GCS logs? I want to be careful about implying operator error because we could probably have checks on AGL prior to a VTOL transition.  
[17:24:47.152 3909.152] GoTo m,w 1  3  (Note: 1=Primary Landing, 3 = IP4)
[17:25:15.002 3937.002] ap dbg: start landing: : 7

### Pat Wells, 2024-07-22

Added statement from operators and requested GCS logs.  @David Grosher

### Alexander Alan Arnold, 2024-07-22

@David Grosher Attached GCS AAR File from Customer

### David Grosher, 2024-07-22

@Jason Scherer When you are back, please take a look at this.  It appears that the operator issue a GOTO to IP4 when the vehicle was at close to 3000ft AGL and it then fell from 1200 ft AGL when the battery ran out of energy. We need to confirm that the goto went to IP4 versus the RTB command that was claimed in the witness statement.

### David Grosher, 2024-07-29

@Wesley Reynolds See my comments for Jason below.

### Wesley Reynolds, 2024-07-29

Notes for this investigation:
During this flight, the vehicle was commanded to GoTo IP4. The vehicle was not commanded to RTB.
The following line in the XCEVLOG.txt file (submitted from the customer) indicates that a GoTo was issued to IP4:
```
[17:24:47.152 3909.152] GoTo m,w 1  3
```
The logic to defend the previous statement can be found in our source code under XComm/UplinkParser.cpp:
```
bool DispatchSystemCommand(const SYSTEM_COMMAND* sc)
{
    ...
    case COMMAND_MISSION:
        AddMessageInt2("GoTo m,w", cmd.Parm1, cmd.Parm2);
    ...
} 
```
The stack trace to see how cmd gets populated is very large, but the critical information for how this data got populated lies in sams/Mission.cpp:
```
enum MissionNames { LAUNCH = 0, PRI_LAND, ALT_LAND, LOSIG, PRIMARY, OVERRIDE, NMISSIONS, LOSIGALT = NMISSIONS };
...
CWaypointArray* CMission::WaypointArray(MissionNames mission)
{
    switch(mission)
    {
        ...
        case PRI_LAND:
        return &m_land1;
        ...
    }
    ...
}
```
Each waypoint in a mission can be uniquely identified using 2 parameters: Parameter 1 and Parameter 2. In each case, Parameter 1 indicates which pattern the waypoint is in, and Parameter 2 indicates which waypoint within the pattern is being identified. A mission waypoint in the Primary Landing Pattern is indicated by Parameter 1 = 1 (see the enumeration MissionNames). Within the Primary Landing Pattern, there are always 6 waypoints (IP1, IP2, IP3, IP4, IP5, PLZ ).
The names IP2 and IP3 are not rendered within the GCS Software, but they exist in the mission file. 

Using 0-based indexing for Parameter 2, it follows that IP1 is identified by a waypoint with Parameter 1 = 1 and Parameter 2 = 0. Moreover, it follows that IP4 is identified by a waypoint with Parameter 1 = 1 and Parameter 2 = 3.
Thus, the existence of the line in XCEVLOG.txt:
```
[17:24:47.152 3909.152] GoTo m,w 1  3
```
serves as evidence that the vehicle was issued a GoTo command that commanded the vehicle to GoTo IP4.

### Pat Wells, 2024-07-29

@Wesley Reynolds Thanks for the detailed explanation of what occurred. 
How soon can we get this formatted into a final report that can be delivered to the customer?   Currently their fleet is grounded pending the final outcome of this investigation.  @David Grosher FYSA

### Wesley Reynolds, 2024-07-29

I just ran across a much more succinct argument.
In the GCS Event Log file (saved as x_event.txt in an AAR) that records the events that the GCS Software keeps track of, when an RTB command is issued, the following data is logged:
```
Time: 003:02.547  RTB Now Command - primary LZ active
```
However, in the GCS Event Log file that was submitted by the customer (T95_V556_240715_131205_event.txt), no such line exists. This is evidence that there was never an RTB command was ever issued.

Instead, this file contains the following log entry:
```
Time: 063:31.891  Change active waypoint: : Mission: Primary LZ  Waypoint: 4
```
This is evidence that a GoTo command was issued to command the vehicle to GoTo IP4.

### Wesley Reynolds, 2024-07-29

@Pat Wells I am not sure what my estimate would be to get this into a formal report for the customer. I have never written or seen such a report yet so I don’t know what kind of format or language would be expected. I would prefer to read over a previous report before creating this report.
That being said, especially if use my second argument rather than my first, I would imagine I could generate the report by the end of the day on Wednesday. I will be in an airport for a large chunk of tomorrow and would not expect to complete this tomorrow.

### Pat Wells, 2024-07-30

@David Grosher tagging you FYSA since you missed Wesley’s findings and comments. 
3rd Group still has their fleet grounded pending a final report.  @Jeremy White informally notified them of the findings but they are unable to return to flight without our report.

### David Grosher, 2024-07-30

@Wesley Reynolds I would like to see both arguments in the report. I will tag you in a different issue with a report you can view.

### Wesley Reynolds, 2024-07-31

I have attached an Incident Investigation Report that outlines:
- What issues occurred
- What we will do to prevent this in the future
- What the customer can do right now to prevent this in the future

Let me know if anything needs to be adjusted before we can present this to the customer @David Grosher @Pat Wells
[embedded: AC556_Investigation.pptx]

### Pat Wells, 2024-07-31

@Wesley Reynolds thank you.  Very thorough report.  
@David Grosher pending your final check before I pass to customer.

### David Grosher, 2024-07-31

@Pat Wells @Wesley Reynolds Approved. Good job Wesley!

### Pat Wells, 2024-07-31

Report provided to PM 7/31

### Jeremy White, 2024-07-31

Thanks for getting this done! I know you are all slammed. It was sent to CW4 Kenneth Myers at 1735 (Eastern) on 31 July 2024.

### Jeremy White, 2024-08-02

@David Grosher @Pat Wells I talked to Kenny this afternoon (investigating officer from 3rd SFG). Does the log have a chronology of events after the “GoTo IP4” command was given? He’s looking for altitudes, locations, and if any other user inputs were given. He’s on vacation until 12 August.

Is “VTOL Landing Paused” (067:43.219 and 067:43.297) a user command or internal to the system? What does “Override Cancelled” (068:05.141 and 068:23.375) mean? (my questions, not the customer).

### David Grosher, 2024-08-02

@Jeremy White The datalog will have altitudes and positions in the local tangential plane, where the origin is the launch point. And the timestamps will show where that is in relation to these events. From what I remember it was just below ~3000 ft AGL when the go to IP4 was sent and it descended a bit prior to VTOL transition about 30 seconds later. The user can command pauses during VTOL descent, it is to facilitate nudge and avoid obstacles.  @Wesley Reynolds Could you comment on the Override cancelled question? And can you put the goto event and VTOL transition on a plot of the AGL altitude? Thanks

### Wesley Reynolds, 2024-08-06

@Jeremy White 
To comment on “Override Cancelled” (068:05.141 and 068:23.375) means:
- When the vehicle transitions to Vertical Landing, the user has the option to “Activate User Override”.
- If the user selects the option to “Activate User Override”, then they will be able to “Nudge” the vehicle while it’s landing in order to control where the vehicle will land.
- Additionally, they will be able to “Cancel User Override”. When the user override is cancelled, the vehicle will go back into “Auto mode”, where the autopilot will be in complete control of the landing.
- This is why at the time 068:05.141 both “Override Cancelled” and “Auto mode automatically activated” are logged.

@David Grosher 
Here is an image that shows the AGL altitude at the time of the GoTo event (~3,909 s). The vehicle is ~2,950 ft AGL.
[embedded: GoTo-event.png]
Here is an image that shows the AGL altitude at the time of the VTOL transition (~3,937 s). The vehicle is ~2,552 ft AGL.
[embedded: Transition-event.png]
I can update the Vehicle Incident Investigation Report to include this if wanted. There are 0 events in between these 2 events, and none of the events that follow the VTOL transition seem extremely interesting to me, but I can plot some more events if wanted.

### Jeremy White, 2024-08-07

@David Grosher @Wesley Reynolds Thanks for your thorough replies! I will pass to the customer and I don’t see a need to redo any reports.

Is FDR000065 the correct datalog report? If so, did the event begin around line 222? I want to make sure I point them at the correct datalog for the tangential plane.

[embedded: image-20240807-122838.png]

### Wesley Reynolds, 2024-08-12

@Jeremy White yes, FDR000065 is the correct datalog report.

### Alexander Alan Arnold, 2024-12-10

@Ted Trowbridge Can this investigation be closed based on the findings?

### Ted Trowbridge, 2024-12-10

@Alexander Alan Arnold 
The corrective actions are being implemented as a change to the GCS that will ship in the next release planned for January.  Should the ticket stay open until then or can it be closed now?

### Alexander Alan Arnold, 2024-12-10

I would check with David G, but if you have nothing left to investigate and we know the CA will be implemented in a future release then I do not see why we can't close it and then the CA item would just stay opened until it is implemented. @Ted Trowbridge

### Alexander Alan Arnold, 2025-01-10

@Ted Trowbridge @David Grosher Are we fine with closing this item since the CA is being worked?

### David Grosher, 2025-01-10

@Alexander Alan Arnold We will close this issue following the release of the software update that fixes it. The release is undergoing testing.

## Attachments (7)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| VTOL_VXE556.zip | archive | 56145 | 2024-07-19 | listed only |
| XCOMM_VXE556.zip | archive | 73291 | 2024-07-19 | listed only |
| T95_V556_240715_131205_pack.zip | archive | 306 | 2024-07-22 | listed only |
| [AC556_Investigation.pptx](attachments/22228_AC556_Investigation.pptx.md) | pptx | 3691 | 2024-07-31 | converted |
| GoTo-event.png | image | 42 | 2024-08-06 | listed only |
| Transition-event.png | image | 39 | 2024-08-06 | listed only |
| image-20240807-122838.png | image | 104 | 2024-08-07 | listed only |
