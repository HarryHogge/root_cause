# VXEP-608: VXE 336 uncommanded aborted launch

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed, but added to Bermuda Triangle List
- **Resolution:** Cannot Reproduce
- **Priority:** Highest
- **Created:** 2024-09-05
- **Updated:** 2026-03-02
- **Resolved:** 2024-11-07
- **Reporter:** Alexander Alan Arnold
- **Assignee:** David Grosher
- **Creator:** Alexander Alan Arnold
- **Labels:** USASOC, Weekly-incident-tracker
- **Links:** relates to FS2-2332 (Investigate AP Link Loss issues on FW AP); relates to VXEP-900 (VXE 337 uncommanded aborted launches)
- **Customer:** USASOC
- **Vehicle Tail Number:** 336
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

During Takeoff sequence aircraft flew approximately 10-15 ft in the air and then aborted the launch without operator commanding abort. Operator also states that no warning was generated to explain the abort. 

Operator says that they completed launch wizard with no issues and saw no anomalies during preflight procedures.
*AAR Attached

## Comments (21)

### Greg Fryer, 2024-09-05

@David Grosher Another AAR read, likely just digging out the error.
@Alexander Alan Arnold FYI, we are tracking and working the need to improve the error messaging (would hopefully cut down on incident reports, if nothing else!). Unfortunately, the AC and Ground Station don’t have a good “message” system, so we’re having to create that first. (We = SW team, not me. 🙂 )

### David Grosher, 2024-09-05

@Jason Scherer This looks like another launch abort for a lost link. Can you look into it. 

[15:30:51.895 1004.895] ap dbg: vt lost link during lch, aborting
[15:30:51.897 1004.897] ap dbg: vt lch abort triggered
[15:30:51.898 1004.898] ap dbg: vt status: 10423

### Alexander Alan Arnold, 2024-09-09

@David Grosher 
I have attached another AAR from a different aircraft where the customer was experiencing the same issue at the same flight location. 

The original file he sent me was about 54 MB so I dug through and tried to pick out what would be needed from the date of the incident please let me know if you need anything from me. I have all the original files he sent us earlier today.

### Pat Wells, 2024-09-12

@David Grosher @Jason Scherer 
Have we gleened anything additional from the two sets of data?

@Alexander Alan Arnold @Michael Mohr FYSA

### Jason Scherer, 2024-09-17

@Pat Wells @Michael Mohr @David Grosher Getting pulled in a few directions here, but initial analysis shows that the fixed wing isn’t receiving GCS messages for up to 5 seconds during launch. This is what leads to the launch abort. Based on customer descriptions it doesn’t seem like it’s tied to a single vehicle or config. I’m in the process of investigating & attempting to recreate the issue on a HIL simulation setup at SLO. If we can get an AAR of one of the successful flights. I could compare data between a good/bad flight and see if anything jumps out at me quicker.

### Pat Wells, 2024-09-18

@Jason Scherer are you seeing the same on both 336 & 337?  In terms of FWAP not receiving GCS messages for up to 5 seconds.

### Jason Scherer, 2024-09-18

@Pat Wells Sorry for the confusion. V336 has the confirmed link timeout launch abort. The log collection for V337 is missing critical logs to confirm that cause. V337 does have the motor profile of a launch abort. I would need the XCEVLOG.txt file from that vehicle or an FDR with data (the one in the log folder only has two rows of data).

### Michael Mohr, 2024-09-18

@Jason Scherer Uploaded the XCEVLOG.txt file that contains both Sept 3rd and 5th that they tried to fly A/C 337.

### Pat Wells, 2024-09-25

Added additional AAR from customer for tracking and historical purposes.
Customer downgraded software to 6.1.2 on their own.  
PM has been notified and will notify customer program office that this is not acceptable. 
AAR-336_2.zip

### Pat Wells, 2024-09-26

@David Grosher operator reported another uncommanded aborted launch today.  AAR file attached. 
See my comment from yesterday.  Operator has rolled back software to 6.1.2.  That is the case in the AAR today as well.   AAR_337_2.zip
@Michael Mohr @Alexander Alan Arnold

### Pat Wells, 2024-09-27

@Jason Scherer do we believe that this issue is due to the issue described in https://jenaero.atlassian.net/browse/FS2-2332 linked issue?

### Jason Scherer, 2024-09-27

@Pat Wells Yes this is the current belief.

### Pat Wells, 2024-09-27

@Jason Scherer is there any risk to the aircraft?  Want to make sure we are advising the operator correctly.
What are the next steps here in terms of the operator not being able to launch.  He is seeing it on two aircraft. 

@Michael Mohr @Alexander Alan Arnold FYSA

### Jason Scherer, 2024-09-27

@Pat Wells @David Grosher I looked at the last AAR posted and the launch abort this time is due to a gyro fault on the VTOL processor. Previously, it was a link drop abort.
[embedded: image-20240927-214348.png]

### Pat Wells, 2024-09-27

@Jason Scherer thank you for looking at that.  The operator has rolled their software back to GCS version 6.1.2 and best I can tell he rolled back FW AP, XCOMM, and VTOL AP.  
Not sure if we even worry about the gyro fault due to old software being used. 
I suspect this operator has some training deficiences.

### Jason Scherer, 2024-09-27

@Pat Wells noted on the second AAR. I took a look at the XCEVLOG log provided by @Michael Mohr. It includes two launch aborts for V337. The first launch abort is due to low climb rate and the second launch abort is due to the link loss. The low climb rate is interesting because it typically means the vtol is not working optimally. If we had the XComm datalog for that flight (xcl00096.csv) I could dig into it a bit more.

### Pat Wells, 2024-10-01

@Michael Mohr please locate the xcomm datalog mentioned in the previous comment. You may have to contact customer and ask them to manually FTP the log from the aircraft.

### Jason Scherer, 2024-10-01

@Pat Wells I spoke with @David Grosher on how to proceed with this incident.
- We would like to confirm that the correct and compatible software has been restored to all subsystems of the two vehicles. This can be accomplished by generating new AARs on the ground for both V336 and V337. This will give us a baseline of data to proceed.
- If the software versions look correct, then we would like to have the customer attempt the flights again with the confirmed software versions.
- If the launch abort issue persists, then we will need complete AARs for each flight to complete the analysis. Additionally, if some flights don’t abort it would be beneficial to get the AARs from those flights as well for comparison.

### Pat Wells, 2024-10-01

@Michael Mohr see below from Jason for next steps.

### Pat Wells, 2024-11-07

@David Grosher receommend we close this with no action. Last report from customer is that aircraft is functioning with no issues.

### David Grosher, 2024-11-07

Aircraft are operating fine.

## Attachments (6)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_336.zip | archive | 1770 | 2024-09-05 | listed only |
| VXE 337 (2).zip | archive | 1458 | 2024-09-09 | listed only |
| [XCEVLOG.TXT](attachments/23233_XCEVLOG.TXT.md) | text | 341 | 2024-09-18 | converted |
| AAR_336_2.zip | archive | 2112 | 2024-09-25 | listed only |
| AAR_337_2.zip | archive | 2459 | 2024-09-26 | listed only |
| image-20240927-214348.png | image | 8 | 2024-09-27 | listed only |
