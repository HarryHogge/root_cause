# XKIT-5525: Updated JST Spec Issue 110-115192

- **Issue type:** Problem
- **Status:** Document C/CA
- **Priority:** Highest
- **Created:** 2026-06-23
- **Updated:** 2026-07-20
- **Reporter:** Jeremy Kostel
- **Assignee:** Matt Philley
- **Creator:** Jeremy Kostel

## Description

V1041 was fitted with a new ESC (SN ES-107697) and exhibited behavior consistent with a loss of CAN communication (ESC appeared unresponsive to commands). Initial troubleshooting identified intermittent continuity on CAN H, which could be induced by manipulating the ESC harness.
Further investigation required removal of adhesive heat shrink covering the JST connector. During this process, it was discovered that the CAN H conductor had pulled out of the JST crimp. After bypassing the JST and hardwiring directly, ESC functionality returned to nominal, confirming a connector-level failure.
Subsequently, the motor failed to home. Inspection of the ESC hall sensor JST revealed the same issue: conductors pulled out of their crimps. Again, direct hardwiring restored normal operation, confirming a second JST crimp failure.
Review of crimping specification (Doc #110-115192) revealed a change implemented on 3/11/2026:
- Previous method: Clear, non-adhesive heat shrink crimped within the insulation support wings (providing strain relief)
- Current method: Removal of this heat shrink from the crimp area

This change has introduced multiple risks:
- Loss of proper strain relief, shifting load to small conductor strands
- Presence of heat shrink + outer adhesive shrink creating a stress concentration/fulcrum at the crimp point
- Undersized wire relative to JST crimp specification exacerbating failure likelihood
- Installation handling loads further increasing risk of conductor pullout or fatigue failure

Compounding issue: E-shop technicians were allowed to follow either old or new spec, and assemblies are not traceable to the method used.
This creates a high risk of:
- Damage during installation
- Latent failures due to vibration and flight cycling
- In-flight failures

[embedded: image-20260626-180423.png]
[embedded: image-20260626-180606.png]

Risk Assesment
Note: Kevin and Nina spoke with Techs in the Eshop and believe this issue to be contained to B35/B40
[embedded: image-20260624-171706.png]
Link to assembly risk assessment: https://jenaero.sharepoint.com/:x:/r/sites/IRAD/_layouts/15/Doc.aspx?sourcedoc=%7BF05A5B8B-AA02-412D-BC39-821F21C032BB%7D&file=JST%20Assembly%20Risk%20Assesment.xlsx&action=default&mobileredirect=true

## Plan

Immediate Containment
- Rework all applicable assemblies currently in E-shop and WIP:
- Inspect JST crimps for conductor retention
- Replace or reterminate as required using controlled method (TBD standard)
- Continue functional validation after rework

Corrective Actions (Proposed)
- Standardize JST termination approach (remove ambiguity in spec)
- Reintroduce reliable strain relief method (e.g., insulation support engagement or alternative strain mitigation)

Escaped Product Assessment
- Identify all assemblies potentially impacted (based on build date + process ambiguity)
- Categorize by risk level (table to be included)
- Define inspection/rework plan for:
- Units in final assembly
- Units already integrated into aircraft

## Issue Status

Sharepoint - https://jenaero.sharepoint.com/:f:/s/ContinuousImprovement/IgDHkpvlto4pQ4Y6O1L80A_DAYCSUl2efTfi-EOsP79ZNIM?e=TXpaHk
Action Item List - https://jenaero.sharepoint.com/:x:/s/ContinuousImprovement/IQB8g5v78oSIRZJnmXSG6LN6AT45EwX-P8TOoIftWS0GhPQ?e=AHl3ol

- Current Status: Root cause identified (JST crimp failure due to process/spec change and strain relief deficiencies)
- Containment: Active (rework of E-shop and WIP units underway)
- Risk Level: High (potential for latent in-flight failures)
- Open Actions:
- Finalize controlled crimp specification
- Complete risk assessment and traceability mapping
- Define and execute rework plan for escaped units

## Comments (1)

### Matt Philley, 2026-06-26

@Christa Meck this has become a production stoppage can I get your help to apply the right tag?

## Attachments (11)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| Legacy Procedure.png | image | 300 | 2026-06-23 | listed only |
| Updated Procedure.png | image | 119 | 2026-06-23 | listed only |
| New_Method_IMG1.jpg | image | 6846 | 2026-06-24 | listed only |
| New_Method_IMG2.jpg | image | 6626 | 2026-06-24 | listed only |
| New_Method_IMG3.jpg | image | 6836 | 2026-06-24 | listed only |
| Old_Method_IMG1.jpg | image | 6444 | 2026-06-24 | listed only |
| Old_Method_IMG2.jpg | image | 6591 | 2026-06-24 | listed only |
| Olg_Method_IMG3.jpg | image | 6533 | 2026-06-24 | listed only |
| image-20260624-171706.png | image | 187 | 2026-06-24 | listed only |
| image-20260626-180423.png | image | 519 | 2026-06-26 | listed only |
| image-20260626-180606.png | image | 619 | 2026-06-26 | listed only |
