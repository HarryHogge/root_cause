# VA-644: Complete approval (fix AR), and deploy UK Windows hardening build

- **Issue type:** Epic
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2023-10-05
- **Updated:** 2024-02-28
- **Resolved:** 2024-02-28
- **Reporter:** Greg Fryer
- **Assignee:** Greg Fryer
- **Creator:** Greg Fryer
- **Links:** blocks VXEP-7 (TPTR-89 Windows Hardening Build Implementation)
- **Sprint:** VXE-2 Mech-Prod 2024-01, VXE-2 Mechanical+Prod 09-Oct, VXE-2 Production, VXE-2 Mech-Prod 2024-6, VXE-2 Mech-Prod 2024-5

## Description

Manage work and tasks to complete this approval/deployment task for the GCS laptops.

## Comments (6)

### Greg Fryer, 2023-10-05

@Craig Burton @Wesley Reynolds I have updated this structure to follow our standard, with an epic for you to manage  things under, and tasks as needed. Also just heard about the pen test and one action outstanding, please document the task to fix, if it is clear.

### Wesley Reynolds, 2023-10-05

There is 1 issue with “Windows Hardening Build” that is not related to the laptop. I don’t know who should be responsible for seeing this change happen:

The silvus radios that are shipped to the TIQUILA customers need to be configured to have “FIPS Mode” enabled before shipping. @Greg Fryer

### Greg Fryer, 2023-12-12

@David Grosher @Wesley Lilienthal @Wesley Reynolds @Sam Miller Do we have the outstanding tasks to complete the UK Hardened build all listed here? We’ve pretty well closed down the base and upgrade laptop configs, would like to see this one off as well.

### Wesley Lilienthal, 2023-12-12

@Greg Fryer @Wesley Reynolds As detailed in https://jenaero.atlassian.net/browse/VA-647, the effort to enable FIPS mode expanded out of necessity into an effort to document and advise on the means to properly upgrade the fleet’s radios to interim Silvus FW 4.0.4.1.1, enable FIPS mode while managing its related settings, and to generate and provide a configuration profile that supports these two actions and also reconfigures the radio for enhanced link performance. The scope of this work may exceed that originally called for by this epic or by TPTR-89, as it also captures our path forward in response to Silvus' directive that no new radios will be shipped with old FW 4.0.3.14 due to IP address contention issues and the resulting need to upgrade the fleet to FW 4.0.4.1.1 with its manual IP address setting ability. 
I sent an email to Darrel and Dhruti at LM with the new configuration profile, firmware, and guide documentation to enable their review last Friday, 12/8/2023. Further discussion is pending in coordination with @Sam Miller. 
Do you see fit to break out or restructure the placement of https://jenaero.atlassian.net/browse/VA-647 to an additional or different epic than this one? Does it need expanded or different treatment?

### Greg Fryer, 2024-01-04

@Wesley Lilienthal I missed your message (got lost in the flood). We need to find out from Sam (though possibly @Wesley Reynolds may know) if the FIPS question is still required to resolve prior to having approval of the Windows Hardened Build for the SGCS-1s.
If it IS required, then the tasks stay here, though we could add more.
If it is NOT required, or just needs to be incorporated in the future, then we will make a new Epic and plan to get the new Silvus FW issue addressed. I will try to track down Sam and see if he knows off hand. (Wes is on vacation or in transit right now)

### Greg Fryer, 2024-02-28

This is released, some tasks lingered but were separated.

## Attachments (0)
