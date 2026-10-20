# VXEP-784: VXE 637 aircraft altitude reporting incorrectly

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-11-21
- **Updated:** 2026-03-02
- **Resolved:** 2025-03-17
- **Reporter:** Pat Wells
- **Assignee:** David Grosher
- **Creator:** Pat Wells
- **Labels:** MOLSON
- **Links:** is caused by GCSS-383 (Incorrect MSL altitudes reported in the UI when operating without DTED)
- **Customer:** MOLSON
- **Vehicle Tail Number:** 637
- **Corrective Action:** Load DTED on to customer Laptop.
- **Root Cause:** No DTED on the GCS
- **Incident Type:** Near Miss
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

Information received from operator:


- They conducted a handover mission which seemingly worked but they couldn't pull the entire mission because of error message "not enough endurance"
- Completed quick mission on different GCS
- Aircraft state panel indicated the av was 500' lower than the flight instruments panel
- The plane orbited for 20mins but wouldn't descend
- They programed IP1 to 200 ft. GCS thought it was 600'
- Then initiated VTOL descent. Plane landed without issues

AAR’s attached

## Comments (20)

### Greg Fryer, 2024-11-21

@David Grosher @Scott Whitney Logs that need review for starters.

### Ted Trowbridge, 2024-11-22

@David Grosher @Pat Wells 
The logs indicate that the system was being operated without elevation (DTED) coverage for the launch area.  During launch the vehicle is  calibrated with elevation at its location to use as a reference point for altitude calculations.  The elevation for the launch area in this flight should have been 515ft MSL but due to missing DTED 0ft MSL was used instead.  This may explain the 500ft observed delta between panels.
I have reproduced the issue in the HIL and found that certain areas of the UI display an incorrect MSL value that would cause confusion.  I’ve filed a defect for the GCS: https://jenaero.atlassian.net/browse/GCSS-383 
Further questions:
- Can we confirm with the customer that they did not have DTED coverage for the launch area?
- Can we ask them exactly which panels and displays were showing the discrepancy in altitude?

### Pat Wells, 2024-11-22

@Ted Trowbridge  I’ve reached out to the customer for clarification on your questions.

### Pat Wells, 2024-11-22

@Ted Trowbridge Response from customer:
”The aircraft status bar read 500ft lower than the instrument panel.”

### Ted Trowbridge, 2024-11-22

@Pat Wells 
”The aircraft status bar read 500ft lower than the instrument panel.”

That is consistent with my findings about not having DTED.  Did we get a response back confirming the lack of DTED data for the launch location?

### Pat Wells, 2024-11-22

@Ted Trowbridge they’re checking into the DTED on Monday.

### Pat Wells, 2024-11-26

@Ted Trowbridge confirmed with operator.  There was not any DTED data loaded on the GCS laptop.
Ready for next steps.

### Ted Trowbridge, 2024-11-26

@Pat Wells this is a known issue when flying without DTED loaded.  I have filed https://jenaero.atlassian.net/browse/GCSS-383 to address the issue.
I would advise them to load DTED for the launch area to workaround this issue, or to ignore the conflicting MSL altitude reported in the status bar.
@David Grosher do you want to do a full audit of everywhere in the GCS MSL altitude is displayed and whether is has this issue?

### David Grosher, 2024-11-26

@Ted Trowbridge @Pat Wells I believe that all of our GCS systems that we send out contain DTED data for the full world. So, we should understand why the DTED is not on that machine, @Wesley Reynolds @Jo Brown can you confirm that we sent it to Molson? Having said that I think the source of this data is the STRM data which I believe has voids in it, but I think this is probably less likely.

### Jo Brown, 2024-11-26

@Pat Wells I have a few questions to try and get to the root issue. How was the missing DTED data checked? There should be a DTED folder inside My GCS. Is that folder there? Is it empty, missing? If it’s there, can you have the operator right click on the DTED folder, then properties, and relay the “Size on disk” section?
@David Grosher There is almost no possibility that the DTED folders were missing when the laptop was shipped. Molson would have received GCS laptops in our standard configuration, to my understanding. That configuration has world DTED data loaded.
I’d only have guesses as to what could have happened, and those would be dependant on whether the folder is there or not.

### Pat Wells, 2024-11-26

@Jo Brown I’ll reach out to customer on your questions.

### Ted Trowbridge, 2024-11-26

@Jo Brown @David Grosher 
Based on location data from the logs I’m certain the area is covered by DTED L2 and is not a void cell - the elevation is 515ft.  I can provide you the exact tile if needed.

### Pat Wells, 2024-11-27

@Jo Brown here’s the feedback I received from your questions:

"I checked by cross referencing the DTED files in the 'my GCS' folder from the GCS 1 laptop, and the other laptop we were using.
The laptop we used clearly had files missing in it.
The DTED folder is there, but there were only three folders. While the original GCS had a ton more folders within it."

### Jo Brown, 2024-11-27

@Pat Wells Thank you, that helps! 
Just to rule out one more thing, can you have them go to OS (C:) > Users  > Public > Public Documents > My GCS > DTED, and confirm that the files are missing from that folder too? It should be the same folder, so they probably will be missing.

@David Grosher The files/folders described are what we include in the installer source. You can find an example at \\condor\software\GCS\release\6.3.4\Installer Source\My GCS\DTED. 
This points to the My GCS folder, or at least its contents, being deleted, and then repopulated by a GCS install. 
I am unsure how that happened, but I know that Molson has been uninstalling and installing different GCS versions. Is it possible that one of the installers accidentally deleted the My GCS folder as part of the uninstall process? User error is possible here, but it would be really strange to navigate to Public Documents and delete the My GCS folder there. I could not reproduce the error with the 6.3.4 installer, but I did not try any Molson releases.

### Pat Wells, 2024-11-27

@Jo Brown confirmed. The files are missing from that folder too.

### Alexander Alan Arnold, 2025-01-10

@David Grosher Is the missing DTED the root cause of this issue and if so can we move this to D5/6? Possibly 8 saying this is operator error due to not having proper DTED on GCS?

### David Grosher, 2025-01-10

@Jo Brown Can we try the same test with the v6.2.9 installer (Upgrade from 6.1.2 with DTED to v6.2.9) to see if the files were deleted? That update would have been made available about the time their birds were being delivered. Just a note, they don’t have a special build yet for the Maritime operations, so we can rule that out. 
@Alexander Alan Arnold If we rule out that other installer then we can probably close this ticket as Burmuda Triangle, with a likely operator error  but no conclusive proof. Regardless of the cause, it would be prudent to check the other GCS systems they have to ensure it wasn’t also done there.

### Alexander Alan Arnold, 2025-01-10

@David Grosher Understood. We will ask the PM to communicate that they check all GCS systems. 

@Pat Wells FYSA

### Alexander Alan Arnold, 2025-02-25

Are we good with calling this a Bermuda Triangle/Operator error? @David Grosher @Jo Brown If so I will close it out.

### David Grosher, 2025-02-25

@Alexander Alan Arnold I think we know the root cause of the observed issue, but we don’t know how the customer received a GCS with no DTED. I think that falls more into a Quality Issue.  If this is a one off then perhaps we close it, if it has happened more than once then I think this should get kicked over to QA. I’ll defer to @Pat Wells on how best to handle this one.

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V637_241113_114115_pack.zip | archive | 3485 | 2024-11-21 | listed only |
| T95_V637_241114_111024_pack.zip | archive | 2957 | 2024-11-21 | listed only |
