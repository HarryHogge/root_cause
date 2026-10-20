# VXEP-1956: VXE 880 MCM Reset inflight after gimbal power cycle

- **Issue type:** Incident (8D)
- **Status:** D4 - Investigating Root Cause
- **Priority:** High
- **Created:** 2026-07-09
- **Updated:** 2026-10-07
- **Reporter:** Alexander Alan Arnold
- **Assignee:** David Grosher
- **Creator:** Alexander Alan Arnold
- **Labels:** Hardware, Redwire, Weekly-incident-tracker
- **Links:** relates to VXEP-1315 (B30 Systemic MCM Resets due to payload power); relates to VXEP-1890 (VXE 902 - user power cycled aux 1&2 simultaneously, and lost comms with the A/C for ~2 minutes. CHAOS payload); relates to MS-1684 (VSM: Accommodate MCM Restarts in Flight); relates to VXEP-2005 (VXE 966 MCM reset led to uncommanded climb ); relates to RMA-1029 (VXE-880 RMA 260527-2)
- **Customer:** Redwire
- **Vehicle Tail Number:** VXE 880
- **Vehicle Configuration:** VXE 30 ADV NAV, Battery, e95, Orbital Sharpshooter payload
- **Corrective Action:** https://jenaero.atlassian.net/browse/VXEP-1315
- **Root Cause:** https://jenaero.atlassian.net/browse/VXEP-1315
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround
- **Executive Summary:** Engineering exploring approaches on how to handle VSM/MCM resets in flight; probable cause Software Issue

## Description

A similar issue happened today while flying in North Carolina with an internal asset. The Operator was experiencing gimbal issues while in flight. The Operator turned off AUX 1 through the Payload Power menu, and lost communication with the airplane shortly afterwards. The Operator got communication of the airplane again and noticed the entire flight plan disappeared. The Operator was unable to upload a new mission or import a saved mission, the error displayed was “reference altitude has not been set”. The Operator tried to fly on the web browser but had the same issue. It appears the MCM reset and/or the VSM was not operating properly. The Operator was able to perform “Loiter Here Now” commands and was able to command “Land PLZ”. Eventually the Operator commanded “Land PLZ” and the vehicle safely recovered. I have attached the AAR and two front end logs to this ticket. 

Aircraft configuration:
B30 Adv Nav (880)
Heavy Payload Main Battery 
OGCS 1.4.1 using the Native App (6.6.1 firmware)
E95 and Orbital Drop Payload System (attached to top AUX Port)

## Plan

Double check command log. Aux 1 off command (SB lower payload/E95). Surprising. I would have guessed Aux 2 off (hood+lower) would be more likely. Could they have turned off then on right after?

## Comments (4)

### Anthony Hansen, 2026-07-09

@Craig Burton @Jonathan Wes Strong

### Craig Burton, 2026-07-09

The restart of the VSM in flight, whether due to an MCM power cycle or not, is not a supported contingency at this time.  In this case, it was a full power cycle and reboot of the MCM, in which all services (namely OGCS/VSM) were started automatically.  Fortunately, the operators pursued the best corrective action in this scenario, because the landing patterns (indeed all routes) were still loaded in the AP and actionable.
Going forward, there are several development approaches that can be taken to restore service after a VSM restart and/or MCM power cycle (that would also impact OGCS/AION/etc.).  We will capture and discuss these in [MS-1684] MCM: Explore Approaches to VSM and/or MCM Restarts in Flight - Jira

### Anthony Hansen, 2026-07-09

@Alexander Alan Arnold

### Alexander Alan Arnold, 2026-07-13

added screen recording and logs from bench testing recreating issue just by cycling gimbal power

## Attachments (7)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_V880_B30N_20260709T135535Z In Air reset 1.zip | archive | 39233 | 2026-07-09 | listed only |
| frontend-native-0023-2026-07-09 1.bin | other | 25286 | 2026-07-09 | listed only |
| [frontend-native-0023-2026-07-09 1.jsonl](attachments/63367_frontend-native-0023-2026-07-09%201.jsonl.md) | text | 2 | 2026-07-09 | converted |
| AAR_V818_B35X_20260709T184132Z (9277d187-90af-417e-8a68-c71adcf1f066).zip | archive | 2783 | 2026-07-13 | listed only |
| AAR_V818_B35X_20260709T184132Z.zip | archive | 2783 | 2026-07-13 | listed only |
| AAR_V818_B35X_20260709T190341Z (809de795-397e-4b64-83c2-243561cd46b8).zip | archive | 5636 | 2026-07-13 | listed only |
| AAR_V818_B35X_20260709T190341Z.zip | archive | 5636 | 2026-07-13 | listed only |
