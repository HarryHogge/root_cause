# 2120003-01 - Electronics - Xcomm Board (1607P01A) 3 - Burn-In Procedure.pptx

Attachment 44672, pptx, 73988 KB, added 2026-02-19 by Ben Norris.

## Slide 1

ProcedurePart Number:		2120003-01Assembly Revision:	DDescription:		XCOMM Burn-In
Procedure Revision: E
31 October 2025
[picture]
UNCONTROLLED WHEN PRINTED

DATE PRINTED:__11/7/2025__

PRINTED COPIES ARE ONLY VALID FOR 24 HOURS FROM THE PRINT DATE UNLESS MARKED “CONTROLLED COPY” IN RED INK.
COPIES OF THESE CONTROLLED DOCUMENTS ARE NOT AUTHORIZED.
1
Edge Autonomy Proprietary Information
2025-10-31

## Slide 2

| Rev | Description | Date |
| A | Original Release. | 2022-11-02 |
| B | Boards now received with conformal coat from supplier. Removing conformal coat process. | 2024-06-20 |
| C | PN updated per ENG-2735 | 2024-10-25 |
| D | Industrial SD Card 2120068-01 | 2025-01-03 |
| E | Updated photos and procedure to show new oven, removed obsolete Op 20 | 2025-10-31 |
Revision History:
2
Edge Autonomy Proprietary Information
2025-10-31

## Slide 3

[picture]
Tools and Supplies:
Tools: 
Oven capable of 70 Degrees C
Board carrier tray
X-comm checkout harness


Power supply
Two banana plug jumpers
Iron Bird laptop
Supplies: 
Conformal coating
General Information: 
THIS ASSEMBLY REQUIRES ESD PROTECTION.
Order of operations is important for this assembly.  Follow all steps in order.
This assembly is serial tracked.  Each assembly produced with this procedure must have unique serial number and be tracked in Condor and in traveler.
This assembly is processed using multiple subsequent documents.  See traveler for document list.
[picture]
3
Edge Autonomy Proprietary Information
2025-10-31

## Slide 4

Safety Information: 
Personal Protective Equipment (PPE): 
General – Wear disposable gloves.​

Safety Guidelines:
General – Do not ingest small parts due to choking hazards. Stay alert to sharp edges and corners of assembly materials.
Heat Gun ​ – Keep flammable materials away from the heat gun. Keep the heat gun away from skin.
Epoxy and Adhesives – Do not ingest, inhale, or touch epoxy and adhesive materials.

In Case of Emergency: 
Seek immediate medical attention and inform supervisors of work-related injuries.
[picture]
4
Edge Autonomy Proprietary Information
2025-10-31

## Slide 5

10
Use a cotton swab to cover the battery and capacitor with conformal coat.

✎ Record the material lot number and expiration date in the Traveler.
5
Edge Autonomy Proprietary Information
2025-10-31
[picture]
[picture]

## Slide 6

20
Unplug AUX cables.
Feed harnesses through the passthrough in the back of the oven.
Plug the hole using the split foam.
6
Edge Autonomy Proprietary Information
2025-10-31
[picture]
[picture]
[picture]

## Slide 7

30
Plug the banana plugs into the power supply located on top of the oven.
Take care to ensure correct polarity.
Ensure the power supply is plugged into a wall outlet that will not get switched off. 
Turn it on and set the voltage to 28.1V and the current to 2.5A.
✘ DO NOT connect X-comm boards until the power supply has been set up.  Failure to set the power supply can result in damage to boards.
7
Edge Autonomy Proprietary Information
2025-10-31
[picture]

## Slide 8

40
Load the X-comms into the oven and plug the test harness into each one.
Note the labels on each cable to be able to tell which plug goes to each board.  
Acceptable to hot mate this connector with PSU turned on.
8
Edge Autonomy Proprietary Information
2025-10-31
[picture]

## Slide 9

50
Ensure the lights on the XCOMM light up after being plugged in.
Close oven once fully loaded.
Place a sign on the door: Testing in progress. DO NOT OPEN.
9
Edge Autonomy Proprietary Information
2025-10-31
[picture]
[picture]
[picture]

## Slide 10

60
Select “Profile Actions” on oven home screen.
Select “Go to Profiles”
Find profile 2, “XCOMM”, and select actions
Select “Run Profile”
10
Edge Autonomy Proprietary Information
2025-10-31
[picture]
[picture]
[picture]
[picture]
[picture]
1
4
3
2

## Slide 11

70
Leave in oven undisturbed for at least six hours.
Acceptable to leave running overnight.
11
Edge Autonomy Proprietary Information
2025-10-31
[picture]

## Slide 12

80
Do not open oven.
Gather IronBird laptop and plug ethernet cable for an XCOMM into the 10.128 network.
12
Edge Autonomy Proprietary Information
2025-10-31
[picture]
[picture]

## Slide 13

90
Navigate on the IronBird laptop to the XCOMM interface at 10.128.1.2 using a web browser.
Log in using default credentials.
Username: stalker		Password: $talkerXE240
Verify the system time field says a minimum of 6 hours.
Any less than 6 hours, as pictured above, is considered a failure and requires a retest or NCR.
13
Edge Autonomy Proprietary Information
2025-10-31
[picture]
[picture]

## Slide 14

100
If the board successfully passed, disconnect the IronBird laptop and turn off the temp switch on the oven.
Flip the main power switch to turn off the power supply to the XCOMM.
14
Edge Autonomy Proprietary Information
2025-10-31
[picture]
[picture]

## Slide 15

110
Demate the XCOMM from the test harness.
Bag and tag the XCOMM boards in individual silver shielding ESD bags and write the following on the bag:
Tested XCOMMPN: 2120003-01
Clean the workspace and put away all test harnesses.
Turn off the oven and return the IronBird laptop to its appropriate location.
🔍 Submit for closeout QC inspection.
15
Edge Autonomy Proprietary Information
2025-10-31
[picture]
