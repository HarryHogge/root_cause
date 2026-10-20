# VXEP-1497: VXE 734 E140 Connection Issues

- **Issue type:** Incident (8D)
- **Status:** New
- **Priority:** High
- **Created:** 2025-09-04
- **Updated:** 2026-04-21
- **Reporter:** Cameron Chapman
- **Assignee:** Justin Hogan
- **Creator:** Cameron Chapman
- **Links:** relates to VXEP-1509 (MOLSON report: E140 unable to get GPS fix and unable to slew to GPS location); relates to VXEP-1452 (New E140 Assemblies video quality issues)
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

Underlined main issues below

Email from Justin Good morning, Mike, 
 
Sorry for the delay on this write up from yesterday. I wanted to take some time to think through this and see if I was missing anything. 
 
Apologies for the delay in getting this write-up to you. I wanted to take some time to think it through and ensure I wasn’t overlooking anything.
John and I went out to Cortland to flight test the E140Z G2 Regulated Payload Cable design. We encountered some unusual behavior from the system during testing enough that, if I were in your position, I wouldn’t feel comfortable sending these cables to the customer. While the final decision is above my level, I recommend we begin exploring alternative options to maintain customer confidence. Below, I’ve outlined the test details to provide more insight into the anomalies we observed.
Test Summary:
    Aircraft Used:
·         #881 (Block 35x)
·         #734 (Block 30)
    Gimbals Used:
·         #6084
·         #6421
    Flight Duration:
·         All flights were approximately 20–25 minutes
Test 1 (Line 33) : We started by testing aircraft #734 with gimbal #6084 and quickly got the aircraft in the air with a good functional checkout and clean video during the entire flight. One thing to note we did experience 80 bad packets in the XCOMM throughput page for the video during boot-up but had zero bad packets during flight.
Test 2 (line 34): We moved gimbal #6084 over to aircraft #881 and quickly got the aircraft up in the air with good clean video and full functionality during the entire flight. One thing to note we did experience 22 bad packets in the XCOMM throughput page for the video during boot-up but had zero bad packets during flight.
Test 3 (Line 35): After test 2, we moved on to testing gimbal #6421 on aircraft #881. During boot-up we noticed bad packet appearing in the XCOMM throughput webpage and was unable to get the gimbal to connect through Epsilon. We went into the XCOMM hardware page and turned AUX 1 power off and back on. After this soft reset the gimbal connected without any issues and stopped receiving bad packets in XCOMM.  A couple things to note:
     1.) we were able to ping the gimbal from the GCS laptop while not being able to connect  
     2.) We did experience 179 bad packets in the XCOMM throughput page for the video during boot-up 
     3.) This whole process took about 30 minutes to run through multiple Epsilon versions. 
Test 4 (Line 36) : After test 3, we moved on to testing gimbal #6421 on aircraft #734. During boot-up we noticed bad packet appearing in the XCOMM throughput webpage and was unable to get the gimbal to connect through Epsilon. We went into the XCOMM hardware page and turned AUX 1 power off and back on. We ended up disassembling the center wing and cycling main power. After this hard reset the gimbal would not connect through Epsilon ver 14 or 13. We luckily still had ver 3.5.5 on the laptop and was able to connect without any issues and stopped receiving bad packets in XCOMM.  A couple things to note:
     1.) we were able to ping the gimbal from the GCS laptop while not being able to connect  
     2.) We did experience 646 bad packets in the XCOMM throughput page for the video during boot-up 
     3.) This whole process took about 30-45 minutes to run through multiple Epsilon versions. 
 
Observations and additional thoughts: 
Although this is a small data set, it raises questions about differences between the gimbals and suggests multiple overlapping issues contributing to the complexity. I wanted to get this to you so you can consider next steps. Based on my limited knowledge, here’s my recommendation:
 
Recommended Option for Moson: 
- Have an EA team travel to the customers' sight and preform an ATP of every aircraft on site with the customer to verify every gimbal, cable and aircraft are working correctly with each other.

- Look to switch the E140 out with an alternate until we resolve all issue with the system. I understand that this may not be well received message across the organization. Please note, this would even be an option in my head if we had more time.

## Plan

Recommendations
- Link a sharepoint summary doc (likely excel) with the following
- Aircraft SN, config, FW versions
- Gimbal SN, config, FW versions
- Gimbal cable PN and SN
- GCS and epsilon GUI SN, config, FW versions
- Test results and issues for these tests
- Start recording and linking common gimbal issues, C/CA statuses.
- Possibly separate above into multiple incidents once it is more clear what different issues exist for various configs/SNs.

## Comments (3)

### Justin Hogan, 2025-09-04

Gimbal Harness table.xlsx

### Cody Smisek, 2025-09-05

I have been loosely following all of the harness issues reported. but will say i have a camera gcs software combination where I simply cannot get the camera to connect on one GCS with a epsilon version .11 but I can get it to connect on a different GCS with a different epsilon version. Never seen that issue before.

### Cody Smisek, 2025-09-05

@Cody Smisek regarding this comment, just discovered dual SA media client v3.3.10 is causing the issue i’m describing. Unsure if at all related to this ticket. informed @Kurt Burian

## Attachments (0)
