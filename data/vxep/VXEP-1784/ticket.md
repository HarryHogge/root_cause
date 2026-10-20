# VXEP-1784: VXE-919 Ocean glide landing after fuel cell stopped working in flight and wouldn't restart.

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** High
- **Created:** 2026-03-23
- **Updated:** 2026-07-06
- **Resolved:** 2026-07-06
- **Reporter:** Michael Mohr
- **Assignee:** David Grosher
- **Creator:** Michael Mohr
- **Labels:** Ann_Arbor, GS_Closed, NSW, RCCA
- **Links:** relates to RMA-966 (VXE-919 RMA 260416-1)
- **Customer:** NSW
- **Vehicle Tail Number:** VXE-919
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical

## Description

On Friday, 20 March 2026, VXE-919 was 3+ hours into a fuel cell flight over open ocean at approximately 3000 feet when the fuel cell shut down and would not restart. It had flown the previous three days without issue. Operator reports that there were 200grams on the gauge when the shutdown occurred. Multiple restarts were attempted. Payload power was shut off, and restart was attempted as well. Aircraft was recovered from the water and is being held at SBT facility until the unit returns to the mainland on Friday the 27th to retrieve it and attempt to download data. 
No data yet, will update as it becomes available.

## Vehicle Configuration

Adv Nav
Fuel cell

## Plan

- Waiting on Customer to provide Data - Customer provided GCS logs only

@Michael Mohr: 
- follow up with Customer on if it was fresh water rinsed. Get pictures. RMA to conduct inspection.
- Pull data from SD cards when the AV is received.


@David Grosher : 
- Check NAV_STATE and VTOL_STATE for indication of automated recovery.
- Check Mission Data on the SD card.
- Check for any other faults.
- If a new mission is uploaded is the origin of the LTP shifted?

## Issue Status

Appears that the Fuel Cell did not stop but throttled down because the HLB was full. HLB was never exhausted. AV appears to have received a new mission and was sent to the PLZ prior to HLB throttling, unclear why the PLZ would be over the ocean. Need to check any automated action that could trigger a recovery.

## Comments (12)

### Drew Hildreth, 2026-03-25

Waiting on Customer to provide Data

### Michael Mohr, 2026-04-16

@David Grosher I looked at the data here and from what I can tell, everything looks normal until the fuel cell appears to shut off.

### David Grosher, 2026-04-16

The system appears to be fine, but I would like to have the AA team look at it, @Christopher Ridgard. It seems that the FC was throttled because the HLB was full. I suspect this was interpreted as it having stopped. It appears to be ramping back up ~400 seconds after power drops off. As it is ramping up the system transitions to VTOL for recovery. All of this happened enroute to the PLZ while it was descending. There are no changes to the FC fault bits or state to indicate that anything abnormal happened. 
[embedded image-20260416-215626.png]

### David Grosher, 2026-04-16

@Michael Mohr Is this the correct data? I don’t see the FC stopping and I see it entering the landing pattern and landing.

### David Grosher, 2026-04-16

@Michael Mohr Can we pull the SD card contents from the XCOMM? Thanks.

### Michael Mohr, 2026-04-16

@David Grosher It is being RMA’d along with 920. I looked at the fuel cell log and it looked like it just stopped. They said it spraled down once the HLB died. Xcomm log looks like thats what happenned from the heading during the decent from what I can tell. Please feel free to correct me if I am missinterpreting the data. It also looks like alot of the Vtol data is missing.

### David Grosher, 2026-04-17

@Michael Mohr I don’t see any indication that the FC stopped in flight from the Fuel Cell log or the fuel cell data in the XCOMM log. It appears to be tracking the desired power output because the HLB was full. I also see no indication of the HLB running out of energy. The VTOL datalog that was captured doesn’t appear to capture the correct logs, it looks like it stops during motor checks before launch. Right now it looks as if it flew the mission as designed. But when we receive the bird we should pull the content from both SD cards.

### David Grosher, 2026-04-17

Here is the observed orbit prior to landing. It appears to be IP1 in the landing pattern. Did not land far from (0,0), need to confirm that the origin does not change with a new mission plan. 

[embedded image-20260417-161743.png]

### David Grosher, 2026-04-17

@Michael Mohr The data is from the 3/19 but the incident in the operators description reported the incident occurred on 3/20. This may have been one of the successful flights referenced in the statement.

### Christopher Ridgard, 2026-04-21

I do not see anything unusual in fuel cell data.  It looks like a typical flight profile.

### David Grosher, 2026-05-15

@Michael Mohr We couldn’t pull the data from this aircraft due to damage on the SD card sustained in the crash. We suspect that it is the same issue as 920 based on the operator statements but we won’t be able to investigate further. I suggest closing this and putting into the Bermuda Triangle. @Drew Hildreth

### Scott Lovett, 2026-07-06

Report sent, Advisory Notice created.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T115_V919_260319_120634_pack.zip | archive | 3952 | 2026-04-13 | listed only |
| image-20260416-215626.png | image | 146 | 2026-04-16 | listed only |
| image-20260417-161743.png | image | 256 | 2026-04-17 | listed only |
