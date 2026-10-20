# FW_ BOSON FLIR Camera operation.eml

Attachment 25369, eml, 830 KB, added 2025-01-13 by Grant Goodman.

From: John Gober
To: Grant Goodman
Date: Mon, 23 Dec 2024 19:52:17 +0000
Subject: FW: BOSON FLIR Camera operation

Latest on what I sent earlier…  The modification to the SLA-3000-FPC is to cut one trace. We won’t be needing to order any parts to support the mod.

Thanks,
John

From: Nick Whaley
Sent: Monday, December 23, 2024 1:14 PM
To: Raj Budhabhatti; SightLine Sales
Cc: John Gober; SightLine Support
Subject: RE: BOSON FLIR Camera operation

Hi,

I will get the instructions today. Our fantastic @SightLine Sales group can assist you with getting a quote for MIPI IN board(s).

As I understand it, once the traces are cut, you can use the Boson camera on J6 of the 1750-OEM (cam0). I don’t have access to that hardware to test and happy to assist if there are any issues.

Rework Instructions:
Overview
The 1750-OEM when attached to SLA-3000-FPC and FPC-BOSON adapter board don’t work properly. The problem is a floating I2C bus. This will be corrected on a follow-on PCB change. In the meantime, the SLA-3000-FPC board can be modified per the instruction below.

Modifications

  1.  Cut the traces as shown in the diagram:
[cid:[email]]
  2.  Use Humiseal 1A33 or a similar epoxy product to seal over the cut traces.

Thanks,
Nick

Nick Whaley | Support Group Lead | SightLine Applications, Inc | Onboard Video Processing  he/him    [phone] mobile | www.sightlineapplications.com<https://nam10.safelinks.protection.outlook.com/?url=http%3A%2F%2Fwww.sightlineapplications.com%2F&data=05%7C02%7Cggoodman%40edgeautonomy.io%7C981b37ff04a04910a28008dd238b4e20%7C1876f61a3bdb4843ae7075ed0ccb7404%7C0%7C0%7C638705803399648386%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=Zr4t%2BNprAMb5k5EsSznYAPWFMSGtbGezE2IVM3W5ivc%3D&reserved=0>

Please note our NEW PORTLAND ADDRESS is:
5711 S Hood Ave., Suite A
Portland, OR 97239
Update your records to avoid any delays in mail and shipping.

SightLine's offices will be closed from December 24th-January 1st in celebration of the holidays. Thank you for your understanding and patience.

From: Raj Budhabhatti
Sent: Monday, December 23, 2024 11:00 AM
To: Nick Whaley
Cc: John Gober; SightLine Support
Subject: Re: BOSON FLIR Camera operation

Hi Nick,
Correct. We don't have MIPI-IN board. We will order one.
Please send the instructions for mod. I understand that it will null the warranty. Once we cut the trace, will it work as in my setup? Is there anything else I need to be aware of?
I understand that you will be away 12/24-1/2 and I will be away 12/29-1/10 so I want to get what I can before that.
Thank you for your excellent support,
Raj

________________________________
From: Nick Whaley
Sent: Monday, December 23, 2024 10:54 AM
To: Raj Budhabhatti
Cc: John Gober; SightLine Support
Subject: RE: BOSON FLIR Camera operation

I don’t see the MIPI IN board in your picture. See section 7.3 of EAN-ICD-Adapter Boards<https://nam10.safelinks.protection.outlook.com/?url=https%3A%2F%2Fsightlineapplications.com%2Fwp-content%2Fuploads%2FICD-Adapter-Boards.pdf%23page%3D18&data=05%7C02%7Cggoodman%40edgeautonomy.io%7C981b37ff04a04910a28008dd238b4e20%7C1876f61a3bdb4843ae7075ed0ccb7404%7C0%7C0%7C638705803399670976%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=o40zvnW32iDdQWznCV8xHLFGPv9w2pCOWG6DtFVpDTo%3D&reserved=0> and the screenshot below.

I have contacted our hardware group and will follow up with you when I have the instructions. Basically, its cutting a trace.

If you choose to modify the 3000-FPC by cutting a trace, please note that doing so yourself will void the warranty on the adapter board. However, if we perform the rework for you, the warranty will remain intact.

Thanks,

Nick

[cid:[email]]

From: Raj Budhabhatti
Sent: Monday, December 23, 2024 10:31 AM
To: Nick Whaley
Cc: John Gober; SightLine Support
Subject: Re: BOSON FLIR Camera operation

Thank you Nick!

I have two MIPI boards, Pi22 and Pi15. Pictures attached. It does not seem like the FPC cable mates with either boards. How do I connect the FLIR camera to 1750?

Is my setup correct?

Also, please send the rework instructions. If I cannot do it, I'll send the board to you.

Here is the pic. Please advise if I have correct boards.

Thank you Nick,

Raj

Get Outlook for iOS<https://nam10.safelinks.protection.outlook.com/?url=https%3A%2F%2Faka.ms%2Fo0ukef&data=05%7C02%7Cggoodman%40edgeautonomy.io%7C981b37ff04a04910a28008dd238b4e20%7C1876f61a3bdb4843ae7075ed0ccb7404%7C0%7C0%7C638705803399686264%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=vsMhtLwncg5Ouk89aRkrWeuLZS3JIAWfaGjhnwrvWJc%3D&reserved=0>

________________________________

From: Nick Whaley
Sent: Monday, December 23, 2024 10:21:24 AM
To: Raj Budhabhatti
Cc: John Gober; SightLine Support
Subject: RE: BOSON FLIR Camera operation

Hi Raj,

Happy to help. Keep sending all your questions!

I would try the MIPI IN board + the 3000-FPC as a workaround for now. Remember, the acquisition settings will need to be for Cam1.

Would you like the rework instructions for the 3000-FPC mod, or would you like to return the boards so we can rework them?

-Nick

Nick Whaley | Support Group Lead | SightLine Applications, Inc | Onboard Video Processing  he/him    [phone] mobile | www.sightlineapplications.com<https://nam10.safelinks.protection.outlook.com/?url=http%3A%2F%2Fwww.sightlineapplications.com%2F&data=05%7C02%7Cggoodman%40edgeautonomy.io%7C981b37ff04a04910a28008dd238b4e20%7C1876f61a3bdb4843ae7075ed0ccb7404%7C0%7C0%7C638705803399700335%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=m2d8rmK65rJXirYWvaIpFzGexn47RDhz9WhU6BEHqaU%3D&reserved=0>

Please note our NEW PORTLAND ADDRESS is:

5711 S Hood Ave., Suite A

Portland, OR 97239

Update your records to avoid any delays in mail and shipping.

SightLine's offices will be closed from December 24th-January 1st in celebration of the holidays. Thank you for your understanding and patience.

From: Raj Budhabhatti
Sent: Monday, December 23, 2024 9:42 AM
To: Nick Whaley
Cc: John Gober; SightLine Support
Subject: Re: BOSON FLIR Camera operation

Hi Nick,

Thank you for your reply.

I have attached Boson through 3000-FPC-BOSON-E board. Here is the pic. I will try it using MIPI board.

Raj

Get Outlook for iOS<https://nam10.safelinks.protection.outlook.com/?url=https%3A%2F%2Faka.ms%2Fo0ukef&data=05%7C02%7Cggoodman%40edgeautonomy.io%7C981b37ff04a04910a28008dd238b4e20%7C1876f61a3bdb4843ae7075ed0ccb7404%7C0%7C0%7C638705803399713861%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=M6auMWVu8%2B6PiTJHVMULzJrp7KFV%2Fi55tYRLdCS4idU%3D&reserved=0>

________________________________

From: Nick Whaley
Sent: Monday, December 23, 2024 8:52:25 AM
To: Raj Budhabhatti
Cc: John Gober; SightLine Support
Subject: RE: BOSON FLIR Camera operation

Hi Raj,

I suspect this may be related to the Boson being on Cam0. Can you confirm you're using Cam0 (J6 input on 1750-OEM)? It requires a modified 3000-FPC to support Cam0. As a workaround, you can connect it to Cam1 (if you have the MIPI IN board). Please send a picture of your set up.

[cid:[email]]

I will follow up with the instructions once I find them 😊.

Best regards,

Nick

Nick Whaley | Support Group Lead | SightLine Applications, Inc | Onboard Video Processing  he/him    [phone] mobile | www.sightlineapplications.com<https://nam10.safelinks.protection.outlook.com/?url=http%3A%2F%2Fwww.sightlineapplications.com%2F&data=05%7C02%7Cggoodman%40edgeautonomy.io%7C981b37ff04a04910a28008dd238b4e20%7C1876f61a3bdb4843ae7075ed0ccb7404%7C0%7C0%7C638705803399727293%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=cYlEa4i9wDfE8uM6jPLCxkQxIcXTYb7i2Tfe2MDAD4s%3D&reserved=0>

Please note our NEW PORTLAND ADDRESS is:

5711 S Hood Ave., Suite A

Portland, OR 97239

Update your records to avoid any delays in mail and shipping.

SightLine's offices will be closed from December 24th-January 1st in celebration of the holidays. Thank you for your understanding and patience.

From: Raj Budhabhatti
Sent: Friday, December 20, 2024 4:13 PM
To: Nick Whaley
Cc: John Gober
Subject: BOSON FLIR Camera operation

Hello Nick,

Good morning.

I have SLA-3000-FPC  plugged in 1750 and connected to the 3000-FPC-Boson-E mounted on Boson 320 FLIR camera. I configure the acquisition settings as shown in the camera settings table. As soon as I click on "Apply" Button in Acquisition Settings window, the Camera Type reverts to "Duplicate".

Board is working since I can stream the USB camera connected to it. I tried with FPC-Boson-E board J2 supplied with 5V and without but the acquisition settings keeps reverting to Camera type = Duplicate.

What am I doing wrong?

Thank you Nick,

Raj

Staff Electrical Engineer

Edge Autonomy

Attached to this email (not converted): image001.png, image002.png, image003.png
