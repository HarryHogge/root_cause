# VXEP-1981: VXE 1003 Erroneous Fuel Level Report after LW Reset

- **Issue type:** Incident (8D)
- **Status:** D4 - Investigating Root Cause
- **Priority:** High
- **Created:** 2026-08-20
- **Updated:** 2026-10-12
- **Reporter:** Zachary Mann
- **Assignee:** David Grosher
- **Creator:** Zachary Mann
- **Labels:** Software
- **Links:** relates to XKIT-5429 (OGCS 1.4.1 Dev07 Shows 11160g fuel remaining on initial power on of aircraft); relates to FS2-5043 (Investigation: VXE 1003 - FC Fuel Report )
- **Customer:** Redwire
- **Vehicle Tail Number:** 1003
- **Vehicle Configuration:** VXE30 ADV NAV, Fuel Cell, OGCS, E140
- **Problem Type:** Other (explain in description)
- **Incident Type:** Mission Failure/Abort
- **Severity:** 3 - Degraded Performance - With Workaround
- **Executive Summary:** OGCS Incorrectly Displaying Propane Tank Weight

## Description

The vehicle was powered up and fuel cell connected, it started out reporting 24.520kg of fuel, then the operator manually entered 970g and started it, which it reported for the next ~3mins. The vehicle was restarted and it reported 4.04kg of fuel without any operator input and continued to report that.

## Comments (10)

### Zachary Mann, 2026-08-20

This was from Ted: “Yeah I think we need to investigate across fuel cell and flight system groups”

### David Grosher, 2026-08-20

@Ted Trowbridge Can you take a look at this?

### Ted Trowbridge, 2026-08-20

@David Grosher I took a look and from the logs it seems like there may be an issue with the fuel cell firmware, or perhaps XCOMM.
Based on the VSM and OGCS logs:
- Vehicle was powered up with a few cell connected, it immediately reported 24,520grams of fuel.  This seems like an issue - why didn’t it report 0?
- The operator manually entered 970grams, this was accepted and the fuel cell reported 970 for the next ~3 minutes.
- The vehicle appears to have been restarted (or at least the MCM was) and the next report showed 4040 grams of fuel.  There was no operator input and the value never changed after that.

@Craig Burton for SA

### David Grosher, 2026-08-21

@Scott Whitney Can we have someone on the embedded side look into this?

### Levi Purdy, 2026-08-24

After an investigation it doesn’t look like xcomm was confused about the fuel remaining, and the error only shows momentarily after vsm resets.

Best hypothesis I have is an uninitialized variable picking up some junk

Fix:
https://bitbucket.org/edgeautonomy/vsm/pull-requests/616/ 

Not sure how to test this

### Scott Whitney, 2026-08-24

FYSA @David Grosher

### David Grosher, 2026-08-24

@Levi Purdy Were we able to successfully isolate the issue to the VSM? Given we can’t readily test the update, it seems like we should document how the issue was isolated to the VSM and impacted code.

### Levi Purdy, 2026-08-28

@David Grosher After many rounds of investigating I’m pretty sure this is isolated to the VSM, because the VSM doesn’t currently consume the initial fuel system state from the embedded side. 
[embedded image-20260828-205730.png]
VSM appears to construct its own fuel remaining status from a user entered initial fuel and then a GBurn rate. 

The errant values don’t occur in the xcomm datalogs. 

We probably need a revisit of https://jenaero.atlassian.net/browse/FS2-3497  and an audit of how the fuel system works for a full fix. The temporary fix is just to init the inital fuel correctly, as my PR does. 

See the attached .zip for the full investigation notes
[embedded file]

### Zachary Mann, 2026-10-07

@Levi Purdy the link you provided is broken; is that something to download and test on the A/C?

### Levi Purdy, 2026-10-12

It isn’t broken, but it is just a PR into the codebase required for the fix. Fair enough, that probably isn’t useful to you. I will follow up with Craig to get this into his codebase and try to get you a new VSM image.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_V1003_B30N_20260819T181011Z - Copy.zip | archive | 10695 | 2026-08-20 | listed only |
| fs2-5043-vxe1003-review-bundle.zip | archive | 1687 | 2026-08-28 | listed only |
| image-20260828-205730.png | image | 116 | 2026-08-28 | listed only |
