# VXEP-1889: VXE 881 Nose Cone ripped free from Fuselage

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed, but added to Bermuda Triangle List
- **Resolution:** Cannot Reproduce
- **Priority:** Medium
- **Created:** 2026-05-13
- **Updated:** 2026-09-23
- **Resolved:** 2026-09-23
- **Reporter:** Drew Hildreth
- **Assignee:** Scott Lovett
- **Creator:** Drew Hildreth
- **Labels:** Hardware, RCCA, Weekly-incident-tracker
- **Links:** relates to RMA-1065 (VXE-881 RMA 260724-1)
- **Customer:** LRR
- **Vehicle Tail Number:** 881
- **Vehicle Configuration:** VXE-30 Advanced Nav Battery Configuration
- **Problem Type:** Discovered Issue
- **Incident Type:** Near Miss
- **Severity:** 1 - Flight Critical
- **Executive Summary:** Awaiting complete aircraft from customer. Probable cause Hardware.

## Description

Pending Operator Statement 

Nose cone and heat sink seemed to have all screws ripped free from the fuselage.

## Comments (6)

### Cody Smisek, 2026-05-27

For whoever looks at this when the statement comes in. Why is a forward prop sheared at the hub? When did that occur and was that the cause or the outcome of the upper fasteners ripping through the nose cone.

### Cody Smisek, 2026-05-27

[embedded: image-20260527-175256.png]

### Cody Smisek, 2026-05-27

@Scott Lovett Based on flight data (take a look at imu accels), I think a reasonable guess is that one of the three props separated during flight (photos show blade separation at hub). I’m of the opinion that the prop led to the nose cone damage, but I don’t know how we’d be able to determine order of events. I believe current software still doesn’t handle this event (supposed to have a fail safe where it will stop forward motor output for this exact issue). 
Logs indicate 51 cycles on the aircraft, current mx guidance is replacement of props at 50 cycles. Not seeing any indication of reset of mx interval in the logs (not 100% sure I’m interpreting that correctly though). I’m not sure we’ve really seen any prop separation on the 3 blade hub design. Previously on the 2 blade it was apparently a more common occurrence. And we’ve been running these real hard during B40/Havoc/X-Kit flights prior to swapping to a different blade design. 
So, maybe prior damage to that blade that wasn’t caught?

### Alexander Alan Arnold, 2026-08-10

aircraft in SLO awaiting RMA intake

### Mathew Papaleo, 2026-08-20

intake complete. blades were extremely tight upon arrival. the maint manual states; “over-tightened propeller screws may cause excessive vibration in flight if the individual blades cannot become “true” and track in the same propeller disc while in operation” @Cody Smisek. zac and lauren are working on the quote to get a new nosecone, and to repair the fuselage-- the receivers that retain the nosecone to the fuselage have been damaged. @Lauren Velasquez

### Mathew Papaleo, 2026-08-21

the fuselage has been repaired with a corresponding traveler, awaiting the nosecone and were done @Lauren Velasquez

## Attachments (20)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_V881_20260512T173822Z.zip | archive | 28019 | 2026-05-13 | listed only |
| Image (41).jpg | image | 276 | 2026-05-13 | listed only |
| Image (42).jpg | image | 488 | 2026-05-13 | listed only |
| Image (43).jpg | image | 676 | 2026-05-13 | listed only |
| Image (44).jpg | image | 599 | 2026-05-13 | listed only |
| Image (45).jpg | image | 330 | 2026-05-13 | listed only |
| Image (46).jpg | image | 409 | 2026-05-13 | listed only |
| Image (47).jpg | image | 518 | 2026-05-13 | listed only |
| image-20260527-175256.png | image | 114 | 2026-05-27 | listed only |
| IMG_5886.JPG | image | 3450 | 2026-08-20 | listed only |
| IMG_5890.JPG | image | 3991 | 2026-08-20 | listed only |
| IMG_5891.JPG | image | 4077 | 2026-08-20 | listed only |
| IMG_5892.JPG | image | 4062 | 2026-08-20 | listed only |
| IMG_5893.JPG | image | 4080 | 2026-08-20 | listed only |
| IMG_5895.JPG | image | 4410 | 2026-08-20 | listed only |
| IMG_5896.JPG | image | 4277 | 2026-08-20 | listed only |
| IMG_5897.JPG | image | 5146 | 2026-08-20 | listed only |
| [scan881.pdf](attachments/64196_scan881.pdf.md) | pdf | 6678 | 2026-08-20 | converted |
| [vxemaintenancelog.txt](attachments/64187_vxemaintenancelog.txt.md) | text | 2 | 2026-08-20 | converted |
| [lastpage.pdf](attachments/64244_lastpage.pdf.md) | pdf | 772 | 2026-08-21 | converted |
