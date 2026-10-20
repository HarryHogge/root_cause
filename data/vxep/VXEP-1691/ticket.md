# VXEP-1691: VXE-576 configured to wrong IP address in IPCOMM web page

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** High
- **Created:** 2026-02-03
- **Updated:** 2026-08-10
- **Resolved:** 2026-08-10
- **Reporter:** Michael Mohr
- **Assignee:** David Grosher
- **Creator:** Michael Mohr
- **Labels:** Software, TIQUILA
- **Links:** relates to VXEP-1698 (NCR: IPCOMM Failures)
- **Issue color:** teal
- **Asset type:** VXE-30 MAGNSS
- **Customer:** TIQUILA
- **Vehicle Tail Number:** VXE-576
- **Severity:** 2 - Degraded Performance - No Workaround
- **Impacted Disciplines:** Software
- **Program (Marquee):** TIQUILA

## Description

Aircraft VXE-576 has wrong IP address in IPCOMM page. SA camera and Trillium are failing to load.

## Vehicle Configuration

VXE-30
Battery

## Comments (6)

### Scott Lovett, 2026-02-17

@David Grosher I was working a tangential issue with Jack and the topic of the mis-configured IP addresses came up, so I took a stab at investigating the broken flow. Here’s what I found (keep in mind that I really don’t know the SW like you guys do)…
How I think the flow should work: The AP sends an XCOMM_APSET message containing the vehicle serial number. XCOMM receives it, derives an IP address, and broadcasts the tail number to IPCOMM via the NetworkMetaLink metadata packet. IPCOMM then uses that to create and push IP addresses to the system.
What I think is broken: During some changes, the JAI protocol files, including hostintf.cpp which contained SendApSet(), were deleted and never replaced. SendApSet() is the only function that generates the XCOMM_APSET message carrying the serial number to XCOMM.
I’ve chased the suspected changes to the following GIT commits:
- Root cause commit: 83091b91- "Working UAP in 4.72 based code" (2025-09-04) deleted hostintf.cpp, hostintf.h, and target.h, and commented out the HostInterface instantiation in ap_proto.cpp.

- Propagation commit: 75d6250e- "Merge UAP changes from 4.72 branch into 4.74" (2025-12-10) merged the deletion into the B40 4.74 UAP dev branch.

Affected branches: feature/B40_4.74_UAP_Dev, feature/4.74_UAP_Dev, and downstream UAP branches. Main still has the files but BUILD_JAI=0, so they were never compiled there either.
Where I think the fix needs to happen:
- AP firmware (primary fix): Port SendApSet() to send XCOMM_APSET over the new CAN-based unified link path. The old JAI serial path was removed but nothing replaced it.

- XCOMM fallback (secondary fix): XCommControl.cpp lines 1385-1388 have a fallback that sets VehicleSN from the config file tail number, but it doesn't call configSaveIpSettings(), so the IP address never actually gets updated or pushed to IPCOMM. Adding that call would at least allow the config-stored tail number to drive IP assignment as a safety net.

### David Grosher, 2026-02-17

@Kurt Burian Can you review these PRs and Scott’s hypothesis? @Scott Lovett @Scott Whitney FYSA

### David Grosher, 2026-02-17

@Kurt Burian @Scott Lovett The UAP branches haven’t been released and are not part of the current release, v6.6.1 where the issue was observed. Further, if the only function that resulted in the configuration of the IP address on IPCOMM was deleted then this issue would have been caught in testing as it would have failed every time.

### Kurt Burian, 2026-02-27

@David Grosher @Scott Lovett Sorry I just noticed this. I IPCOMM uses the discovery broadcast message, same as the legacy GCS, for picking up tail numbers. I wiresharked it and the packet was getting sent at the correct 5 second interval with the correct tail number. 


```
struct CDiscover
{
        unsigned short ownership;
        unsigned short owner_id;


        unsigned char ip[4];
        unsigned char hostip[4];


        unsigned long Options;


        unsigned long treceive;
        unsigned long age;


        short vbatt;
        unsigned short spare;


        struct PayloadMetaVehicle pmv;
        struct PayloadMetaGps pmg;


        unsigned short crc;
};
```
```
struct PayloadMetaVehicle
{
  // ascii length = 29
  unsigned char Type;		// meta type bit				csv: N,
  unsigned char Length;		// length of this structure in bytes	csv: 0,
  short Airspeed;		// TAS in fps, 0.1 fps / count	csv: 123.4,
  short AGL;			// current agl in feet			csv: +12345,
  unsigned short State;		// bitmapped, per above			csv: 65535,
  unsigned short TailNumber;	// vehicle tail number		csv: 65535,
};
```

### Drew Hildreth, 2026-08-10

Customer had swapped radios with another aircraft.

### Alexander Alan Arnold, 2026-08-10

IP comm issue still exist but this specific VXEP was a separate radio (not 576) was installed and the IP comm failing to update is why they saw the wrong IPcomm

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| IP calc.jpg | image | 173 | 2026-02-03 | listed only |
| IPCOMM.jpg | image | 3938 | 2026-02-03 | listed only |
| Trillium.jpg | image | 2995 | 2026-02-03 | listed only |
| XCOMM.jpg | image | 106 | 2026-02-03 | listed only |
