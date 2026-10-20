# VXEP-715: VXE 409 fuel cell stopped functioning in flight, Land immediately commanded

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed, but added to Bermuda Triangle List
- **Resolution:** Cannot Reproduce
- **Priority:** Highest
- **Created:** 2024-10-09
- **Updated:** 2026-08-14
- **Resolved:** 2026-01-20
- **Reporter:** Pat Wells
- **Assignee:** Sean Wendling
- **Creator:** Pat Wells
- **Labels:** D450XR_FuelCell, Hardware, MARSOC, Sustainment, Weekly-incident-tracker
- **Customer:** MARSOC
- **Vehicle Tail Number:** 409
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical

## Description

Statement from Operator: (Gougen)
Fuel cell stopped functioning in flight,  operator executed emergency procedure -Land immediately commanded.
HLB was depleted before aircraft was able to touch down.  Aircraft crashed with moderate damage.

## Corrective Action

Upon determination of exact root cause, the EAES team will provide immediate asset related corrective actions including in-warranty / out of warranty repair requirements for Electrical Power System as well as provide guidance on risk mitigation and reduction.

## Plan

- @Sean Wendling  to review data and provide preliminary information about incident.
- Systematic Issue that could affect other fielded units?
- Operator/Flight Behavior influence on the failure? (Opportunities for additional training or bulletin)
- @Pat Wells @Sean Odell Arrange for the return of the Equipment and repair to aircraft. 
- Fuel Cell should be returned to Ann Arbor, C.O. @Robert Redfield
- Incoming Performance Evaluation:
- Functional Fuel Cell QC Test to assess health and performance.
- Does SOFC Stack need replacement?
- Does FC Control Unit need repair or replacement?
- DC Regulation System Review (Possible failure between Raw Stack Output and Regulated Charge Output
- Assessment of Control Board Function and Communication Accuracy
- Hybrid Lift Battery Individual Cell Voltage Analysis (Cell-to-Cell Variation indicates internal battery failure)
- Connector / Harness Damage due to over-draw or discharge of energy during high current use.
- @Sean Wendling to furnish final incident report to provide to customer.

## Issue Status

Initial Review of After-Action Data confirms Fuel Cell critical fault and operator description of events. The issue is currently still under investigation to attempt to identify the exact root cause of the fuel cell failure.
RMA requested for all equipment involved in the incident in order to evaluate and provide assessments of repairs. Preliminary Data Review summarized and provided within published report.

## Root Cause

Root Cause is still under investigation for this incident. Data review yielded a loss of DC current flow between Hybrid Lift System and Fuel Cell Generator as the fault condition that caused the failure, though additional investigation of the equipment is required to provide additional guidance and repair options.
Leading Potential Root Cause Contributing Factors:
·        Failure of individual cells within the HLB.
·        Excessive Current Flow Resulting in Failure of Electrical Hardware.
·        Intermittent Fuel Cell DCDC Regulation Failure.

## Comments (9)

### Greg Fryer, 2024-10-09

@Sean Wendling @Tom Westrich The description doesn’t say how they know the fuel cell quit, assume that will show up in the AAR. I’ve moved it over to you, as that seems like the likely starting point. Also moved to On Hold until we get the AAR.

### Mike DeJesus, 2024-10-10

Uploaded the AAR, we have not received any additional descriptions or info from the operator. I will add if we get anything else.

### Pat Wells, 2024-10-14

@Alexander Alan Arnold will send a request for the equipment to be returned.  Currently the operators are deployed so likely this will be a lengthy process.
@Sean Wendling FYSA

### Sean Wendling, 2024-10-14

Okay sounds good. I don’t think it inhibits much of the data review. Based on the state of the aircraft I suspect that the fuel cell equipment is damaged anyway. Was there any more information on what happened provided by the operator?

### Pat Wells, 2024-10-15

@Sean Wendling no other information was provided by the operator.

### Alexander Alan Arnold, 2024-12-10

@Sean Wendling Any updates on this investigation?

### Sean Wendling, 2025-05-21

@Drew Hildreth Hey Drew, please review the attached preliminary report. Let me know of any edits you would like made, and I can provide the word document upon request!
The only things I fail to mention directly in the report that you may want to be aware of with this customer:
- There is probably some ways to mitigate this through more risk-considerate mission planning. They are pushing the maximum allowable windspeed throughout the entire flight and the power draw is high. I am not sure how normal this is as normally it isn’t what I am looking for in flight data logs, but with fuel cells some additional care and attention need to be made for the HLB voltage, which they allow to drop to between 40-60% charge. This makes an emergency VTOL landing much more challenging and likely contributed to why the crash occurred as opposed to a safe emergency landing. Still, a power system fault was the primary cause, but these things might be worth mentioning in the final report, I just didn’t want to make claims that their flying might have caused the crash and not our equipment since there was an issue on our end as well.
- This Fuel Cell is the previous generation, and was shipped years ago, (not sure how long exactly, but I can add that in the final report), Once we receive it I will check what software it has, though we don’t build this gen anymore and have resolved many of the issues (including some that could have caused this issue) through software and design updates. We will be limited in how much we can mitigate this failure fleetwide in the event its systematic.

Hope this helps!
thanks, Sean

### Jackson Riley Curvin, 2025-06-02

@Sean Wendling  the investigation looks good, but I think the root cause would be that the power system was operating in maximum output conditions for the majority of the flight, and HLB % charge was continuously in the range of 40-60%.

### Jackson Riley Curvin, 2026-01-20

Closed due to customer not giving the equipment back for investigation.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 409 crash.jpg | image | 3878 | 2024-10-09 | listed only |
| T95_V409_241009_003203_pack.zip | archive | 10807 | 2024-10-10 | listed only |
| [InvestigationReport_VXE-409_Rev1.pdf](attachments/29238_InvestigationReport_VXE-409_Rev1.pdf.md) | pdf | 787 | 2025-05-21 | converted |
