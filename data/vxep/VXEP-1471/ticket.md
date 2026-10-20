# VXEP-1471: Fuel Cell stopped during flight

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-08-13
- **Updated:** 2026-08-11
- **Resolved:** 2026-08-11
- **Reporter:** Drew Hildreth
- **Assignee:** Craig Burton
- **Creator:** Drew Hildreth
- **Labels:** GS_Closed, Software
- **Links:** relates to MS-1276 (VSM:  Fuel Cell should remain On after Land Immediately is commanded)
- **Customer:** TIQUILA
- **Vehicle Tail Number:** VXE 732
- **Plan:** Updated / added corrective actions on 12/31/2025, need implemented and verified. Then close ticket.
- **Incident Type:** Mission Failure/Abort
- **Severity:** 4 - Annoyance

## Description

ISSUE IS FROM AUGUST 2025
During a short fuel cell flight today, while in Manual Mode, I commanded Land Now (in VCSi), then took Control in OGCS and enabled Position Nudge.  During the descent, I received “Vehicle has low energy and is executing an automatic return to base”.  The Land Now descent proceeded as expected.  After landing, it was observed that the fuel cell was Off.  The tank was measured and had 100 grams of propane remaining.  We’re planning to use this specific fuel cell for high density altitude testing next week and want to know why it stopped, and if it’s at risk of stopping on us next week.
 
Preface: The fuel cell failed to start twice prior to successfully starting.  The cause was determined to be a stuck manifold pressure regulator which was remedied.  After setting the pressure regulator to 12 psi, the fuel cell started normally, but stopped at some point during the flight.

## Corrective Action

@Craig Burton to determine if VSM update will be incorporated. 
@Josh Burrell  Update user manuals / supplements if required once Craig makes / doesn’t make changes.

## Issue Status

Logs indicate a fuel cell that is operating nominally. Fuel cell shutoff during land immediately as commanded by VSM (unexpected but as designed).

## Root Cause

During VTOL land immediately, VSM commanded fuel cell shut off (as designed). The intended design was to follow legacy GCS logic, however it was discovered legacy GCS had similar logic commented out.

## Comments (19)

### Jackson Riley Curvin, 2025-12-30

@Ted Trowbridge can you look at this?

### Cody Smisek, 2025-12-31

[embedded image-20251231-150925.png]
[embedded image-20251231-151647.png]

@Jackson Riley Curvin I’m not seeing what you’re seeing with regards to launching. Seems it was fully producing power prior and after launch. 
Also not seeing anything obvious about fuel starvation / regulator issues in the AAR. 
Somewhat concerning is the practice of running the battery all the way down during startup and then running forward motor when the HLB was <20%. 
I’m not familiar with any specific OGCS / VCSI / MCM logs. So you’ll need SW support to help determine if the command came from OGCS (or if it’s even possible to know). I don’t think there’s a way to determine that from xcomm event log, all xcomm knows is that it received the command.

### Cody Smisek, 2025-12-31

[embedded image-20251231-154616.png]

### Cody Smisek, 2025-12-31

@Craig Burton (tagging you, not sure if you’re correct POC for this comment) something that added confusion for @Jackson Riley Curvin and @Sean Wendling 
looks like our states in cucs logs don’t match the states of what the fuel cell is reporting. I see states 1-4 in cucs logs, and the fuel cell ICD / fuel cell reports states 1-6. 
Was there a specific reason for the difference?

### Craig Burton, 2025-12-31

@Cody Smisek The “Land Immediately” workflow triggers this behavior, just like with Jennings GCS.

### Cody Smisek, 2025-12-31

@Craig Burton oh, I was not aware of that. That’s no good.

### Craig Burton, 2025-12-31

@Cody Smisek I can’t remember the exact timeline, but LM had proposed an even smaller number of states for the original STANAG message.  We expanded the number of states from 3 to 5 (4 if we don’t count Disconnected).  Changing this to match the FC ICD would either take cooperation with LM, or we’d have to send an additional message that only we’d use.  This is where the mapping from AP to STANAG happens:

```
FuelCellStatus JaiFuelCellStackStateToStanagState(int8_t stackState)
{
    FuelCellStatus stanagFuelCellStatus = FuelCellStatus::Invalid;

    // We might want to expand the number of enumerations in the VCSi ICD.  These mappings aren't great.  See MS-212.
    switch (static_cast<ApFuelCellState>(stackState)) 
    {
        case ApFuelCellState::Disconnected:
            stanagFuelCellStatus = FuelCellStatus::Disconnected;
            break;
        case ApFuelCellState::Off:
            stanagFuelCellStatus = FuelCellStatus::Off;
            break;
        case ApFuelCellState::Init:
        case ApFuelCellState::Ignition:
        case ApFuelCellState::Warmup:
            stanagFuelCellStatus = FuelCellStatus::Starting;
            break;
        case ApFuelCellState::Operate:
        case ApFuelCellState::Hotswap:
            stanagFuelCellStatus = FuelCellStatus::Running;
            break;
        case ApFuelCellState::Cooldown:
        case ApFuelCellState::Purge:
            stanagFuelCellStatus = FuelCellStatus::Stopping;
            break;
    }

    return stanagFuelCellStatus;
}
```

### Cody Smisek, 2025-12-31

@Craig Burton understood, thanks for the context

### Cody Smisek, 2025-12-31

@Scott Whitney I think engineering should confirm that this is the desired logic of land immediately with fuel cell. I don’t really understand the reasoning for it. Craig has explained that for OGCS, it was implemented as that was what legacy GCS was doing (which makes sense given likely lack of requirements).

### Josh Burrell, 2026-01-02

@Mark Spence @Drew Cunnien We need to look at the corrective action and make sure we capture this in the new FC Rev before we release it.

### Cody Smisek, 2026-01-05

@Josh Burrell We are going to confirm in legacy GCS that this is actually what happens. @Anthony Hansen plans to complete a flight tomorrow with fuel cell and perform land immediately in VTOL and glide.

### Josh Burrell, 2026-01-05

@Cody Smisek Sounds good! We’ll wait on doing anything until we hear the outcome of the flight.

### Cody Smisek, 2026-01-05

@Craig Burton We just tested this on a HIL using legacy GCS (advanced Nav 30 type 115) and did not observe this behavior (no observed commands from GCS to aircraft to shut down fuel cell). Brandon is pulling AAR and I can provide if desired. Additionally, HSV flight ops is going to check with an actual aircraft tomorrow.

### Craig Burton, 2026-01-05

@Cody Smisek Apologies, but no need to test with an actual vehicle.  I am not sure how it happened, but I apparently missed the fact that in Jennings, those lines are commented out.  So this is a bug in VSM, if we want the fuel cell to remain on during Land Immediately:
[embedded image-20260106-014554.png]
FYSA @Ted Trowbridge @Scott Whitney @David Grosher

### Craig Burton, 2026-01-05

Per the comment above, this is a VSM issue:  https://jenaero.atlassian.net/browse/VXEP-1471?focusedCommentId=68847 
Issue created for bugfix:  https://jenaero.atlassian.net/browse/MS-1276

### Cody Smisek, 2026-01-06

@Craig Burton thanks for taking a look. Talked with Kurt yesterday about this, and I think that is some Gordon leftovers from testing and landing in the grass and not wanting to light up the fields they were in.
I think if I put my customer hat on, I want that fuel cell on during a landing. And given that we have been making OGCS function the same as legacy, it seems like that’s another reason to change it back as well.

### Ted Trowbridge, 2026-01-06

@Jackson Riley Curvin I think @Craig Burton  has investigated and determined a root cause and fix for a future release, see his comments.

### Craig Burton, 2026-02-03

This has been fixed and merged into the VSM’s develop branch that will become a part of OGCS 1.4.
FYSA @Drew Hildreth @Cody Smisek

### Pat Wells, 2026-08-11

CA complete

## Attachments (9)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_V732_20250813T000552Z.zip | archive | 22906 | 2025-08-13 | listed only |
| VCSi Data for Fuel Cell Flight.zip | archive | 3913 | 2025-08-13 | listed only |
| image (2).png | image | 151 | 2025-12-30 | listed only |
| image (3) (66aae245-9f5a-4424-9463-aa41da10367b).png | image | 120 | 2025-12-30 | listed only |
| image (3).png | image | 120 | 2025-12-30 | listed only |
| image-20251231-150925.png | image | 153 | 2025-12-31 | listed only |
| image-20251231-151647.png | image | 123 | 2025-12-31 | listed only |
| image-20251231-154616.png | image | 5 | 2025-12-31 | listed only |
| image-20260106-014554.png | image | 99 | 2026-01-05 | listed only |
