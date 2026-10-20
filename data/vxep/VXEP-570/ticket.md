# VXEP-570: VXE 514 overheated on ground and damaged SOFC components

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-08-28
- **Updated:** 2026-03-02
- **Resolved:** 2025-02-25
- **Reporter:** Pat Wells
- **Assignee:** Sean Wendling
- **Creator:** Pat Wells
- **Labels:** USASOC, Weekly-incident-tracker
- **Links:** relates to RMA-336 (D4500630 240905-4 Fuel Cell); relates to VXEP-714 (Generate Table for all Fuel Cell Fault Codes to XCOMM and user action items)
- **Customer:** USASOC
- **Vehicle Tail Number:** 514
- **Production Stakeholder:** Robert Redfield
- **Other Stakeholder (as required):** Sean Wendling
- **Issue Status:** AC Repaired, Fuel Cell to be returned to Ann Arbor for repair.
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

1st SFG

Statement from Instructor: 
When trying to fly the SOFC bird, AC 514, we initially ran into a fault at the first pitot shield in the launch wizard. We were already in the middle of warming up the fuel cell, but had to  recycle power on the aircraft. Once regaining link to the bird we immediately started the fuel cell via the fuel cell control window to avoid any unnecessary cycles on the cell. After restarting the launch wizard I noticed the aircraft health window showed a blinking error rather than showing the charging status (/initializing/ warming up etc..) of the fuel cell. Conversely, the fuel cell control window showed a green (no fault) indicator. I logged into the xcom to see which window was correct since the battery was taking a charge. The xcom had 9360 under the fault code.
 
At this point, I walked out to the aircraft to see if everything looked and sounded copasetic and noticed light smoke coming out of the fuselage via the exhaust ports. The top of the fuselage was too hot to touch, so I immediately shut down the fuel cell and when cooled removed it from the aircraft for inspections of both. The aircraft interior and associated cabling seems to be fine with only some bubbled paint around the exhaust ports. The fuel cell has melted plastic of some sort running down the heat shielding and per your instruction will be added to the RMA with the 2 AC with bad sim cards.
 
Due to several software and aircraft restarts, there are multiple fdr files. I downloaded all files from the xcom that had today's date on them to make sure you have all available data.

Data attached

## Corrective Action

On Immediate Unit: Replace the Front Nose Cone Fan.
For Continuous improvement: Improve GCS to include fault code transcription for all users to be able to identify cause of faults, and actions they need to perform for each fault.

## Plan

- Data review. @Sean Wendling
- Airworthiness of AC - Upon replacement of the Nose Cone Fan, AC should be safe to return to use.
- Investigation of Root Cause - Root Cause determined to be failure of the Nose Cone Fan.
- Return of the Fuel Cell. @Sean Odell 
- Performance in this flight appears healthy, need to verify stack health and repair melted materials for customer return.

## Root Cause

Failure or non-operation of the Nose Cone Cooling fan, resulting in lack of active cooling in fuselage during Fuel Cell operation causing overheat. Internal Fuselage temperature reaching temperatures >100degC.
Additionally, without information about specific Fuel Cell Fault, the operators restarted the aircraft after seeing fault 9360, causing the system to melt.

## Comments (6)

### Pat Wells, 2024-08-28

@Sean Wendling  FYSA

### Sean Wendling, 2024-08-28

I suspect that there is indeed an issue with nose cone cooling fan. Its difficult to see through the losses of connection with the AC, but I can observe the fuselage ambient temperature climbing throughout the warmup consistent with the behavior we see without a nose cone fan. The Fuel Cell fault code indicates excessive board temperature (amb temp on the xcomm) and begins to shut down. I am not sure if this is a result of the loss of connection with the AC, or not. But I do see an indication in the Data (supFanEn) that the AC was attempting to power the nose cone fan throughout the fuel cell warmup. GRAPH Attached.
I cannot speak for certain to the specifics of nose cone fan function, but checking to ensure nothing is interfering with the fan physically, and possibly a replacement would be a good course of action until we can completely verify whether its safe to operate with a fuel cell. 
NOTE: Fuel Cell itself, aside from damage to Nylon components from the heat, appears to be in good health.

### Cameron Chapman, 2024-08-28

@Sean Wendling there are some nose cone fan statuses in the data logs. What do those indicate? We had a similar event on Havoc where the fuel cell fan was not enabled where it should have been. @Carl Graf was that incident and CA recorded?
VXE-FCD-XCOMM Log Glossary.docx
supFanEn            Ditto, fuel cell cooling fan.
I12V                 Measured 12V supply output current, amps. 12V_CURR. Measures blinker pwr, SA cam, fuel cell fan, see VXE30 POWER TREE 107-100444.vsdx
fltV12                    power supply overcurrent fault detected. 12V supply.

### Jeremy White, 2024-08-28

I received a Nose Cone Fan and four new screws today and will bring them with me to the end of NET training to replace the Nose Cone Fan in their spares kit.

### Sean Wendling, 2024-10-01

@Greg Fryer  & @David Grosher , not being a part of SLOs sprint setup, how would you like me to create the corrective action tasks to address the reading of Fuel cell faults and displaying warnings to the user? I think it might be larger project, so I dont want to make one blanket task that isnt compatible with how you guys do things. I can create a task for myself to get warning messages created for all the possible fault codes, but I dont exactly know what goes into getting them added to GCS resource planning.

### Alexander Alan Arnold, 2024-12-10

@Sean Wendling Were you able to make progress on your corrective action plan?

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 1.jpg | image | 757 | 2024-08-28 | listed only |
| 2.jpg | image | 873 | 2024-08-28 | listed only |
| 514 SOFC.zip | archive | 457 | 2024-08-28 | listed only |
| TemperatureGraph_VXE-514.png | image | 298 | 2024-08-28 | listed only |
