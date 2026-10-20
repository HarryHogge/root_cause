# VXEP-880: MAIM v4 Software Release

- **Issue type:** Task
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** High
- **Created:** 2025-01-07
- **Updated:** 2026-03-30
- **Resolved:** 2026-03-30
- **Reporter:** Kurt Burian
- **Assignee:** Kurt Burian
- **Creator:** Kurt Burian
- **Parent:** VXEP-829 Create new software for Advanced Navigation MOD Payload A-Kit
- **Epic Link:** VXEP-829
- **Job Number:** J100132 - VXE Advanced GPS Follow On

## Description

- Migrating from SBG Systems Eclipse AHRS to MAGNUSS will allow navigation in GPS denied environments.​
- MAIM Firmware will need a firmware update to translate MAGNUSS messages to MOD PAYLOAD formatted messages​
- MAGNUSS will need to know the address of the MAIM board. Currently this is hardcoded on the individual MAIM board. We may want to change this behavior to a DHCP-like model where the board autodetects the tail number and assigns itself an expected IP, for example 10.*.*.12. This would still allow the payload port to be assigned the correct address with the MAIM on the same network segment.
- MAGNUSS should ping for the existence of a MAIM board associated with the fuselage. If found state data should be forwarded to MAIM network port.

[embedded file]


Requirements: Advanced Navigation for MOD Payload Kit Requirments.xlsx

## Comments (6)

### Tobi Ogunro, 2025-01-09

@Kurt Burian Please confirm if you have all the task listed here in the software requirements reflected via the Jira task. Advanced Navigation for MOD Payload Kit Requirments.xlsx

### Tobi Ogunro, 2025-01-13

Hey @Kurt Burian @Eric Brewer which subtasks are associated with what is specified in the attached Requirement sheet? Advanced Navigation for MOD Payload Kit Requirments.xlsx

### Eric Brewer, 2025-01-14

@Tobi Ogunro 
#2-> 881
#4-> 890
#1 ->883
#3,7,8 ->882.  I added a note about 7 and 8 into 882 so it isn't missed.
@Kurt Burian FYI.

### Scott Whitney, 2025-02-12

@Kurt Burian  - when do you expect we will get this over to Brandon and Ryan for testing? I want to make sure we have time allocated for them

### Kurt Burian, 2025-02-13

@Scott Whitney Mid week for Brandon and Ryan. The speedgoat testing I’m performing will be the bulk of the testing, I will be comparing simulated output to MAIM output. Brandon and Ryan currently make sure the button presses still work, but none-of that code of changing. I can provide them with a new test case and instructions so they can perform the same data validation going forward, but I need to do this work myself first. Planning on doing this myself by end of day Monday, getting a PR out, and starting a test procedure at that point.

### Kurt Burian, 2025-02-14

Made some additional progress on MAIM firmware debugging last night. Heading in this afternoon to run a sim mission on the speedgoat and get a data capture for validation. Additionally, I managed to get the firmware working in such a way that it autodetects if a red AHRS is present, if not changes to MAGNUSS mode and starts network negotiation. 
 
I will be putting together a few new test cases for software Q/A and get a Pull Request(peer review) out for next week. 
 
Time permitting today, I want to check the status of 2 features out of scope for this effort, but mentioned in the spec. The MAIM should echo a copy of the network state data over the payload serial port. This did not seem to be implemented. Additionally the MAIM+GUI is designed to support a serial-to-ethernet bridge. We have never tested or documented this. I'd like to plan on it for a future release, but it would be nice to at least know the state of it. I can direct solder to the board to accomplish this, but if someone in production had the time to create a 'development' cable for me, this would be easier.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [Existing MOD PAYLOAD PVT Messaging.pptx](attachments/25356_Existing%20MOD%20PAYLOAD%20PVT%20Messaging.pptx.md) | pptx | 72 | 2025-01-10 | converted |
