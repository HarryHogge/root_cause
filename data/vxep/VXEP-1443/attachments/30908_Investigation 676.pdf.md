# Investigation 676.pdf

Attachment 30908, pdf, 388 KB, added 2025-07-23 by David Grosher.

## Page 1

SW is v6.3.4 -
Note: There are Mag robustness deliveries in v6.4
AAR to be delivered from TIQ
Issues to look into:
1. [DONE] Correct Version?
a. Yes, MoD is on v6.3.4 and awaiting approval of v6.4
2. [WIP] Bad Mag Warning (Note: There are Mag robustness deliveries in v6.4)
a. I think in v6.3.4 the FW AP used the FW Mag and that VTOL would fail over to the FW mag. 
i. All of the AP IMU Bxyz were zero, is this expected? Yes, this is expected in 
ii. The data looks good, the warning may have been related to a bad sample on VTOL AP which isn't always 
logged, this was fixed in v6.4
iii. Verifying that all of the attitudes line up between FW AP and VTOL AP. 
3. [WIP] Poor Flying qualities
a. Poor IAS Tracking - Tracking appears OK but command seems to vary between 69 and 53 (fps) Dash and Cruise
i. apSpdMode switches to 3 (CRUISE) during this time. 
ii. See FW AP - oloop.c Airspeed()
1) The command will be slewed and switched between a Climb and Cruise. 
2) OverrideSpeed
3) AutoAirspeedAdj
b. Poor Flight track performance - No indication of an inability to track the flight path, perhaps the commanded 
flight path was not clear to the operator? There appears to an oscillation during time when airspeed command 
is changing where the X/Y flight path track is not tracked as expected. I think this might be an orbit, need to 
confirm. If not this may be the erratic behavior.  It appears to be an orbit during these times. 
i. During the period of poor flying qualities it appears to be in the following modes
1) 2 - Fly to a waypoint 
2) 3 - Orbit
3) 5 - Orbit down
4) 6 - fly along track - During lost comms
c. Crabbing in orbits - There was increased Ay during the latter portion of FW flight. It is unclear if this aligns with 
the same period of time above. 
4. [WIP] Lost Comms (See below)
a. Confirmed seems to be in and out, which may be why it didn't perform expected Lost comms actions. 
i. Check Silvus configuration.
b. Log does show about 9 minutes of comms out. The data rate is slow so it could have still been in and out.
c. Fly along track during lost comms per apMode. 
d. LosRtbActiveLz=0 In last Mission file
i. Given settings what is the expected behavior? 
e. Altitude does seem to have increased during LOS
5. [DONE] Did not land at the updated PLZ
a. Mission.txt on the XCOMM SD card has the Lat/Lon of the last mission 
i. Lat=51.227595, Lon=-1.875112
ii. This is within the walls of the facility. The AP never received the updated PLZ. 
iii. Perhaps it was not uploaded? 
The link was confirmed to be lost. It appears that it was in and out. Check Silvus configuration. 
GCS link is XCOMM SW2 Port 4
The AP IMU Bxyz are all zero, is this v6.4+
Aircraft IAS Command is varying
The aircraft doesn't appear to be flying erratically laterally
Investigation 676
Tuesday, July 22, 2025 1:41 PM
   Quick Notes Page 1

## Page 2

Altitude appears to increase during lost comms
   Quick Notes Page 2
