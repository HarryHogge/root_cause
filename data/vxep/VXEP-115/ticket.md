# VXEP-115: Radio frequency/output power usage

- **Issue type:** Problem
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** High
- **Created:** 2023-09-20
- **Updated:** 2026-03-30
- **Resolved:** 2026-03-30
- **Reporter:** Artis Bertulis
- **Assignee:** Greg Fryer
- **Creator:** Artis Bertulis
- **Links:** is blocked by VA-611 (Investigate FCC requirements and Silvus licenses for the VXE-30 and system.)

## Description

After reading up on some radio usage on frequencies and output power (it’s very broad), it seems like we might be operating outside the regulation requirements.
Default factory settings for our radios are currently:
- Frequency - 2260 MHz
- Output power - 4W (enable max power)

Seems like most sources online say that the output power should be somewhere between 0.100 mW - 1W, and the frequency range usually goes between 2400 - 2486.
One of our PMA customers mentioned that we would be FCC compliant if we operated at 1W between 2412 and 2485 - if this is correct - our factory settings might need to be changed.
Our Silvus radios do come with some licenses, but I don’t have access to those to be able to assess what’s allowed or not.
What I want to get out of this issue is:
- What is our allowable range of operations for the Silvus radios?
- Do we need to change our factory default settings for the radios?
- Does this affect SGCS2 and SGCS3 antennas as they have antennas with higher dBi gain antennas? 
Would they need to be run at lower radio output power because they have higher EIRP (equivalent isotropically radiated power)?

## Comments (1)

### Artis Bertulis, 2023-09-20

@Ruysser Gabler @Sam Miller for awereness

## Attachments (0)
