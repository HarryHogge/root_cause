# VXEP-1474: RTB Sim Irregularity

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-08-14
- **Updated:** 2026-03-02
- **Resolved:** 2026-01-23
- **Reporter:** Drew Hildreth
- **Assignee:** Ted Trowbridge
- **Creator:** Drew Hildreth
- **Labels:** TIQUILA, Weekly-incident-tracker
- **Customer:** TIQUILA
- **Severity:** 2 - Degraded Performance - No Workaround
- **Program (Marquee):** TIQUILA

## Description

This was from an email from TIQUILA, attached are emails from Dan at LM, along with one from Alex and Ruyseer trying to work through this. My understanding is that there is a ticket for a similar issue, but I cannot locate it. @Douglas Baker FYSA

As discussed during JSMT, we did some additional testing in the UK and found some anomalies too. I’ve put the details below. 
At this moment in time, I havent got a warm and fuzzy that we (collectively) know whats going on, and I cant tell if the AV would end up following that spiral orbit. 
If possible – could we understand the following: 
- Has this spirally orbit always been present?
- What instances is it displayed in?
- What impact does this have on the AV during flight
- Has this been observed by any of the EA team – FLOPS, SW etc – My concern right now is it wasn’t reported anywhere (unless I’ve missed it)
- What are the operator actions when this is observed and advice to aircrew
- Is this just an HFI/GUI issue?

When attempting a fly and a mission sim I moved the landing patterns and flight positions multiple times throughout the flight, adjusting with different altitudes and differing headings. Throughout this, when running the sim manually there was no issues on the display and the mission sim looked to be accurate. 
However when running an RTB command, a mission sim would sometimes run and then show a mission sim with the spiral pattern, the mission sim doesn’t always run / display and will just ask for confirmation. When it decides to run it will show a spiral. Regardless of what it displayed it seems the AV will fly the pattens usually unlike what is displayed by the mission sim. Majority of the time when the RTB Sim would display, it shows the AV missing IP1 and sometimes not fully following the IPs 
When ever I continued the RTB the AV continued its flight ignoring the spiral and headed to IP1 then 2 and so on. If I run a mission sim after I accept the RTB, the mission sim showed as normal

## Comments (0)

## Attachments (8)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [6.5 LM Issues.pdf](attachments/31477_6.5%20LM%20Issues.pdf.md) | pdf | 362 | 2025-08-14 | converted |
| [6.5.0 Commanding Land Immediately.pdf](attachments/31483_6.5.0%20Commanding%20Land%20Immediately.pdf.md) | pdf | 459 | 2025-08-14 | converted |
| [6.5.0 Mag Mount GPS.pdf](attachments/31476_6.5.0%20Mag%20Mount%20GPS.pdf.md) | pdf | 142 | 2025-08-14 | converted |
| [6.5.0 Measure Tool.pdf](attachments/31482_6.5.0%20Measure%20Tool.pdf.md) | pdf | 464 | 2025-08-14 | converted |
| [6.5.0 Min Max Altitude.pdf](attachments/31478_6.5.0%20Min%20Max%20Altitude.pdf.md) | pdf | 130 | 2025-08-14 | converted |
| [6.5.0 Regression RTB Sim.pptx](attachments/31479_6.5.0%20Regression%20RTB%20Sim.pptx.md) | pptx | 14704 | 2025-08-14 | converted |
| download.png | image | 949 | 2025-08-14 | listed only |
| download.png | image | 640 | 2025-08-14 | listed only |
