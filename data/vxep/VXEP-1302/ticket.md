# VXEP-1302: VXE-490 Hard Landing

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2025-06-11
- **Updated:** 2025-09-16
- **Resolved:** 2025-09-16
- **Reporter:** Michael Mohr
- **Assignee:** Josh Burrell
- **Creator:** Michael Mohr
- **Vehicle Tail Number:** 490
- **Plan:** Garmin has requested hardware be returned for further inspection of lens. Awaiting address for shipping.
- **Incident Type:** Squawk
- **Severity:** 1 - Flight Critical

## Description

The aircraft usually pauses at 20 ft and then sets down gently. This time it slowed a bit at around 30 ft and then came down fast to the ground. Slight compression to the landing pad.  The vtol motors are not at their limit. everything seemed fine. No damage. 
ADP-VXE30-0122 - Garmin SN 5HA014288
https://jenaero.sharepoint.com/:f:/s/FlightSafety/EtzgcElfLUtPqQ5hrzJkYd0BK0Zt2I8IaU6HNXOjBtxyAg?e=cqKczL

## Corrective Action

Manual Update to include instructions on which cleaners to not use on LRF lens. Avoid harsh chemicals such as ammonia, aromatic solvents, chlorinated hydrocarbon solvents, oils, esters, ketones and any other chemical solvents. @Josh Burrell @Dana Holley

## Issue Status

Appears to be discrepancy between GPS Alt and LRF. Review of lrfbits shows ‘no good’ & ‘RFMM’ flagged during portion of VTOL landing (0x8042d hex and 042d). May be partially expected for landings, review of other unrelated aircraft flights shows typical bits field is 8043f then 043f < 30ft. 
 Operator reports abnormal lens appearance on LRF (as seen in picture). 
Prior to data analysis operator Removed/Replaced ADP with ADP from separate aircraft (from VXE 808, ADP-VXE30-0557). Awaiting feedback on results from a test flight.

6/25/2025 - smisek- Tested ADP at Final Assembly test point. Testing consists of connecting to their HIL and checking readout from LCD screen for height from desk. Height was +/- ~3inch which was subjectively flagged by tech. When holding ADP at chest level, readouts fluctuated +/-30inch, obviously problematic. 
ADP was subsequently dissembled to inspect lidar/lrf unit. The transmit lens on has obvious defect, similar to crazing in aircraft windows. See plan for next steps regarding this.

## Root Cause

Suspected defect or damage to transmitting lens of Garmin Lidar-Lite v3HP resulting in abnormal height above ground measurements provided to aircraft.

## Comments (34)

### Rodney Linch, 2025-06-25

@Jackson Riley Curvin & @Cody Smisek - ADP is with me.  Let me know if you want me to drop it off to you, Cody.

### Cody Smisek, 2025-06-25

@Drew Hildreth @Pat Wells I’m doing some research on the LRF lens material. This looks very similar to crazing that can be found on acrylic when cleaned with ammonia based cleaners. Not an expert on that, but I think it takes time to occur. I’d recommend communicating with your teams that these type of cleaners should not be used on our system.

### Cody Smisek, 2025-06-25

Also, I’ve returned it to @Rodney Linch who is going to work on getting production to replace the LRF with new and ship back out.

### Drew Hildreth, 2025-06-25

@Cody Smisek Thanks Cody, I will go talk to the team and see what they are doing and then highlight your comments above as a “good to know”

### Pat Wells, 2025-06-25

@Cody Smisek got it. Thanks. Will communicate with the team. 
@William Doupis FYSA

### Cody Smisek, 2025-06-27

Garmin states,
Hello Cody,
  
We appreciate you reaching out to us regarding your LIDAR inquiries.
The lenses are made from a cyclo olefin polymer, a material commonly used for camera lenses and lenses in laser printers.
Cleaning is no different than for other common lenses. If you have eyeglass or camera lens cleaning supplies, those should be fine. Avoid harsh chemicals such as aromatic solvents, chlorinated hydrocarbon solvents, oils, esters, ketones and any other chemical solvents.
The change in color they’ve seen is entirely cosmetic. These parts are specified for their optical properties for infrared light at 904 nm. Any visible variations in color are irrelevant.
Thank you for choosing Garmin,
Leslie
Product Support
Garmin International

### Cody Smisek, 2025-06-30

@Jackson Riley Curvin any additional data available to provide?

### Jackson Riley Curvin, 2025-06-30

@Cody Smisek  I uploaded 3 more AARs from last week let me know if you need any more.

### Cody Smisek, 2025-07-01

also observed on ADP SN 0005 - Garmin SN 5HA000700
ADP SN SAXE-1-0031 - Garmin SN 5HA000681

### David Grosher, 2025-08-15

@Cody Smisek Should the manual be updated to include information on how to clean the lenses? Do we expect to get any other information from Garmin? It sounds like they don’t expect this to have caused the issue, but the response also seems generic and doesn’t address the actual observed artifacts on the lens.

### Cody Smisek, 2025-08-15

@David Grosher I am not expecting any further response from Garmin regarding the root cause. I have sent them the defective units for inspection, that was back in July. We should include in the manual information about what not to use for cleaners around the aircraft, that would be any ammonia based cleaners which are known to cause crazing of acrylic.

### Cody Smisek, 2025-09-02

@Josh Burrell @Pat Wells I’d like to close up this ticket. I’ve recommended corrective actions in the CA section. 
I asked Garmin again for status update over the weekend, they have responded that they will not be providing any additional information.

### Cody Smisek, 2025-09-02

@Greg Fryer @David Grosher See comment below. Do we want to perform any additional investigation / work on this ticket, or is my CA recommendation sufficient based on current knowledge of the issue?

### David Grosher, 2025-09-02

@Cody Smisek It is sufficient. This can progress to implementation of the manual updates and continue through the process.

### Pat Wells, 2025-09-02

Yes I’m good with closing it.  @Josh Burrell  are you tracking the documentation update?

@Michael Mohr FYSA

### Josh Burrell, 2025-09-02

@Cody Smisek do you have a recommended time frame of when the operators should clean the lens? @Drew Cunnien

### Cody Smisek, 2025-09-02

@Josh Burrell No. The CA of this ticket is simply that if the operator chooses to clean it, they should comply with the correct cleaning chemicals. 
The frequency of cleaning or lack thereof was not the failure mechanism.

### Josh Burrell, 2025-09-02

@Cody Smisek Thanks, we’ll see what we can come up with.

### Drew Cunnien, 2025-09-02

@Cody Smisek @Josh Burrell You’re correct, but the question is about how to implement it into the manual. Is there a regular interval of cleaning the lens that is recommended during training? Or is this just whenever cleaning occurs?
There is no mention of cleaning the lens in the manuals that I can find so it’d help if there was a recommended interval so I can determine where to put this CA.

### Cody Smisek, 2025-09-02

@Drew Cunnien 
inspect every flight

### Cody Smisek, 2025-06-30

@Jackson Riley Curvin any additional data available to provide?

### Jackson Riley Curvin, 2025-06-30

@Cody Smisek  I uploaded 3 more AARs from last week let me know if you need any more.

### Cody Smisek, 2025-07-01

also observed on ADP SN 0005 - Garmin SN 5HA000700
ADP SN SAXE-1-0031 - Garmin SN 5HA000681

### David Grosher, 2025-08-15

@Cody Smisek Should the manual be updated to include information on how to clean the lenses? Do we expect to get any other information from Garmin? It sounds like they don’t expect this to have caused the issue, but the response also seems generic and doesn’t address the actual observed artifacts on the lens.

### Cody Smisek, 2025-08-15

@David Grosher I am not expecting any further response from Garmin regarding the root cause. I have sent them the defective units for inspection, that was back in July. We should include in the manual information about what not to use for cleaners around the aircraft, that would be any ammonia based cleaners which are known to cause crazing of acrylic.

### Cody Smisek, 2025-09-02

@Josh Burrell @Pat Wells I’d like to close up this ticket. I’ve recommended corrective actions in the CA section. 
I asked Garmin again for status update over the weekend, they have responded that they will not be providing any additional information.

### Cody Smisek, 2025-09-02

@Greg Fryer @David Grosher See comment below. Do we want to perform any additional investigation / work on this ticket, or is my CA recommendation sufficient based on current knowledge of the issue?

### David Grosher, 2025-09-02

@Cody Smisek It is sufficient. This can progress to implementation of the manual updates and continue through the process.

### Pat Wells, 2025-09-02

Yes I’m good with closing it.  @Josh Burrell  are you tracking the documentation update?

@Michael Mohr FYSA

### Josh Burrell, 2025-09-02

@Cody Smisek do you have a recommended time frame of when the operators should clean the lens? @Drew Cunnien

### Cody Smisek, 2025-09-02

@Josh Burrell No. The CA of this ticket is simply that if the operator chooses to clean it, they should comply with the correct cleaning chemicals. 
The frequency of cleaning or lack thereof was not the failure mechanism.

### Josh Burrell, 2025-09-02

@Cody Smisek Thanks, we’ll see what we can come up with.

### Drew Cunnien, 2025-09-02

@Cody Smisek @Josh Burrell You’re correct, but the question is about how to implement it into the manual. Is there a regular interval of cleaning the lens that is recommended during training? Or is this just whenever cleaning occurs?
There is no mention of cleaning the lens in the manuals that I can find so it’d help if there was a recommended interval so I can determine where to put this CA.

### Cody Smisek, 2025-09-02

@Drew Cunnien 
inspect every flight

## Attachments (14)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 11ft ALT with CW attached.jpg | image | 87 | 2025-06-11 | listed only |
| 14ft ALT with CW tilted.jpg | image | 98 | 2025-06-11 | listed only |
| T95_V490_250611_101739_pack.zip | archive | 2442 | 2025-06-11 | listed only |
| T95_V490_250611_134112_pack.zip | archive | 2014 | 2025-06-11 | listed only |
| 490 ADP Lens.jpg | image | 1301 | 2025-06-12 | listed only |
| image-20250612-233935.png | image | 107 | 2025-06-12 | listed only |
| T95_V490_250616_134342_pack.zip | archive | 1789 | 2025-06-16 | listed only |
| 1000018730.jpg | image | 2391 | 2025-06-25 | listed only |
| IMG_0001.jpg | image | 7169 | 2025-06-25 | listed only |
| IMG_0002.jpg | image | 6040 | 2025-06-25 | listed only |
| IMG_0003.jpg | image | 7309 | 2025-06-25 | listed only |
| T95_V490_250620_133511_pack.zip | archive | 1992 | 2025-06-27 | listed only |
| T95_V490_250620_143907_pack.zip | archive | 2401 | 2025-06-27 | listed only |
| T95_V490_250623_114213_pack.zip | archive | 251 | 2025-06-27 | listed only |
