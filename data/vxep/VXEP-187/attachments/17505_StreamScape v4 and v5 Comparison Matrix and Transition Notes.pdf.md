# StreamScape v4 and v5 Comparison Matrix and Transition Notes.pdf

Attachment 17505, pdf, 146 KB, added 2023-11-08 by Matt Philley.

## Page 1

StreamScape v4 and v5 Comparison Matrix and Transition Notes 
October 2023 
 
  SS4 (v4.0.3.X and below) SS4 Interim (v4.0.4.X) SS5 (v5.0.0.0 and up) 
IP Range 
172.20.0.1 - 
172.20.255.254 
172.16.0.1 - 
172.31.255.254 
172.16.0.1 - 
172.31.255.254 
Subnet Mask 255.255.0.0 255.240.0.0 255.240.0.0 
If shipped, can 
update to SS4? Yes No No 
If shipped, can 
update to SS4 
interim? Yes Yes Yes 
If shipped, can 
update to SS5? Yes Yes Yes 
Ability to change IP 
address No Yes No 
Mesh with SS4 Yes Yes No 
Mesh with SS4 
Interim Yes Yes No 
Mesh with SS5 No No Yes 
FIPS 140-2 Level 2 140-2 Level 2 140-3 Level 2 
MAN-IA Yes Yes Yes 
MAN-IC Yes Yes Yes, improved 
MAN-IAC * No No Yes 
MAN-PC No No Yes 
MAN-PW No No Yes 
Future Spec Dom 
Improvements No No Yes 
Future Feature 
Additions No No Yes 
Future Bug Fixes Yes Yes Yes 
    
* Refers to MAN-IA and MAN-IC able to work together simultaneously  
 
 
(see Notes on next page)

## Page 2

Notes: 
All radios currently in the field can switch back and forth between SS4/SS5 without problem.  
The reason that new radios shipping from 1 November 2023 onward might not be 
downgradable from SS5 to SS4 is that they will have an expanded, 20-bit IP address range of 
172.20.x.y with a 255.240.0.0 subnet mask, effectively providing an IP address range of 
172.16.x.y to 172.31.x.y.  If these radios were downgraded to SS4, there would be a risk of IP 
address conflict with other radios in the mesh, because the routing algorithm looks only at only 
the last two octets.  For this reason, from 1 November 2023, Silvus will not ship new radios with 
SS4 production firmware (current version is v4.0.3.15), and we warn our customers against later 
doing their own SS5 to SS4 firmware downgrades for these radios after delivery.  
However, if you find yourself in this situation with an IP conflict, we offer an interim firmware, 
v4.0.4.0, which includes a function to change the radio’s IP address. In v4.0.4.0 you will be able 
to change the IP address in the GUI or API and will be responsible to ensure it does not conflict 
with other IP addresses on the network. The radio will always have its hard-coded 255.240.0.0 
address available for resets in case needed. The hard-coded address is always the IP address 
that Silvus will track for production, support, and record-keeping purposes.
