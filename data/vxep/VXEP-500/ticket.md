# VXEP-500: VXE 674 E140ZG2 gimbals interfere with magnetometer.

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-07-11
- **Updated:** 2025-01-29
- **Resolved:** 2025-01-29
- **Reporter:** Cameron Chapman
- **Assignee:** Greg Fryer
- **Creator:** Cameron Chapman
- **Links:** relates to VXEP-183 (Establish aircraft grounding, bonding, shielding, etc. status and roadmap.); relates to VXEP-813 (E140 Octopus/VXE30 Isolation Issues: Arcing to Fuselage, mag interference suspected)

## Description

See comments for message chain and summarize here. VXE 674 E140ZG2 gimbals interfere with magnetometer. FYI @Greg Fryer @Mike Gomez @Aleksandrs

## Plan

- Dave "This is a Payload hardware issue not a software issue. @Sam Miller Who should this be passed to in Latvia. They don’t have access to our JIRA, so they will need a copy of the data.”
- Email sent to Herberts and Guks
- Hello, 
I hope things are going well for you and your teams. We are experiencing fixed wing magnetometer interference when using an E140 installed into a VXE30.
  
- Have you experienced that in the past?
- Do you have any recommendations for diagnosing and fixing this issue?
- Do you have access to an E140 and VXE30 to test for interference?
- Would it be feasible for us to remove the lens cap magnet and see if that is the source of the interference (or the motors).
- Do you have a system you use for recording issues and project tracking that we could use and access? I don't think JIRA is setup yet for export compliance.
- @David Grosher and @Everett Werner 
- Have we done enough data review to determine if this issue has increased with recent SW or HW changes, or has it always been present with E140 gimbals? 
- Initial impressions seem to point to hardware compatibility.
- Do you think any software changes could/should be made to minimize this issue, or is it primarily a hardware issue (E140 changes, different mag or placement). hardware
- Do you anticipate any upcoming changes are good opportunities to fix this issue (future SW releases, MAGNSS, unified AP)-no
- Should we consider hardware fixes prior to unified AP, or would that drive too much HW and SW scope for a low risk item?

## Issue Status

Summarizing the discussion prior to LRR. 
- Dave and Sam agree no safety of flight. Have been flying for a long time like this. Even when having problems with launch wizard, there has been no impact to flight.
- Greg N mentioned that that interference at LRR was minimal and did not prevent launch wizard.
- Issue appears to be present on all aircraft and gimbals tested. May have been less prevalent earlier, but launch wizard issues have been frequent, and were likely often due to this. Needs data review.

@Everett Werner@Cody Smisek  @David Grosher @Sam Miller @Gregory Nichols does the above description sound accurate? You are welcome to add or clarify if useful. 
FYI @Carl Graf .

## Comments (20)

### Cameron Chapman, 2024-07-11

[12:24 PM] Cody Smisek
Using 674, with e140zg2 sn6084 marked 24-30v, seems to have significant EMI issues that are impacting fixed wing mag.
 
[12:25 PM] Cody Smisek
Attempting to find the sweet spot for positioning gimbal but one gimbal position appears to only work if vehicle direction is not changed
 
[12:25 PM] Cody Smisek
When gimbal is moved in pan, it is obvious fw ap mag is impacted
 
[12:36 PM] Cody Smisek
Also had 2x random Epsilon software crashes. Unknown what contributed.
 
[12:43 PM] Sam Miller
Interesting...the Riga folks also had the same issue with one of their new gimbals...wonder if something changed in the gimbals recently?
 
[12:44 PM] Sam Miller
Positioning the motor in the yoke away from the avionics box during the launch wizard helped
 
[12:45 PM] Cameron Chapman
Cody Smisek 
Using 674, with e140zg2 sn6084 marked 24-30v, seems to have significant EMI issues that are impacting fixed wing mag.

 No bueno. If the cable can reach, you could test by powering from another avionics box or ground test harness to see if the gimbal or harness is the main culprit. Do we have a sco or other gimbal to compare? 
[12:46 PM] Cody Smisek
We're swapping through gimbals right now
 
[12:47 PM] Cody Smisek
This is a lot of trial and error that will be difficult to replicate at the next site under a time crunch
 
[12:56 PM] Cameron Chapman
We should write a jira incident about this and red tag that gimbal if it proves to be gimbal specific. Let me know if you want me to start that. Hopefully that can lead to a c/ca. 
[1:03 PM] Cody Smisek
We tried another gimbal (sn6086). Similar results. Removed gimbal completely and appears mags are happy. So seems the combo of vxe30 and e140 (at least 674 and these two gimbals) is not working well
 
[1:07 PM] Cameron Chapman
Next step test a different aircraft to see if aircraft specific or common? 
[1:08 PM] Cody Smisek
Agreed. Not possible at this exact moment. Other aircraft is being utilized to fly a drop mission, other Other aircraft is in fuel cell. Will grab drop mission aircraft and check after they fly
like 1
 
[1:32 PM] Cody Smisek
Additional info, 6084 is mounted with the forecast3d material. 6086 is mounted with the aluminum mount.
Vxe490 with e95 (sn8012), appears stable mags, with pan in all quadrants. Checking no gimbal and e140 next

### Cameron Chapman, 2024-07-11

Vxe490 has e140zg2 6084, pan gimbal around, up to 40deg in mag change depending on direction gimbal is pointed

### Cameron Chapman, 2024-07-11

[3:13 PM] Cody Smisek
Attempted to place aluminum can cutout on forward portion of avionics enclosure of vxe674 with eps6084. No obvious improvements. >30deg change in fw mag when pan gimbal forward to aft.

### Cameron Chapman, 2024-07-24

[7/12 1:34 PM] Cody Smisek
Initial look at the data confirms significant mag discrepencies on the ground, these differences were not present in the same magnitude on the e-140 flight we have data for.
 
[7/12 1:34 PM] Cody Smisek
From Everett
 
[7/12 1:43 PM]
7/12 1:43 PM Meeting ended: 16m 15s
 
[7/12 1:51 PM] Cody Smisek
T95_V371_230405_090322_pack.zip
T95_V371_230404_133518_pack.zip
T95_V371_230404_095118_pack.zip
 
[7/12 1:51 PM] Cody Smisek
Everett Werner here are 3 flights that were equipped with E140ZG2
 
[7/12 1:59 PM] Cody Smisek
additional flights that state e140zg2
T95_V490_230816_122429_pack.zip
T95_V490_230816_142038_pack.zip
T95_V490_230817_111633_pack.zip
T95_V490_230817_124212_01_pack.zip
 
[7/12 2:34 PM] Cameron Chapman
Update: Dave and Sam agree no safety of flight. Have been flying for a long time like this. Even when having problems with launch wizard, there has been no impact to flight.
- Do we have a procedure/specific orientation for to optimize LW success? Cody Smisek (sorry if repeating questions you have answered. Busy days)
- Can we make a procedure for this?
- Testing Tuesday in HSV.  Can test then.
- Showing up early on Thursday. Setup at the field. Mag cal, tests, etc.

 
[7/12 2:35 PM] Cody Smisek
No i do not have any procedures to optimize success
 
[7/12 2:35 PM] Cody Smisek
orientations did not appear consistent enough to repeat when i was attempting 
 
[7/12 2:37 PM] Cody Smisek
best we can do is probably re orient the aircraft or gimbal and start slam clicking the next button in launch wizard until we pass it
 
[7/12 2:37 PM] Cody Smisek
one of our flights will be a timed takeoff, we will not be able to run through any procedures 
 
[7/12 2:38 PM] Cody Smisek
i'm not sure if 'showing up early on thursday' is an option, defer to Sam on that, don't know what the situation will be like 
 
[7/12 2:39 PM] Cameron Chapman
I hate to say it, but how bad of an idea would it be to disable or have a bypass for that launch wizard step, or the mag portion of it?
 
[7/12 2:39 PM] Cody Smisek
probably a bad idea is my guess. i think we can get past the LW step with enough re orientation 
 
[7/12 2:39 PM] Cody Smisek
it just doesn't look good 
 
[7/12 2:40 PM] Cody Smisek
also defer to software on good/bad of that idea
 
[7/15 8:10 AM] Cameron Chapman
Today I think we plan on putting the E140 and 300 to compare. Other than that, we could look at older flights to see if this condition has always been present or when it was introduced. 
We could also discuss strategy is to optimize the chances of launchwizard success. There seems to be a reasonable risk of not being able to launch in front of the customer during the timed  launch event. 
[7/15 8:10 AM]
Eric Cain added Carl Graf to the chat and shared all chat history.
 
[7/15 8:28 AM] Cody Smisek
I will do that right now
like 1
 
[7/15 8:28 AM] Eric Cain
Let us know if the issue is reproducible.
 
[7/15 8:29 AM] Cody Smisek
I'm sure it is. But will confirm
 
[7/15 8:30 AM] Carl Graf
This issue is definitely the priority over the battery flight so if 300 is needed to support the E140 resolution, please use it. 
 
[7/15 8:40 AM] Cody Smisek
Reproduced. Similar if not greater magnitude
 
[7/15 8:43 AM] Cameron Chapman
Carl Graf
This issue is definitely the priority over the battery flight so if 300 is needed to support the E140 resolution, please use it.

It seems like the best people to work this are firmware, flight science, flight ops, and GCS people. Data review, fimware version comparison, safety of flight, possible GCS launch wizard updates
 
[7/15 8:45 AM] Cameron Chapman
It also seems like the most critical item is finding ways to ensure we easily pass launch wizard at the demo while ensuring there is no risk to flight
 
[7/15 8:54 AM] Eric Cain
I need to run to the airport for a bit to pick up my wife, but it sounds like we may benefit from a quick meeting with the team to coordinate actions on the E140 issue. We can probably have some folks review data while others look at physical resolutions. If there is an EMI/EMC, can we confirm that is the problem by doing something like remotely connecting the E140 moving it further from the mags and confirm that the issue is reduced or disappears with separation? It is possible it is a software bug of some sort, but seems low likelihood. I would love to see confirmation that this is a physical EM problem or not.
 
[7/15 8:54 AM] Carl Graf

Eric Cain
I need to run to the airport for a bit to pick up my wife, but it sounds like we may benefit from a quick meeting with the team to coordinate actions on the E140 issue. We can probably have some folks review data while others look at physical resolutions. If there is an EMI/EMC, can we confirm that…

 Let's discuss at the sprint in a few minutes. 

 
[7/15 8:55 AM] Cameron Chapman
The interference exists with the cable unplugged, so it is the magnetic fields of the motor interfering with the mag. Not much we can do with hardware at this point (unable to redesign motor or move mag)
 
[7/15 8:55 AM] Eric Cain
Meaning the E140 isn't even connected to the aircraft?
 
[7/15 8:56 AM] Cameron Chapman
Correct (from memory of what Cody said)
 
[7/15 8:57 AM] Eric Cain
I'll try to dial into the meeting on my phone, in case you see 303 number
like 1

### Cameron Chapman, 2024-07-24

@Carl Graf updated the above fields with latest status and posted chat and data files.

### David Grosher, 2024-07-24

@Cameron Chapman This is a Payload hardware issue not a software issue. @Sam Miller Who should this be passed to in Latvia. They don’t have access to our JIRA, so they will need a copy of the data.

### Cameron Chapman, 2024-07-24

Asked about regranting access to Latvians to Jira with their new domain while ensuring export compliance here https://jenaero.atlassian.net/browse/ENGINF-275

### Cameron Chapman, 2024-07-24

@David Grosher from what you have seen, would you guess that the issue is mainly caused by magnetic interference from the E140 more than a typical payload, our system being more vulnerable to the interference than it should be, or both? 
Linking EMI/EMC projects. FYI @Abel J. Markow and @Mike Gomez

### David Grosher, 2024-07-24

@Cameron Chapman There is a magnet in the lens for the cap to put in place.  Our system relies on a magnetometer placed near the payload. This is a hardware issue that would need to be addressed either by changing the payload design or by the shielding of the avionics system.  While limited testing has been performed to rate it against other payloads, it is not a desirable solution for aircraft robustness.

### Cameron Chapman, 2024-07-24

Thanks Dave. @Cody Smisek do you have any idea if it would be possible and a good idea to remove the lens cap magnet and retest, or would this require returning to Latvia to repair?

### Cody Smisek, 2024-07-24

@Cameron Chapman I’m not familiar with how the magnet is fixed within the payload. During data gathering, I shielded the magnet with EMI tape and shielded avionics box with EMI tape. This did not yield any obvious results. (not suggesting it should / shouldn’t have, just reporting data). 
Best to ask someone in Riga such as Aleks Guks (likely a ME can provide additional answers but I do not know the org chart there anymore) for more information regarding the magnets and possible removal. My guess is they’re not field removable. 
Sounds like a great idea to get rid of it though. It is great at collecting ferrous metals from the dirt.

### Cameron Chapman, 2024-07-25

Sent this email to Guks and Herberts:
Hello, 
I hope things are going well for you and your teams. We are experiencing fixed wing magnetometer interference when using an E140 installed into a VXE30.
  
- Have you experienced that in the past?
- Do you have any recommendations for diagnosing and fixing this issue?
- Do you have access to an E140 and VXE30 to test for interference?
- Would it be feasible for us to remove the lens cap magnet and see if that is the source of the interference (or the motors).
- Do you have a system you use for recording issues and project tracking that we could use and access? I don't think JIRA is setup yet for export compliance.

### Cameron Chapman, 2024-08-06

8/6 email chain:
Hi Herberts,
Can we engage our EMI lab we used for Safran project and test the following:
- Baseline Measurement: Use a Gaussmeter/EMI detector to measure the ambient magnetic field without the gimbal installed. Record the baseline readings.
- Install Gimbal and Measure: Install the E140 gimbal on the VXE30 and repeat the measurements at the same locations where baseline measurements were taken. Compare the readings to identify any significant changes.
- Identify Interference Sources: Move the measurement device around the gimbal and UAV to map out the magnetic field. Identify areas with high magnetic flux density.
- Shielding and Mitigation Testing: Apply shielding materials (EMI shielding tape) around potential sources of interference and measure again to see if there is any reduction in interference.

Best regards, 
|  | Aidas Kučys VP/General Manager Edge Autonomy - Riga Phone: +371-2-668-7665 Email: akucys@edgeautonomy.eu Address: 1 Jaunbridagi, LV-2167, Mārupe, Latvia |

From: Greg Fryer <gfryer@edgeautonomy.io>
Sent: Tuesday, August 6, 2024 7:01 PM
To: Herberts Stāmers <hstamers@edgeautonomy.eu>; Cameron Chapman <cchapman@edgeautonomy.io>; Aidas Kučys <akucys@edgeautonomy.eu>; Sam Miller <smiller@edgeautonomy.io>; Dave Grosher <Dgrosher@edgeautonomy.io>
Cc: Aleksandrs Guks <aguks@edgeautonomy.eu>; Greg Nichols <gnichols@edgeautonomy.io>; Cody Smisek <csmisek@edgeautonomy.io>
Subject: RE: E140 VXE30 magnetometer interference
 
Herberts – Thank you all for conducting the testing and verifying!
 
I do not have any additional information. We have not altered the one E140 that we have, I do not think we have the tech data or knowledge to open the gimbal up.
 
I agree we should modify one E140 to remove the magnets and repeat the testing, is that process simple? (We don’t have a clean room here.) If not, we would need you to remove the magnets and send a unit to us.
 
Should we have a meeting to discuss? I also need to meet with KK, as we have been discussing the content of the various gimbal kits and support kits. Perhaps we can have one longer meeting to cover both topics – I think several folks would want to be in both discussions.
 
I am free at 0600 or 0700 pacific any day this week or next week. I can meet earlier if it’s helpful.
 
Regards,
Greg
 
 
From: Herberts Stāmers <hstamers@edgeautonomy.eu>
Sent: Monday, August 5, 2024 11:04 PM
To: Cameron Chapman <cchapman@edgeautonomy.io>; Aidas Kučys <akucys@edgeautonomy.eu>; Sam Miller <smiller@edgeautonomy.io>; Dave Grosher <Dgrosher@edgeautonomy.io>; Greg Fryer <gfryer@edgeautonomy.io>
Cc: Aleksandrs Guks <aguks@edgeautonomy.eu>; Greg Nichols <gnichols@edgeautonomy.io>; Cody Smisek <csmisek@edgeautonomy.io>
Subject: Re: E140 VXE30 magnetometer interference
 
Hi all,
I wanted to provide a brief contribution regarding this topic. According to our Flight OPS team, this exact issue was replicated here in Riga, using the following setup: VXE30 equipped with the 140 G2.
Three flights were conducted:
- VXE30 with a gimbal, where calibration of the magnetometer was disturbed.

- Bare UAV, no problems.

- VXE30 with a gimbal, where calibration of the magnetometer was disturbed.

No further actions have been taken.
 
I'm also including @Greg Fryer, who initially brought this question to our attention. Greg, could you provide any insights on this topic? Has the removal of magnets or other actions helped identify the root cause or a potential solution to the problem?
 
 
 
Regards
|  | Herberts Stāmers Project Manager Edge Autonomy – Riga Mobile: +371 25576537 Email: hstamers@edgeautonomy.eu |

 
From: Cameron Chapman <cchapman@edgeautonomy.io>
Sent: 26 July 2024 01:12
To: Aidas Kučys <akucys@edgeautonomy.eu>; Sam Miller <smiller@edgeautonomy.io>; Dave Grosher <Dgrosher@edgeautonomy.io>
Cc: Aleksandrs Guks <aguks@edgeautonomy.eu>; Herberts Stāmers <hstamers@edgeautonomy.eu>; Greg Nichols <gnichols@edgeautonomy.io>; Cody Smisek <csmisek@edgeautonomy.io>
Subject: Re: E140 VXE30 magnetometer interference
 
|  | Some people who received this message don't often get email from cchapman@edgeautonomy.io. Learn why this is important |  |

Hello Aidas, 
 
Initial evidence seems to indicate it has always been present, we were not aware of what was causing the interference/failure to launch until recently. 
 
We have more data and comments in JIRA, but I do not think we have setup a JIRA database that is export compliant yet. I can paste the data and comments into this email until then (see attached). Testing in August sounds like a good plan. I think it will be more efficient for you to test the interference and potential solutions with your payload design knowledge. 
@Dave Grosher do you know if flight data AARs are export controlled? I can send those if not controlled.
 
 
Thank you,
Cameron Chapman
 
 
From: Aidas Kučys <akucys@edgeautonomy.eu>
Sent: Thursday, July 25, 2024 2:52 PM
To: Cameron Chapman <cchapman@edgeautonomy.io>; Sam Miller <smiller@edgeautonomy.io>
Cc: Aleksandrs Guks <aguks@edgeautonomy.eu>; Herberts Stāmers <hstamers@edgeautonomy.eu>; Dave Grosher <dgrosher@edgeautonomy.io>
Subject: Re: E140 VXE30 magnetometer interference
 
Hi Cameron and Sam,
 
Is this a recent discovery, or has this issue always been present, given that E140 has been flown many times?
 
We have VXE30 available in Riga, and we can conduct tests if necessary.
 
However, testing can only be carried out in the first week of August since the factory reopens on August 5th.
 
Regarding tracking, Herberts can initiate a customer non-conformance in our system.
 
@Cameron Chapman, could you please provide more detailed information regarding the interference?
 
It would help us to understand better the effects you are observing on the magnetometer and which specific gimbal operation modes are causing this interference.
 
Best regards,
 
|  | Aidas Kučys |

### Mike DeJesus, 2024-08-14

I spoke with @Aleksandrs this morning. Riga Flight Ops is going to start conducting tests on their units 15 August.

### Mike DeJesus, 2024-08-16

Added pictures of the E140 mount variants

### Greg Fryer, 2025-01-28

@Charles David Madewell We should figure out what there is in this incident, if anything, that is not covered by https://jenaero.atlassian.net/browse/VXEP-813, I suspect it may be redundant now, and we should cancel it. Do you have any thoughts the other way?

### Charles David Madewell, 2025-01-28

@Greg Fryer Which one are you advocating deleting (VXEP-813 or VXEP-500)?

### Greg Fryer, 2025-01-28

@Charles David Madewell Advocating for canceling this ticket https://jenaero.atlassian.net/browse/VXEP-500. The only unique scope here is if Riga decides/can alter the gimbals to not include magnets. I don’t think that is worth tracking on our end, as an incident/project.

### Charles David Madewell, 2025-01-29

@Greg Fryer I did mention to Riga about 2 months ago the thought of removing the magnets from the gimbal.  I will need to revisit that with Aleks for a status.  I agree we should cancel this ticket https://jenaero.atlassian.net/browse/VXEP-500.  For consistency/CM, since you are the assignee, do you want to hit cancel?  It looks like this ticket was created back in July of 2024 so it has been around for some time.

### Greg Fryer, 2025-01-29

Per discussion we are closing this incident, as it is either the magnets in the E140 face (for cover mounting), or a possible ground loop (which is another incident), linked. Given that we are also moving to the wing magnetometer (VTOL), the magnet face issue should resolve and will just be managed with E140 design. We are canceling this incident.

## Attachments (23)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V371_230404_095118_pack.zip | archive | 2389 | 2024-07-24 | listed only |
| T95_V371_230404_133518_pack.zip | archive | 2129 | 2024-07-24 | listed only |
| T95_V371_230405_090322_pack.zip | archive | 2052 | 2024-07-24 | listed only |
| T95_V490_230816_122429_pack.zip | archive | 470 | 2024-07-24 | listed only |
| T95_V490_230816_142038_pack.zip | archive | 1450 | 2024-07-24 | listed only |
| T95_V490_230817_111633_pack.zip | archive | 2414 | 2024-07-24 | listed only |
| T95_V490_230817_124212_01_pack.zip | archive | 2262 | 2024-07-24 | listed only |
| 1 (46a927e1-0cf3-4ff9-abbe-050252c9ba61).jpg | image | 2777 | 2024-08-16 | listed only |
| 1.jpg | image | 2755 | 2024-08-16 | listed only |
| 2 (bc63b77c-cc31-4616-bc5f-c8e8cbde5d62).jpg | image | 2344 | 2024-08-16 | listed only |
| 2.jpg | image | 2633 | 2024-08-16 | listed only |
| 3 (8f408ad8-4008-4937-b9d0-fa47377a7d19).jpg | image | 2961 | 2024-08-16 | listed only |
| 3.jpg | image | 2756 | 2024-08-16 | listed only |
| 4 (b1a5b561-d88d-49f7-8ec1-68b94406b2e8).jpg | image | 2908 | 2024-08-16 | listed only |
| 4.jpg | image | 2726 | 2024-08-16 | listed only |
| 5 (610669d2-6ba9-4bf9-9b08-b9c03135aa90).jpg | image | 1538 | 2024-08-16 | listed only |
| 5.jpg | image | 940 | 2024-08-16 | listed only |
| E140 - Connector.jpg | image | 1855 | 2024-08-16 | listed only |
| E140 - Front Mount.jpg | image | 2387 | 2024-08-16 | listed only |
| E140 - Front.jpg | image | 2455 | 2024-08-16 | listed only |
| E140 - Side Mount 2.jpg | image | 2224 | 2024-08-16 | listed only |
| E140 - Side mount 1.jpg | image | 2002 | 2024-08-16 | listed only |
| E140 - Top Mount.jpg | image | 3181 | 2024-08-16 | listed only |
