# VXEP-844: VXE724 VTOL Climb Abort Lift System Fault

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed, but added to Bermuda Triangle List
- **Resolution:** Cannot Reproduce
- **Priority:** Medium
- **Created:** 2024-12-23
- **Updated:** 2026-09-23
- **Resolved:** 2025-10-28
- **Reporter:** Cody Smisek
- **Assignee:** Jason Scherer
- **Creator:** Cody Smisek
- **Links:** relates to VXEP-723 (VXE 724 MCM reset when changing HLB, other potential issues); relates to FS2-2854 (Jason's Open Investigations); relates to VXEP-1315 (B30 Systemic MCM Resets due to payload power)
- **Vehicle Tail Number:** 724
- **Vehicle Configuration:** preMAGNSS
- **Incident Type:** Squawk
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

NCR linked here VTOL Land odd decent - Detail NCR
From NCR dated Oct 2024
REF NCR 4511:
AC 724 had 2 flights previously but the FLOPS team decided to re do the flights due to the previous NCR's on the AC.
On the first flight of the day the AC climbed normally. On transition the AC froze SA camera for an extended period of time and the VTOL window said that VTOL land was not okay (in red). after 10-20 ish seconds it went back to green.
The transition back to VTOL on landing was normal and it descend to 100ft ish AGL normally. At 100ft AGL the vehicle slowed its decent to (guess of 3ft/s). Normally this happens at 10-20FT agl where the LRF activates. it descended to 50sh ft at that speed and then accelerated to normal decent to the 10-20ft AGL and then slowed again.
This is abnormal and usually does not happen (guess is something with the LRF happened but not sure).
It was also noted that the VTOL control window said there was a VTOL climb abort, lift system fault after it was in fixed wing flight.
AAR and picture of VTOL control window attached.

## Issue Status

6.3.4 Software / Xcomm 4.69V / VTOL 1.55.03 / FWAP 6.05p

Data stored here VXEP-844 VXE724 VTOL Climb Abort and WDT
Compiling list of NCRs and short description
NCR4450: AP Failed to reset during launch wizard. Craig found duplicate cron entries and removed from MCM. Issue resolved. 
(with different CW) NCR4562: VTOL GPS count low. Vehicle position incorrect on GCS. Resolved by updating to 1.55.
NCR4688: Aft green blinker INOP. Removed/replaced and working. 
NCR4604: MCM power cycling (VXEP-723)
NCR4436: No video from forward SA Cam. ADP removed and replaced. 
NCR4377: Network connection between xcomm and SLA intermittent. Unable to reproduce issue.

## Comments (7)

### Cody Smisek, 2024-12-23

This center wing has been sitting in engineering area untouched for a few months. I can take a quick stab at the data but based on current description, likely unable to determine cause without software support.

### Cody Smisek, 2024-12-23

2x WD 08:26 & 08:33

[embedded image-20241223-200740.png]

### Cody Smisek, 2024-12-23

lrfFusion is offset
[embedded newplot (38)-20241223-201709.png]

### David Grosher, 2024-12-23

VTOL WDT on v1.55.03 during flight 241004_093251
trace: func(0) system 6 indicates that simple_tlb_refill_exception happened twice, once during flight as it transitioned to FW flight. This bird has had a number of NCRs registered against it, so in terms of hunting for a cause that may be a good place to start, if I remember correctly there were networking issues on this bird.  This is the only known WDT to have occurred on this version of software. 
@Scott Hunter @Cody Smisek FYSA

### Cody Smisek, 2025-01-07

@David Grosher do you need any further assistance from me on this one?

### David Grosher, 2025-01-07

@Cody Smisek No, I’ll have the SW team look at it.

### David Grosher, 2025-02-18

Changed to Sev-2. There were many NCRs and this particular wing was marked as scrap for engineering to investigate. It is unlikely that this bird is surfacing a systemic issue that could result in a critical failure across the fleet.

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| Media (40).jpg | image | 416 | 2024-12-23 | listed only |
| T95_V724_240926_121928_pack (1).zip | archive | 1890 | 2024-12-23 | listed only |
| T95_V724_241004_093251_pack.zip | archive | 2353 | 2024-12-23 | listed only |
| image-20241223-200740.png | image | 56 | 2024-12-23 | listed only |
| newplot (38)-20241223-201709.png | image | 62 | 2024-12-23 | listed only |
