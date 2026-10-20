# FS2-4887: VXE-1040 XCOMM SD Card Corrupted

- **Issue type:** Task
- **Status:** In Review
- **Priority:** Medium
- **Created:** 2026-07-21
- **Updated:** 2026-07-21
- **Reporter:** Scott Whitney
- **Assignee:** Scott Whitney
- **Creator:** Scott Whitney
- **Links:** relates to VXEP-1943 (VXE-1022 auto aborted VTOL launch at the pause. No XCOMM logs in the AAR.)

## Description

Corrupt SD Issue on v1040
Issue Background: 2026-07-20 v1040 was in SCO for JST checkout. Vehicle was on firmware 6.8.0rc03 which has a known issue, where an Empty Power Event will Zeroize the avionics. SCO attempted to roll back firmware to 6.7.0 for checkout and flights, but was unable to update XCOMM or Fixed Wing

Trouble shooting steps taken:
- Attempt to update FWAP using 6.7.0 (internal) JGCS - Failed to update
- Attempt to update VTOL AP using 6.7.0 (internal) JGCS - successfully updated
- Attempted to log into XCOMM Webpages using Start Webpage script x10+ - Unable to connect to XCOMM webpage
- Power Cycled Vehicle - attempt to connect to webpage - ran script x20+ - unable to connect
- Disconnected VSM from AP - unable to run or connect to webpage
- Connect vehicle to JGCS - Prompted “Avionics SD Card needs to be reformatted”
- Attempt to Reformat XCOMM SD Card - FAILED to reformat
- Attempt to connect to XCOMM webpage with script x20+ - finally starts webpage
- XCOMM webpage shows signs of SD card corruption
- Main page shows memory in ROM (not SD)
- Log files page will not load
- Attempt to reformat SD from Webpages - FAIILED to reformat

NOTE: This process was attempted a few more times without any additional success.

## Plan

NCR to Replace XCOMM SD Card: https://jenaero.sharepoint.com/sites/JAI_Operations/Lists/NCR%20List/DispForm.aspx?ID=10625&commentId=1&e=guDJaintpUiTSy4yVs43nw&at=15&xsdata=MDV8MDJ8c3doaXRuZXlAZWRnZWF1dG9ub215LmlvfDMwZmI3MWVmMTM5NDRiMjFhNjc5MDhkZWU2YmUwZWVlfDE4NzZmNjFhM2JkYjQ4NDNhZTcwNzVlZDBjY2I3NDA0fDB8MHw2MzkyMDE5MDExMjQ3MjU4NzR8VW5rbm93bnxUV0ZwYkdac2IzZDhleUpGYlhCMGVVMWhjR2tpT25SeWRXVXNJbFlpT2lJd0xqQXVNREF3TUNJc0lsQWlPaUpYYVc0ek1pSXNJa0ZPSWpvaVRXRnBiQ0lzSWxkVUlqb3lmUT09fDB8fHw%3D&sdata=ZDlsQWNpcS9yRzcvQnNLdXJsYk0wVnkyOHNCUE5aMlpwVEQ2N25FNHlMaz0%3D&CT=1784650147431&OR=OWA-NT-Mail&CID=962dfa00-fda1-dc9a-7e89-14257e3e5a55&SI=NonSentItems&clickParams=eyJYLUFwcE5hbWUiOiJNaWNyb3NvZnQgT3V0bG9vayBXZWIgQXBwIiwiWC1BcHBWZXJzaW9uIjoiMjAyNjA3MTAwMTMuMTIiLCJPUyI6IldpbmRvd3MgMTEifQ%3D%3D&SLSync=N

## Comments (0)

## Attachments (0)
