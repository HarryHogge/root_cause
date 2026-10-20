# VXEP-1908: VXE 850 had a VTOL auto abort after coming down at approximately 100 feet. A/C crashed into the river and has not been recovered.

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2026-06-08
- **Updated:** 2026-08-18
- **Resolved:** 2026-08-10
- **Reporter:** Stephan Johnson
- **Creator:** Stephan Johnson
- **Labels:** GS_Closed, Hardware, MARSOC, RCCA, Training, Weekly-incident-tracker
- **Customer:** MARSOC
- **Vehicle Tail Number:** VXE 850
- **Severity:** 1 - Flight Critical

## Description

Customer had a VTOL auto abort after coming down at approximately 100 feet. A/C wouldn’t transition to VTOL again, either in the PLZ or when selecting land immediately. Customer tried landing at the PLZ 4 more times. Each time it would blow through the transition point after IP5 with no errors or pop-ups. Customer also restarted the GCS, created a new mission, and checked his ELZ/PLZ selection. GS advised the customer to try the PLZ landing a couple more times to no avail. GS advised the customer to attempt to U-drive the plane to the PLZ and do a land immediately. The plane did not acknowledge the land immediately command. A/C went down after it sounded like they had it in a bank and lost comms. A/C has not been recovered yet, but unit will get us data once the A/C has been recovered.
```

```

## Root Cause

Unable to identify because aircraft has not been recovered

Operators did not set an ELZ to recover vehicle

## Comments (5)

### Cody Smisek, 2026-06-09

It seems like AP aborted VTOL landings should not be followed up with an attempt to continue to land the aircraft via VTOL. May want to consider recommended guidance be glide landings when seeing this behavior.

### Drew Hildreth, 2026-06-10

@Cody Smisek That recommendation was given, however they responded that they didn’t have enough room to conduct that safely.

### Scott Lovett, 2026-07-06

Aircraft never found.

### Scott Lovett, 2026-07-06

No AIRFRAFT OR DATA

### Alexander Alan Arnold, 2026-08-10

closed

## Attachments (0)
