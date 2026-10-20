# VXEP-780: VXE 732 Fuel cell flameout while in flight

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-11-18
- **Updated:** 2026-03-02
- **Resolved:** 2025-03-20
- **Reporter:** Pat Wells
- **Assignee:** Sean Wendling
- **Creator:** Pat Wells
- **Labels:** TIQUILA, Weekly-incident-tracker
- **Links:** relates to ENG-2984 (732 Fuel Cell Flameout); relates to RMA-471 (D4500509 250122-1); relates to RMA-472 (D4500510 RMA 250122-2)
- **Customer:** TIQUILA
- **Vehicle Tail Number:** 732
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

Statement received from LM FSR:
Flight profile was to fly a full endurance fuel cell flight with Tequila baseline HD55 payload. 
On the 13 November flight the aircraft was loaded with a fully serviced propane tank (922g of propane). Weight and balance was checked, aircraft weight was 44.7lbs. The aircraft was flown in a racetrack pattern. The flight was on track for an estimated 6.5 hrs when at about 5.2 hrs the fuel cell indicated an error and was no longer charging the hybrid battery. The HLB was approximately 55% and the VTOL control window indicated about 7 min of battery remaining. The fuel cell was commanded to stop, and then start was commanded. This did not correct the problem. The hybrid battery charge state was a little questionable for a VTOL landing so an uneventful glide landing was performed. Post flight it was determined that the cause of the fuel cell error was fuel starvation. The fuel tank was empty but the software indicated one hour of fuel remaining. 
On the 14 November flight the aircraft was again loaded with a fully serviced propane tank (922g of propane).  Prior to flight we leaked checked the system (from fuel tank to the fuel cell fitting in the nose) with the tank and manifold that was flown the day prior – no leaks detected.  We then leak checked using the manifold we were going to fly for the second flight– no leaks detected.  We flew the same plane, V732, with a different fuel tank, a different manifold, and different filter, and different fuel cell.  At approximately 6:00 into the flight, fuel cell control window indicated ~100 grams of propane remaining, and fuel cell control window and GCS telemetry indicated ~45 minutes endurance remaining, and the fuel cell stopped producing power.  The fuel cell status in the GCS telemetry said ERROR and flashed red.  The aircraft remained on mission.  The aircraft was commanded Go to IP4 of the PLZ while the HLB still had plenty of energy for a vertical landing with no issues. Post flight it was determined that the cause of the fuel cell error was fuel starvation. The fuel tank was empty but the software indicated fuel remaining. 
When the fuel cell stops in flight, or “shuts down” the software will begin non-stop chiming, there’s a pop-up that the fuel cell has shutdown inflight, and that the aircraft will automatically RTB for low energy. These things did not happen for either flight when the fuel cell quit generating power. On the first flight the data will show that those events occurred but that was because we commanded a shutdown.
Without intervention, we believe the plane would have remained on mission until the HLB was at 21 volts, commanded zero throttle, and glided down to the ground while continuing to navigate the mission.  We believe the aircraft should treat a loss of fuel cell power as a “fuel cell has stopped” and execute an Automatic Low-Energy RTB.
AAR’s and pictures attached

## Corrective Action

Team has been able to verify correction of issue through defect repair and recalibration of the fuel system. This is demonstrated in Section 5 of this report. Both units delivered to Ann Arbor for this incident will receive recalibration and retesting to certify conformance to standard outgoing specifications and then be returned to the customer.
At this time, the corrective action is only available onsite at Ann Arbor manufacturing facility; however, development is ongoing to prepare a field service alternative for units that have low operational hours to be repaired by technician at equipment site or preferred customer location. This is intended to address the issue on a fleetwide level and minimize impact to customers. Further information regarding options will be provided along with the ongoing CAR.

## Plan

D4500509 returned to user. 
@Sean Wendling Continuing to Study D4500510.

## Issue Status

At this time, team has determined the primary root cause, and has demonstrated successful implementation of corrective action on one of the two provided units including full endurance verification cycle and description of results. D4500509 is to be shipped back to the customer, while D4500510 is under continued investigation by AA team.

## Root Cause

The primary root cause determined to be a manufacturing defect in the fuel routing through a directionally sensitive mass flow meter.  While plumbed in the correct flow orientation, the mass flow meter is able to accurately report fuel consumed within a 5% error margin.  When fuel is plumbed in the incorrect (reverse) direction, the measured fuel flow rate can become inaccurate, resulting in the under-reporting of fuel consumed.  The degree of inaccuracy is a function of the ambient temperature and fuel temperature at the time of use but is generally 8% to 13% over the -20°C to 50°C operational range of the D450 . This has serious implications for the aircraft’s operation as the endurance estimations can result in up to 150g deficit in the most extreme cases.  See Section 3.3 of the report for more detailed investigation findings.
Results of this report have triggered the beginning of an ongoing CAR led by the Edge Autonomy Quality Department that is to be an ongoing effort to assess and correct this issue fleetwide. This report will discuss the corrective action required specifically for these units and serve to provide evidence and information for the ongoing CAR.

## Comments (13)

### Pat Wells, 2024-11-18

@Sean Wendling  FYSA

### Sean Wendling, 2024-11-18

@Pat Wells , thank you for sharing. I will get back to you ASAP about what we can do on the Fuel Cell Side.

### David Grosher, 2024-11-18

@Ted Trowbridge Can you take a look at the GCS warnings that supposedly did not occur. 
@Sean Wendling I’m not familiar with the fuel remaining calculations, where does that occur?

### Sean Wendling, 2024-11-18

@David Grosher Fuel Cell is reporting its real-time measured fuel utilization to the GCS, I suspect this is being subtracted from the value the user enters into the Launch Wizard for total fuel. I will check into this and get back to you.

### Alexander Alan Arnold, 2024-12-10

@Sean Wendling any updates?

### Sean Wendling, 2024-12-10

Hey @Alexander Alan Arnold , I reviewed the data and it might be best to get it back to Ann Arbor for evaluation. There is some margin of error for fuel flow, but what they are reporting does seem significant. 
@Robert Redfield FYI

### Alexander Alan Arnold, 2024-12-10

@Sean Wendling we will ask for the fuel cell

### Alexander Alan Arnold, 2024-12-10

@Sean Wendling If you look at the linked VIT2 ticket they are reporting that two fuel cells had similar issues. SN 510 SN 509. do you want both returned to Ann Arbor?

### Alexander Alan Arnold, 2025-01-10

@Sean Wendling Just following up to confirm that you want both fuel cells

### Sean Wendling, 2025-01-15

Hey Alex, yes send them both back

### Sean Wendling, 2025-02-13

@Pat Wells I have attached the revision 1 of the Investigation Report for this unit. Please let me know if you would like it updated in any way. I will publish a revision 2 along with the D4500510 unit once it has been corrected. Additionally, I have attached an excel file with the data from the endurance verification flight that Lockheed had requested we perform (and that is summarized in the report).

### Pat Wells, 2025-03-17

@Sean Wendling  can we move to closing this?

### Sean Wendling, 2025-03-17

@Pat Wells , I would say yes as this has moved into a QA managed investigation. Only holdout is that we still have D4500510 here in Ann Arbor. We are done studying it now, and I should be able to get it shipped in the next week or so. 
Its still captured in the RMA list though, and with the Engineering work done, I think we could close this. I will end up sending an updated version of the attached report once we send SN510 back to SLO.

## Attachments (9)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| IMG_2821.jpg | image | 2439 | 2024-11-18 | listed only |
| IMG_2822.jpg | image | 1758 | 2024-11-18 | listed only |
| IMG_2825.jpg | image | 1632 | 2024-11-18 | listed only |
| IMG_2826.jpg | image | 2090 | 2024-11-18 | listed only |
| Screenshot 2024-11-17 174821.JPG | image | 270 | 2024-11-18 | listed only |
| T95_V732_241113_073820_pack.zip | archive | 6776 | 2024-11-18 | listed only |
| T95_V732_241114_081728_pack.zip | archive | 7357 | 2024-11-18 | listed only |
| D4500509_VIT2-500_FuelEnduranceVerification_2.7.2025 (1).zip | archive | 6369 | 2025-02-13 | listed only |
| [InvestigationReport_VIT2-500_Rev1.pdf](attachments/26213_InvestigationReport_VIT2-500_Rev1.pdf.md) | pdf | 1329 | 2025-02-13 | converted |
