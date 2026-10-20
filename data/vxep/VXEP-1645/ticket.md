# VXEP-1645: VXE 880 Failing to Connect in OGCS but can connect via SSH

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** High
- **Created:** 2025-12-15
- **Updated:** 2026-02-18
- **Resolved:** 2026-02-18
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Alan Burnsworth
- **Creator:** Alexander Alan Arnold
- **Labels:** Weekly-incident-tracker
- **Vehicle Tail Number:** VXE 880
- **Vehicle Configuration:** ADV NAV, standard battery, e140G2Z
- **Severity:** 1 - Flight Critical

## Description

We have an aircraft being used for training VXE 880, ADV NAV with OGCS enabled.  The aircraft was preforming fine Thursday, Friday and most of today. Now they are unable to connect in OGCS but are able to connect via SSH. They have tried power cycling, sending commands via SSH, and verified date time but are unable to use OGCS.
The sign in failure message displayed "bad gateway". They also received a "No Space left on device" message in the cmd prompt when trying to start CUCS. 

Quick status:  no root cause found yet.  I spent a little time with Jackson performing triage and the SSD appears to be healthy and the file system does not appear to be corrupt, but I can’t find the source of the file system being full.- Craig B

## Comments (4)

### Alan Burnsworth, 2025-12-16

### Diagnosing the issue:

I ran the following command to check the allocated disk space for the “/” partition labeled “APP”.
sudo parted -l

The output of that command stated the following:
Warning: Not all of the space available to /dev/nvme0n1 appears to be used, you
can fix the GPT to use all of the space (an extra 6 blocks) or continue with the
current setting?
Fix/Ignore?

So, I did a "Fix" to repair it.
Afterwards the command gave me the expected output of all drives and partitions.
After analysis of the output, I determined the “APP” partition size looked correct, as seen below.
1      954MB   1000GB  999GB   ext4         APP                        msftdata

I then ran the following command to see the mounted partition size of “/” (aka “APP”).
sudo df -h /

The output of that command showed roughly half of the allocated partition space was being used, as seen below.
/dev/nvme0n1p1    422G  404G  161M 100% /


### Fixing the issue: 

To resize the “APP” partition so that it utilizes the full allotted space, run the following command using the device path as seen in the previous “df”. 
sudo resize2fs /dev/nvme0n1p1

Afterwards, run the following command to verify the partition size has been expanded.
sudo df -h /

The output should reflect roughly the size stated from the “parted” command.
/dev/nvme0n1p1    916G  404G  475G  46% /

If correct, then reboot the MCM so everything comes up properly. This can be performed by power cycling the aircraft or running the following command:
sudo reboot

### Alan Burnsworth, 2025-12-16

NOTE: This issue has been seen before with the “Edge” partition on MCM’s coming out of Production. This is the first time I have seen it happen to the “APP” partition.
Tagging POI: @Jo Brown @Bethany Ponce @Craig Burton

### Bethany Ponce, 2025-12-16

@Alan Burnsworth thank you for the clear instruction and reference!

### Scott Lovett, 2026-02-18

Fixed

## Attachments (0)
