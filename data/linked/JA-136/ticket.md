# JA-136: Convert Problem to Major Problem - Link + data loss questions

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2024-08-29
- **Updated:** 2024-12-03
- **Resolved:** 2024-10-24
- **Reporter:** Greg Fryer
- **Assignee:** Christa Meck
- **Creator:** Christa Meck
- **Fix versions:** 12/3/2024
- **Links:** relates to VXEP-540 (Recent AS150 Connectors causing intermittency and difficulty to connect and disconnect correctly and safely (AS150 Socket Issues)); relates to JA-161 (Custom Field Pruning and Consolidation)

## Description

@Christa Meck Can you verify that if I change this Problem into a Major Problem (which is appropriate) we won’t lose any data? I want to update it, and then link it to  https://jenaero.atlassian.net/browse/VXEP-444   as a child (thanks to your prior updates).

## Comments (6)

### Christa Meck, 2024-10-22

Comparing https://jenaero.atlassian.net/browse/VXEP-540 (Major Problem) and https://jenaero.atlassian.net/browse/XKIT-3008 (Problem).
Here are the differences I see when comparing MP to P.  These are not a concern as there is no data on Problem to get lost in the move to Major Problem.
- Root Cause present in MP and not in P
- Corrective Action present in MP and not P
- Severity is present in MP and not P
- Problem type is present in MP and not P
- Incident type is present in MP and not P
- Monitor type is present in MP and not P
- Monitored Flight/Event Count is present in MP and not P
- External Stakeholder is present in MP and not P


Here are the differences I see when comparing P to MP.  These ARE a concern we are now losing data during the move to Major Problem.
- Latest Status is present in P and not MP
- Asset type is present in P and not MP
- Leadership Stakeholder is present in P and not MP
- Change Type is present in P and not in MP
- Change Risk is present in P and not MP
- Customer is present in P and not MP
- Estimated Finish Date is present in P and not MP
- P/N Revision(s) is present in P and not MP
- Approvers is present in P and not MP
- Customer Tracking ID is present in P and not MP
- Engineering Change Notice (ECN) Number is present in P and not MP
- Impacted Core Subsystems is present in P and not MP
- Impacted Disciplines is present in P and not MP
- New Requirement is present in P and not MP
- Impact is present in P and not MP
- Applicable Subsystem is present in P and not MP
- Target Start is present in P and not MP
- Target End is present in P and not MP

### Christa Meck, 2024-10-24

Next I will review all tickets for data in any of these fields and then remove the custom fields that aren’t being used.  Then we can see what we are up against.

### Christa Meck, 2024-10-24

- Root Cause present in MP and not in P (175 tickets)
- Corrective Action present in MP and not P (125 tickets)
- Severity is present in MP and not P (160 tickets)
- Problem type is present in MP and not P (185 tickets)
- Incident type is present in MP and not P (185 tickets)
- Monitor type is present in MP and not P (37 tickets)
- Monitored Flight/Event Count is present in MP and not P (19 tickets)
- External Stakeholder is present in MP and not P (13 tickets)

- Latest Status is present in P and not MP (54 tickets) - 10062
- Asset type is present in P and not MP (43 tickets) - 10036
- Leadership Stakeholder is present in P and not MP (56 tickets) - 10100
- Change Type is present in P and not in MP (8 tickets) - 10005
- Change Risk is present in P and not MP (9 tickets) - 10006
- Customer is present in P and not MP (8 tickets) - 10047
- Estimated Finish Date is present in P and not MP (51 tickets) - 10101
- P/N Revision(s) is present in P and not MP (48 tickets) - 10099
- Approvers is present in P and not MP  ** This is a JSM field and shouldn’t even be on non-JSM screens!!!   (6 tickets) - 10003
- Customer Tracking ID is present in P and not MP (27 tickets) - 10114
- Engineering Change Notice (ECN) Number is present in P and not MP (108 tickets) - 10093
- Impacted Core Subsystems is present in P and not MP (38 tickets) - 10113
- Impacted Disciplines is present in P and not MP (29 tickets) - 10112
- New Requirement is present in P and not MP (6 tickets) - 10121
- Impact is present in P and not MP (11 tickets) - 10004
- Applicable Subsystem is present in P and not MP (5 tickets) - 10122
- Target Start is present in P and not MP (89 tickets) - 10027
- Target End is present in P and not MP (121 tickets) - 10028

Well… Looks like we can’t easily remove any fields.  sigh

### Christa Meck, 2024-10-24

OK now let’s ask the API for all the data and see if we “lost” anything when https://jenaero.atlassian.net/browse/VXEP-540 was changed.

### Christa Meck, 2024-10-24

- Latest Status 10062 - null
- Asset type 10036 - null
- Leadership Stakeholder 10100 - gfryer@edgeautonomy.io
- Change Type 10005 - null
- Change Risk 10006 - null
- Customer 10047 - null
- Estimated Finish Date 10101 - null
- P/N Revision(s) 10099 - null
- Approvers 10003 - null
- Customer Tracking ID 10114 - null
- Engineering Change Notice (ECN) Number 10093 - null
- Impacted Core Subsystems 10113 - null
- Impacted Disciplines 10112 - null
- New Requirement 10121 - null
- Impact 10004 - null
- Applicable Subsystem 10122 - null
- Target Start 10027 - null
- Target End 10028 - null

Long story, summarized:  The only data that was visible when this ticket was a Problem that you can no longer see after the move to Major Problem is the Leadership Stakeholder field.  You are already a watcher, @Greg Fryer so no worries on this one.

### Christa Meck, 2024-10-24

The data is still there, we just need to use the API to see it.  It’s worth noting that we should TOTALLY standardize on a set of fields that are important, consolidate where possible, and prune as many fields as we can.  Future Christa Problem.

## Attachments (0)
