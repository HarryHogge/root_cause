# SS5 Transition Release Notes.pdf

Attachment 17504, pdf, 77 KB, added 2023-11-08 by Matt Philley.

## Page 1

SS5 Transition 
 
 
Changelog vs SS4 (4.0.3.15): 
New Features / Changes: 
1. [MAN-PC, MAN-PW, Explicit Beamforming] Initial Release. 
2. [FIPS] Support for FIPS-140-3 validation. Additional steps are needed to fully transition a 
radio to FIPS 140-3 approved mode. Please see below for more details. 
3. [MAN-IA] Added ability to add bias to MAN-IA frequencies. 
4. [Aggregation Delay] Added support for per-QoS aggregation delay. This helps with 
reducing airtime when traffic has lots of small packets. 
5. [GUI] Upgraded to Jquery v3.6.3. 
6. [NodeID] NodeID is now a 20-bit identifier. Please see below for transition details. 
7. [GPS] 1. Now supports 57600 input serial baud rate. 2. GPS saved coordinates now 
reset to 0,0,0 upon Factory Reset. 
8. [PHY] Added option code 43. 
 
Bug Fixes: 
1. [GUI-Advanced] Bug fix: setting Routing Beacon Period to Auto would cause Apply/Save 
and Apply to stop working. 
2. [Save] Bug fix: Excessive save could cause the radio to brick. 
3. [Spectrum Scan] Bug fix: Fix time sync / hanging issues causing spectrum scan failures. 
4. [DLEP] Bug fix: DLEP was broken in previous releases, would not work after vlan 
settings change. 
5. [MPS] Bug fixes: Miscellaneous GUI fixes. 
6. [Translations] Bug fixes: Updated all text to now show correct translations. 
7. [GUI] Bug fixes: Topology focus issue and other miscellaneous fixes. 
8. [IGMP] Bug fix: Wired backbone radios would cause all radios on the network to send 
multicast data to them due to querier. 
9. [Upgrade] Bug fix: Upgrade over multiple hops in a congested network could fail. 
10. [Spectrum Scan, Frequency Change, Beamforming] Bug fix: Changing any of these 
settings could cause the radio to lockup/reboot. 
11. [Factory Reset] Bug fix: enc_hmac_key and enc_wrap_key were being reset during 
factory reset. 
12. [Security] Important Security Updates

## Page 2

13. [MANET Multicast] Bug fix: low data rate multicast will cause receivers to get duplicate 
packets. 
 
Compatibility 
 
SS4.0.x.x will not talk to 5.0.0.0 over RF or wired/wan backbones. This is due to the addition of 
the following new features: 
a. MAN-PW 
b. MAN-PC 
c. Explicit Beamforming 
d. FIPS 140-3 support. 
 
IP / MAC Range 
172.16.0.0 - 172.32.255.254 
255.240.0.0 
C4:7C:8D:A0:00:00 - C4:7c:8D:AF:FF:FF 
Transitioning from firmware < 5.0.0.0 
 
If FIPS mode is turned off, the radios may be upgraded directly. However, note the following: 
 
1. Configurable settings (e.g. Frequency) are stored in a different way in 5.0.0.0 and up. 
The first time a radio is upgraded to 5.0.0.0, these settings will be safely transferred to 
the new format. However, if the radio is downgraded again to a lower firmware version, 
the settings will not be transferred and will revert to what they were before the upgrade 
to 5.0.0.0. 
2. If https is turned on, only TLS v1.3 is supported. This may impact systems where 
browsers are not allowed to be upgraded. Any browser pre 2018 will not support the 
Web GUI. 
3. When a radio is upgraded on the Firmware Upgrade page, the radio will automatically 
reboot. There is no need to click on Reboot. 
4. There is a new FIPs compatible encryption option "Static GCM 256-bit" that is more 
suitable for dense networks like IVAS. This option uses static GCM keys which have less 
overhead than the “GCM ECDH” option. The downside is that unlike the ECDH option, 
the encryption keys are not negotiated on a per-neighbor basis, so it is less secure. 
5. The Large Network Routing is the only option for 5.0.0.0. Radios on legacy routing will 
automatically switch to Large Network Routing. 
6. The node ids have transitioned from a 16-bit to a 20-bit value. This affects the following 
API which take node id as a parameter or return node ids:

## Page 3

a. nbr_mcs 
b. nbr_mcs_rx 
c. nbr_rssi 
d. routing_path 
e. ptt_hq_link_notifications 
f. white_list 
g. black_list 
h. link_stats_total_air_time 
i. link_stats_total_rate 
j. link_stats_total_loss 
k. link_stats_var_gi_mode 
l. link_stats_var_gi_cyc_pre_len 
m. Link_stats_mcs 
If the node id is <= 65535, it is automatically upgraded to a 20-bit node id in the following 
way: 
New serial number = Original serial number + 4 * 65536. 
If the node id is > 65535, it is used as is. 
 
 
 
 
If FIPS mode is turned on, the radios may be upgraded, but the user must follow the steps in the 
next section to put the radio in full FIPS 140-3 compliance. 
FIPS Mode 
SS5 adds support for FIPS 140-3 Level 2. Note that the certificate is still under review by NIST, 
and is expected to be complete in a year from now. 
 
Below are the main changes from FIPS 140-2 Level 2  (firmware >= 3.16.0.0 and < 5.0.0.0): 
1. SSH needs to be disabled. 
2. API Logging needs to be enabled. 
3. SNMP needs to be disabled. 
4. Passwords need to be at least 8 characters long, and Password Complexity needs to be 
turned on. 
5. The Web Server now only supports TLS v1.3 
6. Encryption needs to be turned on with Profile set to AES GCM Static, or AES GCM 
ECDH. The AES GCM Static option is new for 140-3. 
7. All security settings need to be set to non-default values. Note that this was a policy 
requirement (not enforced by firmware) for FIPS 140-2, but it is now enforced by the 
firmware as required by FIPS 140-3. The below list include the settings: 
a. Passwords (all users). 
b. API Key 
c. Encryption keys - RF Bcast / Static Key, RF Unicast Key

## Page 4

d. TLS Host Key 
 
 
 
Transitioning from 4.0.x.x when FIPS is enabled on a radio: 
 
1. Upgrade to 5.0.0.0. 
2. When the radio powers back up, it will be in “Transitional FIPS” mode. In this mode, all 
features will be operational, but the GUI will show the FIPS indicator on the right 
information pane to be Amber. Some settings need to be correctly configured for the 
radio to be fully FIPS compliant. See the settings list above. 
3. The GUI will present a consolidated list of the above settings. Once all the settings are 
correctly configured, the FIPS indicator on the right information pane will show green, 
which indicates that the radio is now fully FIPS 140-3 compliant.
