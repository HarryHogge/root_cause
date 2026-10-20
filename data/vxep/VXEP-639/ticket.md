# VXEP-639: VXE 515- HLB Unexpected Voltage fluctuation. Aircraft flown multiple times after, leading to damage

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed, but added to Bermuda Triangle List
- **Resolution:** Cannot Reproduce
- **Priority:** High
- **Created:** 2024-09-19
- **Updated:** 2026-03-02
- **Resolved:** 2025-05-21
- **Reporter:** Alexander Alan Arnold
- **Creator:** Alexander Alan Arnold
- **Labels:** USASOC, Weekly-incident-tracker
- **Links:** relates to VA-573 (Poor Quality/higher impedance plating on AS150 power contacts - Containment and Corrective Action); relates to VXEP-282 (VXE 533 VTOL power issue on transition led to Uncontrolled drift and crash on landing); relates to RMA-438 (VXE-515 USASOC 241209-5 GW)
- **Customer:** USASOC
- **Vehicle Tail Number:** 515
- **Vehicle Configuration:** Battery Only
- **Incident Type:** Mission Failure/Abort
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

Sharepoint Files: https://jenaero.sharepoint.com/sites/FlightSafety/Shared%20Documents/Forms/AllItems.aspx?csf=1&web=1&e=dp79vR&CID=9bd3abdd%2Dfb01%2D46ba%2D838d%2Daa9ec6c9c424&FolderCTID=0x012000D03119522A011A40817D7F0F59E3A7EF&id=%2Fsites%2FFlightSafety%2FShared%20Documents%2FIncident%20Reports%2FVXE%20515%2D%20HLB%20Unexpected%20Voltage%20fluctuation%2E%20Aircraft%20flown%20multiple%20times%20after%2C%20leading%20to%20damage&viewid=7181a7a2%2Dd286%2D47c9%2Dbdd3%2D9195ef18282c 
Working Report: VXE 515- HLB Unexpected Voltage fluctuation. Aircraft flown multiple times after, leading to damage Investigation Report.docx
Report from Operator
For everyone's SA, we had an issue with an HLB today. After transitioning to fixed wing the battery percentage drained quickly down to 19% while we were climbing to altitude. Then it started climbing to 45% and just continued to bounce between 19-45% while the voltage flickered from 24.5-27.3. We decended back down to pattern altitude to land and while we did that it claimed back up to 76% and stabilized. We vtol landed with no issues and swapped HLB's and it didn't happen again when we put it back up. We marked the battery and we're guna send the flight data back to WOC Collins.
Statement confirmed by data 

[embedded: image-20240919-203942.png]

*AAR Attached

## Plan

This looks like it could be the common AS150 issue, but the symptoms look a little different (voltage fluctuations with no load) and may be related to some other issues where voltage fluctuation has been seen.
Updated 10/17/24
- Perform steps that Cameron listed in comments:
- Something is clearly going wrong with the voltage measurement here that is not related to bad contacts (bad contacts will cause voltage drops with current). This voltage fluctuates without VTOL current. (plot vs fixed wing voltage and current). It could be both bad contacts and something else.
- It seems to be directly related to Vref measured, so the issue seems to be in that circuit, grounding issues, etc.
[embedded: image-20241015-181309.png]
 
[embedded: image-20241015-181321.png]
- Physical investigation. Vehicle in SLO
- @Lauren Velasquez can you please link the RMA. The linked one is for 515.
- Inspect battery and CW power contacts for any damage, burning smell, visible solder, etc.
- Inspect/test ground isolation circuitry to ensure it is working properly.
- Inspect HLB since replacing HLB seemed to have resolved the voltage fluctuation issues in the field.
- A launch wizard motor spinup with the same battery compared to another could be a good way to isolate it to the battery or not (but this may not be enough power to cause the issue). A strapped down simulated launch would be, but we have never had customers do that, and it requires a quick abort not to overcurrent/temp components.
- Return CW. Perform inspection and impedance test.
- Link to confluence doc for inspecting good/bad contacts.

## Issue Status

VXE-515 was a Goodwill Replacement Aircraft that has been in and out of RMA already. The replacement aircraft shipped mid April. CW never made it back overseas so we have no way of inspecting it. 
Per Drew Hildreth, if the center wing is required to finish this investigation we should lean on closing it out without action and should it pop back up, we can reference it again.

## Comments (35)

### Alexander Alan Arnold, 2024-09-19

@Greg Fryer 
Sorry but it would not let me upload the zip file for some reason. I have attached everything the operators sent me.

### Pat Wells, 2024-09-19

@David Grosher added correct AAR zip file.

### Cameron Chapman, 2024-09-19

This looks like it could be the common AS150 issue, but the symptoms look a little different (voltage fluctuations with no load) and may be related to some other issues where voltage fluctuation has been seen. @Alexander Alan Arnold where is this aircraft and HLB located? 
- I recommend the following ASAP. Ground and quarantine the HLB and CW involved ASAP until the following are determined.
- Inspect battery and CW power contacts for any damage, buring smell, visible solder, etc.
- Evaluate sending FSR out or both back to SLO or HSV for inspection, impedance test, etc
- @Adrian Garcia can you please link this to other issues with similar VTOL voltage fluctuations, further look into this flight data, and recommend next steps?


[embedded: image-20240919-203120.png]

### Alexander Alan Arnold, 2024-09-19

@Cameron Chapman CW and HLB are currently overseas with a deployed military unit. I will pass on the information to the unit POC.

### Cameron Chapman, 2024-09-19

Thanks @Alexander Alan Arnold. It is difficult to tell what is causing this behavior from data, but historically it has more often been an issue in the CW than the battery. Can you also please ask them to upload data from the following flight?

### Alexander Alan Arnold, 2024-09-19

@Cameron Chapman 
zip ending in 102123 Is same CW different battery and the same issue
zip ending in 112150 is the same CW different HLB and this time the aircraft executed an emergency landing resulting in damage to aircraft.

I have told the Operators to stop using the CW associated with this behavior. I am currently awaiting operator statements and pictures from emergency landing. We have also asked for pictures of CW power connector

### Cameron Chapman, 2024-09-19

Thanks @Alexander Alan Arnold. It sounds like we should add/emphasize in training that voltage fluctuations like these or other anomalies should ground an aircraft until review is complete confirming ok to fly. Please also include description/photos of damage and coordinate a RMA with @Sean Odell if needed.

### Cameron Chapman, 2024-09-19

@Alexander Alan Arnold the same behavior with multiple batteries seems to indicate the issue is in the center wing. I recommend either sending the whole aircraft back, or at minimum the center wing.

### Adrian Garcia, 2024-09-19

@Cameron Chapman @Alexander Alan Arnold I am unable to download the AAR zip files.

### Alexander Alan Arnold, 2024-09-19

@Adrian Garcia Which zip specifically or is it all of them? 
I have had issues recently since the zScaler download psuhed to my computer. I can try and email them to you if you would like.

### Alexander Alan Arnold, 2024-09-19

@Cameron Chapman I told them to stop using the center wing immediately. I will talk with them about the possibility of getting it back to us. but it may take a while since they are deployed.

### Cameron Chapman, 2024-09-19

@Alexander Alan Arnold I provided the zip files to Adrian. Working for me.

### Adrian Garcia, 2024-09-19

Some quick data review before I leave for the day. This is from the AAR ending in 112150. BMS voltage is reading as expected and looks normal, but VBAT on the VTOL AP board is showing a weird upside down parabola that I have not seen yet suggesting that the voltage is charging up then discharging in-between landing and takeoff could also be from the AS150 connecting and disconnecting from itself but I would have to check Ibatt (havent gotten there yet). VBAT also has a sharp drop to ~23.5V which is not seen in the BMS voltage. @Cameron Chapman 

[embedded: image-20240919-225819.png]

[embedded: image-20240919-225824.png]

[embedded: image-20240919-225837.png]

### Adrian Garcia, 2024-09-20

@Cameron Chapman I created an investigation folder linked above and added my data with graphs in there as well. In both AARs Vbatt fell down to about 23V and during fixed wing the HLB would recharge and discharge. Also during takeoff the current would peak above 200A (this could be because a payload was mounted but I am unable to confirm). Furthermore, the BMS voltage does not necessarily line up with VBatt, Id say there is a 2V difference. Something else I found interesting was that VREF was positive, which in my experience has always been negative. My suggested next steps would to perform a pull test on on the HLB is we can get it, a resistance check on the power harness, and ask software to review the event logs. After that I think it would be worth while to check the current sensing circuit since that is where VREF is located. 
Another finding is that the yaw in the emergency landing AAR had a lot of oscillation but could be caused from environmental issues

### Cameron Chapman, 2024-09-20

@Adrian Garcia please start a word doc investigation from the template. It can be a rough draft for now, but a good way to collect data and observations

### Adrian Garcia, 2024-10-08

@Sean Odell Do we have the aircraft on sight or any update regarding its location?

### Adrian Garcia, 2024-10-10

On hold until aircraft is on sight

### Cameron Chapman, 2024-10-15

@Adrian Garcia recommendations when you are available to work on this again.
- On each of your plots and the test report, report what flight it was on. Date, if it was in the incident, etc.
- Something is clearly going wrong with the voltage measurement here that is not related to bad contacts (bad contacts will cause voltage drops with current). This voltage fluctuates without VTOL current. (plot vs fixed wing voltage and current). It could be both bad contacts and something else. 
- It seems to be directly related to Vref measured, so the issue seems to be in that circuit, grounding issues, etc. 
[embedded: image-20241015-181309.png]

[embedded: image-20241015-181321.png]
b. Please update the plan and status fields every time you work on an investigation. I have said this many times. 
- Added to investigation checklist. Please use and update that. EE Checklists.xlsx

### Mark Squillante, 2024-11-12

@Cameron Chapman @Adrian Garcia this looks to me to be an issue with grounding or VREF (measured ground voltage). I’d be curious to see whether the ground isolation board is connecting the HLB and main battery grounds or leaving the 100 ohm resistor in the path. I do not think this is an AS150 contact issue. I would like a chance to look at the CW when it gets here.

### Cameron Chapman, 2024-11-12

Thanks @Mark Squillante. The AWHLB CAN connector also bypasses the ground isolation board (not on purpose). I am curious if that could be negatively affecting things, especially if connected in different orders.

### Mark Squillante, 2024-11-13

@Cameron Chapman @Adrian Garcia I found that one of the VTOL logs showed very high voltage on VREF. Typically it’s in the tens of millivolts range, here it was ~2V. I plotted that along with HLB voltage and the fluctuations definitely track, indicating a problem with VREF. 
It’s interesting that the problem was resolved by switching to another HLB. That points to HLB as likely the problem. I would be interested in checking out the HLB if possible.
[embedded: image-20241113-195006.png]

### Adrian Garcia, 2024-11-13

@Mark Squillante We probably wont be able to the HLB since it was in an accident and they are not allowed to be shipped over flight. I definitely agree that something is going on with VREF

### Cameron Chapman, 2024-11-14

@Mark Squillante @Adrian Garcia strange if the HLB could affect this, since all HLB should have the same grounding, but it is possible. You could look into the HLB schematic, perform some measurements here on another one, and recommend measurements for the customer to perform overseas using the equipment they have (battery checker, charger, they could maybe use a DMM to probe checker terminals, but this might not be safe).
Please update the plan section every time you work on an investigation. I have asked this many times.

### Adrian Garcia, 2024-11-14

@Cameron Chapman @Mark Squillante Spoke to @Sean Odell about when the vehicle would arrive on sight and he stated that since it is over seas it may take around 6 months to arrive. Additionally the customer has not requested an RMA yet. 

The last time I worked on this issue was 10/17 and crossed out all items that have been completed. I did not want to delete them incase they are important later on and useful for documenting what has been done before. 
@Pat Wells FYSA

### Cameron Chapman, 2024-11-14

Sorry @Adrian Garcia. You are right. I think I mixed up this investigation with one where the aircraft recently arrived.

### Lauren Velasquez, 2025-03-17

@Adrian Garcia @Cameron Chapman  This AC has arrived- RMA will be doing standard intake (as much as possible with severely damaged AC) and then Delivering to Engineering area, unless otherwise requested.

### Alexander Alan Arnold, 2025-04-08

@Cameron Chapman Since this AV is in the waiting area at SLO will you assign it to a member of the EE team and continue investigation?

### Alexander Alan Arnold, 2025-05-06

@Steve Gonzales Have you had chance to look into this one any? I know you've tasked with other items just checking in on this one.

### Steve Gonzales, 2025-05-06

@Alexander Alan Arnold 
I have only looked at the logs so far, voltage should be at zero, root cause TBD.  5/13 correction; code for Vref performs calculation to log correct vbatt value.  Definition needs an update in VTOL decoder.  This chart is normal then. RCA still TBD. 
[embedded: image-20250506-164103.png]

### Cameron Chapman, 2025-05-13

@Steve Gonzales when do you think you will have availability to work on this?

### Steve Gonzales, 2025-05-13

@Cameron Chapman I have started on this one previously.  I can continue today on it as well with vehicle 489.

### Cameron Chapman, 2025-05-20

@Giovanni Gonzalez Steve is out this week. Are you available to work on this?

### Giovanni Gonzalez, 2025-05-20

@Cameron Chapman Vehicle has still not arrived to RMA in SLO, will inspect upon arrival

### Drew Hildreth, 2025-05-20

@Giovanni Gonzalez VXE-515 was a Goodwill Replacement Aircraft that has been in and out of RMA already. The replacement aircraft shippeed mid April. I just talked to Lauren and she thinks they have what you need. If there is something else that you need. please reach out or tag me and I will do my best to get you whatever it is in a timely manner. 

On a side note, I have two FSR’s in SLO this week working with FLOPS that may also be able to assist if they are in the building.

### Drew Hildreth, 2025-05-21

This aircraft was replaced. The center wing never returned. IOT continue RCA center wing is required. This ticket will be closed with no further action required.

## Attachments (12)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V515_240917_113259_pack.zip | archive | 3219 | 2024-09-19 | listed only |
| T95_V515_240919_102123_pack.zip | archive | 2107 | 2024-09-19 | listed only |
| T95_V515_240919_112150_pack_Emergency_Landing_Damage.zip | archive | 5312 | 2024-09-19 | listed only |
| image-20240919-203120.png | image | 46 | 2024-09-19 | listed only |
| image-20240919-203942.png | image | 54 | 2024-09-19 | listed only |
| image-20240919-225819.png | image | 46 | 2024-09-19 | listed only |
| image-20240919-225824.png | image | 19 | 2024-09-19 | listed only |
| image-20240919-225837.png | image | 44 | 2024-09-19 | listed only |
| image-20241015-181309.png | image | 24 | 2024-10-15 | listed only |
| image-20241015-181321.png | image | 33 | 2024-10-15 | listed only |
| image-20241113-195006.png | image | 79 | 2024-11-13 | listed only |
| image-20250506-164103.png | image | 26 | 2025-05-06 | listed only |
