# VA-609: Review VXE-380 launch abort log, determine cause or if unknown

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-09-27
- **Updated:** 2023-11-09
- **Resolved:** 2023-10-03
- **Reporter:** Greg Fryer
- **Assignee:** Jason Scherer
- **Creator:** Greg Fryer
- **Links:** blocks VXEP-102 (VXE-380 Launch abort); relates to FS2-754 (GNSS Multi-Constellation Support)
- **Sprint:** VXE-2 Greg's Team 9-17
- **Customer:** FBI

## Description

See parent https://jenaero.atlassian.net/browse/VXEP-102 for file to review.

## Comments (10)

### Greg Fryer, 2023-09-27

@Jason Scherer please review, John says you will need time to learn how to read this, that’s ok as it is not our most urgent investigation. Based on behavior, we anticipate (hope) this is a normal abort, and it is just not well-published to the user. If it is more mysterious, please let me know and we will re-plan.

### Jason Scherer, 2023-09-28

@Greg Fryer Preliminary Analysis indicates that this AC had bad LRF and GPS data which caused the AC to RTL shortly after launch.
@John Clark @David Grosher

### Greg Fryer, 2023-09-28

@Jason Scherer Excellent work! Please verify the LRF behavior is normal like we discussed and generate final report from what you have. Great data presentation.

### David Grosher, 2023-09-29

@Jason Scherer A few comments: 

- The version number in the log is a response to a GCS query, please remove the reference to the WDT event on slide 3
- The task hits and func hits is a counter that will be reset when it is read. The data log rate is variable and the rate for all of these events is consistent when accounting for the varying rate of the log. Please remove this from the analysis deck on slide 4.
- LRF is basically useless above 120ft, so this is expected behavior and is almost certainly not the problem. It is really hard to evaluate the LRF on the plot because the range is on the y1-axis, which is scaled to the thousands, but it looks like it starts to get bad around 125ft.
- CN/0 doesn’t get poor until after the RTL is issued so this is unlikely to be the issue.
- However the GPSstat does change around the time that the RTL is issued. I believe this is a status mask, we should look at the different bits and the meaning.

@Greg Fryer FYI

### Jason Scherer, 2023-09-29

Updated Slides Per @David Grosher with some scale changes to make the data more readable. I will dig into the RTL a bit more after the morning standup meetings

### Jason Scherer, 2023-09-29

@Greg Fryer @David Grosher @John Clark 
Analysis complete. Final “preliminary” report attached. I will create the official report and update the ticket status next. Findings summary, GPS outage caused auto RTL.

### Jason Scherer, 2023-09-29

@Greg Fryer Official Report attached

### Greg Fryer, 2023-10-02

@Jason Scherer Last task, please move the investigation file to here: Incident Reports
(We keep them on sharepoint so the whole “duplicates on Jira” doesn’t happen.)
Also, last edits:
1) Delete the workflow page from the PPT.
2) If vehicle switched to RTL, what does it mean that RPIC aborted the launch? e.g. RTL was already happening, did the pilot ALSO do an abort, and if so was that impactful or had no impact.
3) I think the only improvement we should advertise in the investigation is making it more clear when GPS is lost during launch. Since that is SW, that will reach everyone. While we are investigating hardware changes to improve GPS reception, that will be a change that may not go to every aircraft (they may not want the upgrade).

### Greg Fryer, 2023-10-02

(Sorry, had to re-do comments due to “something”)
@Jason Scherer Last task, please move the investigation file to here: Incident Reports
(We keep them on sharepoint so the whole “duplicates on Jira” doesn’t happen.)
Also, last edits:
- I don’t see a response to  ‘s comment - he said the RTL happened after GPS fault. or are there TWO RTLs (see my bullet #2) where it RTL’d due to GPS, then a 2nd RTL due to the pilot hitting an abort?
- Delete the workflow page from the PPT.
- If vehicle switched to RTL, what does it mean that RPIC aborted the launch? e.g. RTL was already happening, did the pilot ALSO do an abort, and if so was that impactful or had no impact.
- I think the only improvement we should advertise in the investigation is making it more clear when GPS is lost during launch. Since that is SW, that will reach everyone. While we are investigating hardware changes to improve GPS reception, that will be a change that may not go to every aircraft (they may not want the upgrade).

Given 0 and 2, I think you need to add a timeline page. Just a bar on a blank sheet that shows time from launch, and when events (both impactful and not) happened. See me if that’s confusing.

### Jason Scherer, 2023-10-02

@Greg Fryer Updated the slides per your request. The launch abort from the RPIC occurred well after the AC was in a controlled descent and already in a launch abort state, so it did not have any affect other than to log the message. I added a slide with the full flight timeline with indicators for RTL and the GCS launch abort. Dave’s comment about the GPS hit not occurring during the RTL was actually incorrect, but I think it was my chart with bad y-axis scales that threw him off. I’m still getting the hang of Liam’s flight data analysis tool. I went over the GPS data again with him and he confirmed that it was the GPS that caused the RTL.
Let me know if you are happy with this report and I will post it to SharePoint.

## Attachments (0)
