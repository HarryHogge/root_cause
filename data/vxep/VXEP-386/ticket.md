# VXEP-386: Develop Replacement for AS150 Connections

- **Issue type:** Initiative
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-09-18
- **Updated:** 2026-05-06
- **Resolved:** 2026-05-06
- **Reporter:** Cameron Chapman
- **Assignee:** Scott Stuckey
- **Creator:** Cameron Chapman
- **Parent:** SP-206 Improve Power Connector, Contacts, and Signal Connectors
- **Links:** relates to VXEP-385 (New Connectors and Contacts, Overall Requirements Review); is duplicated by XKIT-760 (Main AS150 replacement issue-Develop new battery power connectors for Havoc Block 5); duplicates ENG-1805 (Improve High Power Contacts and Connectors); relates to XKIT-1716 (SB40 Vehicle Power Switch); relates to VA-573 (Poor Quality/higher impedance plating on AS150 power contacts - Containment and Corrective Action); relates to VXEP-326 (AS150 pin connectors diagnosing the reason the parts are OOS when assembled (could be pin dimensions, threads too deep, etc).  Identify long term C/CAs and short term workarounds. Ex 107-102189 114-106508)
- **Part Number(s):** 107-102264 114-106085 100-102573 100-102570
- **Issue Status:** Closing as duplicate

## Description

Files: AS150 Replacement
AS150 Replacement RVTM.xlsx

## Sprint

VXE-1 Cameron's Team 9-17, VXE-1 Electrical-8, VXE-2 Everything Else 2024-03, VXE-1 Electrical 10/29, VXE-1 Electrical 11-20-12/10, VXE-1 Electrical 10/9, VXE-1 Electrical-7

## Comments (8)

### Cameron Chapman, 2023-09-22

About replacing contacts: 
It will be pretty easy to test if a soft start is needed or not. Connect all 4 ESCs to power supply or battery power and see if there is a spark or evidence of one. The battery would create a bigger spark usually, depending on the capacitance of the battery vs the big cap on the power supply.
 
It would be awesome if anti-spark wasn’t required for these ESCs. We would get better current capacity, reliability, and could more easily upgrade to a better contact when time allows. I think we aim to replace these contacts for Block 35, but probably not x-kit unless needed.
 
We will either need to ensure ESCs don’t require soft starts, or introduce a soft start circuit before getting rid of the anti-spark contacts.
 
Thank you,

### Connor Peebles, 2023-10-16

I added subtasks to this to evaluate replacement candidates. As we come up with other candidates, we can add them to the table in Description.

### Connor Peebles, 2023-11-20

I’m going to pivot this into creating a major task, replace AS150 contacts

### Cameron Chapman, 2025-02-11

@Connor Peebles  please link the new task before closing. We should have a task for VXE30 and Havoc. Reopening until then.

### Connor Peebles, 2025-02-11

@Cameron Chapman My recollection serves that we’re not replacing VXE30 contacts. Looks like the new contacts for Havoc is captured here: https://jenaero.atlassian.net/browse/VXEP-385  (in relates to).

Please verify that replacing the VXE30 contacts is a project we were actually going to pursue.

### Cameron Chapman, 2025-02-11

@Connor Peebles If we plan to keep selling VXE30s, I think we should plan to replace the contacts when able to. They have caused a lot of crashes. If not, then we should update relevant Jira CAs to say something like (CA=upgrade to havoc). @Greg Fryer do you have any thoughts/directions wrt this? @Connor Peebles

### Greg Fryer, 2025-02-12

@Cameron Chapman We should collect it under it’s own project. You are correct our primary CA is for folks to upgrade to Havoc. If that doesn’t happen (for whatever reason), there will be a project to push the Havoc design back into the standard, e.g. “Block 35”. That would be an extensive project, and likely only be possible in the factory. e.g. solving the problems AND maintaining some level of hardware compatibility is likely impossible (though I am open to ideas).

### Connor Peebles, 2025-02-12

My vote is that we close all previous tickets relating to VXE30-AS150 replacement. When we’re ready to proceed with Greg’s below direction, then we’ll open up new projects.

## Attachments (0)
