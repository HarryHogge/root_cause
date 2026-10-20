# VLAN Tagging Payload Issues.docx

Attachment 63355, docx, 513 KB, added 2026-07-08 by Alexander Alan Arnold.

When VLAN Tagging was enabled on 462 (normal VXE30) running 6.6.1 the UDP multicast traffic was not reaching the CRP2. When 462 was reverted to 6.5.1 the CRP2 functioned as expected even while VLAN Tagging was left on

The CRP2 functioned as intended on both 464 (MCM Bird) and 910 (AdvNav) on 6.6.1 while VLAN Tagging was enabled

When checking the Throughput tab in XComm, traffic to the payload for 462 was being passed through the port labeled “Switch 2, Port 1, xponder”. UDP multicast traffic would not go through that port when VLAN Tagging is enabled on 6.6.1 but http/https traffic would. This allowed us to load the GUI but not actually use the payload

Enabling/Disabling VLAN Tagging required a power-cycle of the AV even after clicking save & update configuration

VLAN Toggle in Configuration page on EXcomm

Traffic to Payload on 462 (while working)

Traffic to Payload on 464/910
