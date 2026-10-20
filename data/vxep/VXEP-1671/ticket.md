# VXEP-1671: HP Radio IPCOMM Component Ratings Exceeded

- **Issue type:** Problem
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2026-01-29
- **Updated:** 2026-09-17
- **Resolved:** 2026-09-17
- **Reporter:** Jacob Troyer
- **Assignee:** Connor Peebles
- **Creator:** Jacob Troyer
- **Links:** relates to AV-532 (Detailed Electrical Analysis for High Power Radio on B30); relates to AV-564 (2130230-01 IPCOMM V2 - Rev A (replacing 1610P01A)); relates to AV-1431 (IPCOMM V2 thermal review and radio ES-110163 handoff)
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

**September 17 update**

I've linked AV-1431 for the PCB thermal review and test-radio checks.
Casey's 60°C/max-data results include converter/inductor temperature comparisons. Cameron said no further PCB testing was needed. Testing was at 2370 MHz, roughly 7.8–8 W RF by API telemetry and up to 44.8 W electrical input—not direct RF verification or confirmed C-band coverage.
The thermal results alone don't close the trace-current, inductor-saturation or B30 low-voltage concerns. Connor's direction still applies: close this incident once its linked tasks are closed. Engineering's decision and approved operating configuration also need to be recorded through AV-1355.
**Original incident and analysis**

Detailed electrical analysis of the HP Silvus Radio (2124664-01) shows that the following components may exceed their rating:
B40 and 30
- IPCOMM 18VSW trace at output of U5 regulator
- ICCOMM L2 inductor saturation current

B30 with LEMB
- IPCOMM buck‑only regulator cannot support 18V output at LEMB low‑voltage (17.5V)

See the following for more details:
- Analysis Spreadsheet: Silvus Increased Power Analysis.xlsx
- Analysis PowerPoint: High Power Silvus Radio Power Analysis.pptx

## Corrective Action

Containment Actions
- https://jenaero.atlassian.net/browse/VXEP-1688

## Plan

Short term containment 
- For any HP Silvus radios in use, it is suggested to limit transmit output power to 4W and the frequency to the 2200-2500 MHz band (see https://jenaero.atlassian.net/wiki/spaces/EE/pages/859734046/Product+Radio+and+Antenna+Map)
- 4W transmit power limits amount of current on traces
- 2200-2500 MHz frequency band limits peak current through inductor

Fix
- Complete replacement PCB to ensure ratings are not exceeded when operating at max power.https://jenaero.atlassian.net/browse/VA-2907

## Issue Status

1/30/26
- Traces & Inductor need further analysis/test and possible replacements/upgrades. See plan and background fields for more information.
- For any HP Silvus radios in use, it is suggested to limit transmit output power to 4W and the frequency to the 2200-2500 MHz band (see https://jenaero.atlassian.net/wiki/spaces/EE/pages/859734046/Product+Radio+and+Antenna+Map)
- 4W transmit power limits amount of current on traces
- 2200-2500 MHz frequency band limits peak current through inductor

## Comments (8)

### Cameron Chapman, 2026-01-30

Traces
Background
The 18VSW trace is limited to 2A per Altium. See https://jenaero.atlassian.net/wiki/spaces/EE/pages/1019215873/IP+COMM#18VSW-Capability 
Using Silvus Increased Power Analysis.xlsx (Links & Power Calcs tab) you can see that the sustained current is > 2A when at 100% duty cycle for C, S, and L-band
C-Band = 2.7A (example below), S-band = 2.2A, L-Band = 2.2A
Options
- Limit duty cycle/airtime
- Not possible as airtime is dependent upon many factors and is a reported byproduct metric as opposed to a knob
- Limit transmit output power
- Will limit sustained consumed power, but there is not a straightforward equation to calculate the max transmit power that reduces trace current to 2A. See https://jenaero.atlassian.net/wiki/spaces/EE/pages/630849545/SC4200+Silvus+Radios#Average-Consumed-Power-and-Transmit-Power

- **Limiting transmit output power to 4W** ← Best short-term solution
- This should be safe for 2 reasons. (1) It’s the same output power of the standard Silvus radio and (2) the 4W version of the same radio consumes 24W sustained. Although not guaranteed, the consumed power of a 10W radio limited to 4W should be near 24W (at least not 36W which is the cutoff to get the traces to 2A).

- ***Further analysis & test on traces to see if “true” rating is > 2A*** ← Best long-term solution

Inductor Saturation Current
Background
The L2 inductor saturation current is 4.5A. See inductor 7447798131
Using Silvus Increased Power Analysis.xlsx (Links & Power Calcs tab) you can see that the peak current is > 4.5A when at 100% duty cycle for C-band and <4.5A at 100% duty cycle for S-band & L-band.
NOTE: Peak duration is 100µs duration and occurs every 10ms when transmitting.
C-Band = 4.8A (example below), S-Band = 4.0A, L-Band = 3.2A
 
Options
- Limit duty cycle/airtime
- Does not impact peak power. See https://jenaero.atlassian.net/wiki/spaces/EE/pages/630849545/SC4200+Silvus+Radios#Peak-Power-Occurrence
- Limit transmit output power
- Does not impact peak power. See https://jenaero.atlassian.net/wiki/spaces/EE/pages/630849545/SC4200+Silvus+Radios#Peak-Power-Occurrence

- **Use radio only in S and L band** ← Best short-term solution
- ***Analysis/ and test on impacts of exceeding inductor saturation current. Replacing inductor if unacceptable*** ← Best long-term solution
- Laszlo’s insight 1-30-26: “I'm definitely not recommending anything running out of the spec. Considering that Inductors are usually holds +-20% tolerance as far as inductance goes and rising temperature makes that worse. At Scientific Drilling we've done some crazy evaluations and classifications for extreme environment violating the specs, but in this case I'm voting to re-consider and improve the application for better margins.”

### Cameron Chapman, 2026-01-30

@Laszlo Juhasz On the TPS54560-Q1 converter, do you know what happens if Vin is less than the Vout setpoint? Jacob didn’t see anything on the datasheet. He asked TI if you don’t know.

### Laszlo Juhasz, 2026-02-03

@Cameron Chapman Sorry not to respond sooner. The answer is in that freewheeling or body diode. That diode is sometimes not indicated on the SCH level, but it’s there. That means if the Voltage at “VIN” drops below “SW” then the diode will conduct and feeding the VIN from the SW output. In many applications a series diode at WIN might be required to block that and affecting the VIN feeding path.
[embedded: image-20260203-184020.png]

### Jacob Troyer, 2026-02-19

@Laszlo Juhasz I wish all schematics showed the body diode! Thanks for drawing it in. We should have clarified that SW is a load (without any external battery) and that VIN is our battery, so there’s really no source (beside output capacitance) to backfeed SW into VIN. Furthermore, this is in the IPCOMM board that has a FET with a body diode (drawn on the schematic!) to prevent backfeeding.
[embedded: image-20260219-232008.png]

I reached out to TI and they pointed me to this forum. From my reading, it sounds like Vout will drop with Vin and will turn off occasionally to charge the BOOT capacitor, which I think will add ripple. I added you to the TI email thread. I think we’ll likely need to test to really see what happens.

### Connor Peebles, 2026-07-30

Issues reported by Jacob are being resolved in IPCOMM V2, see linked tasks

### Tobi Ogunro, 2026-08-28

@Connor Peebles Should we close this?

### Connor Peebles, 2026-08-31

@Tobi Ogunro once the linked tasks are closed

### Connor Peebles, 2026-09-17

[AV-564] 2130230-01 IPCOMM V2 - Rev A (replacing 1610P01A) - Jira has been released, this new version of the IPCOMM board can handle (steady state) the 78W at 18V maximum needed for 10W radio operation when installed in enclosure with specified heat-sinking at system operating limits.

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20260203-184020.png | image | 239 | 2026-02-03 | listed only |
| image-20260219-232008.png | image | 119 | 2026-02-19 | listed only |
