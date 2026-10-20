# VXEP-1880: LEMB CAN EE Investigation

- **Issue type:** Epic
- **Status:** In Process
- **Priority:** Medium
- **Created:** 2026-05-06
- **Updated:** 2026-09-16
- **Reporter:** Jeremy Kostel
- **Assignee:** Samuel Lopez
- **Creator:** Jeremy Kostel
- **Parent:** VXEP-1568 VXE-818 Lift System didn't disengage - Crash - CAN bus error 
- **Links:** relates to VXEP-1608 (VXE 881 CW not detected but able to access .10 page and GPS Satellites displayed in SUAV); relates to RMA-853 (LEMB 3-0042 RMA 251120-4); relates to VXEP-1999 (B30 ADVNAV CANJAM CAN Issues)
- **Epic Status:** To Do
- **Epic Color:** ghx-label-10
- **Issue color:** blue

## Description

The first LRR delivery utilized the B35X version (adapted from B30) and experienced multiple issues during deployment. The suspected root cause is the LEMBs delivered with these aircraft. These LEMBs include a Battery Management System (BMS) that connects to the aircraft CAN bus to provide enhanced State of Charge (SoC) reporting and other telemetry.
We believe the LEMB BMS is introducing CAN bus errors, which may be cascading into broader aircraft system issues.
Sharepoint
https://jenaero.sharepoint.com/:f:/r/sites/JAI_Operations/Shared%20Documents/NCR%20Investigations/VXEP-1880%20LEMB%20CAN%20Investigation?csf=1&web=1&e=Tq9pws

Background
- LEMBs include a CAN connection between the battery BMS and the aircraft BMS board
- CAN communication is intended to improve battery telemetry (e.g., SoC accuracy)
- Field issues observed on B35X align temporally with use of these LEMBs
- There are currently three (3) LEMBs in Receiving and one (1) LEMB in the ENG battery cabinets

Objective
Determine whether LEMBs, specifically their CAN/BMS connection, are responsible for CAN bus errors and related aircraft issues when installed on a B35X.
Scope
Testing will compare CAN bus health across multiple battery configurations on a B35X aircraft.

## Plan

- @Samuel Lopez can you please update the investigation showing that component ratings were exceeded with transients during testing. Please also indicate if this occurs in B30 configuration and if that design should change. https://jenaero.sharepoint.com/:p:/r/sites/JAI_Operations/_layouts/15/Doc.aspx?sourcedoc=%7BE1983CDF-DBD9-4295-9547-5F9C5D9748C3%7D&file=B35x%20CAN%20LEMB%20battery%20investigation%20II.pptx&action=edit&mobileredirect=true
- Sammy Lopez is this correct? Can you please report if such transients were present in the B30 config and if any design updates are recommended to the B30 HLB? Please update the ppt with that info.
- Follow up questions to proposed containment: @Scott Whitney's team can best answer this. Scott, can you have someone answer the following?
- Are main battery cell voltages or anything related visible on the 35X OGCS? I am pretty sure the main battery voltage is still measured in the XCOM and should still function with this disconnected.   
- SW: No OGCS does not display MB cell voltages. LEMB is a Smart MB therefore the cell voltages come from the BMS
- Are those cell voltages used in any firmware, or just logged? 
- SW: Just logged
- Are they logged in the AAR for 35X?
- SW: There should be from April to May of 2025 on v757 (https://jenaero.sharepoint.com/:f:/s/SLOFLOPS/IgDEol02a1KVR5BsLGFVZTiBAez1z4JonByrZVT4Bv9kFPg?e=CWPerr)
- 

Containment proposed see below. Needs approval and plan to distribute from product owners, PM, and GS. @Tom Westrich @Douglas Baker @Pat Wells @Alex Drouin. Asked in this chat LEMB Containment
- Containment: There are a two (2) B35x units still out in the field for which Redwire is to provide indefinite support. Recommended containment actions are.​
- Leave LEMB data unmated​
Instruct our customer to disconnect the four pin CAN LEMB monitor and keep using the battery normally. This will likely prevent any failures on the TVS diodes of the controller board. Disconnecting that data line would guarantee that even if a failure were to occur, it wouldn’t be able to cascade to the rest of the CAN architecture on the rest of the plane. However, the customer will not be able to monitor the cell voltages.​
- Determine if additional LEMBs will ever be produced. If so, implement and test fixes. If not, can they be removed from the catalog?



​

## Issue Status

Containment proposed see below. Needs approval and plan to distribute from product owners, PM, and GS. https://jenaero.sharepoint.com/:p:/r/sites/JAI_Operations/_layouts/15/Doc.aspx?sourcedoc=%7BE1983CDF-DBD9-4295-9547-5F9C5D9748C3%7D&file=B35x%20CAN%20LEMB%20battery%20investigation%20II.pptx&action=edit&mobileredirect=true

We weren't able to recreate the failure, but we were able to demonstrate that the 35X configuration causes transients that exceed the component ratings on the diodes that failed. Demating the LEMB data cable removed these transients (since it removed the extra ground loop) This seemed like sufficient evidence to indicate these transients likely caused the issue and that the recommended containment would be effective.

## Comments (14)

### Jeremy Kostel, 2026-05-06

@Samuel Lopez plan laid out in this ticket is just what I would propose, but has not been coordinated with @David Grosher or @Erik Hanson 
Please reach out to them with questions
Erik can also likely help you locate asset batteries/vehicles

### Samuel Lopez, 2026-05-20

First Notes

The four aircraft in question are 817, 818, 828, and 829.  Checking the travelers for each, these are all using the older XCOMM, VTOL AP, and ADB that each have CAN terminations, in addition to the Tail and Left Boom.

### Samuel Lopez, 2026-05-20

Iron Bird Testing 1.0

Case 1: B30
Case 2: B35 battery no CAN
Case 3: B35 battery with CAN (SN: 3L-0028)

Measured with a differential probe, the CAN bus on Case 1 and Case 2 read normally from 0 to 2V (pictures attached).
However, on 
Case 3, the differential only measured from 0V to 1V, meaning something is pulling the signal low.  This is likely root cause behavior.  After some time, the square wave develops significant transients on the rising edge as shown below.

*Notes about testing.  This was on the B30 Iron Bird has only two on XCOMM and VTOL which together measure 60 ohms.
B30
[embedded B30 Battery.png]
B35 with no Data
[embedded B35 Battery no Data.png]
B35 with Data (1Vpp SN 28 and 30)
[embedded B35 Battery with Data 1.png]
B35 with Data (may or may not be instrumentation error)

Of the three batteries that came back from the customer, two of them exhibit the behavior described below with a CAN differential of 1 V.  SN 32 worked intermittently.  Half the time, the CAN measured normally at 2V, but it sometimes degraded to 1.4V.   The serial numbers are listed.

| SN | CAN Vpp |
| 3L-0028 | 1V |
| 3L-0030 | 1V |
| 3L-0032 | 1.4V (2V) |

### Samuel Lopez, 2026-05-22

OBSOLETE: The B35x only has three terminations, not four.  Therefore, this data is good only for recognizing that extra terminations reduce differential voltage magnitude.
This data is interesting, but not truly representative of B35x.
Termination: 24Ω vs 60Ω
Additional termination was added to the CAN line to simulate the four b35x aircraft that have five terminations (24 Ω).  Adding extra resistance on the CAN line to the iron bird caused two things - the voltage magnitude to fall, the CAN waveform to degrade (see sharepoint for images). Below is a table detailing the voltage peak-to-peak on both 60 Ω - a proper termination, and 24 Ω - what the aircraft actually has.

| CAN Vpp |
| SN | 60 Ω | 24 Ω |
| 3L-0028 | 1V | 750 mV |
| 3L-0030 | 1V | 460 mV |
| 3L-0032 | 1.4V - 2V | 1.2V |

### Samuel Lopez, 2026-05-22

Details
B30 Advanced Nav - two terminations on XCOMM and VTOL AP.  Battery does not have CAN node.
B35x Advanced Nav - three terminations on XCOMM, VTOL AP, ADB + an extra CAN node on battery.
Normal CAN differential voltage ranges from 2V to 2.2V on a healthy CAN bus line that is properly terminated at 60 ohm the way the B30 Iron Bird is.  Per the datasheet of transceiver MAX3051, the minimum differential CAN voltage should be greater than 1.2V.   When B35x battery CAN node is connected to the rest of the architecture, it pulls down the CAN differential voltage to between 1V to 1.4V.  This is likely being caused by something in the B35x CAN hardware.
[embedded 1.1.jpg]

### Jeremy Kostel, 2026-05-27

@Samuel Lopez a few times in here you mention 5 CAN terminators in the loop - where are the five? XCOM, VTOL, ADP if old. Is there one on the BMS board? what is the 5th?

### Samuel Lopez, 2026-05-27

@Jeremy Kostel Thank you Jeremy for the clarification.  A lot of confusion between B35 and B35x.  This means that B35x is only over-terminated by one (XCOMM, VTOL AP, and ADB, which equal 40 Ω).

No, the BMS is not terminated.

### Samuel Lopez, 2026-06-02

The following CAN differential voltages are from all B35x batteries and no Iron Bird or other devices/CAN nodes.  Only a single 120 ohm resistor across the CAN line.

*Note.  SN10 and SN41 come from the shelf in SLO site.  SN28, 30, and 32 come from customer.
| SN | CAN Vpp |
| 10 | 2.5 |
| 41 | 1.5 |
| 28 | 1.1 |
| 30 | 0.750 |
| 32 | 1.0 |

### Samuel Lopez, 2026-06-02

B35x battery 
SN32 stopped working!

SN 32 was opened to probe whether the DC regulator is behaving appropriately and other tests.  Upon being opened, the CAN line stopped working altogether.  Additionally, 3.3VDC reads zero on the actual PCB board.  No heat was applied.  Running continuity 28V and GND on BMS with multimeter reveals open circuit.  

After removing the charger board and removing epoxy, it is discovered that the ‘open’ is on the input J6 connector itself (see image below).  This does NOT explain CAN irregularities, however, as the Battery Controller board by itself still exhibits abnormal behavior.

Investigation will continue on both SN32 Battery controller board and SN28 battery.
[embedded image-20260610-214258.png]
*Note.  Voltage regulation on battery controller board measures 3.265V when 28V is manually applied.  This is true on both SN32 and SN28.  Buck converter is not the problem.

### Samuel Lopez, 2026-06-10

[embedded image-20260610-232338.png]

It has been determined that the TVS diodes on the battery controller are either malfunctioning, installed backwards, or damaged.  Lab diodes were then added where the two diodes had been removed.

SN32 - with diodes
[embedded SN32 60 ohm both diodes-20141101-190000.png]
SN32 - diodes removed 
[embedded SN32 60 ohms diode removed.png]
SN32 - lab diodes added
[embedded SN32 120 ohm with diode back in.png]


Conclusion: There seems to be a hardware problem related to the diodes.  There are several questions that remain.
- Why did the TVS diodes fail?
- Could they have been installed backwards? No, see next question.
- What do the diodes measure when out of the circuit?  After being removed, measuring red to anode and black to cathode measures 0.714V and OL when the other way around for D14 (CANH tvs).  For D10 (CANL tvs), the measurements are 0.413V and OL.


Next steps.
Remove diodes on SN28 and see if issue is fixed.

### Tom Westrich, 2026-06-17

FYSA @Stephen Peters , @Dylan Peters ,  we should review these findings and plan our corrective actions accordingly.  While B35X development is currently lower priority than B35/40, this issue was the fundamental blocker to continued release of advanced cells to the B30/35x fleet.

### Samuel Lopez, 2026-07-08

Waiting to hear how much longer we will support B35x CAN LEMBs.  After that, will report to Tom W and Stephen P of results.

Dave G and Greg F will be consulted on containment.


https://jenaero.sharepoint.com/:p:/r/sites/JAI_Operations/Shared%20Documents/NCR%20Investigations/VXEP-1880%20LEMB%20CAN%20Investigation/Presentation/B35x%20CAN%20LEMB%20battery%20investigation%20II.pptx?d=we1983cdfdbd9429595475f9c5d9748c3&csf=1&web=1&e=hlgfyR

### Cameron Chapman, 2026-07-17

Moving info from plan field that seems to be done (see linked ppt)
Test Plan / Recommended Steps
- Baseline Configuration
- Install a standard main battery (non‑LEMB)
- Measure CAN bus health
- Record CAN logs
- Capture CAN bus waveforms using an oscilloscope
- LEMB Installed – CAN Disconnected
- Install a LEMB with the CAN/BMS connection disconnected
- Measure CAN bus health
- Record CAN logs
- Capture CAN bus scope data
- LEMB Installed – CAN Connected
- Install a LEMB with the CAN/BMS connection connected
- Measure CAN bus health
- Record CAN logs
- Capture CAN bus scope data

Expected Results
- Clean, error‑free CAN bus behavior with:
- Standard main battery
- LEMB installed with CAN disconnected
- CAN bus errors present only when the LEMB CAN/BMS connection is active

This would indicate the issue is specifically related to adding the LEMB BMS node to the CAN bus.

Acceptance Criteria
- CAN logs and scope captures clearly demonstrate correlation (or lack thereof) between LEMB CAN connection and bus errors
- Results are repeatable and documented
- Clear go/no‑go conclusion on whether the LEMB BMS is the source of CAN instability

Next Steps (Post‑Acceptance)
If the LEMB CAN connection is confirmed as the issue, proceed with isolated investigation of the LEMB/BMS hardware and firmware independent of the aircraft.

### Tom Westrich, 2026-08-12

@Cameron Chapman@Jeremy Kostel  @Samuel Lopez , what are our next steps on this issue to get to a corrective action?  If the issue is limited to the CAN interface on the LEMB, then we’ll need to have an identified corrective action (e.g., CAN isolation before the HLB BMS board or updated TVS  diodes on the HLB BMS board) before we can complete productionization of the LEMB.  At this phase, I’m really looking for a time estimate for completion so I can add it to our production release planning.  Thank you!

## Attachments (9)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| B30 Battery (793f21bd-8c5a-4307-80f1-a44e576af959).png | image | 43 | 2026-05-21 | listed only |
| B35 Battery no Data (3ceeff55-ccbc-4143-9d46-c1cdbf2419c8).png | image | 43 | 2026-05-21 | listed only |
| B35 Battery with Data 1 (8aa3ce1c-420e-4748-ac3d-3e5fb38ac9b2).png | image | 41 | 2026-05-21 | listed only |
| 1.1.jpg | image | 93 | 2026-05-22 | listed only |
| SN32 120 ohm with diode back in.png | image | 57 | 2026-06-10 | listed only |
| SN32 60 ohm both diodes-20141101-190000.png | image | 46 | 2026-06-10 | listed only |
| SN32 60 ohms diode removed.png | image | 43 | 2026-06-10 | listed only |
| image-20260610-214258.png | image | 18597 | 2026-06-10 | listed only |
| image-20260610-232338.png | image | 101 | 2026-06-10 | listed only |
