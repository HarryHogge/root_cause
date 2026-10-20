# FS2-2338: Investigation into GCS taking over 1 min to reconnect to vehicle when GCS IP address changed due to switching ethernet ports while connected.

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-09-30
- **Updated:** 2024-11-01
- **Resolved:** 2024-11-01
- **Reporter:** Scott Whitney
- **Assignee:** Scott Whitney
- **Creator:** Scott Whitney
- **Components:** Vehicle Incident Support 
- **Parent:** FS2-2335 VXEP-555 Anomalies on Launch and in flight
- **Links:** relates to VXEP-555 (VXE 530 Anomalies on Launch and in flight)
- **Epic Link:** FS2-2335
- **Sprint:** FS2 Sprint 25, FS2 Sprint 26

## Description

- During flight, radio Ethernet cable was moved from one Ethernet port to the other to eliminate multiple SA camera video feeds in the downlink. Cable was reconnected within 2-3 seconds. GCS software took 60+ seconds to reconnect to aircraft. Comms (per Silvus GUI) were great.

More details in https://jenaero.atlassian.net/browse/VXEP-555

## Comments (6)

### Michael Berger, 2024-09-30

@Scott Whitney Likely explanation. Could be tested on a Laptop with multiple ethernet ports.
This is likely caused by vehicle (FW AP) refusing to connect to a new GCS because it was already connected to another GCS. 
Each ethernet port has a unique IP address. Suppose the IP for port 1 is 10.10.10.1 and port 2 is 10.10.10.2.
When the cable was disconnected, the vehicle detected that it lost link with the GCS at IP address 10.10.10.1. It then started waiting for the GCS at IP address 10.10.10.1 to reconnect. During this time the vehicle would not allow connections from other GCSs (specifically the one at IP address 10.10.10.2).
When the vehcile eventually. timed out on the connection, it then allow the GCS at IP address 10.10.10.2 to connect.,

The vehicle could not tell that it was the same GCS trying to reconnect. It thought it was another GCS trying to take control.

In a handoff, which is what this was, the GCS must manually disconnect from the vehicle, and then reconnect.,

Switching Ethernet ports while connected to a vehicle is not a supported operation.

### Michael Berger, 2024-09-30

edited the title to say reconnect, not connect.

### Michael Berger, 2024-10-07

One of the ports on the GCS has an address of 10.x.x.51 and the other port has an address of 10.x.x.52.

### Scott Whitney, 2024-10-18

@Michael Berger  - are customers aware of this? Is it in the manuals?

### Michael Berger, 2024-10-18

@Scott Whitney is how computers work.
No where does it say that you can switch ports while connected to a vehicle and expect a quick reconnection.
the switched it because of multiple SA camera feeds or something. They did this because the ports are not the same. Because the ports are not the same you cannot switch ports with an active connection.
This has nothing to do with the GCS software.
The tiquila docs include the port info.

### Scott Whitney, 2024-11-01

Updated https://jenaero.atlassian.net/browse/VXEP-555#icft=VXEP-555 and moving this to done

## Attachments (0)
