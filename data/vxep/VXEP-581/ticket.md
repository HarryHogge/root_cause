# VXEP-581: Seal Air Data Pod Assembly PN 107-101141

- **Issue type:** Improvement
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Medium
- **Created:** 2023-02-27
- **Updated:** 2025-04-15
- **Resolved:** 2025-04-15
- **Reporter:** Ryan Ferguson
- **Assignee:** Former user
- **Creator:** Ryan Ferguson
- **Labels:** EE-Intern, Rate#
- **Links:** relates to ENGPRJA-32 (Heated pitot system prototype for 2023 demo); relates to ENG-823 (Test Air Data Board with alternate potting compound); relates to VXEP-266 (VXE (all) ADP: Heated Pitot/New SA CAM/Remove other obsolete components)

## Description

When building the Air Data Pod, a significant amount of time is spent sealing individual components.  To process a batch of 12 air data boards, PN 107-103560, an approximate 3 hours of touch time is required to fully seal all of these assemblies.  If a defect is found in the sealant of any of these assemblies, an additional 45 minutes of touch time is required to do the rework.  If all work is done right the first time, it takes approximately 2.5 hours to cure this board entirely.
The SA cam also requires a certain amount of ToughSeal for waterproofing purposes, estimating 20 minutes of touch time for each camera assembly.  The laser range finder does not need sealing.

Sealing the air data pod will make it possible to build the air data board without any toughseal or conformal coatings.  This will save approximately 4 hours of touch time and 3.5 hours of cure time for each batch.

## Comments (7)

### Greg Fryer, 2023-02-27

@Ryan Ferguson I moved this over to projects, because it’s definitely that. Will need to go through our wickets to figure out how long such a change would take, and if there is any history that needs to be taken into account.   We’re still figuring that out, but most likely something like going to the CCB first.

### Ryan Ferguson, 2023-02-27

I have attached the project proposal document.  This project can be summarized in two different phases, namely sealing the pod and removing unnecessary adhesives from the subassemblies within.  
[embedded file]
This project may have some relevance or impact on the heated pitot tube project https://jenaero.atlassian.net/browse/ENGPRJ-215  but for the time being I am treating that as out of scope considering it is still in the early R&D phase.

### Mark Squillante, 2023-04-17

I think we should revisit this issue in light of the DP100 cracking on the air data boards during temp cycle testing. The DP100 appears to be too hard after curing. If we could seal the air data pod completely there might not be a need to pot the air data board. It also seems this would save a lot of time for Production. 
Air data board testing with DP100: https://jenaero.atlassian.net/browse/ENG-823

### Cameron Chapman, 2023-04-19

@Former user, do you have a ROM for how feasible this would be? Guessing potting the ADB with an alternate compound will be quicker and less risk, but worth evaluating.  @Scott Stuckey

### Former user, 2023-04-21

@Cameron Chapman Aren’t there other risks involved with removing sealant/ conformal coating and exposing components on the boards to environmental factors? Aside from waterproofing. Is there a more efficient way to processing boards that hasn’t been considered?

### Cameron Chapman, 2023-04-21

If the pod was sealed, we would still likely conformal coat the boards, but conformal coating is done externally and much quicker than full waterproofing. 
The main problem currently is finding a good way to waterproof the boards and handle the environment without using tough seal. Efficiency is great, but not top priority. 
We will probably end up finding another way to waterproof the board, but I thought it could be helpful to get a ROM to waterproof the ADP, to see if it is worth considering. Waterproofing the pod would lead to multiple part labor savings.

### Christa Meck, 2025-04-15

Both Reporter and Assignee are no longer with the company.  There has been no work on this item in quite some time.  Canceling.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [Improvement  Project Proposal - Sealing Air Data Pod.pptx](attachments/12883_Improvement%20%20Project%20Proposal%20-%20Sealing%20Air%20Data%20Pod.pptx.md) | pptx | 769 | 2023-02-27 | converted |
