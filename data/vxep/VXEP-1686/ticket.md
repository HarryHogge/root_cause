# VXEP-1686: VXE 966 Intermittent Loss of communication to Xcomm

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2026-01-30
- **Updated:** 2026-07-13
- **Resolved:** 2026-07-13
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Samuel Lopez
- **Creator:** Alexander Alan Arnold
- **Labels:** GS_Closed, RCCA, Weekly-incident-tracker
- **Links:** relates to RMA-920 (VXE-966 RMA 260206-3); relates to XKIT-5219 (AC 966 - Flight Test - Power bus fault); relates to VXEP-1951 (VXE 996 RR Motor detached from boom)
- **Customer:** Redwire
- **Vehicle Tail Number:** VXE 966
- **Vehicle Configuration:** VXE 30 ADV NAV OGCS, Battery,
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

During testing at IVY sting we have seen communication drop out from the aircraft while conducting ground testing. I can still access the Silvus GUI for the aircraft but I cannot access OGCS or the Xcomm page. 

This happened over Silvus and a wired connection through the AUX 2 port. 

We will not fly this aircraft again after seeing this issue multiple times.

## Plan

- Aircraft sounds repaired and ready for RMA.
- RMA requested new radio.


Radio Troubleshooting. 
- Started group chat: 966 Investigation Radio Issue | Group Chat | Microsoft Teams
- Test 
- Reflashing radio and other settings.
- with alternate IPCOMM
- Contact silvus if not successful.
- If repaired, determine plan for radio. (iron bird, internal asset build, etc).

## Issue Status

From RMA: we didnt see any intermittent issues with plugging into the xcom. we were able to access the xcom page. we were able to get to the radios ipcomm page. we were not able to get to the silvus virtual ip address assigned to the vehicle. we were able to get onto the silvus default 172.x.x.x network. we changed the virtual ip to tail #1 address and got it to connect, but when we swithced back to  its assigned vIP it wasnt working. we swapped with a known good radio, and set the vIP to the assigned tail # with no issues

## Comments (7)

### Alexander Alan Arnold, 2026-01-30

@Craig Burton FYSA

### Craig Burton, 2026-02-11

@Alexander Alan Arnold Were the problems encountered on Jan 29th or 30th?  I’m just trying to narrow down the amount data to look through.

### Cody Smisek, 2026-02-11

@Craig Burton I just added a big zip of zip of zip folder pulled from 966. Should have at least 1 of the dates we’re looking for. @Alexander Alan Arnold

### Scott Lovett, 2026-02-12

Affected flights were: Jan 26th, 27th, & Feb3

### Ronnie Baker, 2026-02-17

@Craig Burton Intake complete by RMA, ready for you to pick up to continue investigation. 
This is a high priority RMA.

### David Grosher, 2026-02-17

@Alexander Alan Arnold @Scott Lovett @Ronnie Baker We don’t currently have the bandwidth to prioritize this asset. I also don't think we can recreate the congested RF environment in which the issue was observed.

### Scott Lovett, 2026-02-17

@David Grosher Ok, i’ll discuss with the team. Thanks!

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_V966_20260130T195354Z.zip | archive | 35425 | 2026-01-30 | listed only |
| [mcadmin@eamcm0966~$ ip route.txt](attachments/41528_mcadmin@eamcm0966~$%20ip%20route.txt.md) | text | 5 | 2026-01-30 | converted |
| archive_20260211_231037.zip | archive | 119769 | 2026-02-11 | listed only |
