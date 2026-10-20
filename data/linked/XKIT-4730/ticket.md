# XKIT-4730: SB40x - N376VX: Network Issue

- **Issue type:** Problem
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2025-06-16
- **Updated:** 2026-03-30
- **Resolved:** 2026-03-30
- **Reporter:** Carl Graf
- **Creator:** Carl Graf
- **Parent:** XKIT-4517 Test & Down-Select New Motors for SB35/40
- **Links:** is blocked by VXEP-1309 (SB40X VXE376 Xcomm SD Issue); relates to VXEP-1230 (VXE 401 Lost Connection After Mission Sync); relates to VXEP-944 (VXE 614 Erratic behavior and propulsion failure led to crash ); is duplicated by VXEP-1307 (SB40x - N376VX: Network Issue); blocks XKIT-4741 (SB40x N376VX XCOMM SD Issue)
- **Epic Link:** XKIT-4517
- **Components (EA Aircraft):** Aircraft, full assembly

## Description

During flight testing per FTR039, operator reported loss of comms with aircraft while fuel cell was powered on and aircraft idle on the ground. Prior to this event, aircraft had aborted takeoff due to ‘vt lost link during lch’. 
Operator reported via Silvus RF, could see silvus and ipcomm but not xcomm or vtol. Operator direct connected through hood payload port and could see xcomm and vtol but not ipcomm or silvus. 
Outside air temp ~80-90F. 
Aircraft has avionics from 695 installed. 
Background 
- Aircraft configuration. Fuel cell every time? 4 total times.  Aircraft was powered via power supply (with fuel cell installed) in attempt to replicate problems on 6/14. Aircraft powered inside and outside for ~1-2hrs with no issues noted. Xcomm and silvus enclosure removed and replaced with new. Flight ops attempted to test again and issue persist when fuel cell was in the run state. FC each time (Not always in the same state of the FC, one warm, two in run, one in off.
- Locations? Huasna each time
- Radio or hardwired?

- Over radio each time when initially seen

6/17 Attempted Flights
Significant events from chat.
- 6/17 1240 Just lost data link and xcom on warm up of FC. I have the radio still 
- out of curiosity, where was the fuel cell at in this process?
 It was in warm I have the radio still
- 1245I now have everything back, I did nothing to change anything Was in warm up 
- When I got it back and was able to get into fc page. It was in state 5 run / system state 1 start 
and power output or zero output when you looked, just trying to see where the fuel cell is at when this is occuring 
 theory is that fuel cell is causing ground problems
- When I came back it was in state 5 run / system state 2 run and producing power
- 1250 Should we proceed to fly? Last time this happened we had done a launch and it aborted then this happened while we were waiting on data
- 1258 confirming same battery use this time as last time? and it was the grey one?   It was the grey one Record SN.
- 1333 The AC dropped while getting the AAR

## Plan

- Perform inspection of electrical grounding for potential power issues effecting network switches on xcomm.
- Record SN of battery.

## Issue Status

Aircraft was powered via power supply (with fuel cell installed) in attempt to replicate problems on 6/14. Aircraft powered inside and outside for ~1-2hrs with no issues noted. 
Xcomm and silvus enclosure removed and replaced with new. Issue persist when fuel cell is in the run state.

## Comments (4)

### Carl Graf, 2025-06-18

@Cody Smisek you swapped the XCOMM board and Silvus enclosure and we returned to flight but did we get enough data to close this ticket or did the new issues prevent us from collecting the necessary data to close this ticket?

### Cody Smisek, 2025-06-18

@Carl Graf I complete the xcomm and silvus swap. Aircraft did not return to flight. Issues persist. Recommend coordination with EEs to determine next steps.

### Cameron Chapman, 2025-06-18

6/17 Chat History
i probably wouldnt
 A Flight I’m not sure we want a lost coms with this Ac 🤔 
not with these untested changes 
 I vote for calling it until we know for sure, this would be the 1st flight since a lot of changes and we rely on RC backup for safety. Since it hasn’t flown yet I don’t trust it enough, I’d like someone to acknowledge and accept that risk if we proceed 
if it was back on the previous versions of known results, maybe if the reward was worth the risk. but i'm not seeing much reward here
 
yeah i mean, i don't really buy RC being a backup in general.... we're already 3 for 3 on comms drop outs. Don't fly it.
 
I'll talk to EEs see if there's recommendation on anything to scope to see what's going on for grounding, probably PITA to figure out 
 
I would also suggest not flying it. Might cause more issues than just lost comms if its a grounding issue in FC
 
Hah, that’s fair on the RC. 
 But yes, I don’t want the first transition to be potentially blind
 Shutting down the FC 
pull logs please
 
Cody Smisek
remaining items that seem most probable, 1) fuel cell causing power issues, 2) software doing software things

i'm also completely guessing on these ideas. input from others would be good
 
i'm not even sure how we'd locate / address a ground related issue 
 
confirming same battery use this time as last time? and it was the grey one?
 It was the grey one The AC dropped while getting the AAR AAR not completed but packing down FC had been off for a little while 
 
Cody Smisek 
i'm not even sure how we'd locate / address a ground related issue

 Measure for voltages where there shouldn’t be any. Test unplugging stuff, ab testing. Etc.
 
 I’ll be back tomorrow (and hopefully awake after a late arrival tonight) 
Cameron, Cody, Jeremy, Christopher, let's discuss at this afternoon's EPS Weekly. Cody/Jeremy, I just added you to the invite.
 
Sounds good. Let me know I can help/catch up sooner. 
 
Do we have anywhere we are documenting the problem/troubleshooting steps
 
Carl Graf I don't see this project listed on the top priorities board, this also conflicts with a meeting i have for a project that is. I will only be available for the first half 
 
Cameron Chapman
Do we have anywhere we are documenting the problem/troubleshooting steps

https://jenaero.atlassian.net/browse/XKIT-4742
[embedded: 10565]
XKIT-4742: SB40x - Resolve Fuel Cell/SW/?? Issue from flight on 20250617
 
Cody Smisek
CarlGraf I don't see this project listed on the top priorities board, this also conflicts with a meeting i have for a project that is. I will only be available for the first half

This board? Top5.xlsx
Top5.xlsx
 
i have no idea what that spreadsheet is, i'm referring to the whiteboard downstairs 
 
Carl Graf we should already have numerous tickets created with documented information. what is that ticket for that you just sent?
 
Cody Smisek
CarlGraf we should already have numerous tickets created with documented information. what is that ticket for that you just sent?

It sounded like yesterday's issue was a new issue. Was it not? 
 
Previous was SD Issue, then a new ticket was issued for a Network Issue, and yesterday's was described as a Fuel Cell/SW issue. Are they all the same and we are just chasing the symptoms or are they different issues?

### Cody Smisek, 2025-10-21

Hardware related to 695, 376 placed in storage under stairwell in NCR/red tagged cabinet.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 10565 | other | 2 | 2025-06-18 | listed only |
