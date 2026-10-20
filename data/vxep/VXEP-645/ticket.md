# VXEP-645: Mobile GPS MAG Puck no fix

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-09-19
- **Updated:** 2026-03-02
- **Resolved:** 2025-02-03
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Josh Burrell
- **Creator:** Alexander Alan Arnold
- **Labels:** GCS, USASOC, Weekly-incident-tracker
- **Links:** relates to SMUP-53 (New Procedure for support to address: Mobile GPS MAG Puck no fix)
- **Customer:** USASOC
- **Issue Status:** CA appears to address the issue.
- **Root Cause:** Unclear, possibly changing pucks between multiple GCS systems or connecting two pucks to a single system.
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

Operator report  Castillo
I am experiencing and issue with my VXE30 stalker system. We are trying to do mobile GCS ops, the problem we are having is when trying to do the operations we get a warning that pops up and says, “GCS GPS fix lost while mobile GCS active.” We have gone through the trouble shooting steps in the manual. Additionally, we have tested the puck outside of the vehicle stationarily to make sure the armored vehicle was not the problem, and we still don’t have any fixes on the GPS status tab. I reached out to the fielding team, and they mentioned something about the puck needing a software update. We are not sure how to go about those or even how to request the file.

## Corrective Action

https://jenaero.atlassian.net/browse/SMU-136 
New Procedure: 
- Connect GPS Puck
- Open GPSinfo
- Select COM Port: Prolific...
- Baud Rate: 4800
- Start GPS
- If issues, continue
- Stop GPS
- Close GPSinfo
- Open device manager
- Click "View" at the top, then "Show hidden devices"
- Expand "Ports (COM & LPT)"
- If there are any gray Prolific devices, right click them, then click "Uninstall device"
- On the pop up, click "Uninstall"
- DO NOT tick the box that says "Delete the driver software..."
- Right click the remaining Prolific device and select "Properties"
- Click Port Settings at the top of the window
- 4800 Bits per second, 8 Data bits, no Parity
- Click "Advanced..."
- COM Port Nuimber: COM4
- Click OK on the advanced window, then OK on the Prolific Properties window
- Restart the GCS laptop
- Open GPSinfo
- Prolific..., 4800
- If it worked, you should now see blue status on the satellite connections
- Stop GPS and close GPSinfo
- Open VXE SUAV
- Settings > Edit GCS GPS Settings > Mobile Mag Mount GPS
- Settings > GCS GPS Status
- Confirm that Fix = 1. If not, let us know.

## Comments (18)

### Alexander Alan Arnold, 2024-09-19

At the Huntsville site we had a MAG GPS puck plugged into two different GCS laptops one on 6.2.9 and 6.3.4. We were only able to see the GPS Puck on the 6.2.9 Machine. In the VXE GCS software we selected mobile gps config and then opened the GCS GPS Status. We were able to see that it had 8 satellites, grid coordinates updating but a 0 next to fix. 

We asked the SCO team if they could replicate our issues. They were using a 6.3.4 GCS and a MAG GPS Puck and were also getting the 0 fix 

We will upload pictures once we have them. We are coordinating with the SCO team right now.

### David Grosher, 2024-09-19

@Ted Trowbridge @Michael Berger @Jo Brown  Has something changed in the SW or laptop configuration that causes problems with the GPS puck. I know we are using the puck for Molson which is based on v6.3.4, so it seems strange that it would be GCS software related.

### David Grosher, 2024-09-19

@Michael Berger @Jo Brown What data do you need to be pulled from the GCS to help isolate the issue?

### Alexander Alan Arnold, 2024-09-19

update 
We have flight ops personnel down at Ft. Moore using 6.3.4 and they said they were able to get a fix with their MAG Puck

### Cameron Chapman, 2024-09-19

Thanks @Alexander Alan Arnold, does that mean this issue is ok to close? For corrective action, or there procedural, training, or firmware updates recommended?

### Alexander Alan Arnold, 2024-09-19

@Cameron Chapman No I was just providing that it worked on a 6.3.4 system so it may not be 6.3.4 related.

Ruyseer in SCO was unable to get his to work

### Jo Brown, 2024-09-19

@David Grosher Not sure what we would need to pull from the GCS. 
Final assembly hasn’t reported any issues with their GPS configuration steps, even after switching to 6.3.4.

Do we know what kit number for the GCS is? I’m curious when it was configured and sent over to them, if that’s possible to figure out.

I’ve been seeing problems with GPSinfo on my own machine, but those have been specifically with the internal GPS. I’ve never had a problem with any of the GPS pucks that I’ve had access to. I assumed the issues I was seeing were to do with GPSinfo itself and not noteworthy; both GPS receivers had a fix within GCS software when I saw them.

I’ll tag up with Ruysser ASAP about his GCS laptop and try and see if I can spot something. In the meantime, as annoying as it is as advice, I always recommend a restart of the GCS laptop first.

### Jo Brown, 2024-09-20

@David Grosher @Alexander Alan Arnold Here’s what I gave to SLO FLOPS, which worked for their devices. 
Let me know if it does or doesn’t work for any remaining GCS laptops affected. If I need to turn this into a procedure with screenshots, let me know that as well.

- Connect GPS Puck
- Open GPSinfo
- Select COM Port: Prolific...
- Baud Rate: 4800
- Start GPS
- If issues, continue
- Stop GPS
- Close GPSinfo
- Open device manager
- Click "View" at the top, then "Show hidden devices"
- Expand "Ports (COM & LPT)"
- If there are any gray Prolific devices, right click them, then click "Uninstall device"
- On the pop up, click "Uninstall"
- DO NOT tick the box that says "Delete the driver software..."
- Right click the remaining Prolific device and select "Properties"
- Click Port Settings at the top of the window
- 4800 Bits per second, 8 Data bits, no Parity
- Click "Advanced..."
- COM Port Nuimber: COM4
- Click OK on the advanced window, then OK on the Prolific Properties window
- Restart the GCS laptop
- Open GPSinfo
- Prolific..., 4800
- If it worked, you should now see blue status on the satellite connections
- Stop GPS and close GPSinfo
- Open VXE SUAV
- Settings > Edit GCS GPS Settings > Mobile Mag Mount GPS
- Settings > GCS GPS Status
- Confirm that Fix = 1. If not, let us know.

### David Grosher, 2024-09-20

@Jo Brown Thanks! @Alexander Alan Arnold Can you pull together a procedure based on Jo’s comment to provide to any customers? 
@Pat Wells FYSA

### Alexander Alan Arnold, 2024-09-20

@Jo Brown @David Grosher @Pat Wells 
FYSA
I have sent the steps to the customer that was reporting the issue we will see if it resolves his issue 
I do not have the means to test the steps in Huntsville and see if it resolves the issues on our GCS

### Michael Berger, 2024-09-21

@Wesley ReynoldsAm I remembering correctly that you shouldn’t swap pucks between different GCSs? Did we change the puck which is shipped with GCSs in the last year?

### Jo Brown, 2024-09-23

@Michael Berger You can swap pucks between GCSs, so long as you don’t connect 2 at the same time. FLOPS does this somewhat regularly.

If we’d prefer operators to not swap GPS pucks, especially if we determine that this is what caused the issue we’re seeing, there are steps we can and should take to make that more obvious for the operator, such as a label update.

### Pat Wells, 2024-11-07

Customer has deployed with their system.  Will follow up if they reach out again.

### David Grosher, 2024-12-05

@Jo Brown @Alexander Alan Arnold Do we have a published procedure for global support at this point?

### Alexander Alan Arnold, 2024-12-06

@David Grosher We have a draft of one that we made. I am not sure if @Jo Brown has an official document.

### Jo Brown, 2024-12-06

@David Grosher @Alexander Alan Arnold I have not made an official document. Have we seen the issue again, or is making one a priority? I can put together something relatively quickly. 

Wasn’t sure if this was considered completed or not after the customer’s specific issue as resolved.

### Alexander Alan Arnold, 2024-12-10

@Jo Brown Operator has not reached back out with this issue. No other reports of this issue have been received.

### Greg Fryer, 2025-02-03

@Josh Burrell I’m closing this incident, since you’ve moved the long term fix into SMU (linked ticket). We can re-open if it resurects.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| GPS no fix 6.3.4.jpg | image | 214 | 2024-09-19 | listed only |
