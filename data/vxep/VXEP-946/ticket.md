# VXEP-946: VXE 401 Centerwing failing to report proper VTOL battery state

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-02-03
- **Updated:** 2026-09-09
- **Resolved:** 2026-07-13
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Steve Gonzales
- **Creator:** Alexander Alan Arnold
- **Labels:** Hardware, No_crash, PMA263, Weekly-incident-tracker
- **Links:** relates to RMA-510 (VXE-401 Center Wing RMA 250206-2); relates to ENG-2946 (Investigate where the harness failure occured and why); relates to ENG-2944 ([REMOVE from VXEP] VXE 689 - VTOL battery voltage sensor stopped working after power cycling. )
- **Customer:** PMA263
- **Vehicle Tail Number:** VXE-401
- **Vehicle Configuration:** Standard VXE30 Battery
- **Corrective Action:** Linking corrective action with https://jenaero.atlassian.net/browse/VXEP-542
- **Root Cause:** Replace Current Sense Board. Same issue was found in with aircraft 689: https://jenaero.atlassian.net/browse/VXEP-542
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

“All, I am not able to go through a pre-flight check because the vtol battery shows low.  See attached picture.  The center wing does not give a proper voltage of the vtol battery.
 It is my understanding that I can't get an FDR because I can't finish the pre-flight checks.  Please advise.”

Michael From INL 

SharePoint Folder: https://jenaero.sharepoint.com/sites/FlightSafety/Shared%20Documents/Forms/AllItems.aspx?newTargetListUrl=%2Fsites%2FFlightSafety%2FShared%20Documents&viewpath=%2Fsites%2FFlightSafety%2FShared%20Documents%2FForms%2FAllItems%2Easpx&id=%2Fsites%2FFlightSafety%2FShared%20Documents%2FIncident%20Reports%2FVXEP%20%2D%20946%20%2D%20VXE%20401%20Centerwing%20failing%20to%20report%20proper%20VTOL%20battery%20state&viewid=7181a7a2%2Dd286%2D47c9%2Dbdd3%2D9195ef18282c

## Plan

- Assigning to @Steve Gonzales to review current status, ppt, and update plan. FYI @Pat Wells
- HW in SLO. Verify issue repeats and identify source of incorrect readings.

Further data review
- Vtvbatt is calculated using vref. If that looked abnormal compared to other vehicles, it could indicate a wiring issue.
- inspect internals of CW
- Replace Dual Current Sense Board 
- @Adrian Garcia we can return remaining equipment once we are sure this issue is isolated to the CSB, but we should keep this issue open to try to identify what caused that damage and how we can prevent it if possible.

## Issue Status

2/24: CW was delivered to ENG 
2/25: CW’s webpage does not read voltage. Removing center panel for further inspection
26 AWG wire that connects from the AS150 to the 2P latched molex does not have continuity

## Comments (23)

### Alexander Alan Arnold, 2025-02-03

@Greg Fryer I have attached the AAR from the aircraft. The customer is stating that CW is incorrectly reporting HLB status, and they cannot continue through the launch wizard. Pleased let me know if you need anything else.

### Greg Fryer, 2025-02-03

@David Grosher will need a data look to see if we can tell what’s happening

### David Grosher, 2025-02-03

@Alexander Alan Arnold @Pat Wells Can they successfully use a different battery? I just want to understand if the severity is set correctly. It seems like this should be lower.

### Alexander Alan Arnold, 2025-02-03

@David Grosher No this has been happening with a few other batteries. They place the supposed “bad” battery in a different aircraft and the issue does not exist.  I have added two screenshots the customer provided.

### Ruysser Gabler, 2025-02-04

@David Grosher This seems similar to the issue that we had with the CW on 689 while doing MAGNSS testing before the deliverable was due. https://jenaero.atlassian.net/browse/VXEP-542?atlOrigin=eyJpIjoiMGE2NGUyZDliYjhlNDFhN2E4NzBiOTJjNmYxMmU2ZTgiLCJwIjoiaiJ9

### Cameron Chapman, 2025-02-04

The measurement definitely seems off. The log times also don’t match up. The bms value is likely much more accurate, as it is measured on the battery. 
@Alexander Alan Arnold how many vehicles and batteries do they have? This would be a quick way to isolate the problem parts. I am guessing more likely in the CW. FYI @David Grosher 
- New CW with the same battery and fuselage.
- They could also measure the voltage at the boom connector.

Further data review
- Vtvbatt is calculated using vref. If that looked abnormal compared to other vehicles, it could indicate a wiring issue.

[embedded: image-20250205-045809.png]
[embedded: image-20250205-050221.png]

### Alexander Alan Arnold, 2025-02-05

@Cameron Chapman I will ask what they have available but as stated in my previous comment they have already placed the supposed “bad” HLB in a different aircraft and had no issues during ground checks on a different system, so it does seem isolated to the 401 CW.

### Cameron Chapman, 2025-02-05

Thanks @Alexander Alan Arnold. Understood. The main thing left to test in the field is to isolate it to the CW independent of fuselage. Could we then return the CW for investigation?

### Alexander Alan Arnold, 2025-02-05

@Cameron Chapman I am having the customer begin the RMA process to have the CW returned to SLO. I will update you when we know it is being returned.

### Adrian Garcia, 2025-02-19

Typically Vref follows the inverse curve of VBatt and is in the negative range as seen in the first two graphs. V401 does not follow that. It seems like it reinitializes, but it does not go down to zero so I can not tell if that is the case. Maybe @Jason Scherer might answer that better. My next steps are to try to replicate this first and then check the current sensing harness once the CW is in house. 

[embedded: image-20250219-210418.png]
[embedded: image-20250219-210444.png]
[embedded: image-20250219-210459.png]

FYSA @Cameron Chapman @David Grosher

### Rodney Linch, 2025-02-24

@Cameron Chapman - VXE-401 CW arrived today. With this VXEP ticket logged, I am taking the Center Wing to the Engineering Drop-Off table. Please let me know if you have any questions.

### Cody Smisek, 2025-02-24

@Rodney Linch @Cameron Chapman 
When bringing equipment over, please add tags or something that identifies the equipment as customer hardware. We have a significant amount of customer assets in engineering now, mixed in with Edge owned equipment. 
I have been adding customer property tags to anything that I get involved on. 
@Greg Fryer @Pat Wells @Adrian Garcia

### Cameron Chapman, 2025-02-24

@Rodney Linch can you please add tagging customer equipment to your process/checklist when delivering equipment to engineering?

### Adrian Garcia, 2025-02-25

I connected the Center Wing to the Iron Bird and powered the avionics box and center wing’s power connector to emulate the battery using two different power supply, but the voltage was not being detected on the webpage. I will remove the center panel and test for continuity to check if anything is disconnected in the VREF circuitry: 
FYSA @Cameron Chapman @David Grosher

### Adrian Garcia, 2025-02-25

@Cameron Chapman @David GrosherI tested for continuity across the power and ground bus in the Center Wing and found no continuity in the highlighted harness. This fault closely resembles—if not exactly matches—the issue that @Jeremy Kostel  and I previously investigated, where the 26 AWG wire connecting ground to the CSB was disconnected. I have linked that investigation to this one for reference.https://jenaero.atlassian.net/browse/VXEP-551. 
[embedded: image-20250225-222920.png]

### Cameron Chapman, 2025-02-25

@Adrian Garcia good updates. For this issue and the other one, if we carefully probe and/or disassemble, we should be able to identify exactly where the wires are breaking, solder is incomplete, etc. This will be important for the CA for both. Can you please investigate. Laszlo may be able to help carefully disassemble. We want to try to maintain evidence. With 2x of this issue recently, it seems like something recently changed (assembly, installation, parts, etc).

### Cameron Chapman, 2025-02-25

@Adrian Garcia if we can prove the issue is resolved with a replacement, then we could remove the faulty part for investigation and return the aircraft for RMA. Doing this should always be the priority.

### Adrian Garcia, 2025-02-28

@David Grosher @Cameron Chapman , @Giovanni Gonzalez replaced the Dual Current Sense board and tested the center wing using a power supply to verify if the battery voltage would be accurately read on the VTOL webpage. The test was successful, and the system correctly displayed the power supply’s voltage. The current sense board now needs to be sent back to RMA for proper reintegration per standard procedures. I recommend performing a pre-flight check before returning the unit to the customer if it not already in the procedure.
FYSA @Rodney Linch

### Cameron Chapman, 2025-02-28

Thanks @Adrian Garcia. Good find. We should keep the broken one and this investigation open to try and determine what on the DCSBA broke and how. Previous flight data or questions to the customer may help. There is some risk returning the aircraft back without knowing what was damaged, but it is likely low. I think ok to return the aircraft and keep the damaged equipment for investigation.

### Adrian Garcia, 2025-02-28

Sent center wing back to @Rodney Linch with the new current sense board that I received from inventory. 
FYSA @Cameron Chapman @David Grosher

### Lauren Velasquez, 2025-03-25

@Adrian Garcia Was there travelers for this?
@Rodney Linch FYSA

### Jackson Riley Curvin, 2025-12-01

[embedded: VXE 401 Centerwing failing to report proper VTOL battery state.pptx]

### Jackson Riley Curvin, 2026-07-13

Corrective action was canceled, report sent to customer.

## Attachments (10)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| Battery issue.jpg | image | 389 | 2025-02-03 | listed only |
| T95_V401_250203_135049_pack.zip | archive | 1227 | 2025-02-03 | listed only |
| launch wizard low battery.jpg | image | 457 | 2025-02-03 | listed only |
| image-20250205-045809.png | image | 44 | 2025-02-04 | listed only |
| image-20250205-050221.png | image | 38 | 2025-02-04 | listed only |
| image-20250219-210418.png | image | 36 | 2025-02-19 | listed only |
| image-20250219-210444.png | image | 31 | 2025-02-19 | listed only |
| image-20250219-210459.png | image | 39 | 2025-02-19 | listed only |
| image-20250225-222920.png | image | 109 | 2025-02-25 | listed only |
| [VXE 401 Centerwing failing to report proper VTOL battery state.pptx](attachments/35079_VXE%20401%20Centerwing%20failing%20to%20report%20proper%20VTOL%20battery%20state.pptx.md) | pptx | 3325 | 2025-12-01 | converted |
