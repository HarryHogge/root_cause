# RE Issue with loading DTED in flight .msg

Attachment 16129, msg, 146 KB, added 2023-09-06 by Craig Burton.

From: Sam Miller
To: "[email]"; "[email]"; "Lloyd; Daniel (US)";	"[email]"; Carson Buckley; Artis Bertulis;	Gabriel Staples; Dave Grosher; Craig Burton; "Greg Fryer"
Date: 2023-09-05 14:17:35-04:00
Subject: RE: Issue with loading DTED in flight 

Thanks, Garret!  

For everyone’s SA, the software has always worked this way.  I wouldn’t call this a bug, but rather a loophole exposed last week after ~20 years of operation.  I believe this was due to an uncontrolled GFE laptop that had the GCS software installed by the customer.  All laptops delivered from Edge have a world load of DTED, so the risk to customers is extremely low – probably why we’ve only seen this once.   

I’m sure that we can code around it, but I wouldn’t put this as a high priority.   

Thanks, 

Sam

From: [email] 
Sent: Tuesday, September 5, 2023 11:09 AM
To: [email]; Lloyd, Daniel (US); [email]; Sam Miller; Carson Buckley; Artis Bertulis; Gabriel Staples
Subject: Issue with loading DTED in flight 

Take aways:

1.	If you’re going to add DTED, add it and restart the GCS software before calibrating and launching the plane.
2.	If you do add DTED and restart the GCS software while in flight, disconnecting, closing the GCS software, deleting the DTED, and restarting the software will resolve the issue.  

The story:

The laptop from SGCS1-70 that was used for the Video Based Navigation (VBN) testing at YPG last week did not have DTED loaded for the YPG area.  This was not an issue since we were (for the first 3 flights) operating nearby over flat terrain.  Prior to the 4th launch, however, while at the final Calibration screen in the Launch Wizard, JHU requested that a racetrack be placed at a different location where I was not certain of the terrain elevation.  I copied DTED for the area from my thumb drive onto the GCS laptop and indexed the maps thinking this would get the GCS software to recognized the DTED.  It did not.  The GCS software must be restarted.  I should have cancelled the Launch Wizard, restarted the GCS software, and restarted the Launch Wizard, but in an effort to save time, I elected to do the final Calibration, launch the plane, then restart the software.  

Elevation at YPG is 1300 ft.  The plane was calibrated at 1300 ft MSL and was flying at 500 ft AGL (1800 ft MSL).  Without DTED, the autopilot thought it was calibrated at zero MSL and though it was flying at 500 ft MSL.  After restarting the GCS software the system knew that the terrain elevation was 1300 ft, the altitude indicator showed -800 ft AGL, and the plane climbed 1300 ft to where it thought it was 500 ft AGL, but where it was actually 1800 ft AGL.  Fortunately, this was okay for the test point, but landing was going to be a problem.  The HLB had enough energy to do a vertical landing from 1800 ft, but because it was going to think it was near the ground at 1300 ft, it would slow its rate of descent and run out of HLB well before landing.  I considered changing the minimum waypoint altitude setting in the ini file and turning off all of the auto terrain clearance settings (and the Terrain Dodge gains), and seeing if I could command or U-Drive the plane down to -1500 ft AGL and command Land Immediately.  Thank you to Sam and Artis for recommending I try a more simple solution of simply deleting the DTED and restarting the software.  I was concerned that this might not fix it because deleting DTED off of the computer might not delete the DTED that was uploaded to the autopilot, but it did.  The plane went back to believing Earth was flat and that it was 500 MSL was 500 AGL.  The  plane landed with no issues.

Cheers,

Garret Moose

Stalker sUAS, Lead Instructor

Lockheed Martin Aeronautics Company

[phone]
