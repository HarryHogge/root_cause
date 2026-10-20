# VXEP-1607: Update cable design process to ensure planning for tooling and cable testers is complete so that they are ready when builds need to happen.

- **Issue type:** Major Project
- **Status:** Assigned
- **Priority:** Low
- **Created:** 2025-11-17
- **Updated:** 2026-09-29
- **Reporter:** Cameron Chapman
- **Assignee:** Samuel Raumin
- **Creator:** Cameron Chapman
- **Links:** relates to VXEP-172 (Cable Tester Documentation and Training); relates to VXEP-1767 (Evaluate and implement new policy to ensure new cables have cable tester connections when first built, or build them in parallel)

## Description

- Actions.
- Will to make cable design and build checklist with most important steps that people will use on all designs.

 
- Once connector is considered/selected, do the following
- Notify stakeholders. Make a plan for the following.
- Make a plan for tooling.
- Do we have tooling. Check sheet.
- Ensure QE is involved.
- Make a plan for testing
- See if we have existing adapters or board. Identify which are needed.
- If not, make a plan to make adapter cable or board.
- Board (PCB files ready to order will arrive when time to build)
- Cable adapter. Plan to build in parallel with first article.

## Comments (5)

### William Dresser, 2025-12-19

@Cameron Chapman I had a good chat with Ben Norris about harness testing. I believe 90% of the materials that we need for B40 or gimbal harness testing already exist, it's just some odds & ends that we don't have adapter cables for. E-shop handles making the adapter harnesses and test plans, so the responsibility of engineering is limited to identifying the gaps and ordering the material to fill those gaps (micro-d connectors & DSUB for gimbal, glenair & microlock connectors for B40 FDB, etc.), then making a request for those adapters and test plans. In the future we can have engineering develop purpose-made PCBs on a per-harness basis (there are some benefits to this over the breakout harnesses + breakout PCBs) but that step should wait until after a harness has fully transitioned to production and we are ready to commit.

### Cameron Chapman, 2025-12-23

@William Dresser Thank you. Please add ordering mating connectors and requesting adapters to your new harness design checklist. Is it worth ordering mating connectors for B40 and gimbal harnesses now? I would think so. We could also order for HSV if they plan to build any (not sure better for us to do that, or HSV after production transitions builds there)

### William Dresser, 2025-12-23

@Cameron Chapman “Please add ordering mating connectors and requesting adapters to your new harness design checklist.” Can do.
”Is it worth ordering mating connectors for B40 and gimbal harnesses now? I would think so. We could also order for HSV if they plan to build any (not sure better for us to do that, or HSV after production transitions builds there)” Agreed, that was my plan. I have an excel started which is intended to capture that information. I was under the impression we should be building duplicates to share with HSV. Let me know if that is not the case.

### Cameron Chapman, 2025-12-23

@William Dresser that sounds good. When submitting the first request, we can ask production if they would rather build adapters for both sites in one location and ship, or build adapters at the site they will be used. @Daniel Ceja  what do you recommend?

### Daniel Ceja, 2025-12-29

@Cameron Chapman I recommend that we build adapters in one location and then ship them as this would give us a single point of control where we can verify that both adapter harnesses are identical and are behaving the same way before being implemented into production. We want to avoid is a situation where a cable passes our cable tester setup but fails in a different location so I think this option would eliminate as many variables as possible.

## Attachments (0)
