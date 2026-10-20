# VXEP-385: New Connectors and Contacts, Overall Requirements Review

- **Issue type:** Initiative
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** High
- **Created:** 2023-08-14
- **Updated:** 2025-05-28
- **Resolved:** 2025-05-28
- **Reporter:** Cameron Chapman
- **Assignee:** Matt Weber
- **Creator:** Cameron Chapman
- **Labels:** 8-28-Sprint
- **Parent:** SP-206 Improve Power Connector, Contacts, and Signal Connectors
- **Links:** relates to VA-33 (VXE511 Aborted Launch at 2ft, VTOL ESCs stuck in initialization loop); relates to ENG-2226 (114-106085 - Need Note on Drawing about Squeeze-out Stay Out Zone); causes ENG-2983 (511 LW motor test failed. 511 and 516 center wings damaged. ); relates to VA-31 (EA Internal: 516 center wing damaged. 511 fuselage+516CW LW motor test failed. ); relates to VXEP-481 (8D #24 – CW to HLB AS150 Connection Issues​ Corrective Actions); relates to VXEP-477 (Old, internal work - Develop plan for latching power connectors (AS150 Replacements)); relates to VXEP-386 (Develop Replacement for AS150 Connections); relates to VA-553 (Review and improve receiving inspections for AS150 contacts); relates to VA-573 (Poor Quality/higher impedance plating on AS150 power contacts - Containment and Corrective Action); relates to XKIT-609 (Estimate Engineering tasks to deliver X-Kit Harnesses to Production); relates to VA-482 (553  Current Sense CW Power Connector, AS150 pin has solder blob.); relates to XKIT-603 (Production ROM); relates to ENG-3061 (VXE 454 Center Wing Power Connector solder melted); relates to ENG-1805 (Improve High Power Contacts and Connectors)
- **Part Number(s):** 107-102264 114-106085 100-102573 100-102570
- **Problem Type:** Discovered Issue

## Description

Summarizing recent issues and options to resolve. Shared onenote book here. Lift Power Connectors  (Web view) You are all welcome to add/modify. Likely easier to modify in onenote. 
Formal 8D: https://jenaero.sharepoint.com/:p:/s/ContinuousImprovement/EUP5VvyBE09Mte_5wSGWcHUBXCvOKny6UYF6mzoYLSLRWw?e=s3wCj5 
Relevant Parts: 107-102264 Dual Current Sense Assy (AS150 Connector) 114-106085 Hybrid Lift Battery, Heated, Assy​ 100-102573 – Connector Housing, AS150, Socket, D-Shaped 100-102570 – Connector Housing, AS150, D-Shaped

Process
- Move this to VXEP.
- Cleanup and merge duplicate process.
- Create epic and linked tasks for the tasks below. Assign to Connor or delegate
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

Consider combined power+signal connectors.

## Comments (8)

### Matt Philley, 2023-08-15

Added a note based on feedback from Thomas about the solder inspection for the contacts not being well defined. He mentioned the resistance might be fairly different part-to-part and we may not know it.

### Cameron Chapman, 2023-08-24

Linking subtasks to parent

### Cameron Chapman, 2023-10-12

@Connor Peebles are you availablle to create linked tasks and start this project?

### Connor Peebles, 2023-10-12

@Cameron Chapman yes I can do that, let me know priority and if it’s in current sprint

### Cameron Chapman, 2023-10-13

@Connor Peebles added to this sprint, high priority, but behind immediate production and field testing tasks.

### Cameron Chapman, 2023-11-17

@Connor Peebles , can you please make an epic for the tasks in this project, add to next sprint, and move this project to VXEP

### Cameron Chapman, 2023-12-11

Moving this out of description.



- Gather more info
- Record customer feedback/incidents.
- Link related incidents/problems.
- Add additional problems below.
- Problems and potential resolutions (need to scope each)
- Connectors are hard to mate and demate
- High force required to mate/demate connectors
- GO/NO GO force gauge
- Difficult to pull on connector, no pull strap
- Sharp adjacent fuselage edges cause operator injury.
- Contacts are hobby grade and not well controlled.
- Improve receiving inspection criteria.
- GO/NO GO mating connector.
- Evaluate tolerance stackups in connectors.
- No mating rention feature other than friction (ex: latch, bayonet, etc)
- Connector redesign.
- No complete mate indicator.
- Evaluate if adding a high-vis strip would work/help.
- Higher temp solder would give more thermal/current margin.
- Production issues/inspection misses
- Missing retention springs on socket contacts. Could increase wear/contact resistance/heating.
- Potting compound from sealing may be interfering with full mate. Could increase contact resistance/heating.
- Hard to control/inspect/and build consistent soldering/assembly process.
- Crimp contacts would be better, but not compatible and likely larger.
- Solder inspection is just visual, but evaluate if we need any resistance check or testing for soldering of these contacts.
- Multiple damaged connector incidents. More recently.
- Link issues.
- May be caused by factors above.
- Contacts are from an unreliable manufacturer. Too much variation and risk. Plating issues. https://jenaero.atlassian.net/browse/VA-573 
- Replacement contact needs to be anti-spark or upgrade ESCs and other electronics to no longer require.
- Implement plan for what issues to work on and when.

### Connor Peebles, 2023-12-11

I made this initiative [VA-1004] Improve Power Connector, Contacts, and Signal Connectors - Jira (atlassian.net) and moved all relevant information from this ticket to that one. The new ticket is the parent ticket of this one.
I am also pivoting this ticket as to collect the New Connector and Contacts Requirements and Review.

## Attachments (0)
