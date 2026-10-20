# SP-206: Improve Power Connector, Contacts, and Signal Connectors

- **Issue type:** Program
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2023-12-11
- **Updated:** 2026-05-06
- **Resolved:** 2026-05-06
- **Reporter:** Connor Peebles
- **Assignee:** Adrian Garcia
- **Creator:** Connor Peebles
- **Labels:** EE-Consultant
- **Links:** is caused by ENG-3061 (VXE 454 Center Wing Power Connector solder melted); is caused by ENG-2983 (511 LW motor test failed. 511 and 516 center wings damaged. ); is caused by VA-573 (Poor Quality/higher impedance plating on AS150 power contacts - Containment and Corrective Action); relates to ENG-2427 (Evaluate alternate connectors for production units); relates to XKIT-761 (Evaluate using crimped and locking signal connectors for new X-kit connectors); relates to VXEP-232 (Overheating Battery/Cable (Fuel Cell Support Kit SCO Test Config) -); relates to XKIT-2033 (Perform Market Survey/Down-Select, All Connectors); relates to XKIT-1716 (SB40 Vehicle Power Switch); relates to XKIT-753 (Design SB40 Electrical Power System (EPS))

## Description

Summarizing recent issues and options to resolve. Shared onenote book here. Lift Power Connectors  (Web view) You are all welcome to add/modify. Likely easier to modify in onenote. 
Formal 8D: https://jenaero.sharepoint.com/:p:/s/ContinuousImprovement/EUP5VvyBE09Mte_5wSGWcHUBXCvOKny6UYF6mzoYLSLRWw?e=s3wCj5 
Files: AS150 Replacement
AS150 Replacement RVTM.xlsx
Created a Marquee to encompass the desired replacement of all necessary contacts for VXE2024
IRAD Project folder: VXE_Contact_&_Connector_Replacement
See AS150 Replacement, Contact Options Matrix.xlsx

Everything below here is to be organized better…

Process
- List requirements.
- List contacts and connector options.
- Modify existing connectors
- Outsource connector design.
- Test contacts.
- Downselect contacts and connectors.
- Ensure new ESCs have anti-spark circuitry, or develop alternate option. Link to here.
- Test and integrate.



FYI @Greg Fryer @Scott Stuckey @Sam Miller @Matt Philley @Ryan Ferguson @Ben Norris 

Requirements List
Connector
- Need to have
- Latching/locking feature
- Mate indicator (not required if latching obvious/visible/audible).
- Sealed. Rain, submersion if water pools in aircraft.
- Approximately the same size as existing. We can send dimensions.
- Bulkhead mount for battery one.
- 2024 version not compatible with VXE30 to prevent plugging 60V into 28V VXE30.
- Anti spark feature may be required. Ideally not if soft start added to downstream devices.
- Reliable.
- Reduce force required to mate and demate.
- Nice to have
- blind mate if feasible, ?
- Mixed Signal and power connector.

 
Contacts
- Need to have
- Meets current profile in 50C OAT. List for each.
- High enough mate cycles.

 
- Nice to have
- Crimped contacts.
- Multiple sources (Ex: mil standard).

## Comments (4)

### Connor Peebles, 2023-12-11

@Cameron Chapman @Greg Fryer I organized the Contact and Connector Replacement Project into an initiative with branching Major projects, Epics, and tasks, hoping for the @Carl Graf Signal of approval.
Going to name it a VXE2024 initiative, though some replacements may be effective VXE30 but that decision should be solidly made

### Connor Peebles, 2023-12-12

Updated to Marquee w/ initiatives per Carl’s direction

### Connor Peebles, 2023-12-14

This task was updated into an all-encompassing marquee that also includes AS150 replacement that you’ve been helping me with. There is also this seemingly duplicate task assigned to Stephen Peters [XKIT-760] Develop new battery power connectors for production Xkit. - Jira (atlassian.net). Granted it is for x-kit.
@Cameron Chapman Could you clarify who is doing the work? Is the work separate?

### Cameron Chapman, 2023-12-14

@Connor Peebles they are related and duplicate. We should combine info from both and close that one. Since it involves mechanical vehicle design, we should assign it to all then communicate ideas and battery requirements to AA

## Attachments (0)
