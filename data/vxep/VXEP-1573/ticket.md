# VXEP-1573: Provide summary of all ADC changes from B30 to Xkit to B40 to Scott H, then audit code changes required

- **Issue type:** Epic
- **Status:** In Process
- **Priority:** Low
- **Created:** 2025-10-29
- **Updated:** 2025-11-25
- **Reporter:** Cameron Chapman
- **Assignee:** Scott Hunter
- **Creator:** Cameron Chapman
- **Parent:** VXEP-1512 SB40 Software (Release 6.7.0)
- **Links:** relates to VXEP-1512 (SB40 Software (Release 6.7.0))
- **Plan:** Assigning to Scott to see if more information is needed/helpful

## Description

B40 to 30 DIO+ADC Summary.xlsx

## Comments (2)

### Jeremy Kostel, 2025-11-19

[embedded: image-20251119-183732.png]
FYSA @Cameron Chapman 
Needs more formalized documentation when time is provided. Screenshot directly from conversation with Scott H

Short Summary:
B30 has direct A/D values providing both voltage and current measurements from the main battery - neither of these exist in B40 anymore. No other analog values of significance are populated on any platform (see connector J24 - DNP on all platforms). B40 sees only the A/D reading of 28V DCDC voltage and no current.

### Cameron Chapman, 2025-11-21

thanks for the link. Do you have the softcopy of that table I could expand on? 
seems like that might just be XCOM, but there are changes to VTOL AP A/D as well

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20251119-183732.png | image | 281 | 2025-11-19 | listed only |
