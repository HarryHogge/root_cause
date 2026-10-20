# VXEP-2018: Vehicle 401 Descended into the ground after level up command given (A/C 398 AV box)

- **Issue type:** Incident (8D)
- **Status:** D2 - Gathering Information
- **Priority:** Highest
- **Created:** 2026-10-09
- **Updated:** 2026-10-13
- **Reporter:** Zachary Mann
- **Assignee:** David Grosher
- **Creator:** Zachary Mann
- **Labels:** Crash, RCCA, Weekly-incident-tracker
- **Customer:** INL
- **Part Number(s):** 401/398
- **Vehicle Tail Number:** 401
- **Vehicle Configuration:** Standard Battery, VXE Block 30, Hood Payload, Radio Payload (A/C 398 Avionics Box)
- **Incident Type:** Aircraft Loss
- **Severity:** 1 - Flight Critical
- **Components (EA Aircraft):** Aircraft, full assembly

## Description

While operating at 1,500 ft, the aircraft initiated a descent down to 350 ft AGL and subsequently continued descending into the ground approximately 400 m from the GCS. The operator issued a "level up" command, but the aircraft pitched down into a nose dive and impacted the terrain. The aircraft was configured with a full standard hood payload and radio payloads.

Logs appear to be xcl00607 and vtl00279

## Comments (8)

### Zachary Mann, 2026-10-09

@Eric Brewer @Jeremy Kostel @Everett Werner

### Jeremy Kostel, 2026-10-09

[embedded: image-20261009-194437.png]
Quick look at the data, FWD motor did come back on when commanded via the AP

### Alexander Alan Arnold, 2026-10-12

@Everett Werner @Eric Brewer is there a chance we can have a “best guess” or initial theory by the end of the day?

### Eric Brewer, 2026-10-12

@Alexander Alan Arnold @Everett Werner initial look suggests an issue with pitch control.  The vehicle tried to pitch up but couldn’t.  I think the top items to check in this case would be:
1. Was mass/CG within tolerance?
2. Is the elevator functioning properly (can check on the ground if it wasn’t damaged too badly)
3. Inspect pitot system to make sure this wasn’t due to a stall (did not appear to be based upon airspeed/groundspeed measurements)

### Alexander Alan Arnold, 2026-10-13

@Eric Brewer CG was good our gtow was 47.8, elevator was definitely sticking and hard to move when we recovered it but we put on it another tail and did like 50 surface checks on it and couldn’t get it to bind at all it moved normally-from customer

### Eric Brewer, 2026-10-13

@Alexander Alan Arnold thanks - to clarify - you’re saying the elevator in the crash was sticking, and another tail from a different vehicle was not? Or are they saying that they put the crashed tail on a different airplane and it functioned normally?

### Alexander Alan Arnold, 2026-10-13

@Eric Brewer i believe he was saying physically moving the elevator after the crash it was sticking hard. they installed it on a different tail boom and tested it and had no issue. i asked him to test on the crashed tail if possible

### Eric Brewer, 2026-10-13

@Alexander Alan Arnold Got it - a sticking elevator would certainly explain what we saw - but I’d like to understand why that’s happening.

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V398_261009_070400_pack.zip | archive | 5191 | 2026-10-09 | listed only |
| image-20261009-194437.png | image | 178 | 2026-10-09 | listed only |
