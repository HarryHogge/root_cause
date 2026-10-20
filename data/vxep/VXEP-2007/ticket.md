# VXEP-2007: VXE 978 lost link after struggling to maintain altitude and crashed

- **Issue type:** Incident (8D)
- **Status:** D2 - Gathering Information
- **Priority:** Highest
- **Created:** 2026-09-24
- **Updated:** 2026-10-19
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Matthew Aguirre
- **Creator:** Alexander Alan Arnold
- **Links:** relates to RMA-1112 (VXE-978 RMA 260928-1); relates to RMA-1113 (EPS6508 RMA 260928-2)
- **Customer:** USAACE
- **Vehicle Tail Number:** VXE 978
- **Vehicle Configuration:** VXE 30 ADV NAV,battery,e140g2,Vidar payload
- **Incident Type:** Aircraft Loss
- **Severity:** 1 - Flight Critical
- **Executive Summary:** Gathering data and aircraft for investigation

## Description

o issues throughout assembly, and preflight. Caution populated after approx. 1.2 hours of flight “Aircraft
cannot maintain commanded altitude” at 1100 feet AGL at the time (Approx 11:05 Local). The instructor (SSG
Xiong) re-commanded aircraft climb to mission altitude 1200 Feet AGL (11:10 Local) to ensure aircraft is
maintaining altitude. Aircraft climbed up to 1200 Feet AGL according to the “Altitude” GUI on OGCS and
looked at “Main battery” display GUI which read “37%”. Before Instructor (SSG Xiong) commanded aircraft to
“Land PLZ”, the SGCS-1 lost all connectivity with the aircraft during flight (11:15 Local). The instructor went to
Silvus radio page to ensure that the aircraft was still on the Mesh network at that point the aircraft was not
populating within the “Network Topology” menu within the Silvus radio GUI. The instructor had ground crew
that maintained eyes on aircraft as it descended from altitude during lost link procedure.

## Plan

- Evaluate the crashed hardware for any damage that does not appear crash‑related, including thermal signs or other irregularities.
- Inspect AS150 connectors for thermal damage and verify antispark resistor values.
- Verify that the avionics box is safe to apply power (check for shorts or other risks).
- If feasible, perform an in‑fuselage power‑on of the avionics box; monitor current draw and output voltages for irregularities.
- If an in‑fuselage power‑on is not possible, move the avionics box to a bench setup for isolated power‑on testing.
- If the avionics box powers on normally with no irregularities observed, proceed with reintegration of the box onto the iron bird.

## Issue Status

(10/15) No root cause determined yet. Was able to power on Fuselage and Nose with no hiccups, lower current draw was reported by the vehicle on VXE978 vs B30 Adv Nav IB w/ CW disconnected. Will continue investigating tomorrow.  - Matt A.
(10/16) Wasn’t able to determine any root cause with an in-fuselage power-on of the avionics box. Moved the avionics box to the IB and posted results below. So far everything seems to be functioning normally but will continue testing functionality. Expecting to be able to inspect the battery used in-flight during crash Tuesday (10/20) for signs of power failure. - Matt A.

## Comments (16)

### Alexander Alan Arnold, 2026-09-28

@David Grosher @Eric Brewer Data is uploaded in the one drive zip file. There is also data labeled for 885, not sure why they sent that, but the tail is 978. We are working to get it sent back as well.

### Eric Brewer, 2026-09-28

@Alexander Alan Arnold @David Grosher as far as I can tell it’s a complete avionics power failure.  Xcomm/vtol/fdr cut all around the same time. I did see that there was some altitude tracking issue but I’m not sure it was indicative of a real problem vs. just altitude tracking issues that happen sometimes.

Here’s a summary from the logs:
xcomm log XCL00329.csv, event log 260925.txt
xcomm event log cuts off at [18:13:41.584 6629.584]
next startup indicates 'power reset'
vtol log VTL00270.csv stops mid flight, seems like around same time as xcomm
VTEV log cuts at [07:26:21.029 1175.029]
Lining up time using attitude data, appears vtol/xcomm logs cut within ~2s of one another (well within range of potential buffer differences, i.e. total power loss seems plausible).
FDRRECOV.csv cut around the same time.
FW attitude diverged from vtol/novatel right at the end of the log. (fw thought pitch down and low roll), though low update rate of logs makes it hard to know if that's real or not.

### Alexander Alan Arnold, 2026-09-28

@Ted Trowbridge Since this was an FTP it did not recover the OGCS logs.Is there anything specific you want pulled from the aircraft? I can have them power on the fuse and log into OGCS sometime today.

### Ted Trowbridge, 2026-09-28

@Alexander Alan Arnold grabbing everything on the MCM from /mnt/edge/vsm/logs and /mnt/edge/cucs/logs would help – we could see if the MCM also lost power.

### David Grosher, 2026-09-28

@Jeremy Kostel FYSA, see below.

### Jeremy Kostel, 2026-09-29

@Samuel Lopez This is the one I mentioned yesterday. Taking a quick look, no obvious battery troubles. Both MB and HLB are at an acceptable voltage and everything appears to be pulling current appropriately. See Plan section for some suggested steps. Also adding in a folder with only the flight logs Eric pointed out below[embedded: V978.zip] 
[embedded: image-20260929-141448.png]

### Jackson Riley Curvin, 2026-10-12

@Samuel Lopez  Has anyone had a chance to look at the aircraft?

### Zachary Mann, 2026-10-12

@Jeremy Kostel 978 is in SLO on the engineering table, do we have any further information on the status of it? Thank you.

### Jeremy Kostel, 2026-10-12

@Jackson Riley Curvin @Zachary Mann wasn’t aware hardware had come in yet. We’ll take a look this week

### Zachary Mann, 2026-10-12

@Jeremy Kostel Awesome sauce, thank you.

### Jeremy Kostel, 2026-10-12

taking another look at this one, still dont see anything obvious. Voltages remain healthy, FWD motor seems to be responding fine to commands. Then everything stops logging at the same time. That mixed with the lost comms makes it look like a MB internal or connection problem. Need to troubleshoot the hardware
[embedded: image-20261012-180227.png]

### Jeremy Kostel, 2026-10-12

@Matthew Aguirre heres the one I mentioned earlier that ill have you take a look at this week.
First step as a quick intake, we’ll want to power on as much of the plane as possible in the state it came in at. I haven’t had eyes on the vehicle yet - so not sure how much is possible.
If you deem it unsafe to power on in any current state, take good pictures and remove AV box, Silvus, VTOL Stack, and ADP. Test all of their functionality and power on an isolated bench first - then ok to move to iron bird. 
Find me with questions

### Jeremy Kostel, 2026-10-12

@Jeremy Kostel also ok to wait a day until after you’ve gone through investigation training tomorrow afternoon

### Matthew Aguirre, 2026-10-13

@Jeremy Kostel read my mind, thank you boss!

### Matthew Aguirre, 2026-10-15

- Inspected AS150 connection to battery, no thermal damage seen, however, did notice some sort of grease inside of the negative terminal of the connector (picture included). Not too familiar with installation process so not totally sure if it’s just some sort of anti-corrosion grease. Will need to verify with someone more familiar with operating handbook.
- Verified AS150 anti-spark resistor, ohmmeter measured around 6.2 ohms.

[embedded: AS150 Negative Term Grease (englarged).jpg]
- Inspected harnesses and wiring in the fuselage and nose. Only major damage (wiring-wise) noticed was small nicks in the insulation to the power lines connected to xt30 connector (pictures included) branching off the fuse power harness (107-102189). After inspecting nicks on the aforementioned wires w/ a magnifying glass, it was determined the damage was contained only to the insulation and no bare wire strands were damaged. Kapton tape was added to the nicks to prevent shorting and continue with powering on fuselage and nose with benchtop power supply. Hard to say at this time if this damage was due to the crash or was caused by excessive vibration during flight. Will keep this in mind while further investigating.

[embedded: Fuse Power Harness Nicks.jpg]
- After powering only the CW and nose (with overcurrent protection), the current draw was noted to be around 0.7 A after about 3 minutes of waiting for steady-state. For comparison on the B30 Adv Nav Iron Bird (w/ CW connection disconnected), the current draw was noted to be around 1.1 A after the same amount of wait time. This difference in current draw was initially hypothesized to be due to a broken link to the silvus enclosure, as disconnecting the silvus on the B30 IB (w/ CW connection disconnected) yielded a current draw of around 0.8 A. However, this was deemed not to be the case as I was able to connect to the Silvus webpage on VXE978 when powered on. 
[embedded: VXE978 Fuse and Nose Steady State Measurements.png]
[embedded: B30 Adv Nav IB Fuse and Nose Steady State Measurements.png]
[embedded: B30 Adv Nav IB Fuse and Nose (no Silvus) Steady State Measurements.png]

### Matthew Aguirre, 2026-10-19

2026-10-16
- Removed avionics box from 978 and installed into B30 Iron Bird for sensor/performance comparison.
- Main differences noticed were values not being reported from ADP, UTC not iterating, and slight discrepancies in i12aux and iret readings (most likely nothing major, but will continue investigating)
- Reached out to possibly inspect B30 batteries used during flight that resulted in crash. Expecting the materials to arrive Tuesday 2026-10-20and will perform inspection for any signs of power failure.

[embedded: 978 Avionics Box on B30 IB Sensor Page.png]
[embedded: B30 Adv Nav IB Sensor Page with CW Connection.png]

## Attachments (12)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| VXE30 sn 978.zip | archive | 14718 | 2026-09-24 | listed only |
| OneDrive_2026-09-25.zip | archive | 552313 | 2026-09-28 | listed only |
| V978.zip | archive | 1290 | 2026-09-29 | listed only |
| image-20260929-141448.png | image | 212 | 2026-09-29 | listed only |
| image-20261012-180227.png | image | 342 | 2026-10-12 | listed only |
| AS150 Negative Term Grease (englarged).jpg | image | 1714 | 2026-10-15 | listed only |
| B30 Adv Nav IB Fuse and Nose (no Silvus) Steady State Measurements.png | image | 114 | 2026-10-15 | listed only |
| B30 Adv Nav IB Fuse and Nose Steady State Measurements.png | image | 108 | 2026-10-15 | listed only |
| Fuse Power Harness Nicks.jpg | image | 3064 | 2026-10-15 | listed only |
| VXE978 Fuse and Nose Steady State Measurements.png | image | 116 | 2026-10-15 | listed only |
| 978 Avionics Box on B30 IB Sensor Page.png | image | 92 | 2026-10-19 | listed only |
| B30 Adv Nav IB Sensor Page with CW Connection.png | image | 100 | 2026-10-19 | listed only |
