# XKIT-2421: XKIT - Demo Prep Incident 20240612

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-06-12
- **Updated:** 2026-03-02
- **Resolved:** 2024-08-08
- **Due:** 2024-06-21
- **Reporter:** Carl Graf
- **Assignee:** Carl Graf
- **Creator:** Carl Graf
- **Labels:** Havoc, XKIT
- **Links:** relates to XKIT-2269 (Perform Weight Envelope Expansion Test Flight - Flutter VTOL C&A (20240612)); relates to XKIT-2436 (Create and Implement Protocol to cut fuel to FC in the event of emergency (similar to auto-cut & safe motors mode)); relates to XKIT-2478 (VTOL Ibatt readings varying during FW flight of Xkit test flight V371); relates to XKIT-1958 (Havoc 550 fuse 371 CW - Land Transition Failure 20240423); relates to VXEP-283 (VXE-533 Uncontrolled drift and crash after failed VTOL abort); relates to VXEP-231 (VXE-496 with 550 wing set-failure during VTOL transition-AS150 contact issues); relates to XKIT-1848 (Track Asset #N371VX (FC SN004) (AV Crashed))
- **Start date:** 2024-06-12
- **Sprint:** XKIT 7/10-7/30, XKIT 5/29-6/18, XKIT / LRR 6/19-7/9, XKIT 7/31-8/20
- **Customer:** XKIT
- **Vehicle Tail Number:** N371VX
- **Vehicle Configuration:** Stalker-Havoc Prototype (XKit)
- **Problem Type:** Other (explain in description)
- **Incident Type:** Aircraft Loss
- **Monitor Type:** Flight Test (Engineering)
- **Severity:** 1 - Flight Critical
- **Components (EA Aircraft):** Aircraft, full assembly
- **Job Number:** J100114 - VXE X-Kit Prototype

## Description

Sharepoint folder: XKIT-2421
Powerpoint: XKIT-2421.pptx
SW version: 6.2.9
- Prep for flight
- Flight prior to drop
- On base turn to drop run, lost Silvus, typical dead zone on approach to drop
- VTOL webpage had stopped updating
- Drop - dropped Quad FPV & mortar
- Post-drop
- VTOL webpage was still not updating
- Continued with orbits, discussion and response
- Called Kurt
- Got consensus of what to look for
- CAN data was going thru but nothing else
- Kurt and Dave were consulted on how to land aircraft
- Weighed pros/cons of VTOL vs FW landing
- Attempted VTOL with RC as back up
- Spent good 10 minutes discussing how to respond to a fire event
- Collected fire suppression equipment in
- Attempted landing
- Transition to VTOL
- Did not look good
- Overshot first landing spot, large dirt patch near corner of pen
- Overshot second landing spot
- RC control attempted but did not get command from aircraft
- Controllers appeared to be fighting each other
- GCS indicated RC was active
- Nose dive into ground very quickly, no time to cycle between systems
- VTOL props spinning (video from Carl)
- Crash
- Aircraft immediately caught fire
- Artis, Matt & Carl pulled up in van with extinguishers and doused flames quickly
- Got propane tanks away from fuselage to prevent adding fuel to fire
- One tank ruptured, one remained in tact
- Key parts with data
- Avionics box & VTOL board (located outside Greg’s office)
- Data was retrieved
- Resemblances to previous incidents
- 550, Camp Lejuene 
- VTOL task lock during FWF
- VTOL system came on during landing transition but was not sending correct signals to control the AV properly
- Destabilization of AV
- Take off transition was considered normal
- VTOL lock up appears to only affect landing transition
-

## Comments (3)

### Carl Graf, 2024-06-13

@Greg Fryer I captured your notes in the presentation I am working that is now linked in the description of this ticket.

### Carl Graf, 2024-06-24

@Kurt Burian @Hayden Jeanor just a reminder to capture info (artifacts, time spent, etc.) related to the most recent incident here under this incident ticket. Populate the PowerPoint as needed to support the RCCA.

### Christa Meck, 2025-04-17

Removed parent to prep for Incident hierarchy change.  Parent is linked as Linked issue.

## Attachments (0)
