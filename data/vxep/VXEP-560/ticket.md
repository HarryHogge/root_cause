# VXEP-560: Determine factors that have changed from previous to current connectors of both types (pin dimensions, assembly technique, potting compound, are they built to print, etc.).

- **Issue type:** Sub-task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2024-08-26
- **Updated:** 2024-10-10
- **Resolved:** 2024-09-27
- **Reporter:** Cameron Chapman
- **Creator:** Cameron Chapman
- **Parent:** VXEP-540 Recent AS150 Connectors causing intermittency and difficulty to connect and disconnect correctly and safely (AS150 Socket Issues)

## Comments (1)

### Nina Menon, 2024-10-10

SLO build tips/improvements from Ben N that were emailed to Ryan F 8/27/2024 - 
Builds with male pins (107-102189-1/-2):
- Checking the depth callout (.100 +/- .15) prior to potting, per page 4 of the procedure
- Luca is working on a go-no gauge for the depth. In the meantime, we are using a calibrated depth gage or calipers. If the pins sit too deep, unscrew them a bit until the dimension is hit

Builds with female sockets (114-106508, 114-106509, 107-102613):
- During the soldering process, hold the AS150 socket on the pin until the joint has cooled (reference below image from step 5 of 114-106508 procedure).

[embedded download.png]
Both build types:
- Using an improved potting jig that locates the pins/sockets to ensure better perpendicularity. Jigs are located in the vault and PNs were sent over on 9/9/2024

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| download.png | image | 1383 | 2024-10-10 | listed only |
