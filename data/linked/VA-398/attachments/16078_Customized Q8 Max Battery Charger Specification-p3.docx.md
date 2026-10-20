# Customized Q8 Max Battery Charger Specification-p3.docx

Attachment 16078, docx, 2402 KB, added 2023-08-30 by Cameron Chapman.

## Custom Configuration Q8 Max Battery Charger Specification:

This document describes the software interfaces changes required to customize the Q8 Max Battery Charger for Jennings Aeronautics Inc.

| Rev | Date | Edited | Changes |
| P3 | 10/1/21 | C Chapman | Added screenshots. Updated settings to be preset/locked. |

## Summary

## Details

The supplier shall bid a software utility to allow the distributor to edit the below parameters and flash the settings to the unit via USB.   This software utility will not be released to the customer and will be protected as proprietary information.  Once the parameters are programmed, the user cannot change them on the charger. They can only be changed by flashing alternate settings.

Chemistry

Condition

Able to program a specific voltage for  the charge and storage tasks.

Able to program a voltage range for the discharge task. The user can then select to discharge to any voltage in this range.

Cells

Current

Discharge Voltage

Minimum input voltage

Maximum input power

Software utility is compatible with all active versions of Microsoft Windows.

Firmware can be to changed to custom version and reverted to the stock one.

If chargers ship with newer Q8 firmware, distributor can revert to an older version, ideally with the same program that flashes the settings.

After flashing settings, the unit shall limit the user to the following three modes of operation:

Charge

Discharge

Storage

Delete the remaining tasks so that they cannot be selected

The unit shall require the user to attach the balance port connector for all three cycles and check the cell count automatically at the beginning of charge or discharge to prevent the user from attempting to charge or discharge a pack that does not match the programmed cells setting.

The charger shall not attempt to charge when any cell voltage is below 2.80V.

The unit shall balance the pack while charging in either “Charge” or “Storage” mode.

The charger is not required to balance the cells while discharging in either “LiPo Full Discharge” or “LiPo Storage” mode, but shall stop the discharge cycle if any cell drops below 3.00V, regardless of the other cell voltages.  The unit’s current “low cell voltage warning” message is acceptable; no change to the message is required.

During a charge or discharge cycle, the unit shall display status information as it does now (No changes required, see examples from manual below):

While charging or discharging, the user shall be able to press the “up” or “down” buttons on the front face of the unit to cycle through the main status display and the individual cell voltages or other information as it does now (No changes required, see example from manual below):

The unit shall display error messages as it does now (No changes required).

## Appendix-

## Questions

IDST/PRC

What does "keep trickle" in settings mean?

JAI won’t sent to PRC or ISDT

Should users to be able to select discharge voltage?

They may want to discharge to 30% SOC for air shipping, 0% for capacity test. Either option will take a long time. Better to use discharger.

Ok to leave settings available to user? They can only be accessed with a long press on the main menu. User may want to adjust Max input power for different power supplies, min input voltage if a car battery is used, self test, and calibration.

Previous software customization document listed 12.6V min (car battery engine on) and 50A max.

Do we want to enable operating with a car battery engine off? >11.5V?

Completion and navigation beep preferences? Keep stock? (set to repeat and high volume)

## Deleted Sections from icharger

1.	The “Lithium Battery Check Time” shall be set to “1 min”

2.	The “Bal. Speed” shall be set to “Slow” and the “Bal. Trickle” shall be set to “ON”

3.	The “Li Balance” shall be set to “CV Phase”.  The unit shall reduce charge/discharge current by 50% during the CV phase if the internal temperature exceeds 55C to allow the unit to perform balancing at ambient temperatures up to 45C.

4.	The “Wait Time CHG/DCHG” shall be set to “10 min”

1.	Using an LM35DM temperature sensor contained inside the battery as connected to the existing three pin thermister port, the unit shall prevent the user from charging or discharging the battery or stop charging or discharging if the temperature is lower than 0C or higher than 45C.   It is assumed that the change in resistance due to interconnecting cable harnesses and connectors is negligible.

The “Safety Timer” shall be set to “OFF”

The “Capacity Cut-Off” shall be set to “OFF”

The “Watt Limit” shall be set to “CHG: 380W” and “DCHG: 80W”, (see 1b)

The “Key Beep Buzzer” shall be set to “OFF”

The “Completion Ring Beep” shall be set to “Beep 5 times”

The “Back-light” shall be set to “50%”.  The “Cooling fan” shall be set to “AUTO”.

The “Discharge Reduce” shall be set to “OFF”

The “Regenerative DSC” shall be set to “OFF”

The “LiPo Termination Voltage” shall be set to “4.20V”

The user shall be able to start the selected cycle with ONE press of the Start Button on the face of the unit.  No confirmation (second button push) shall be required to start a cycle.

Appendix
