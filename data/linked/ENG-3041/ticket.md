# ENG-3041: Tail 380, Aborted launch "VT lost link during lnch, aborting"

- **Issue type:** Problem
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2023-04-17
- **Updated:** 2025-06-02
- **Resolved:** 2023-06-30
- **Reporter:** Artis Bertulis
- **Assignee:** John Clark
- **Creator:** Greg Fryer

## Description

After a successful 1st SCO flight for this aircraft, during the second launch, it reached about 250ft and aborted take-off on its own, landed safely. Debug window showed a message "VT lost link during lnch, aborting", 4 other flights were performed after this abort - the aircraft was able to take off and transition as usual.
Related NCR 890: 
Aborted take-off

## Comments (14)

### John Clark, 2023-04-17

@Artis Bertulis could you attach the logs for this flight, please?

### Artis Bertulis, 2023-04-17

@John Clark 
[embedded: T95_V380_230413_132543_pack.zip]

### John Clark, 2023-04-17

@Artis Bertulis the failure encountered was software related. The Abort relates to the fact that communications were lost with the Host (GCS) for more 5 seconds and that the loss occurred in the launch phase of flight before VTOL was completed.

### Artis Bertulis, 2023-04-17

Thanks @John Clark for the report. I do feel like I had a link and the data from the aircraft was updating in the GCS software during the climb, so it’s odd that the lost link got triggered. For that reason, I was under impression that VT link means VTOL link, or the link between VTOL and Fixed Wing, not the general communication with the GCS. 
Does the data confirm that it was the link between the aircraft and GCS that was lost?

### John Clark, 2023-04-17

@Artis Bertulis strictly speaking the FW AP that aborted only has a single interface. That’s the serial port. Most commands that influence the uplink status would seem to me to be from the GCS, “uplink”. So, that’s an assumption from me based on the fact we seem to be waiting for a Command response. The vt is coming from the fact the FW AP is in the Vtol.cpp module, I think, since most of the logging in that module uses the prefix and nothing elsewhere does. To answer your question directly. No, but the command set associated with MaintainLink() sure do appear to me to originate from there. Question, how would you determine the Rx commands from the GCS were arriving? From watching the GCS? What I’d like to see is a pkt sniffer on the radio link itself. : )

### Artis Bertulis, 2023-04-18

@John Clark Is it possible to test lost-comms launch on HIL, to simulate if the same error appears?
@Artis Bertulis timeout, not Lost Comms. There is a difference, I think.

### John Clark, 2023-04-18

I’m sure I could simulate this somehow. The state machine was in State 9, “command departure altitude” (LCH_GOALT) and awaitng state 10, “wait for departure altitude, monitor health” (LCH_WAITGOALT). ManageLostLink() kicked in and created an “Abort Launch”. Because most of those timeouts relate to GCS related Commands I speculated that was the source of the timeout that occurred. But simply starving the state machine in Vtol will probably induce failure. Is the goal to prove we can do that, or did you want to try and change the state machine to prevent it? If we want to start trying to prevent Launch Aborts I think we need to carefully examine why those are there and if we want to be doing that. 
Again, I am fairly certain GCS communications are the culprit here. I cant really print out the code here. But if you want to drop by I can give you a tour.

### Artis Bertulis, 2023-04-18

My goal is not to remove any of the safety features, I’m actually glad it aborted on it’s own when detecting a problem. I just want to make sure there’s not a deeper problem in this vehicle before we send it to customer.
GCS comms fail I’m fine with, it happens sometimes, but if there was a problem in between the 2 autopilots talking, that would concern me.
@Artis Bertulis this failure occurred because the FW AP lost the link. As stated, that’s the serial connection into the FW AP. The failure was based on a timeout that occurred in Vtol. That is a critical phase of flight.

### John Clark, 2023-04-18

@Artis Bertulis here is what I think I know from the status:
// apm support
// Options bits
#define APM_ONLINE 0x0001	// getting heartbeat messages
#define IMU_MATCH 0x0002	// rpy good compared to AP
#define POS_MATCH 0x0004	// lla good compared to AP
#define SERVO_ON 0x0008		// servo pulses above 1200? uS
#define SERVO_IDLE 0x0010	// servo pulses at idle value 1002 uS
#define SERVO_SAFE 0x0020	// safe mode enabled
#define APM_FLYING 0x0040	// currently flying according to the vtol controller
#define APM_HOVER 0x0080	// "stationary"
#define APM_POWER 0x0100	// power enough to fly
#define APM_ARMING 0x0200	// arming for takeoff active
#define APM_CAL 0x0400		// sensor calibration/home set active
#define APM_HOME 0x0800		// set home acknowledged
#define APM_RC 0x1000		// manual control active
#define APM_ATT 0x2000		// attitude okay (inside specified pitch and roll
#define LAND_PAUSE 0x4000	// landing is currently paused
#define LAND_DETECT 0x8000	// landing detected (land mode plus low enough laser agl
Also, looked at the VTOL logs and I dont see any abnormalities.

### Artis Bertulis, 2023-04-18

Ok, thanks, John. To sum up what we discussed (and feel free to correct me if I'm wrong) - There was a timeout between the Legacy autopilot’s responses to the VTOL autopilot which caused it to abort the landing. This is a software thing and not an aircraft-specific issue, it’s very rare but can happen to every vehicle.

### Matt Philley, 2023-04-19

@Artis Bertulis @John Clark 
So it sounds like a decision has been made. Please make sure to input the final determination in the NCR with a clear decision. Is this Use As Is with a technical justification or do we need to perform any rework or additional testing. 
Thanks for the help! 
Link here and in the description: Aborted take-off

### John Clark, 2023-04-19

@Matt Philley The failure encountered was software related. No decision to change the behavior has been made. There is no need to perform additional testing or rework.

### Matt Philley, 2023-04-19

@John Clark sounds good! Are you good with me updating the NCR with a Use-as-is for you so we can close it out? @Matt Philley Use-as-is

### Cameron Chapman, 2023-08-24

Linking subtasks to parent.

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V380_230413_132543_pack.zip | archive | 2289 | 2023-04-17 | listed only |
| [Vehicle 380 incident report.pptx](attachments/13954_Vehicle%20380%20incident%20report.pptx.md) | pptx | 74 | 2023-04-17 | converted |
