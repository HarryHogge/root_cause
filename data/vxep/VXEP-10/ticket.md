# VXEP-10: TPTR-85 VXE 509 Fixed Wing Autopilot Failed on First Flight

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-08-23
- **Updated:** 2023-09-19
- **Resolved:** 2023-09-19
- **Reporter:** Allen Gardner
- **Assignee:** Greg Fryer
- **Creator:** Allen Gardner
- **Links:** relates to VA-34 (VXE 509 - Connection to vehicle lost while idle on the ground); relates to VXEP-68 (Evaluate standardizing soldering iron temperatures and other build processes. ); relates to ENG-2350 (Determine and document electronics IPC and other requirements we will use for assembly and inspection.  ); is blocked by VA-63 (VXE509 CA - Customer risks assessment. Statistical analysis of left over magacc2 boards.)
- **Customer:** TIQUILA
- **Vehicle Tail Number:** VXE 509
- **Other Stakeholder (as required):** Brad Crampton
- **Incident Type:** Mission Failure/Abort
- **Severity:** 1 - Flight Critical
- **Impacted Disciplines:** Hardware, Quality Assurance

## Description

8D Link: 8D flight 509.pptx
Flight Safety Report Link: Vehicle Investigation V509.pptx (sharepoint.com)
NCR AC509 - RMA - AP (Green) Failure during Pre-Launch
APB-10460

During Stalker FAT: on Stalker vehicle (S/N 509), the pre-launch wizard was successfully completed then lunch was taken. The vehicle was then moved after lunch to it’s launch point. When attempting to arm the vehicle, the vehicle errored and it was found that the Fixed Wing Autopilot had failed. One of the AP circuit board failed resulted in a failed launch.

## Corrective Action

Summary
Quality: Containment of unlabeled assemblies.  CARS in place for production
Engineering: - Statistical survey of assemblies- Risk assessment of magacc2 failure in flight

Details:
- Implement checks on traveler for solder balls, F.O.D., and undried moisture before soldering the shield on.
- VXE509 CA - Implement humidity check, Bake out MAGACC2 board before shield, Conformal coat before shield - Test the best route forward
- Quarantine old, un-labeled magacc2 assemblies that are in E-shop.
- Customer risks assessment. Statistical analysis of left over magacc2 boards.
- quantify risk of magacc2 failure during flight
- Confirm that the serial bus going to the magacc2 board has a fail safe mode (if magacc2 is deemed not functional, it will not further boot processor) - [software task]
- Determine if service bulletin or airworthiness directive is recommended.


Not a potential cause for this issue, but discovered during the investigation, and should be resolved. 
- Add conformal coating to inside of magacc2 board before can is installed
- Link to this Jira on suggestions of removing conformal coating
- Require gloves for all avionics/ clean before CC/ bake out boards before CC & shield installation
- https://jenaero.atlassian.net/browse/VA-473

## Issue Status

8/8: The incident maggacc board 3.3V test point is showing 2.7V. The 5.0V test point is showing 2.5V. This suggests some failure around the voltage regulators on the maggacc board. I would like to take the shielding can off to get a look at the components
After probing inside this while powered to attempt to narrow down where the voltage was dropping, there was a small spark around R1. After powercycling the board it was noted that the 5V and 3.3V test points were back to their correct values. The board was then able to successfully connect to the GCS.
8/9: I suspect that there was F.O.D. bridging to the RF shield can (GND in this circuit), potentially making a voltage divider.
I suspect the F.O.D. made enough contact to induce a spark which may have separated the bridge, allowing normal operation. 3.3V TP = 3.3V and 5.0V TP = 5.0V 
There is no indication that the previous NCRs (1022, 1165, and 1349) are caused by an adjacent or reoccuring problem in AC509

## Root Cause

Quality issue.  Excessive solder balls, F.O.D. and potential corrosion was found on the component side of the magacc2 board (1710P01A), potentially as a result of missed quality check. This caused a short that inhibited functionality of the board.

## Comments (9)

### Allen Gardner, 2023-08-25

@Sam Miller Can you please assemble the list of all corrective actions to make sure we have every to-item captured? Perhaps this is being worked under https://jenaero.atlassian.net/browse/VA-34, but I’m guess there is more todo that we need to capture.

### Marc Richardson, 2023-09-05

@Brad Crampton Please put together an 8D for this issue. We will need to show containment and corrective actions to the customer for this issue.

### Matt Philley, 2023-09-11

added copy of root cause summary

### Former user, 2023-09-18

Per coordination with LM, this TPTR has been closed
@Greg Fryer @Sam Miller 
JSMT 230918.pptx

### Greg Fryer, 2023-09-19

Investigating if final action (internal) is complete, then will close.

### Greg Fryer, 2023-09-19

Per discussion with Brad, final quality actions are complete.

### Greg Fryer, 2023-09-19

No CCB required.

### Greg Fryer, 2023-09-19

@Former user @Former user FYI per discussion with you and verification of tasks, I closed TPTR-85

### Former user, 2023-09-19

Thanks
Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: Greg Fryer (Jira) <jira@jenaero.atlassian.net>
Sent: Tuesday, September 19, 2023 5:15:00 PM
To: Glen Francis <gfrancis@edgeautonomy.io>
Subject: [JIRA] Greg Fryer mentioned you on https://jenaero.atlassian.net/browse/VXEP-10#icft=VXEP-10
Greg Fryer mentioned you on an issue
VXE Problems/https://jenaero.atlassian.net/browse/VXEP-10#icft=VXEP-10 TPTR-85 VXE 509 Fixed Wing Autopilot Failed on First Flight  ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌
Greg Fryer mentioned you on an issue
VXE Problems<https://jenaero.atlassian.net/browse/VXEP?atlOrigin=eyJpIjoiNjE0YjRiMDM1OWU2NDA3OThiYjk2ZjgwZjZlMDgzY2EiLCJwIjoiaiJ9>
/
VXEP-10<https://jenaero.atlassian.net/browse/VXEP-10?atlOrigin=eyJpIjoiNjE0YjRiMDM1OWU2NDA3OThiYjk2ZjgwZjZlMDgzY2EiLCJwIjoiaiJ9>
TPTR-85 VXE 509 Fixed Wing Autopilot Failed on First Flight <https://jenaero.atlassian.net/browse/VXEP-10?atlOrigin=eyJpIjoiNjE0YjRiMDM1OWU2NDA3OThiYjk2ZjgwZjZlMDgzY2EiLCJwIjoiaiJ9>
https://secure.gravatar.com/avatar/30932faa17de9dd3cc101850fcc4eb8c?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FGF-0.png       Greg Fryer 3:14 PM PDT
@Glen Francis @Jeran Heistermann FYI per discussion with you and verification of tasks, I closed TPTR-85
View issue<https://jenaero.atlassian.net/browse/VXEP-10?atlOrigin=eyJpIjoiNjE0YjRiMDM1OWU2NDA3OThiYjk2ZjgwZjZlMDgzY2EiLCJwIjoiaiJ9>
Get Jira notifications on your phone! Download the Jira Cloud app for Android<https://play.google.com/store/apps/details?id=com.atlassian.android.jira.core&referrer=utm_source%3DNotificationLink%26utm_medium%3DEmail> or iOS<https://itunes.apple.com/app/apple-store/id1006972087?pt=696495&ct=EmailNotificationLink&mt=8>.
Manage notifications<https://jenaero.atlassian.net/jira/settings/personal/notifications?emailPreferences=true&atlOrigin=eyJpIjoiNjE0YjRiMDM1OWU2NDA3OThiYjk2ZjgwZjZlMDgzY2EiLCJwIjoiaiJ9#emailpreferences>  •  Give feedback<https://surveys.atlassian.com/jfe/form/SV_9X3zi1X4q1gKsqF>  •  Privacy policy<https://www.atlassian.com/legal/privacy-policy>
[cid:atl-generated-e4f59835-f517-41e3-87fd-d6b0b0e58b9c]
[cid:atl-generated-e4f59835-f517-41e3-87fd-d6b0b0e58b9c]
- - WARNING: This email originated from outside of the organization. Do not click links or open attachments unless you recognize the sender and know the content is safe. **

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [TPTR-85 - AC509 Autopilot Failure - Customer Summary 23.09.11.pdf](attachments/16186_TPTR-85%20-%20AC509%20Autopilot%20Failure%20-%20Customer%20Summary%2023.09.11.pdf.md) | pdf | 1592 | 2023-09-11 | converted |
