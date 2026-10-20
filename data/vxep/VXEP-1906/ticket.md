# VXEP-1906: VXE-845 GPS error on Launch Abort

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2026-06-05
- **Updated:** 2026-10-16
- **Resolved:** 2026-06-30
- **Reporter:** Jackson Riley Curvin
- **Assignee:** Scott Lovett
- **Creator:** Jackson Riley Curvin
- **Labels:** External, Hardware, No_crash, RCCA, Weekly-incident-tracker
- **Customer:** PMA263
- **Vehicle Tail Number:** VXE-845
- **Vehicle Configuration:** VXE-30 Standard Main Battery
- **Problem Type:** Discovered Issue
- **Root Cause:** exceeded GPS threshold on launch
- **Severity:** 3 - Degraded Performance - With Workaround
- **Executive Summary:** After investigation it is concluded that this is a training issue, the wrong freqs were used.

## Description

Upon transition a VTOL error appeared and the aircraft auto aborted Link to data is here: https://jenaero.sharepoint.com/:f:/s/GlobalSupport2/IgCAOVAMTtdTSoYBw1kv9MF0AUMb26iIjonPlOHrqNjWJa4?e=PG7sBN

## Comments (7)

### Cody Smisek, 2026-06-05

Exceeded accuracy thresholds during launch.
Would help to have entire VTOL logs (for history of system) given they’ve already provided all XCOMM. Follow on questions, is this a 1 off event (could be determined via full VTOL log set)? Any reason to believe GNSS issues in the area of the flight? 
If 1 off event, try again.
[embedded image-20260605-170948.png]
[embedded image-20260605-165654.png]

### Jackson Riley Curvin, 2026-06-05

@Cody Smisek I believe this is the AAR from this incident.

### Cody Smisek, 2026-06-05

@Jackson Riley Curvin Yeah, already reviewed and charts below are from that. Someone pulled all of the xcomm logs via FTP. Doing the same for VTOL would help as we could then do a batch review of all flights to determine frequency of this issue.

### Jackson Riley Curvin, 2026-06-05

@Cody Smisek I was the one to pull the data on the XCOMM but i dont know where the VTOL data went but i was able to get all the AARs for 845 that was on the gcs from this incident and i put them here "\\condor\Engineering\AARS_ALL\FlightsByTailNumber\V845"

### Cody Smisek, 2026-06-05

@Wesley Lilienthal I’m told that @Abel J. Markow was out with the customer during this timeframe. Do we have a write up on what we found with regard to spectrum analysis that were performed? Please attach here.

### Wesley Lilienthal, 2026-06-10

@Cody Smisek - There was very little time to operate the analyzer, and no GNSS-band analysis was performed to my knowledge. @Abel J. Markow can confirm or clarify.

### Jackson Riley Curvin, 2026-06-30

Aircraft performed as expected.

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V845_260326_234714_pack.zip | archive | 1451 | 2026-06-05 | listed only |
| image-20260605-165654.png | image | 199 | 2026-06-05 | listed only |
| image-20260605-170948.png | image | 8 | 2026-06-05 | listed only |
| [AIR PMO Multiple Vehicle Investigation Report_20260709.pdf](attachments/63402_AIR%20PMO%20Multiple%20Vehicle%20Investigation%20Report_20260709.pdf.md) | pdf | 1142 | 2026-07-09 | converted |
