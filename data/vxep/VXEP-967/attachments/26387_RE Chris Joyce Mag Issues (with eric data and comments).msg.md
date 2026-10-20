# RE Chris Joyce Mag Issues (with eric data and comments).msg

Attachment 26387, msg, 515 KB, added 2025-02-19 by Alexander Alan Arnold.

From: Eric Brewer
To: Kendel Godfrey; Alexander Arnold; Thavirak Kong;	Support Conference Room - Huntsville; "Chris Joyce"
Date: 2025-02-19 15:36:13-05:00
Subject: RE: Chris Joyce Mag Issues

Thank you for sending the data.  In the VTOL data for 464 I’m seeing a pretty big difference in the total measured mag field as the vehicle spins around.  This is atypical, and usually points to an issue with the sensor or potentially some local disturbance to the magnetic field lines (either due to something electrical or magnetic in the vicinity of the mag).  Note the bottom left graph ‘mag magnitude’, that should be constant earth’s mag strength at your location in the ideal case (about 0.5).  Is anything different than stock about the vehicle configuration?  If not, there’s likely a mag cal issue and/or a sensor issue.    


The data for 465 looks much more stable:


 

For some reason I didn’t see the xcomm logs for the associated spins to compare against.  Are you able to look on the webpages and manually download any logs close in number to the ones in the AAR? For 465 this would be near xcl00443.csv and xcl00444.csv (likely before these, but if there are later logs grab those too).  For 464 I have xcl00573.csv and xcl00574.csv.  Once I have the xcomm logs I can make a determination about the health of the fixed-wing mag.

 

I did have a brief internal discussion and we can send you all the calibration tools and instructions as well to do a factory recalibration if we think that will help based upon the data review.  

 

Thanks,

 



Eric Brewer

Lead, GNC and Autonomy

Edge Autonomy – SLO (formerly Jennings Aeronautics)

Email: ebrewer@edgeautonomy.io <mailto:ebrewer@edgeautonomy.io> 

Mobile: 540-729-6792

 

 

From: Kendel Godfrey <kendel.godfrey@synergy-aero.com> 
Sent: Wednesday, February 19, 2025 1:46 PM
To: Alexander Arnold <aarnold@edgeautonomy.io>; Thavirak Kong <thavirak.kong@synergy-aero.com>; Support Conference Room - Huntsville <Support-HSV@edgeautonomy.io>; Eric Brewer <ebrewer@edgeautonomy.io>; Chris Joyce <chris@trinitybend.com>
Subject: Re: Chris Joyce Mag Issues

 

AARs.

465 was using wingset 465. 

464 was using 464 wingset, couldn't connect, so switched to 4034.

________________________________

From: Chris Joyce <chris@trinitybend.com <mailto:chris@trinitybend.com> > on behalf of aarnold@edgeautonomy.io <mailto:aarnold@edgeautonomy.io>  <aarnold@edgeautonomy.io <mailto:aarnold@edgeautonomy.io> >
Sent: Wednesday, February 19, 2025 10:25 AM
To: Kendel Godfrey <kendel.godfrey@synergy-aero.com <mailto:kendel.godfrey@synergy-aero.com> >; Thavirak Kong <thavirak.kong@synergy-aero.com <mailto:thavirak.kong@synergy-aero.com> >; Support Conference Room - Huntsville <Support-HSV@edgeautonomy.io <mailto:Support-HSV@edgeautonomy.io> >; Eric Brewer <ebrewer@edgeautonomy.io <mailto:ebrewer@edgeautonomy.io> >; Chris Joyce <chris@trinitybend.com <mailto:chris@trinitybend.com> >
Subject: Fw: Chris Joyce Mag Issues
When: Wednesday, February 19, 2025 12:30 PM-1:30 PM.
Where: Microsoft Teams Meeting; Support Conference Room - Huntsville 

 

 

 

Chris Joyce

________________________________

From: Alexander Arnold <aarnold@edgeautonomy.io <mailto:aarnold@edgeautonomy.io> >
Sent: Wednesday, February 19, 2025 6:07:17 AM
To: Support Conference Room - Huntsville <Support-HSV@edgeautonomy.io <mailto:Support-HSV@edgeautonomy.io> >; Eric Brewer <ebrewer@edgeautonomy.io <mailto:ebrewer@edgeautonomy.io> >; Chris Joyce <chris@trinitybend.com <mailto:chris@trinitybend.com> >
Subject: Chris Joyce Mag Issues
When: Wednesday, February 19, 2025 9:30 AM-10:30 AM.
Where: Microsoft Teams Meeting; Support Conference Room - Huntsville 

 





________________________________________________________________________________

Microsoft Teams Need help? <https://nam10.safelinks.protection.outlook.com/?url=https%3A%2F%2Furldefense.proofpoint.com%2Fv2%2Furl%3Fu%3Dhttps-3A__aka.ms_JoinTeamsMeeting-3Fomkt-3Den-2DUS%26d%3DDwMFAw%26c%3DeuGZstcaTDllvimEN8b7jXrwqOf-v5A_CdpgnVfiiMM%26r%3DhSX6YFyAq9gIFV1LtNkTccqodFx2NkrtcnhUH6zIAd8%26m%3DJad9zVlUioO7FVd9ln8yvXucU2YyPPHxkx3k_P3_7kQIPGiI-aTPLI23VUlvMhgx%26s%3DlX9BW0AhZTjmcB2_xkftRRYZLd4Dl1Zg3mdXyb77SIU%26e%3D&data=05%7C02%7Caarnold%40edgeautonomy.io%7C4b4e8cb9831543c3b11a08dd51250d47%7C1876f61a3bdb4843ae7075ed0ccb7404%7C0%7C0%7C638755941782271174%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=epo%2BrGQX6ZMn9uoU2UieR4fLl6Lpg%2F54%2FyqyQ9VSVm8%3D&reserved=0>  

Join the meeting now <https://nam10.safelinks.protection.outlook.com/?url=https%3A%2F%2Furldefense.proofpoint.com%2Fv2%2Furl%3Fu%3Dhttps-3A__teams.microsoft.com_l_meetup-2Djoin_19-253ameeting-5FMmFjZWRmMzMtZWMyMy00YmQwLTgzN2ItYzNkNjk3ODA0ODY1-2540thread.v2_0-3Fcontext-3D-257b-2522Tid-2522-253a-25221876f61a-2D3bdb-2D4843-2Dae70-2D75ed0ccb7404-2522-252c-2522Oid-2522-253a-2522dfa106af-2D481a-2D4ee1-2D8e09-2De89037308746-2522-257d%26d%3DDwMFAw%26c%3DeuGZstcaTDllvimEN8b7jXrwqOf-v5A_CdpgnVfiiMM%26r%3DhSX6YFyAq9gIFV1LtNkTccqodFx2NkrtcnhUH6zIAd8%26m%3DJad9zVlUioO7FVd9ln8yvXucU2YyPPHxkx3k_P3_7kQIPGiI-aTPLI23VUlvMhgx%26s%3D64N2S4Edh-ThYarJA4Vb0lASe_krC1wrsvVjzCxZoVk%26e%3D&data=05%7C02%7Caarnold%40edgeautonomy.io%7C4b4e8cb9831543c3b11a08dd51250d47%7C1876f61a3bdb4843ae7075ed0ccb7404%7C0%7C0%7C638755941782294596%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=P8QUzAxBBzay8Cve2nBfLE9zb0c817R92uTsbh%2Fsr8Y%3D&reserved=0>  

Meeting ID: 275 421 590 394 

Passcode: P4Bi2s4D 

________________________________

For organizers: Meeting options <https://nam10.safelinks.protection.outlook.com/?url=https%3A%2F%2Furldefense.proofpoint.com%2Fv2%2Furl%3Fu%3Dhttps-3A__teams.microsoft.com_meetingOptions_-3ForganizerId-3Ddfa106af-2D481a-2D4ee1-2D8e09-2De89037308746-26tenantId-3D1876f61a-2D3bdb-2D4843-2Dae70-2D75ed0ccb7404-26threadId-3D19-5Fmeeting-5FMmFjZWRmMzMtZWMyMy00YmQwLTgzN2ItYzNkNjk3ODA0ODY1-40thread.v2-26messageId-3D0-26language-3Den-2DUS%26d%3DDwMFAw%26c%3DeuGZstcaTDllvimEN8b7jXrwqOf-v5A_CdpgnVfiiMM%26r%3DhSX6YFyAq9gIFV1LtNkTccqodFx2NkrtcnhUH6zIAd8%26m%3DJad9zVlUioO7FVd9ln8yvXucU2YyPPHxkx3k_P3_7kQIPGiI-aTPLI23VUlvMhgx%26s%3DxYDsbQieUYsjLsHgKLw0AuhCvC2Z8yBrh6YpxeOq9TM%26e%3D&data=05%7C02%7Caarnold%40edgeautonomy.io%7C4b4e8cb9831543c3b11a08dd51250d47%7C1876f61a3bdb4843ae7075ed0ccb7404%7C0%7C0%7C638755941782305760%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=8gwrAIXfSO47XTTBIKxbVG%2FnNEypuFCzHur7MeyE69k%3D&reserved=0>  

________________________________________________________________________________

Attached to this email (not converted): image001.png, image002.png, image003.png
