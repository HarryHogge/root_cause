# GCSS-129: Document VTOL/HLB power, temperature and voltage thresholds

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-10-20
- **Updated:** 2024-03-20
- **Resolved:** 2024-03-20
- **Reporter:** Craig Burton
- **Assignee:** Craig Burton
- **Creator:** Craig Burton
- **Links:** blocks VA-714 (Review and determine launch wizard fail criteria for battery voltage and current. ); relates to MS-180 (Provide VTOL/HLB power, temperature and voltage thresholds to LMCDL)
- **Sprint:** GCSS Sprint 8 V2, GCSS Sprint 8, GCSS Sprint 9, GCSS Sprint 11, GCSS Sprint 7, GCSS Sprint 10

## Description

External ground stations and launch and recovery systems will need to display to the user various thresholds for reliability and safety of flight.  We need to document the following:
- Battery Power (kW)
- Battery Voltage (V)
- Battery Temperature (oC)
- Battery Balance (V)

## Comments (6)

### Craig Burton, 2023-11-01

@Michael Berger Cameron indicated that https://jenaero.atlassian.net/browse/VA-714 encompasses main battery, HLB and Fuel Cell.
I’m reaching out to LM for a sample section of their UI to show you what they’re trying to accomplish, which will differ from the bigger picture of “VA-714”.

### Michael Berger, 2023-11-06

Values from VXE30 SUAV configuration
\\condor\software\GCS\release\6.1.2\Installed\ProgramData\GCS\XEVTOLGCS\gcs.ini
Launch Wizard Main Battery:
```
[LAUNCHWIZBATTERY]
StableRange=1.000000
StableIterations=2
;Timer=100 Min 100 Duration in ms software will wait for each cycle of battery measurement
Timer=100
FullChargePercent=90.0 
```
Every Timer milliseconds the dialog checks the calculated battery life.
If the calculated battery life is +/- StableRange of the previous values for StableIterations,
the dialog then compares the calculated battery life to FullChargePercent.
If calculated battery life is >= FullChargePercent, a green battery is displayed and the message “Main Battery is fully charged”.
If calculated battery life is > the calculated mission elapsed time, then a yellow battery is displayed and the message “Main Battery not fully charged, but energy is sufficient to complete current mission."
Otherwise, the red battery is displayed and the message "Battery energy is not sufficient to complete current mission" is displayed.
Until the calculated battery life stabilizes an unknown battery is displayed.
If next is clicked when the battery is not green or yellow a message saying "Battery energy is LOW. Continue anyway?" with a yes/no prompt. If the operator clicks yes, then the launch wizard continues.
For block 25 (non VTOL vehicles) most messages which say “Main Battery” instead say “Battery”.

Launch Wizard Hybrid Battery (Fuel Cell Start):
```
[LAUNCHWIZHYBRIDBATTERY]
StartStableRange=1.000000
StartStableIterations=2
;StartTimer=100 Min 100 Duration in ms software will wait for each cycle of battery measurement
StartTimer=100
StartChargePercent=20.000000
```
Every StartTimer milliseconds the dialog checks the calculated battery life.
If the calculated battery life is +/- StartStableRange of the previous values for StartStableIterations,
the dialog then compares the calculated battery life to StartChargePercent.
If the fuel cell is running then the message “Fuel cell is running. Click next to proceed is displayed”.
If calculated battery life is >= StartChargePercent then the message "Hybrid battery has sufficient charge to complete fuel cell start sequence. Click "Next" to proceed to fuel cell startup sequence." is displayed. along with a green battery.
Otherwise the message "Hybrid battery does not have sufficient charge for fuel cell start sequence.Replace battery and click "Back"." is displayed with a red battery.
Until the calculated battery life stabilizes an unknown battery is displayed. 
Launch Wizard Fuel Cell Hybrid Battery
```
[LAUNCHWIZFCHYBRIDBATTERY]
LaunchStableRange=1.000000
LaunchStableIterations=2
;LaunchTimer=100 Min 100 Duration in ms software will wait for each cycle of battery measurement
LaunchTimer=100
LaunchChargePercent=90.000000
LaunchFuelCellTemp=500
ForceFuelCellOK=0
```
Every LaunchStartTimer milliseconds the dialog checks the calculated battery life.
If the calculated battery life is +/- LaunchStableRange of the previous values for LaunchStableIterations,
the dialog then checks the status of the fuel cell and compares the calculated battery life to LaunchChargePercent.
If fuel cell is ok and the calculated battery life is >= LaunchChargePercent then a green battery is displayed and the message "Fuel cell is running. Hybrid battery has sufficient charge to launch. Click "Next" to continue." is displayed.
If fuel cell is ok and calculated battery live is not >= LaunchChargePercent then the message “Fuel cell is running. Charging hybrid battery. please wait..." is displayed.
If the calculated battery life is >= LaunchChargePercent but the fuel cell in not OK than the message "Checking fuel cell. Hybrid battery has sufficient charge to launch, please wait..." is displayed.
If calculated battery life is >= LaunchChargePercent the green battery is displayed, if calcualted battery life >= (LaunchChargePercent / 2) then the yellow battery is displayed and if calculated battery life < (LaunchChargePercent / 2) then the red battery is displayed.
Until the calculated battery life stabilizes an unknown battery is displayed.

### Craig Burton, 2023-11-06

@Michael Berger Thank you for the detailed workflows for these two scenarios – this will be ideal when we are working on the Launch & Recovery back-end!
I’ve attached the screen shots from the VCSi developer: 
[embedded: generalized-range-bar.png]
[embedded: vtol-hlb-status.png]
Here’s their “ask” of us:
We are looking for the mins. maxes, and threshold values for “Warning” and “error” ranges. For example, the “orange” and “red” portions of this readout. Basically, a numerical value for the minimum, low error threshold (red), low warning threshold (orange), high warning threshold (orange), high error threshold (red), and maximum.
Warning and error thresholds are optional, but it is good to indicate these states to the operator.

Do we have the numerical values for the ranges, or does the vehicle report values in percentages?

### Michael Berger, 2023-11-08

VTOL Land OK and VTOL Launch OK are set based on the following.

```
VTOL Launch OK
if (m_xcommhealth.faults & VT_FAULT_CANT_LAUNCH) RED otherwise GREEN

VTOL Land OK
if(m_xcommhealth.faults & VT_FAULT_CANT_LAND) RED or
if(vehicle->m_DtedAGL > m_VtolEnergyState.landalt) RED otherwise GREEN

xcom sends this message XCOMM_HEALTH
with this as the contents.

struct CXCommHealth
{
	// health bits
	unsigned long faults;	// VT_FAULT.., AP_FAULT.. bits
	unsigned long pwrfaults;
};

 // fault bits
#define VT_FAULT_LOWPWR 0x00000001
#define VT_FAULT_HIGHPWR 0x00000002
#define VT_FAULT_MINTHR 0x00000004
#define VT_FAULT_MAXTHR 0x00000008
#define VT_FAULT_DIFFTHR 0x00000010
#define VT_FAULT_POWER 0x00000020

#define VT_FAULT_LINK 0x00000040	// Loss of link, GCS <> vehicle
#define VT_FAULT_LINK_VT 0x00000080	// Loss of link, xcomm <> vtol
#define VT_FAULT_LINK_AP 0x00000100	// Loss of link, xcomm <> ap
#define VT_FAULT_CTRL_VTOL 0x00000200	// Vtol controllability
#define VT_FAULT_CTRL_FW 0x00000400	// FW controllability
#define VT_FAULT_FAIL_AP 0x00000800	// Autopilot failure
#define VT_FAULT_FAIL_VT 0x00001000	// Vtol failure
#define VT_FAULT_FAIL_XC 0x00002000	// Xcomm failure
#define VT_FAULT_LINK_FC 0x00004000	// fuel cell link stopped
#define VT_FAULT_LINK_SLA 0x00008000
#define VT_FAULT_LINK_TURRET 0x00010000
#define VT_FAULT_LINK_VTRX 0x00020000	// Loss of link, xcomm <> vtol, vtol not receiving from xcomm
#define VT_FAULT_LINK_APRX 0x00040000
#define VT_FAULT_LINK_CANAIR 0x00080000

#define AP_FAULT_ROLL			0x00100000	// impared roll control detected
#define AP_FAULT_PITCH			0x00200000	// impared pitch control detected
#define AP_FAULT_AIRSPEED		0x00400000	// airspeed sensor fault
#define AP_FAULT_ALT			0x00800000	// altitude sensor fault
#define AP_FAULT_IMU			0x01000000	// imu fault
#define AP_FAULT_PWR			0x02000000	// propulsion system fault

#define VT_FAULT_BATT_VOLTAGE	0x04000000
#define VT_FAULT_BATT_CHARGE	0x08000000

#define VT_FAULT_CANT_LAUNCH	0x10000000
#define VT_FAULT_CANT_LAND		0x20000000

// xcomm power fault bits
#define XC_PWR_FAULT_LEFT	0x00000001
#define XC_PWR_FAULT_RIGHT	0x00000002
#define XC_PWR_FAULT_TAIL	0x00000004
#define XC_PWR_FAULT_RET	0x00000008
#define XC_PWR_FAULT_V128	0x00000010
#define XC_PWR_FAULT_AUX	0x00000020
#define XC_PWR_FAULT_TEMP	0x00000040

xcomm sends this message XCOMM_APM
Which sometimes starts with 5 which means the contesnts are vtol energy state
struct CVtolEnergyState
{
	unsigned short state;	// 0 .. 100
	unsigned short energy;	// w*h
	unsigned short vbatt;	// mV
	short ibatt;			// a * 10
	unsigned short lchalt;	// ft
	unsigned short landalt;
	unsigned short whpfoot;	// in 0.0001 wh/foot
	unsigned short wh100ft;	// integer watt hours for last 100 feet
};
```

### Michael Berger, 2023-11-09

gcs.ini
[SMARTBATTERY]
;MaxGoodCellImbalance=100 Good maximum cell imbalance to attempt launch / landing (mV) (default 100)
MaxGoodCellImbalance=100
;MaxOKCellImbalance=200 OK maximum cell imbalance to attempt launch / landing (mV) (default 200)
MaxOKCellImbalance=200
;MinGoodLaunchTemp=200 Good minimum battery temp to attempt a VTOL launch (degrees C * 10) (default 200 (20 C))
MinGoodLaunchTemp=200
;MinOKLaunchTemp=180 OK minimum battery temp to attempt a VTOL launch (degrees C * 10) (default 180 (18 C))
MinOKLaunchTemp=180
;MinGoodLandTemp=150 Good minimum battery temprerature to attempt a VTOL landing (degrees C * 10) (default 150 (15.0 C))
MinGoodLandTemp=150
;MinOKLandTemp=100 OK minimum battery temprerature to attempt a VTOL landing (degrees C * 10) (default 100 (10.0 C))
MinOKLandTemp=100
HLB Balance GREEN <= 100
HLB Balance YELLOW <= 200
HLB Balance RED > 200
HLB Launch Temp GREEN >= 200
HLB Launch Temp YELLOW  >= 180
HLB Launch Temp RED <180
HLB Land Temp GREEN >= 150
HLB Land Temp YELLOW >= 100
HLB Land Temp RED < 100

### Michael Berger, 2023-11-09

PERCENT is 0-100 - No GREEN YELLOW RED
POWER Range ? - No GREEN YELLOW RED
VOLTAGE Range 0-30ish - No GREEN YELLOW RED
VTOL ENERGY Range 0 → ? - No GREEN YELLOW RED

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| generalized-range-bar.png | image | 4 | 2023-11-06 | listed only |
| vtol-hlb-status.png | image | 31 | 2023-11-06 | listed only |
