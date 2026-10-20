# Risk Assessment - AC 604 and 406 CPU Loading and Mag Issue Crashes, Use As Is - 24.02.21.pdf

Attachment 18890, pdf, 439 KB, added 2024-02-21 by Matt Philley.

## Page 1

Problem Information
Top Assembly PN
Point of Contact Date Issue Found
Problem Statement
Suspected Cause
Proposed Action
Risk Assessment
Category Category Descrip Low Med High Comments
Quality
Does this impact the Ability for the 
product to meet Quality 
requirements?
Example:
CofC, Inspection Points, Customer 
Specific Reporting, etc.
No Impact to Product 
Requirements
Impact to Internal 
Product Requirement, 
but does not Impact 
Impact to External 
Product Requirements, 
Certification, and/or 
Qualification
Flight Test does not have parameters to check for CPU 
loading, so we cannot monitor this directly, but we 
have an option for an "override" which could allow 
the aircraft to land safely if this happens again (See 
JIRA).
Unlikely to be hardware related to something we 
could visually detect based on AC 406 which has had 
many flights and is ~1 year old.
Engineering/
Function
Does this impact the Ability for the 
product to properly function now 
or meet design/Engineering 
requirements?
Example:
Impact to SCO checkout, Flight 
Test, Customer Interaction with 
Equipment, etc.
No impact to Product 
Function
Inconvenience to Product 
Function
Product not able to 
Function properly with 
this issue
Do not have finalized root cause, but based on 
investigation so far signs are pointing to this being a 
Software Issue that is caused by legacy code decisions 
that are being actively investigated, understood, and 
improved with each release iteration. There have 
been no recenty code changes that would have 
created this condition it is part of the same code we 
have been flying since the last major update.
Both aircraft did fail due to CPU loading and bad 
Magnetometer data even though the Magnetometer 
hardware was fine, which supports this being a 
software issue.
Based on this the risk to new Production versus 
Fielded Aircraft is essentially the same and that risk is 
"known" and accepted based on our general decision 
to continue with Production and Flights given the 
other known Software opportunities for 
Improvement.
Delivery
Does this impact the current 
Production Schedule or Ability to 
Ship On Time?
No Impact to Production 
Schedule
Impact to Internal 
Production Schedule, but 
no Delivery impact or 
manageable impact
Production Line Stop and 
will Impact On Time 
Delivery
10+ aircraft for Feb already are thru Flight Test and 
are getting ready for invoicing/Source unless we 
implement a hold.
We have 8+ aircraft still needing Flight Test for Feb 
deliveries
Customer
Does this impact something the 
Customer will see and/or interact 
with related to the Product? 
Does this impact any Airworthiness 
Requirements?
No Impact to anything 
Customer will see or is 
involved in.
Inconvenience to 
Customer, but 
manageamble with clear 
communication
This issue will cause a 
Customer Complaint
Delivery schedule impact… system delivery impacts…
RISK ASSESSMENT FORM
Purpose: A template to document critical problem details, facilitate a risk-based discussion for cross-functional issues, capture concerns, and establish decisions.
Determine if these 2 incidents pose some risk to additional crashes for Flight Test and/or Flight Operations.
Determine if the suspected cause is something that is worth holding for resolution or is this just an assumed risk until we dig deeper 
into control software to correct legacy "foundational" issues.
VXE30 Aircraft
TBD
107-102560
1/30/2024
Qty 2 aircraft have crashed with a similar cause within 2 weeks of one another. 
On Jan 30, 2024 AC 604 crashed during Flight Test at SLO.
Initial investigation per JIRA VXEP-263 showed that "Problem appears to be due to excessive CPU load leading to use of the internal 
magnetometer which is unreliable when the VTOL system is active."
On Feb 8, 2024 AC 406 crashed at AEWE
Initial investigation per JIRA VXEP-275 states "Problem appears to be due to excessive CPU load leading to use of the internal 
magnetometer which is unreliable when the VTOL system is active."
Initial suspected cause on AC 604 (SLO) was thought to be due to manaully triggered Burst Data feature that we have been activating 
during Test Flights to collect more data for Engineering during VTOL. This additional data could "overwhelm" the CPU and cause the 
excessive CPU load.
Based on this suspected cause and the fact customers cannot activate this we decided to not halt flight test or deliveries.
However, AC 406 did not have this Burst Data triggered. So, now the risk to fleet and flight test is uncertain.

## Page 2

Service
Does this impact the ability to 
Service or Maintain the Product?
No Impact to the 
Serviceability or Service 
Lift of the Product
Inconvenience to Service, 
but can be resolved with 
a Service Bulletin and/or 
Service Kit
Will require recall of 
Product
High impact for all service whenever an aircraft 
Results
Risk Evaluation (Highest Score):
Low
Medium
High
Disposition/Decision:
Action Notes:
Actions
Owner
Matt Philley
Artis Bertulis
Artis Bertulis + ??
Participants
General Manager Production Engineering Quality Customer Rep.
Participants Ryan S Kyle D Dave G Marc R Pat W
Date 2/20/2024 2/20/2024 2/20/2024 2/20/2024 2/20/2024
RISK ASSSESSMENT FORM, DOC# TBD - DRAFT 24.01.25
Action
Capture risk notes and send out to attendees.
Attach to JIRA tickets and NCR
Draft an instruction on what we could potentially do to save an 
aircraft if this were to happen again during Flight Test based on 
Dave Grosher's comment
Send and "train" Flight Ops team on that instruction so they are 
also aware about how to recognize the issue and what can be 
done to potentially save an aircraft that has this issue. 
Status
N/A
Continue Production and Deliveries as-is.
Based on the investigation so far the issue is software related, however our existing software does not collect the data needed to fully 
understand the detailed software interactions that ultimately resulted in the crashes, but this does not add "new risk" to our "baseline 
risk" that is so far accepted due to our legacy software "technical debt".
The next software release will provide additional data collection and improve the ability for Engineering to be able to investigate 
incidents like this more effectively. 
High, but this issue poses no new risk beyond what has already been accepted for the past 1+ year that we have known about legacy 
code issues with this VXE30 Program
NCR Dispo and attach this completed form. Close Issue, No other follow-up needed
NCRs needed, POC needs to be responsible for actions/owners to resolve issue and communicate with team. Action tracked in MRB Meeting(?)
8D required to manage the larger investigation and ensure issue is getting adequate resource to solve it
