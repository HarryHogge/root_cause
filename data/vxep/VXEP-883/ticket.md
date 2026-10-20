# VXEP-883: MAGNSS Firmware - Forward state data to MAIM if found on expected IP

- **Issue type:** Sub-task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2025-01-07
- **Updated:** 2025-01-24
- **Resolved:** 2025-01-24
- **Reporter:** Kurt Burian
- **Assignee:** Joshua Boren
- **Creator:** Kurt Burian
- **Parent:** VXEP-880 MAIM v4 Software Release

## Description

Ping for MAIM board on expected address. If found, forward IMU+GPS data to MAIM address

## Comments (2)

### Joshua Boren, 2025-01-22

[embedded: xcomm_202_20250122_090237_361_a8e2e83.zip][embedded: maim_msg.py]
Using this build on the XComm and this python script to act as the maim, I was able to verify the desired functionality.
With the correct build on the XComm and the connected dev machine setup with the *.12 IP address based on the XComm’s tail number, the dev host can act like the maim sending the hello message and show that the XComm and the OEM7700 start logging messages to it.
** EDIT ** For clarification, the MAGNSS test HIL can’t be in HIL mode.  If the HIL asset is in HIL mode for the XComm, it needs to be taken out of HIL mode.
- Open a TCP connection using Putty or Teraterm to the OEM7700’s IP address port 15715.  Secure ICOM is enabled and you will have to login to execute any commands.  The login command is login admin <password> The <password> is the same as the webpages password.  Once logged in, execute the log loglist command and observe there are no messages being logged on ICOM3
```
[ICOM7]log loglist
<OK
[ICOM7]<LOGLIST ICOM7 0 69.0 COARSESTEERING 2350 321362.000 02400000 c00c 17136
<     22
<          COM1 INSPVASB ONTIME 0.250000 0.000000 NOHOLD
<          COM1 INSPOSXB ONTIME 10.000000 0.000000 NOHOLD
<          COM2 UPTIMEB ONTIME 2.000000 0.000000 NOHOLD
<          COM2 RXSTATUSB ONCHANGED 0.000000 0.000000 NOHOLD
<          COM2 RXSTATUSEVENTB ONNEW 0.000000 0.000000 NOHOLD
<          COM2 INSATTB ONTIME 0.100000 0.000000 NOHOLD
<          COM2 TIMEB ONTIME 2.000000 0.000000 NOHOLD
<          COM2 LUAOUTPUTB ONNEW 0.000000 0.000000 NOHOLD
<          ICOM1 GPGSVB ONTIME 1.000000 0.000000 NOHOLD
<          ICOM1 GPGSAB ONTIME 1.000000 0.000000 NOHOLD
<          ICOM2 BESTGNSSPOSB ONTIME 0.100000 0.000000 NOHOLD
<          ICOM2 INSPVAB ONTIME 0.100000 0.000000 NOHOLD
<          ICOM2 INSSTDEVB ONTIME 0.100000 0.000000 NOHOLD
<          CCOM1 BESTGNSSPOSB ONTIME 0.100000 0.000000 NOHOLD
<          CCOM1 BESTGNSSVELB ONTIME 0.100000 0.000000 NOHOLD
<          CCOM1 INSPVACMPB ONTIME 0.100000 0.000000 NOHOLD
<          CCOM1 INSPVASDCMPB ONTIME 0.100000 0.000000 NOHOLD
<          CCOM1 TIMEB ONTIME 1.000000 0.000000 NOHOLD
<          ICOM7 LOGLIST ONCE 0.000000 0.000000 NOHOLD
<          SCOM1 INSPVASA ONTIME 1.000000 0.000000 NOHOLD
<          SCOM1 BESTGNSSPOSA ONTIME 1.000000 0.000000 NOHOLD
<          SCOM1 INSUPDATESTATUSA ONCHANGED 0.000000 0.000000 NOHOLD
```
- Open up wireshark and start a capture on the HIL interface.   Use the following two filters to observe expected or unexpected traffic:
```
XComm
udp && udp.port == 43322

OEM7700
udp && udp.port==22335
```
- There should be no datagram packets observed with either of those filters.
- Download the attached maim_msg.py script to the dev machine connected to the HIL andupdate it to use the correct 10.* IP addresses for the XComm and OEM7700.
- Execute the maim_msg.py script and observe datagram packets for each filter above
- From the TCP connection to the OEM7700 in Putty or Teraterm, execute the log loglist command again and observe there are messages being logged on ICOM3:

```
[ICOM7]log loglist
<OK
[ICOM7]<LOGLIST ICOM7 0 60.5 COARSESTEERING 2350 321774.000 02400000 c00c 17136
<     27
<          COM1 INSPVASB ONTIME 0.250000 0.000000 NOHOLD
<          COM1 INSPOSXB ONTIME 10.000000 0.000000 NOHOLD
<          COM2 UPTIMEB ONTIME 2.000000 0.000000 NOHOLD
<          COM2 RXSTATUSB ONCHANGED 0.000000 0.000000 NOHOLD
<          COM2 RXSTATUSEVENTB ONNEW 0.000000 0.000000 NOHOLD
<          COM2 INSATTB ONTIME 0.100000 0.000000 NOHOLD
<          COM2 TIMEB ONTIME 2.000000 0.000000 NOHOLD
<          COM2 LUAOUTPUTB ONNEW 0.000000 0.000000 NOHOLD
<          ICOM1 GPGSVB ONTIME 1.000000 0.000000 NOHOLD
<          ICOM1 GPGSAB ONTIME 1.000000 0.000000 NOHOLD
<          ICOM2 BESTGNSSPOSB ONTIME 0.100000 0.000000 NOHOLD
<          ICOM2 INSPVAB ONTIME 0.100000 0.000000 NOHOLD
<          ICOM2 INSSTDEVB ONTIME 0.100000 0.000000 NOHOLD
<          ICOM3 BESTGNSSPOSB ONTIME 1.000000 0.000000 NOHOLD
<          ICOM3 CORRIMUSB ONTIME 0.100000 0.000000 NOHOLD
<          ICOM3 GPGSAB ONTIME 1.000000 0.000000 NOHOLD
<          ICOM3 INSPVAXB ONTIME 0.100000 0.000000 NOHOLD
<          ICOM3 TIMEB ONTIME 1.000000 0.000000 NOHOLD
<          CCOM1 BESTGNSSPOSB ONTIME 0.100000 0.000000 NOHOLD
<          CCOM1 BESTGNSSVELB ONTIME 0.100000 0.000000 NOHOLD
<          CCOM1 INSPVACMPB ONTIME 0.100000 0.000000 NOHOLD
<          CCOM1 INSPVASDCMPB ONTIME 0.100000 0.000000 NOHOLD
<          CCOM1 TIMEB ONTIME 1.000000 0.000000 NOHOLD
<          ICOM7 LOGLIST ONCE 0.000000 0.000000 NOHOLD
<          SCOM1 INSPVASA ONTIME 1.000000 0.000000 NOHOLD
<          SCOM1 BESTGNSSPOSA ONTIME 1.000000 0.000000 NOHOLD
```

These steps demonstrate that the MAIM traffic won’t be sent until the XComm hears from the MAIM.  Once the XComm hears from the MAIM, it will configure the OEM7700 to log messages and start sending AirMagData to the MAIM.

### Ryan Smith, 2025-01-23

Tested and passed👍

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [maim_msg.py](attachments/25493_maim_msg.py.md) | text | 0 | 2025-01-22 | converted |
| xcomm_202_20250122_090237_361_a8e2e83.zip | archive | 16670 | 2025-01-22 | listed only |
