# new_adp_software_integration.docx

Attachment 33361, docx, 15 KB, added 2025-10-28 by Kurt Burian.

## New ADP – Software Changes

The new ADP uses a different encoder than its predecessor. The new encoder features a EO and IR mode sent over a single stream. To support this camera, video client integrators will first need to determine if their end target is a New or a Legacy pod to determine the correct stream URL.

Detecting Pod Type

The new ADP pod uses a Sightline 1750 encoder, which supports the SLA discovery protocol. After waiting ~60 seconds for the encoder to boot, the client should send a UDP packet to port 51000 and check for a response. If no response is received, it can be assumed a legacy pod is installed. If a valid sightline response is received with the correct encoder type at the predicted IP, the end device is a new ADP.

Sightline Discovery Protocol Details

SightLine Applications Command, Control, and Script API: SightLine Discover Protocol

The RTSP url for the new ADP is: rtsp://<camera-ip>/net0

Switching Imager

The EO/IR imager is toggled by sending the 0xA4 message, SLAVideoDisplay_t.

Camera Index selects between EO and IR

Camera Index 0: IR

Camera Index 1: EO

Destination should be set to Network 0, 0x0002.
