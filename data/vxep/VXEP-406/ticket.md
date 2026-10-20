# VXEP-406: Secure the code that generates file system crypto keys (VTOL AP and X-Comm)

- **Issue type:** Sub-task
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Medium
- **Created:** 2024-05-07
- **Updated:** 2026-03-30
- **Resolved:** 2026-03-30
- **Reporter:** Ryan Ferguson
- **Assignee:** David Grosher
- **Creator:** Ryan Ferguson
- **Parent:** VXEP-405 VTOL autopilots and X-comms fail to generate full length crypto keys

## Description

The vehicle uses AES256 to encrypt the contents of the SD card on the VTOL autopilot and X-Comm.  This code has however been very insecure in production with most of the key being repeated between multiple autopilots.  This task requires an analysis to determine what generates the crypto keys and some code modifications to bring more randomness into the keys.  The code for this appears to be kept in EncryptDecrypt.c.
Below is an example key which would be used to encrypt the vehicles file system:
```
0xd01bebe8 0x14175c25 0xa3da2fe4 0xaa55aa55 0xaa55aa55 0xaa55aa55 0x1bd0255c 0x7e525b58
```
This above key came from autopilot APB-1-1126 which has a MAC address of e8:eb:1b:d0:25:5c
Key breakdown: 
Key 0:  0xd01bebe8 - This is an inverse of the first 4 parts of the MAC address.  This is insecure as the MAC address is broadcast over the network whenever the vehicle is powered.
Key 1:  0x14175c25 - The last 4 characters of this are the remainder of the MAC address.  The source of the first 4 characters in this key are an xor of the MAC address and 0xFF
Key 2:  0xa3da2fe4 - This key has come up one character short multiple times, driving fallout in production.  The source of this key is an xor of the MAC address and 0xFF
Key 3:  0xaa55aa55 - This is almost always aa55aa55.
Key 4:  0xaa55aa55 - This is almost always aa55aa55.
Key 5:  0xaa55aa55 - This is almost always aa55aa55.
Key 6:  0x1bd0255c - This appears to be driven by the reading of DEVSN0, the first part of the PIC processor’s SN.
Key 7:  0x7e525b58 - This appears to be driven by DEVSN1, the second part of the PIC processor’s SN.

Based on the above, if someone can get the SN of the processor and power it up to get a MAC address (no logging in necessary), our key has 52 characters of known values.  The remaining 12 characters may or may not be known, further investigation should be performed to figure this out.

Short keys
It also appears the code which drives the above keys is buggy.  For example, autopilot T-S101447 has a crypto key which is 1 character short.  Its mac address is 74:d5:c6:04:fa:04.  The key generated for this autopilot can be seen below:
```
0x4c6d574 0x2a8b04fa 0xfb05fb39 0xaa55aa55 0xaa55aa55 0xaa55aa55 0xc604fa04 0x7e7bf836
```
Based on the schema where MAC addresses drive the first key, the crypto key should be 0x04c6d574 but the leading 0 was never added to the string.  This is likely a logic error somewhere in the code.


UPDATE5/13/2024 - Kurt Burian was able to determine the source of the leading 0 being dropped.  The function which prints the key to the VTEV log file has a bug which dropped the 0.  This will be fixed in the upcoming release.  This does not however fix the security vulnerability identified in this ticket.  The PIC32 chip used in our autopilot has a PRNG function built-in however which should be able to generate sufficiently randomized keys for our cryptography.  I estimate the time needed for such a change would be minimal compared to some other projects currently in work.

## Comments (1)

### David Grosher, 2024-05-08

@Scott Whitney FYSA

## Attachments (0)
