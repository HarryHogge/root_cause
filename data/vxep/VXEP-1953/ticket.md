# VXEP-1953: 6.6.1 update removes functionality of CRP2 system on standard VXE 30

- **Issue type:** Bug
- **Status:** In Review
- **Priority:** High
- **Created:** 2026-07-08
- **Updated:** 2026-10-19
- **Reporter:** Alexander Alan Arnold
- **Assignee:** David Grosher
- **Creator:** Alexander Alan Arnold
- **Links:** relates to FS2-4863 (VXEP-1953 - Investigation in Multicast Traffic filtering)

## Description

We received a call last week from V34 saying the CRP-2 payload stopped working after they got their birds updated to 6.6.1. We tried to help them over the phone but no luck. We replicated their setup at the lab this week and found something interesting with 6.6.1 and the XCOMM VLAN settings that prevent CRP2 functionality. We have been able to verify this issue with a few aircraft so far:
 
- Tail 462 delivered back to SASIL from RDW a few weeks back with 6.6.1
- Unknown tail (10xx) from SOI-W on 6.6.1
- V34 tails 475 + 654 on 6.6.1

 
We do have a fix for the issue but not sharing outside this circle since it requires access to XCOMM. We verified the issue exists without going into XCOMM for the fleet birds. At this point we are assuming this impacts all standard VXE30 standard aircraft with SW version 6.6.1.
 
- There is something under the hood in SW 6.6.1 on standard VXE-30 that prevents multicast traffic (FMV) from hitting the transponder port (SW2 port 1). The transponder port is used for CRP2 power and Ethernet on the standard VXE-30.
- In 6.6.1 by default VLAN tagging in XCOMM is set to ON, this prevents all multicast traffic from passing through that port.
- In 6.5.1 by default VLAN tagging is XCOMM is also set to ON, but it does not prevent multicast traffic from passing through the port.
- To fix this issue in 6.6.1 the user would need to go into XCOMM and turn VLAN tagging off and cycle power the aircraft.
- This is NOT an issue when using the advanced nav aircraft or the MCM aircraft with 6.6.1 (different ports)

## Comments (22)

### Alexander Alan Arnold, 2026-07-08

Can we get the following questions answered soon please.
- What is the VLAN tagging doing?
- What is the difference between 6.5.1 and 6.6.1 that is causing the issue with the same VLAN tagging toggle being ON?
- Is there a fix for this without going into XCOMM?

@John Clark @Scott Whitney

### Alexander Alan Arnold, 2026-07-08

Linked suspect based on Eric B comment, unsure why work item isn't linking properly

### John Clark, 2026-07-09

After speaking to @Eric Brewer some history:
- I blocked Multicast traffic to Switch 2, Port 1 out of concern for the Novatel and possible resets due to traffic from cameras and such.
- The VLAN configuration is likely side effect that simply prevents that blocking configuration. The VLANS are used to help the DHCP server find its targets and the switch configurations permit or deny that process. That’s an unusual approach as MAC Addresses and other methods are more common and accepted.

Having said the above perhaps it’s possible to correct the problem and still block the Multicast to the Novatel on the GNSS Network Switch. I’ll look into that. @Alexander Alan Arnold can you tell me please, where the CRP2 is connected in the switching fabric?

### Alexander Alan Arnold, 2026-07-09

@John Clark I have asked the CDIPT (customer reporter) to provide network and interface documentation for the CRP2

### Alexander Alan Arnold, 2026-07-09

“CRP 2 connects to the transponder port. The CRP 2 uses the power and ethernet on that port. It is setup completely layer 2. It also connects to the bulgin for the 12v flag to control power for the payload. The Ethernet is used on that port too but is routed to what we call the maintenance port (easy way to connect to aircraft via laptop)”. @John Clark @Eric Brewer 
 added picture in attachments

### John Clark, 2026-07-09

Are these Aircraft non-Advanced Nav, or does your CRP 2 share Switch 2, Port 1? @Alexander Alan Arnold Also please confirm the “maintenance port” is Switch 1, Port 2?

### Alexander Alan Arnold, 2026-07-09

@John Clark 
Based on the write up in the description it works on ADV NAV because they utilize a different port. The issue exists on standard VXE 30 only from my understanding. The port on a standard vxe is the “transponder port” not sure what they are referring to as maintenance port. I believe all interfacing with the CRP2 is done through the switch 2, port 1

### Alexander Alan Arnold, 2026-07-09

@John Clark 
Based on the write up in the description it works on ADV NAV because they utilize a different port. The port on a standard vxe is the “transponder port” not sure what they are referring to as maintenance port

### John Clark, 2026-07-09

@Alexander Alan Arnold Hmmm… The XComm Network Switch 2, Port 1 is the xponder port. This is connected to the GNSS Network Switch, Port 2 and to the Novatel OEM7700 on Port 3 and the DACU (if present) on Port 1. I am wondering if the “physical xponder port” is still available and they are jacked into that. Let me do a little research and I’ll report back on that. If you can confirm they are Adv Nav that would be helpful.

### Alexander Alan Arnold, 2026-07-09

@John Clark All aircraft that experience the issue are standard VXE 30, no novatel, no mcm, old black avionics box

### John Clark, 2026-07-09

@Alexander Alan Arnold Thanks!! That helps a lot. Adv Nav all have Novatel. The change I described was added to protect the Novatel from Multicast which we feel can cause resets. Now I can return to the original question(s).
- What is the VLAN tagging doing? - As explained earlier the VLAN tagging is a proprietary method for DHCP address assignment. It permits the DHCP Server the ability to assign what is a “static address” to a given port. This is useful to customers who need Web Server access to a payload and want to know which address it will have.
- What is the difference between 6.5.1 and 6.6.1 that is causing the issue with the same VLAN tagging toggle being ON? - The Multicast filtering is performed when the Switch is configured for the VLAN tagging. By disabling the tagging you very likely prevent Multicast configuration whether tagging is actually configured or not.
- Is there a fix for this without going into XCOMM? - There are a number of approaches that would permit customers that are not Adv Nav users to use the xponder port and not require XComm Web Page access, which is highly discouraged. All of them would require a software change.

This ticket is already assigned to @David Grosher, my superior. I will discuss those options with him and @Eric Brewer who requested the Multicast traffic blocking and reply as soon as I have guidance. I would look to @Scott Whitney to provide availability of any changes.

### Alexander Alan Arnold, 2026-07-09

@John Clark thanks for all the input and Information!

### John Clark, 2026-07-09

@Alexander Alan Arnold thank you for that, as well. I hope my answers are satisfactory.

### Alexander Alan Arnold, 2026-07-09

@John Clark extremely I know im not a software guy or coder but this info seems like it may help with another smoking gun where the MAIM is not receiving info from the Novatel, just a thought. https://jenaero.atlassian.net/browse/VXEP-1952?atlOrigin=eyJpIjoiNWM4OWI0MTEwNDg1NGIxODhhY2NiOGY2YjJhN2E3YzAiLCJwIjoiaiJ9

### John Clark, 2026-07-09

@Alexander Alan Arnold thank you. I’ll share with @Kurt Burian who is the assigned engineer.

### David Grosher, 2026-07-16

@Drew Hildreth What is the priority of this issue? Who uses CRP2 and how many birds is it on?

### Alexander Alan Arnold, 2026-07-16

@David Grosher This a standard payload for the entirety of the marine corps. the issue of the blocked multicast traffic on the transponder port effects all of there standard VXE platforms. the current work around requires changin the VLAN settings in the XCOMM so at this time only the CDIPT folks are using the workaround. I would say its fairly high prioity given the size of the PMA263 standard VXE fleet @Drew Hildreth

### David Grosher, 2026-07-16

@John Clark Can we provide a solution to the VXE30 standard only?

### John Clark, 2026-07-20

@David Grosher I am able to discuss this whenever you have some time. If there is a way to determine AdvNav (Novatel) presence at initialization that would allow me to configure/not configure blocking Multicast to the GNSS Switch. Would that be acceptable?

### David Grosher, 2026-08-28

@John Clark @Scott Whitney Do we have a status on this issue?

### Zachary K Malik, 2026-10-13

@John Clark @Scott Whitney Any progress on this so we can keep the ball moving forward?

### Scott Whitney, 2026-10-16

@Zachary K Malik we have identified the issue and will resolve this for Blk30 Std in the 6.8.1 software release, which is currently planned for early (jan/feb) 2027.

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [VLAN Tagging Payload Issues.docx](attachments/63355_VLAN%20Tagging%20Payload%20Issues.docx.md) | docx | 513 | 2026-07-08 | converted |
| CRP2.png | image | 140 | 2026-07-09 | listed only |
