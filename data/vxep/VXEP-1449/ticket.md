# VXEP-1449: Systemic Hybrid lift battery unexplained cell failures in flight

- **Issue type:** Incident (8D)
- **Status:** D4 - Investigating Root Cause
- **Priority:** Highest
- **Created:** 2025-07-23
- **Updated:** 2026-09-02
- **Reporter:** Pat Wells
- **Assignee:** Sean Wendling
- **Creator:** Pat Wells
- **Labels:** Weekly-incident-tracker, battery
- **Links:** Cannot finish until linked issue is finished. VXEP-1435 (VXE-674 Second Hard Landing); Cannot finish until linked issue is finished. VXEP-1413 (HLB Issues 4139, 3908, and 3867); Cannot finish until linked issue is finished. VXEP-1398 (VXE-808 Aborted launch cell balance ); Cannot finish until linked issue is finished. VXEP-1293 (VXE 758 Aborted Launch at 30 feet AGL ); Cannot finish until linked issue is finished. VXEP-1417 (VXE-674 Abort and hard landing); relates to VXEP-1499 (VXE 559 Aircraft did not transition to VTOL Launch at 300ft AGL ); relates to BAT-367 (Provide investigation status for bad cells and prevention methods); relates to RMA-797 (VXE-559 RMA 250908-1); relates to BAT-223 (SB30 HL Battery Voltage Drop-Out RCCA); Linked issue cannot finish until this issue finishes. VXEP-1622 (PMA263 Master Systemic HLB Cell Failure)
- **Customer:** ALL
- **Production Stakeholder:** Alex Senita
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical
- **Executive Summary:** Probable cause appears to be Battery.

## Description

Sharepoint High Level: 7.2025 - Hybrid Lift Battery Cell Voltage Dropout https://jenaero.atlassian.net/wiki/spaces/EF/pages/23363854/Incident+Troubleshooting+and+Resolution+Tracking. 
Shared RCA investigation summary: Investigation Summary VXEP-1449 HLB Incidents.xlsx
Investigation Summary (8D): EAES_8D_HLBVoltageDropout.pptx
Testing Logs:
- HLB Self Discharge Test Data: HLB SelfDischargeTestLog.xlsx

Ticket is to track and consolidate findings for multiple failed cells on HLB’s. See linked issues.

## Corrective Action

Corrective Actions:
- Development of a kit for field Battery Analysis that can be rolled out to preventatively test batteries onsite with users.
- Enhanced Storage and Maintenance guidance from Edge to be added to a customer advisory notice along with notification of field operable tool.

## Plan

Ann Arbor Plan Updated 8/6:
Goals Week of 8/6:
- Testing Performed in HSV and Ann Arbor on HLBs:
- [ALL BATTERIES AVAILABLE] - HSV & AA; Voltage Loss Test (2-day self-discharge) - Charging batteries to 100%, allowing to sit for 48hrs, and measuring the cell variation over that time as a means to grow the population of data and identify a containment metric.
- [Damaged and EOL Batteries] - AA Only; Battery disassembly and Impedance / Internal Resistance - check on the cells themselves to further characterize poor performing batteries performed by @Stephen Peters & @Alex Senita.
- Upon completion of above test, batteries at failure are being selected to deliver to (2) Battery development facilities (Tree Town Tech & Advanced Energy) for Cell and Pack RCA @Stephen Peters to coordinate shipping.

________________________________________
Ann Arbor Preliminary Plan:
- Preliminary Data Review and Consolidation Performed in Ann Arbor @Sean Wendling @Stephen Peters
- Global Support to continue to try to collect and provide any missing data for investigation.
- @Alexander Alan Arnold @Drew Hildreth , Please plan to quarantine and/or route any batteries that are displaying this issue to us in Ann Arbor for review.
- Once handful of batteries are received; RCA will begin, and information will be provided by @Sean Wendling  to Global Support in regards to containment and whether advisory notices / warnings need to be issued.
- @Stephen Peters @Alex Senita  will perform onsite RCA and testing on returned batteries and collaborate with Vendor.

## Issue Status

Information Gathering Phase, Root Cause on received batteries to begin 24 JULY 2025. Status of available batteries being tracked by Ann Arbor (Updated 8/6)
| Battery SN | Date of Occurrence | Where | Status | AC Serial | # of Cycles | Received? | Data? | Jira Ticket |
| 3490 | 5-Jun-25 | TRAINING EXERCISE (USBP) | INTERNAL | VXE758 | 18 | Yes | Yes | Yes |
| 4139 | 2-Jul-25 | SLO SCO | INTERNAL | VXE880 | 40 | Yes | Yes | Yes |
| 3397 | 9-Jul-25 | PMA 263 (UNKNOWN) | CUST | VXE801 | UNK | No | No | No |
| 4115 | 10-Jul-25 | TRAINING EXERCISE | INTERNAL | VXE808 | 18 | Yes | Yes | Yes |
| 3288 | 14-Jul-25 | UNKNOWN | CUST | VXE401 | UNK | No | No | No |
| 4066 | 17-Jul-25 | FT SILL (MFIX DEMO) | INTERNAL | VXE674 | 28 | Yes | Yes | Yes |
| 3748 | 18-Jul-25 | TRAINING EXERCISE | INTERNAL | VXE674 | 22 | Yes | Yes | Yes |
| 3785 | UNKNOWN | SLO SCO | INTERNAL | UNKNOWN | 25 | Yes | No | Yes |
| 3980 | UNKNOWN | SLO SCO | INTERNAL | UNKNOWN | 44 | Yes | No | Yes |
| 3889 | UNKNOWN | SLO SCO | INTERNAL | UNKNOWN | 43 | Yes | No | Yes |
| 3908 | 8-Apr-25 | SLO SCO | INTERNAL | VXE757 | 48 | Yes | Yes | Yes |
| 3867 | 11-Jan-25 | SLO SCO | INTERNAL | VXE689 |  | No | Yes | Yes |
| 3083 | 30-July-25 |  | INTERNAL | VXE559 | UNK | No | Yes | Yes |

## Root Cause

Battery Dissection led to discovery of leaking / evaporating electrolyte material inside the 3300mAh Advanced Energy Cells within the HLB. Including one instance of the Z-fold being caught in the pouch’s hermetic seal resulting in air passing through and reduced performance.
This evaporation can occur over time and would likely not be detectable in outgoing testing and would propagate over the course of the life of the battery. This is one of multiple possible contributing factors that affect battery performance, and additional analysis will circulate around the emphasis on quality control and inspection at the vendor facility as well as regular functional health tests on HL Batteries.

## Comments (11)

### Greg Fryer, 2025-07-23

@Tom Westrich FYI

### Alexander Alan Arnold, 2025-07-23

We combed through the available GCS we had on hand in HSV and uploaded AARs associated with the batteries we identified. @Sean Wendling @Tom Westrich

### Sean Wendling, 2025-07-23

Hey @Alexander Alan Arnold , thank you for this! super helpful. We are investigating right now and will continue to update in this ticket.

### Sean Wendling, 2025-07-23

@Stephen Peters @Alex Senita

### Sean Wendling, 2025-07-24

@Pat Wells @Drew Hildreth , I placed a chart in the Issue status box. The last 3 columns show whether we have what we need to investigate. So far there are (3) units that we have here in AA and have data to review. I am going to recommend investigation priority on those. As you collect more information, let me know and we can widen the scope.
FYI, data is the most important item at the moment, so if I don’t have it but I have data I will also evaluate those.
Thanks!

### Sean Wendling, 2025-08-06

Updated plan and issue status, will continue to update as more information is collected.

### Pat Wells, 2025-08-08

@Sean Wendling @Drew Hildreth @Alexander Alan Arnold @Jackson Riley Curvin 
We’ve updated the self discharge data sheet.

### Sean Wendling, 2025-09-05

Updated Chart to show latest https://jenaero.atlassian.net/browse/VXEP-1499.

### Scott Lovett, 2026-02-02

Next Steps: Awaiting delivery of battery tester kit to Huntsville. Estimated week of 2026-02-16 @Sean Wendling

### Scott Lovett, 2026-07-06

@Sean Wendling @Tom Westrich Now that the HLB tester is done, how do we come up with (or update) a test plan?

### Tom Westrich, 2026-07-06

@Scott Lovett 
Ultimately, our best test would look like a Takeoff and Landing event sequence, would require ~ 2hrs per battery to measure, and our pass/fail requirements would be based on a cell voltage imbalance.  Stephen has identified that the primary loss of function in the battery results in a higher cell or pack impedance, which should be measurable by a DCIR test, preferably at 60% SOC (storage conditions) to minimize the required battery charge/recharge time during the test.
 
Therefore, we will need to update the analysis to include the calculation of the per-cell impedance during the current/power pulse step.  Can this be included in your results and dashboard?  One looming question we have is what power or current pulse is required to statistically identify a poorly performing battery.  If we had a perfect measurement system and all batteries performed identically, we could perform this test with a low-power electronic load.  Unfortunately, the cumulative uncertainties between measurement systems, test timing, and cell states of charge will force us to evaluate impedance at higher currents.
 
Once we are able to calculate the cell impedance in the analysis, I would recommend that we re-run batteries with the following sequence (taken from Slide5 here:  HLB voltage drop-off test plan.pptx)
- Charge to 60%SOC and within temperature range
- Pulse 3 24C events (24C*6.6Ah = 158.4A)
- Cool, recharge to 60%, repeat with 12C and 6C pulses

 
I would also recommend that we have as many good batteries as possible go through this procedure to grow the baseline data set of ‘healthy’ battery impedance at each of these load conditions.

## Attachments (11)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 2-3490.zip | archive | 8047 | 2025-07-23 | listed only |
| 2-3748.zip | archive | 10077 | 2025-07-23 | listed only |
| 2-4066.zip | archive | 7372 | 2025-07-23 | listed only |
| 2-4115.zip | archive | 20606 | 2025-07-23 | listed only |
| T95_V490_250430_125056_01_pack.zip | archive | 3537 | 2025-07-30 | listed only |
| T95_V674_250421_110556_01_pack.zip | archive | 3765 | 2025-07-30 | listed only |
| T95_V734_250424_175322_02_pack.zip | archive | 4102 | 2025-07-30 | listed only |
| T95_V734_250623_113336_pack.zip | archive | 2563 | 2025-07-30 | listed only |
| T95_V734_250623_142713_pack.zip | archive | 3793 | 2025-07-30 | listed only |
| T95_V758_250514_152444_pack.zip | archive | 819 | 2025-07-30 | listed only |
| T115_V880_251112_142255_pack.zip | archive | 2104 | 2025-12-05 | listed only |
