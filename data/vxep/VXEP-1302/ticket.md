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

### Cody Smisek, 2025-06-12

@Michael Mohr we see messages regarding user commanded pauses during landing. Can you confirm that this was the case? Also, other details would be appreciated. Such as purpose of flight, aircraft configuration, environmental conditions, geographic location.
Can you confirm the GCS SN that was in use? Which version of xbox controller?

### Michael Mohr, 2025-06-12

@Cody Smisek There were two flights yesterday with two AARs loaded above. The flights were a part of the Border Patrol training currently going on. The two pictures of the GCS above indicate the crew moving the center wing from flat to angled to show the bad indicated altitude. The second flight was a test, by the Edge operators, to try and replicate the first issue where the aircraft slowed down at 30ft then continued it decent without the pause at 20 ft. The Operator (Edge) expected the anomaly and paused several times during final 20ft to ease the A/V to touchdown. We troubleshoot it down to the ADP (pictured above). We swapped ADPs today with another A/V and expect to fly tomorrow to test. Ground test looks good and is reflecting the expected zero altitude.

### Cody Smisek, 2025-06-12

Working with Eric B to understand discrepancy between gps alt and LRF and why LRF status appears good even though aircraft didn’t arrest descent rate
[embedded: image-20250612-233935.png]

### Cody Smisek, 2025-06-13

@Michael Mohr @Drew Hildreth 
the lrfbits data seems to agree with the decision to swap out the ADPs. The bit fields for ‘nogood’ and ‘RFMM’ are flagged. Not entirely sure how that works out for what the VTOL AP starts using, but I’m assuming it’s not giving much credit to the LRF anymore at that point.

### Drew Hildreth, 2025-06-13

@Cody Smisek Thank you for looking into this so quickly and getting back to us. We truly appreciate it. I hate that something is broken but pleased to know that Mike and the FLOPS Team were on the same sheet with what was potentially causing the issue. 

We will continue to provide data when FLOPS gets a chance to fly. Weather here today is not favorable for flying.

### Drew Hildreth, 2025-06-13

@Cody Smisek SGCS SN: SGCSS1-JA11
Controller: RAZER WOLVERINE V2 SN: PM2041C07400323
Please let me know if you need anything else from me.

### Cody Smisek, 2025-06-13

@Drew Hildreth Can we get SN from suspected defect ADP and replacement/test ADP

### Drew Hildreth, 2025-06-13

@Cody Smisek Suspected Defective ADP. SN: ADP-VXE30-0122
Replaced with VXE-808 ADP. SN: ADP-VXE30-0557

### Drew Hildreth, 2025-06-16

@Cody Smisek FLOPS conducted ground checks and test flew VXE-490 today. No issues to report. Jackson will upload the AAR shortly for reference.
Additionally. Mike Mohr is bringing the suspected broken ADP to SLO with him today.

### Jackson Riley Curvin, 2025-06-16

@Cody Smisek  AAR uploaded from todays flight.

### Cody Smisek, 2025-06-20

@Jackson Riley Curvin any data available from yesterday?

### Jackson Riley Curvin, 2025-06-20

@Cody Smisek unable to fly yesterday due to weather and the team did not get back before I had to leave so I'll get it from them Monday morning.

### Cody Smisek, 2025-06-25

@Jackson Riley Curvin any updates? additionally, where did the ADP end up?

### Jackson Riley Curvin, 2025-06-25

@Cody Smisek I'm still waiting on the team to send me AARs but they haven't had any issues flying it this week @Michael Mohr  took the ADP with him to SLO last week not sure what he did with it. @Rodney Linch do you know what happened to it?

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
