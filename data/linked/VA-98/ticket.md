# VA-98: Review VXE371 for overweight and above nominal current draw during AEWE

- **Issue type:** Sub-task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2023-05-11
- **Updated:** 2023-11-09
- **Resolved:** 2023-05-17
- **Reporter:** Cody Smisek
- **Assignee:** Cody Smisek
- **Creator:** Cody Smisek
- **Parent:** VA-93 Record typical, max, and max tested lift current and voltage profiles. Save test data to confluence. Establish and implement limits and abort if exceeding.
- **Links:** relates to ENG-2987 (VXE371 Centerwing Boom Power Connecter Melted / signs of overheat or arcing); relates to VA-93 (Record typical, max, and max tested lift current and voltage profiles. Save test data to confluence. Establish and implement limits and abort if exceeding.)

## Sprint

VXE-1 Electrical-8, VXE-2 Everything Else 2024-03, VXE-1 Electrical 10/29, VXE-1 Electrical 11-20-12/10, VXE Product Dev & Sup 2024-07, VXE Product Dev & Sup 2024-05, VXE-1 Electrical-7, VXE Prod Dev & Sup 2024-08

## Comments (8)

### Artis Bertulis, 2023-05-12

The centering has been taken apart, but we did manage to find the cables to take them for inspection.
@Cameron Chapman recommended giving those for inspection (without disassembly) to @Laszlo Juhasz , so that’s what I did.

### Cody Smisek, 2023-05-15

@Laszlo Juhasz Can you report your findings here for 371?

### Laszlo Juhasz, 2023-05-15

Good Morning @Cody Smisek , @Artis Bertulis . I’ve checked the cables visually and yes, I’ve seen some discoloring and sign of heated carbon ring. I’m in the process of implementing a high current test platform to be able to quantify the generated heat over a certain time (matching the flight profile). Also, FYI I’ve found three out of about fifty connectors without spring ring from our production inventory, and that is something concerning as far as the reliability goes. Correcting actions been taken care of. 
[embedded: IMG_20230515_092339696.jpg]

[embedded: Missing Spring Ring.jpg]

### Cody Smisek, 2023-05-15

@Laszlo Juhasz Are the corrective actions being tracked in any other Jira Issue? When do we suspect that issue began occurring? Is this field repairable and do we need to implement any directive to add a ring?

### Laszlo Juhasz, 2023-05-15

@Cody Smisek  That is in the hands in the QC dept. and production now. The good news is that, it’s in the battery assembly and not in the plane, therefore   the replacement is more suitable.

### Artis Bertulis, 2023-05-15

Checked the flight asset batteries, all of them have the spring rings on.

### Cody Smisek, 2023-05-15

@Laszlo Juhasz thank you for clarifying that these are the battery connectors not the aircraft side.

### Laszlo Juhasz, 2023-05-15

I’m also testing if the ring springs are changing or not the “springiness” over several temperature cycling (800F°).

## Attachments (11)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| IMG_20230515_092339696.jpg | image | 2051 | 2023-05-15 | listed only |
| Missing Spring Ring.jpg | image | 2444 | 2023-05-15 | listed only |
| 371_230309_111529-supertriclops50lb-takeoff.png | image | 55 | 2023-05-17 | listed only |
| 371_230309_130113-supertriclops50lb-takeoff.png | image | 54 | 2023-05-17 | listed only |
| 371_230314_191845-unknownWeight-takeoff.png | image | 52 | 2023-05-17 | listed only |
| 371_230315_111508_unknownweight-takeoff.png | image | 54 | 2023-05-17 | listed only |
| 371_230323_113725-supertriclops50lb-takeoff.png | image | 55 | 2023-05-17 | listed only |
| 371_230403_084342-140G2-46lb-takeoff.png | image | 50 | 2023-05-17 | listed only |
| 371_230404_095118-140G2-46lb-takeoff.png | image | 49 | 2023-05-17 | listed only |
| 371_230405_090322-140G2-46lb-takeoff.png | image | 51 | 2023-05-17 | listed only |
| 371_230405_133319-140G2-46lb-takeoff.png | image | 53 | 2023-05-17 | listed only |
