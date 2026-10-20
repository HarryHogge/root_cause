# BAT-78: Repair, update to 1.2.32, and Test Charger SN0009

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2025-07-24
- **Updated:** 2026-03-02
- **Resolved:** 2025-07-26
- **Reporter:** Tom Westrich
- **Assignee:** Tom Westrich
- **Creator:** Tom Westrich
- **Fix versions:** 03/02/2026
- **Parent:** BAT-83 NCR-250626 - 6536
- **Links:** relates to BAT-54 (NCR-250626 - 6536)
- **Epic Link:** BAT-83

## Description

Charger SN0009 was connected to a Main FCR battery, which has a known effect of shorting battery power to battery ground through the cell balance lines and the BMS balance board in the charger.  This unit was returned for repair and updates.

## Comments (6)

### Tom Westrich, 2025-07-24

On initial inspection: 
- No obvious signs of electrical damage on charger.
- 13Ohm short between battery ground and battery positive on main charge leads.
- Physical damage to active balancing board on cell 7
- Significant damage to U16 on PCA0120 (DCDC)

### Tom Westrich, 2025-07-26

Replaced the repaired PCA0120 from SN0024 (ignition circuit damage to U6) into this unit.  Updated cals for SN009 are attached here, and are based on calibrations from the previous SN0024 control board.[embedded: ChargerSN009_NCR_Cals.csv] 
Also replaced the BMS control board and active balance boards from an engineering test asset.
Software has been updated to 1.2.32.
Quick functional checkout of cell voltage display, battery voltage display, discharge function, and charge function were all briefly demonstrated on 7/25.  Full checkout remains.

### Tom Westrich, 2025-07-26

Test 1: LEMB Connection Test (3X-ENG1, 97%)
Passes 10x LEMB connections without damage
 
Test 2: Charge LEMB (3X-ENG2) to 60%
Start time: 8:34am
LEMB starting voltage = 25.30V (56% on charger)
Cell voltages (mV) = 3632 3625 3624 3627 3627 3629 3630 (min/max delta = 8mV)
End time: 8:43am
LEMB final voltage = 25.54V (59% on charger)
 
Test 3: Discharge LEMB (3X-ENG2) to 25%
Start time: 8:45pm
LEMB starting voltage = 25.54V (59% on charger)
Cell voltages (mV) = 3665 3658 3657 3660 3660 3663 3663 (min/max delta = 8mV)
End time: 8:55am
LEMB final voltage = 24.65V (49% on charger)

### Tom Westrich, 2025-07-26

Unit passes outgoing testing on LEMB.

### Tom Westrich, 2025-07-26

Passes testing on LEMB

### Tom Westrich, 2025-07-26

Shipped, Fedex tracking number: 883081813909

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [ChargerSN009_NCR_Cals.csv](attachments/30970_ChargerSN009_NCR_Cals.csv.md) | csv | 0 | 2025-07-26 | converted |
