# VXEP-779: SLO - Ground Battery System Integration Testing

- **Issue type:** Epic
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Highest
- **Created:** 2024-11-15
- **Updated:** 2026-03-30
- **Resolved:** 2026-03-30
- **Reporter:** Jeremy Kostel
- **Assignee:** Jeremy Kostel
- **Creator:** Jeremy Kostel
- **Parent:** VXEP-752 Integrate Amprius Heavy Payload Main Battery for Hatchet+AEWE demos and future use 
- **Links:** relates to VA-1915 (Find/build a better battery cell voltage/temp logger); blocks FS2-2557 (Heavy Lift Battery Safety of flight test)
- **Epic Status:** To Do
- **Epic Color:** ghx-label-12
- **Issue color:** grey
- **Issue Status:** Waiting for battery to be delivered to SLO. Hoping to start test 1 on Monday

## Description

Requirements from Jeremy:
- Make any required GCS battery adjustments for the new battery.
- Confirm available payload weight.
- Provide max endurance estimate. 
- This requires more testing to be able to use the whole battery. Do you want us to continue that testing, estimate what is currently available (we have to reduce battery capacity to not hit the motor shutoff), or estimate what should be available?
- Provide limits and procedures for required battery level, wx, or other performance limitations.
- We shouldn’t need 2 flight hours for the integration nor demo flights. 
- Integration event. 1 hour of flight would be ok.
- What are the required and nice to have durations for the integration and demo flights?
- Would we want to reduce environmental limits (winds) to enable longer flights, or better to reduce endurance and keep? The endurance is reduced as winds increase. 
- Sept 28/29. 2 days at AEWE.
- Orbital: Need to fly in all approved conditions. Probably quick flights. 1hr likely. 800-1200ft.
- Hatchet is much higher, probably not realistic for VXE30 and this battery.

## Plan

Link procedure, requirements, and test data sheet here. 
- Prototype Main Battery Test Plan - Heavy Payload Main Battery.docx
- Previous testing Amprius 30V Model and Misc Calcs.xlsx
- AA Testing: HPMB SN 8-0001 Test Report.docx
- Fit check
- Charge battery. Configuration settings should be set to 7S, 29.4V max voltage, 9A charge rate.
- Run Discharge profile that matches AA ESR test with battery in vehicle.
- Load AA ESR measurement before the test.
- Discharge ~300W to 0% SOC with intermittent high current spikes.
- Validates AA testing and calculations as seen by the aircraft.  
- Link procedure. Add SOC range here. Verify cruise levels and test at that range.
- Aircraft Low Voltage No Load Test-skip if test 4 voltage stays above min voltage tested previously.  
- already performed - need to link jira ticket
- Aircraft Integrated Battery Test
- Recharge to ~10% SOC.
- Ramp throttle to 100% for 10 seconds. This step is to verify max power at lower SOC.
- acceptance criteria: >500W @ 1% SoC
- @Eric Brewer  can you please take a look at this data? it looks like this battery is not as linear as the baseline Amprius ones. Can you please review to see if we can improve with paramater changes, if it is good enough, or if we should make model changes?


11/21 Testing plan:
The goal of this test is to detmine at what vehciel reported SoC the vehcile will pull the battery voltaeg down to 18V while commanding full power on the FW system. Proceedure:
- Start with  ~50% mfg SoC (~35 vehicle reported SoC)
- Command full throttle for ~3 minutes or until Vbatt reports 18V
- command 350W for ~30s
- repeat step 2 and 3 until test complete

## Comments (10)

### Jeremy Kostel, 2024-11-19

Test 1: Vehicle Level ESR Testing
- During testing, about ~15 minutes in the GCS lost connection to the aircraft
- This happened earlier in the day as well, but it was after a power cycle and was written off as abnormal but not problematic
- Post this happening, ethernet cable was swapped with a different one and connections were checked
- Battery voltage was ~27.6V at the time this occurred
- Last recorded point from data logger: 
[embedded image-20241119-222206.png]
- While recharging the HPMB - a VXE30 main battery was put into the vehicle to see if issues persisted
- Connection was successful
- When running through LW and trying to push ini file to vehicle, this pop up box showed up: 
[embedded image-20241119-220714.png]
- Cody and Artis both have never seen this before, indicating it is uncommon
- “Datalink” at bottom of the screen observed turning yellow at least once during this
- About 3 minutes into running the motor at ~300W (28V) the FWD motor began to cut in and out
- Was being commanded by RC
- RC window never showed any throttle cutouts - stayed at constant commanded value
- Cutouts happened sometimes for ~20s and up to a minute of time
- Motor prop fault? Was under the impression this didnt happen unless throttle was over 55% - we were at less than 40
- also a window popped up showing a failure to download the FDR
- Cody indicated this is somewhat common
- CW was connected but it did not have an ADP which could be leading to issues?
- ADP now installed

The effort now is to establish if this vehicle has inherent issues or if the ini file changes are causing some issues

### Jeremy Kostel, 2024-11-19

Hayden confirmed GCS ini values with Kurt and Eric B. All on the same page there (link ini files)
Now, vehicle will connect to GCS but webpages not working
Will not generate FDR

### Jeremy Kostel, 2024-11-19

After another power cycle, able to connect to GCS but still not webpages. Battery at 28.6V

### Jeremy Kostel, 2024-11-20

- Test 1 Completed (11/19)
- Data can be located here: IRAD - Heavy Payload Main Battery - All Documents
- Vehicle issues attributed to potential hardware issue when connecting via ethernet 
- aircraft is potential payload risk
- able to connect via radio
- Test 2: Aircraft Integrated Battery Test
- started this morning
- 10-1% SOC in 2% increments, tested at 100% throttle for 10s
- using VEHICLE SOC, not battery SOC
- looking for minimum 500W
- See SoC curve vs. No load Voltage for 10% and below here: 
[embedded image-20241120-174418.png]

### Jeremy Kostel, 2024-11-20

Test 2 Issues
- Motor cutouts present at 10% Soc (21V unloaded)
- ramp up to 100% throttle
- likely caused by motorcutoff value in ini file: 17.5V
- Logs show some transients below 17.5
- cell logger does not show cells below 2.5V, but is only logging 1 point per second so could be missing data points
- Ramp causes voltage to be pulled below the cutoff and motor to stop
- GCS then uses unloaded voltage to determine it is ok to start motor again and cycle continues
- Potential solution
- adjust where the bottom of our SoC curve ends. Make it a higher voltage value, so that 100% throttle (which achieves over 500W) can be reached without causing cutouts or other issues with the aircraft

### Jeremy Kostel, 2024-11-21

Data from 11/21 test plan found here: Finding Min. SoC for Flight
Vehicle reported SoC of 35% allows for 2:15s of 1200W

### Jeremy Kostel, 2024-11-22

11/22 testing: Back to vehicle level ESR testing with updated gcs ini file
Updated settings here: 
[VXE_MAIN]
MotorCutoff=17500
MotorStart=20000
BattFull=28700
BattEmpty=22500
BattCapacity=3680
NominalEndure=170
PowerLimit=0
BasePower=0
ESR=30
HybridUpperLimit=0
HybridLowerLimit=0
HybridPowerLimit=0
Spare1=0
Spare2=0
Spare3=0
Options=767
BatteryTable[00]=0
BatteryTable[01]=3
BatteryTable[02]=3
BatteryTable[03]=3
BatteryTable[04]=3
BatteryTable[05]=1
BatteryTable[06]=0
BatteryTable[07]=-1
BatteryTable[08]=-2
BatteryTable[09]=-3
BatteryTable[10]=-3
BatteryTable[11]=-3
BatteryTable[12]=-2
BatteryTable[13]=-3
BatteryTable[14]=-4
BatteryTable[15]=-2
BatteryTable[16]=2
BatteryTable[17]=6
BatteryTable[18]=5
BatteryTable[19]=3
BatteryTable[20]=0
BatteryTable[21]=0

### Jeremy Kostel, 2024-11-22

11/22 testing: Back to vehicle level ESR testing with updated gcs ini file
- Test Start: 8:10AM
- per HJ instructions this test will be slightly different than the previous test:

- 30-second initial pulse at 30 Amps (simulates climb and drives internal heating of the pack)
- 15-minute, 300W load
- 10-second, 30A load
- Continue steps 2&3 until the Main battery reaches 30% SOC
- 20-second, 30A load
- 3-minute, 300W load
- Continue steps 5&6 until Main battery pack voltage reaches ~17.5V or 2.5V per cell

### Jeremy Kostel, 2024-11-22

11/22 testing: Back to vehicle level ESR testing with updated gcs ini file
- Cell voltage logger cut out around 15 minutes into testing - decision was made to restart testing
- cell logger exited monitor mode for unknown reason
- FDR of first 15 min found here: IRAD - HPMB Vehicle ESR Testing First 15 min - All Documents
- Charging battery and restarting
- testing restarted at 9:00AM


Side note, V686 has failed to download FDR on last two attempts

### Jeremy Kostel, 2024-11-22

CRITICAL UPDATE
11/22 testing: Back to vehicle level ESR testing with updated gcs ini file
- during testing, the cell voltage logger lost connection to cell voltage 7
- It was an immediate value of 0V, indicating more likely a connection failure than a cell failure
- total pack voltage did not dip
- Relevant data from cell logger:
[embedded image-20241122-221752.png]
- Post testing, we conducted tests to see where the failure occurred
- pinout of charging harness:
- [embedded image-20241122-221712.png]
- Charging harness proved to still have conductivity but was reterminated anyway. Still has conductivity
- We were able to see all other cell voltages from the 9pin XHP, indicating it was not a grounding issue and all other cells were still reporting correctly
- Finally, we probed directly on the ODU connected to the battery. We were able to read cell voltages 1-6 but not cell 7. Total pack voltage was higher than the rest of the cells showed, indicating cell 7 was ~2.8V, the same as the other cells
- this indicates the failure occurred on the battery harness, not the charging harness
- we do not have direct access to this harness
- Without the cell 7 reading, our charger will not charge (that we know of) because it cannot balance cells. It is possible this could be worked around, by telling the charger it is a 6 cell battery, but this poses risks as there wouldnt be the correct cell balancing and no monitoring of cell 7 voltage
- Leading recommendation right now is to have Laszlo open the battery, as he has experience doing so

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20241119-220714.png | image | 1823 | 2024-11-19 | listed only |
| image-20241119-222206.png | image | 6 | 2024-11-19 | listed only |
| image-20241120-174418.png | image | 23 | 2024-11-20 | listed only |
| image-20241122-221712.png | image | 114 | 2024-11-22 | listed only |
| image-20241122-221752.png | image | 50 | 2024-11-22 | listed only |
