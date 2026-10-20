# VXEP-141: VXEP-140   Sparking on boom connection of 565 Identify C/CA

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2023-10-10
- **Updated:** 2023-11-09
- **Resolved:** 2023-10-11
- **Reporter:** Cameron Chapman
- **Assignee:** Connor Peebles
- **Creator:** Cameron Chapman
- **Links:** blocks VXEP-140 (Sparking on boom connection of 565)

## Description

AC 565 - Lift Boom Connector Scorch Marks

## Comments (3)

### Connor Peebles, 2023-10-11

- Answers to the fried ESC can be seen here Rear left lift motor ESC fried *Note this one was completely destroyed and was found to be a build quality issue.
- The sparking on the boom connector for this plane was noted after a replacement to that previously destroyed ESC was installed. *Note this issue and the one mentioned above are different issues

Cause: The soft-start circuit of the Lift ESC barely works if the connector is plugged in quick and level enough to attain good surface contact before the soft-start circuit finishes its action. It is expected that hot-swapping the booms will lead to arcing of the EC5 contacts because of this. Even if the arcing may be imperceptible, an in-rush current and sparking will most likely still happen.
Corrective Action: is for SCO to follow the Manual when it comes to attaching the booms: The booms are to be connected before the HLB is plugged in.
@Matt Philley @Cameron Chapman @Carson Buckley 
Closing this ticket.

### Cameron Chapman, 2023-10-11

@Connor Peebles reopening. Please link and assign corrective action tasks to the parent VXEP before closing this one. Ok to close after.

### Connor Peebles, 2023-10-11

CA created and assigned to prod engr supervisor Trevor Gronner, link in parent VXEP of this task
[VXEP-144] VXEP-140 Sparking on boom connection of 565 CA: When creating SCO procedure, follow manual during boom installation - Jira (atlassian.net)
closing this task

## Attachments (0)
