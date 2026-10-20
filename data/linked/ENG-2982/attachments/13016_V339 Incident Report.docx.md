# V339 Incident Report.docx

Attachment 13016, docx, 17 KB, added 2023-03-10 by Cameron Chapman.

V339 Incident Report

By Garret Moose

09 March 2023

Helendale Aircraft Facility

V339, HLB 2-1682, Fuel Cell D4500243, Fuel Tank 151, HD45 712

Here is these series event leading up to V339’s crash:

Several flights today with this configuration.

Relaunched without removing aircraft wing or restarting GCS software.

Launched with Manual Nudge Override Buttons.

Landed with Manual Nudge Override Buttons.

Downloaded FDR.

Start Launch Wizard.  Selected Fuel Cell power source (only option).

Waiting for aircraft response Retry 1, 2, 3, 4, 5.  Timed out.

IP GREEN.  Datalink RED.

Confirmed aircraft radio connected in Silvus webpage.

Receiving SA video in Media Client.

AP not talking.

Disconnected and tried to reconnect.  Aircraft #339 is not on the network.

Logged into XComm.

Sensor page showed lots of 0.00 and - - - .

Hardware page, set Web Control: Override ON, AP Power: OFF, AP Power: ON, Web Control: Override OFF.  No affect.

Utilities page, Soft Reset.  No affect.

Disconnected HLB.  No affect.

Disconnected propane manifold until nose cone fan shut off and fuel cell hand were spinning down.

Connected HLB and propane manifold.

Reloaded XComm page and logged in again.

Commanded fuel cell Start in XComm Fuel Cell page.

Connected to aircraft in GCS software.

Launch Wizard and normal launch.

<Test point was to command (glide) Land Immediately while in U-Drive and confirm still had U-Drive control.>

Put aircraft in a ground track at 400 ft AGL down Runway 22.

Activated U-Drive and confirmed left and right turn response.

(Forgot to activate Emergency Glide Landing before next step.)

Commanded Land Immediately, OK.

Aircraft transitioned to VTOL and began a vertical descent.

Activated User Landing Control.

Response to joystick nudge inputs seemed to be Manual Nudge mode, but indicator said Autonomous.

Landed on runway approximately 750 m NE of launch location.

Comms were weak, FDR was downloading slowly, so it was cancelled.

Drove stand to aircraft and placed aircraft on stand.

Ran through Launch Wizard with no issues.

“Aircraft temperature above normal limits” warning 2 or 3 times during launch wizard.

Upon launch, aircraft transitioned immediately and accelerated forward barely off the ground. (We have SA video of the launch.)

Altitude indicated -21000 ft and increasing at what seemed like a normal rate.

Commanded RTB.

Commanded Go to IP4.

Airplane flew the landing pattern but continued to climb to 1000-1200 ft AGL.

After IP5, aircraft transitioned to VTOL and began to descend.

HLB 83%.

Aircraft descended very slowly.

Enabled Land at Emergency LZ.

Commanded Land Immediately.

Popup said something about not enough energy for VTOL landing, executing emergency glide landing, but continued VTOL descent.

HLB <50%.

Tried to increase rate of descent with full deflection Position Nudge.

HLB <30%.

Tried to increase rate of descent with full deflection Manual Nudge.

As aircraft descended below ~300 ft it pitched down, then pulled up repeatedly.

Aircraft weather-vaned into a variable wind from the south and moved forward (south) and was no longer over the runway.

Aircraft turned ~ 90° right.

HLB = 0°

Pitched down, then pulled up (with zero vertical speed) approximately 10 ft off of the ground.

Pitched down and impacted the ground about 80° nose down approximately 114 m south on the PLZ.

Commanded Fuel Cell Stop.

Recovered aircraft.

Removed HLB.  Volts = 15 volts

Connected new HLB.

Repeated attempts to download FDR failed, but downloaded 18 files, 2 MB).

Moved all gear to the building.

Hardwired GCS to the aircraft with center wing attached.  Connected GCS software to aircraft.

Media Client recording.  Command Stop and it Starts again (set to “Always in Flight”).  Seems like the plane thinks it’s flying even after having power cycled multiple times.

Created an AAR in the building.  FDR downloaded with no error (27 files, 7.5 MB).

Red light on center wing does not come on when plane is powered up.
