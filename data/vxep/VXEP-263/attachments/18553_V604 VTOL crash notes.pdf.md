# V604 VTOL crash notes.pdf

Attachment 18553, pdf, 313 KB, added 2024-01-31 by David Grosher.

## Page 1

Observations: 
1. VTOL AP reset after hitting the ground. A large jerk was measured and logged. This leads the flight 
data analysis tool to not plot the correct file. 
2. There is no Crash report following the reset. The VTOL AP did not power up for more than 6 
minutes. 
3. The XCOMM does not reset.
4. The XCOMM indicates an airspeed fault before the event: [23:22:07.709 3328.710] ap dbg: 
airspeed fault detected
5. No obvious indication of nudge
6. An RTC update occurred during the flight
7. Prior to saying the vehicle landed there was a sequence of messages saying the vehicle was made 
safe: 
[23:22:14.857 3335.857] RCS_SAFE 1
[23:22:14.858 3335.858] DebugMsg SAFE ON
[23:22:14.861 3335.861] RCS_ARM 0
[23:22:14.862 3335.863] DebugMsgInt CMD ARM: 0
This was a message from the FW AP to the VTOL AP and caught by XCOMM
8. Indicated crash time on the VTOL AP: [15:22:09.345 3015.345]
9. Land task begins on the XCOMM: [23:22:19.117 3340.117] veh state says landed -113  48  -1  2  
121
10. The airspeed fault detection is a detection on the last received airdata packet timestamp. This 
data is received by the FW AP from XCOMM. 
a.
11. If the UTC time between XCOMM and VTOL AP is synced then the airspeed air would have 
occurred prior to the crash. Should this be reflected in the VTOL AP?
a. The last Landing pause command at XCOMM is at [23:22:08.053 3329.053] RCS_PAUSE 0
b. The last landing pause command in the VTOL is at [15:22:09.184 3015.184] mc land paused 
10000
c. VTOL AP appears to be 1 second behind the XCOMM, which would indicate that the airdata 
error happened just before the crash. Hard to be sure it was before. The link faults supports 
that the Air data on the can was lost prior to the crash. 
12. There are a number of faults and flags that go high on from the VTOL. IDENTIFY THE FLAG 
MEANINGS. 
13.
14. On the VTOL data log it looks like the current is spiking and voltage is dropping as the datalog 
ends. Possibly indicating a power failure or drained HLB (although the voltage has been lower 
before in good datasets).  Last datalog was at CPUTIME 3013.367 (about 2 seconds prior to the 
last entry in the event log)
V604 VTOL crash after burst
Tuesday, January 30, 2024 7:43 PM
   Quick Notes Page 1

## Page 2

last entry in the event log)
15.
16.
Questions: 
1. The Airdata from the XCOMM should not be required but may be indicative of another failure. The 
Airdata is on the CAN bus.  What power bus is the airdata on?
2. How is XCOMM and VTOL APs synced via UTC time?
   Quick Notes Page 2
