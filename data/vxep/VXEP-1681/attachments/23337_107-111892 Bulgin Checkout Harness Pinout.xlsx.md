# 107-111892 Bulgin Checkout Harness Pinout.xlsx

Attachment 23337, xlsx, 41 KB, added 2024-09-20 by Cameron Chapman.

## Sheet: Table

107-111637, GSE Silvus Programming Cable, PINOUT
Rev		Changes		Released by		Date
A		Initial release of breakout harness		RF		2023-03-06 00:00:00
Signal Name	Source	Primary Connector	Pin Number	Wire Color	Wire AWG	Cut Length (in)	Destination	Secondary Connector	Pin Number	Bundle
PRIM_PWR GND	NC	NC	NC	NC	NC
PRIM_PWR_IN	NC	NC	NC	NC	NC
PRIM_PWR_IN	NC	NC	NC	NC	NC
AUX_PAYLOAD_RXP	PAYLOAD P	Bulgin Buccaneer PX0410/12S/6065 	11	WHITE	26 AWG PTFE	12		RJ45 Crimp		2
AUX_PAYLOAD_RXN	PAYLOAD P	Bulgin Buccaneer PX0410/12S/6065 	12	GREEN	26 AWG PTFE	12		RJ45 Crimp		2
AUX_PAYLOAD_TXP	PAYLOAD P	Bulgin Buccaneer PX0410/12S/6065 	7	YELLOW	26 AWG PTFE	12		RJ45 Crimp		3
AUX_PAYLOAD_TXN	PAYLOAD P	Bulgin Buccaneer PX0410/12S/6065 	10	ORANGE	26 AWG PTFE	12		RJ45 Crimp		3
PRIM_PWR GND	NC	NC	NC	NC	NC
12V PAYLOAD, SWITCHED	PAYLOAD P	Bulgin Buccaneer PX0410/12S/6065 	9	RED	26 AWG PTFE	12		4mm Bullet Female		1
GND	PAYLOAD P	Bulgin Buccaneer PX0410/12S/6065 	1	BLACK	26 AWG PTFE	12		4mm Bullet Female		1
1PPS	PAYLOAD P	Bulgin Buccaneer PX0410/12S/6065 	8	NC	NC
GCS_RX	PAYLOAD P	Bulgin Buccaneer PX0410/12S/6065 	5	NC	NC
GCS_TX	PAYLOAD P	Bulgin Buccaneer PX0410/12S/6065 	6	NC	NC
NC	PAYLOAD P	Bulgin Buccaneer PX0410/12S/6065 	4	NC	NC
VID_GND	PAYLOAD P	Bulgin Buccaneer PX0410/12S/6065 	3	NC	NC
VIDEO	PAYLOAD P	Bulgin Buccaneer PX0410/12S/6065 	2	NC	NC
Notes:
Ensure ETH pairs are fully back twisted
All lengths are for reference only.
Pot connector backshells when complete
Cover all lengths with TechFlex and heat shrink
Apply reference designator labels to all connections
Inject RTV732 into RJ45 connector housing.  Ensure RTV does not extrude out connector face or interfere with pins.
Insert dummy pins into unused crimp sockets.
Prototype notes
Add picture of completed assembly and criticial steps to this document after first build.

## Sheet: BOM

	EDGE AUTONOMY PROPRIETARY INFORMATION
DATE	REV	DESCRIPTION			SIGN
2023-04-11 00:00:00	A	Silvus GSE Programming Cable			R. Ferguson
	NHA	P/N			PG OF
	N/A	107-111637			1 OF 1
ITEM #	DESCRIPTION	PART NUMBER	QTY	UNIT MEAS	VENDOR/MANUFACTURER	VENDOR/MFG PART NUMBER
1	Hse-221 0.34" heat shrink label	100-105676	2	IN	BROTHER	HSE-221
2	Hse-231 0.46" heat shrink label	100-110001	2	IN	BROTHER	HSE-231
3	26 awg black wire	100-106740	12	IN	DIGI-KEY/ALPHA WIRE	5853/19 BK001
4	26 awg green wire	100-107051	48	IN	DIGI-KEY/ALPHA WIRE	5853/19 GR001
5	26 awg orange wire	100-107052	48	IN	DIGI-KEY/ALPHA WIRE	5853/19 OR001
6	26 awg red wire	100-107053	12	IN	DIGI-KEY/ALPHA WIRE	5853/19 RD001
7	26 awg white wire	100-106742	48	IN	DIGI-KEY/ALPHA WIRE	5853/19 WH001
8	26 awg yellow wire	100-106743	48	IN	DIGI-KEY/ALPHA WIRE	5853/19 YL001
9	Heat Shrink, 2:1, 1/4" ADH	100-104830	2	IN	MCMASTER-CARR	74965K63
10	QUICK SET EPOXY ADHESIVE, 3M DP100, 1.64 OZ	107-109866	AR	OZ	MCMASTER-CARR	7467A21
11	DOWSIL SEALANT RTV, BLACK, CORNING 732 (DOW732)	100-102206	AR	OZ	MCMASTER-CARR	7587A2
12	Heat Shrink, 3:1, 3/8" ADH	100-106125	4	IN	MCMASTER-CARR	7861K44
13	Heat Shrink, 3:1, 3/4" ADH	100-106134	2	IN	MCMASTER-CARR	7861K56
14	RJ45 Crimp	100-104464	1	EA	PLATINUM TOOLS	100010C
15	Braid, Nylon, 3/16"	100-106965	48	IN	TECHFLEX/DIGI-KEY	NMN0.19BK
16	Braid, Nylon, 1/4"	100-106136	12	IN	TECHFLEX/DIGI-KEY	NMN0.25BK500
17	4MM Bullet Connector, Female	100-102412-1	7	EA	AMASS	GC4010-F
18	Bulgin, PX0410-12s-xxxx Connector Plug	100-105250	1	EA	BULGIN	PX0410/12S/6065
19	Bulgin contact
	EDGE AUTONOMY PROPRIETARY INFORMATION

## Sheet: Pictures

(empty)
