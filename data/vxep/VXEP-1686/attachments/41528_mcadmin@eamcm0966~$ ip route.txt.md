# mcadmin@eamcm0966~$ ip route.txt

Attachment 41528, text, 5 KB, added 2026-01-30 by Alexander Alan Arnold.

mcadmin@eamcm0966:~$ ip route
10.0.0.0/8 dev eth1 proto kernel scope link src 10.131.198.30 metric 100
169.254.0.0/16 dev eth1 scope link metric 1000
172.17.0.0/16 dev docker0 proto kernel scope link src 172.17.0.1 linkdown
172.18.0.0/16 dev br-4838d7e652fa proto kernel scope link src 172.18.0.1
224.0.0.0/4 dev eth1 proto static scope link metric 100
mcadmin@eamcm0966:~$ ip -s link show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    RX: bytes  packets  errors  dropped overrun mcast
    1650569    12283    0       0       0       0
    TX: bytes  packets  errors  dropped carrier collsns
    1650569    12283    0       0       0       0
2: dummy0: <BROADCAST,NOARP> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
    link/ether 86:e6:bd:9f:52:6e brd ff:ff:ff:ff:ff:ff
    RX: bytes  packets  errors  dropped overrun mcast
    0          0        0       0       0       0
    TX: bytes  packets  errors  dropped carrier collsns
    0          0        0       0       0       0
3: eth0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc mq state DOWN mode DEFAULT group default qlen 1000
    link/ether 00:0c:8b:56:09:88 brd ff:ff:ff:ff:ff:ff
    RX: bytes  packets  errors  dropped overrun mcast
    0          0        0       0       0       0
    TX: bytes  packets  errors  dropped carrier collsns
    0          0        0       0       0       0
    altname enP1p1s0
4: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000
    link/ether 3c:6d:66:15:f3:4c brd ff:ff:ff:ff:ff:ff
    RX: bytes  packets  errors  dropped overrun mcast
    3788079    35605    0       199     0       10154
    TX: bytes  packets  errors  dropped carrier collsns
    11801577   20759    0       0       0       0
    altname enP8p1s0
5: l4tbr0: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
    link/ether 5e:18:fc:2f:14:91 brd ff:ff:ff:ff:ff:ff
    RX: bytes  packets  errors  dropped overrun mcast
    0          0        0       0       0       0
    TX: bytes  packets  errors  dropped carrier collsns
    0          0        0       0       0       0
6: rndis0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast master l4tbr0 state DOWN mode DEFAULT group default qlen 1000
    link/ether 5e:18:fc:2f:14:91 brd ff:ff:ff:ff:ff:ff
    RX: bytes  packets  errors  dropped overrun mcast
    0          0        0       0       0       0
    TX: bytes  packets  errors  dropped carrier collsns
    0          0        0       0       0       0
7: usb0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast master l4tbr0 state DOWN mode DEFAULT group default qlen 1000
    link/ether 5e:18:fc:2f:14:93 brd ff:ff:ff:ff:ff:ff
    RX: bytes  packets  errors  dropped overrun mcast
    0          0        0       0       0       0
    TX: bytes  packets  errors  dropped carrier collsns
    0          0        0       0       0       0
8: br-4838d7e652fa: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DEFAULT group default
    link/ether 72:6f:cd:47:c0:9b brd ff:ff:ff:ff:ff:ff
    RX: bytes  packets  errors  dropped overrun mcast
    9700739    2288     0       0       0       0
    TX: bytes  packets  errors  dropped carrier collsns
    1929568    13593    0       0       0       0
9: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN mode DEFAULT group default
    link/ether 1a:96:7d:aa:01:b9 brd ff:ff:ff:ff:ff:ff
    RX: bytes  packets  errors  dropped overrun mcast
    0          0        0       0       0       0
    TX: bytes  packets  errors  dropped carrier collsns
    0          0        0       0       0       0
18: vetha820782@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-4838d7e652fa state UP mode DEFAULT group default
    link/ether 26:f9:f7:9a:55:81 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    RX: bytes  packets  errors  dropped overrun mcast
    54017      279      0       0       0       0
    TX: bytes  packets  errors  dropped carrier collsns
    103497     386      0       0       0       0
19: veth8d86268@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-4838d7e652fa state UP mode DEFAULT group default
    link/ether e2:bd:d6:76:f8:9c brd ff:ff:ff:ff:ff:ff link-netnsid 1
    RX: bytes  packets  errors  dropped overrun mcast
    5541140    3304     0       0       0       0
    TX: bytes  packets  errors  dropped carrier collsns
    2042149    13815    0       0       0       0
20: veth3230ccf@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-4838d7e652fa state UP mode DEFAULT group default
    link/ether fa:48:89:f1:03:4c brd ff:ff:ff:ff:ff:ff link-netnsid 2
    RX: bytes  packets  errors  dropped overrun mcast
    4373585    216      0       0       0       0
    TX: bytes  packets  errors  dropped carrier collsns
    23744      235      0       0       0       0
21: veth76b3cae@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-4838d7e652fa state UP mode DEFAULT group default
    link/ether 9e:b2:c4:d4:cf:12 brd ff:ff:ff:ff:ff:ff link-netnsid 3
    RX: bytes  packets  errors  dropped overrun mcast
    10193678   5833     0       0       0       0
    TX: bytes  packets  errors  dropped carrier collsns
    10198454   6615     0       0       0       0
