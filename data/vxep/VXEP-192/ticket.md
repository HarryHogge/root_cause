# VXEP-192: 107-102264 Dual Current Sense harness needs testing values defined

- **Issue type:** Problem
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Medium
- **Created:** 2023-11-14
- **Updated:** 2025-06-10
- **Resolved:** 2025-06-10
- **Reporter:** Liam Limon
- **Assignee:** Cameron Chapman
- **Creator:** Liam Limon
- **Links:** relates to VA-573 (Poor Quality/higher impedance plating on AS150 power contacts - Containment and Corrective Action); relates to VA-623 (Generate contact impedance test procedure for use on contact+wire assemblies in production)
- **Issue color:** purple
- **Target end:** 2023-12-31
- **Part Number(s):** 107-102264
- **Production Stakeholder:** Liam Limon
- **Other Stakeholder (as required):** Ryan Ferguson
- **Issue Status:** Questions sent to ryan for next steps.

## Description

Dual Current Sense harness does not currently have a production procedure for testing. We need acceptable testing values to be provided by engineering so that we can ensure the test we perform checks for the correct values to pass this cable.

## Comments (21)

### Carson Buckley, 2023-11-15

@Cameron Chapman Failures of the CS are rare in SCO, and usually related to a miswired harness.

### Ryan Ferguson, 2023-11-15

I already did some work to create a pass/fail criteria on these back before the EE team had enough headcount to do this sort of work.  
Based on the datasheet for the ACS770ECB-200U-PFF-T datasheet, I was able to find the sensor has a +/- 2.4% tolerance.  By using this number and assuming linearity of the sensor is good, we can get a min and maximum reading.  At 10A going through OUT1, we should be able to read the following voltages on VIOUT1:  Minimum: 0.244v  Target: 0.250v  Maximum: 0.256v.

I also did part of the designs for these harnesses.  They can be seen in this directory:
C:\JAI Vault 1\Production eng\4 - Electronics\3 - Tooling & Shop Aides\107-111704 Dual Current Sense Test Assembly
[embedded file]
The DCS Test Signal Harness is the only part which still needs a pinout made.  It breaks out all of the signal pins from the DF13 connector for probing with a multimeter.  The Pin 6 can probably just be left as another multimeter probe point rather than being tied back to the power input of the DCS like is shown in the diagram above.

### Ryan Ferguson, 2023-11-15

As an additional test, we can also measure the 5V supply on the board.  Looking at the spec sheet for that component, we can get an acceptance criteria - Minimum: 4.90v  Target: 5.00v  Maximum: 5.100v.  In all we can get the following acceptance criteria for this assembly:


| Connection Point A | Connection Point B | Function | Acceptance criteria |
| DF13 pin 1 | DF13 Pin 5 | VBATT / AP Pwr | When 28.0v is applied to the input of DCS: Min: 27.9v  / Target: 28.0v  / Max: 28.1v |
| DF13 Pin 1 | DF13 Pin 2 | VTOL GND Sense | When 28.0v is applied to the input of DCS: Min: 27.9v  / Target: 28.0v  / Max: 28.1v |
| DF13 Pin 3 | DF13 Pin 2 | VIOUT1 (L) | When 28v is applied to the input of the DCS and 10A load applied between OUT1+ and GND: Min: 0.244v  / Target: 0.250v  / Max: 0.256v |
| DF13 Pin 4 | DF13 Pin 5 | VIOUT2 (R) | When 28v is applied to the input of the DCS and 10A load applied between OUT2+ and GND: Min: 0.244v  / Target: 0.250v  / Max: 0.256v |
| DF13 Pin 2 | 5V Test Point | 5V Reg | When 28.0v is applied to the input of DCS: Min: 4.90v  / Target: 5.00v  / Max: 5.10v |


@Cameron Chapman Please let me know if this sounds acceptable.  The signal harness should take less than an hour to design, so all that’s needed is to build and test the hardware.

### Liam Limon, 2023-11-15

@Ryan Ferguson thank you for responding with all that information. @Cameron Chapman I’m sorry I forgot to mention in the original post that the goal of getting the pass/fail criteria is to create a testing fixture and procedure so that we can remove testing of the Dual Current Sense Assembly from the Iron Bird. It looks like Ryan has already put together everything we need but the final harness. If we can get that portion ironed out and get approval on the values we can move forward with building the test fixture and then writing the procedure and updating documentation like travelers. @Ryan Ferguson does any of this need to be defined on the drawing once it has been decided on by engineering so that quality has a reference for their traveler requirements?

### Ryan Ferguson, 2023-11-15

I understand the new Systems Engineering team has been setting up some sort of system to keep records of acceptance criteria and requirements.  For that reason I don’t know where we should keep this sort of information as it might fall under their systems or it might need to be in the drawings.  Either one would be acceptable to me to keep records of this sort of information.  From there we can roll it into a procedure and handle the Production side of things.  I do not like the idea of making our procedures and travelers the only record of a pass/fail criteria as the review process does not allow me to see the previous version of a document when approving for release.

### Cameron Chapman, 2023-11-16

@Ryan Ferguson great work with this. those test criteria are approved. The 28V tolerance is very tight and may fail with power supply or meter tolerance/drift. We can expand range now or update later if an issue. 
For initial testing, I think we should measure VIOUT1 and 2 at 0A and 5A as well. We may want to remove them later if 10A suffices to indicate all issues. 
We should add the impedance measurement to this test, even if for now it says have engineering perform measurement per the current method. Eventually production when the test is ready. 
I do not think listing test values belongs on the drawing. There are many times where we won’t know the values until a part is built, or we will want to update it faster than a drawing if new info is discovered. 
I am unaware of a systems eng system to record this info, but we should wait for them to release it before using it. @Travis Storm or @Kat Gulstad do you have something like this in work?
For now, I think we should keep test criteria in the traveler. You can see previous revs using the history/save function in the vault. If we want all versions available in search, we could/are planning to have pdfs generated of all revs then moving obsolete ones to obsolete state, then ensuring techs can’t view that state. 
[embedded file]

### Cameron Chapman, 2023-11-16

One more question, @Ryan Ferguson are you able to generate a pinout and build an adapter harness?

### Travis Storm, 2023-11-16

@Cameron Chapman  can you clarify what you mean by “record this info”?

### Cameron Chapman, 2023-11-16

@Travis Storm Ryan said “I understand the new Systems Engineering team has been setting up some sort of system to keep records of acceptance criteria and requirements. For that reason I don’t know where we should keep this sort of information as it might fall under their systems or it might need to be in the drawings.”
Acceptance criteria for PCB functional tests.

### Ryan Ferguson, 2023-11-16

@Cameron Chapman when you say generate a pinout, do you mean make a new one in Excel?  I have always had to build my harnesses and pinouts by hand as I do not have access to the new cable design software that is going through the EE team.  If there are requirements beyond this spreadsheet, it will likely have to be taken care of by Electrical Engineering.  If we are still accepting pinout tables, I can make one in Excel for this after the next milestone on the TAS project is reached.  
This is a very simple harness.  I’m sure it would only take roughly 2 hours for an EE to perform the same work.

### Travis Storm, 2023-11-16

Thanks @Cameron Chapman, I follow now.
That’s true to the extent that ATPs are on the list of typical SE work products to support/facilitate. They come late in the design cycle (they’re CDR entry criteria) and we have not gotten to that point with VXE-2024, and there’s not much of an active effort to “catch up” with VXE-30. So in short, no, nothing exists at this time.
What I suggest is an Acceptance Test Procedure as a configuration controlled document that describes the unit(s) under test, the test objectives, success criteria. I don’t know if Edge has such a template already. If not, let me know if you need help creating one.

### Cameron Chapman, 2023-11-16

@Ryan Ferguson excel pinouts are acceptable for test cables. If you need a EE to make this documentation, it will not get priority for a while based on other projects. We are trying to get a drafter req opened, but are awaiting approval.

### Cameron Chapman, 2023-11-16

Thanks @Travis Storm. I think the existing traveler+build procedure can meet these requirements “What I suggest is an Acceptance Test Procedure as a configuration controlled document that describes the unit(s) under test, the test objectives, success criteria.”

### Liam Limon, 2023-11-16

@Cameron Chapman @Ryan Ferguson  Per this comment: https://jenaero.atlassian.net/browse/VXEP-192?focusedCommentId=29109 Ryan and I just had a discussion with Garrett yesterday about testing values for the servo boost board and we decided that the testing criteria should be included on the engineering documentation because otherwise you are leaving testing definitions up to production or quality. How do we know that our testing methodology identifies the important criteria that engineering cares about in the function of the part? We need the test values defined and controlled and then it can be left to production engineering to develop a test that can meet that criteria and quality can reference the engineering defined values to decide if something is passing or failing. It will definitely require more work down the road to update testing requirements if they change but that already requires us to open an NCR, complete a Jira ticket and then get engineering time to determine if the values are indeed accurate, so at that point you’re not really adding much work to also transfer those findings to your documentation and have a revision history of how they have changed over time. 
At the end of our discussion I think we ultimately decided on having the testing requirements be included as a separate page of the engineering documentation and included in the release packet, but it doesn’t have to be on the physical drawing itself. But it still does need to be engineering controlled in the vault.

### Cameron Chapman, 2023-11-16

@Liam Limon @Ryan Ferguson @Garrett O'Neill That makes sense. 
I recommend one of these options. 
- (easiest) Engineering is part of the release signoff for production procedures involving functional tests. Include pass fail criteria there to reduce number of documents to review.
- (seems more documents to manage, and harder, but could work) Engineering creates a separate released and config controlled document like “PN Desc Test Criteria”. Procedure references it and traveler records what version was used.  Future drawings could also say test per this document.

Would either of those options work? Adding @Matt Philley and @Marc Richardson any guidance on what is acceptable/how to document the process we choose? 
Drawing is not recommended. It will drive more drawing updates, which will mean less important drawing updates get done.

### Liam Limon, 2023-11-16

@Cameron Chapman see my edit, a separate document that is controlled by engineering is acceptable, but it still has to remain as part of the released engineering documentation. It doesn’t have to define testing equipment or requirements, but just the values that are relevant to determining if a part is passing or failing. We also wanted to change from ambiguous language like the +/- to a more min-target-max language where all 3 values are clearly defined. that way if additional range is needed in the plus or minus it can be easily accounted for.

### Liam Limon, 2023-11-16

@Cameron Chapman I also don’t think that framing it as pushing back more important document updates isn't a fair assessment since updates to drawings should include reviewing those requirements. This just highlights the fact that a more robust and streamlined process needs to be developed for how documentation is updated and released. It could be as simple as grouping Jira tickets that are all associated to the same part number together and then addressing the whole, rather than tackling each individual issue as they come. 
Also, as we continue to clean up the release process, hopefully better documentation will be coming out that will require less updates. If the pre-release process is better and has more collaboration then you should see less tickets coming in for revisions and changes. Developing a checklist that is used by all of EE for how to review and release drawings would be a good first step in shoring up this process and making sure that all EE’s are doing things the same way every time. This could also be where the instructions for how to include testing requirements in released documents could be included.

### Cameron Chapman, 2023-11-16

@Liam Limon the root of many of our issues is too many projects and not enough people and processes defined/time to develop them. 
The goal/process is to group associated Jira tickets for each document update, but that process could use more development and training. This is in the checklist below. 
We have checklists in development here. Everyone is welcome to add. EE Checklists.xlsx. The updated ECN process should give more stakeholder involvement as well. 
 I think many of our drawing issues originate to a time where we had even worse understaffing, no peers to review, standards defined, etc. so new releases should improve. 
We could also add a mfg or quality review state if anyone has bandwidth to support that.

### Cameron Chapman, 2023-11-16

@Liam Limon I updated this page. You are welcome to comment/request changes. https://jenaero.atlassian.net/wiki/spaces/EE/pages/22183937/EE+Drawing+Documentation+Information+and+Examples

### Liam Limon, 2023-11-16

@Cameron Chapman Thank you for including the links to those. Perhaps Garrett and I can keep working off of those as we develop our template. I’m definitely happy to help with developing the process and continuing to improve. I know staffing has been an issue, but more cross functional support I think will help alleviate some of the pressure on fixing things like documentation and processes. 
I think it would be a smart idea to add Manufacturing and Quality review to the release process. I’ve been making myself available to Garrett and Nadia for review of everything we’re taking to Huntsville as well as helping Jack and Maxime review the MCM avionics box documents and I’m happy to continue to do that for future projects. Going forward for general releases we should probably direct the review to the relevant supervisor; so myself for center wing and lift, Ben N, for avionics, GCS, and Batteries, and Ben H for fuselage. For quality the reviewer would probably be Brad C.

### Liam Limon, 2023-11-16

@Cameron Chapman Thank you for including the links to those. Perhaps Garrett and I can keep working off of those as we develop our template. I’m definitely happy to help with developing the process and continuing to improve. I know staffing has been an issue, but more cross functional support I think will help alleviate some of the pressure on fixing things like documentation and processes. 
I think it would be a smart idea to add Manufacturing and Quality review to the release process. I’ve been making myself available to Garrett and Nadia for review of everything we’re taking to Huntsville as well as helping Jack and Maxime review the MCM avionics box documents and I’m happy to continue to do that for future projects. Going forward for general releases we should probably direct the review to the relevant supervisor; so myself for center wing and lift, Ben N, for avionics, GCS, and Batteries, and Ben H for fuselage. For quality the reviewer would probably be Brad C.

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20231115-170247.png | image | 128 | 2023-11-15 | listed only |
| image-20231116-201000.png | image | 109 | 2023-11-16 | listed only |
