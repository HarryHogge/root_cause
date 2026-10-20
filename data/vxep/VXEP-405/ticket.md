# VXEP-405: VTOL autopilots and X-comms fail to generate full length crypto keys

- **Issue type:** Bug
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2024-05-07
- **Updated:** 2025-10-06
- **Resolved:** 2025-10-06
- **Reporter:** Ryan Ferguson
- **Assignee:** David Grosher
- **Creator:** Ryan Ferguson
- **Labels:** Production, Rate#
- **Links:** relates to FS2-1832 (VTOL AP failure to generate full-length crypto keys); relates to FS2-1831 (VTOL autopilots and X-comms fail to generate full length crypto keys); relates to FS2-1835 (X-comms fail to generate full length crypto keys); relates to ENG-2521 (TAS Release 2.0)
- **Issue color:** purple
- **Part Number(s):** 1409P01D 1607P01A
- **Impacted Disciplines:** Software

## Description

In Production, one leading cause of VTOL autopilot rejection is what is commonly referred to as ‘fs_crypto_keys’.  This name comes from the TAS database record of the SD card crypto keys.  When the AP Judge determines if an autopilot is acceptable, it checks to make sure the autopilot has crypto keys that are at least 87 characters long.  If an autopilot does not have crypto keys present in the VTEV log or the keys do not add up to the minimum length, the Judge will reject the autopilot.  After 75 days of operation of the TAS, this failure has been responsible for 11 of the 38 autopilot rejections that occurred during this period.  This hints to an 11.7% failure rate caused by this issue.

Software has not been able to provide clear instruction on what the minimum length of the keys should be.  87 was chosen during TAS development because it aligns with a full 32 bit crypto key.  See below for an example key
```
0x686e959c 0x6a639cbe 0x63419791 0xaa55aa55 0xaa55aa55 0xaa55aa55 0x6e68be9c 0x7e696cbb
```
Passing key.  Total length is 87 characters long

```
0x686e959c 0x6a63f7ea 0x8159791 0xaa55aa55 0xaa55aa55 0xaa55aa55 0x6e68eaf7 0x7e69f708
```
Failing key.  Total length is 86 characters long

```
0x696e959c 0x6a636932 0xaa55aa55 0x6e693269 0x7e693813
```
Failing key.  Autopilot did not save all of the crypto keys to the VTEV log.

Based on the above, it seems multiple issues are driving this failure mode.
- Autopilots are not generating crypto keys properly, resulting in keys not meeting the minimum length requirement.
- The autopilot only writes the crypto key to the VTEV log once.  If something interrupts this write cycle, the key is never written again to the log.


The second failure mode can be easily fixed by making the autopilot write the crypto key to the VTEV log at every boot.  This will not affect security as it already writes the full key to the log which is kept on the vehicle until wiped.
The first failure mode is more difficult and will require a code review to figure out what is causing the failure.  Several security concerns are also raised by this mode as the autopilots almost always have 3 of the 8 keys identical.

The request for the software team is to implement fixes for the second failure mode at a minimum.  This should be a very low hour count request.  A separate ticket will be made to address the first failure mode.

## Comments (6)

### David Grosher, 2024-05-07

@Scott Whitney FYSA

### Kurt Burian, 2024-05-08

Problem seems to be with sprintf formatting in the log. We should make a ticket to address down the road, but for now we can fix this procedurally by padding leading zeros in the first 3 rows to make the sprints 8 hex digits long plus leading '0x'. If we want to be extra cautious validation can be performed on the first 16 bytes by the below psudocode:
for(0;i<6;i++){
    if(XOR(key[i],0xFF) != key[i+6])
        FAIL(“Bad Key Validation”)
}

### Ryan Ferguson, 2024-05-08

[embedded file]
I wrote the above script to convert the MAC address to a crypto key, minus the last two lines.  This will be used to disposition NCRs against the autopilots and X-comms which have a missing character in their crypto keys.  It uses the pseudocode provided by @Kurt Burian to generate the key without any padded zeros the way the autopilot will report them.

If an autopilot has a line with a missing character in its crypto key, use this Python script to generate a correct crypto key.  Pad leading zeros to the first 3 rows to make them meet the minimum length requirement of 8 characters per line, excluding the leading ‘0x’ portion.  If the first 5 lines from the padded autopilot crypto key match the result of the above script, the autopilot can be UAI’d assuming no other failures are present.

Note that due to the sensitive nature of this script, caution should be taken to ensure this script does not leave the company.

### Ryan Ferguson, 2024-05-24

AP Judge Release 2.0 added functionality related to the below MAC to crypto key script.  It allows the Judge to recalculate the crypto key off the MAC address and compare the calculated key to the recorded key from the AP.  If the results are comparable, the Judge overrides the result of that check and allows the autopilot to pass per this Jira ticket even though the key is short.  This essentially allows the script to UAI an autopilot for this specific issue.  

Note that this fix does not address the security concerns raised by this ticket and https://jenaero.atlassian.net/browse/VXEP-406.  It only allows Production to continue processing autopilots without being held up by these failures and writing NCRs that will get UAI’d for this issue.  It also does not fix the fact the autopilots are generating short crypto keys.  That issue has to my knowledge been addressed by@Kurt Burianfor a future update.

### Christa Meck, 2025-09-25

@David Grosher This has been around for over a year now.  Did we fix or obsolete this problem ?

### David Grosher, 2025-10-06

@Christa Meck We don’t use the VXEP project to track bugs in the SW/FW. So this has languished. This was just an issue in printing the key on generation. It has been fixed and this can be closed.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [MAC to crypto key.py](attachments/20428_MAC%20to%20crypto%20key.py.md) | text | 3 | 2024-05-08 | converted |
