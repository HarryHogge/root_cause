# VXEP-262: 100-106956 MGRM-WHF-3A-BLK-120 Ordering Uncertainty

- **Issue type:** Problem
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-01-30
- **Updated:** 2024-04-05
- **Resolved:** 2024-04-05
- **Reporter:** Cameron Chapman
- **Assignee:** Wesley Lilienthal
- **Creator:** Cameron Chapman
- **Links:** relates to VA-1203 (100-106956 data card description update: Is 1.7 - 6GHz, should be 1.7 - 7.2GHz); relates to VA-1291 (Create or update documentation for 100-106956 to meet new processes)
- **Issue color:** purple
- **Production Stakeholder:** Trevor Gronner
- **Supply Chain Stakeholder:** Laura Bertule
- **Other Stakeholder (as required):** Nadia Brown

## Description

Status: Assigning to @Laura Bertule to place order. She can then assign to @Carson Buckley to test or delegate test when it arrives. 

Sort out ordering uncertainty. See email in comments.
Our Mfr PN: MGRM-WHF-3A-BLK-120   //  3 dBi 1.7-6GHz Mag Mount Antenna w 10ft. RF-195, TNC-Male
New spec sheet/quote: MGRM-WHF-3A-BLK-120 Broadband Mag antenna, with 10 ft low loss LL-195 cable, TNC-male, (1.7- 7.2GHz) 
Spec sheet: 1.7 - 7.2 GHz , 5 dBi Peak
16-249-UNIT COST: $81.50

## Plan

@Wesley Lilienthal since this is for SGCS1 silvus radios, I think you are the best person to answer this. Can you please review the new vs old equipment and determine if they are both acceptable? If so, please coordinate completing the engineering change.

## Comments (21)

### Cameron Chapman, 2024-01-30

New description is approved. Spec was updated by the mfr. 
New Desc: 1.7 - 7.2 GHz , 5 dBi Peak (this wider range and higher gain indicates antenna performance has improved)
Old Desc 3 dBi 1.7-6GHz.
Since we don’t have a NHA accessible currently, I recommend fixing that and testing the unit as soon as it arrives.

### Cameron Chapman, 2024-01-30

Assigning to @Laura Bertule to place order. She can then assign to @Carson Buckley to test or delegate test when it arrives. Sound good?

### Laura Bertule, 2024-01-30

Sounds good!

### Carson Buckley, 2024-01-30

@Cameron Chapman This looks like a surface mount UHF and not a mag mount, unless I’m misunderstanding?

### Cameron Chapman, 2024-01-31

@Carson Buckley from the datasheet. “MGRM-WHF ( Mag Mount Model )"I have not looked into how we currently use this part. I think it is used in SGCS1
[embedded file]

### Carson Buckley, 2024-01-31

@Cameron Chapman These are used for SGCS1 as extended antennas for the hand-held Silvus radios. They must be magnet mount base to be of any use in this application.

### Cameron Chapman, 2024-01-31

@Carson Buckley sounds good. It seems like MGRM-WHF is magnet mounted, which is the part we are ordering. Same PN, updated spec sheet.

### Laura Bertule, 2024-01-31

@Cameron Chapman @Carson Buckley Yes, the MGRM is magnet mounted and that is what I have issued the order for.

### Mark Squillante, 2024-03-07

@Cameron Chapman @Carson Buckley did this get resolved yet? I created an ECN for the update here: https://jenaero.atlassian.net/browse/VA-1203

### Laura Bertule, 2024-04-01

@Carson Buckley @Cameron Chapman @Wesley Lilienthal  this is still stuck in QA. What needs to be done to get this moving? This is already a production stoppage.

### Cameron Chapman, 2024-04-02

@Wesley Lilienthal since this is for SGCS1 silvus radios, I think you are the best person to answer this. Can you please review the new vs old equipment and determine if they are both acceptable? If so, please coordinate completing the engineering change. 
FYI @Laura Bertule

### Wesley Lilienthal, 2024-04-03

@Cameron Chapman - Yes, will do.
@Laura Bertule - Are you able to provide the older spec sheet you mention below as having a discrepancy in the peak gain figure (in dBi)? I do not expect an extended operating range upper limit from 6 GHz to 7.2 GHz to be an issue alone, but a revision to peak gain suggests that the antenna element(s) may in fact be different, contrary to the vendor’s indication in your email thread below that the antenna has not changed. I need to review the old spec sheet against the new.

### Laura Bertule, 2024-04-03

@Wesley Lilienthal I have requested it from our Vendor.

### Wesley Lilienthal, 2024-04-03

@Laura Bertule Thank you. Would you please clarify what you meant when you said in the below email thread that “dBi Peak looks different”? Was this in reference to the change from “1.7 - 6 GHz” to “1.7 - 7.2 GHz” on the line that also calls out “5 dBi Peak”? Did you observe a difference in the peak gain figure of 5 dBi, or only a difference in the frequency range with the increase from 6 GHz to 7.2 GHz?

### Laura Bertule, 2024-04-03

@Wesley Lilienthal at the time when I placed the order, all I had was the information in the Vault and SP, and in the Vault it states 3dBi, this potentially means that information in the Vault could be wrong or obsolete?

### Cameron Chapman, 2024-04-04

@Wesley Lilienthal since the old one is not available, I do not think they have to be 100% identical. The new one just needs to be compatible. I think a functional test should suffice. Do you agree? 
@Carson Buckley are you available to do that?

### Carson Buckley, 2024-04-04

@Cameron Chapman @Wesley Lilienthal Functional check for these is “connect to a radio and verify it works”. This is not a test that needs to be run by SCO. If you need a more defined answer then they can also be checked on the VSWR by a technician trained to use it.

### Wesley Lilienthal, 2024-04-04

@Laura Bertule - Thank you for advising. I see the inclusion of 3 dBi in the description for this antenna in the vault, and have inquired with the vendor for clarification. 
@Cameron Chapman The difference between the 3 dBi figure included in our description and the 5 dBi figure included in both the previous and current spec sheets from the vendor is the current wrench in the gears, as if the peak gain has indeed changed from 3 dBi to 5 dBi, it implies a meaningful change to the radiated efficiency and/or directivity of the antenna that would meaningfully affect real-world performance. 5 dBi is not necessarily better than 3 dBi. It depends upon the application, as such a change to peak gain implies increased directivity if not solely due to an improvement to efficiency. We need to know the exact effects on the radiation pattern in order to conclusively determine whether such a change is acceptable. Measuring the radiation pattern requires an anechoic chamber and specialized equipment that we do not have and would require outsourcing to accomplish. In order to determine if the current antenna is compatible with the old, we need this radiation pattern characterization data. VSWR testing with a VNA may be a reasonable substitute as long as measurements turn out identical. If not identical, pattern data is required to determine the reason for the differences observed. That said, I suspect the vendor may not have actually changed the antenna electrically, and may have simply revised the spec to more-accurately reflect the actual performance of the antenna. 
I have called the vendor and sent the below email requesting confirmation or clarification from their Engineering team: 
Hi Danny,
Thank you for the quick chat today. Per our discussion, would you please inquire with your engineering team whether the MGRM-WHF-3A-BLK-120 has changed from a radiated performance standpoint since we began procuring it from you and to what degree if so? We have in our system the description "3 dBi 1.7-6GHz Mag Mount Antenna w 10ft. RF-195, TNC-Male" for this antenna. The two most notable differences between the current spec/description and previous spec/description that we have are:
- A change from 3 dBi peak gain listed in our existing description to 5 dBi peak gain listed in both the "(005) (Previous Version)" and current Rev 2 RA-08/2023 spec sheets.
- A change in the operating frequency range from "1.7 - 6 GHz" listed in both our existing description and the "(005) (Previous Version)" spec sheet to "1.7 - 7.2 GHz" listed in the current Rev 2 RA-08/2023 spec sheet.

I suspect the increase of the upper end of the operating frequency range from 6 to 7.2 GHz may simply be a spec update to match the actual performance the antenna and may not represent a change to the antenna element(s) itself. Please confirm or clarify this.
A change from 3 dBi to 5 dBi peak gain, however, appears to represent a meaningful change to either the efficiency and/or directivity of the antenna, implying a material change to the antenna element(s) and radiated performance.
Would you please advise whether the MGRM-WHF-3A-BLK-120 has changed at all electrically since our initial procurement of this antenna, such that radiated performance is different than it has been in the past? Or are the above changes to operating frequency range and peak gain exclusively spec changes that represent no actual difference in performance?
Attached are the two spec sheets referred to above for reference. 
Appreciated, 
- Wes

### Wesley Lilienthal, 2024-04-04

The vendor (MobileMark) has responded that the antennas have in fact been redesigned, which accomplished the expanded operating frequency range (extended to 7.2 GHz). This means we should evaluate the performance of both old and new designs and compare. As described below, this is ideally radiation pattern data, which requires either obtaining it from the vendor (I have requested) or outsourcing anechoic chamber measurements. Alternatively, and I think justified, is measuring VSWR/Return Loss on both old and new designs and using to compare. This is very rudimentary gauge, but seems justified for this antenna and its use case. 
I will proceed with VSWR/Return loss measurement of old and new designs, and also hope for radiation pattern data from the vendor.  
I have placed both old and new tech sheets (from vendor Engineering) and spec sheets (from vendor Marketing) on the vault here: C:\JAI Vault 1\Shared\COTS Information\MobileMark

### Wesley Lilienthal, 2024-04-05

The vendor has provided radiation pattern data for both old and new designs. I have reviewed, and the two designs are equivalent to a meaningful degree, with no red flags. Slightly higher peak gain is in fact achieved at some elevation angles with no meaningful degradation elsewhere in the pattern, suggesting improved efficiency.
Tech sheets, spec sheets, and radiation pattern documents are attached, and are located on the vault here: C:\JAI Vault 1\Shared\COTS Information\MobileMark
The 3 dBi figure listed in the description of the part in our vault must have come from a description on the price list from the vendor in the paast. This 3 dBi gain figure is called out as typ gain in the radiation pattern document for the old design, beside the 5 dBi peak gain figure.
In summary, the vendor revised the design, increasing the upper end of the operating frequency range, kept the same part number, and did not notify us of the change. Data describes the change as a net wash if not a net win in performance. No further validation is necessary from my perspective aside from whatever binary pass/fail check we do during SCO prior to shipment. The existing vendor part number stands unchanged: MGRM-WHF-3A-BLK-120
See https://jenaero.atlassian.net/browse/VA-1203 for ECN process.

[embedded file][embedded file][embedded file][embedded file]

### Wesley Lilienthal, 2024-04-05

The vendor has provided radiation pattern data for both old and new designs. I have reviewed, and the two designs are equivalent to a meaningful degree, with no red flags. Slightly higher peak gain is in fact achieved at some elevation angles with no meaningful degradation elsewhere in the pattern, suggesting improved efficiency.
Tech sheets, spec sheets, and radiation pattern documents are attached, and are located on the vault here: C:\JAI Vault 1\Shared\COTS Information\MobileMark
The 3 dBi figure listed in the description of the part in our vault must have come from a description on the price list from the vendor in the paast. This 3 dBi gain figure is called out as typ gain in the radiation pattern document for the old design, beside the 5 dBi peak gain figure.
In summary, the vendor revised the design, increasing the upper end of the operating frequency range, kept the same part number, and did not notify us of the change. Data describes the change as a net wash if not a net win in performance. No further validation is necessary from my perspective aside from whatever binary pass/fail check we do during SCO prior to shipment. The existing vendor part number stands unchanged: MGRM-WHF-3A-BLK-120
See https://jenaero.atlassian.net/browse/VA-1203 for ECN process.

[embedded file][embedded file][embedded file][embedded file]

## Attachments (7)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [RM-WHF-Spec-Sheet 1.pdf](attachments/18545_RM-WHF-Spec-Sheet%201.pdf.md) | pdf | 221 | 2024-01-30 | converted |
| image-20240131-173727.png | image | 82 | 2024-01-31 | listed only |
| [RM-WHF-Spec-Sheet (005) (Previous version).pdf](attachments/19814_RM-WHF-Spec-Sheet%20(005)%20(Previous%20version).pdf.md) | pdf | 328 | 2024-04-03 | converted |
| [MGRM-WHF-3A-BLK-120 - Antenna Radiation Patterns - New Design With Expanded Operating Frequency Range.pdf](attachments/19885_MGRM-WHF-3A-BLK-120%20-%20Antenna%20Radiation%20Patterns%20-%20New%20Design%20With%20Expanded%20Operating%20Frequency%20Range.pdf.md) | pdf | 275 | 2024-04-05 | converted |
| [MGRM-WHF-3A-BLK-120 - Antenna Radiation Patterns - Old Design.pdf](attachments/19887_MGRM-WHF-3A-BLK-120%20-%20Antenna%20Radiation%20Patterns%20-%20Old%20Design.pdf.md) | pdf | 343 | 2024-04-05 | converted |
| [MGRM-WHF-3A-BLK-120 - Tech Sheet (Engineering) - New Design With Expanded Operating Frequency Range.pdf](attachments/19886_MGRM-WHF-3A-BLK-120%20-%20Tech%20Sheet%20(Engineering)%20-%20New%20Design%20With%20Expanded%20Operating%20Frequency%20Range.pdf.md) | pdf | 135 | 2024-04-05 | converted |
| [MGRM-WHF-3A-BLK-120 - Tech Sheet (Engineering) - Old Design.pdf](attachments/19884_MGRM-WHF-3A-BLK-120%20-%20Tech%20Sheet%20(Engineering)%20-%20Old%20Design.pdf.md) | pdf | 79 | 2024-04-05 | converted |
