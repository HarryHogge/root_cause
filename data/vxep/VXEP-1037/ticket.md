# VXEP-1037: Record power return to case findings of silvus enclosure. Evaluate and test separating power return from case. May be required for Havoc.

- **Issue type:** Sub-task
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2025-02-18
- **Updated:** 2026-03-30
- **Resolved:** 2026-03-30
- **Reporter:** Cameron Chapman
- **Assignee:** John Gober
- **Creator:** Cameron Chapman
- **Parent:** VXEP-1034 VXE 734 Smoking Gimbal

## Description

While investigating VXEP-813, I discovered a probable path to ground through the body of the Silvus. 
Notes from VXEP-813 Test: Test 7 VXEP-813 E140Z G2 Ground Loop 18 FEB 25.docx
Related:
https://jenaero.atlassian.net/browse/VXEP-813

## Plan

@Hayden Jeanor @Jeremy Kostel @Carl Graf @Tom Westrich we will need to test all assemblies for similar issues before implementing the Havoc bonding architecture. 

Cam comments in bold. 
- I think we should start with verifying the problem on a radio that hasn't crashed.
- Verify ground path from Silvus ODU to Silvus body on a radio that hasn’t been crashed. Good idea. Compare on a few radios if avaialble to confirm consistency.
- Quantify and record resistance to ground through fuselage, radio and harness - back to battery if possible. Please record findings and test plans in documents saved to a shared sharepoint and add the link to the JIRA issue. Since fuselages aren't purposefully bonded in B30, you may get varying results. Test on a few. This will need to have a B40 plan, as we are planning on purposefully bonding cases and structures for better RF connection.
- Consult with our RF expert (I’m told this person is Wes) on whether breaking the ground connection between the radio and the fuse will affect RF performance. I think it will.
- Consult with Silvus on same (if necessary)
- Engage Mechanical to design a non-conductive mounting solution for Silvus. I do not think we want to do this. Better to fix the issue. It is not creating known issues currently on B30.
- Build and test new non-conductive mounting. See above.
- Ground Testing
- Flight Testing

## Issue Status

25 FEB 25 Further testing in HSV on hold until an aircraft is made available.  GS / FLOPS currently TDY with all HSV assets for five weeks.

## Comments (0)

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| Picture2.jpg | image | 1338 | 2025-02-24 | listed only |
| Picture3.jpg | image | 884 | 2025-02-24 | listed only |
| Picture4.jpg | image | 913 | 2025-02-24 | listed only |
