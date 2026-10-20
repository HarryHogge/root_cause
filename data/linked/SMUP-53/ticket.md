# SMUP-53: New Procedure for support to address: Mobile GPS MAG Puck no fix

- **Issue type:** Task
- **Status:** New
- **Priority:** Lowest
- **Created:** 2024-12-11
- **Updated:** 2025-10-06
- **Reporter:** David Grosher
- **Assignee:** Mark Spence
- **Creator:** David Grosher
- **Parent:** SMUP-5 VXE30 Operations Manuals <Next Version>
- **Links:** relates to VXEP-645 (Mobile GPS MAG Puck no fix )
- **Epic Link:** SMUP-5

## Description

A draft was created for linked ticket.

## Comments (6)

### Josh Burrell, 2025-01-30

@Dana Holley FYI

### Dana Holley, 2025-02-18

New Procedure: 
- Connect GPS Puck
- Open GPSinfo
- Select COM Port: Prolific...
- Baud Rate: 4800
- Start GPS
- If issues, continue
- Stop GPS
- Close GPSinfo
- Open device manager
- Click "View" at the top, then "Show hidden devices"
- Expand "Ports (COM & LPT)"
- If there are any gray Prolific devices, right click them, then click "Uninstall device"
- On the pop up, click "Uninstall"
- DO NOT tick the box that says "Delete the driver software..."
- Right click the remaining Prolific device and select "Properties"
- Click Port Settings at the top of the window
- 4800 Bits per second, 8 Data bits, no Parity
- Click "Advanced..."
- COM Port Nuimber: COM4
- Click OK on the advanced window, then OK on the Prolific Properties window
- Restart the GCS laptop
- Open GPSinfo
- Prolific..., 4800
- If it worked, you should now see blue status on the satellite connections
- Stop GPS and close GPSinfo
- Open VXE SUAV
- Settings > Edit GCS GPS Settings > Mobile Mag Mount GPS
- Settings > GCS GPS Status
- Confirm that Fix = 1. If not, let us know.

### Dana Holley, 2025-02-18

@Josh Burrell Do we add a troubleshooting chapter in the Ops manual for this? Also- I think Grace and/or Billy should go through this to provide a mark-up as well as photos after their transition is completed.

### Josh Burrell, 2025-02-19

@Dana Holley Yes, I think we would need to add a new section for troubleshooting. @Grace Burgess @William Doupis Can you please take a look at the suggested procedure Dana created and provide him with what he’s requesting?

### Dana Holley, 2025-02-27

@Jo Brown Do you know if this issue with the GPS puck receiver will be ironed out through production efforts?

### Dana Holley, 2025-06-19

@Matt Weber Do you know if this checklist is still required for VXE30 Ops Manual? See second comment from the bottom.

## Attachments (0)
