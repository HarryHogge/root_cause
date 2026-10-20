# VXEP-533: VXE 551 software crashed while trying to create a racetrack orbit in flight

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-08-12
- **Updated:** 2024-09-05
- **Resolved:** 2024-09-05
- **Reporter:** Cameron Chapman
- **Assignee:** David Grosher
- **Creator:** Cameron Chapman
- **Labels:** Edge_Asset
- **Links:** clones VXEP-532 (VXE 551 Significant HLB state of charge drop with fuel cell)
- **Vehicle Tail Number:** 591
- **Vehicle Configuration:** Fuel cell
- **Plan:** - Data review.
- **Incident Type:** Mission Failure/Abort
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

Edge FLOPS asset being operated at live demo/exercise

Aircraft 551 with fuel cell config lost significant HLB percentage, 98% to under 60%, during a short 30-45 min timespan, with no significant changes in environmental factors (wind speed and direction) or flight path. The aircraft also flew for roughly 3 ½ hours before this occurred. Tracked in original issue https://jenaero.atlassian.net/browse/VXEP-532 

Also on this flight, the software crashed while trying to create a racetrack orbit in flight. We had to manually exit the software to reconnect to the aircraft. (created separate incident for this issue )

AAR attached

## Comments (10)

### Greg Fryer, 2024-09-04

@Cameron Chapman You logged this one, does it need to go to SW for data analysis, or do you suspect HW?

### Cameron Chapman, 2024-09-04

@Greg Fryer I logged this one after separating from the linked issue @Pat Wells recorded. It seems like SW analysis is next. Should I just assign those to @David Grosher directly when that seems like the next step? Guessing yes.

### Greg Fryer, 2024-09-04

@Cameron Chapman  Yes, Dave’s still coordinating. Definitely reassign with a detailed comment, since there’s a long tail on these analysis items.

### David Grosher, 2024-09-04

@Pat Wells Can we pull the GCS log from this location (C:\ProgramData\GCS\CrashDumps) to debug the GCS crash.

### Pat Wells, 2024-09-05

@David Grosher the GCS laptop does not have that folder. 
It has C:\ProgramData\GCS but no CrashDumps folder

### David Grosher, 2024-09-05

@Michael Berger @Ted Trowbridge, Was Windows Error Reporting delivered in v6.2.9 or v6.3.4 for the GCS? Are there types of crashes that may not result in a log dump being created?

### Ted Trowbridge, 2024-09-05

@David Grosher @Michael Berger 
Also on this flight, the software crashed while trying to create a racetrack orbit in flight. We had to manually exit the software to reconnect to the aircraft. (created separate incident for this issue )

If the software crashed how/why were they still able to manually exit?  Sounds like the software hung and was forcibly quit - in this case there would be no crash report generated.  The report can sometimes take a few seconds to generate during which it will appear frozen/hung - the user should give it a few seconds if they are able (may not be possible during flight).
I’m sure there are other scenarios or types of crashes where a report is not generated but in my experience WER tends to catch the vast majority of crashes.

### David Grosher, 2024-09-05

@Pat Wells Without a crash dump it will be impossible to recreate the issue on our side. I suggest we close out this task.

### Pat Wells, 2024-09-05

@David Grosher agree.  I will close with no action due to lack of data.

### Pat Wells, 2024-09-05

Data not available to investigate issue,

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V551_240809_121102_pack.zip | archive | 5595 | 2024-08-12 | listed only |
