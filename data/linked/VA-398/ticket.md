# VA-398: TPTR-101 Battery Charging Failure with 12V DC-Identify C/CA

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-08-29
- **Updated:** 2023-11-09
- **Resolved:** 2023-09-29
- **Reporter:** Cameron Chapman
- **Assignee:** Madeleine Masiello
- **Creator:** Cameron Chapman
- **Links:** relates to VXEP-23 (TPTR-101 Battery Charging Failure with 12V DC)
- **Sprint:** VXE-1 Cameron's Team 9-17, VXE-1 EE Team Sprint 8/28-9/17

## Description

See attachments. Charger is supposed to be programmed to 10.5V min, but is displaying input voltage <12.6V error.

**Investigation Plan**

- The battery charger manufacturer may have put the cutoff at 12.6V to avoid you draining your car battery. It tends to guide the user to operate the charger with the car running, which is really what you’d want to do. There may be a workaround here that would allow us to meet the requirements: use the inverter in the FSK, run the charger with the AC power supply. The inverter might let you go to a lower input voltage. I recommend the shortest, lowest cost path to closure of this bad requirement.
- Is it worth it to get ISDT to update firmware for this requirement?

## Comments (20)

### Cody Smisek, 2023-08-30

@Maxime Jeanneau @Cameron Chapman 12V power supply was the power supply provided with the chargers / battery kits. You can modify the power supply to provide 12VDC instead of 24VDC or whatever its default is. The charger was ours that is provided in the battery kits. The charger was supposedly good to 12VDC input. But when 12VDC input is provided, the charger screen shows “input voltage lower than 12.6V”.

### Cameron Chapman, 2023-08-30

@Cody Smisek Is there a contract requirement to operate the power supply at 12V, or why was it set to 12V instead of 24? 
I think the chargers are set to a 10V minimum, so it may have been misconfigured. We need to check the vault version of this document (don’t have VPN currently). 
Do you know if there is any log of what charger was used, or which chargers you would recommend checking? 
@Madeleine Masiello are you available to help check these once we have an idea where to look?
[embedded: Customized Q8 Max Battery Charger Specification-p3.docx]

### Madeleine Masiello, 2023-08-30

@Cameron Chapman Yes, that sounds good I can help.

### Cody Smisek, 2023-08-31

I will create a presentation of what was performed.

### Cody Smisek, 2023-08-31

@Cameron Chapman see attached slides. Log of tested equipment is irrelevant but I will track it down. Let me know if further information is required.

### Cody Smisek, 2023-08-31

Added this comment to wrong place yesterday, adding here to right place. @Cameron Chapman Indago is having same issue, possibly same charger being used. They’re developing a solution. LMUK to possibly share information. @Sam Miller may have more information

### Cody Smisek, 2023-09-05

@Cameron Chapman I have no further information to provide at this time. Reassigning.

### Cameron Chapman, 2023-09-05

@Hayden Jeanor you are welcome to see if interns or others can help with this.

### Sam Miller, 2023-09-06

The battery charger manufacturer may have put the cutoff at 12.6V to avoid you draining your car battery.  It tends to guide the user to operate the charger with the car running, which is really what you’d want to do.  There may be a workaround here that would allow us to meet the requirements: use the inverter in the FSK, run the charger with the AC power supply.  The inverter might let you go to a lower input voltage.  I recommend the shortest, lowest cost path to closure of this bad requirement.

### Cameron Chapman, 2023-09-09

The charger custom firmware is supposed to enable operation to 10V, but something seems to have gone wrong.
@Madeleine Masiello, after you confirm our production chargers don’t operate with 12V in, you can check the minimum voltage of the inverter in the FSK.

### Madeleine Masiello, 2023-09-11

@Cameron Chapman After taking a look and probing the connection to the battery charger, I didn’t find or see any odd voltage drops. While there was expected noise, the average voltage was seemingly steady and accurate to the power supply. However, as expected, the error message popped up when I set the voltage less than 12.7V, which means that the production chargers do not operate as they should. Taking a look at the minimum voltage of the inverter in the FSK now.

### Cameron Chapman, 2023-09-11

Thanks @Madeleine Masiello are you able to manually change the minimum in settings, or is that prevented by our custom FW? Does it display the minimum?

### Madeleine Masiello, 2023-09-11

Under system settings, I was able to find that the “Lowest input voltage” is set to 12.6. I wasn’t able to change it. I have attached a picture of what I am seeing. @Cameron Chapman This seems to be our error.
[embedded: MicrosoftTeams-image.png]

### Cameron Chapman, 2023-09-11

Piecing together email history and attaching. It looks like i requested changing the min voltage to 10.5V on 3/30/22, but it may not have ever been confirmed. 
[embedded: RE_ Charger Status.msg]
This may have been after Sam recommended it lowered. I can dig more later. For now, we can focus on the inverter idea.

### Cameron Chapman, 2023-09-11

Confirmed, we never actually updated the min voltage. From: Cameron Chapman 
Sent: Friday, February 25, 2022 10:12 AM
To: LM Dustin Gamble <dustin.gamble@lmco.com>
Cc: Lawton Ziedses Des Plantes <lzdp@edgeautonomy.io>; Victor Vandor <vvandor@edgeautonomy.io>; Kyle DeBernardi <kdebernardi@edgeautonomy.io>; Briana Hitchen <bhitchen@edgeautonomy.io>; Sam Miller <smiller@edgeautonomy.io>; LM Matthew Curran <matthew.curran@lmco.com>; Gordon Jennings <gjennings@edgeautonomy.io>; Elias Sullwold <esullwold@edgeautonomy.io>
Subject: 96X-3-08-1503 Alligator Clips replacement. Charger min voltage change.
 
Good morning everyone, specifically Sam, Matt, Dustin,
 
I tested a sample of each battery clip to replace the obsolete ones, and think CT4410 (below) is the best option. It is easier to install, looks more professional, and does not require us soldering a banana socket onto the clip. I also tested both charging a main battery at 13A with my car running. Both temps stayed reasonably cool (Old ~49C max, new 44C max at the 4mm banana plug). We expect them to get warm, as the main battery charge requires ~30A from a car battery.  Let me know if you disagree. I’ll leave a sample of each on my workbench if you’d like to check them out.
 
Also, I think we should change our minimum charger input voltage. It is currently set to 12.6V (value from XE25 selected to ensure alternator is running and charging a car battery). In the case of my Civic, is seems like the alternator turned off during the charge (I think because the car battery was full, but I’m not a car expert), which set the voltage to 12.5 OCV and stopped the charge. I think a value of 11V would be better. This way, you could charge from a car battery with the engine running or not, but it should still cutoff the charge before the car battery was empty. Please let me know if you recommend another value. We will have to contact ISDT to update the firmware accordingly.

### Madeleine Masiello, 2023-09-12

FSK inverter looks good at 12V. Attaching video/pictures of test for reference. @Cameron Chapman 
[embedded: MicrosoftTeams-image (2).png]
[embedded: MicrosoftTeams-image (1).png]
[embedded: IMG_6718.mov]

### Cameron Chapman, 2023-09-12

Great work and good idea Sam. After reviewing the requirement, it looks like we will have to document charging both batteries to complete this requirement. 
@Madeleine Masiello  and @Mark Squillante , can you please do the following tomorrow?
- Clean up the bench. Stage equipment for good photos (they may be submitted to the customer).
- Repeat HLB test and photos.
- Repeat for main battery charge


Acceptance Criteria
Demonstrate for the system that the system batteries can be charged from 12/24/110/240 volts supply e.g. DC or AC from a vehicle battery, generator or mains power supply.

### Madeleine Masiello, 2023-09-12

@Cameron Chapman Yes that sounds good I can do that. Thanks

### Madeleine Masiello, 2023-09-13

@Cameron Chapman@Mark Squillante  We repeated the hybrid battery test, and also the main battery test. 

Here are the photos of the hybrid battery test: 
[embedded: hybrid1.png]
[embedded: hybrid3.png]
[embedded: hybridredo.png]

Here are the photos of the main battery test:
[embedded: main2.png]
[embedded: main4.png]
[embedded: main redo.png]

Let me know if these look okay. Not too hard to run the tests again if needed.

### Carl Graf, 2023-09-28

@Cameron Chapman was just taking a look at the Uberboard and came across @Madeleine Masiello for this ticket. Should this be closed or reassigned?

## Attachments (13)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [Customized Q8 Max Battery Charger Specification-p3.docx](attachments/16078_Customized%20Q8%20Max%20Battery%20Charger%20Specification-p3.docx.md) | docx | 2402 | 2023-08-30 | converted |
| [detailed Explanation of battery charginer 12v error.pptx](attachments/16079_detailed%20Explanation%20of%20battery%20charginer%2012v%20error.pptx.md) | pptx | 935 | 2023-08-31 | converted |
| MicrosoftTeams-image.png | image | 1655 | 2023-09-11 | listed only |
| [RE_ Charger Status.msg](attachments/16198_RE_%20Charger%20Status.msg.md) | msg | 248 | 2023-09-11 | converted |
| IMG_6718.mov | video | 26685 | 2023-09-12 | listed only |
| MicrosoftTeams-image (1).png | image | 1963 | 2023-09-12 | listed only |
| MicrosoftTeams-image (2).png | image | 1424 | 2023-09-12 | listed only |
| hybrid1.png | image | 1135 | 2023-09-13 | listed only |
| hybrid3.png | image | 1064 | 2023-09-13 | listed only |
| hybridredo.png | image | 164 | 2023-09-13 | listed only |
| main redo.png | image | 157 | 2023-09-13 | listed only |
| main2.png | image | 1459 | 2023-09-13 | listed only |
| main4.png | image | 1766 | 2023-09-13 | listed only |
