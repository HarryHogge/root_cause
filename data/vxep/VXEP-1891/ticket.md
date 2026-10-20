# VXEP-1891: VXE 592 experienced several losses of GPS.

- **Issue type:** Incident (8D)
- **Status:** D4 - Investigating Root Cause
- **Priority:** Highest
- **Created:** 2026-05-15
- **Updated:** 2026-09-02
- **Reporter:** Michael Lindsay
- **Assignee:** Eric Brewer
- **Creator:** Michael Lindsay
- **Labels:** GS_Closed, MOLSON, Qaulity, RCCA, Weekly-incident-tracker
- **Links:** relates to RMA-1037 (VXE- 592 RMA 260604-1)
- **Customer:** MOLSON
- **Vehicle Tail Number:** 592
- **Vehicle Configuration:** VXE30 Adv Nav, Battery Configuration,
- **Problem Type:** Discovered Issue
- **Severity:** 1 - Flight Critical
- **Executive Summary:** Waiting on test flights after RMA complete to validate root cause. Probable cause Software.

## Description

Original Title: VXE 592 While conducting training flights for Molson 6, the final flight of the day experienced several losses of GPS
The aircraft last GPS several times while conducting a training flight, All the GPS lost warning came during the end of the training flight.  The first one was prior to the aircraft going to IP 1 and it also lost GPS during the landing.

## Comments (17)

### Michael Lindsay, 2026-05-15

@David Grosher We had the GPS lost yesterday during a training event.  would you be able to have a look at this.

### David Grosher, 2026-05-15

There appears to be an issue with the Novatel losing connection with the XCOMM resulting in the receiver being reset. This was observed recently on a few other aircraft. 

```
Long Configuration Times
[19:10:00.936 1021.936] :NOV: Configuration Complete

Two Commanded Resets in Flight
[19:34:14.801 2475.801] :NOV: Heartbeat timeout 30035
[19:34:14.802 2475.802] :NOV: Resetting OEM7700
[19:34:15.802 2476.802] :NOV: Waking Up OEM7700 after reset

[19:37:58.806 2699.806] :NOV: Heartbeat timeout 30030
[19:37:58.807 2699.807] :NOV: Resetting OEM7700
[19:37:59.807 2700.807] :NOV: Waking Up OEM7700 after reset
```
@Michael Lindsay @Eric Brewer

### Eric Brewer, 2026-05-15

@Michael Lindsay if we have the aircraft available I’d like to request that we pull debug logs from the NovAtel.  It looks like both xcomm and vtol lost communications with the unit around the same time which would typically point to an unexpected reset of the novatel.

### Michael Lindsay, 2026-05-15

@Eric Brewer I have uploaded the debug logs from the Novatel on 592

### Eric Brewer, 2026-05-15

@Michael Lindsay thank you.  It shows a GPS receiver crash occurred, we’ll need to send the data over to Novatel.  @David Grosher FYI - we probably need an RMA.

### Eric Brewer, 2026-05-17

Hi Michael,
Novatel is also requesting these two logs from the receiver:
EDRDATA/SDDRDATA

I believe ‘log edrdata’ and ‘log sddrdata’ would provide them.  Let me know if you need me to walk you through logging these with putty again.

### Michael Lindsay, 2026-05-19

@Eric Brewer Hi Eric,
I will get the additional information as soon as i get back to Ottawa as I drop off the aircraft on the weekend.

### Michael Lindsay, 2026-05-26

@Eric Brewer I have uploaded the new data that was requested let me know if you need anything else.

### Eric Brewer, 2026-05-28

@Michael Lindsay thanks.  Based upon feedback from NovAtel that receiver crash is old and occurred before October of last year.  Given that I’m not sure what caused xcomm to lose communications with the receiver.  Reviewing logs in a bit more detail to determine next steps.

### Michael Lindsay, 2026-06-26

@Eric Brewer I uploaded the order confirmation with the auth code, is this I will will require or do I have to download any firmware as well.

### Eric Brewer, 2026-06-26

@Michael Lindsay just the auth code is required.

### Michael Lindsay, 2026-06-26

@Eric Brewer I have attached the AAR, I power cycled the aircraft and let it run for approx. 30 minutes. @Lauren Velasquez @Drew Hildreth FYSA the licence has been installed on 592.

### David Grosher, 2026-08-10

@Eric Brewer Do you need more data here? Or have we exhausted all potential avenues for investigation?

### Eric Brewer, 2026-08-10

@Michael Lindsay did this one return to flight after installing the license?  @David Grosher FYI.  This one was missing the lua license which I believe drove more content on the connection that usual.

### Michael Lindsay, 2026-08-11

@Eric Brewer 592 has not flown yet, the cable for the main battery got chafed to the wire so it is in transit to Huntsville for repair.  It will not be flown until we receive it back.

### Eric Brewer, 2026-08-11

@Michael Lindsay got it. We can keep an eye on the novatel connection when we do system checkouts during the RMA, but I suspect after the license was installed we likely won’t have more issues. @David Grosher FYI.

### David Grosher, 2026-09-01

@Drew Hildreth @Michael Lindsay This is on hold from our perspective while we wait confirmation that the LUA license resolved the issue.

## Attachments (7)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 592Novatel | other | 138 | 2026-05-15 | listed only |
| T115_V592_260514_121350_pack.zip | archive | 2644 | 2026-05-15 | listed only |
| Novatel592_additional_data | other | 6436 | 2026-05-26 | listed only |
| Novatel ver 2 | other | 4 | 2026-05-28 | listed only |
| [XCEVLOG.txt](attachments/58963_XCEVLOG.txt.md) | text | 101 | 2026-05-28 | converted |
| [Order Confirmation OM - 4757476 25-06-2026 10-18.pdf](attachments/63153_Order%20Confirmation%20OM%20-%204757476%2025-06-2026%2010-18.pdf.md) | pdf | 712 | 2026-06-26 | converted |
| T115_V592_260626_121556_pack.zip | archive | 10173 | 2026-06-26 | listed only |
