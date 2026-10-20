# VXEP-1316: B30 Advanced Nav Fuel Cell Configuration over MGTOW

- **Issue type:** Problem
- **Status:** New
- **Priority:** High
- **Created:** 2025-06-27
- **Updated:** 2025-06-27
- **Reporter:** Cameron Chapman
- **Assignee:** Artis Bertulis
- **Creator:** Cameron Chapman
- **Issue color:** purple

## Description

Gathering info after Artis mentioned this in ADP FRR

## Plan

- Asked Artis. I'd like to follow up and resolve the comment you made in the FRR about the fuel cell config being overweight. Are you able to summarize in this chat or this JIRA? https://jenaero.atlassian.net/browse/VXEP-1316
- Review fuel cell weigh limits in manual.
- Update confluence page.

## Comments (1)

### Artis Bertulis, 2025-06-27

During attempted endurance testing with a VXE30 ADV NAV vehicle (Tail #757), with a Fuel Cell configuration and simulated Octopus E140 MWIR weight, we discovered that the vehicle weight was significantly over what the Fuel Cell operational supplement indicates as “MAX TOW”.
Should be 44.5 lb / Was 46.4 lb, see pictures below:
[embedded image-20250627-201011.png]
VXE-OS-23-012 Fuel Cell Operation and Maintenance Supplement Rev 1.1
[embedded image-20250627-201029.png]
Measured weight of 797 with an E140MWIR mass sim (the scale was zeroed with empty vehicle stand on it)
MTOW of 46.4 did not raise a safety concern as the same vehicle in battery configuration takes off at 49lb, hovewer, this does raise a concern on maintaining a level flight as we’re unsure if FC can produce enough power to compensate for a level flight at this weight. And if it can, how impacted would the endurance be?

For more details on the payload:
To achieve a simulated E140 MWIR weight, we attached weights to a regular E140 gimbal to bring its weight up to the reported weight of measuring an actual E140 MWIR that was located in HSV at the time (5 lbs 6.6 oz or 86.6 oz fully assembled with mount plate, cable, and GPS). Here was the total payload weight before installing it into the vehicle #797.
[embedded image-20250627-201843.png]
@Cameron Chapman for awareness

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20250627-201011.png | image | 16 | 2025-06-27 | listed only |
| image-20250627-201029.png | image | 2337 | 2025-06-27 | listed only |
| image-20250627-201843.png | image | 16678 | 2025-06-27 | listed only |
