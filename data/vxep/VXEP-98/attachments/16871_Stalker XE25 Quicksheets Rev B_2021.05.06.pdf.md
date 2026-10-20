# Stalker XE25 Quicksheets Rev B_2021.05.06.pdf

Attachment 16871, pdf, 26916 KB, added 2023-10-06 by Craig Burton.

## Page 1

Fuselage
B
P21-05414

## Page 2

(no text on this page; probably an image or scan)

## Page 3

NETWORK ILLUSTRATION
6pin: Enet/pwr
 x=8
6pin: Enet/pwr
x=7
 x=8
Avionics
Xcomm x=2
Encoder x=4
RJ45: Enet
x=100-119
10.128.TAIL#.x
RJ45: Enet
x=100-119
GCS & other computers
10.0.GCS#.x
Comms box
Radio: x=3
IPcomm/DHCP server: x=1
IPComm/DCHP server: x=1
7pin: Enet/pwr/vid
Radio: x=3
Xcomm: x=2
ENTIRE NETWORK SETTINGS
Subet: 255.0.0.0
Gateway: 10.0.0.1
PAYLOAD RESERVED LIST
HD encoders: 10.0.0.60 - 10.0.0.69
WiFi Hotspot: 10.0.0.100 - 10.0.0.110
Wave Relay payload: 10.0.0.200 - 10.0.0.210
E������ N������ IP A������ L���
Airframe tail number 232
and ground station serial number 5
with one extra payload and laptopIPComm
10.128.232.1
Xcomm
10.128.232.2
Radio
10.128.232.3
Video Encoder
10.128.232.4
Extra Payload
10.128.232.8
IPComm Xcomm Radio Ground Station Laptop Payload Operator Laptop
10.0.5.1 10.0.5.2 10.0.5.3 10.0.5.100 10.0.5.101

## Page 4

SPECIFICATIONS
Operational Temperature Range Rain, Hail, Snow, Ice
-4°- 122° F .25 inch/hour Rain/
Snow Only
Maximum Launch Maximum Operating
12,000 ft 15,000 ft
Aloft Crosswind
Launch
20 mph 30 mph 10 mph 0 mph
MGTOW 28.5 lbs (Typical with battery and EO: 26.5 lbs)
Cruise Dash Limit climbs to 2000 ft
30 kts
(34 mph)
39 kts
(45 mph) with 5 min
between climbs
GCS Powered with FCR Battery Laptop Battery (Standalone)
Up to 3 hoursUp to 12 hours
Center Frequencies Bandwidths
40 channels from
2.200 to 2.500 GHz
5,10, 20 MHz
FREQUENCY AND BANDWIDTH ARE SET USING SILVUS WEB PAGE INTERFACE
Launch Tailwind
Launch

## Page 5

LAUNCH
100+ Ft. Field Width
Obstacle height x10 = distance needed to launch ~125 ft.
Bungee Hard Point Release Point
Obstacles
NOTE: Bungee temperature should be 60º+ for best performance. If bungee is below 60º, preheat bungee.
WARNING:
Keep launch area
clear when bungee
is being pulled.

## Page 6

LANDING

## Page 7

BM
346.8
BM
353.8
Fivemile
Bridge
BM
346.8
Fivemile
Bridge
R4
BM
346.8
BM
353.8
Fivemile
Bridge
= Target
= Target
Recommended orbit around a target
is 1200 ft AGL and 500 m radius
or greater to avoid detection.
Adjusting the orbit to 1400 ft AGL
and 250 m radius will alter the slant
angle for a diﬀerent perspective.
A racetrack at 1200 ft AGL and
minimum 500 m oﬀset from the target
can take advantage of sun angle.
Orient orbits and racetracks to
avoid terrain conﬂicts.
ORBITS
BM
346.8
Fivemile
Bridge
R4

## Page 8

TURRET CONTROL BUTTON GUIDE
Look Aft

## Page 9

U-DRIVE AND LANDING NUDGE BUTTON GUIDE
Forward=Shorter
Back=Longer

## Page 10

(no text on this page; probably an image or scan)

## Page 11

TROUBLESHOOTING
No GPS Fix on Ground (fewer than 4 sats for more than 5 minutes)
Mission Simulation Status Warnings and Errors
Failed to Connect With Vehicle
Ensure aircraft has unobstructed view of sky
Cycle power on aircraft
Try moving aircraft 100+ feet away from GCS antenna
If no GPS after this step, suspect aircraft GPS failure as cause; if multiple GPS units
(multiple vehicles, handheld GPS) suspect interference or jamming from unknown source.
Warning - Waypoints closer than 300 ft
Warning - Flight level below 300 ft
View color topo map and alter route or raise waypoints
Software will not allow you to launch with this error
Warning - Loss of line of sight
View color topo map and consider changing route or raising waypoints
Software will allow you to launch with this error
Error - Not enough endurance for mission
Reduce loiter time of orbits
Software will allow you to launch with this error
Check the GcsCommServer shows aircraft is on the network.
Check that aircraft and GCS radio are powered (green IP indicator)
If other operators are in same area, deconﬂict frequencies
Check radio cables and antennas
Reset power on aircraft and restart software
Examine mission, move waypoints further apart
Software will allow you to launch with this error

## Page 12

TROUBLESHOOTING
No Turret Video
Hot Keys (keyboard shortcuts)
Click Open Source     Automatically Detect
Toggle video source from Turret to Oﬀ, wait a second, then select Turret.
Video should show up after ~3-5 seconds
Black Screen in SA Video
Click Open Source     Automatically Detect
Shutdown media client and restart it.
No Picture-In-Picture for SA Video
Ctrl-A - Abort landing
Ctrl-K - Change map contrast
Ctrl-O - Orbit left (orbits look point at current active waypoint MSL altitude) 
Ctrl-W - Toggle coordinate display types
Ctrl-3 - Show 3D display
Up Arrow - Zoom in
Down Arrow - Zoom out
F2 - Toggle video overlay
Full hot key list can be displayed by pressing F1 or by selecting “Hot Keys” in the about menu
Click Open Source     Automatically Detect

## Page 13

Aircraft Departs Programmed Mission
Command “GO TO”
Direct aircraft to a safe known waypoint OR
Command “RTB”
If aircraft doesn’t recover...
Initiate “U-DRIVE”
If aircraft recovers, consider aborting mission
and landing at the earliest opportunity.
If aircraft is not recovered,
see “Loss of Aircraft” checklist.
Aircraft Departs Controlled Flight
Command “LAND IMMEDIATELY”
If vehicle again departs controlled ﬂight again after
aborting the “Land Immediately” command...
Land vehicle and produce after-action.
 If aircraft does not stabilize, see Loss of Vehicle Checklist.
Activate U-Drive to direct aircraft to
a safe landing zone, if possible.
Command “RTB”
Abort Landing
Command “LAND IMMEDIATELY”

## Page 14

Loss of GPS Signal
Attempt to Locate Aircraft
If aircraft is beyond visual line-of-sight, use
onboard cameras, ground references, and
map display to monitor aircraft progress
back to the landing zone.
If autonomous navigation appears deﬁcient,
or to navigate to alternate locaton:
Initiate “U-DRIVE”
Manually steer the aircraft to the best available landing zone
Steer aircraft using forward camera or visually.
Loss of Propulsion
Command “LAND IMMEDIATELY”
Produce After Action Report
INITIATE “U-DRIVE”
Manually steer the aircraft to the 
best available landing zone or;
COMMAND “GO TO”
Direct aircraft to a safe waypoint in 
which or toward which to land.
 “Land Immediately” can be commanded to reduce the 
distance the aircraft will glide before touching down.

## Page 15

Loss of Communications Link
Command “AUTONOMOUS”
Check GCS for Green IP Indicator
Check GCS Antenna
Direct aircraft to a waypoint where
comms is expected to be good.
If in U-drive mode.
Reestablish if required.
Verify proper connection.
Verify patch antenna is pointed toward aircraft.
Verify no blockage of line-of-sight.
Command “RTB”
If aircraft is not recovered...
See “Loss of Aircraft” checklist
Command “GO TO”

## Page 16

Loss of Aircraft
Command “NVG and/ or VISIBLE STROBES ON”
If vehicle has crashed or has not
returned from programmed mission,
if operations allow...
Command “BEEPER ON”
Attempt to Locate Aircraft
Query end of ground track on GCS to get last
known location, altitude, and heading.
If comms link is active:
If comms link has been lost:
Use GCS in mobile conﬁguration to search
for aircraft signal in area of last known
location/estimated aircraft location.
Note vehicle GPS coordinates on GCS.
Produce an After Action Report
Estimate aircraft location.

## Page 17

(no text on this page; probably an image or scan)

## Page 18

(no text on this page; probably an image or scan)
