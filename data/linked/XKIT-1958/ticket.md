# XKIT-1958: Havoc 550 fuse 371 CW - Land Transition Failure 20240423

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-04-23
- **Updated:** 2026-03-02
- **Resolved:** 2024-07-02
- **Due:** 2024-05-02
- **Reporter:** Cameron Chapman
- **Assignee:** Carl Graf
- **Creator:** Cameron Chapman
- **Labels:** XKIT
- **Links:** relates to VXEP-283 (VXE-533 Uncontrolled drift and crash after failed VTOL abort); relates to VXEP-231 (VXE-496 with 550 wing set-failure during VTOL transition-AS150 contact issues); relates to XKIT-2421 (XKIT - Demo Prep Incident 20240612); relates to VXEP-835 (VXE 568 turned 180 degrees entering VTOL, made strained noise then nose dived); relates to XKIT-1027 (Track Asset #550 (Crashed 550 fuse w/#371 Wings, FC SN005))
- **Start date:** 2024-04-23
- **Sprint:** XKIT Sprint 4/13-5/7, XKIT 5/8-5/28, XKIT 5/29-6/18, XKIT / LRR 6/19-7/9
- **Customer:** XKIT
- **Vehicle Tail Number:** 550 fuse 371 CW rudder and elevator
- **Vehicle Configuration:** XKit
- **Other Stakeholder (as required):** Travis Blaschke
- **Problem Type:** Other (explain in description)
- **Incident Type:** Aircraft Damage
- **Monitor Type:** Flight Test (Engineering)
- **Severity:** 1 - Flight Critical
- **Components (EA Aircraft):** Aircraft, full assembly, Software, VTOL, VTOL Board
- **Job Number:** J100114 - VXE X-Kit Prototype

## Description

Please save related files here: 
XKIT-1958 Havoc 550 fuse 371 CW - Land Transition Failure
From Sam,
All, the MARSOC briefing and first flight of the Havoc demo was flawless. The second flight with FOV drop and mortar drop also went well…until landing. Unfortunately, we appear to have experienced a hardware failure of the lift system that we could not recover from. The lift system was extremely loud when it engaged.  It appeared that the vehicle aborted to fixed wing flight, but the lift system would not shut off…perhaps a race condition? We tried to override the VTOL several ways to attempt a glide landing, but to no avail. We honestly didn’t have a whole lot of time and ultimately ran out of altitude, crashing in the dense woods away from the demo site. Thankfully, no fire and we had comms with it enabling us to find it quickly. We have recovered the main pieces and are trying to find the lift motors and tanks now. Very sorry guys.
 
 
From Cody,
Configuration was, 550 fuselage and 371 center wing. Payloads were dropped prior to landing (1x FPV and 1x 1lb 60mm), E95 was in center payload. <500g fuel. 4.7”cg
On final, VTOL system powered on with greater noise level than usual. Vehicle passed landing zone and continued with what appeared to be both fixed wing and vtol system active. Shortly after a land immediately was commanded with no change. GCS popped notification that ELZ was active / vehicle was going to ELZ. Lost communications occurred for brief period of time. Communications came back and a go to was issued (possibly this occurred prior to lost comms, cannot recall). Vehicle appeared to track back towards orbit but then changed path again. Vehicle then proceed back to wood line where RC was commanded in fixed wing mode and both sticks were moved to forward position in attempt to terminate flight in wooded area. Unknown if this had any effect but flight terminated in wooded area.
 
Vehicle was partially recovered. Missing portions of lift booms and one motor/esc combo and one ESC.
 
AARs & SA cam video are uploaded  here. Photos of damage available upon request (Sam has some). Forward as required. Pictures of damaged parts here: Flight Safety - VXE-550 pics - All Documents (sharepoint.com)
XComm Datalog: T95_V550_240423_091839_xcl00319.csv
VTOL DataLog:

## Corrective Action

Corrective action was to roll the version back to the last known good version. This is captured in the following ticket.https://jenaero.atlassian.net/browse/XKIT-2176

## Plan

- Data review. 
- Kurt and Jason are looking into SW/FW data
- Hayden is reviewing ESC data
- Canceled Envelope Expansion Flight Test on 4/24
- Delivery of equipment shows 4/29 between 8am and 3pm. It's on a private sprinter. No tracking number
- Tag equipment involved with Jira and AV#. Install AP boards in to 510 IB HIL (currently on Liams desk).
- Dave: “I would like to get the AP boards and get them into an iron bird configuration for testing. We can run it on the current software for a while to see if we can recreate an issue. And if we can we can see if the new SW fixes it or at least helps us to debug it. “

## Issue Status

result of our Initial investigation. Data indicates the VTOL experienced priority inheritance (a known bug fixed in VTOL 1.54) mid fixed wing flight which prevents the priority 1 tasks from running. This is evident in the XComm logs as the data received from the VTOL only updates from tasks, in the VTOL AP, that are above priority 1 while priority 1 data becomes static. This likely caused issues during landing which could account for the observed abnormal behavior. After missing the landing, the operator issued a "Land Immediately!" command which caused the land abort bug to be activated in the fixed wing (known bug resolved in the upcoming FW AP 6.05p release).
Vehicle was partially recovered. Missing portions of lift booms and one motor/esc combo and one ESC. Cody will pull logs before shipping back tomorrow. No one will likely look for more parts unless we send someone out. Have fuselage and center wing. Have 1 motor with ESC. Another motor with no enclosure. FL motor and ESC intact.
[11:10 AM] Dave Grosher
FYI, it appears that the VTOL AP had all of the Priority 1 tasks locked out for the last ~7 minutes of flight. I have never seen the VTOL AP lock up for this long. I would like to get the AP boards and get them into an iron bord configuration for testing.

## Root Cause

Not identified. Ironbird/HIL sims did not yield a repeat task lock-up. Mitigation through SW revision. See https://jenaero.atlassian.net/browse/XKIT-2176

## Comments (20)

### Cameron Chapman, 2024-04-23

Crash location was in heavily wooded area. We found what we could without a full blown carrier walk.
Cody 
From: Hayden Jeanor <hjeanor@edgeautonomy.io>
Sent: Tuesday, April 23, 2024 11:45 AM
To: Cody Smisek <csmisek@edgeautonomy.io>; Carl Graf <cgraf@edgeautonomy.io>; Travis Blaschke <tblaschke@edgeautonomy.io>; Travis Storm <tstorm@edgeautonomy.io>; Dave Grosher <Dgrosher@edgeautonomy.io>
Cc: Greg Fryer <gfryer@edgeautonomy.io>; Michael Archuleta <MArchuleta@edgeautonomy.io>; Kurt Burian <kburian@edgeautonomy.io>; Sam Miller <smiller@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>; Matt Weber <mweber@edgeautonomy.io>; Scott Stuckey <sstuckey@edgeautonomy.io>; Jason Scherer <jscherer@edgeautonomy.io>; Jeremy White <jwhite@edgeautonomy.io>
Subject: RE: Havoc Incident Camp Lejeune 4/23/2024
 
Unfortunate to hear gents. Thanks for the work out there. Locating all the ESCs will be extremely beneficial to the investigation in case they are in-tact enough to pull logs from.
 
Thanks,
 
|  | Hayden Jeanor |

### Jason Scherer, 2024-04-23

BLUF: Yes there was a land abort, but it was a symptom of a bigger still unidentified issue.
XComm noted a minimum power (<500W) fault during landing as well as differential throttle values during the landing phase. An abort was eventually executed but not till after the operator issued a “Land Immediately!” command from the GCS. After talking to Cody the vehicle unresponsiveness started before this.
The normal landing aborts were commented out of x-kit firmware a while back, but you will still see the messages in the logs to identify vehicle issues. 
Example: 
[embedded: image-20240423-203129.png]
However, the “Land Now” state machine which is started after issuing a “Land Immediately!” command from the GCS still have some paths to abort logic.
This is the code (fixed wing ap) that contains the abort that was executed during this flight. 
[embedded: image-20240423-203036.png]

### Jason Scherer, 2024-04-23

Here is a breakdown of the vt status bits reporting at the start of the land abort. 
[embedded: image-20240423-205717.png]

### Jason Scherer, 2024-04-23

VT reported altitude during crash flight as reported by XComm. X-Axis is UTC
Edit: Added HLB volts/current, throttles, HLB volts reported by FC.
[embedded: image-20240423-212432.png]

### Jason Scherer, 2024-04-23

Altitude, Forward Power (watts), and airspeed as reported by fixed wing ap.
[embedded: image-20240423-214418.png]

### Jason Scherer, 2024-04-23

Real Altitude versus Commanded Altitude from XComm log
[embedded: image-20240423-222307.png]

### Jason Scherer, 2024-04-23

I12V (12 Volt Bus Current) compared to altitude. Hayden believes the drop-off in current after launch is due to the nose cone fan turning off.
[embedded: image-20240423-224529.png]

### Jason Scherer, 2024-04-23

Network link between XComm and VTOL is up the whole flight. 
[embedded: image-20240423-225354.png]

### Carl Graf, 2024-04-23

[embedded: image-20240423-232310.png]


[embedded: image-20240423-232328.png]

### Carl Graf, 2024-04-23

Can someone please share with me what Sam means by “race condition”?

### Cameron Chapman, 2024-04-23

@Carl Graf Linked other race condition incidents. Firmware guys could explain better, but similar incidents sounded like
- VTOL abort due to something like a power fault
- FWAP tries to take over.
- VTOL AP never cedes control, so they both try to control the aircraft until crash.

I think the latest software has some fixes for it, but as you know, it has not been merged into Havoc yet. Please correct anything above. 
 https://jenaero.atlassian.net/browse/VXEP-283 
https://jenaero.atlassian.net/browse/VXEP-231

### Cameron Chapman, 2024-04-24

Throttle 4 (left rear) is low throughout 1 as well, 3 is high. This seems to indicate the vehicle was rolling more right that it wanted to. @Hayden Jeanor Are those seconds on the X axis? I think no. I think adding time to X axis would be helpful

Based on the description, it sounds like transition started and quickly aborted for some reason, and the VTOL didn't shut off similar to those previous incidents. @Jason Scherer @Hayden Jeanor @Carl Graf re we able to line up these events to see if they happened in the right order?
- Transition commanded
- VTOL throttles and VTOL current start simultaneously.
- Do we have record of an automatic transition/VTOL landing abort?
- When did the VTOL board stop reporting data to the XCOM in this sequence?
- Compare expected vs actual VTOL power based on throttles.

[embedded: image (2)-20240424-162521.png]

### Hayden Jeanor, 2024-04-24

I think I got the VTOL logs figured out: 
- Vtl 446 Is the flight prior
- Vtl447 the takeoff of the crash flight and ~half of FW flight
- End of Vtl447 corresponds with data loss (Ibatt and Vbatt) between Xcomm and VTOL @ UTC 163059
- Vtl448/449 is during/after the crash?
- the reason there is an abnormal number of VTOL logs in the AAR - VTOL doesnt normally reset during flight


@Cameron Chapman Time is plotted on the Xaxis. Not UTC, though. CpuTime

### Rajesh Budhabhatti, 2024-04-30

Repaired the dropper assembly and returned it to Artis.

### Rajesh Budhabhatti, 2024-04-30

Uploaded pictures of damaged parts here: Flight Safety - VXE-550 pics - All Documents (sharepoint.com)

### Rajesh Budhabhatti, 2024-05-01

Extracted AP, electronics and harnesses from center wing. Extracted XCOMM avionics box. Most electronics look ok with a few wires ripped off. Avionics box looks fine. I will label harnesses and will move them to Ironbird/HIL testing today. Investigation report started here: XKIT-1958 Havoc 550 fuse 371 CW Investigation Summary.docx.

### Rajesh Budhabhatti, 2024-05-01

Completed setting up Ironbird/HIL for Jason.

### Carl Graf, 2024-06-25

@Kurt Burian, this is the ticket for the Marsoc crash on 4/23. There is a PowerPoint file in the hyperlinked folder in the Description above. Please add some notes and LMK. I will review and close out the ticket.

### Carl Graf, 2024-07-02

This issue is similar to https://jenaero.atlassian.net/browse/XKIT-2421 in terms of a VTOL lock up. Unfortunately, a comparison of the two incidents cannot confirm identical root causes/corrective actions. 

Fortunately, the other incident had a diagnostics-enabled version of SW that allowed for identification of the root cause, implementation of a corrective action and test results that confirm that the issue is unlikely to recur.

### Christa Meck, 2025-04-17

Removed parent to prep for Incident hierarchy change.  Parent is linked as Linked issue.

## Attachments (11)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20240423-203036.png | image | 54 | 2024-04-23 | listed only |
| image-20240423-203129.png | image | 28 | 2024-04-23 | listed only |
| image-20240423-205717.png | image | 561 | 2024-04-23 | listed only |
| image-20240423-212432.png | image | 166 | 2024-04-23 | listed only |
| image-20240423-214418.png | image | 91 | 2024-04-23 | listed only |
| image-20240423-222307.png | image | 49 | 2024-04-23 | listed only |
| image-20240423-224529.png | image | 56 | 2024-04-23 | listed only |
| image-20240423-225354.png | image | 11 | 2024-04-23 | listed only |
| image-20240423-232310.png | image | 151 | 2024-04-23 | listed only |
| image-20240423-232328.png | image | 512 | 2024-04-23 | listed only |
| image (2)-20240424-162521.png | image | 331 | 2024-04-24 | listed only |
