# VXEP-2022: Ping200 reporting incorrect altitudes when above 6,000ft.

- **Issue type:** Incident (8D)
- **Status:** D2 - Gathering Information
- **Priority:** Medium
- **Created:** 2026-10-14
- **Updated:** 2026-10-14
- **Reporter:** Stephan Johnson
- **Assignee:** Stephan Johnson
- **Creator:** Stephan Johnson
- **Labels:** RCCA, USAACE_(2-13th), Weekly-incident-tracker
- **Customer:** USAACE
- **Vehicle Tail Number:** 1020 and 1068
- **Problem Type:** Other (explain in description)
- **Incident Type:** Squawk
- **Severity:** 3 - Degraded Performance - With Workaround
- **Executive Summary:** Working on finding out when the units were last calibrated.

## Description

Customer noticed that their Ping200 is reporting incorrect altitudes when the aircraft climbs above 6,000ft msl. For context, field elevation there is ~4,300.
Operator statement:
"On AV 1068 we only did 6000ft and 9000ft and 6000ft was accurate while 9000ft was reporting 8700ft.
On AV 1020 we tested 6000ft still accurate, 7000ft was
reporting 6900ft, 8000ft was reporting 7800ft, and at 9000ft it was reporting 8700ft."
The altitudes were being compared between the local tower, the aircraft (OGCS), and the Ping. Tower and the aircraft altitudes were the same, with the Ping200 reporting inaccurately.
After speaking with @Cody Smisek, it was discovered that some Ping200 units left the factory with dust covers installed on the pitot static port. Customer checked and verified that the dust cover was not installed on this unit.

## Comments (2)

### Stephan Johnson, 2026-10-14

[embedded: Ping200 User Manual.pdf]
Here is the uAvionics user and installation manual

### Cody Smisek, 2026-10-14

@Stephan Johnson the ping unit only has a static pressure port. No pitot. Model unit in use by RDW (last I checked) is the Ping200X, not a 200XR.
It is highly unlikely that these units (the ping hardware itself) are defective or providing incorrect information. They are TSOd hardware.
If a full investigation is taking place on this, we need the following
- the AARs/flight data from the flights
- Were they using OGCS or legacy GCS
- The location, date, time of the flights
- What type of ATC facility is referenced and their facility equipment capabilities, were they using mode c altitude, radar altitude, adsb gps altitude
- what ICAO and N number was being used (as configured in the transponder software) at the date/time of flights. It is possible we will be able to utilize publicly available data through PAPR https://adsbperformance.faa.gov/paprrequest.aspx


The more likely causes of the customer observations are as follows
- misunderstanding by all parties on how transponders report altitude. ie they use pressure altitude via Mode C altitude encoder on embedded in the unit. This is likely what ATC would see/report back. Some facilities are equipped for ADSB but pretty unlikely they are referencing anything from the ADSB. Our system has many altitudes it uses / reports. Depending which GCS version they were using would determine the quantity/type of altitudes our GCS shows.
- known baro altitude issues for our system (on VXE side) that can result in altitude discrepancies.
- inaccurate pressure altitude due to location of transponder (hood payload impacted by forward motor air pressure) and ping enclosed in secondary enclosure surrounding it.


The calibration mentioned within the Ping manual has to do with complying to CFRs for use on certified systems, which ours is not. However, it does give reasonable guidance as to how accurate the equipment should be. Which is +/-125ft (this is specific to the pressure altitude reporting). This is typically tested using an air data test system along with the use of something like an IFR6000. The air data test system is its own calibrated tool used to provide pressure (positive/negative compared to ambient) to the static port, and then run up to the manufactures recommended (or regulatory authority required) pressure altitude. 
This raises a question as well, at what point are we no longer involved in the vendor supplied hardware? We are not a transponder company and the vendors manual provides the steps necessary to calibrate the equipment if they believe the transponder itself is not calibrated correctly (or has subsequently gone out of calibration since delivery). 

The statement, 
“The altitudes were being compared between the local tower, the aircraft (OGCS), and the Ping. Tower and the aircraft altitudes were the same, with the Ping200 reporting inaccurately.”
makes no sense in the context of this situation. Further elaboration of what is being described by this statement would be required, as requested in my bullet points above.

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| Ping200 Settings.jpg | image | 482 | 2026-10-14 | listed only |
| [Ping200 User Manual.pdf](attachments/65383_Ping200%20User%20Manual.pdf.md) | pdf | 1102 | 2026-10-14 | converted |
