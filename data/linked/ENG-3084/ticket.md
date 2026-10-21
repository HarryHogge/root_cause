# ENG-3084: VXE 401 Failed VTOL Landing from 10ft (Crash)

- **Issue type:** Problem
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-04-20
- **Updated:** 2025-06-02
- **Resolved:** 2025-05-05
- **Reporter:** Cody Smisek
- **Assignee:** Laszlo Juhasz
- **Creator:** Cody Smisek
- **Links:** is blocked by ENG-3075 (V401: Vehicle reached IP4 and Commanded Emergency Glide Landing while at 75% for Hybrid Lift Battery); is blocked by ENG-3066 (V401: Vehicle ascended to 1500ft during orbit when orbit was set to 1200ft.); relates to RMA-116 (VXE-401 230424); relates to VA-93 (Record typical, max, and max tested lift current and voltage profiles. Save test data to confluence. Establish and implement limits and abort if exceeding.); relates to ENG-3061 (VXE 454 Center Wing Power Connector solder melted); relates to ENG-3160 (Determine overcurrent abort limit, then implement auto-abort when present. Update manuals accordingly. ); is caused by ENG-2250 (Try to ensure customers don't operate outside of published limits. Develop method to track when customers are given approval to operate outside of published limits. ); relates to ENG-3177 (Review other system logs for any other abnormal conditions); relates to ENG-3175 (Inspect System to determine possible causes); relates to ENG-3176 (Coordinate Return of Damaged Equipment)

## Description

Investigation Files: https://jenaero.sharepoint.com/:f:/r/sites/EngineeringTeam/Shared%20Documents/Investigations/VIT2-248%20VXE%20401%20Failed%20VTOL%20Landing%20from%2010ft%20(Crash)?csf=1&web=1&e=v8nGCS 

From: Chris Joyce <chris@trinitybend.com>
Sent: Wednesday, April 19, 2023 4:33:11 PM
To: Kevin Sivertson - Bend <ksivertson@edgeautonomy.io>; Charles McElroy <charles@trinitybend.com>; Sam Miller <smiller@edgeautonomy.io>
Cc: Matthew L. Balderree <matthew.balderree@inl.gov>; Michael W. Shurtliff <michael.shurtliff@inl.gov>
Subject: RE: FDR 50.8 lb 4/19
 
Kevin,
 
This FDR is from the crash we just had. The aircraft was landing nothing abnormal. About ten feet off the ground it abruptly rolled and slammed into the ground. We don’t have video of the landing… Seemed as if half or maybe all the vtol motors stopped. VTOL battery was at 60 % when checked power on the ground.
 
Winds were 10 g15 . This FDR is priority to look at compared to the two previous flights.
 ---------------------------------------------------------

## Comments (31)

### John Clark, 2023-04-21

Attached Summary Report and linked to 283

### Sean Odell, 2023-05-02

@Cody Smisek The Aircraft has gone through intake and brought over to Engineering to start evaluation.

### Cody Smisek, 2023-05-02

@Cameron Chapman do you have insight on who will inspect?

### Cameron Chapman, 2023-05-03

@Laszlo Juhasz , can you please inspect this aircraft. “•The VTOL Lift System appears to have suffered rapid loss of Voltage approximately 10’ above final level.” I think start by looking into all VTOL power connectors. Please discuss findings and plan before proceeding with any testing that modifies aircraft parts. (ok to open ESC cases if needed).

### Cameron Chapman, 2023-05-03

@Cody Smisek , you finally motivated me to document our investigation process. More. Please see here. https://jenaero.atlassian.net/wiki/spaces/EF/pages/23363854/VIT2+Project-Incident+Troubleshooting+and+Resolution+Tracking.

### Laszlo Juhasz, 2023-05-05

The VXE401 Aircraft was inspected by measuring the continuity of the power supply wiring to all four lift motors. There were no anomality. The ESC’s/motors were also tested for measurable back EMF generated DC by spinning the blades by hand and all four produced equal amount DC across the Positive and Return terminals at the power connectors. The Autopilot chamber was opened, and all PCBs were inspected for possible damages. One of the vibration damping weight was broken off from the PCB assembly. (That might be from the impact of the crash). A more in-depth ESC investigation/test will be conducted in the next couple of days.
[embedded: IMG_20230505_142217562-20230505-212218.jpg]
[embedded: IMG_20230505_134338720-20230505-204339.jpg]
[embedded: IMG_20230505_140801516-20230505-210804.jpg]

### Cody Smisek, 2023-05-08

@Laszlo Juhasz Can the ESCs cause complete loss of voltage for the entire lift system? The data suggest that voltage was lost for the entire lift system (not sure where that voltage input is measured from).

### Laszlo Juhasz, 2023-05-08

@Cody Smisek Good question. One of the reasons such event can occur when the connection breaks. The other one is when the uCU in the ESC locks-up and keeps the driver Mos-Fets in conducting for a longer period of time, basically DC biasing the motor and that can draw enormous amounts of current during that time. That will not necessarily cause catastrophic failure in the system, but it can cause significant voltage sag. It would be great to know if the loss of the Voltage was caused by excessive current. So far there is no indication of discoloration or other sign of such event. I might need to open the ESCs to see if that was the case.

### Cody Smisek, 2023-05-08

@Laszlo Juhasz Thanks for the explanation. I went back to the data and captured the current. Not sure how much current counts as excessive so you’ll have to interpret the results (doesn’t look excessive). First set of plots from the incident flight
[embedded: image-20230508-191815.png]
[embedded: image-20230508-193046.png]

Second set of plots from an arbitrarily selected flight on different system (VXE398). Not sure the reason between incident flight having lower current than below. Possibly weight configuration?   
[embedded: image-20230508-192037.png]

### Laszlo Juhasz, 2023-05-08

Awesome data. Thanks Cody. My question then is: -Do we have the battery in our hands what was installed during this recording of incident?

### Cody Smisek, 2023-05-08

Not at this time. I’ll see what I can do about that but given it was in a fall from 10ft, it may not be safe to ship. 
This event was observed on the flight prior (not resulting in a crash) with a completely different battery.

### Laszlo Juhasz, 2023-05-08

Unfortunately, that is a problem not able to inspect the battery. From the attached charts I can see a bit longer lasting pick current (over 5kW of total power) for the failed vehicle. Could you please explain the x axis scaling. Is that the sample count and/or some time base?  If you happen to have a higher resolution data for that duration, that would be great to see then.
[embedded: Ipeak_Compared.jpg]

### Cody Smisek, 2023-05-08

That’s a complicated answer. It was just quick plotting, so samples but I believe our data rate changes during certain times (like takeoff / landing). Regardless, replotting based off time in seconds. 
[embedded: image-20230508-222848.png]
[embedded: image-20230508-223324.png]
[embedded: image-20230508-223530.png]
[embedded: image-20230508-223635.png]

### Laszlo Juhasz, 2023-05-08

That is actually great data. Thank you Cody for the effort.

### Cameron Chapman, 2023-05-08

Thanks both of you for the investigation work. Some recommendations. 
- Since the voltage and current are sensed in the CSB in the CW, a voltage drop like that without a corresponding current increase indicates a battery or connection issue in the CSB, battery, or between them
- Even if the battery cannot be shipped, we should mark it as related to this investigation and perform some cell voltage measurements with the battery checker if possible.
- You should plot things with CPU time or a similar one on the x axis, that will make sure the spacing is correct.
- I recommend saving plots/excel sheets in a shared location, like here https://jenaero.sharepoint.com/:f:/r/sites/EngineeringTeam/Shared%20Documents/Electrical/Investigations?csf=1&web=1&e=UJseP7
- Have you tried the https://jenaero.atlassian.net/wiki/spaces/EF/pages/18579459/Automated+Flight+Data+Processing

Checkout this page https://jenaero.atlassian.net/wiki/spaces/EF/pages/13467649/Flight+Data+Review

### Cody Smisek, 2023-05-08

Based on a response from the customer today, they already returned the HLB back into service (I was previously under the impression it was not being used). And based on the fact this issue occured on two separate flights with two separate batteries, it seems reasonable to rule out the HLB. However, if we need to ask the customer to return or stop using the HLB for further inspection we'll likely need an immediate HLB to provide as replacement. @Sean Odell any idea on inventory availability of HLB? @Cameron Chapman do you have additional suggested checks? I will ask that they use the voltage checker but based on their “return to service reply” I would believe that cell voltage was and is still normal.
The most recent set of plots utilized time in seconds which is what the CPU column provides and is denoted in the x axis label. 
I will start saving data in the additional suggested location.
I will give the automated process a try. FYI, if the process uses similar methods of denoting events like takeoffs and landings like LMs version, certain events will prevent plotting appropriately. In which case its back to basics.

### Cody Smisek, 2023-05-09

@Laszlo Juhasz 
Plot from the previous flight before landing. Possibly intermittent connection? There are 2x Vbatt columns in the VTOL data, I think the cleaner one is just filtered and it goes to GCS to provide operator with status. 
Are we inducing any shaking during checks? What happens when we provide HLB voltage? 
[embedded: image-20230509-171322.png]

### Cameron Chapman, 2023-05-09

Laszlo reports the CW power connector smells burnt. If that is the case, then I would start the inspection there. Remove braid behind the connector and inspect for signs of reflowing or mfg variations. 
Also, the original VXE was designed and tested using a max takeoff current of 140A. The max CSB test ever was 200A. If we are routinely meeting or exceeding 200A, that seems like a major issue that requires some requalification and testing. 
Opening up a subtask for that. 
[embedded: VTOL2-CURRENT RATINGS-share.xlsx][embedded: CSB-and-contacts-tests.xlsx]

### Laszlo Juhasz, 2023-05-11

[embedded: IMG_20230511_095240155.jpg]
The burnt smell caused by the inrush limiting resistor. Most likely at excessive current that resistor heats up and that leads to the solder melting in the connector as well. Further testing is planned to quantify the current and heat dissipation relation in the power connector.

### Cody Smisek, 2023-05-11

@Laszlo Juhasz without destructive methods, is there any way to inspect these connectors?

### Laszlo Juhasz, 2023-05-11

Yes, indeed the result is very obvious. This attached picture was taken without the “vandalism” from the 454 bird.
As far as seeing any sign of damage prior to the “final” episode, I’m not sure of it. 
It’s definitely worth to try screening them after each flight. 
[embedded: IMG_20230511_113736988.jpg]

### Sean Odell, 2023-05-19

@Laszlo Juhasz Any updates on this aircraft? The customer is pinging me and would like to understand what the next step is for this AC. Thank you for your hard work by the way!

### Laszlo Juhasz, 2023-05-19

@Sean Odell Good Morning Sean, I’m in the process of quantify the lift battery connection margins under excessive current conditions (=>200A) as we can see from the chart provided by Cody. I’m just about to run that test today and will report back soon. As far as the status of that vehicle is concerned, there is no obvious signs of failure of the ESCs and motors but that needs to be tested deeper to validate. The Autopilot compartment was opened and investigated for possible damages. One of the vibrations dumping weight broke off most likely from the impact of the crash. Again, the melting solder in the connector is definitely an indication or the result of flying the plane under excessive stress what could cause such temperature rise.
More data is on the way.

### Cameron Chapman, 2023-05-22

@Sean Odell added these to the fields above. Cody has also had some communication with the customer (attached). Lift system current was over 200A. Much higher than what the aircraft was designed for (~150A). This indicates they were likely flying overweight. Need to record by how much.
Record weight customer was flying in status.
https://jenaero.atlassian.net/browse/ENG-1695

### Cody Smisek, 2023-05-22

I have added the weight they stated they were flying at. 50.6lb

### Laszlo Juhasz, 2023-05-22

@Cody Smisek @Sean Odell @Cameron Chapman @Mark Squillante 
I’ve done the high current evaluation for the lift battery connection. Attached, is the log of a side-by-side comparison of the 150A vs 200A heat rising measured at the connector pins and the wire itself. The wire runs hotter than the connectors and the second most heated is the positive connection pin. 
The graph clearly shows that the temperature rises up significantly faster to the point when the wire temperature hits the melting point of the solder (~280F°).
[embedded: Thermal Data_5_22_23_Cmpl (db428499-3ed6-4007-bc21-e7f035bbd371).jpg]

### Cody Smisek, 2023-05-23

@Laszlo Juhaszany idea on the factors that would get us to melting temp in ~20-30 seconds instead of 70 seconds?

### Laszlo Juhasz, 2023-05-23

Good morning Cody. Yes, the most significant factor is the single strand 8AWG wire heats up faster than the dual 10AWG return wires. That is what heats up the connecting pins faster as well.

### Cameron Chapman, 2023-08-21

Nina “we are building the center wing, tail boom, and fuse from scratch FYI final assembly is almost done”
Boom harness and ESCs should also be closely evaluated and considered for reuse or rebuild.

### Laszlo Juhasz, 2023-08-24

@Cameron Chapman @Sean Odell As of yesterday, all four lift motors and ESCs were tested for functionality and were removed from the booms. These motors and ESCs were not showing any sign of wear or tear from overheating. All four ESCs were working as they meant to be without any anomality. I’m recommending to saving them for NOT production use or strictly testing.

### Cameron Chapman, 2023-08-24

Linking subtasks to parent.

## Attachments (38)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 20230419_171231.jpg | image | 4015 | 2023-04-20 | listed only |
| 20230419_171235.jpg | image | 4676 | 2023-04-20 | listed only |
| 20230419_171237.jpg | image | 5150 | 2023-04-20 | listed only |
| 20230419_171248.jpg | image | 4443 | 2023-04-20 | listed only |
| 20230419_171253.jpg | image | 4608 | 2023-04-20 | listed only |
| 20230419_171303.jpg | image | 3869 | 2023-04-20 | listed only |
| 20230419_171310.jpg | image | 3691 | 2023-04-20 | listed only |
| 20230419_171313.jpg | image | 2477 | 2023-04-20 | listed only |
| 20230419_171353.jpg | image | 916 | 2023-04-20 | listed only |
| 20230419_171408.jpg | image | 3430 | 2023-04-20 | listed only |
| 20230419_172115.jpg | image | 943 | 2023-04-20 | listed only |
| 20230419_172434.jpg | image | 1889 | 2023-04-20 | listed only |
| MicrosoftTeams-image.png | image | 91 | 2023-04-20 | listed only |
| T95_V401_230419_134913_pack.zip | archive | 2453 | 2023-04-20 | listed only |
| [Vehicle 401 incident report.pptx](attachments/14131_Vehicle%20401%20incident%20report.pptx.md) | pptx | 6823 | 2023-04-21 | converted |
| [VXE401 Intake Written Form.pdf](attachments/14328_VXE401%20Intake%20Written%20Form.pdf.md) | pdf | 3108 | 2023-05-02 | converted |
| VXE401 Intake.zip | archive | 141612 | 2023-05-02 | listed only |
| IMG_20230505_134338720-20230505-204339.jpg | image | 3173 | 2023-05-05 | listed only |
| IMG_20230505_140801516-20230505-210804.jpg | image | 2677 | 2023-05-05 | listed only |
| IMG_20230505_142217562-20230505-212218.jpg | image | 3097 | 2023-05-05 | listed only |
| Ipeak_Compared.jpg | image | 157 | 2023-05-08 | listed only |
| image-20230508-191815.png | image | 57 | 2023-05-08 | listed only |
| image-20230508-192037.png | image | 53 | 2023-05-08 | listed only |
| image-20230508-193046.png | image | 38 | 2023-05-08 | listed only |
| image-20230508-222848.png | image | 65 | 2023-05-08 | listed only |
| image-20230508-223324.png | image | 83 | 2023-05-08 | listed only |
| image-20230508-223530.png | image | 95 | 2023-05-08 | listed only |
| image-20230508-223635.png | image | 63 | 2023-05-08 | listed only |
| [CSB-and-contacts-tests.xlsx](attachments/14407_CSB-and-contacts-tests.xlsx.md) | xlsx | 14397 | 2023-05-09 | converted |
| [VTOL2-CURRENT RATINGS-share.xlsx](attachments/14408_VTOL2-CURRENT%20RATINGS-share.xlsx.md) | xlsx | 20009 | 2023-05-09 | converted |
| image-20230509-171322.png | image | 61 | 2023-05-09 | listed only |
| 20230421_143039.jpg | image | 1457 | 2023-05-10 | listed only |
| IMG_20230511_095240155.jpg | image | 2319 | 2023-05-11 | listed only |
| IMG_20230511_113736988.jpg | image | 2547 | 2023-05-11 | listed only |
| 401_230419_134913-50lb-Takeoff.png | image | 45 | 2023-05-17 | listed only |
| 401_230419_134913-50lb-landingCrash.png | image | 57 | 2023-05-17 | listed only |
| [RE_ VXE401 Update.msg](attachments/14827_RE_%20VXE401%20Update.msg.md) | msg | 93 | 2023-05-22 | converted |
| Thermal Data_5_22_23_Cmpl (db428499-3ed6-4007-bc21-e7f035bbd371).jpg | image | 757 | 2023-05-22 | listed only |
