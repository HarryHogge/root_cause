# 107-101047 - Electronics - Amicell Cell Pack Test - Work Instruction.pptx

Attachment 24242, pptx, 21370 KB, added 2024-10-28 by Hayden Jeanor.

## Slide 1

ProcedurePart Number: 	107-101047Assembly Revision:  ADescription:  Amicell Li-Po Cell Pack, 60Ah Testing
Procedure Revision: A
January 9, 2024
1
Edge Autonomy Proprietary Information
1/9/2024
[picture]
UNCONTROLLED WHEN PRINTED

DATE PRINTED:__1/9/2024__

PRINTED COPIES ARE ONLY VALID FOR 24 HOURS FROM THE PRINT DATE UNLESS MARKED “CONTROLLED COPY” IN RED INK.
COPIES OF THESE CONTROLLED DOCUMENTS ARE NOT AUTHORIZED.

## Slide 2

| Rev | Description | Written by | Checked by | Approved by | Date |
| A | Original Release. | B. Norris / N. Menon |  |  | 1/9/2024 |
2
Revision History:
Edge Autonomy Proprietary Information
1/9/2024

## Slide 3

3
Edge Autonomy Proprietary Information
1/9/2024
[picture]
Tools and Supplies:
Tools/PPE:
Fireproof Gloves
Fire retardant suit or apron
Windows 10 PC with BK Precision
Main Battery Charger Assembly (116-106151-3)
Main Battery Checker Assembly (112-105827)
>4000 W Electrical load and cables to connect to battery
Supplies:
Red Step Can
Fire Blanket
CO2 Fire extinguisher
Clay Litter
General Information: 
This procedure does not require ESD protection.
[picture]

## Slide 4

4
Edge Autonomy Proprietary Information
1/9/2024
Safety Information: 
Personal Protective Equipment (PPE): 
General – Fireproof gloves.

Safety Guidelines:
General – Do not ingest small parts due to choking hazards. Stay alert to sharp edges and corners of assembly materials.
Heat Gun ​ – Keep flammable materials away from the heat gun. Keep the heat gun away from skin.
Epoxy and Adhesives – Do not ingest, inhale, or touch epoxy and adhesive materials.
WI-1100-022 – Battery Emergency and Safety Handling Procedures
WI-1100-007 – Fire Prevention Plan

In Case of Emergency: 
Seek immediate medical attention and inform supervisors of work-related injuries.
[picture]
[picture]
WARNING – This procedure attempts to identify all hazards possible.  Due to the unpredictable nature of lithium batteries, additional hazards may exist that are not documented in this procedure.  Exercise best judgement and escalate any safety concerns if found.
This procedure is to be completed only by or under the supervision of personnel with proper fire and battery handling safety training.

## Slide 5

1
5
Edge Autonomy Proprietary Information
1/9/2024
[picture]
Receipt Voltage
Measure Receipt Voltage with Main Battery Checker Assembly (112-105827)
➤ Charge level will vary between batteries. Battery charger should detect similar voltages in cell 1–7 and nothing in cell 8.
Weigh battery in grams. Acceptable range is 5360-5500 grams
Enter measured voltages and weight in the Receipt Voltage section for each cell in spreadsheet VXE30 Main Battery Datasheet.xlsx located at:
C:\Users\YOUR USERNAME\Edge Autonomy\Battery Relocation\Documents\Battery Testing\VXE30 Main Battery Info
Use Main Battery Charger (116-106151-3) to charge battery to storage charge
[picture]

## Slide 6

2
Balance Voltage 
Fully charge Main Battery Cell Pack with Main Battery Charger (116-106151-3)
Turn on Power Supply
Press “Start” on Power Supply
Press “Middle Button” on Charger
Select “Charge” on Charger 
Select “Start” on Charger
Screen will turn blue once fully charged
6
Edge Autonomy Proprietary Information
1/9/2024
[picture]

## Slide 7

3
Balance Voltage
Measure voltages with Main Battery Checker Assembly (112-105827)
Enter respective voltages in the Balance Voltage section for each cell in spreadsheet VXE30 Main Battery Datasheet.xlsx located at:
C:\Users\YOUR USERNAME\Edge Autonomy\Battery Relocation\Documents\Battery Testing\VXE30 Main Battery Info
7
Edge Autonomy Proprietary Information
1/9/2024
[picture]

## Slide 8

4
High Stress Discharge Test
Power on the BK Precision Load and connect battery
Launch the BK Precision Software
Select “Sequence Test Program”
8
Edge Autonomy Proprietary Information
1/9/2024
[picture]
[picture]

## Slide 9

9
Edge Autonomy Proprietary Information
1/9/2024
5
High Stress Discharge Test
Select DC Load
Click “Connect” 
Click “Enable Remote Sense” checkbox
Click “Enable Fail Safe Protection” checkbox
Set Fail Safe Condition to min = 21 to max = 31
Click “Recall Sequence”  
Select VXE30 Main Battery Production Test Rev B 220413.txt located at C:\Users\YOUR USERNAME\One Drive - Edge Autonomy\Battery Relocation\Documents\Battery Testing\VXE30 Main Battery Info
Click “OK”
[picture]
1
2
3
4
5
6
7
8

## Slide 10

10
Edge Autonomy Proprietary Information
1/9/2024
6
High Stress Discharge Test
Verify the sequences
Sequence 1: Action: Discharge CW, W = .001, Stop Condition = Time, 5 Sec
Sequence 2: Action: Discharge CC, A = 80, Stop Condition = Time, 3 Min
Sequence 3: Action: Discharge CC, A = 17, Stop Condition = Voltage, 22.4 V
Step 1: Start Seq = 1, End Seq = 3. Repeat = 0
[picture]
2
1
.001
17.000
80.000
3
5

## Slide 11

11
Edge Autonomy Proprietary Information
1/9/2024
7
High Stress Discharge Test
Under Log Settings, Click “Log Data” checkbox
Click Folder icon to save data to the current year and batch number folder: CSV Files
C:\Users\YOUR USERNAME\One Drive - Edge Autonomy\Battery Relocation\Documents\Battery Testing\VXE30 Main Battery Info\VXE30 Main Battery Production Tests\CSV Files
3. Click an existing .csv file and rename it with the SN of the battery being tested and today’s date
4. Click “OK”
[picture]
3
4
5

## Slide 12

12
Edge Autonomy Proprietary Information
1/9/2024
8
High Stress Discharge Test
Once the file is correctly named, click “Start”
Closely observe the battery during Sequences 1 and 2 to ensure they run with no issues (estimated time = 3 minutes)
Let Sequence 3 run (estimated time = 3 hours)
[picture]

## Slide 13

13
Edge Autonomy Proprietary Information
1/9/2024
9
High Stress Discharge Test
After the test ends, wait 10 minutes
Measure voltages with Main Battery Checker Assembly (112-105827)
Enter voltage values in Discharge V After 10 section for each cell in spreadsheet VXE30 Main Battery Datasheet.xlsx located at:
C:\Users\YOUR USERNAME\Edge Autonomy\Battery Relocation\Documents\Battery Testing\VXE30 Main Battery Info
[picture]
[picture]
03:00:00

## Slide 14

14
Edge Autonomy Proprietary Information
1/9/2024
10
Post Discharge Test 
Open the file that was just created: 60Ah AXXXX-XXX YYMMDD B1.csv
Copy the 2 values in the final row of Columns E&F – Capacity(Ah) and Capacity(Wh)
Paste the 2 values in Columns AU and AV of VXE30 Main Battery Datasheet.xlsx for the tested battery
Select “Paste Values” Option to maintain the conditional colors
[picture]
[picture]
[picture]
[picture]

## Slide 15

15
Edge Autonomy Proprietary Information
1/9/2024
11
Post Discharge Test 
Measure internal resistance (IR) with Main Battery Charger (116-106151-3)
Turn on Power Supply
Press “Start” on Power Supply
Press “Middle Button” on Charger
Select “Charge” on Charger 
Select “Start” on Charger
Wait 1 minute
Press “Down Button” to get the IR reading in mΩ
Add the 7 values together and round to the nearest milliohm
Enter the sum into Column AT on VXE30 Main Battery Datasheet.xlsx
[picture]
[picture]
[picture]

## Slide 16

16
Edge Autonomy Proprietary Information
1/9/2024
12
Storage Voltage
Charge Main Battery Cell Pack to Storage Charge with Main Battery Charger (116-106151-3)
Turn on Power Supply
Press “Start” on Power Supply
Press “Middle Button” on Charger
Select “Storage Charge” on Charger 
Select “Start” on Charger
Record Storage Charge Value in VXE30 Main Battery Datasheet.xlsx
[picture]
