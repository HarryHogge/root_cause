# VXEP-525: VXE 300 - MCM v1.0 failure to take off

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-08-05
- **Updated:** 2024-08-23
- **Resolved:** 2024-08-23
- **Reporter:** Scott Whitney
- **Assignee:** David Grosher
- **Creator:** Scott Whitney
- **Links:** relates to MS-364 (v300 Mechanical Damage and Repair Assessment ); relates to MS-365 (v300 Electrical Damage and Repair Assessment ); relates to VXEP-526 (DUPLICATE ISSUE - DELETE WHEN CONVENIENT)
- **Corrective Action:** See above
- **Production Stakeholder:** Desiray Johnston
- **Severity:** 1 - Flight Critical

## Issue Status

Today in the attempt to do a “Launch Abort” test the vehicle failed its take-off and flipped upside down, braking:
- Nosecone
- FWD props
- Front lift blade props
- Tail boom
- Right wingtip (mostly cosmetic and shear in the Kevlar)

When fixing it, (even though the rear lift blades are intact) I do ask to replace all Motors/ESCS since the motors were stopped by impact and not the system disarming, so I wouldn’t trust them for future use.
 
There’s a good reason to believe that the legacy GCS software would have detected a failure of this sort during launch wizard, as well as aborted the take-off detecting unusual angles.
 
3 items added to “Flight Critical” issues after today:
- Launch wizard doing all the background checks that the old GCS software did and not allowing to proceed if something fails
- Launch mode being able to detect a failure and abort the take-off
- And per Dave’s request – VSI continuing to send the LI commands every 5 seconds (might cause a drift away problem if the LI is commanded during a vertical flight phase)



It looks like the pitch estimate was way off. Which explains the flip on launch. 
[embedded: image-20240805-185735.png]
The actual launch event didn't get into the log. But that was the estimate up to 10 seconds prior to the VTOL event log cutting out, which does capture the launch event. 
It also appears that the only valid status bit for GPS was GPS time.

## Root Cause

- VTOL AP had the sensor Task blocked and GPSParse task hung on the I2C2 bus. The coupling of the tasks has already been fixed in the 6.3 release. There is still a path for the I2C bus to hang on initialization https://jenaero.atlassian.net/browse/FS2-2142 https://jenaero.atlassian.net/browse/FS2-2143  and a fix for this will be provided in 6.4 along with a change of when the RTC will be allowed to be updated (only after landing) https://jenaero.atlassian.net/browse/FS2-2141 .
- The OGCS failed to prevent launch when issues were detected on the AP itself. A series of critical issues and fixes have been implemented in the v1.0 release of the VSM and OGCS to address this. There are still a few checks that can’t be implemented without changes to the XCOMM to provide additional data to the VSM.  There are too many issues in the MS project to link here.

## Comments (1)

### Cameron Chapman, 2024-08-05

info from duplicate issue that will be closed. 

**Cameron Chapman 2 seconds ago**

@Matt Philley I will do what I recommended below and close this one. Thank you for reporting.
Edit·Delete·
**Matthew Philley 2 minutes ago**

@Cameron Chapman whoops! you are right. Scott and I talked about making one this morning but I didnt think he got to it yet lets keep with the his since it was first
**Cameron Chapman 3 minutes ago**

@Scott Whitney @Matt Philley we seem to have some duplication. I think https://jenaero.atlassian.net/browse/VXEP-525 duplicates this issue. This issue is the correct issue type, but https://jenaero.atlassian.net/browse/VXEP-525 has more information. I recommend changing https://jenaero.atlassian.net/browse/VXEP-525 to an incident, moving info from this one to that, then close this one as a duplicate.
Edit·Delete·
**Matthew Philley 6 minutes ago**

@Greg Fryer @Scott Whitney @Ryan Babigian @Artis Bertulis AC 300 incident ticket created to track the resolution.
AC 300 is still the only flyable asset with MCM only, so it is needed in order to complete MCM Software Regression Testing which is a gating activity for PreMAGNSS and MAGNSS.
It is not clear the path to get the asset flyable again, but sounds like it needs a Mechanical and Electrical checkout at a minimum to determine the extent of the damage.
 
@Artis Bertulis @Ruysser Gabler if yall have any photos/videos or documentation please attach or link here.

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V300_240801_084723_pack.zip | archive | 14521 | 2024-08-05 | listed only |
| image-20240805-185735.png | image | 22 | 2024-08-05 | listed only |
