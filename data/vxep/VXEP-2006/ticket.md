# VXEP-2006: VXE 1013 Glide landed while PLZ was selected

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** High
- **Created:** 2026-09-24
- **Updated:** 2026-10-13
- **Resolved:** 2026-10-13
- **Reporter:** Jackson Riley Curvin
- **Assignee:** Ted Trowbridge
- **Creator:** Jackson Riley Curvin
- **Labels:** RCCA, Weekly-incident-tracker
- **Links:** relates to VXEP-1988 (VXE 1014 Inccorect altitudes entered during LW led to crash)
- **Customer:** ARMY_Cyber
- **Vehicle Tail Number:** VXE 1013
- **Vehicle Configuration:** Blk 30 ADV NAV, main battery, E-95
- **Corrective Action:** Flew aircraft again and performed as expected.
- **Problem Type:** Discovered Issue
- **Root Cause:** Operator Error
- **Incident Type:** Near Miss
- **Severity:** 1 - Flight Critical
- **Components (EA Aircraft):** Aircraft, full assembly
- **Executive Summary:** appears operator landed with a tail wind causing the drop in altitude.

## Description

After relaying findings from 1014 issue involving plz alttitude changing during mission planning, operator attempted to fly again stating “I was supervising the flight and confirmed all the connections on the stalker. I also watched the mission planning. I made specific note the altitudes entered for the landing pattern were 400ft AGL and 200ft AGL, straight in landing, centered on vehicle. I specified that my pilot set a straight in landing as it made the entire landing pattern occur over a flight line where I could watch it the whole time.” Aircraft appeared to have the same behavior from the 1014 incident.

## Comments (19)

### Jackson Riley Curvin, 2026-09-24

@Ted Trowbridge @David Grosher  army cyber had a similar incident with their other aircraft and said that they verified the altitude was set correct.

### Ted Trowbridge, 2026-09-24

@Jackson Riley Curvin let me know when we have AARs for this.  If it was on the native app please ensure they grabbed frontend logs.

### Jackson Riley Curvin, 2026-09-24

@Ted Trowbridge  should be in now.

### Ted Trowbridge, 2026-09-24

@Jackson Riley Curvin I can confirm that all landing patterns were set correctly with a pattern altitude of 200ft

### David Grosher, 2026-09-24

@Everett Werner Can you take a look at the altitude commands as the vehicle sequenced through the pattern to see if they were the expected 200ft. @Eric Brewer Perhaps, the other error sources here are the source of the problem, can you take a look at the actual problematic behavior and the altitude error as the vehicle approached the pattern.

### Everett Werner, 2026-09-24

According to this AAR it looks like the vehicle transitioned correctly and the vtol took over fully. The vehicle was then udrived in attitude mode half a mile back to the landing pad. Is this the correct aar? I dont see anything that looks particularly similar to the 1014 flight. @Jackson Riley Curvin 



[embedded image-20260924-213907.png]
A straight in landing was setup and uploaded but then a left turn landing plan at 200ft was uploaded afterwards. I do see a discrepancy between vtol altitude setpoint and fixed wing altitude setpoint (200ft vs 300ft) during the transition however.

### Everett Werner, 2026-09-24

@Jackson Riley Curvin Is this AAR the correct one?

### Ted Trowbridge, 2026-09-25

@Everett Werner @Eric Brewer @David Grosher 
Here is a recording of the flight replayed through OGCS at 10x speed.  Around 2:40 it looks like the vehicle is nudged aggressively.
[embedded Screen Recording 2026-09-25 072348.mp4]
Note: All the locations are scrambled in recordings so relative headings/bearings are incorrect.  This is corrected in a later version of OGCS.

### Eric Brewer, 2026-09-25

@Ted Trowbridge thanks - this is super helpful to visualize. This matches what I saw in the autopilot logs.  The vehicle transitions to VTOL normally and tracks to the commanded location, what shows as ‘LZ’ on the screen recording.  During the descent, the operators take over in manual nudge and move the airplane toward “AP” on the map.  Is it possible there was a misunderstanding of the landing definition?@Everett Werner @Jackson Riley Curvin @David Grosher 

[embedded image-20260925-143400.png]

### Alexander Alan Arnold, 2026-09-28

@Everett Werner @Eric Brewer @Ted Trowbridge apologies jack and I were out Friday, based on discussions with the customer this is the AAR they generated after recovering the vehicle. Date of incident was September 22nd. I can double check with them again.

### Everett Werner, 2026-09-28

@Alexander Alan Arnold That would be great thank you. If they are sure they experienced a glide landing I would recommend an FTP data collection. The AAR folder does not have any other relevant cached files in it.

### Alexander Alan Arnold, 2026-09-29

@Everett Werner 22SEP2026 ~1100, I did a check flight with SSG Ramos. He attended the two-week training in HSV alongside myself back in July. I wanted to verify that he was still able to safely operate the Stalker. WO1 Graves was also there and likewise attended the training. Nothing significant noted during assembly. I verified all connections and that all thumbscrews were tightened. Weight and balance were not conducted as I had done that previously and we were not flying a new configuration. WO1 Graves acted as the ground crew during preflight checks while I watched SSG Ramos on the GCS. I checked all of his mission planning and made sure he got through that launch wizard correctly. I made two corrections on his landing pattern. I specified that he use a straight in landing along the flight line we were operating on and that he set a left turn emergency landing pattern at the same location. I also made special note that his altitudes on the primary landing pattern were 400ft and 200 ft AGL. He specifically highlighted the entire block to delete the default 300ft and typed 200ft. Sorry if that’s too much detail. Winds were calm at around 7-9mph out of the northeast. Nothing of note during takeoff or flight operations. During landing the aircraft looked stable and made it to IP4 before suddenly pitching down and dropping to around 50ft AGL before pulling up and transitioning to hover. All four motors were operating. The aircraft was still around 300ft short of its PLZ. WO1 Graves directed SSG Ramos to nudge the aircraft to the left (west) where it would contact a dirt and grass area rather than gravel. It was still attempting to move forward to its PLZ but did not have the altitude and contacted the ground. Once it did I called to cut and safe the motors before approaching. Once the aircraft was safe I picked it up and carried it back to the PLZ where I put it in its cradle, did an initial inspection and downloaded the flight logs.

this is the detailed operator write up which seems to lean towards operators misunderstanding the landing logic? 
initially it was reported as “same behavior” from their first incident, but this one seems like they didn't fully understand where they told it to land?

### Everett Werner, 2026-09-29

@Alexander Alan Arnold Thanks for the writeup, this does not match what I see in the data. The pitch down and drop to 50ft agl sounds like something worth investigating but this flight looks like a nominal transition and then a landing nudge back to the launch point.

### Jackson Riley Curvin, 2026-10-12

@Ted Trowbridge @Everett Werner  i think we can closer this ticket I flew this aircraft this past week with no issues. Would landing with a tailwind cause the aircraft to drop?

### Everett Werner, 2026-10-12

@Jackson Riley Curvin Yes it is not recommended to land with a tailwind as far as I am aware? I could be wrong about that though.

### Jackson Riley Curvin, 2026-10-13

Flew aircraft on 10/6/2026 and performed as expected.

### Cody Smisek, 2026-10-13

@Everett Werner The operators manual does not limit wind direction. The only limit for launch and landing is max wind speed.

### Everett Werner, 2026-10-13

@Cody Smisek We dont specifically limit it but I was under the impression SOP was to land with wind at head. Performance will be worse with a tailwind landing. @Jackson Riley Curvin  I doubt that the large altitude loss being reported was due to a tail wind unless it was extreme, the data provided does not show the reported behavior though so I cannot say with certainty.

### Cody Smisek, 2026-10-13

@Everett Werner Limitations are limitations. If we do not specifically limit it, than nothing beyond that matters. 
Yes, it is common practice to attempt to avoid tailwind landings. But again, our published operating limitations do not restrict it.

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_V1013_B30N_20260922T154308Z_Ramos_Test.zip | archive | 19162 | 2026-09-24 | listed only |
| image-20260924-213907.png | image | 247 | 2026-09-24 | listed only |
| Screen Recording 2026-09-25 072348.mp4 | video | 194402 | 2026-09-25 | listed only |
| image-20260925-143400.png | image | 985 | 2026-09-25 | listed only |
