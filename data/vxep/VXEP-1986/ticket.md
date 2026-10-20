# VXEP-1986: B30 Customer Furnished CRPA Integration Causing 12V Bus Issues

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2026-08-25
- **Updated:** 2026-08-27
- **Resolved:** 2026-08-27
- **Reporter:** Jeremy Kostel
- **Assignee:** Matthew Aguirre
- **Creator:** Jeremy Kostel
- **Links:** relates to FS2-4192 (12v Current Sense Scaling Showing Current Overload (2025 ADP Major Contributor) ); relates to VA-2936 (B30 Advanced nav ICD has incorrect information about the APNT port 12V capacity)
- **Issue color:** dark_purple

## Description

Investigation into excessive current draw indications on the B30 12V_SWITCHED bus and associated CRPA integration anomalies observed during testing of aircraft 575 and 576.
During initial flight testing with CRPA antennas installed, multiple anomalies were observed including intermittent GNSS availability, SA camera disruptions, and reported high current draw on the 12.8V_SWITCHED bus. Early troubleshooting suggested that CRPA power consumption may have exceeded the available power budget of the 12V bus. Reported current measurements included approximately 2.7A for CRPA SN82 and 4.4A for CRPA SN124, compared to approximately 0.44A observed with the FRPA installation. These observations led to an initial assessment that the CRPA installations may have been overloading the bus and contributing to bus protection events.
Ground testing was performed in SLO by Matthew Aguirre and Christopher Booker using benchtop power supplies, aircraft-level testing, and the B30 Integration Bench. Testing demonstrated that the primary issue was not excessive CRPA power consumption but an incorrect current scaling factor present in software build 2ae959d (SW Release 6.6.1). The current gain on the 12.8V_SWITCHED monitor was effectively halved, causing the XCOMM to report approximately 2x the actual current draw. The same behavior was reproduced on aircraft 575, aircraft 576, and the B30 Integration Bench operating on the same software build.
Measured CRPA power consumption was determined to be:
- CRPA SN82: ~0.99A (12.7W) on benchtop testing
- CRPA SN84: ~1.50A (19.2W) on benchtop testing
- CRPA SN124: ~1.78A (22.8W) on benchtop testing

Aircraft and integration bench testing showed corresponding current monitor readings approximately twice the actual load:
- SN82: 2.6 to 2.7A reported, ~1.3A actual
- SN84: 3.7A reported, ~1.8A actual
- SN124: 4.5 to 4.7A reported, ~2.2 to 2.4A actual

These results confirmed that the reported overcurrent condition was largely attributable to the software current-monitor scaling issue rather than a CRPA hardware fault or aircraft electrical integration issue.
A separate GNSS issue was identified on aircraft 575 only. Unlike aircraft 576, none of the tested CRPA units would power on when installed on aircraft 575, while the FRPA operated normally. Investigation by Christopher Booker, Carson Buckley, and Connor Peebles determined that the root cause was a recessed pin in the avionics box blind-mate connector supplying power to the CRPA interface. Because the CRPA and FRPA utilize different power pins, the FRPA remained operational while all tested CRPA units failed to power. After reseating the recessed pin, CRPA power was restored and GNSS functionality returned, confirming the root cause as a connector workmanship issue rather than a NovAtel, center wing, or CRPA hardware problem.
The investigation concluded that:
- The initially suspected excessive CRPA current draw was not the primary issue.
- Current reported on the 12.8V_SWITCHED monitor was approximately double the actual load due to a software scaling error in the installed firmware build.
- GNSS failures on aircraft 575 were caused by a recessed power pin in the avionics box blind-mate connector.
- No systemic CRPA hardware issue was identified.
- Aircraft 575 and 576 are capable of supporting CRPA operation when the software and connector discrepancies are addressed.

## Plan

- Increase the 12.8V_SWITCHED current limit from 3A to 6A as a short-term mitigation to support CRPA flight testing on aircraft 575 and 576.
- Update aircraft to the latest approved software release containing the corrected 12.8V_SWITCHED current-monitor scaling as the long-term corrective action.
- Perform verification ground testing following software update to confirm current reporting accuracy and proper overcurrent protection behavior.
- Verify continued GNSS operation on aircraft 575 following correction of the recessed blind-mate connector pin.
- Validate CRPA operation with flight-test hardware configurations and ensure adequate power margin, particularly when operating higher-power units such as SN124.
- Document test results, implemented corrective actions, and configuration recommendations for future CRPA integrations

## Issue Status

Closed / Root Cause Identified
Investigation determined that the initially suspected excessive CRPA current draw was not the primary cause of the observed anomalies. Ground testing on aircraft 575, aircraft 576, and the B30 Integration Bench demonstrated that software build 2ae959d (SW Release 6.6.1) incorrectly reported approximately 2x the actual current on the 12.8V_SWITCHED bus due to current-monitor scaling. Actual CRPA power consumption was within expected operating ranges and no CRPA hardware fault was identified.
A separate GNSS issue affecting aircraft 575 was traced to a recessed power pin in the avionics box blind-mate connector that prevented CRPA power from reaching the unit. After the pin was properly seated, CRPA power and GNSS functionality were restored.
Short-term mitigation is to increase the 12.8V_SWITCHED current limit from 3A to 6A for flight-test support. Long-term corrective action is to upgrade to the latest approved software release containing the corrected current-monitor implementation. Root causes have been identified and corrective actions defined.

## Comments (3)

### Matthew Aguirre, 2026-08-25

Working with Chris Booker and Jimmy Powell (mainly Chris) in troubleshooting the different CRPA modules, mainly SNs 82, 84, and 124. Based on testing of benchtop power supply, IB B30, and AC 575, I am recommending that both AC 575 and 576 have their 12.8V_SWITCHING current limit increased from 3A to 6A as a short-term solution for preparing for flight tests (long term solution would be updating to newest FW). Both 82 and 84 CRPAs should be fine to fly with no problems. 124 CRPA is close to the limit proposed by Jacob, therefore I am recommending that at the very least blinkers are disabled, heated pitot ADP is installed, and no fuel cell installed, to allow for proper headroom while flying. Summarized findings below:

Both XCOMMs on AC 576 and 575 were on the same build (2ae959d, tied to SW release 6.6.1 in dec 2025) as the XCOMM on B30 IB which did not include the increase in 12.8V_SWITCHING current limit from 3A to 6A. This is due to the current gain being halved, which doubles the actual current before displaying as the measured value. The fixed software build wasn’t released until April 2026. 

CRPAs 82, 84, and 124 are different modules that have different power requirements. The following measurements were taken after 5 minutes of waiting for the CRPAs to “stabilize” their readings.
| Using iTech IT6722A power supply, directly connected to CRPA units.  Vset = 12.8, I_lim = 2A. |
| Unit SN | Current Draw (A) | Calculated Power Draw (W) |
| 82 | 0.99 | 12.67 |
| 84 | 1.5 | 19.20 |
| 124 | 1.78 | 22.78 |

| Connecting to AC 576 (just fuselage w/ only MB and center wing w/ ADP installed) |
| Unit SN | Current draw reported by XCOMM 12.8V_SWITCHING (A) | Actual estimated current draw (A) | Calculated Power Draw (W) |
| FRPA unit | 0.372 | most likely smaller than 20mA, as current draw reported by XCOMM 12.8V_SWITCHING was about the same value when FRPA was disconnected. |  |
| 82 | 2.611 | 1.3055 | 16.71 |
| 84 | 3.686 | 1.843 | 23.59 |
| 124 | 4.47 | 2.235 | 28.61 |

| Connecting CRPAs to B30 IB (measurements were slightly higher |
| Unit SN | Current draw reported by XCOMM 12.8V_SWITCHING (A) | Actual estimated current draw (A) | Calculated Power Draw (W) |
| 82 | 2.7 | 1.35 | 17.28 |
| 84 |  |  |  |
| 124 | 4.7 | 2.35 | 30.08 |



As a separate note for the GNSS connectivity issues. Since this was a bit more than I could chew, I reached out to @Connor Peebles for assistance in troubleshooting, after Carson Buckley was unable to assist Chris B. and I. Connor found that the problem was the pin that feeds power to the CRPA was recessed, which is a different power pin that feeds to the FRPA. This explains why after replacing the CW to rule out communication issues and trying 3 different CRPA modules on AC 575 did not yield any solutions. Theoretically after properly seating the pin, the Novatel should behave as expected and should interface with the CRPAs similarly to AC 576. Although further ground testing should be done to provide assurance.

### Connor Peebles, 2026-08-25

@Matthew Aguirre After correcting the recessed pin10 on the blindmate connector of the AC575 avi box, Chris’s CRPA module did indeed power up and he was able to connect to it just as the other three aircraft!

### Jacob Troyer, 2026-08-27

Adding comment about 12V bus power with added equipment beyond CRPAs for future reference. Summary below, excel attached if someone wants to modify: [embedded file] 

[embedded image-20260827-191431.png]

## Attachments (7)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T115_V576_260824_133947_01_pack (1).zip | archive | 1199 | 2026-08-25 | listed only |
| T115_V576_260824_133947_pack (1).zip | archive | 2093 | 2026-08-25 | listed only |
| image (5).png | image | 24 | 2026-08-25 | listed only |
| image (6).png | image | 60 | 2026-08-25 | listed only |
| image-20260130-165835.png | image | 157 | 2026-08-25 | listed only |
| [U5 12V w CRPA Power Numbers.xlsx](attachments/64318_U5%2012V%20w%20CRPA%20Power%20Numbers.xlsx.md) | xlsx | 10 | 2026-08-27 | converted |
| image-20260827-191431.png | image | 41 | 2026-08-27 | listed only |
