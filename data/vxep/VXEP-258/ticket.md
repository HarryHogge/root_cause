# VXEP-258: Potting concerns. DP100 may be too viscous or cure too fast to properly wick between ODU solder cups.

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-01-24
- **Updated:** 2025-06-10
- **Resolved:** 2025-06-10
- **Reporter:** Cameron Chapman
- **Assignee:** Matt Philley
- **Creator:** Cameron Chapman
- **Links:** relates to VXEP-440 (Add Loctite 262 to Drawings/BOMs with ODU Backshells - Deviation); relates to VXEP-286 (VXE 603 HLB Data Connector Shorted. Evaluate equipment. )
- **Production Stakeholder:** Emalee Johnson
- **Supply Chain Stakeholder:** Victor Vandor
- **Other Stakeholder (as required):** Mark Squillante
- **Severity:** 1 - Flight Critical

## Description

one backshell broke off with wires. I suspect DP100 is too viscous or cures too fast to properly wick between ODU solder cups. It could also be that one instance DP100 was applied after the recommended window.
https://jenaero.sharepoint.com/sites/JAI_Operations/Lists/NCR%20List/DispForm.aspx?ID=2321&commentId=1&e=trrIlTPHy0KNMuTuixGm3g&at=15 
https://jenaero.sharepoint.com/sites/JAI_Operations/Lists/NCR%20List/DispForm.aspx?ID=2308&commentId=2&e=x7Tahf4bME6ZVwOUde-p3Q&at=15 
https://jenaero.sharepoint.com/sites/JAI_Operations/Lists/NCR%20List/DispForm.aspx?ID=2309&commentId=3&e=b23ps2znOECJQpF8u37ITA&at=15 
[embedded: image-20240124-233250.png]

File location: https://jenaero.sharepoint.com/:f:/r/sites/EngineeringTeam/Shared%20Documents/Investigations/DP100%20ODU%20potting%20issue?csf=1&web=1&e=7VV4Us 
Test Report: DP100 ODU Detailed Investigation Report.docx

## Corrective Action

- Make links to track each of the below tasks.
- Consider Switch to a potting compound with longer working life such as EA-E20 or EA-E60, or pot ODU connectors in smaller batches to ensure completion before curing.
- (ODU uses DP100 on the cables they build, so the compound should be acceptable if applied correctly)
- Investigate alternate application methods
- Shorten application window. See test report. Approximately < 3 minutes.
- Consider field test for testing backshell looseness. That seems to be a good indicator of potting not fully wicking.
- Implement in process inspection of potting applications, limit work time of component.
- Apply Loctite 262 to connector/backshell threads
- Evaluate switching to ODU crimped band vs Bandit. New tooling, maybe more reliable, price savings per connector.

## Plan

- gauge the severity by potting some wired ODU connectors with DP100 at the beginning of its application window, at the end, some time after, then inspecting the solder cups once cured. Pot from the top of the backshell to see if it wicks down. @Mark Squillante

[embedded: obsolete 115-105407-B1 Branch Cable.pdf]

## Issue Status

Investigation complete: https://jenaero.sharepoint.com/:f:/r/sites/EngineeringTeam/Shared%20Documents/Investigations/DP100%20ODU%20potting%20issue?csf=1&web=1&e=7VV4Us

Potting completed at 1.5 minute intervals. 4x potted at top of cavity, 4x potted at base of cavity. 
- The backshell of the last connector potted at top of cavity (4.5 minutes into potting compound’s worklife) can be unscrewed by hand
- All other backshells unable to be unscrewed by hand
- 3 minutes after mixed DP100 still flows to bottom of ODU regardless of whether applied at top or bottom of cavity
- More than 3 minutes after mixing exhibits poor flow, does not reach base of ODU
- Whether using shorter or longer mixing nozzle seems to make no difference

## Root Cause

- DP100 cures quickly to do large batches of ODUs, resulting in poor flow/wicking between solder cups.
- No in process inspections for potting.
- No controls/procedure checking working life of potting compound, applying potting compound at the bottom of the cup, etc.
- Reports of improper potting techniques (reusing mixing tips, not tracking mix time, etc).
- Working life listing on spec sheet (5 min) of potting compound is longer than the tested applicable window (<3 .5 min).

## Comments (5)

### Mark Squillante, 2024-01-25

Soldered wires and potted backshells with DP100 qty: 4 ODU connectors (100-103070). Applied potting compound to top of cavity and allowed to flow down. Potted at 1.5 minute intervals (right away, 1.5 minutes, 3 minutes, 4.5 minutes into working life).

Also repeated with another 4 connectors but applied potting compound to bottom of cavity and allowing to fill upward, same time intervals.

Initial observations are applying DP100 to top of cavity causes air to get trapped underneath, also at 4.5 minutes into work life it is already cured enough to make it extremely difficult to use (nozzle broke from applying too much pressure)

Will disassemble them after curing overnight and compare results.

### Mark Squillante, 2024-01-26

here are pictures of the one where the backshell was able to be unscrewed by hand. Potting was applied at top of cavity about 4 minutes 30 seconds after mixed in nozzle. This was after fully unscrewing backshell. Wires twisted with backshell but didn't break
[embedded: IMG_0628 marked up.jpg]
[embedded: IMG_0629 marked up.jpg]

### Mark Squillante, 2024-01-26

3 minutes after DP100 is mixed still shows good flow to bottom of ODU regardless of whether applied at top or bottom of cavity, but 4 minutes 30 seconds after mixing shows poor flow.
DP100 applied at bottom of cavity 4 minutes 30 seconds after mixed: 
[embedded: Bottom 4.5 min after mix 1.jpg]
[embedded: Bottom 4.5 min after mix 2.jpg]
[embedded: Bottom 4.5 min after mix 3.jpg]

DP100 applied at bottom of cavity 3 minutes after mixed: 
[embedded: Bottom 3 min after mix 1.jpg]
[embedded: Bottom 3 min after mix 2.jpg]
[embedded: Bottom 3 min after mix 3.jpg]

DP100 applied at top of cavity 3 minutes after mixed:
[embedded: Top 3 min after mix 1.jpg]
[embedded: Top 3 min after mix 3.jpg]
[embedded: Top 3 min after mix 2.jpg]

### Mark Squillante, 2024-01-29

Investigation report completed. See link in Description or Investigation Status fields.

### Matt Philley, 2024-02-09

Added link to https://jenaero.atlassian.net/browse/ENG-2530 to cover the urgent implementation of Loctite on the backshells under deviation I am working on with @Emalee Johnson

## Attachments (13)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20240124-233250.png | image | 70 | 2024-01-24 | listed only |
| [obsolete 115-105407-B1 Branch Cable.pdf](attachments/18495_obsolete%20115-105407-B1%20Branch%20Cable.pdf.md) | pdf | 388 | 2024-01-24 | converted |
| Bottom 3 min after mix 1.jpg | image | 7339 | 2024-01-26 | listed only |
| Bottom 3 min after mix 2.jpg | image | 6779 | 2024-01-26 | listed only |
| Bottom 3 min after mix 3.jpg | image | 6754 | 2024-01-26 | listed only |
| Bottom 4.5 min after mix 1.jpg | image | 6865 | 2024-01-26 | listed only |
| Bottom 4.5 min after mix 2.jpg | image | 6616 | 2024-01-26 | listed only |
| Bottom 4.5 min after mix 3.jpg | image | 7093 | 2024-01-26 | listed only |
| IMG_0628 marked up.jpg | image | 220 | 2024-01-26 | listed only |
| IMG_0629 marked up.jpg | image | 169 | 2024-01-26 | listed only |
| Top 3 min after mix 1.jpg | image | 6954 | 2024-01-26 | listed only |
| Top 3 min after mix 2.jpg | image | 6924 | 2024-01-26 | listed only |
| Top 3 min after mix 3.jpg | image | 6693 | 2024-01-26 | listed only |
