# Wing Vibration Report.docx

Attachment 16137, docx, 1190 KB, added 2023-09-06 by Jack Waeschle.

Wing Oscillation Report

VXE30

Author: Jack Waeschle

Status: Draft

Issue: 1.0

Issue Date: 5 September 2023

Issue Records

| Issue | Issue Date | Status | Pages Affected | Comments/Notes |
| 1.0 | 9/5/2023 | Draft | All |  |
|  |  |  |  |  |
|  |  |  |  |  |

## Summary

This document attempts to capture all testing and analysis related to wing oscillations observed during hover on various VXE-30 aircraft. The majority of this testing was conducted in the Spring of 2023. Some analysis and further investigations were left incomplete as this became a lower priority issue.

## Previous Incidents

This investigation was originally opened after two new engineering assets, vehicle 490 and 491 exhibited an uncharacteristic amount of oscillation/vibration of their wings after pausing on descent. This phenomenon has been observed with multiple vehicles to varying levels of severity. See table 1 below for details.

| Vehicle Tail Number | Oscillation Amplitude | Notes |
| 406 | - | 1-2 mph wind, 4/6/2023 |
| 414 | Small | With center wing from 306 |
| 481 | - | Straight into wind, present on one of three flights |
| 490 | Medium | Engineering asset |
| 491 | Large | Engineering asset, very prone to oscillate |
| 507 | Medium |  |

Table 1. Summary of oscillation prone vehicles. Note this table is representative of multiple engineers’ experiences and reports both from San Luis Obispo and Bend.

## Test Overview

Multiple test efforts were conducted related to this issue. These were tracked on Jira ticket VIT2-225 and the following is mostly a recycling of the information documented there. Additionally, footage of this oscillation phenomenon can be found on the Jira ticket linked above.

## Root Cause Investigation

In an effort to pinpoint the component(s) or firmware causing oscillation issues, the following test plan was created by Enoch Nicholson, Will Harris and Jack Waeschle.

All flights required a 5-10 mph wind. Planes would take off in a 90-degree orientation relative to the wind, and abort between 25- and 50-feet elevation before the aircraft could weathervane into the wind, and then hover/pause during descent to observe oscillation characteristics. During pause, a high-rate capture from the VTOL “flight” web page was attained for later use.

The following table and figure summarize the test plan.

| Test | Fuselage | CW | Lift booms | Joiners | Wing tips | FW AP Firmware | XCOMM Firmware | VTOL Firmware |
| 1 | 491 | 491 | 491 | 491 | 491 | 6.05m | 4.67 | 1.52 |
| 2 | 490 | 490 | 490 | 490 | 490 | 6.05m | 4.67 | 1.52 |
| 3 | 491 | 491 | 491 | 491 | 491 | 6.05m | 4.67 | 1.44 |
| 4 | 490 | 490 | 490 | 490 | 490 | 6.05m | 4.67 | 1.44 |
| 5 | 491 | 300 | 300 | 300 | 300 | 6.05m | 4.67 | 1.52 |
| 6 | 491 | 300 | 300 | 491 | 491 | 6.05m | 4.67 | 1.52 |
| 7 | 491 | 300 | 491 | 491 | 491 | 6.05m | 4.67 | 1.52 |
| 8 | 491 | 300 | 491 | 300 | 300 | 6.05m | 4.67 | 1.52 |
| 9 | 491 | 491 | 300 | 300 | 300 | 6.05m | 4.67 | 1.52 |

Table 2. Initial test plan

On the day of testing vehicle 490 was unavailable so tests 2 and 4 were omitted.

Figure 1. Test plan flow diagram. See Table 2 for test details.

## Environmental Requirements

Oscillations during hover have been observed in multiple wind conditions, however light crosswinds most commonly trigger the phenomenon. With higher winds, the aircraft weathervanes, making crosswinds impossible.

Any future testing will require the oscillatory behavior be replicated to establish environmental conditions are representative.

## Yaw Command Investigation

As the vibration issue seems most prevalent during a crosswind, the controls related to maintaining a bearing while hovering could be influencing the wing oscillation during hover. High speed burst data was taken during hovers with and without oscillation for analysis.

## Wing Stiffness Investigation

One theory is that our newer aircraft feature a slightly stiffer wing assembly that has pushed the natural frequency of the assembly closer to whatever excitations are found in during hover. This increase in stiffness would be from various process improvements in our manufacturing.

Wing assemblies were supported six inches from each wingtip and various weights were added to the center. A string was held under tension running between the two supports, acting as a datum to measure deflection. A spread of measurements was used to characterize the stiffness of each wing assembly tested. A chart showing these stiffnesses can be found in the results section of this report.

## Results

## Root Cause Investigation

The actual test deviated from the test plan listed above slightly as oscillation/wobble proved to be more complex than a single component issue. Trials that deviated from the initial test plan have a letter added (e.g. 6a). Tests are listed in chronological order. Ryan Christino and Jack Waeschle carried out testing.

Test 1: VXE 491 achieved significant oscillations/wobble in our current configuration of firmware (VTOL 1.52).

Test 3: We then rolled the VTOL software back to the previous customer release (1.44) and the same oscillations were observed.

Test 5: After rolling the VTOL firmware forward to the current version (1.52), we swapped in the entire wing assembly from vehicle 300 (the least stiff we have measured) including the original, looser fitting spar joiner tubes that were recently replaced on that aircraft. The center wing from 300 produced completely smooth hover, suggesting this oscillation is a linked to the mechanical properties of our newer wings.

Test 6a: Center wing, lift booms and joiners from 300 with 491 wing tips produced very smooth hover. This suggests that wing tips do not influence wobble.

Test 7: 300 center wing with 491 wing tips, joiners & lift booms produced moderate wobble.

We repeated this flight and observed moderate/high wobble. This suggests joiner tubes and lift boom assemblies influence wobble.

Test 6b: Center wing and joiners from 300 with 491 wing tips and lift booms produced moderate/low wobble. This suggests lift booms alone can influence wobble.

Test 6c: Center wing, joiners and wing tips from 491 with 300 lift booms produced low wobble. Confoundingly, lift booms are not the only factor in wobble.

Test 8: Center wing, joiners, wing tips from 300 with 491 lift booms produced medium/low wobble. Clearly lift booms are part of the equation though.

Takeaways

This testing was very useful for getting a better understanding of this phenomenon. We believe the lift booms are a contributor, but this is a more complex issue than a single component, as test 6c and test 8 show. This appears to be a mechanical issue, as some combination of components will produce wobble while some combinations do not. The firmware/control system though is also involved though as aircraft do not wobble while sitting stationary on the ground. A more representative test could be holding the aircraft above one’s head with a crosswind to better expose the aircraft to a freestream flow, but it would be very surprising to achieve wobble with wind alone while the vehicle is powered off. This is an avenue for further investigation.

## Yaw Command Investigation

As this behavior is most commonly seen with a crosswind, the aircraft must be giving a yaw command to counteract the tendency to weathervane. This can be seen by a separation in power between the front right and front left VTOL motors in the first half of figure 2a below.

The following plots correspond to VXE 491 with center wing 4024 during SCO flights on March 23rd. There was a 5-6 mph wing with 8 mph gusts (measured with an anemometer 8 feet off the ground).

Figure 2a. Flight log data for cross wind landing with wobble.

These flight log data show a separation of power between the two front VTOL motors during the initial descent of landing. This represents a yaw command as the aircraft maintains its bearing instead of weathervaning. The right front motor (green) has consistently higher power than the left front motor (orange) for the initial descent. The first green spike to 94% throttle limit corresponds to a pause during the descent. Wobble began after a nudge command that can be seen in the yellow box in figure 2b.

Figure 2b. Close up of hover condition. Note the cyclical power separation between left and right VTOL motors.

These data are not from a high rate burst and are sampled at about 10 Hz. Burst data is sampled at about 100 Hz. As mentioned above, the nudge command caused the plane to roll to the right and then left a few times and can be clearly seen in the separation in power between the right and left side VTOL motors. Otherwise, these data show little to indicate wing resonance is occurring. Burst data could prove more enlightening.

Figure 3. Oscillation free landing.

On the subsequent flight, the vehicle weathervaned and then had a smooth, stable descent, hover and landing. Both with and without oscillations, the power commands have a lot of noise. Future investigations could attempt to reduce these small spikes in power.

At this time the burst data has not been investigated and this analysis will be left to a future revision of this document.

## Wing Stiffness Investigation

The following measurements indicate that newer wing assemblies are stiffer than older, well used ones. This could be from small failures in bond lines or cracks in foam cores, however this is entirely speculative.

Figure 4. Wing stiffness characterization. Vehicle 300 is the oldest included in this test.

## Conclusion

## Summary of Results

These investigations failed to find a single smoking gun. However, it seems that our stiffer wings and control system are prone to approaching resonance when faced with a crosswind. The vibrations should be directly related to the VTOL system as the aircraft sitting on the ground with a light crosswind does not begin to shake. If we were to pinpoint a single structural component that was causing the resonance, the solution would likely still involve modifying the control system to tune out this behavior. This could be accomplished but would require a lot of experimental testing to validate.

Currently, the most extreme oscillations are far from causing a structural failure. While oscillating, vehicles still maintain flight controls and function, and thus we do not think this issue poses a direct risk to customer assets.

## Future Investigations

If we choose to further pursue this issue, the solution likely lies within tuning our VTOL firmware control system to reduce or eliminate the vibration during crosswind hover with our newer, stiffer wing assemblies. The first step in this process would be analyzing the burst data from the root cause testing documented in this report. This burst data can be found in a zip file attached to the Jira ticket mentioned earlier in this report.

Additionally, center wings could be further inspected for both lateral and torsional rigidity using the center wing fixture designed by Will. Currently we do not quantify or control for these stiffnesses, and finding how much these values vary from aircraft to aircraft could be useful for both this analysis and for validating new vendors.
