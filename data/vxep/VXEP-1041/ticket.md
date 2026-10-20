# VXEP-1041: SoC Testing

- **Issue type:** Epic
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2025-02-19
- **Updated:** 2025-04-18
- **Resolved:** 2025-04-18
- **Reporter:** Erik Hanson
- **Assignee:** Hayden Jeanor
- **Creator:** Erik Hanson
- **Parent:** VXEP-1040 LEMB Integration and Testing
- **Epic Status:** To Do
- **Epic Color:** ghx-label-11
- **Issue color:** teal

## Description

(Stolen from @Ryan Christino Flight Systems Jira ticket)
Enhance the State of Charge (SoC) calculation by incorporating temperature data. Ensure the updated calculation provides accurate and reliable results.
Notes from Hayden:
https://jenaero.atlassian.net/wiki/x/JYD1HQ
Initial Test Plan Ideas Here:
- Discharge Sweep at STD Room Temperature Across Different Current Levels.  (Measuring ESR, Temperature, Voltage, Current)
- Varying current in 10 Amp increments up to 80 Amps.
- Cruise Power Correlates to ~ 15 Amps. Collect One Additional Curve at this Point.
- Output: ESR Scaling for Current Value.
- Output: Battery Capacity.
- Discharge Sweep Across Expected Operating Temperature Range.
- Increment in 10 Degrees from -20F to 120F/140F.
- Output: ESR Scaling for Temperature Values.
- Lifetime Degradation Sweep at 25 50 100 Battery Cycles?
- Repeat Discharge Curve at Nominal Operation Point.

Neutral Battery (Purpose of the Model) is defined as battery at 70F at 15 Amp Current Draw.
These will feed into a battery coefficient table in the AP and two XCOMM look up values to scale “R”.
Notes:
Discharge to Minimum Voltage? Is that 21V for LEMB?
 
How to Test on the Aircraft?
Probably makes sense to do a few RC test in which a specified power setting is applied for an extended duration. The consistency of the power will allow for a capacity estimate which could be compared against the remaining capacity of the battery via Voltage measurements.
Could do that in the hotbox across temperatures to make sure the scaling is appropriate too. Will need to heavily measure battery temperature in that case.

## Comments (0)

## Attachments (0)
