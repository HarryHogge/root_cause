# VXEP-136: Lift motor assembly bench tester

- **Issue type:** Major Project
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Medium
- **Created:** 2022-10-25
- **Updated:** 2025-04-01
- **Resolved:** 2025-04-01
- **Reporter:** Cameron Chapman
- **Assignee:** Laszlo Juhasz
- **Creator:** Cameron Chapman
- **Labels:** EE, Intern
- **Links:** relates to XEO-272 (VTOL Motor/ESC Test Fixture-Mechanical Design); is blocked by VA-669 (Update design of Lift Motor/ESC Tester from bench proto to production tool); relates to VA-825 (NCR 1842 CA - Update 107-102974 Traveler Inspection of OP # 20); relates to VA-941 (Make high power switch PCB for motor/ESC bench tester)

## Description

Files C:\JAI Vault 1\projects\124 - test equipment\electrical design\motor tester
we may want a sharepoint for draft files (easier to collaborate), but vault for now.

12/19 Planning a prototype review meeting to discuss the following.

Goal:
- Develop a way to quickly and safely test ESC assemblies, ideally in the electronics shop.
- This is most needed to test spare lift ESC assemblies, as they are currently not tested at full power until the customer first operates them. It could also improve testing of all ESCs, but they are already flight tested by us. Additional testing would take more time.
- A tool like this could also be useful for engineering development. Ex: identifying hotspots on ESC boards. Testing loading conditions hard to replicate on the dyno.

Status
- Prototype built and functional. Needs mechanical and other improvements to use in production and higher power.

 
Actions:
EE:
- Plan for VXE2024 lift assemblies.
- Probably need higher power motor and load for VXE2024. Evaluate if we should do that now or after VXE30 design.
- Order parts for 3 assemblies.
- Motor https://store.tmotor.com/goods-330-U12+KV90.html
- Ask RC benchmark about PCB availability. Procure extras. Alternate RCB PCBs may also work. Have 2. Need to locate or find a third.
- Files
- Output pdfs of current wiring diagram and schematics. Send to Cam for review when done.
- Check all files into vault.
- Clean up folder. Move old/obsolete files to another folder. Move main diagram and pdf to main folder,
- Record safe operation limits for testing. Automatic shutoffs where possible. Investigate RC benchmark temp sensors.
- Develop basic example script to demo. Ex: 600W 10 seconds
- When tester can safely run full power profile, develop production checkout script. ~1500W for 30 sec.
- Consider capacitor circuit (like the dyno) to prevent motor breaking damage.
- Investigate ways to eliminate RC benchmark lag. Guessing EMI. Shorter cables, shielding, etc.
- Simulate Aircraft wiring associated ripple current, see NCR 1842 as to why.
- Cover exposed conductors.
- Develop RPM and power requirements for lift and forward ESCs.
- Ideally add margin for future development.
- Send for review and
- ensure tester can handle those requirements.
- Safety shutoff switch.
- Develop how to document for production (script) and engineering (variable load) uses.
- Document safety limits for manual testing (temperature, power vs duration, etc.) Instrument if reasonable.
- Define normal and fail values of everything. Automatically measure and abort.
- Case temp
- Install thermistor
- Power/efficiency.
- Automate testing. Ryan F may be able to help with this.
- Design reviews with all stakeholders at applicable points.
- Test
- Determine if secondary motor cools faster than primary. If it will cool down enough by the time the primary is ready to go again
- Procedure.
- Ensure everything is installed before power is applied

MechE: The current stand rattles at high speeds and can be improved for safety and testing efficiency.
- Machined coupler to reduce high speed vibration. Done.
- More sturdy stand. Done.
- Quicker way to install and remove motor assemblies. Maybe slide the secondary motor+coupler back to enable swapping of the primary. Done.
- Create Jira subtasks for the above. Done.
- Package up final setup.
- Document installation and parts. How does someone order and install a new one.

 
 
Questions
- Do we spare nose ESCs and motors, or just nose cone assemblies? Are those tested at full power before shipment?
- Should we develop one of these stands or adapters for forward motors?
- Once the initial production version is ready, how many would we want to build?  Starting with 1 for eng, 1 for production and parts for 1 spare.

## Comments (21)

### Cameron Chapman, 2022-12-19

@Laszlo Juhasz , can you please list the current location for any related documents for this project? 
“Motor Bench Tester Prototype and Project Review “ meeting invite sent for 12/20

### Laszlo Juhasz, 2022-12-19

@Cameron Chapman  The files are: Motor_ESC_Load Tester

### Laszlo Juhasz, 2022-12-19

@Cameron Chapman The control PCBA from Tytorobotics should be back in stock later this month or early in January.
[embedded file]

### Cameron Chapman, 2022-12-19

Thanks Laszlo. Looks like a good start. Can you please do the following (see PCB process doc for questions):
- Assign one PCBA PN per PCB used. Ex: “2210A02A PCB Desc”
- Move design files to this folder “C:\JAI Vault 1\Projects\124 - Test Equipment\Electrical Design\Motor Tester”. 
- It is ok to keep draft design files on teams/elsewhere, but they are easiest to sort and review on the vault.
- Create one folder for each PCB, (ex: 2210A02A) move files for that PCB to that folder. Files pertaining to the whole project or not specific to those boards can stay in the main folder.
- Create one .prj file for each PCB. Multiboard projects can be useful for linking and documenting mutiple boards.
- Create a BOM for each of the PCBs.
- Create a wiring diagram and BOM for and the major parts used on the tester (power supply, motor, wire AWG, connectors, etc.)
- Start a document describing the operation of the prototype. Word doc+photos. Save to the main folder.

### Laszlo Juhasz, 2022-12-19

@Cameron Chapman  Yes, I’m on it.

### Laszlo Juhasz, 2023-01-11

@Cameron Chapman Good Morning, the control board from TytoRobotics for the RC Benchmark Software is available right now. 
What is your suggestion as far as quantity to order?

Thank you,
[embedded file]

### Cameron Chapman, 2023-01-11

As discussed. 4. 2 for planned builds, 2 for additional/spares.

### Laszlo Juhasz, 2023-02-10

I’m working on filtering and sorting the latest design files for this project and all of the files are at: C:\JAI Vault 1\Projects\124 - Test Equipment\Electrical Design\Motor Tester\Motor_ESC_Load Tester

### Laszlo Juhasz, 2023-02-10

@Mark Squillante Please place the design files here: C:\JAI Vault 1\Projects\124 - Test Equipment\Electrical Design\Motor Tester\Motor_ESC_Load Tester\Safety Relay Controller

### Cameron Chapman, 2023-02-10

@Former user

### Cameron Chapman, 2023-05-17

@Former user @Scott Stuckey next step for this is to make the stand more mechanically stable and rugged. Would this be a good intern project, or need more experience?

### Former user, 2023-05-17

@Cameron Chapman I don’t think an intern would have any trouble with this.

### Cameron Chapman, 2023-05-17

Sounds good. Do you have an intern project list to add this to? I’ve been using the Jira label EE-Intern for mine.

### Former user, 2023-05-17

@Cameron Chapman There may be one somewhere. I’ve added the tag to this project so we can find it later.

### Cameron Chapman, 2023-06-19

@Scott Stuckey this could be a good summer project for interns. Essentially, we need some mechanical support to make Laszlo’s prototype tester more rugged, handle higher speeds, and enable quicker motor assembly swaps.

### Matt Philley, 2023-10-09

@Marc Richardson @Greg Fryer @Cameron Chapman 
We just had another lift motor pass shop testing, but roast itself once it was installed in the aircraft during hover testing. Can we evaluate the priority for this project again?
With the inclusion of the TCI-1 spares kits we are shipping out hundreds of spare lift motor & ESC’s now that we know are not being adequately tested which seems like a risk worth discussing again.
Ref. NCR 1637 from AC 565 on 10/12/23 (Rear left lift motor ESC fried)

### Cameron Chapman, 2023-10-09

Agreed. Shipping ESCs not tested at full load is very risky. Next step in this project is we need MechE support to make the test rig more rugged. 
Alternatives until that is ready. 
- Hover testing (caught this failure, but not full load)
- Tether test aircraft before flying.
- Test spare ESCs by installing on the dyno , boom, or stationary position (pretty labor intensive and ties up a test asset)

### Greg Fryer, 2023-10-09

@Matt Philley @Cameron Chapman By luck (or let’s pretend it’s planning), @Noah Richardson should have a chunk of time free as X-kit moves from build to test. Just ran him through the basics. I need to check if there’s anything more urgent, but hopefully we can start something moving.
@Scott Stuckey FYI, since this will need design & review.
Cameron - Also, will need Laszlo or another EE familiar to give Noah the basic operation tour.
All - Moved to VXEP and will make some Epics.

### Connor Peebles, 2023-11-13

added EE Action 7. a. “Simulate Aircraft wiring associated ripple current, see NCR 1842 as to why.“ as a corrective action for NCR 1842. Though it might interfere with action 7 itself…

### Christa Meck, 2025-03-25

@Laszlo Juhasz and/or @Cameron Chapman Does this work from 2022 still need to be done?

### Christa Meck, 2025-03-25

@Laszlo Juhasz and/or @Cameron Chapman Does this work from 2022 still need to be done?

## Attachments (7)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| PWM2V_Converter.gif | image | 506 | 2022-10-26 | listed only |
| [2210P02A_SCH.pdf](attachments/11216_2210P02A_SCH.pdf.md) | pdf | 433 | 2022-11-02 | converted |
| 3D image.jpg | image | 253 | 2022-11-02 | listed only |
| PWM2V_PCB.jpg | image | 262 | 2022-11-02 | listed only |
| [PWM_to_V.pdf](attachments/11215_PWM_to_V.pdf.md) | pdf | 298 | 2022-11-02 | converted |
| image-20221219-225430.png | image | 24 | 2022-12-19 | listed only |
| image-20230111-171455.png | image | 315 | 2023-01-11 | listed only |
