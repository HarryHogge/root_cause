# VA-391: Address loose bus bar on VTOL AP board. Determine if service bulletin or AD are recommended. Create tasks for that if so.

- **Issue type:** Task
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2023-08-29
- **Updated:** 2026-03-30
- **Resolved:** 2026-03-30
- **Reporter:** Greg Fryer
- **Assignee:** Adrian Garcia
- **Creator:** Greg Fryer
- **Parent:** VA-1030 TPTR-6 (VXE 489 w/408 CW VTOL partial start) and loose bus bar
- **Links:** blocks VXEP-8 (TPTR-6 VXE 489 fuse 408 CW VTOL Motor delayed start); is duplicated by VA-245 (VXE489 Fuse/VXE408 Determine (and define) if a Corrective Action needs to be taken to prevent Ballast weight from breaking loose again); relates to VA-476 (Investigate if autopilot was reused from previous incident and could have contributed to latest crash. ); Linked issue cannot finish until this issue finishes. VA-1922 (VXE 464 VTOL AP weight, dust, and sand discovered loose in center wing)
- **Epic Link:** VA-1030

## Description

Based on parent incident, review Center Wing Avionics Board Assy (P/N: 107-101161) and determine if plastic fasteners on one bus bar can/should be replaced with brass (like other side). May need EE support to check for shorts (unk why one side is plastic).
Initial options: 
- replace nylon screws with more durable material? -open linked corrective action.
- Potential over torque-review traveler, implement torque spec/tool.
- Was the correct loctite used in this case?
- Is the screw too long, bottoming out against the opposing screw? Check tolerances.

## Sprint

VXE-1 Electrical-8, VXE-2 Everything Else 2024-03, VXE-2 Greg's Team 9-17, VXE Product Dev & Sup 2024-07, VXE-2 Mechanical+Prod 09-Oct, VXE-2 Production, VXE Product Dev & Sup 2024-05, VXE-1 Electrical-7, VXE Prod Dev & Sup 2024-08

## Plan

@Matt Weber what is the concern with using brass? It is non-ferrous, so should not affect the magnetometer. We could measure the increase in weight vs total for the board and see if it would affect the AP vibration isolation.

## Issue Status

Investigation shows CW408 was not inspected after its hard landing. Are we comfortable attributing this broken fastener to that incident and closing this task? Otherwise we have 2 options
- Quality gets a torque wrench and we continue to use current hardware
- Quality gets a torque wrench and we continue to use current hardware until EE tests circuits etc. and gives an ok to use brass

@Matt Philley l’m assigning to you, please close if you think we’ve found root cause or assign to the appropriate person to implement tools and update work instructions.

## Comments (17)

### Greg Fryer, 2023-08-29

@Matt Weber I assigned this to you, putting it in the current sprint. See linked issues for more info. (Its a bit of a tangle of tickets, sorry)

### Matt Weber, 2023-08-30

@Ryan Ferguson I’m looking at assembly 107-101161, and changing the screws appears to have no impact on the AP Interface board, in fact the opposite screws started out as nylon and were changed to brass shortly after.  The VTOL autopilot board, however, has a lot of components close to the fastener locations (see pic).  Using brass screws will bridge locations 1 and 2.  Is this ok?
I think that if we need to maintain isolation of these points, we should still use metallic hardware for strength but change the ballast(s) to be non-conductive.
[embedded: image-20230830-215731.png]
[embedded: image-20230830-220248.png]

### Ryan Ferguson, 2023-08-31

@Matt Weber my understanding is that the screws highlighted have always been nylon.  This is due to the risk of interfering with the magnetometers located on the VTOL autopilot, less than an inch away.  We have apparently had issues when metallic screws were used in this assembly in the past.  
I do not believe there are any electrical concerns with bridging the two locations as the screw posts are all electrically grounded through the carrier PCB anyway.  @Cameron Chapman can probably confirm this.
Might I ask what swapping to brass screws will change?  I saw the ticket (VIT-272) about the ballast swinging, however I do not see how changing screw materials from nylon to brass will prevent them from backing out.  The only methods I know of that would prevent this would be to stake the screws with an adhesive (RTV 732?), using safety cable, or redesigning the mechanism with a locking mechanism to retain the screw.

### Matt Weber, 2023-08-31

@Ryan Ferguson I believe the fastener had broken and that a stronger screw should fix that issue.  If it is a case of backing out, then yes, any of the solutions you have stated would be sufficient.  From VIT-272 there are pictures of the threads still engaged with the head missing.  @Hayden Jeanor can you confirm that is what’s in the photo? It looks like you had posted it originally.
[embedded: image-20230831-213056.png]
I feel that magnetometer interference of the ballast itself overshadows the addition of metallic screws, but I don’t exactly how those numbers add up.  If we do need to use non-metallic screws, a button head should survive where the csk fails as the sharp edge can knife into fasteners.

### Hayden Jeanor, 2023-08-31

@Ryan Ferguson @Matt Weber Sorry it is hard to see from the picture, but the nylon screw sheared off likely due to vibration/over torqueing

### Matt Weber, 2023-09-06

So what’s the call, @Ryan Ferguson… do you need plastic or can I sub in brass?

### Ryan Ferguson, 2023-09-07

I believe we can work with brass.  Given that this failure could be partially contributed to an incorrect torque value, could we also get a torque specified for all screws on the VTOL AP assembly?  This would be easy to add to the drawing while making the brass substitution.  We can partner with Quality to get an appropriate torque screwdriver on order for production.

### Hayden Jeanor, 2023-09-07

@Matt Weber if we switch to a brass screw, EE will probably want to perform some testing to ensure there is no interference with the mag. I dont anticipate introducing a a little more brass near the mag considering the much-larger ballast weight is closer in proximity to the mags and because brass isn’t ferrous. Also to respond to your previous comment, @Ryan Ferguson , the screw posts are connected to the ground of the AP interface board, but the brass ballast weight is separated from these posts via a nylon spacer (item 9). My concern is that the pervious designers isolated the weight to prevent any current from flowing through the weight and creating a magnetic field surrounding the weight, passing through the mag. Replacing the nylon screw with brass would allow this current to flow again.

### Matt Weber, 2023-09-11

This plane was potentially involved in a hard landing / high-G incident and is currently under investigation.  If these fasteners had previously experienced higher loads than designed and were not replaced, this could be a stand-alone incident and we may not need to look into changing hardware across the fleet.

### Matt Philley, 2023-09-11

AC 408 VIT2 for the hard landing: https://jenaero.atlassian.net/browse/VIT2-193

### Matt Weber, 2023-10-03

Investigation shows CW408 was not inspected after its hard landing.  Are we comfortable attributing this broken fastener to that incident and closing this task?  Otherwise we have 2 options 
- Quality gets a torque wrench and we continue to use current hardware
- Quality gets a torque wrench and we continue to use current hardware until EE tests circuits etc. and gives an ok to use brass

@Matt Philley l’m assigning to you, please close if you think we’ve found root cause or assign to the appropriate person to implement tools and update work instructions.

### Matt Philley, 2023-10-03

@Marc Richardson FYSA I believe you assigned TPTR-6 to Brad, so I will assign to you for now for that hand-off.

### Cameron Chapman, 2024-09-03

@Matt Weber what is the concern with using brass? It is non-ferrous, so should not affect the magnetometer. We could measure the increase in weight vs total for the board and see if it would affect the AP vibration isolation.

### Matt Weber, 2024-09-03

ME has no concerns with brass and would actually prefer it for strength.

### Cameron Chapman, 2024-09-03

@Adrian Garcia can you please coordinate testing brass screws in this location? I am thinking something like this. 
- Record VTOL mag readings without the brass bar. This mag is already highly influenced by VTOL current, and therefore is not used much in flight.
- Record with the brass bar and standard nylon screws
- “ with brass bar and brass screws. Measure resistance and voltage between both sides to see if it changes/indicates current.
- Report information to me and SW engineering. See if they think and risk and if they are ok with flight testing this change.
- Install on engineering asset. Ground and flight test.
- Review data to see if any performance impact.

### Matt Weber, 2024-09-10

@Adrian Garcia I have the screws for you, PN2119142-06

### Cameron Chapman, 2025-03-11

@Pat Wells here is the previous issue. Please link to latest.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20230830-215731.png | image | 41 | 2023-08-30 | listed only |
| image-20230830-220248.png | image | 2392 | 2023-08-30 | listed only |
| image-20230831-213056.png | image | 1853 | 2023-08-31 | listed only |
