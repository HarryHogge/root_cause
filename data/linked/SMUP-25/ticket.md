# SMUP-25: Update all Software generated Warnings/Cautions/Alerts and VTOL Messages

- **Issue type:** Sub-task
- **Status:** Canceled
- **Resolution:** Not Verifiable
- **Priority:** Low
- **Created:** 2024-05-30
- **Updated:** 2025-03-16
- **Resolved:** 2025-01-15
- **Reporter:** Dana Holley
- **Assignee:** Dana Holley
- **Creator:** Dana Holley
- **Fix versions:** New beginnings!
- **Parent:** SMUP-3 Create new Ops Manual Rev
- **Links:** relates to VXEP-342 (VXE 439 The autopilot has detected one or more of its VTOL sensors have failed warning)

## Comments (5)

### Dana Holley, 2024-05-30

I’m discovering that that our Pop-Up and VTOL messages that appear in the flight software aren’t being captured in our Operations manual. @Michael Berger can you provide a full detailed list these messages so I can conduct a gap analysis?

### Michael Berger, 2024-05-30

@Dana Holley A full detailed list of these messages does not exist.
A good number of the messages are generated in the GCS when the vehicle reports that something has failed, but does not say specifically what failed.

### Dana Holley, 2024-05-30

@Michael Berger Understood. I know we use very general and broad messages, so we can’t capture specifically what failed, but do we have a list of those types of messages?

### Michael Berger, 2024-05-30

@Dana Holley I do not know of any list of messages. Creating a list would likely require searching the code for MessageBox function calls and message strings.

### Dana Holley, 2025-01-15

Cannot produce information for request.

## Attachments (0)
