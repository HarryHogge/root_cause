# GCSS-77: D450+ Fuel Cell Control dialog Fan RPM Exceeds Upper Limit of Gauge

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2023-08-09
- **Updated:** 2024-01-31
- **Resolved:** 2024-01-31
- **Reporter:** Cody Smisek
- **Assignee:** Michael Berger
- **Creator:** Cody Smisek
- **Links:** relates to VXEP-26 (TPTR-96 Fan RPM shown incorrectly on GCS during fuel cell start up)
- **Sprint:** GCSS Sprint 6, GCSS Sprint 5, GCSS Sprint 8, GCSS Sprint 7
- **Part Number(s):** NA

## Description

D450+ FW now reports “actual output” for fan RPM. It was previously reporting ~1/3 the output (per @Sean Wendling )
When fan RPM exceeds 10,000 RPM, indicator remains at top of dialog in caution range.

## Comments (4)

### John Clark, 2023-08-10

@Craig Burton @Michael Berger please assign to the backlog and track here as well.

### Michael Berger, 2023-08-10

@Sean Wendling @Tom Westrich 
At this point the settings on some of the gauges change based on the FC type (first 2 digits of Serial number).
[embedded: image-20230810-171143.png]
what model is a D450+? is it 45?
What should the Yellow, Green, Yellow, MAX arcs be for a D450+

### Sam Miller, 2024-01-18

@Michael Berger Will the fix for the max RPM display be fixed in the upcoming release?

### Michael Berger, 2024-01-31

It should be in there for the next release

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| MicrosoftTeams-image (33).png | image | 398 | 2023-08-09 | listed only |
| image-20230810-171143.png | image | 140 | 2023-08-10 | listed only |
