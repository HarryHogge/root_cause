# maim_msg.py

Attachment 25493, text, 0 KB, added 2025-01-22 by Joshua Boren.

#!/usr/bin/env python3

import socket

XCOMM_IP = "10.129.222.2"
XCOMM_PORT = 43322
OEM7_IP = "10.129.222.22"
OEM7_PORT = 22335
MESSAGE = b"hiya"

print(f"Sending to {XCOMM_IP}:{XCOMM_PORT} ", MESSAGE)

xcomm_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
xcomm_sock.sendto(MESSAGE, (XCOMM_IP, XCOMM_PORT))

oem7_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ("10.129.222.12", 53456)
oem7_sock.bind(server_address)

oem7_sock.sendto(MESSAGE, (OEM7_IP, OEM7_PORT))
