# StreamScape v4 and v5 Comparison Matrix and Transition Notes v2 (1).pdf

Attachment 19587, pdf, 153 KB, added 2024-03-18 by Matt Philley.

## Page 1

StreamScape v4 and v5 Comparison Matrix and Transition Notes 
February 2024 
 
  
StreamScape 4 Legacy  
v4.0.3.15 and below 
StreamScape 4 Interim  
v4.0.4.1 
StreamScape 5 
v5.0.0.0 and up 
IP address/netmask if 
radios shipped with builtin 
IP address/netmask of 
172.20.x.y/255.255.0.0 172.20.x.y/255.255.0.0 172.20.x.y/255.255.0.0 172.20.x.y/255.240.0.0 
IP address/netmask if 
radios shipped with builtin 
IP address/netmask of 
172.(16~31).x.y/255.240.0.0 172.20.x.y/255.255.0.0 172.20.x.y/255.255.0.0 172.(16~31).x.y/255.240.0.0 
If shipped, can update to 
SS4? Yes No No 
If shipped, can update to 
SS4 interim? Yes Yes Yes 
If shipped, can update to 
SS5? Yes Yes Yes 
Ability to change the last 
two octets of the IP address No Yes No 
Mesh with SS4 Yes Yes No 
Mesh with SS4 Interim Yes Yes No 
Mesh with SS5 No No Yes 
Critical Security Updates No No Yes 
FIPS 140-2 Level 2 140-2 Level 2 140-3 Level 2 
MAN-IA Yes Yes Yes 
MAN-IC Yes Yes Yes, improved 
MAN-IAC No No Yes 
MAN-PC No No Yes 
MAN-PW No No Yes 
Future Spec Dom 
Improvements No No Yes 
Future Feature Additions No No Yes 
Future Bug Fixes Yes Yes Yes 
 
(see Notes on next page)

## Page 2

Notes: 
All radios currently in the field can switch back and forth between SS4/SS5 without problem.  
The reason that new radios shipping from 1 November 2023 onward might not be 
downgradable from SS5 to SS4 is that they will have an expanded IP address range of 172.16.x.y 
to 172.31.x.y with a 255.240.0.0 subnet mask.  If these radios were downgraded to SS4, there 
would be a risk of IP address conflict with other radios in the mesh, because the routing 
algorithm looks only at only the last two octets.  For this reason, from 1 November 2023, Silvus 
will not ship new radios with SS4 production firmware (current version is v4.0.3.15), and we 
warn our customers against later doing their own SS5 to SS4 firmware downgrades for these 
radios after delivery.  
However, if you find yourself in this situation with an IP conflict, we offer an interim firmware, 
v4.0.4.1, which includes a function to change the last two octets of the radio’s IP address. In 
v4.0.4.1 you will be able to change the IP address in the GUI or API and will be responsible to 
ensure it does not conflict with other IP addresses on the network. The radio will always have its 
hard-coded factory address available for resets in case needed. The hard-coded address is 
always the IP address that Silvus will track for production, support, and record-keeping 
purposes.
