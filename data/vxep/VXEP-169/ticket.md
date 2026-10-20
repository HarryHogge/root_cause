# VXEP-169: Testing gaps for MOD Payload

- **Issue type:** Problem
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Medium
- **Created:** 2023-10-31
- **Updated:** 2025-06-02
- **Resolved:** 2025-06-02
- **Reporter:** Emalee Johnson
- **Assignee:** Kaleb Bellenbaum
- **Creator:** Emalee Johnson
- **Labels:** Production-Priority
- **Links:** relates to VXEP-172 (Cable Tester Documentation and Training); relates to VA-764 (purchase parts required for these adapter cables and coordinate the build, documentation, and test setup); relates to VXEP-423 (Mod Payload support - customer requests & issues)
- **Part Number(s):** 111-105026, 111-105025, 111-104977
- **Production Stakeholder:** Liam Limon
- **Other Stakeholder (as required):** Kelly J Furlong
- **Problem Type:** Production Issue

## Description

Ground Maintenance Harness (111-105026): no cable testing at the lower level, impossible to test at the highest level without cutting cable ties and breaking the previous quality checks from final assembly. 
MOD Payload Harness (111-105025): Does not get tested at the lower level 
This cable document seems done. Is that correct @Emalee Johnson @Ben Norris ? See 111-105025 MOD Payload Harness Cable Test Pinout.xlsx on the vault. 
MAIM Harness (111-104977): Does not get tested at the lower level
Only thing that is tested is at the end: MAIM Board, MAIM Harness, AHRS & GPS at the assembly level.

Steps: 
- Identify mating connectors and backshell/boots for the cables above.
- Create pinout and BOM for each cable to connect connector to cable tester boards.
- See examples listed here https://jenaero.atlassian.net/browse/VXEP-172
- Test files located here. C:\JAI Vault 1\Projects\124 - Test Equipment\Production\Electronics Shop. Please make an actual BOM with mfr PNs on a separate tab of this document (rather than using general description)
- Handoff to production for purchases and builds.
- Create summary of all locations involved, how to design new test cables and boards, etc. (check existing production procedures).

Protoboard, 1mm pitched: 8020 Vector Electronics | Prototyping, Fabrication Products | DigiKey

## Plan

Engineering to provide pinout and BOM for all cables for now. Hope to hire test engineer for this in the future. @Cameron Chapman Adrian will work on this starting 2/2.

## Issue Status

Status date: 2/10
Ground Maintenance Harness Cable Tester and Maim Cable Tester BOM and Pinout can be found here: 
C:\JAI Vault 1\Projects\124 - Test Equipment\Electrical Design\Wire Harness\124-116259 Ground Maintenance Harness Cable Tester
C:\JAI Vault 1\Projects\124 - Test Equipment\Electrical Design\Wire Harness\124-116274  Maim Harness Cable Tester
Status date: 2/12
BOMs for MOD Payload Harness made and can be found here: 
 C:\JAI Vault 1\Projects\124 - Test Equipment\Electrical Design\Wire Harness\MOD Payload Harness Cable Tester
BOM is incomplete because mating connectors have not been assigned yet. Will look into that
Status date: 2/13
Added manufacturing part numbers to the BOMs since those parts do not have an internal number yet. Completed all BOMs and pinouts and can be found here:

C:\JAI Vault 1\Projects\124 - Test Equipment\Electrical Design\Wire Harness\124-116259 Ground Maintenance Harness Cable Tester

C:\JAI Vault 1\Projects\124 - Test Equipment\Electrical Design\Wire Harness\MOD Payload Harness Cable Tester

C:\JAI Vault 1\Projects\124 - Test Equipment\Electrical Design\Wire Harness\124-116274  Maim Harness Cable Tester

Status Date 2/19: 
Was going to add internal part numbers to new mating connectors however my solidworks/vault is not creating the document number and is under investigation by IT
Status Update 2/20:
Mating connectors are in the vault and BOM is updated. @Cameron Chapman @Emalee Johnson ready for review

## Comments (15)

### Emalee Johnson, 2023-10-31

@Desiray Johnston @Liam Limon @Trevor Gronner @Ben Norris FYI

### Cameron Chapman, 2023-10-31

@Garrett O'Neill did you work on these tests before? May have been @Hayden Jeanor. Please link applicable Jira tasks if they exist. 

It seems like the best way to test these would be create adapters and cables for the cable tester. @Ben Norris , @Emalee Johnson, @Ryan Ferguson, who is leading that process currently?

### Ben Norris, 2023-10-31

I’m still the leading support on cable tester testing and troubleshooting. If we have all the connectors I can have a tech build the adapters and I can make and verify the tests. If there are board only adapters we need we can either solder leads directly to the pcb leads or we can design an adapter board.

### Emalee Johnson, 2023-10-31

@Cameron Chapman Agreed, the cable tester will likely be the quickest way to test and as @Ben Norris mentioned we can coordinate production to support building the testing cables.

### Cameron Chapman, 2023-10-31

@Ben Norris and @Emalee Johnson are you able to identify and purchase the mating connectors, or would you like @Garrett O'Neill to support that? 
I think we were tracking mating connectors and cables in the files here C:\JAI Vault 1\Projects\124 - Test Equipment\Electrical Design\PCB see linked project.

### Hayden Jeanor, 2023-11-01

@Cameron Chapman i haven't worked on these cables before, just a heads up

### Emalee Johnson, 2023-11-01

@Cameron Chapman I can help procure the items that you guys need for the build but I think engineering needs to be designing and identifying the test equipment required as well as creating any associated documentation.

### Cameron Chapman, 2023-11-01

The cable tester operation and documentation was handed off to production in January. Documented here https://jenaero.atlassian.net/browse/ENGPRJ-243 . @Trevor Gronner are you ok for your group to continue owning this, or would you like design engineering to help with things like purchasing mating connectors?

### Trevor Gronner, 2023-11-02

@Cameron Chapman Production Engineering will still need support from design engineering in identifying parts/design for testing equipment. When I look at https://jenaero.atlassian.net/browse/ENGPRJ-243 it looks like the parts that were handed off to production were the parts after the actual design was completed (in other words building/purchasing the fully designed test equipment and implementing the equipment in production). From my limited understanding of this issue, the necessary design work for the test equipment on these parts was never completed. Please let me know if I am misunderstanding these two Jira tickets. Thanks!

### Cameron Chapman, 2023-11-02

@Trevor Gronner, We thought it was a full, but it looks like we should have specified who would select parts for new adapters. We can help with that. @Garrett O'Neill,  can you please purchase parts required for these adapter cables and coordinate the build, documentation, and test setup? Thank you.

### Cameron Chapman, 2023-12-07

@Garrett O'Neill can you please prioritize this soon? Either developing a test and pinouts for those cables, or handing off the whole process for others to pick up. We do not want to ship untested cables. Kurt developed a cable tester for the mod payload harness. We might be able to use the parts from that. 
@Emalee Johnson , in the mean time, can we manually perform continuity and isolation measurements or functional tests?

### Garrett O'Neill, 2023-12-07

@Ben Norris Would someone in Electronics have time to pick this up? I currently don’t have bandwidth to work on this. I put a link to a protoboard in the description. I would recommend buying a board like this and soldering the mating Picoclasp/Microclasp connectors to it (in place of a customized adapter PCB). You can use that to create a test setup for all 3 cables per the normal process.

### Adrian Garcia, 2024-02-08

Finished pinout for Ground Maintenance Harness (111-105026) and MAIM Harness (111-104977). Still need to work on BOM. Half of BOM is complete just need to verify some stuff. @Cameron Chapman @Emalee Johnson do you want the BOM and Pin out all in the same file or separate files for them?

### Cameron Chapman, 2024-02-09

@Adrian Garcia please separate BOM and pinouts.

### Cameron Chapman, 2024-07-25

@Adrian Garcia were these ever built? If not, @Kaleb Bellenbaum this would be a good candidate for a test PCB after the MAGNSS ones.

## Attachments (0)
