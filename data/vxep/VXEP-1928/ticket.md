# VXEP-1928: VXE 1006 would not maintain altitude during descent in landing pattern leading to mishap

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed, but added to Bermuda Triangle List
- **Resolution:** Cannot Reproduce
- **Priority:** Highest
- **Created:** 2026-06-22
- **Updated:** 2026-07-28
- **Resolved:** 2026-07-07
- **Reporter:** Stephan Johnson
- **Assignee:** David Grosher
- **Creator:** Stephan Johnson
- **Labels:** GS_Closed, InternalIncident, RCCA, Weekly-incident-tracker
- **Links:** is fixed by OGCS-605 (No Landing Transition Altitude Limits); relates to XKIT-5523 (OGCS Allows Landing transitions of 0ft); relates to RMA-1069 (VXE-1006 RMA: 260728-1)
- **Customer:** Redwire
- **Severity:** 1 - Flight Critical

## Description

Instructor 1: During landing using a straight in approach, the aircraft was commanded to Land PLZ. It flew through IP1 and started descending in IP2.
The aircraft was struggling to maintain IP2 orbit during the entire descent. While the aircraft was descending I was walking though the landing phase
of flight and going over all the menus and controls with the student. I was monitoring the altitude and SA cam during descent. When the aircraft
reached 200' it began descending rapidly. Wes then called out that we were extremely low. I immeditaely took the controller and commanded abort.
The aircraft began climbing and enroute back to IP1 of the landing plan. After flying back though IP1, the aircraft began descending again in IP2.
Once again, the aircraft reached 200' and immediately began losing altitude quickly. Once at roughly 100' I attempted another abort. The aircraft
began trying to climb but was unsuccessful and crashed into a field. After the crashed, we reviewed the the landing pattern and it was showing an IP2
altitude of 2' and a transition altitude of 0'. I was monitoring the student create the flight plan and am 99.9 % sure that 200' was input for the landing
plan.
Instructor 2: I saw the aircraft in IP2 Decent, everything looked normal until it started descending below what I could tell was 200ft. I called it out that it was low
and that we should abort. I mentioned that it might be a settings issue and that we should check settings out loud. Once they sent it to IP2 again the
plane started to get too low again and I said out loud to abort. The aircraft left wing tip touched the bushes but took off and started to climb.
I called out what I was seeing and that we needed to abort/get out of landing. Even though the aircraft climbed a little it did not appear to leave landing
logic and finally dipped below a small hill and crashed.

## Plan

- @Drew Hildreth  is anyone in FLOPs available to audit other all data entry values and make sure only valid entries are acceptable (ex: could we enter 0ft in an other critical values). Notify OGCS to create linked issues to resolve identified issues.

## Comments (16)

### Craig Burton, 2026-06-22

Edit:  My analysis below is incorrect, please read my response below.
The VSM logs indicate that DTED was not found:
cburton@Ubuntu22:/media/sf_VBShared/incident$ grep dted vsm-info.06.22.2026
15:00:44.548288:  dted            File header is valid
15:19:04.535500:  dted            File not found
15:19:04.535577:  dted            File not found
15:19:04.535606:  dted            File not found
15:19:04.535617:  dted            File is null
15:19:04.884290:  dted            File not found
15:19:04.884368:  dted            File not found
15:19:04.884396:  dted            File not found
15:19:04.884405:  dted            File is null
15:19:05.892358:  dted            File not found
15:19:05.892435:  dted            File not found
15:19:05.892464:  dted            File not found
15:19:05.892499:  dted            File is null
15:43:13.097577:  dted            File not found
15:43:13.097686:  dted            File not found
15:43:13.097736:  dted            File not found
15:43:13.097753:  dted            File is null
As a first pass, can we please check the directory on the MCM to see the size of the L2 that is available?
- Log in to MCM as mcadmin
- Run this from anywhere:  du -sm /opt/maps/dted/DTED/DTED_L2

### Craig Burton, 2026-06-22

It would also be helpful to understand why we don’t see a valid Redwire Board Support Package version identifier in the logs:
==== New /mnt/edge/vsm/logs/vsm-info Log File == opened on 06/22/2026-15:00:44 ====
15:00:44.108890:  init            /mnt/edge/vsm/bin/vsmd build 'main/1ca5053a'
15:00:44.109083:  init            Starting...
15:00:44.136917:  init            Jetson Model:   CTI Hadron + Orin NX
15:00:44.136971:  init            Serial Number:  1613924611421
15:00:44.136979:  init            Tegra Release:  36.4.4 (JetPack 6.2.1)
15:00:44.136984:  init            CTI BSP:        ORIN-NX-NANO-36.4.4-V005
15:00:44.136989:  init            RDW BSP:        /
15:00:44.137601:  processor       udp listening to port: 50101
15:00:44.137718:  processor       udp listening to port: 50102
15:00:44.137764:  processor       udp listening to port: 50150

### Drew Hildreth, 2026-06-22

@Cody Smisek I heard that Anthony set you the data and you provided him with a conclusion. Can you please update what you found here so it is tracked within the ticket.

@David Grosher FYSA 
Also, if there is anything else that you see in here, please let me know.

### David Grosher, 2026-06-22

@Craig Burton What is the difference between “File not Found” and “File is null”? And, how can we see a null file if the DTED is entirely missing? Additionally, how can we see a valid header but have other missing files? It seems like this might be different than wholesale missing DTED folders.

### David Grosher, 2026-06-22

@Bethany Ponce @Alan Burnsworth Is the RDW BSP included in the MCM image?

### Cody Smisek, 2026-06-22

@Drew Hildreth As I told Anthony, my analysis was not official and I instructed the team to create a Jira ticket such that the software team can conduct an investigation. 
My review of the logs indicated that the AP followed the commanded 22ft. As to why it was commanding that low, I am unable to determine conclusively. 
We tested on OGCS that you can set landing transition to 0ft AGL so I would reasonably conclude that an operator could accidentally set a transition altitude that would result in CFIT. At a minimum, adding protection to prevent that should be a CA from this incident. Whether or not that was the actual cause I am unsure.

### Michael Mohr, 2026-06-22

@Craig Burton We found 474310 MB. Like you said, looks like a pretty full set.

### Craig Burton, 2026-06-22

@Michael Mohr Thank you for checking that, Michael.
@David Grosher Good questions, my earlier analysis was incorrect.  The log statement File header is valid is the initial lookup based on AP telemetry of position and indicates that a DTED tile at the vehicle’s position was located and the header was valid.  This file name and handle are cached for subsequent queries, which is why it only appears once per VSM run:
15:00:44.548288:  dted            File header is valid
All of the subsequent blocks of the following happened immediately after AP restart when the vehicle sends (0.0, 0.0) and there is no tile available in any resolution.  The DTED interface first looks for L2, then L1, then L0, then gives up (“null”):
15:19:04.535500:  dted            File not found
15:19:04.535577:  dted            File not found
15:19:04.535606:  dted            File not found
15:19:04.535617:  dted            File is null
Note that we don’t see these messages with a HIL, part of the reason for my poor analysis earlier, unless we kill X-Plane and XPI while the reset is occurring.  Here is an example of that with a “show position” flag set to true (not used in Production):
14:19:44.235402:  dted            L2 calculated file: '/opt/maps/dted/DTED/DTED_L2/w001/n00.dt2'
14:19:44.235413:  dted            Opening file: '/opt/maps/dted/DTED/DTED_L2/w001/n00.dt2'
14:19:44.235440:  dted            File not found
14:19:44.235463:  dted            L1 calculated file: '/opt/maps/dted/DTED/DTED_L1/W001/N00.dt1'
14:19:44.235473:  dted            Opening file: '/opt/maps/dted/DTED/DTED_L1/W001/N00.dt1'
14:19:44.235490:  dted            File not found
14:19:44.235509:  dted            L0 calculated file: '/opt/maps/dted/DTED/DTED_L0/W001/N00.dt0'
14:19:44.235519:  dted            Opening file: '/opt/maps/dted/DTED/DTED_L0/W001/N00.dt0'
14:19:44.235535:  dted            File not found
14:19:44.235545:  dted            File is null

### Calvin Rogers, 2026-06-22

[embedded: frontend-logs-2026-06-22T16-25-16-454Z.tar.gz]
@Ted Trowbridge

### Ted Trowbridge, 2026-06-22

At ~33 minutes after MCM boot the logs indicate that the operator commanded a Straight-In Primary Landing with a IP1 altitude of 1500ft and a pattern altitude of 2ft.  The pattern was previewed briefly while the angle was set to 130deg and then it was uploaded.
Earlier on the same flight at ~25 minutes after boot there was an original PLZ and ELZ set up that both had valid IP1 and Pattern altitude (1500ft and 200ft)
All indications suggest operator error: the value was entered as 2 feet instead of 200 feet. The fact that 2 is exactly 200 with its zeros dropped lends some further credibility to this, either the zeros were accidentally deleted or the keystrokes were never registered.
Do we know why the PLZ was edited at the end?  It looks like it was moved horizontally ~130 feet.

### Ted Trowbridge, 2026-06-22

https://jenaero.atlassian.net/browse/OGCS-605 is in work as a CA.

### Ted Trowbridge, 2026-06-22

[embedded: VXEP-1928-T1006-Landing.mp4]
Here is a recording of the landing and CFIT.  There is one abort back to IP1 after which the vehicle does regain some altitude, but once it captures IP1 it goes back to IP2 and descends rapidly.
Note: The locations are scrubbed by OGCS so this is shown in a “random location”.  Headings/bearings do not line up so aircraft crab angles during navigation are incorrect.

### Craig Burton, 2026-06-22

Adding similar validations in VSM under https://jenaero.atlassian.net/browse/MS-1669

### Drew Hildreth, 2026-06-23

@Cody Smisek appreciate you taking a look at this and providing feedback. We are also going to have some internal discussions with our teams here to reiterate how we report issues/incidents.

### Anthony Hansen, 2026-07-01

@Ted Trowbridge I am not sure where I can suggest this as well to prevent future issues, I forgot to put it on my B35 LRR IQT AAR. In Jennings there is a warning that pops up if the Operator attempts to perform a VTOL Land Immediately at an altitude above the estimated HLB energy remaining (I believe it came out in 6.4). From what I have seen in the HIL testing with OGCS 1.4.1 and older it is very possible to perform a VTOL Land Immediately at unsafe altitudes, with an insufficient energy warning after the Land Immediately is commanded.

The pop up in Jennings suggests the Operator to not continue, although allows the Operator to continue with the VTOL Land immediately after selecting through the warning.

### Stephan Johnson, 2026-07-07

Issuing SW mod to ensure customer cannot input less than 200ft for transition altitude

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [1006 Mishap Report.pdf](attachments/63025_1006%20Mishap%20Report.pdf.md) | pdf | 325 | 2026-06-22 | converted |
| AAR_V1006_B35_20260622T162500Z.zip | archive | 18576 | 2026-06-22 | listed only |
| VXEP-1928-T1006-Landing.mp4 | video | 390629 | 2026-06-22 | listed only |
| frontend-logs-2026-06-22T16-25-16-454Z.tar.gz | archive | 4826 | 2026-06-22 | listed only |
