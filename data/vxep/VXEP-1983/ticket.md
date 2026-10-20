# VXEP-1983: VXE 1021 Recognized Pylons but Would Not Arm Them w/ Droppers

- **Issue type:** Incident (8D)
- **Status:** D4 - Investigating Root Cause
- **Priority:** High
- **Created:** 2026-08-21
- **Updated:** 2026-10-14
- **Reporter:** Zachary Mann
- **Assignee:** David Grosher
- **Creator:** Zachary Mann
- **Labels:** LRR, RCCA, Weekly-incident-tracker
- **Customer:** LRR
- **Vehicle Tail Number:** 1021
- **Vehicle Configuration:** VXE35, OGCS, E140
- **Problem Type:** Other (explain in description)
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround
- **Executive Summary:** WUP Shipped to SLO for Further Investigation

## Description

For A/C 1021, it recognized the pylons but would not arm them. Both the student and instructor stated that it wouldn't give them the option to arm on the ground, so they launched hoping it would arm in flight for drops. The OGCS software gave alerts like it was armed when approaching the drop waypoint, but it did not arm or drop. The droppers were swapped to 1039. Later on when they were wrapping 1021 up, the back left boom did not spin when commanded during launch wizard.

## Comments (13)

### John Clark, 2026-08-21

Hi @Zachary Mann I am the Engineer assigned to this Ticket. In this case, I am concerned that the Pylons are not detected. I see several messages  to “Disarm” Pylon 1 and 2. What I dont see here is any attempt to Arm them. They should be Armed to Test the Drop function.

### Alexander Alan Arnold, 2026-08-26

@David Grosher Addison just pinged me on this one should we just set and arm droppers and do a test? Apparently a report or brief summary was promised to the army tomorrow… @John Clark please weigh in with any testing you would like done

### John Clark, 2026-08-26

@Alexander Alan Arnold you need a procedure, sir. Do you have documentation? In https://jenaero.atlassian.net/browse/VXEP-1984 @Cody Smisek responds to similar issues.
[embedded: image-20260826-185929.png]
The WUPs need to be physically configured onto the appropriate Aircraft Type (There are two kinds - Ethernet or Serial) and the OGCS used with the WUP after being powered if they are Ethernet and you have an SSR board. The OGCS may then be used to configure and test the individual droppers.
There is also the issue of the CWDB (Center-wing Distribution Board) which we should also take some stock of in your particular configuration.
What I observed in https://jenaero.atlassian.net/browse/VXEP-1984 above appears to be the Pylon never being recognized in any testing.
In the above test for this Ticket I do not see any detection of WUPs

### Jackson Riley Curvin, 2026-08-26

@John Clark In the vsm-event.08.19.2026 line 195 and 206 are these arm commands?
[embedded: image-20260826-222640.png]

### John Clark, 2026-08-26

@Jackson Riley Curvinyes, sir. I'm away from my station but that looks to be working.

### Jackson Riley Curvin, 2026-08-26

@John Clark are you saying that we need to locate the procedure to configure the droppers. Follow up does the configuration have to happen each time you swap aircraft, because the same drop kit was used on 1039 but only the right dropper worked.

### John Clark, 2026-08-26

@Jackson Riley Curvini have previously noted I have no output files I have reviewed where that particular dropper was working. I'm not sure what the problem is with it. Has it ever been verified working?

### Alexander Alan Arnold, 2026-08-26

from what i remember they worked before delivery to customer@John Clark alright we are going to install droppers on 1021 with no gimbal installed and run a wireshark capture. from my understanding after talking with abel is that the droppers will either recieve .7/.8 or .11/.12 in the aircraft network scheme. we are also going to see if they do receive an IP if they somehow have the same MAC address. the reason for no gimbal is that the MANI is currently set up to receive a .7 or .8 from the aircraft upon power up. Outside of a regular AAR to capture data what else needs to gathered from the available logs on the aircraft?

### John Clark, 2026-08-26

@Alexander Alan Arnoldplease reach out more directly tomorrow. The droppers work on the .100-.119 DHCP address pool.

### Zachary Mann, 2026-08-28

Reached out to @John Clark about logs

### Zachary Mann, 2026-09-01

Reviewed with @John Clark does not appear to show any discrepancies.

### Zachary Mann, 2026-10-01

Being shipped to SLO

### Zachary Mann, 2026-10-12

Tracking Number: 12116607107

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_V1021_B35_20260819T165708Z.zip | archive | 36876 | 2026-08-21 | listed only |
| image-20260826-185929.png | image | 50 | 2026-08-26 | listed only |
| image-20260826-222640.png | image | 100 | 2026-08-26 | listed only |
| 1021_drop_test_1.pcapng | other | 5435 | 2026-08-28 | listed only |
| AAR_V1021_B35_20260826T230013Z.zip | archive | 12492 | 2026-08-28 | listed only |
