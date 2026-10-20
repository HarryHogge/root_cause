# VXEP-635: Drop payload PCB. Gather PCB files, firmware, and other relevant documentation to send to treetown for RFQ

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-09-16
- **Updated:** 2025-05-27
- **Resolved:** 2025-02-05
- **Reporter:** Cameron Chapman
- **Assignee:** Gary Angelus
- **Creator:** Cameron Chapman
- **Parent:** VXEP-523 Old. B40 Wing Utility Dropper Requirements/Scope
- **Epic Link:** VXEP-523
- **Job Number:** J100130 - VXE Fuel Cell & Heavy Fuel Development

## Comments (10)

### Cameron Chapman, 2024-09-16

@Gary Angelus are you available to start this today or this week?

### Gary Angelus, 2024-09-16

Will work on this.

### Gary Angelus, 2024-09-16

@Cameron Chapman  who can I collaborate with to get the doc numbers or project files?

### Cameron Chapman, 2024-09-16

@Gary Angelus see https://jenaero.atlassian.net/browse/ENG-2174 . Probably Connor and John Clark.

### Gary Angelus, 2024-09-20

@John Clark I'm compiling data files for a RFQ with TreeTown for the redesign of the Drop Payload circuit card.  Can you provide files for the firmware associated with the design?  Thanks.

### Cameron Chapman, 2024-09-23

found firmware 
**How to program 0716P01 Dropper PCB**

- Install MPLAB X IPE v5.20.

Note that we tried to install the latest version (v6.2) but had difficulties programming the device so se reverted to v5.20 that worked.
- Connect PC to MPLAB PICkit5 programmer
- Connect 5V to the 0716P01 PCB
- Connect the programming header to J3
- Run MPLAB X IPE v5.20
- Select Tool and Connect
- Load Hex file ESD11drop.hex from \\condor\production\archives\dropPayload
- Click “Program”
- Once the board is programmed, you should see a red LED flash.

### Gary Angelus, 2024-09-25

@Rajesh Budhabhatti  FOR YOU

### Rajesh Budhabhatti, 2024-09-25

@Cameron Chapman Here is the list of changes. I also have redlines for drafting. Let me know when you have time to review and decide on the connector. Drop PCB Re-spin component change list.docx
Thank you

### Cameron Chapman, 2024-09-25

@Rajesh Budhabhatti please drop redlines on my desk before drafting. I will review tomorrow

### Gary Angelus, 2024-12-23

12/20 sent Treetown files to Sierra Circuit for fab and assembly.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [0716P01 Drop Payload.pdf](attachments/23162_0716P01%20Drop%20Payload.pdf.md) | pdf | 37 | 2024-09-17 | converted |
| [Drop Payload CCA.pdf](attachments/23176_Drop%20Payload%20CCA.pdf.md) | pdf | 197 | 2024-09-17 | converted |
| [DropPayLoad Brd OL.pdf](attachments/23163_DropPayLoad%20Brd%20OL.pdf.md) | pdf | 1187 | 2024-09-17 | converted |
