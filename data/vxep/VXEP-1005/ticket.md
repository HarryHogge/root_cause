# VXEP-1005: 19P ODU current capability testing

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2025-02-12
- **Updated:** 2025-02-13
- **Resolved:** 2025-02-13
- **Reporter:** Hayden Jeanor
- **Assignee:** Adrian Garcia
- **Creator:** Hayden Jeanor
- **Parent:** VXEP-1003 LEMB Test Plan and Execution
- **Epic Link:** VXEP-1003
- **Issue Status:** Testing complete and is documented on sheet 4 of  LEMB Connector list.xlsx

## Description

Determine amount of thermal loading that the 19P ODU (mfg pn: A1AYAR-P19XCD0-0000) endures in our two proposed configurations, outlined here LEMB Connector list.xlsx, at their rated current as well as the LEMB rated current (18.6A).

## Plan

- Find scrap 19P ODUs that we would have already terminated around the shop (male and female housings)
- Terminate test articles such that they can be plugged into a power supply and load (most likely banana connectors).
- Monitor test with FLIR thermal camera.  Note steady state ambient temps at the beginning of test.
- Get a baseline of running the rated current through each connector while mated(do this first in case the connector is damaged from the higher currents)
- note the delta T after steady state thermal response (~10min)
- Run the desired max charge LEMB current through each configuration 18.6A.
- note the delta T after steady state thermal response (~10min)

## Comments (0)

## Attachments (0)
