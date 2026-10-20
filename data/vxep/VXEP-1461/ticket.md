# VXEP-1461: VXE-881 MCM and XCOMM Lost connection

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Not Verifiable
- **Priority:** Highest
- **Created:** 2025-08-05
- **Updated:** 2026-06-30
- **Resolved:** 2026-06-30
- **Reporter:** Jackson Riley Curvin
- **Assignee:** Justin Hogan
- **Creator:** Jackson Riley Curvin
- **Labels:** GS_Closed
- **Customer:** Redwire
- **Vehicle Tail Number:** VXE-881
- **Problem Type:** Other (explain in description)
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

While test the newest version of epsilon cable with the ethernet magnetic interference PCB.
Instance 1: Powered on aircraft using ac power adapter, while trying to connect via silvus while making changes in silvus web page I noticed the gimbal turned off and lost connection to the web page within a couple of seconds the MWIR powered back on and never saw it again. 
Instance 2: Alex was showing me how he was doing the testing procedure, while in the minute or so waiting period for the payload to initialize between power cycle and OGCS release/take over, the plane reset and we lost connection to it, no chirp
Instance 3: approximately ten seconds after the epsilon finished its BIT after a power cycle, lost connection to everything again, no chirp
Instance 4: Happened while the payload was powering back on, didn't see anything out of the ordinary, listening to the payload doing its bit, watched the ogcs gui disconnect from the plane and my xcomm webpage also lost connection. failed during payload start up
 
All instances happened with no hands on the keyboard, no active inputs from the users

## Plan

Assigning to @John Gober. @Jackson Riley Curvin  can you please include payload and harness part numbers, serial numbers, and location for this and every payload incident. FYI @Justin Hogan

## Comments (17)

### Jackson Riley Curvin, 2025-08-05

@David Grosher @Mike DeJesus @John Gober

### Mike DeJesus, 2025-08-05

@Greg Fryer

### Alexander Alan Arnold, 2025-08-05

@Mike DeJesus @Greg Fryer Jackson uploaded an AAR from during the XComm/MCM reset, we did a dull data pull and uploaded it please let us know if we need to gather additional files from the aircraft.

### Mike DeJesus, 2025-08-05

@Craig Burton  Can you please take a look at the logs for this? @David Grosher thinks it may be a networking issue

### Craig Burton, 2025-08-05

@Mike DeJesus The attached files do not contain any logs from the MCM.

@Alexander Alan Arnold Can you get an AAR via OGCS?  Or pull the VSM and OGCS logs directly?

What is the working theory?  That a networking issue (somewhere) is causing the MCM to reset and take down XComm as well?

### Alexander Alan Arnold, 2025-08-05

@Craig Burton what is the process for pulling logs from the MCM the XCOM download we did earlier was by typing the ip address in file explorer and pulling them that way. 

Does the AAR generated in SUAV differ from an AAR generated in OGCS? 

Do want us to induce another MCM reset and pull new logs a specific way?

### Alexander Alan Arnold, 2025-08-05

@Craig Burton I have uploaded an AAR generated from OGCS. Please let me know if you have the data required or if we need induce andother MCM reset and generate a new AAR.

### Alexander Alan Arnold, 2025-08-05

@Justin Hogan

### Justin Hogan, 2025-08-05

[embedded file][embedded file]
MCM Log files attached here. @Craig Burton @Alexander Alan Arnold

### Craig Burton, 2025-08-05

Thank you for the logs.  Because of the system date not being accurate, it is not straightforward to identify a specific event at a specific time.  Note that the syslog shows that 881’s MCM has booted 55 times on May 5 (presumably the last date that its clock was set by NTP).  We’ll regroup tomorrow and explicitly set the date and time prior to testing.

```
cburton@UbuntuMC:~/Documents/881-resets/var/log$ grep -a "Booting Linux on physical CPU" syslog
Aug 29 11:09:54 eamcm0378 kernel: [    0.000000] Booting Linux on physical CPU 0x0000010000 [0x410fd421]
Aug 29 17:23:01 eamcm0378 kernel: [    0.000000] Booting Linux on physical CPU 0x0000010000 [0x410fd421]
Sep  4 09:51:36 eamcmXXXX kernel: [    0.000000] Booting Linux on physical CPU 0x0000010000 [0x410fd421]
Sep  4 10:52:17 eamcmXXXX kernel: [    0.000000] Booting Linux on physical CPU 0x0000010000 [0x410fd421]
Sep  5 11:21:29 eamcmXXXX kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
Oct  1 08:53:37 eamcmXXXX kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
Oct  1 08:53:10 eamcmXXXX kernel: [    0.000000] Booting Linux on physical CPU 0x0000010000 [0x410fd421]
Oct  1 08:53:10 eamcmXXXX kernel: [    0.000000] Booting Linux on physical CPU 0x0000010000 [0x410fd421]
Dec 16 12:10:17 eamcmXXXX kernel: [    0.000000] Booting Linux on physical CPU 0x0000010000 [0x410fd421]
Dec 16 12:10:17 eamcmXXXX kernel: [    0.000000] Booting Linux on physical CPU 0x0000010000 [0x410fd421]
Dec 16 12:10:17 eamcmXXXX kernel: [    0.000000] Booting Linux on physical CPU 0x0000010000 [0x410fd421]
Dec 16 12:10:17 eamcmXXXX kernel: [    0.000000] Booting Linux on physical CPU 0x0000010000 [0x410fd421]
Dec 16 12:10:17 eamcmXXXX kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcmXXXX kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcmXXXX kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcmXXXX kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcmXXXX kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcmXXXX kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcmXXXX kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcmXXXX kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcmXXXX kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcmXXXX kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcmXXXX kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcmXXXX kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcmXXXX kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcmXXXX kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcmXXXX kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcmXXXX kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
May  5 10:35:13 eamcm0881 kernel: [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd421]
```

### Greg Fryer, 2025-08-07

@Justin Hogan You were already commenting on this, but this is the incident. As you get through this, if we prove to ourselves this is not cable related, do state that explicitly. I moved this to you from @John Gober given the working theory of the mis-configured* MCM. (*Very simplistic explanation)

### David Grosher, 2025-08-15

@Justin Hogan Have we confirmed that this is an MCM/XCOMM reset or if the network connection was simply lost.

### Justin Hogan, 2025-08-18

@David Grosher There are a series of things that are impacting the MCM reset issue. 

1.) Hot plug the gimbal - Connor is spot on with his analysis that hot plugging the gimbal will cause the MCM to reboot. I don’t see this being an issue with flight due to the connector having a locking mechanism. I would also recommend that we stop hot plugging the gimbal while on ground without turning power of to the gimbal through XCOMM software.  Logs attached below for the Hot plug. 
[embedded image-20250818-160925.png]
2.)  PMC Reset error - I believe is tied to MCM partitioning being configured incorrectly. After Alan and I reconfigured the MCM, we haven’t seen the PMC Reset after that in the SYSLog (cd /var/log) .  Below is a look at the PMC reset error and then Also detailed write ups for the partitioning issues from production. I’d like to see someone set a test up with MCM not configured correctly to reproduce this as a step to confirm. 
https://jenaero.atlassian.net/browse/NCC-174 https://jenaero.atlassian.net/browse/NCC-168 https://jenaero.atlassian.net/browse/NCC-161 
[embedded image-20250818-161634.png]
3.)EMI/Grounding issue - John and I noticed this last Friday when doing a final checkout of the cable. Whenever the cable is installed in the Block 30 or Block 30 AdvNav aircrafts the video is fragmented and delayed. I also did a ping test from the MCM to the gimbal on the AdvNav aircraft with shocking results. We experienced 60-40% packet loss over 15 minutes.  We did not experience this issue on the BLOCK 35X aircraft. More testing is still needed to help define the issue here but John has the team creating a cable with shielding. 

4.) DC/DC board overheating - Faulty DC/DC board.

### David Grosher, 2025-08-18

@Justin Hogan Yes, I am tracking most of this. I was just concerned that this particular issue was different and I want to be sure it is causing a reset versus some issue with the network. Especially in the case of the XCOMM.

### Justin Hogan, 2025-08-18

@David Grosher I haven’t seen the XCOMM board go down from a forced reset through hot plugging the gimbal. I only logged into the XCOMM board after power cycle and never had to log back into the interface. Is there a better way to verify this on the XCOMM board itself? Ie. logs or something else

### David Grosher, 2025-08-18

@Justin Hogan The XCOMM event log may show a crash dump if there was a WDT event. Or the CPU time in logging timestamps would have reset to 0 in the event of a power based reset.

### Jackson Riley Curvin, 2026-06-30

@Justin Hogan  I believe this can be closed if I'm not mistaking the corrective action was the new mounts for the gimbal correct?

## Attachments (7)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_V881_20250805T171236Z.zip | archive | 36860 | 2025-08-05 | listed only |
| T115_V881_250804_121239_pack.zip | archive | 7100 | 2025-08-05 | listed only |
| XCOMM VXE-881.zip | archive | 9740 | 2025-08-05 | listed only |
| tn880_varlog_20250805.zip | archive | 5701 | 2025-08-05 | listed only |
| tn881_varlog_20250805.zip | archive | 7274 | 2025-08-05 | listed only |
| image-20250818-160925.png | image | 439 | 2025-08-18 | listed only |
| image-20250818-161634.png | image | 20 | 2025-08-18 | listed only |
