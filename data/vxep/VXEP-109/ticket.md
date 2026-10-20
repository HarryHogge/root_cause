# VXEP-109: 107-101141 Air Data Pod Airspeed/Pressure Testing Setup Needs Evaluation

- **Issue type:** Problem
- **Status:** On Hold
- **Priority:** Low
- **Created:** 2023-08-24
- **Updated:** 2025-11-05
- **Reporter:** Matt Philley
- **Assignee:** Daniel Ceja
- **Creator:** Matt Philley
- **Links:** relates to ENGPRJA-63 (Build test fixture for Air Data Pod assembly PN 107-101141); relates to ENG-2122 (ADP Reoccurring Leak Issue: 107-101141); relates to ENG-1016 (Air Data Pod (PN 107-101141) Deep Dive)
- **Part Number(s):** 107-101141
- **Production Stakeholder:** Desiray Johnston
- **Other Stakeholder (as required):** Ryan Stafford
- **Problem Type:** Production Issue

## Description

Various Production Improvements have been made to the sealing and other aspects of the ADP Test Fixture like the HIL Box, but the pressure testing side of the test fixture has aged terribly and needs to be addressed.
We are seeing an increasing number of test failures that may be attributed to the test setup. We need to at a minimum refurbish the existing fixture, but long-term redesign it with more robust test criteria and a repeatable setup.
Test Procedure: 107-101141 - Final Assembly - Air Data Pod (ADP HIL) - Procedure (Doc# 111270)

Test Setup: 
[embedded: image-20230824-192128 (9ff6f971-1e42-4256-8ca6-b7bf1a396dcf).png]

Issues:
Tubing shows wear throughout setup
Micromanometer has not been calibrated since 2002
Aquarium pump is several years old and seems to be dying
red solo cup with wooden stick is not ideal
Black hose around ADP probe does not seal well
Pass/Fail criteria is in Procedure based on legacy process. No clear understanding on how these tests and values apply to aircraft conditions
Aircraft failures seem to happen at higher temperatures, but testing does not involve any temperature control or modification

## Comments (5)

### Matt Philley, 2023-08-24

@Kyle England @Noah Chavez  I created this Jira so we can add details as we have test failures as related to test fixture issues moving forward

### Matt Philley, 2023-08-24

@Desiray Johnston @Ryan Stafford @Trevor Gronner I have generated this Jira to track the ADP Test Fixture issues we have. I have also linked the other similar topics around ADP in general and the leak issue that seems to be resolved. 
We may need sub-tasks to address the specific issues if we can’t budget to address them all at once. 
Also, I highly recommend we just focus on refurbishing the existing fixture and dont get caught trying to kick off too large a project to overhaul the full thing when most of our issues might be resolved by just cleaning this up a bit.

### Matt Philley, 2023-08-24

Submitted purchase requests for the following to replace the red solo cup and piece of wood….
https://www.mcmaster.com/2766T62/ 
https://www.amazon.com/Chemical-Resistant-Steel-Lab-Stand/dp/B00HUUWYIO/ref=sr_1_3?crid=1H4NCWMDCQ9OU&keywords=lab%2Bstand&qid=1692906026&s=industrial&sprefix=lab%2Bstand%2Cindustrial%2C232&sr=1-3&th=1

### Greg Fryer, 2023-09-27

@Trevor Gronner We should discuss, and I can trigger this project when you have the bandwidth to do this based on urgency.

### Trevor Gronner, 2025-11-05

@Daniel Ceja I am going to reassign this ticket to you since I think this will fall under Production Test. This is an ancient ticket and some of this has already been improved/changed. I am not in the loop on exactly where we are at with the new ADPs, but I think most of our leak issues have been reduced considerably since this ticket was originally created. No immediate action needed, but I was going through old open tickets and I figured it was worth keeping you in the loop on this open ticket.

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20230824-192128 (9ff6f971-1e42-4256-8ca6-b7bf1a396dcf).png | image | 1444 | 2023-08-24 | listed only |
| image-20230824-192128.png | image | 1444 | 2023-08-24 | listed only |
