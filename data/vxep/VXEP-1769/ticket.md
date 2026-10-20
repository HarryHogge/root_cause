# VXEP-1769: VXE 508 Comms Failure in flight

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** High
- **Created:** 2026-03-09
- **Updated:** 2026-03-17
- **Resolved:** 2026-03-17
- **Reporter:** Alexander Alan Arnold
- **Assignee:** David Grosher
- **Creator:** Alexander Alan Arnold
- **Labels:** FBI, RCCA, Weekly-incident-tracker
- **Vehicle Tail Number:** 508
- **Vehicle Configuration:** VXE 508 Octopus MWIR
- **Severity:** 1 - Flight Critical

## Description

Operator Statement

During an operational flight last night we had a complete comms failure on our stalker. At the time of the failure the bird had been up for 1 - 1.5 hours with no anomolies to the bird, however it was flying an MWIR payload and the video was very "jerky" (not smooth) however the video was not showing any loss of link. 
 We were using an SC4200 connected to mag mount antennas and battery powered via S band. 20000 max link and 20 mhz bandwith were our settings. Initially it was only that one radio and the bird but as the link loss troubleshooting progressed we brought up a 2nd 4200 with "bendy" antennas. 
 With no other observed anomolies we got a signal degradation message on the GCS. We verified a complete link loss by green flashing light on the SC4200.
 We immediately brought up a 2nd 4200 which we plugged into the GCS replacing the first. As expected both 4200's link lights went solid. Checking within streamcaster we saw all 3 nodes (2 ground, 1 UAV) connected. The UAV was pushing approximately 6 MB of data. We could see video via epsilon but the GCS would still not connect. We swapped to a 2nd GCS which also would not connect but did indicate that the bird was connected by another GCS.  Both GCSes prepopulated the correct tail number indicating to me it could see something on the network. We tried disconnecting from the bird on GCS 1 to do a "handoff" but even after the disconnect GCS 2 would not connect. GCS 1 could not re-connect after disconnect.
 The bird executed its loss comms procedure and landed. Once on the ground, prior to any power cycling we attempt to connect to the bird which was sitting within 400 feet of the GCS but it failed to connect. We exited GCS software, rebooted the computer and all attempts failed to connect. We power cycled the bird, still no connection. We pulled the MWIR and power cycled again, still no connection. We verified that the bird was still seen within streamcaster, which it was.
 This morning we hooked the bird back up to power, utilized the same GCS and same radio as last night and it connected fine and dumped the FDR which i'm sending via teleporter.
 I did note that at one point with epsilon shut down the bird was still pushing 6 MB which I would not expect if the video was not being consumed.

## Comments (3)

### David Grosher, 2026-03-17

@Alexander Alan Arnold This is unrelated to our other issues. You can close this ticket per your other support in the field.

### Alexander Alan Arnold, 2026-03-17

Spoke with customer, user had WIFI enabled, and traffic on wrong port

### Alexander Alan Arnold, 2026-03-17

customer issue

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V508_260225_113804_pack.zip | archive | 2691 | 2026-03-09 | listed only |
