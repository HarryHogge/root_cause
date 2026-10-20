# FS2-3635: MOD Payload Customer Support

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2025-09-08
- **Updated:** 2025-09-18
- **Resolved:** 2025-09-18
- **Reporter:** Kurt Burian
- **Assignee:** Kurt Burian
- **Creator:** Kurt Burian
- **Links:** duplicates VXEP-1501 (Maim on VXE-30 Advanced Nav )
- **Sprint:** FS2 Sprint 34

## Description

Helping Jackson Curvin with a support requestKurt, the marines are trying to use trickster with their Advanced nav aircraft and here are some of the issues they are having. 
 ----
From Jackson Curvin:
 So we got the maim to update from v30000 to v30001 on the Trickster laptop. 
We are about to do the mag calibration and then reconnect and see if the trickster is getting gps. 
For the maim gui. I will not see the ahrs do anything bcs of the adv nav correct?
Maim is on the advanced nav stalker. Trickster is also connected. Siginter can see the Trickster in his system. I can see the stalker in the maim and have the maim heart beat. The maim AHRS is state is an X. (Edge is also suppose to reach out soon as well)  we tried updating the maim from v30000 to v30001, from the maim upload procedure that was on the Trickster laptop. (We moved all of the filed for the maim over to my gcs laptop for the stalker and installed everything. When I  click program on the Texas instrument, and reprogram on the maim, the text instrument sits on "connecting" and doesn't connect. In the maim, while the payload is on also, their are no watts being pushed and the trickster is getting gps. @Bowen Keith Schultz when hes available can talk more to what the Trickster portion.

## Comments (1)

### Kurt Burian, 2025-09-08

Customer did not have correct firmware/GUI. Seem concerned that upgrading will cause issues:

this is Nick from Motorola. I’m trying to help debug the issue with the Adv Nav aircraft. 
We have never integrated with that before. Mod payload has two ways of feeding INS stream, one is via Ethernet packets, and the second is via a binary data stream.
For firestorm we expect to see the binary data stream and PPS from the MAIM. My concern is that is different for this implementation. Do you know anything about that?

My Response:
The ethernet stream and binary stream are different yes, but its been made to mimic the AHRS output
so it should appear correct as if a Eclipse was supplying the data
I recommend upgrading to the latest firmware/GUI whether or not you are using advanced nav. Firmware, detects if a AHRS is present and configures itself accordingly

## Attachments (0)
