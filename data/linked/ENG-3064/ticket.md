# ENG-3064: TPTR-55 Fuel Cell Fault SN D4500249 /247

- **Issue type:** Problem
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2023-06-28
- **Updated:** 2025-06-02
- **Resolved:** 2025-05-21
- **Reporter:** Daniel Lloyd
- **Assignee:** Robert Redfield
- **Creator:** Daniel Lloyd
- **Labels:** Jun2023Incident
- **Links:** relates to VXEP-22 (TPTR-55 Fuel Cell Failure Immediately after launch)

## Description

Aircraft 510 had a fuel cell fault during the launch wizard. Operators report that they cycled power on the fuel cell to clear the error. After launch the fuel cell errored again and the aircraft was landed. Fuel cell S/N 4006249. Error code 19472.

## Comments (17)

### Tom Westrich, 2023-06-29

@Robert Redfield , can you please take a look at this data and see if we need to issue an RMA?  Based on the description of FC history, it sounds like a high reactor temperature fault condition occurs frequently, but not persistently over the previous several cycles.

### Daniel Lloyd, 2023-06-29

I uploaded all the logs from 242 and 249. Perhaps you can find a trend.
@Tom Westrich

### Sam Miller, 2023-07-10

@Tom Westrich @Robert Redfield , can you please provide status on this?  Our TIQUILA customer asked about this today in our call.

### Robert Redfield, 2023-07-11

Hello all,  
Based on the data, I am able to see an elevated Reactor Temperature. However when I look at our cycle data I can see a definite spike in temperatures during Cycle number 7.  Something significant happened between cycles 6 & 7.  
Our stack performance is still good.  I can also verify all system components as being operational.  
I want to issue an RMA for this fuel cell so that I can examine some of the likely root causes for this failure mode; notably the Fuel FMS, Cathode Interface, & the stack Heat Exchanger.

[embedded: image-20230711-120940.png]

### Greg Fryer, 2023-07-13

@Robert Redfield Please reach out to @Sean Odell and @Pat Wells  to engage on the RMA front. They will be able to coordinate.

### Robert Redfield, 2023-07-14

As system D4500242 was behaving in a similar manner I have added it to the list.  attached you should find (2) RMA support tickets for these fuel cells.  (D4500249 & D4500242)
Once these get back to the shop we can begin failure analysis to determine root cause and repair actions.

### Pat Wells, 2023-08-03

@Daniel Lloyd do you still have possesion of fuel cell S/N 4006249?

### Sam Miller, 2023-08-03

For everyone’s SA, this should not be a pacing item for TIQUILA FAT.  This fuel cell is not a TIQUILA deliverable.

### Daniel Lloyd, 2023-08-03

@Pat Wells I’m checking with Jeff to see where it went. It’s not with me.

### Pat Wells, 2023-08-03

@Daniel Lloyd because this fuel cell is not a TIQUILA deliverable is there anything else holding up 510?  Assuming you have that aircraft.

### Daniel Lloyd, 2023-08-03

I don’t think there is anything wrong with 510. We plan on using it during FAT next week.
@Pat Wells

### Sean Odell, 2023-08-03

Adjusting Title since VXE510 has nothing actually wrong with it. This is a fuel cell RMA.

### Daniel Lloyd, 2023-08-03

@Pat Wells fuel cell S/N 4006249 was sent to Adaptive and arrived there 27 July.

### Robert Redfield, 2023-08-04

Yes,  I can confirm that SN0249 is in Ann Arbor.  Root cause analysis has not yet started on it as we have been focusing our efforts towards the D450+ launch.

### Cameron Chapman, 2023-08-24

Linking subtasks to parent.

### Cameron Chapman, 2023-08-29

@Daniel Lloyd do you know if this is related to TPTR-58 Fuel Cell error during climb?
@Robert Redfield and @Tom Westrich as this is related to TIQUILA, it is very high priority. Is anyone available to work on this? Please contact Allen for any priority sorting questions.

### Daniel Lloyd, 2023-08-30

@Cameron Chapman I created this, VIT-320, the description are my words. Those words are repeated in TPTR-55. I do not recognize the words in TPTR-58. It may be the same incident but reported by someone else. I don’t know.

## Attachments (14)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V510_230626_124718_01_pack.zip | archive | 3146 | 2023-06-28 | listed only |
| [T95_V366_230622_140828_fuelcelllog.csv](attachments/15248_T95_V366_230622_140828_fuelcelllog.csv.md) | csv | 284 | 2023-06-29 | converted |
| [T95_V414_230613_134758_fuelcelllog.csv](attachments/15245_T95_V414_230613_134758_fuelcelllog.csv.md) | csv | 221 | 2023-06-29 | converted |
| [T95_V414_230615_093302_fuelcelllog.csv](attachments/15246_T95_V414_230615_093302_fuelcelllog.csv.md) | csv | 501 | 2023-06-29 | converted |
| [T95_V489_230407_143326_fuelcelllog.csv](attachments/15240_T95_V489_230407_143326_fuelcelllog.csv.md) | csv | 193 | 2023-06-29 | converted |
| [T95_V489_230410_132221_fuelcelllog.csv](attachments/15242_T95_V489_230410_132221_fuelcelllog.csv.md) | csv | 290 | 2023-06-29 | converted |
| [T95_V510_230620_162652_fuelcelllog.csv](attachments/15243_T95_V510_230620_162652_fuelcelllog.csv.md) | csv | 261 | 2023-06-29 | converted |
| [T95_V510_230621_125744_fuelcelllog.csv](attachments/15247_T95_V510_230621_125744_fuelcelllog.csv.md) | csv | 226 | 2023-06-29 | converted |
| [T95_V510_230621_145511_fuelcelllog.csv](attachments/15241_T95_V510_230621_145511_fuelcelllog.csv.md) | csv | 342 | 2023-06-29 | converted |
| [T95_V510_230623_135119_fuelcelllog.csv](attachments/15244_T95_V510_230623_135119_fuelcelllog.csv.md) | csv | 254 | 2023-06-29 | converted |
| [D4500249 Combined run Data.xlsx](attachments/15397_D4500249%20Combined%20run%20Data.xlsx.md) | xlsx | 1170 | 2023-07-11 | converted |
| image-20230711-120940.png | image | 35 | 2023-07-11 | listed only |
| [RMA23088.pdf](attachments/15448_RMA23088.pdf.md) | pdf | 55 | 2023-07-14 | converted |
| [RMA23089.pdf](attachments/15447_RMA23089.pdf.md) | pdf | 55 | 2023-07-14 | converted |
