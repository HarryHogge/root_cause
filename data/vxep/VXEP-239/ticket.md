# VXEP-239: Endurance drop-off in flight. VXE-453

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2024-01-22
- **Updated:** 2026-03-02
- **Resolved:** 2025-05-13
- **Reporter:** Dana Holley
- **Assignee:** Cameron Chapman
- **Creator:** Dana Holley
- **Labels:** MCWL, PMA263
- **Issue color:** purple
- **Customer:** MCWL, PMA263
- **Other Stakeholder (as required):** Pat Wells
- **Issue Status:** Test steps sent to operator. Waiting for results.

## Description

[embedded file]
USMC MCWL customer was flying VXE30 453.  Endurance for both batteries dropped significantly for a time period of about 1 minute then came back up to normal levels. Occurrence happened once, still awaiting the phase of flight of when it occurred.  Customer would like to fly again ASAP. I had advised them not to fly based on engineering advice. Will advise them to fly again as soon as issue is resolved

@Pat Wells this is a contact prior to you arrival. Could you can take the reigns from here?

## Plan

Update for findings after customer flight. 
It would be great to get the AAR from the flight after the incident if possible. It would also be helpful if they could send back the bad battery for us to test if they would like to.
Here is what I recommend.
- Inspect main battery terminals for damage.
- If they have other equipment, perform the following to try to isolate the issue.
- Test battery in another aircraft using launch wizard. Report lowest voltage observed. (is this visible with launch wizard window open? We could point them to the webpage if not).
- Test a new battery in this aircraft. Repeat step a.
- Report results. You can give them my contact info if preferred direct.
- @David Grosher @Craig Burton we should review flag values for voltage too low during launch wizard or takeoff.

## Comments (11)

### Pat Wells, 2024-01-22

@Dana Holley got it from here.

### Pat Wells, 2024-01-22

@Greg Fryer  FYSA.. didn’t want you to miss this one.

### Greg Fryer, 2024-01-22

@Pat Wells @Dana Holley Will work with Dave to get someone to review and determine if it was aircraft or GCS glitch or something else. Thanks for the ping!

### David Grosher, 2024-01-22

@Pat Wells @Greg Fryer @Cameron Chapman It looks like there was a big drop in the voltage of the main battery.  I would not recommend flying. 
[embedded file]

### Cameron Chapman, 2024-01-22

Agreed. Do not fly. @Dana Holley @David Grosher @Greg Fryer @Pat Wells 
Observations
- Main batt is too low. HLB seems low as well during takeoff, but not much lower than a normal profile. https://jenaero.atlassian.net/wiki/spaces/EE/pages/11272193/Power+and+Temperature+Profiles

Here is what I recommend. 
- Inspect main battery terminals for damage.
- If they have other equipment, perform the following to try to isolate the issue.
- Test battery in another aircraft using launch wizard. Report lowest voltage observed. (is this visible with launch wizard window open? We could point them to the webpage if not).
- Test a new battery in this aircraft. Repeat step a.
- Report results. You can give them my contact info if preferred direct.
- @David Grosher @Craig Burton we should review flag values for voltage too low during launch wizard or takeoff.

[embedded file]

### Craig Burton, 2024-01-22

@Cameron Chapman @David Grosher We are documenting these values in https://jenaero.atlassian.net/browse/GCSS-129

### Pat Wells, 2024-01-23

@Cameron Chapman I’ve passed along your instructions to the operator. Will report back when I have the information.

### Cameron Chapman, 2024-01-24

Thanks @Craig Burton . I don’t see any abort, warning, RTB, etc. criteria in that ticket, or units on many of the values. Can you or @Michael Berger add those (ideally in the summary field), or translate from the information there?

### Pat Wells, 2024-01-26

@Cameron Chapman As directed I notified the customer twice on two different communications to not fly the aircraft while we evaluate his data.  Also asked him to perform the requested tests and report back. 
Customer notified me yesterday that he flew the aircraft anyway with different batteries and experienced no issues.  I again asked him to complete the tests and report back.
Customer contacted me today and said he has determined that his batteries from the initial flight are bad and that there’s nothing wrong with his aircraft. 
Not sure where you want to go with this one? Definitely want to keep a record of this in the event that this aircraft is involved in a future mishap.

### Cameron Chapman, 2024-01-26

Thanks @Pat Wells . It is their aircraft to do what they want with. It sounds like a battery issue. It would be great to get the AAR from the flight after the incident if possible. It would also be helpful if they could send back the bad battery for us to test if they would like to.

### Pat Wells, 2024-02-21

@Cameron Chapman  I don’t anticipate receiving anything further from the operator on this issue.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V453_240122_121810_pack (1).zip | archive | 1593 | 2024-01-22 | listed only |
| image-20240122-230847.png | image | 90 | 2024-01-22 | listed only |
| image-20240122-232817.png | image | 123 | 2024-01-22 | listed only |
