# JA-126: Latvia JIRA access with new domain

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2024-07-24
- **Updated:** 2026-04-13
- **Resolved:** 2026-04-08
- **Reporter:** Cameron Chapman
- **Assignee:** Christa Meck
- **Creator:** Cameron Chapman
- **Components:** Atlassian Software Maintenance/Configuration, Compliance
- **Fix versions:** 4/13/2026
- **Parent:** JA-174 Work with IT on these
- **Epic Link:** JA-174

## Description

@Greg Fryer @David Grosher @Mike Gomez do we want to establish access for Latvians to use Jira with their new email addresses? I don’t think they can currently access it with their new email addresses, but Jira access would be useful for payload troubleshooting, improvements, etc. 

To ensure export compliance, would the best method be to establish a separate project meant for interacting with them, so that we don’t have to scrub the rest of our projects? 
@Christa Meck

## Comments (6)

### David Grosher, 2024-07-24

@Cameron Chapman @Greg Fryer @Mike Gomez @Christa Meck Given many of our current efforts, we can’t provide the Latvian team access to our Jira system without violating ITAR restrictions. If they have access it should be removed and they should be provided a partitioned or separate account.  Once that is complete then we can consider a method collaborate on projects that aren’t covered by ITAR restrictions.

### Greg Fryer, 2024-07-24

@David Grosher We’ve got issue based security turned on (Padlock on the upper right). So we can group folks by function and control who has access to what. That’s how we blocked out the exisitng LM folks without turning off their access immediatley.
We’d need to robust-ify that a bit (limit who can change security level), but I’m sure @Christa Meck can do that too.
I don’t think the need is urgent, the Latvian crew wasn’t driving to use Jira, so it can wait. (I believe)

### David Grosher, 2024-07-24

@Greg Fryer Dan Lloyd still has access to the system so I don’t think we have effectively scrubbed it. And I don’t think the padlock will be used reliably to ensure we are compliant with ITAR restrictions.  Access needs to be at the system level and controlled by administrators not at the user level.

### Christa Meck, 2024-07-29

I’ve had opening discussions with @Sam Jones on this.  If we’ve hit the point where we need to move forward on this work, we’ll set it in motion.

### Christa Meck, 2024-08-01

Moving to JA project.

### Christa Meck, 2026-04-08

Non-US access to Atlassian apps has been revoked for quite some time now WITH THE EXCEPTION OF the Canadian Team.
The Canadian Team has their own Jira space and their own Confluence Space.  What they can and can’t see inside both tools is limited by:
- Group based permissions set at the space level in Jira.
- Group based permissions set at the space level in Confluence.
- Individual page restrictions set by the page author on certain pages in Confluence.

I expect there will be additional configuration Coming Soon(tm) when we go to the FedRAMP instances.  (In the Quote process now.)

## Attachments (0)
