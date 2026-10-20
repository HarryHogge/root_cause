# VXEP-539: Main battery (s/n: 3-1976) connector heated up while plugged into V692

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-08-14
- **Updated:** 2024-10-31
- **Resolved:** 2024-10-31
- **Reporter:** Hayden Jeanor
- **Assignee:** Hayden Jeanor
- **Creator:** Hayden Jeanor
- **Links:** relates to VXEP-432 (Define Lifetime Fail Criteria for AS150 Anti spark connector resistance); relates to VXEP-540 (Recent AS150 Connectors causing intermittency and difficulty to connect and disconnect correctly and safely (AS150 Socket Issues))
- **Corrective Action:** https://jenaero.atlassian.net/browse/VXEP-540

## Description

Main battery (s/n: 3-1976) exhibited strange thermal behavior (~100F+) on the connector and “burning smells” after being plugged into V692 for ~3-4min⁠. 

Files: VXEP-540 Manufacturing defect in AS150 Connectors from EAES causing intermittency and difficulty to connect and disconnect correctly and safely
Findings: Main battery (sn 3-1976) overheating connector - JIRA VXEP-539.docx

## Plan

- plug main battery into load with current control - run it at 1A to see if connector heats up again
- if unable to replicate, ^repeat but with connector barely mated
- @Hayden Jeanor please add findings from yesterday.
- Please replace 692 power harness ASAP

## Issue Status

- Problem has been isolated down to AS150 connector of MB (s/n: 3-1976)
- V692 needs Fuse power harness replacement (p/n: 107-102189-1)

## Comments (9)

### Hayden Jeanor, 2024-08-14

Battery pack voltage = 26.45V
cell voltages:
| V1 | 3.772 |
| V2 | 3.780 |
| V3 | 3.780 |
| V4 | 3.782 |
| V5 | 3.786 |
| V6 | 3.774 |
| V7 | 3.761 |

### Hayden Jeanor, 2024-08-14

Vehicle side connector shows no visible signs of damage
[embedded: image-20240814-225530.png]
[embedded: image-20240814-225522.png]

### Cameron Chapman, 2024-08-14

do you know how long they had it on for? Long enough for logs? Do you know what the voltage was on the vehicle before? Those values should be in a log

### Hayden Jeanor, 2024-08-14

Problem has been isolated down to the AS150 connector on the Main battery. I will add evidence to show tomorrow morning. Removing NFF red tag from V692.

### Hayden Jeanor, 2024-08-15

@Matt Philley @Cameron Chapman 
It seems that V692’s anti-spark contact was possibly damaged (could have been a poor quality AS contact from production) from the exposure to the heat created by the incident. 
anti-spark contact resistance = 20.6Ohms (nominally 6Ohms)

This falls within the acceptance criteria that i (arbitrarily) established in this ticket https://jenaero.atlassian.net/browse/VXEP-432 

However, when mated and de-mated with a battery 10 times, 1 spark was observed. This is not a flight risk in the short term, but if this is a production asset, i recommend we replace the Fuse power harness due to the long term effects a sparking AS150 contact has on the quality of the contact.

### Cameron Chapman, 2024-08-15

@Hayden Jeanor yes, please replace that 692 harness ASAP. Coordinate with @Matt Philley @Liam Limon and whoever they add.

### Matt Philley, 2024-08-15

@Cameron Chapman thanks! Now that NCR has been dispo’d by Hayden we will take it from here to get AC 692 reworked.

### Cameron Chapman, 2024-08-25

@Hayden Jeanor and @Blake Falkenberg do you still have this battery? It could be useful for investigating, and laszlo says the seals can be opened with alcohol. This would let us reuse the pack which would be a good process to test, since they are worth a lot.

### Hayden Jeanor, 2024-08-26

@Cameron Chapman yes, eng still has this battery stored in our battery cabinet with a red tag. I do not plan of giving it to @Blake Falkenberg because the problem is not due to the battery itself

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20240814-225522.png | image | 13344 | 2024-08-14 | listed only |
| image-20240814-225530.png | image | 14266 | 2024-08-14 | listed only |
| [XCL00065.csv](attachments/22430_XCL00065.csv.md) | csv | 819 | 2024-08-15 | converted |
