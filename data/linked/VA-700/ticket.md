# VA-700: VXEP-149   VXE 398 Connector Hot and Burnt - Investigate C/CA

- **Issue type:** Task
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** High
- **Created:** 2023-10-18
- **Updated:** 2025-06-02
- **Resolved:** 2025-06-02
- **Reporter:** Cameron Chapman
- **Assignee:** Connor Peebles
- **Creator:** Cameron Chapman
- **Links:** relates to VXEP-149 (VXE 398 Connector Hot and O-rings burnt); relates to VA-939 (VXE 398 Connector Hot and O-rings burnt); is a child of VA-939 (VXE 398 Connector Hot and O-rings burnt)

## Description

Plan:
- Attempt to identify anomaly in customer supplied logs

## Sprint

VXE-1 Electrical-8, VXE-2 Everything Else 2024-03, VXE-1 Electrical 10/29, VXE Product Dev & Sup 2024-07, VXE Product Dev & Sup 2024-05, VXE-1 Electrical-7, VXE Prod Dev & Sup 2024-08

## Comments (19)

### Connor Peebles, 2023-10-27

Perform resistance measurement from the tip of the AS150 anti-spark contact to the base. Report findings.
 9.8 tip to base positive pin (this seems high??)  it was 5.7 on the other birds
- Repeated measurement, 21.1 Ohms Anti-spark tip-to-base.


Measure resistance between positive (from the base of the terminal) and negative terminals.
3.5 base to base negative-pos , 0.9 inside negative to base of positive
- Repeated measurement, 1.0 MOhm which drops and rises because of capacitance in the fuselage

### Connor Peebles, 2023-10-27

Very different measurements on the system, plus I powered it up and connected to it just fine, no overheating on the power cable

### Connor Peebles, 2023-10-27

From main battery connector to nose connector:
+: 0.2 Ohms, -: 0.2 Ohms
No signs of hot-swapping/ arcing on nose power harness
[embedded: IMG_E6721.JPG]
[embedded: IMG_E6719.JPG]

### Connor Peebles, 2023-10-27

The Main Batt AS150 Anti-spark silicon ring does indeed look melted and it is hard to tell because of the angle, but it looks like the solder reflowed on the anti-spark as well. This would make sense as (per Laszlo) it takes about 400degreeF to melt the silicone ring
[embedded: IMG_0556.jpg]
[embedded: IMG_0557.jpg]
Capacitance reading of the nose and also from the main batt harness shows ~37uF. Other noses in the lab show normally ~32uF capacitance of the nose.
Resistance of the nose shows ~1.48 KOhms, other noses in lab show normally exactly 1.5 KOhms

### Connor Peebles, 2023-10-30

The high resistance of the anti-spark pin and the hot wire suggests a power surge of some sort. Since I cannot recreate this power surge, whatever caused it seems to have cleared itself. That could point to signs of a bridge short or possibly a mosfet blowing in the FWD ESC. The logs provided in the parent ticket do not show any large power surges.
@Cameron Chapman I’d like to open up the FWD ESC and perhaps the Avionics Box afterwards.

### Cameron Chapman, 2023-10-30

@Connor Peebles approved to open both boxes. Thanks for the detailed findings. Please tag any parts removed from the aircraft with this incident and aircraft number. We should inspect and measure the fwd CSB for damage  as well.

### Connor Peebles, 2023-10-31

looking at xcomm logs (28-44, 46, 48, 49, 50, 51, 52, 53, 54, 55, 56) still don’t show any major power surges

### Connor Peebles, 2023-11-01

There are no signs of damage in the FWD ESC. I do not think it is worth it at this time to pull the board out of the enclosure (to see the bottom side). 
[embedded: IMG_E6792.JPG]

### Connor Peebles, 2023-11-01

no damage to the CW pins

### Connor Peebles, 2023-11-01

Damage found to one of the power pins of the Fuselage Payload Harness on the upper payload hood. This could be the path of the power surge. Damage is reminiscent of arcing or overheating.
[embedded: IMG_0559-edited.jpg]

### Connor Peebles, 2023-11-01

Most of the logs have something plugged into 12Vaux with a pretty continuous 1.5A pull with peaks in the log showing almost 3A but could be higher peaks, just without the resolution to see it. Still, I am doubtful that this kind of power pull would heat up the main battery connector much.
[embedded: image-20231101-180825.png]

### Connor Peebles, 2023-11-01

Avionics Box does not show any signs of damage, although there was a loose screw (see below) which was detached from Avionics Enclosure XCOMM Mount Post (965-1-01-3108).
[embedded: IMG_6794.JPG]
[embedded: IMG_E6795.JPG]

and another screw was still holding the board was threaded in at a slight angle and tightened
[embedded: IMG_0560.jpg]

### Connor Peebles, 2023-11-01

If SW cannot find an anomaly in the logs;
- I would recommend replacing aft portion of the Fuselage Power Harness [(107-102189-1) or the whole 107-102189 FWD and AFT, whichever is easier for Production]. 
- give the removed portion to ENGR for further testing, especially for testing the anti-spark AS150.
- Recommend re-assembling and re-testing the avionics box through the check-out procedure and then doing the same for the whole VXE398, which is done in the RMA process I believe.
- Recommend re-testing of the FWD ESC
- and FWD Motor

I am recommending production do the re-testing because it will have to be done anyway for the RMA process, and since there are no signs of faultiness it seems unnecessary to do it twice.

### Cameron Chapman, 2023-11-02

@Connor Peebles can you please start and investigation ppt and save a link to it and the files in the desc?

### Connor Peebles, 2023-11-03

Looking more into the fuselage payload harness, it looks like there is No Connection (NC) from the PRIM_PWR_IN to the MOD J1 (from nose to Mod payload hood). It could be a manufacturing defect or perhaps the heat that was felt at the battery harness melted the PWR_IN wires on the Payload Harness or at the nose. Connection is there, looking more into it
Pinout from nose to AUX P2 (branch cable connection) is correct.
All of the Fuselage Payload Harness checked out on the harness tester: 
[embedded: MicrosoftTeams-image (2).png]

### Connor Peebles, 2023-11-13

wiggle testing harnesses while powered did not show any anomalies

### Connor Peebles, 2023-11-15

looking through all the logs that were pulled (found in Flight Safety - LOGS - All Documents (sharepoint.com)) it seems that they did send the wrong logs with the VIT2 ticket based on the described time ranges, but also that there are still no power surges or current spikes (apIbatt) on any of the logs. The most that can be found are continuous 3A draws for a couple of hours on end.
Still not enough to cause the melting of the ring on the anti-spark AS150, without some other un-accounted for factor. 
The running theory is that the resistor inside the anti-spark pin failed which will cause higher than normal contact resistance where such loads applied might be able to heat the connector up as described. Thermal calculations derived from power dissipation are extremely complicated and would take quite a bit of modeling to do right.
The plan to finish this up is to measure the contact resistance of the anti-spark AS150 and then attempt a 3A pull for such a while to replicate the heat build up.

### Connor Peebles, 2023-11-15

Measuring the contact resistance of the AS150 anti-spark contact came up with a value of 488uOhms. This is about twice as high as the acceptable field test value of the AS150 contacts.
(AS150 testing reference here: 107-102264 - Dual Current Sense Harness - Contact Impedance Test Report - P5.docx)

### Connor Peebles, 2023-11-21

Removed aft portion of the Fuselage Power Harness (107-102189-1) for further diagnosis. The rest of the parts can go back into RMA.

## Attachments (11)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| IMG_0556.jpg | image | 4050 | 2023-10-30 | listed only |
| IMG_0557.jpg | image | 4476 | 2023-10-30 | listed only |
| IMG_E6719.JPG | image | 3308 | 2023-10-30 | listed only |
| IMG_E6721.JPG | image | 1921 | 2023-10-30 | listed only |
| IMG_0559-edited.jpg | image | 2866 | 2023-11-01 | listed only |
| IMG_0560.jpg | image | 6864 | 2023-11-01 | listed only |
| IMG_6794.JPG | image | 2620 | 2023-11-01 | listed only |
| IMG_E6792.JPG | image | 2420 | 2023-11-01 | listed only |
| IMG_E6795.JPG | image | 2357 | 2023-11-01 | listed only |
| image-20231101-180825.png | image | 18 | 2023-11-01 | listed only |
| MicrosoftTeams-image (2).png | image | 137 | 2023-11-03 | listed only |
