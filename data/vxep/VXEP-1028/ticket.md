# VXEP-1028: Updates needed for the 116-106838 Battery Charger Power Supply drawing

- **Issue type:** Problem
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Medium
- **Created:** 2024-02-01
- **Updated:** 2026-03-30
- **Resolved:** 2026-03-30
- **Reporter:** Liam Limon
- **Assignee:** Greg Fryer
- **Creator:** Liam Limon
- **Labels:** Electronics_Drafting
- **Issue color:** purple
- **Sprint:** EE Drafting
- **Production Stakeholder:** Ben Norris
- **Other Stakeholder (as required):** Ryan Ferguson

## Description

On the Battery Charger Power Supply PN: 116-106838 there are a couple of issues with the drawing that we have identified. 
The first and largest is that there is a note referencing the production documentation for the instructions for how to process the assembly. This has resulted in a new process being introduced for quality to inspect the board after disassembling the supply, and then identify any solder joints that need rework and return to the tech to rework. This process is not identified anywhere on the drawing and depending on the components and joints that are being called out it is resulting in damage to parts on the board. We also do not train our techs in re-working lead free solder and since lead free solder is used a whole process would need to be developed and provided by engineering for reworking lead free joints and re-alloying them with our leaded solder. There is a good chance that all rework that has been performed on these power supplies up to this point has not been done with the proper training for using lead free solder.
There is also a flag note on the drawing, note 6, that is just a list of part numbers and the flag doesn’t reference anything on the drawing. 
Any pertinent information that is contained within the procedure needs to be pulled from the procedure and included on the drawing so that quality has an engineering document to refer to for creating their inspection sheets.

## Comments (5)

### Catherine Wagner, 2024-04-25

@Greg Fryer There are two REV E pdfs accessible in the Vault with different approval dates at minimum. I am not sure what other differences there are. FYA @Liam Limon @Ben Norris @Brad Crampton @Matt Philley @Sloan Payne 
[embedded image-20240425-173158.png]

[embedded image-20240425-173343.png]

### Greg Fryer, 2024-04-25

@Garrett O'Neill It looks like you made the fully-named file. Can you deconflict between the two PDFs and get whichever one is un-needed removed? Scott S. or I could likely do it.
Other improvements on this ticket will wait (unfortunately).

### Garrett O'Neill, 2024-04-25

@Greg Fryer @Scott Stuckey I marked the wrong one obsolete.

### Catherine Wagner, 2024-05-08

@Garrett O'Neill Is the correct one active now or does this still need update?

[embedded image-20240508-163841.png]

### Garrett O'Neill, 2024-05-08

@Catherine Wagner Ignore the obsolete PDFs, only reference the one in a “shared” state.

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [116-106838-E.PDF](attachments/18576_116-106838-E.PDF.md) | pdf | 64 | 2024-02-01 | converted |
| image-20240425-173158.png | image | 74 | 2024-04-25 | listed only |
| image-20240425-173343.png | image | 111 | 2024-04-25 | listed only |
| image-20240508-163841.png | image | 45 | 2024-05-08 | listed only |
