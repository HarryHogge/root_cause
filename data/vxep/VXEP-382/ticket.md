# VXEP-382: 100-105620 FAIs received, multiple xREFs, 100-105620 alternates

- **Issue type:** Sub-task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2024-04-29
- **Updated:** 2025-02-17
- **Resolved:** 2025-02-17
- **Reporter:** Catherine Wagner
- **Assignee:** Connor Peebles
- **Creator:** Catherine Wagner
- **Parent:** VXEP-373 Need an approved Substitution for 100-105620

## Description

Vault MFG PN approved: CINCH DCCM21PSB “yellow chromate over cadmium”
Ordered and received: CINCH DCCM21PSBN “Electroless nickel“
- Approve alternate in Vault.
- Approve Supplier ‘OnlineComponents.com’
- Ideally add catalog or datasheet for reference: https://www.belfuse.com/resources/catalogs/cinchconnectivitysolutions/duracon/ca-CSS-DURA-dura-con-catalog.pdf

Components are on FAI shelf in quality inspection - not sure who’s responsible for evaluating these. Part marking and mfg cert appear to indicate these are OEM connectors.
 FYA @Irfan Sultan @Matt Philley @Garrett O'Neill @Cameron Chapman

## Comments (21)

### Cameron Chapman, 2024-04-30

@Garrett O'Neill is the default assignee to either investigate or delegate. See EE Default assignment list.xlsx

### Garrett O'Neill, 2024-04-30

@Matt Philley These parts were approved before purchase. The datacard fields are full, so we put the info in the comment section of the datacard.

### Matt Philley, 2024-04-30

@Garrett O'Neill 
I dont see CINCH DCCM21PSBN in the comments of the data card
EDIT: I pulled latest and now I see it as the vendor C. All good!
[embedded image-20240430-200355.png]
Edit:

[embedded image-20240430-200727.png]

### Matt Philley, 2024-04-30

@Catherine Wagner I think this is resolved with vault updates?

### Catherine Wagner, 2024-05-02

@Matt Philley @Garrett O'Neill Looks good - is it normal to have to force refresh in the vault? I see it now after pulling latest version.

### Catherine Wagner, 2024-05-06

@Irfan Sultan All first articles are at receiving inspection. Could you please put together a cross-functional team meeting to review what we need to check before releasing  them? FYA @Matt Philley @Steve Stack

### Catherine Wagner, 2024-05-06

[embedded file][embedded file]
Datasheets attached with annotations useful for inspection.

### Nina Menon, 2024-05-07

@Matt Philley @Trevor Gronner @Garrett O'Neill Of the 4 alternate connectors that Cat has, 3 are different finishes but the same size (the first 3 listed below) - those are acceptable for production. The Glenair connector (Newark #98AH0737) is not an acceptable alternate, see attached pics. The housing width is smaller so it would not mate properly when Ben N tested it.
[embedded image-20240507-180631.png]
[embedded Image (3).jfif]
[embedded image-20240507-181223.png]

### Matt Philley, 2024-05-07

@Kenneth Weber @Irfan Sultan FYSA not all of the parts ordered for 100-105620 are acceptable. Nina is helping sort them and relay info back to Engineering.

### Irfan Sultan, 2024-05-07

@Matt Philley thanks for the update, awaiting the findings to initiate next steps.

### Irfan Sultan, 2024-05-08

@Nina Menon @Catherine Wagner are you able to round these up and i can request a RMA?

### Catherine Wagner, 2024-05-08

@Irfan Sultan It is the full Newark PO 240423-09, qty 53. To be clear, we received what we ordered and engineering approved as a suitable alternate so this would not be vendor responsibility. FYA @Matt Philley @Nina Menon @Garrett O'Neill @Cameron Chapman

### Irfan Sultan, 2024-05-09

@Catherine Wagner Noted, this part was also NCNR.

### Catherine Wagner, 2024-05-13

100-105620 alternate part qualification failed fit check @Irfan Sultan @Matt Philley @Nina Menon NCR written.

### Catherine Wagner, 2024-05-21

100-105620 alternate part qualification failed fit check @Irfan Sultan @Matt Philley @Nina Menon NCR written

### Catherine Wagner, 2024-05-21

@Garrett O'Neill @Matt Philley Is CINCH DCCM21PSBN “Electroless nickel“ approved to move forward? I don’t see it updated in the Vault.

### Garrett O'Neill, 2024-05-22

@Catherine Wagner DCCM21PSBN is approved

[embedded image-20240522-200736.png]

### Catherine Wagner, 2024-05-24

@Garrett O'Neill Received M83513/01-CC for evaluation. According to Cinch catalog it is equivalent to DCDM21PSB, which has another insulator type. Is this acceptable for 100-105620? I do see it in Vault comments but wanted to confirm.
[embedded image-20240524-175842.png]
[embedded image-20240524-180032.png]

### Garrett O'Neill, 2024-05-24

@Catherine Wagner These should both be acceptable.

### Connor Peebles, 2025-02-17

closing, task was completed by Garret last year

### Connor Peebles, 2025-02-17

closing, task was completed by Garret last year

## Attachments (10)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20240430-200355.png | image | 16 | 2024-04-30 | listed only |
| image-20240430-200727.png | image | 27 | 2024-04-30 | listed only |
| [100-105620 Cinch DCCM21PSB.pdf](attachments/20385_100-105620%20Cinch%20DCCM21PSB.pdf.md) | pdf | 5264 | 2024-05-06 | converted (cut) |
| [100-105620 Glenair MLDM_L-21PSB.pdf](attachments/20387_100-105620%20Glenair%20MLDM_L-21PSB.pdf.md) | pdf | 458 | 2024-05-06 | converted |
| Image (3).jfif | image | 1327 | 2024-05-07 | listed only |
| image-20240507-180631.png | image | 20 | 2024-05-07 | listed only |
| image-20240507-181223.png | image | 11513 | 2024-05-07 | listed only |
| image-20240522-200736.png | image | 84 | 2024-05-22 | listed only |
| image-20240524-175842.png | image | 54 | 2024-05-24 | listed only |
| image-20240524-180032.png | image | 38 | 2024-05-24 | listed only |
