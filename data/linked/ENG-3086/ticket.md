# ENG-3086: Nose fan failing to shut off

- **Issue type:** Problem
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2024-08-23
- **Updated:** 2025-06-02
- **Resolved:** 2025-03-20
- **Reporter:** Garret Moose
- **Assignee:** Pat Wells
- **Creator:** Garret Moose
- **Links:** relates to VXEP-597 (VXE 600 Nose cone fan failing to shut off after fuel cell cool down)

## Description

The nose fan on V530 and V600 failed to shut off once the fuel cell is cooled down.  GCS had already been packed up, so don’t have the actual temperature on V530, but V600’s fan was still running while temp was <100°C.  In both cases, battery power was disconnected while the fan was still running.
See photo of temperature reading attached.
AAR for V600 is attached for configuration.  Fuel cell might have cooled below 150°C before the FDR was successfully downloaded.

## Comments (8)

### Pat Wells, 2024-10-14

@Garret Moose   Investigation complete. 
Final report attached.

### Pat Wells, 2024-11-20

@Garret Moose do you have any additional logs from this event?  The AAR you provided was captured before the system reached the temp threshold to shut the fan off. 
Also was this aircraft glide landed during the flight covered by the AAR you provided?

### Garret Moose, 2024-11-20

I added the only two other AARs I have from the event.  I’m not certain if they were produced after the fuel temperature was below 150°C or not.  Yes, all landings were glide landings.

### Pat Wells, 2024-11-21

@Garret Moose recieved. 
Thank you

### Pat Wells, 2024-12-06

@Garret Moose We do not think we can debug this without more data. We specifically would want an AAR log set that includes the time when the temperature has reduced but the fuel cell fan is still on.
The logsets we have, the XComm and fuel cell logs cut off when the reactor temp is still high. If the flight logs have not been cleared it’s possible they are still on the aircraft. The last xcomm log on the 133603 log set is ‘T95_V530_240822_133603_xcl00118.csv'. If there is an xcl00119.csv/xcl00120.csv it’s possible these might contain the data we’re looking for. If these logs do not exist, it may indicate the avionics were powered down before the incident,

### Garret Moose, 2024-12-06

The aircraft are in the UK and have almost certainly flown since August.  I don’t know if those logs persist after resetting the autopilot in the Launch Wizard.  This might now be a mute point, as I don’t recall the fan staying on after the fuel cell cooled down after multiple flights 3 weeks ago using AP FW 6.05p .

### Pat Wells, 2024-12-06

@Garret Moose I concur. What’s needed on your side to close this out with the customer?

### Pat Wells, 2024-12-10

Aircraft being returned to SLO for updates. 
Will evaluate upon return.

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| IMG_1595.jpeg | image | 1189 | 2024-08-23 | listed only |
| T95_V600_240823_101808_01_pack.zip | archive | 8167 | 2024-08-23 | listed only |
| [Investigation Report VXE-530&600_9OCT2024.pdf](attachments/23933_Investigation%20Report%20VXE-530&600_9OCT2024.pdf.md) | pdf | 685 | 2024-10-14 | converted |
| T95_V530_240822_133603_pack.zip | archive | 2259 | 2024-11-20 | listed only |
| T95_V530_240822_151625_pack.zip | archive | 1849 | 2024-11-20 | listed only |
