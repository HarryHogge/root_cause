# ENG-3241: Troubleshoot ADB.

- **Issue type:** Sub-task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-03-13
- **Updated:** 2025-06-09
- **Resolved:** 2025-06-09
- **Reporter:** Cameron Chapman
- **Assignee:** Connor Peebles
- **Creator:** Cameron Chapman
- **Parent:** ENG-2982 VXE 339 Mishap. Abnormal readings, behavior, and slow descent led to HLB empty and crash
- **Links:** relates to ENG-2982 (VXE 339 Mishap. Abnormal readings, behavior, and slow descent led to HLB empty and crash)

## Description

TS order @Connor Peebles 
- Connect to ADB using CW cable. See if issues in parent ticket can be replicated. - Done, replicated when cold
- If replicated, remove ADP. Connect a new one, see if issues go away. - Done, eng. asset ADP did not replicate parrent issue when subjected to same conditions
- Check with FW group to see if any configuration or calibration information can be pulled from the ADB. If not, connect the problematic pod to the ironbird and see if issues can be replicated.

## Comments (28)

### Connor Peebles, 2023-03-13

First thing that I noticed was the IAS of the Air Data Board (on Remote Air page of the VTOL AP webpage) was staying steady around mid 20’s Ft/s. This was an uncovered pitot tube just sitting there. It should normally be around 0-7 Ft/s when uncovered and still. 
[embedded: image-20230313-190125.png]
After covering the pitot and drain tube 2 times to verify IAS would increase normally (which it did) it eventually settled back down into 0-7 Ft/s uncovered as it should.
[embedded: image-20230313-190341.png]
Going to try to replicate parent issue as per 1.

### Connor Peebles, 2023-03-13

Can’t seem to replicate parent issues. Air Data Board is calibrated and configured correctly.
Going to begin cold tests.

### Connor Peebles, 2023-03-13

Putting the entire 339 fuse+CW into a box freezer (-22C/ -7F) for ~8 minutes was able to successfully replicate parent issue. Took it out of the freezer and monitoring as it warms up. Will post videos
339’s ADP functioned normally as it displayed a temp of ~74F

### Connor Peebles, 2023-03-13

@Connor Peebles 
[embedded: IMG_4117.mov]
[embedded: IMG_4116.mov]

### Connor Peebles, 2023-03-13

swapped to engineering asset ADP: AD-10520 w/ FW 2010, 
339 Cold test w/ asset ADP
- starting at 2:56pm & at 76.8F
- passing 10min in freezer, temp is 66.5F. Asset ADP still functioning normally.
- pulled out at 20min in freezer, temp is 55.9F. Asset ADP still function normally, letting it warm up.
- Asset ADP on 339 has gone back up to 76.0F without replicating parent issue, confident problem is in 339’s ADP.

### Cameron Chapman, 2023-03-13

Fridge temp -22C= -7F

### Connor Peebles, 2023-03-13

One thing to note is that the asset ADP, AD-10520, is out of spec according to the Check Out Procedure point #7 of the 1502P01D/C (Air Data Board)
[embedded: image-20230313-222942.png]
[embedded: image-20230313-223033.png]

### Connor Peebles, 2023-03-13

Will now narrow investigation to 339’s ADP and air data board. Will perform in temp chamber in E-shop:
- Wiggle test (on wires)
- Inspect components on air data board
- …maybe internal to processor or other IC on board?

### Connor Peebles, 2023-03-14

[embedded: IMG_4127.jpeg]
Opening up ADP, nothing appears unusual

### Connor Peebles, 2023-03-14

- Wiggle test on wires did not prove fruitful
- Swapping air data boards (ADB) between engr asset ADP still showed the parent issue only appearing on 339’s ADB. Meaning the problem is on the board assembly and not on the Air Data Pod Cable.
- Ready to start inspecting the board @Cameron Chapman

### Cameron Chapman, 2023-03-14

Thanks Connor. I think we should check with the fw team and maybe research the source of the temperature measurement before excavating the potting compound on the board.

### Connor Peebles, 2023-03-15

Thanks @Ryan Ferguson for some more testing ideas
- Swinging (quick punching motions and circular motions) both 339’s ADP and the asset ADP showed functional accelerometers and did not replicate the parent issue. 339’s air data board SN is AD-10707.

[embedded: proFCS AP Tail# 339 - Work - Microsoft​ Edge 2023-03-15 11-33-53.mp4]
[embedded: proFCS AP Tail# 339 - Work - Microsoft​ Edge 2023-03-15 11-36-57.mp4]
- Air speed and altimeter changes are normal as well

### Connor Peebles, 2023-03-15

Have not extracted the board from the potting material yet, but looking into the ICs on the board I believe BOM Item U5 is the source of the temperature measurement (https://www.digikey.com/en/products/detail/te-connectivity-measurement-specialties/MS561101BA03-50/5277445)
It could be as simple as some toughseal got in/on the sensor holes during assembly. 
Considering that the parent issue happens during a decrease in temperature, it is likely that it is a solder joint or internal IC problem because contraction is the trigger and not expansion.

### Cameron Chapman, 2023-03-16

[embedded: image-20230316-200713.png]
[embedded: image-20230316-200722.png]
U5 reference pictures top left of board

### Cameron Chapman, 2023-03-16

Proposed test: (edited 3.3V is not available to measure on connector)
Please pause for review and note any anomalies if encountered.  
- Test on a spare dead board removing potting compound or U5 housing without risk to damage components.
- Firmware questions
- Confirm with firmware team that U5 is the source of the temperature measurement and could cause these issues.
- Can any more firmware configuration, status, or other data can be pulled from the ADB that has not already been pulled. @Kurt Burian , are you available to help answer these when you return 3/17?
- Can the processor report the 3.3V voltage, or easier to remove potting and measure it?
- See if you can safely measure 3.3V without disturbing components (ex: remove potting from J2 connector)
- Once FW questions are resolved, remove U5 grown housing. Attempt not to disturb any components. If tough seal cannot be easily removed, consider cutting housing open to inspect.
- Attempt to replicate issue by cooling. If still present, proceed
- Inspect U5 and surrounding components for any solder, blocked holes, or other manufacturing issues.
- If none found, reflow U5 solder joints.
- Attempt to replicate issue by cooling. If still present, proceed.
- Replace U5. Attempt to replicate issue by cooling.

Adding  @Dustin Gamble @matthew.curran

### Connor Peebles, 2023-03-16

Removed potting compound on a scrap board relatively easily. Could still power it and read off it.  
[embedded: IMG_4131.jpeg]

### Connor Peebles, 2023-03-17

Thanks to Kurt for looking at it with me. 
We noticed that the accelerometer is pulling 8 g’s after sitting for a while, other asset ADP’s accelerometers more accurately report standing still. 

[embedded: image-20230317-213923.png]

So whatever is happening is passively affecting the accelerometer U9 (MPU-9250 TDK InvenSense | Sensors, Transducers | DigiKey) and only actively affecting U5 when subjected to dramatic temperature decreases

### Connor Peebles, 2023-03-17

[embedded: image-20230317-221813.png]
When triggering the parent issue with cold temps, the accelerometer reverts back to reasonable values.

### Connor Peebles, 2023-03-17

@Cameron Chapman I think we are good to go with the test plan your last comment had, adding we can look at the serial bus through testpoint of J5 and we should also inspect the accelerometer U9

### Kurt Burian, 2023-03-17

@Connor Peebles is doing a great job debugging. Seemed like a SPI bus issue, probably a bad chip pulling CS down when it shouldn't or maybe a iffy solder joint. Ideas going forward:
- Watch the accelerometer values over a length of time during checkout. They drifted to crazy values over a minute, but looked normal on power up.
- Add test points and firmware that exercises the SPI with expected request response values. We can monitor with a A/D and likely detect something like a CS line hanging.
- Add code to throw a error of the air data accelerometer values are wierd during launch wizard cal. I don't know if it reported -8g's during launch wizard but we sure saw it on the bench.
- We see this on the VTOL AP. We might have the same issues on two boards accelerometers due to manufacturing or a bad part or both(more Conner testing to determine this)

### Connor Peebles, 2023-03-21

Carefully pulling off the bottom potting material of the suspect ADB, C23 pulled off really easily with the potting. 
[embedded: IMG_0074.jpg]
[embedded: IMG_0075.jpg]
This might be our suspect solder joint because looking at the schematic C23 is filtering for AVSS. It may have been retained with the potting and cold temperature contraction caused the cold solder to separate, causing parent issue. 
[embedded: image-20230321-200946.png]

I will solder C23 or equivalent back onto suspect board and attempt to replicate parent issue. 
May also pull C23 off a scrap board and see if I can replicate parent issue.

### Cameron Chapman, 2023-03-21

Good findings and test ideas @Connor Peebles. I think we should start with this order, 
- pull C23 off a functional scrap board and see if I can replicate parent issue (ideally at ambient, but test cold if not).
- I will solder C23 or equivalent back onto suspect board and attempt to replicate parent issue.
- Then Kurt’s other recommendations if nothing found in 1-2.  Thanks Kurt for your help.

### Connor Peebles, 2023-03-21

Ah sorry @Cameron Chapman I already did 1. & 2. today. Could only still replicate parent issue on 339’s ADB with or without C23. It is just a noise filtering capacitor. @Maxime Jeanneau And I found what might be something wrong with the 3.3V Rail coming from the processor though.

### Cameron Chapman, 2023-03-22

No worries. 3.3V issues could definitely create issues. I’ll stay tuned. Good work.

### Connor Peebles, 2023-03-22

3.3V is functioning normally on 339’s ADB afterall. Before we move onto excavating the rest (top/barometer side) of the board we will see what we can glean from troubleshooting the bottom/processor side.

### Connor Peebles, 2023-03-27

Next steps taken were to isolate the accelerometer first and then the barometer to see if disabling one or the other fixed the issue the other was seeing.
Starting with disabling the accelerometer’s ability to talk by desoldering R37 & R36.
[embedded: image-20230327-225607.png]
Attempts to replicate parent issue by applying cold temperatures failed. Either the accelerometer is bad, perhaps a solder joint is bad, or somehow the accelerometer and barometer started talking over each other on the SPI bus.
[embedded: image-20230327-225815.png]
To continue investigating the accelerometer I will;
- Resolder R37 & R36, test for parent issue
- Reflow all solder joints for the accelerometer, test for parent issue
- Replace accelerometer, test for parent issue

### Connor Peebles, 2023-03-28

- Resoldering R36 & R37 allowed the accelerometer to talk again, after which there was no more erroneous accelerometer data. It no longer drifted to +8 g’s X and +6 g’s Y, in fact the readings looked ideal and matched board movement.
Attempts to replicate parent issue by exposing the board to several cycles of cold temperatures were not successful. The issue has become not reproducible.

My immediate theory is that there was a cold solder joint that was reflowed/redone when replacing R36 & R37. I used a reflow station and I believe 1 or 2 pins on U9 may have been reflowed when working on R36/37. I am going to spend some time looking through the flight data to see if all affected sensors match, perhaps try to replicate parent issue on another board.

[embedded: IMG_0076.jpg]
Another theory is that the accelerometer and barometer were talking over each other, giving the erroneous data. Given that the issue could only be triggered by exposing to cold temps I’d wager it on a cold solder joint contracting which then gave an intermittent connection on the SPI bus which enabled this talking-over-each-other on the SPI bus.

### Cameron Chapman, 2023-03-28

It seems like you have pretty good evidence that the issue was caused by a bad solder joint (because it caused by cooling and was fixed by reflowing the joints). Great work! As discussed, unable to see the bad solder joint under normal and close inspections. The best way to catch issues like this would likely be pre-flight checks, anomalous value flags, etc, so the corrective actions should target those. Ok to close this subtask and update issue root cause.

## Attachments (21)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| IMG_4116.mov | video | 32699 | 2023-03-13 | listed only |
| IMG_4117.mov | video | 37093 | 2023-03-13 | listed only |
| image-20230313-190125.png | image | 63 | 2023-03-13 | listed only |
| image-20230313-190341.png | image | 47 | 2023-03-13 | listed only |
| image-20230313-222942.png | image | 123 | 2023-03-13 | listed only |
| image-20230313-223033.png | image | 12 | 2023-03-13 | listed only |
| IMG_4127.jpeg | image | 3130 | 2023-03-14 | listed only |
| proFCS AP Tail# 339 - Work - Microsoft​ Edge 2023-03-15 11-33-53.mp4 | video | 35769 | 2023-03-15 | listed only |
| proFCS AP Tail# 339 - Work - Microsoft​ Edge 2023-03-15 11-36-57.mp4 | video | 20769 | 2023-03-15 | listed only |
| [1502S01C AIRDATA POD Schematic.pdf](attachments/13129_1502S01C%20AIRDATA%20POD%20Schematic.pdf.md) | pdf | 537 | 2023-03-16 | converted |
| IMG_4131.jpeg | image | 1838 | 2023-03-16 | listed only |
| image-20230316-200713.png | image | 747 | 2023-03-16 | listed only |
| image-20230316-200722.png | image | 1041 | 2023-03-16 | listed only |
| image-20230317-213923.png | image | 59 | 2023-03-17 | listed only |
| image-20230317-221813.png | image | 91 | 2023-03-17 | listed only |
| IMG_0074.jpg | image | 6546 | 2023-03-21 | listed only |
| IMG_0075.jpg | image | 6619 | 2023-03-21 | listed only |
| image-20230321-200946.png | image | 30 | 2023-03-21 | listed only |
| image-20230327-225607.png | image | 56 | 2023-03-27 | listed only |
| image-20230327-225815.png | image | 22 | 2023-03-27 | listed only |
| IMG_0076.jpg | image | 3889 | 2023-03-28 | listed only |
