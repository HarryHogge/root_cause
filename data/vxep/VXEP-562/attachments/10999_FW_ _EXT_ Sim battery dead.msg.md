# FW_ _EXT_ Sim battery dead.msg

Attachment 10999, msg, 312 KB, added 2022-10-03 by Cameron Chapman.

From: Connor Peebles
To: Cameron Chapman
Date: 2022-10-03 14:54:23-04:00
Subject: FW: [EXT] Sim battery dead

Connor Peebles

Electrical Engineer

Edge Autonomy – SLO

From: Kurt Burian 
Sent: Thursday, September 29, 2022 11:49 AM
To: Connor Peebles 
Cc: Justin Neel 
Subject: Fw: [EXT] Sim battery dead

Jonathan from JHU sent us the original configuration file. We modified it with our CG offset and mount position. I can glance through your report on Friday/Monday, but we basically want as much the same as possible and if questionable set toward a small quickly pitching and rolling vehicle. We can also ask LM Matt if he has anyone to reach out to. We never got much guidance other then the config file he attached and being told they do in-flight mag calibration so dont worry about doing it on the ground.

-Kurt 

From: Hijuelos, Jonathan C.
Sent: Monday, May 10, 2021 9:02 PM
To: Kurt Burian; Speulstra, Kenneth R.
Cc: Elias Sullwold
Subject: RE: [EXT] Sim battery dead 

From: Kurt Burian 
Sent: Monday, May 10, 2021 4:08 PM
To: Speulstra, Kenneth R.; Hijuelos, Jonathan C.
Cc: Elias Sullwold
Subject: RE: [EXT] Sim battery dead

Hey Jonathan,

Any chance we can hang onto the payload SIM a bit longer? We are setting up an automated cable test to verify our production cables, but it would be nice to retain the SIM for another week or two until it’s up and running. If its needed elsewhere, complete understand, just thought no harm in asking.

Ken,

I broke another part on the SIM. We had a manufacturing issue that caused a few of the pins in the back shell to short! We found the problem and added some more rigorous validation to our process. However, the volt/current sense function seems to be dead. I was going to order that I thought was the replacement chip, but was unable to source the part in a reasonable amount of time. Sorry!

One last unrelated thing, the AHRS units come from the factory with 1PPS disabled. Any harm in us enabling the 1PPS output(1ms rising I think?) I assume you guys basically wipe the AHRS config and mag-cal, but I wasn’t sure about that particular setting.

Thanks,

Kurt Burian

Engineer 

Jennings Aeronautics

From: Speulstra, Kenneth R. 
Sent: Thursday, April 29, 2021 6:49 AM
To: Kurt Burian; Hijuelos, Jonathan C.
Cc: Elias Sullwold
Subject: Re: [EXT] Sim battery dead

This SIM only detects rising edge.

Ken

From: Kurt Burian
Date: Wednesday, April 28, 2021 at 2:14 PM
To: "Speulstra, Kenneth R.", "Hijuelos, Jonathan C."
Cc: Elias Sullwold, "Arnold, Eric T."
Subject: RE: [EXT] Sim battery dead

Hey Ken,

Quick question for you on the 1PPS signal. What does the sim expect to see, a 1ms pulse, a 10ms pulse, etc. I cant seem to get the 1PPS indicator in the sim GUI to light up and I don’t know if it’s a configuration issue with the AHRS or something else. I have the AHRS set to PPS output with 10000us pulse currently.

Thanks,

Kurt

From: Speulstra, Kenneth R. 
Sent: Friday, April 23, 2021 10:00 AM
To: Kurt Burian; Hijuelos, Jonathan C.
Cc: Elias Sullwold; Arnold, Eric T.
Subject: Re: [EXT] Sim battery dead

Tracking info attached.

Ken

From: Kurt Burian
Date: Thursday, April 22, 2021 at 12:52 PM
To: "Hijuelos, Jonathan C.", "Speulstra, Kenneth R."
Cc: Elias Sullwold, "Arnold, Eric T."
Subject: RE: [EXT] Sim battery dead

That’s great news. Thank you!

-Kurt

From: Hijuelos, Jonathan C. 
Sent: Thursday, April 22, 2021 9:00 AM
To: Kurt Burian; Speulstra, Kenneth R.
Cc: Elias Sullwold; Arnold, Eric T.
Subject: RE: [EXT] Sim battery dead

Kurt 

We can ship out to you tomorrow, so you can have for Monday.  2 weeks should be fine.

J

From: Kurt Burian 
Sent: Thursday, April 22, 2021 12:34 AM
To: Hijuelos, Jonathan C.; Speulstra, Kenneth R.
Cc: Elias Sullwold; Arnold, Eric T.
Subject: RE: [EXT] Sim battery dead

I think the sooner the better at your convenience. We have already done a manual validation of the production hardware and cables as thoroughly as possible, but it would be nice to know everything will work first time with the ‘real’ payload.

Thanks,

Kurt

From: Hijuelos, Jonathan C. 
Sent: Wednesday, April 21, 2021 5:09 PM
To: Kurt Burian; Speulstra, Kenneth R.
Cc: Elias Sullwold; Arnold, Eric T.
Subject: RE: [EXT] Sim battery dead

Kurt

Ken got it back up and working without too much difficulty.  When you thinking for wanting it again?

J

From: Kurt Burian

Date: Wednesday, Apr 21, 2021, 14:02

To: Hijuelos, Jonathan C., Speulstra, Kenneth R.

Cc: Elias Sullwold

Subject: RE: [EXT] Sim battery dead

Hey Jon/Ken,

Hope you two are doing well. Any luck repairing the SIM we broke? We were wondering if it would be possible to get the unit back for a week or two and test out our production cables.

Thanks,

Kurt Burian

Engineer

Jennings Aeronautics

From: Hijuelos, Jonathan C. 
Sent: Wednesday, March 24, 2021 2:02 PM
To: Kurt Burian; Speulstra, Kenneth R.
Cc: Elias Sullwold
Subject: RE: [EXT] Sim battery dead

Please use ken’s name rather than Bryan’s.  Otherwise good

From: Kurt Burian

Date: Wednesday, Mar 24, 2021, 13:49

To: Hijuelos, Jonathan C., Speulstra, Kenneth R.

Cc: Elias Sullwold

Subject: RE: [EXT] Sim battery dead

I’m going to try to get the SIM in the mail today. Is the return address on box the correct place to send the SIM?

Bryan Koch

Applied Physics Laboratory

11100 Johns Hopkins Rd.

Laurel, MD 20723

Thanks,

Kurt

From: Hijuelos, Jonathan C. 
Sent: Tuesday, March 23, 2021 10:35 AM
To: Kurt Burian; Speulstra, Kenneth R.
Cc: Elias Sullwold
Subject: RE: [EXT] Sim battery dead

Thanks for the update, Kurt.  Glad to hear it wasn’t the other around.  We can repair pretty easily.

J

From: Kurt Burian

Date: Tuesday, Mar 23, 2021, 13:26

To: Speulstra, Kenneth R.

Cc: Hijuelos, Jonathan C., Elias Sullwold

Subject: RE: [EXT] Sim battery dead

Hey Ken,

We’re pretty confident the LVDS and US232 transceivers on the SIM have been damaged from a incorrect payload cable. I probed the LVDS and serial lines coming off of the MAIM, the signals are present but the SIM GUI doesn’t show the data. I’m planning on running our remaining boards through the SIM this afternoon and verifying max payload current as well as ethernet connectivity. We are planning on sending the SIM back for repairs once we get that done.

Best Regards,

Kurt

From: Speulstra, Kenneth R. 
Sent: Tuesday, March 23, 2021 5:25 AM
To: Kurt Burian
Cc: Hijuelos, Jonathan C.
Subject: Re: [EXT] Sim battery dead

Kurt,

Have you made any more progress using the SIM?  You had a couple things listed below and wanted to get further feedback.

Ken

From: Kurt Burian
Date: Tuesday, March 16, 2021 at 12:30 AM
To: "Speulstra, Kenneth R.", "Hijuelos, Jonathan C.", Elias Sullwold
Cc: "McAlister, Mac F."
Subject: RE: [EXT] Sim battery dead

Hey Ken,

We fixed our cable issue and had some success with a fresh MAIM. I connected to the sim and have gone through most of the test points. I suspect serial and LVDS damage. Sim shows no SBG Data, 1PPS never blinks, and zeroize never resets low. I’m also getting a voltage alarm under max current and in-rush mode, 26.75V at max current. I checked the voltage at the MAIM connector at it was around 26.9 so it’s not from an unusual cable loss. I’ll poke around a bit more tomorrow to see if I can debug the voltage drop, but I don’t think there’s much we can do about the serial/LVDS. 

Thanks,

Kurt Burian

Engineer

Jennings Aeronautics

From: Kurt Burian 
Sent: Thursday, March 11, 2021 1:19 PM
To: Speulstra, Kenneth R.; Hijuelos, Jonathan C.; Elias Sullwold
Cc: McAlister, Mac F.
Subject: RE: [EXT] Sim battery dead

Hey Ken,

I opened the case up and no glaring problems like smoldering craters on the circuit board. There is a little discoloration on the top of U7, but it could be nothing. I did some probing around the ethernet lines and they are beeping correctly on the transformer pins so I went back over our cable and may have found an issue. I’m having the cable reworked and will get back to you tomorrow afternoon with the results.

Thanks,

Kurt

From: Kurt Burian 
Sent: Thursday, March 11, 2021 9:38 AM
To: Speulstra, Kenneth R.; Hijuelos, Jonathan C.; Elias Sullwold
Cc: McAlister, Mac F.
Subject: RE: [EXT] Sim battery dead

Hey Ken,

My name is Kurt Burian. I’m probably the best person to chat with about what happened. Cell: [phone]. 

Brief summary below:

1.	Plugged SIM into MAIM through payload data/power port. Plugged maintenance cable into MAIM to supply power. Plugged aux payload ethernet from MAIM to laptop.
2.	Turned SIM switch on. Saw green light.
3.	Activated MAIM payload port through GUI.
4.	Attempted to get SIM GUI to recognize SIM. Default IP range of SIM looked like 10.3.*.* address. MAIM IP default range was 192.168.1.*. Played around with this for a bit, give up for the night, packed everything away.
5.	Came in the next day, plugged equipment in as previously. Made sure SIM switch was up. Applied payload power. POP!. Shutdown everything and inspect setup. SIM light wasn’t illuminated with the switch up.
6.	Emailed you guys, asked how to charge a dead SIM. Charged over USB. Checked after a few hours, light was illuminating once again.
7.	Removed burnt LVDS driver, possibly burnt AND chip, and possibly burnt RS232 driver. Board booted fine after doing this. Connected SIM power, but not data. Activating payload power was successful without any further damage. Connected payload data and attempted ethernet connected to SIM. Ethernet port light on MAIM failed to light. Probed SIM ethernet port with continuity tester. Expect transformer connected pairs. One pair beeped short like it should, second pair showed open connection. 
8.	Replaced LVDS driver on MAIM. Connected SIM. Activated payload power. POP!

Thanks,

Kurt

From: Speulstra, Kenneth R. 
Sent: Thursday, March 11, 2021 6:08 AM
To: Hijuelos, Jonathan C.; Elias Sullwold
Cc: Kurt Burian; McAlister, Mac F.
Subject: Re: [EXT] Sim battery dead

Elias,

Can I get a phone number that we can chat a little more about what happened?

Ken

From: "Hijuelos, Jonathan C."
Date: Wednesday, March 10, 2021 at 9:09 PM
To: Elias Sullwold
Cc: "Speulstra, Kenneth R.", Kurt Burian, "McAlister, Mac F."
Subject: RE: [EXT] Sim battery dead

Elias

Clear to crack open the Sim.  We do have a second sim, but I currently have it with me supporting another MP integration (and for what it’s worth, I think I fried mine today, thanks to a bad cable).  So it would be a few days before I could get a spare back out.

Ken, 

Can you please direct Elias / Kurt on where to check once opened?  Please also discuss if there is a quick workaround that makes sense (maybe forego some functionality).

J

From: Elias Sullwold 
Sent: Wednesday, March 10, 2021 5:47 PM
To: Hijuelos, Jonathan C.
Cc: Speulstra, Kenneth R.; Kurt Burian; McAlister, Mac F.
Subject: RE: [EXT] Sim battery dead

Jonathan

It appears we have damaged the MAIM sim. We could use your help deciding on a best course of action. We accept full responsibility for any repair or replacement costs.

Kurt gives a short summary of what happened:

The battery got left on overnight either from me forgetting to switch it off or accidently flipping it while putting it back in the foam case. I didn’t notice the SIM’s power light wasn’t illuminated. As a result, when I activated payload power, I believe we had a latch-up(inadvertent short circuit) through the LVDS driver. The driver chip on the MAIM blew. I repaired the broken MAIM and repeated the test after charging the sim. Exactly the same result so I suspect reciprocal damage was done to the LVDS driver in the SIM. If there is a spare SIM, the best course of action would be to cross-ship a replacement. If not, can we crack the SIM open and attempt a repair?

I apologize to you and the customer for being so careless. I should have double checked the battery state before applying power. If there is documentation handy, I’d be happy to pop open the SIM and see if I can make the necessary repairs. Please let me know how to proceed.

Thank you,

Elias

From: Hijuelos, Jonathan C. 
Sent: Wednesday, March 3, 2021 7:51 PM
To: Elias Sullwold
Cc: Speulstra, Kenneth R.
Subject: RE: [EXT] Sim battery dead

Elias

It should charge off the payload port, but we’ve seen some issues when drained completely.  Let it charge for a while and see if comes back up.

Ken, please chime in as you’re more familiar with this than I.

J

From: Elias Sullwold

Date: Wednesday, Mar 03, 2021, 21:38

To: Hijuelos, Jonathan C.

Subject: [EXT] Sim battery dead

Hi Jonathan,

I am worried we killed the internal battery on the SIM.

Somehow the switch got flipped on for enough time to drain the battery. Will it charge off the payload port or can we swap out a battery?

Sorry and thank you,

Elias

Attached to this email (not converted): image001.jpg, image002.jpg, Ellipse_Settings_ModPayload.bin.REMOVEME, 74AEAA1A76D040F58BDB6C37AF051B2D[194463].png, 70E180BE3C5B45C8A7B8BEECA368ADA6.png
