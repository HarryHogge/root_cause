# MS-725: VSM update to provide fault codes in FC messages to GCSs

- **Issue type:** Sub-task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2025-06-17
- **Updated:** 2025-07-10
- **Resolved:** 2025-07-10
- **Reporter:** David Grosher
- **Assignee:** Craig Burton
- **Creator:** David Grosher
- **Parent:** MS-711 [TPTR-402] Numerous issues with Fuel Cell Fault codes and alerts
- **Sprint:** MS Sprint 28, MS Sprint 29, MS Sprint 30

## Description

Reported by TIQ:  Fault codes were not present in VCSi or OGCS and was only in the XCOMM page that it was discovered.

## Comments (5)

### Craig Burton, 2025-07-03

I am having trouble finding the customer-facing list of Fault codes raised by the Fuel Cell.  I didn’t find the codes in my May 2023 version of the FC Ops Supplement and can’t currently access WebManuals to see if there is a more current version.  This is all that is shown in this version of the supplement:
[embedded: image-20250704-004630.png]
Wesley R found this on SharePoint, which lists these values:
[embedded: image-20250704-004729.png]

Is this the definitive list, @Tom Westrich @Sean Wendling ?  Or should the Fault Codes listed in the D450XR ICD (sample below) be used?
[embedded: image-20250704-005055.png]

Do we want to display the fault codes in Decimal or Hexadecimal values, @David Grosher ?
FYSA @Scott Whitney

### Craig Burton, 2025-07-07

The Jennings GCS’s fuel cell model was used as a reference for the VSM.  As such. primary faults were expected to be discrete values like “1” or “6” with their associated strings to display to the user:
```
void CFuelCellControl::SetFault(int fault, int op)
{
    if(fault == 1)  // danger
    {
        m_fault.SetBackGroundColor(0x0000ff);
        m_fault.SetValue((double) fault);
        m_fault.SetUnitsText(" fault");
        m_fault.SetFontColor(0xffffff);
        SetWindowText("Fuel Cell - FAULT!");
        if(vehicle->IsFlying() && !m_landing)
            MessageBeep(MB_ICONEXCLAMATION);
    }
    else if(fault == 6) // shut down
    {
        m_fault.SetBackGroundColor(0x0000ff);
        m_fault.SetValue((double) fault);
        m_fault.SetUnitsText(" shutdown");
        m_fault.SetFontColor(0xffffff);
        SetWindowText("Fuel Cell - Shutdown");
        if(vehicle->IsFlying() && !m_landing)
            MessageBeep(MB_ICONEXCLAMATION);
    }
```
These fault values are not what are received from the AP when AE fault values are injected into the FC simulator.  For example, the 0x9c20 value, pertaining to “insufficient fuel flow to fuel cell”, when injected to the AP, results in the fault value being exactly 0x9c20 in CFuelCellStateEx.Fault meaning that the AP appears to be simply passing the value through to the GCS.  When I run the Jennings GCS while this fault is active, the GCS does not show a fault at all:
[embedded: jennings-fault-0x9c20.png]
However, if I set the FC fault to integer value “6”, we see this:
[embedded: jennings-fault-6.png]
On the AP side, I can’t see where the values “1” or “6” might be set.  It looks like we’re simply grabbing the fault value from the FC string, parsing it, and assigning it to the attribute in the struct.  Unless I’m missing something, the Jennings GCS is “broken” in the same way the VSM is currently.  The latest rev shows Mike B’s work, but I went back to the original version and it was “pass through” there as well.  I must be reading this code incorrectly.
[embedded: image-20250707-182649.png]
Also, the comment in the struct for the Fault field implies filtered values (0, 1, 2, 0x80 and 4, but no 6):

[embedded: image-20250707-214304.png]

### Craig Burton, 2025-07-07

For good measure, I modified the Fuel Cell Simulator to set the Fault value to 0x9c20 after the Operating state was reached.  The fault field remained green.  The status panel in the vehicle strip (far right region once connected) flashed Error in red, but there was no indication of the fault code value itself.

### Sean Wendling, 2025-07-08

Added the customer facing decimal message list. Would you also like the HEX conversions? @Craig Burton

### Craig Burton, 2025-07-09

Thank you, Sean.  If the customer-facing documentation will have decimal values, I think it will be best if the VSM reports decimal.

## Attachments (8)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20250704-004630.png | image | 34 | 2025-07-03 | listed only |
| image-20250704-004729.png | image | 37 | 2025-07-03 | listed only |
| image-20250704-005055.png | image | 37 | 2025-07-03 | listed only |
| image-20250707-182649.png | image | 24 | 2025-07-07 | listed only |
| image-20250707-214304.png | image | 55 | 2025-07-07 | listed only |
| jennings-fault-0x9c20.png | image | 17 | 2025-07-07 | listed only |
| jennings-fault-6.png | image | 17 | 2025-07-07 | listed only |
| [FaultCodeMatrixFinal_MAR2025.xlsx](attachments/30430_FaultCodeMatrixFinal_MAR2025.xlsx.md) | xlsx | 20 | 2025-07-08 | converted |
