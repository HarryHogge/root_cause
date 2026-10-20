# VXEP-275: VXE-406 crash on landing at AEWE (Edge asset)

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-02-14
- **Updated:** 2024-08-23
- **Resolved:** 2024-08-23
- **Reporter:** Pat Wells
- **Assignee:** David Grosher
- **Creator:** Pat Wells
- **Labels:** Bad_Mag_Data, Edge_Asset, Weekly-incident-tracker
- **Links:** relates to RMA-217 (VXE-406 240212 Edge Asset); relates to VXEP-263 (VXE-604 crash during SCO/ Flight test)
- **Impact:** Significant / Large
- **Customer:** Edge_Asset
- **Vehicle Tail Number:** 406
- **Vehicle Configuration:** Replacement 406 was delivered in March 2023
- **Severity:** 1 - Flight Critical

## Description

From Edge AEWE flight ops team 2/8/2024:
Final flight crashed on landing; was in VTOL mode coming down then the team could not see what happened in the dark. It ended up at across the runway (see last pic)…appeared to be trying to reenter the pattern (see pic). Team will pull the FTR manually tomorrow; gimbal looks okay…full function check will be done tomorrow as well.
AAR/FDR/Pictures attached
Sharepoint Repository: VXE-406 crash on landing at AEWE (Edge asset)
Working Investigation Report: VXE-406 crash on landing at AEWE (Edge asset) - Report.pptx

## Plan

- https://jenaero.atlassian.net/browse/VXEP-276
- https://jenaero.atlassian.net/browse/VXEP-277
- https://jenaero.atlassian.net/browse/VXEP-278 
- Manually overload CPU and see if that leads to bad mag data. Has this been done?  Have we proven that CPU overload leads to mag data going bad/switching to the AP one?
- Does the imusrc flag change in that case?
- I think we should add a fishbone to this and the linked investigation.
- Consider testing magnetometer with induced current through wing, but this seems unlikely to cause a failure.

## Issue Status

Open.
Hypothesis: CPU load is often an instance of a task locking up, which leads to corrupting data on the mag. 
Dave mentioned the external mag was being used the entire time for both events. 
- @Ben Triplett @David Grosher @Gregory Nichols @Artis Bertulis SCO team reports that the AEWE team did not have any VXE webpages open (just Silvus), and did not activate burst mode. 
- This seems to indicate that the guidance we provided does not cover all potential causes of this issue. The guidance was meant to reduce risk. It was not ever considered a work around or containment.
- The system was operating with and additional radio on the hood. @Cody Smisek can you link to that project or list applicable documents?
- It is likely there was a low priority task hung in the system. But I can’t confirm this with the data that we have.
- The external Mag was being used. It is unclear what led to the bad data, but the leading ideas are EMI given the I2C bus runs along the voltage line to the boom or the SW corrupting the data (the mechanism that could cause this is unclear at the moment, but given the strong correlation between CPU loading and bad mag data we are chasing it down)
- Considering the large number of aircraft and other systems operating at AEWE, it is possible that the aircraft was operating in a more contested EM environment than normal.
- Center Wing powered up successfully and received data from external Magnetometer on 2/20. No anomalies. Wiggling, pulling, etc. the Magnetometer harness does not affect stability of the live data.

## Root Cause

Artis to work on interim internal guidance. If aircraft seems to be veering off due to bad mag data, switch to attitude mode (will ignore bad data) and nudge into position. This might not work if CPU is locked up, but worth a shot.

## Comments (15)

### Pat Wells, 2024-02-14

@David Grosher FYSA

### Pat Wells, 2024-02-14

@Sean Odell please alert the team when the aircraft has arrived back at SLO.

### Connor Peebles, 2024-02-14

converted to an Incident Ticket

### Connor Peebles, 2024-02-14

Dropped incident priority from Highest to High based on priorities of other engineering projects

### David Grosher, 2024-02-16

@Ben Triplett Can you look into this incident? Data is attached. @Jason Scherer did a quick first pass, you may want to touch base with him.

### Ben Triplett, 2024-02-16

Cursory look at the data indicates same issue as VXE604: 
[VXEP-263] VXE-604 crash during SCO/ Flight test - Jira (atlassian.net)
Writing up the PPT now to show the details.

### Cameron Chapman, 2024-02-19

@Ben Triplett @David Grosher @Gregory Nichols @Artis Bertulis SCO team reports that the AEWE team did not have any VXE webpages open (just Silvus), and did not activate burst mode. This seems to indicate that the guidance we provided does not cover all potential causes of this issue. 
- Do you know what else could have caused the CPU usage to increase and cause this issue.
- Is there anything to prove which magnetometer was being used when? (do we know the increased mag noise was due to switching magnetometers, or could it have been using the internal before that point and then only experienced interference as the VTOL current ramped up?)

### David Grosher, 2024-02-19

@Cameron Chapman The guidance was meant to reduce risk. It was not ever considered a work around or containment. 
- It is likely there was a low priority task hung in the system. But I can’t confirm this with the data that we have.
- The external Mag was being used. It is unclear what led to the bad data, but the leading ideas are EMI given the I2C bus runs along the voltage line to the boom or the SW corrupting the data (the mechanism that could cause this is unclear at the moment, but given the strong correlation between CPU loading and bad mag data we are chasing it down)

### Matt Philley, 2024-02-20

@David Grosher  I agree with @Cameron Chapman 
Based on the guidance about the burst data being the cause we lifted a flight test hold and shipping hold on VXE30, so if we had another crash with the same symptoms and the burst data was not the cause that seems like we need to re-evaluate our decision on that…
@Marc Richardson FYSA

### Cameron Chapman, 2024-02-20

@David Grosher @Ben Triplett considering the two recent mishaps suspected due to processor overloading do you think that a recent change could be exacerbating this issue, or are they more likely unlucky coincidences due to separate causes (Ex: 1-heavy webpage and burst mode usage, 2-AEWE EMI/EMI, etc)? We are wondering if any containment should be triggered.

### David Grosher, 2024-02-20

@Matt Philley I think there may have been a miscommunication regarding the rationale of the lifting of the shipping hold. We did not lift the flight test and shipping hold based on the guidance about burst data. In my discussions with @Greg Fryer we decided the hold was not required because the NCRs related to 604 and 606 were not related and that we didn’t believe that there was a systemic issue present in a recent batch of production vehicles. 
Having said that there is a bug and it is systemic (based on v406 and v604) but the issue is unrelated to production batches. So, the amount of risk to continue shipping and flying new aircraft is on par with the amount of risk the current fleet assumes.  Having said that, the team is welcome to re-evaluate the decision on whether a hold should be placed on shipping new aircraft. 
Note: At no point was either investigation ever closed or was a conclusion made that burst data caused the issue. The issue was observed when there was a significant CPU loading and Burst data results in a significant additional processor load. The recommendation was made simply to mitigate the risk.  
@Cameron Chapman We believe they are related, but not tied to any recent changes. In fact, there has been limited updates with the FW for about a year at this point. We don’t yet know the cause but we are looking to recreate and isolate the issue but even that will likely require the speedgoat HIL to be up and running.

### Cameron Chapman, 2024-02-20

Thanks @David Grosher and @Ben Triplett. Since both incidents happened during vtol descent, have you looked at other descents  that didn’t end in crashes to see if similar cpu load increases happen? 
We could look at the same aircraft on earlier flights and different aircraft.  We could also manually test the CPU load impact of additional webpages, burst mode, and other events on CPU loading.

### Matt Philley, 2024-02-21

@Marc Richardson Risk Assessment related to this topic has been attached.

### Garrett O'Neill, 2024-02-21

@Cameron Chapman @David Grosher 
Initial testing results for Center Wing 406:
- Visual inspections did not find any immediate evidence of defects or damage to the Magnetometer PCB, Magnetometer harness, or any other electronic components of the Center Wing. Did not completely tear down the Center Wing, so it is still possible there are defects/damage left to be discovered, particularly to the VTOL AP board assembly.
- Center Wing was powered up (without fuselage) and data appears to be getting exchanged successfully between external Magnetometer and VTOL AP:
- In VTOL AP webpage, under “Main/Calibration/Mag Cal”, Bxyz shows live data for external Magnetometer.
- Wiggling, pulling, etc. the Magnetometer harness does not affect stability of the live data.
- This was the steady state data of the Magnetometer: 
- Bxyz Live: 0.2919, 0.2204, -0.4921
- This was the Magnetometer data in response to a metallic object placed nearby the board:
- Bxyz Live: 0.0358, 1.3615, -0.6670
- Aligned the Center Wing so that the “nose” of the aircraft pointed south. Center Wing was upside down with the Magnetometer board held level. The heading below (from Instrument Panel) is what was displayed.
- [embedded: image-20240221-170820.png]

### Cameron Chapman, 2024-02-21

Thanks @Garrett O'Neill see updates in the fields above. Please update in the future as you go.

## Attachments (8)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| Incident 2.8.2024.jpg | image | 1110 | 2024-02-14 | listed only |
| Screen.jpg | image | 279 | 2024-02-14 | listed only |
| T95_V406_240208_144713_01_pack.zip | archive | 1019 | 2024-02-14 | listed only |
| T95_V406_240208_144713_02_pack.zip | archive | 774 | 2024-02-14 | listed only |
| T95_V406_240208_144713_pack.zip | archive | 941 | 2024-02-14 | listed only |
| T95_V406_240209_060928_pack.zip | archive | 3594 | 2024-02-14 | listed only |
| [Risk Assessment - AC 604 and 406 CPU Loading and Mag Issue Crashes, Use As Is - 24.02.21.pdf](attachments/18889_Risk%20Assessment%20-%20AC%20604%20and%20406%20CPU%20Loading%20and%20Mag%20Issue%20Crashes,%20Use%20As%20Is%20-%2024.02.21.pdf.md) | pdf | 439 | 2024-02-21 | converted |
| image-20240221-170820.png | image | 10 | 2024-02-21 | listed only |
