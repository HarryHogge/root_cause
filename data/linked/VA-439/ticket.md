# VA-439: Record 371 YPG near miss incident, the procedure you used to fix it, and any recommended corrective actions to prevent it in the future?

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-09-01
- **Updated:** 2023-11-09
- **Resolved:** 2023-11-06
- **Reporter:** Cameron Chapman
- **Assignee:** Gabriel Staples
- **Creator:** Cameron Chapman
- **Links:** causes GCSS-99 (Force Restart of GCS Following Load of DTED); blocks VXEP-45 (371 mis-configured (ready for flight then DTED loaded))

## Description

Good morning @Artis Bertulis and @Gabriel Staples . Great work landing 371 and making that demo happen. I heard there was an issue with the incorrect DTED being loaded, which caused a near miss. Can you ensure someone records this incident in JIRA, the procedure you used to fix it, and any recommended corrective actions to prevent it in the future? 
FYI @Greg Fryer@David Grosher  @John Clark @Sam Miller

## Comments (11)

### Artis Bertulis, 2023-09-01

@Cameron Chapman I didn’t participate in the flight but here’s what I’ve gathered.

Problem description:
- Launch wizard (at least the pitot calibration) happened without DTED loaded (aircraft thinks it’s at 0ft MSL)
- At some point after calibration, DTED was loaded
- The aircraft flew ~1000 - 1500ft higher than it was supposed to because it didn’t have ground elevation reference during calibration, but after GCS got the DTED (elevation) data it commanded to climb to maintain the same altitude, but above the newly obtained elevation data
- A concern/assumption was made that during the landing aircraft could start the transition to VTOL at a very high altitude and run out of HLB power. And there wasn’t a known safe way to command aircraft to fly lower than the GCS elevation.


Solution:
- Delete the uploaded DTED (elevation) files
- Set a lost comms orbit with at least a 10min timer
- Restart GCS software
- Confirm that ground elevation is back to “0”
- Sync the mission to the aircraft

### Gabriel Staples, 2023-09-05

This sounds all correct to me based on my notes too. Thank you @Artis Bertulis for writing this up. 
The pilot in command was Garret Moose (garret.moose@lmco.com) of Lockheed Martin. He has a writeup (email) with more details too.

### Gabriel Staples, 2023-09-05

Here’s the email chain and writeup. My reply is on top, with Garret’s initial writeup at the bottom of the PDF:
[embedded: Mail - Gabriel Staples - Outlook [altitude too high incident writeup].pdf]

### Gabriel Staples, 2023-09-05

Big thanks to @Artis Bertulis  for helping to provide the solution (I called him live during the incident). It sounds like both he and @Sam Miller  independently came up with the same answer.

### Gabriel Staples, 2023-09-05

Additional info. is in my writeup in my readme in my logs repo (where I stored the flight logs) here: https://bitbucket.org/edgeautonomy/jhu_vbn_saved_logs/src/main/

### Cameron Chapman, 2023-09-06

Great work and writeup everyone. What do you recommend for corrective actions? Some ideas:
- Update GCS to not allow loading DTED after pitot calibration, or force a recalibration if that happens. @Craig Burton
- Should we add that procedure to any emergency or other manuals?

### Craig Burton, 2023-09-06

Created https://jenaero.atlassian.net/browse/GCSS-99 to track.

### Gabriel Staples, 2023-09-06

@Craig Burton Can DTED currently be reloaded in-flight? If so, either force a process where the user is warned and told they will have to restart the GCS in-flight (and should increase the return to base timeout to 10 minutes perhaps before this), or don’t allow updating DTED in-flight.

### Gabriel Staples, 2023-09-06

or force a recalibration if that happens

Same thing here. Are DTED upates allowed in-flgiht? If so, recalibrating in-flight is not possible.

### Craig Burton, 2023-09-06

@Gabriel Staples We are tracking the remedy to this issue in https://jenaero.atlassian.net/browse/GCSS-99.  Michael will probably have a few ideas to prevent this from happening in the field again.

### Greg Fryer, 2023-09-19

@Gabriel Staples I moved this to “in development” because it was clearly being worked. It also looks like it’s done (I see the report), please advanced to closed. (This is me pestering everyone to click the button in Jira! 🙂 )

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [Mail - Gabriel Staples - Outlook [altitude too high incident writeup].pdf](attachments/16127_Mail%20-%20Gabriel%20Staples%20-%20Outlook%20[altitude%20too%20high%20incident%20writeup].pdf.md) | pdf | 358 | 2023-09-05 | converted |
