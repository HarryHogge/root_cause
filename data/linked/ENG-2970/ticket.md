# ENG-2970: VXE466 Course Deviation and Crash

- **Issue type:** Problem
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2023-03-08
- **Updated:** 2025-06-02
- **Resolved:** 2025-04-22
- **Reporter:** Former user
- **Assignee:** Cameron Chapman
- **Creator:** Former user
- **Labels:** Crash
- **Links:** relates to RMA-120 (VXE-466 RMA 230510 LM); relates to FS2-522 (VIT2-227 ); relates to ENG-3184 (Review flight logs to explain delayed handoff and update report.)

## Description

After 1 hr flight, vehicle hand off was done for recovery. After hand off, vehicle departed mission with motor off. It flew level with power off until it impacted terrain.
It had started snowing during the flight which lead them to start a landing.

From Gordon
“The XC00037 file shows that something happened around UTC 182300.
The roll, pitch and power trims are mostly constant leading up to the “event.”  Then the trims take off and full power (over about 1 – 2 minutes) is required to maintain altitude.  Then we hit the ground.
The “event” is probably a mechanical shift of some sort, like a wing tip that rotates.”

## Comments (33)

### Dustin Gamble, 2023-03-09

Towards end of the flight there is a big altitude dip, 400 ff to 250 ft then it comes back to 350ft. It has trouble holding that altitude and adds more and more power. As it does the GPS ground speed starts going up. Airspeed is around 53 ft/s but GPS ground speed of both fixed wing and VTOL report increasing with each orbit. Power is getting higher and it at full power towards the end. At the the end the GPS ground speed is 117 ft/s while the airspeed is still reporting ~52 ft/s. 
Airspeed doesn’t match GPS speed. 
Chris reported that it has started snowing so they were bringing it in to land. Maybe airspeed had snow inside of it.
Chris did say they have flown XE25 in the snow. 
XE25 and VXE30 has the same pitot tube system, however the pitot tube is in a different location in the pod. XE25 pitot is next to the SA camera. On VXE30 it is further away. I wonder if there was some SA pitot drain pocket heating happening on XE25
[embedded: image-20230309-161035.png]

[embedded: image-20230309-161045.png]

### John Clark, 2023-03-10

Added a bit more data from my investigation. Possible weather related failure.

### Former user, 2023-03-10

Thanks @John Clark I think you mislabeled your report with tail #339 vs 466. the report is the right one, just has the incorrect tail #

### John Clark, 2023-03-17

•After 1 hr flight, vehicle hand off was done for recovery. After hand off, vehicle departed mission with motor off. It flew level with power off until it impacted terrain.
•It had started snowing during the flight which led them to start a landing.
•Slide 3 in the attached Incident Report shows divergence in IAS (indicated airspeed) from the pitot static system and airspeed as measured by the GPS. The data indicates the operation of the pitot static system degrades over time.
•Without a functional pitot static system the aircraft cannot maintain safe flight.
•Slides 5, 6, and 7 in the attached Incident Report indicate a sudden loss of altitude followed by a recovery then crash
•Probable causes of pitot static systems can be weather related when snow or freezing rain blocks the pitot tube. This causes airspeed to decay and prevents safe flight.

### matthew.curran, 2023-04-05

Has anyone looked at the hardware or inspected the airdata system?  We used to see similar failure modes when the tubing in the airdata developed kinks.

### matthew.curran, 2023-05-01

Please look at items in RED in the 466 deck.  If you can help, let us know.  Customer would like feed back on the Hardware aspects next week. (did we look into the probe for blockage? can we tell them what is salvagable?)  They would like a copy of the 466 deck.  Notify when it its ready to give them.

### John Clark, 2023-05-01

@matthew.curran wilco.

### Sean Odell, 2023-05-10

@John Clark The vehicle is having initial evaluation by myself and Chris Jones. Does your team need to do any evaluation on this aircraft based on the type of failure listed in this ticket?
FYI @Cameron Chapman

### John Clark, 2023-06-30

Incident Report report rewritten 6/30/2023

### John Clark, 2023-07-10

@Michael Berger I need your help to address the missed hand off.

### matthew.curran, 2023-07-18

the data points to the airdata system not working.  we assumed this to be a result of snow.  did anyone ever test the airdata unit to make sure it generates the correct values at flight airspeed?  If it does, then the crash was caused by snow.  customer is asking

### Michael Berger, 2023-07-18

@matthew.curran reviewing logs regarding handoff problems, it appears that the new GCS was not able to connect to the vehicle because the old GCS was still connected to the vehicle. The vehicle is refusing the new connection because it still has an existing connection.

### matthew.curran, 2023-07-24

Re typing my question from April “Has anyone looked at the hardware or inspected the airdata system?”  I need to know if that airdata is working properly.  If not please surrender the hardware so LM can send it out for testing.

### John Clark, 2023-07-25

@Cameron Chapman  can you answer @matthew.curran  on the airdata pod, please?

### Cameron Chapman, 2023-07-25

I will have someone try to locate and test it asap. 
Adding @Pat Wells for tracking.

### Connor Peebles, 2023-07-26

@Madeleine Masiello @Carson Buckley Can we get eyes on the traveler for the Air Data Pod for VXE 466? We are trying to actually find it and we suspect it is being used as an asset (hopefully not in the air). So if we can get the SN for the POD and the Air Data Board inside if it, that would be helpful. Maddie might come by later to ask about this when you’re ready Carson.

### Carson Buckley, 2023-07-26

@Connor Peebles @Madeleine Masiello VXE 466, ADP-VXE30-0071, ADB AD-1-0500, DoM 2022-01-30

### matthew.curran, 2023-08-03

The ADP was with airframe 466, was it found and tested?

### Connor Peebles, 2023-08-07

It is not with the airframe in the RMA area

### Mark Squillante, 2023-08-16

Setting status to Waiting until we find ADP

### Cameron Chapman, 2023-08-22

@Marc Richardson do you want to link this to your Corrective Action?

### Cameron Chapman, 2023-08-22

Assigning to @Pat Wells to determine process improvements to prevent hardware from going missing between RMA, engineering, and production.

### Cameron Chapman, 2023-08-22

Thanks @Pat Wells are you able to list a Jira link or document number here to track those process updates?
We still need to determine a plan to complete search and a plan of what to do if not found.

### Cameron Chapman, 2023-08-24

Linking subtasks to parent.

### matthew.curran, 2023-08-29

Can we have the traveler for the airframe pulled to get the ADP Serial number?  This will make it easier to find.
This has been escalated with our customer. Please find and test the ADP.

### Carson Buckley, 2023-08-29

@matthew.curran ADP-VXE30-0071

### Pat Wells, 2023-09-11

@matthew.curran  ADP was located today and will be tested ASAP

### Pat Wells, 2023-09-22

@matthew.curran Updated incident report attached, includes ADP test report / data.  The ADP is functioning properly.

### Pat Wells, 2023-10-19

@matthew.curran have you received disposition from the customer on this ACFT?  Repair quote was provided back in May 20203.
@Sean Odell

### matthew.curran, 2023-10-19

Not yet.  I informed the customer that this was not a warranty replacement.  
Is that repair quote you sent us something we can actually get on order, or will Edge not accept it from LM.  I just don’t want to waste everyone’s time trying to fund a repair/replace if Edge is not going to take the repair PO from LM.

### Sean Odell, 2023-10-19

@matthew.curran We are accepting funded repair orders for support. Please keep @Pat Wells and myself in communication so we can keep things going smoothly during this repair. Thank you for your assistance as well Matt.

### Pat Wells, 2023-11-15

@matthew.curran any feedback from the customer on moving forward with this repair?

@Sean Odell

### Pat Wells, 2023-12-07

@matthew.curran 
Do we have any decision from the customer on this repair?  Or should we return it as BER?
@Sean Odell

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AC466 Mishap.zip.allow | other | 15126 | 2023-03-08 | listed only |
| image-20230309-161035.png | image | 112 | 2023-03-09 | listed only |
| image-20230309-161045.png | image | 90 | 2023-03-09 | listed only |
| Weather Data 3_8_2023.xls | other | 252 | 2023-03-10 | listed only |
| [Vehicle 466 incident report .pdf](attachments/16491_Vehicle%20466%20incident%20report%20.pdf.md) | pdf | 1113 | 2023-09-22 | converted |
