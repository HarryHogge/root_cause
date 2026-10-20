# VXEP-1506: VXE-471 - Cannot connect to GCS. Harness and avbox damage

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** High
- **Created:** 2025-09-10
- **Updated:** 2025-09-12
- **Resolved:** 2025-09-10
- **Reporter:** Cameron Chapman
- **Assignee:** Ben Norris
- **Creator:** Cameron Chapman
- **Links:** relates to RMA-745 (VXE-471 RMA 250722-3)

## Description

VXE-471 requires electronics troubleshooting.  The aircraft came in for a 'tier 1 diagnostic' assessment due to the customer stating they're having issues connecting to the GCS. We found that the Fuselage Power harness was compromised- requested additional evaluation.

## Plan

- Which pins were shorted?
- Was this cable tested on the cable tester?
- Did it go through all standard inspections?
- Any ideas why it may have passed initially and shorted in the field?
- Was this the nose connector?
- Please red tag avionics box and harness for evaluation. Ok to replace the damaged harness and avionics box, but please do not ship without engineering evaluation and approval, in case something else might have been damaged.

## Issue Status

Call with @Andrew Hildreth: 6 aircraft in various states of not working. No longer under warranty. Customer does not have service agreement. Tiered system diagnostic report. Tier 1. Engineering support not required of authorized.  @Drew Hildreth ⁠  there may be some risk of other damaged parts not being detected. This should be communicated to the customer in some fashion, but ok if they are ok with that risk,   Plan:  Please Replace defective units and retest.

## Comments (14)

### Cameron Chapman, 2025-09-10

@Gary Passanisi @Ben Norris was this cable ran through the cable tester? I am wondering if there are other shorts that could have caused this damage.

### Cameron Chapman, 2025-09-10

Call with @Drew Hildreth: 6 aircraft in various states of not working. No longer under warranty. Customer does not have service agreement. Tiered system diagnostic report. Tier 1. Engineering support not required of authorized. 
- Can you publish tiers to confluence if we continue to use this system?

Plan:
- Replace defective units and retest.

### Drew Hildreth, 2025-09-10

@Cameron Chapman If we continue to do this, I think that publishing to Confluence would be a great idea.

### Cameron Chapman, 2025-09-10

Call with @Andrew Hildreth: 6 aircraft in various states of not working. No longer under warranty. Customer does not have service agreement. Tiered system diagnostic report. Tier 1. Engineering support not required of authorized.  @Drew Hildreth ⁠  there may be some risk of other damaged parts not being detected. This should be communicated to the customer in some fashion, but ok if they are ok with that risk,   Plan:  Please Replace defective units and retest.

### Gary Passanisi, 2025-09-10

@Cameron Chapman It was, and there was another short that popped up, but we couldn’t see where it was. In the past, when there is a short in that 16p ODU, the tester will indicate a short in the F_C solenoid line, but it is usually a false read. The only we could confirm is the 5 and 7 pin short

### Cameron Chapman, 2025-09-11

@Gary Passanisi thanks for that info. @Ben Norris @Daniel Ceja the cable tester should not be giving false reads and should be able to identify all shorts. Do you know why this behavior is happening and how to resolve it? Do we follow up such results with identifying where a short is manually, and verifying that the solenoid is a false read? I recommend tracking in a separate linked Jira issue.

### Gary Passanisi, 2025-09-11

@Cameron Chapman @Lauren Velasquez After looking into it a bit more, we found that the nose power harness, fuselage harness, and avi box are fried. A severe power surge burned wires and components from nose to box. Ben and Liam are trying to figure out a root cause.

### Ben Norris, 2025-09-11

@Cameron Chapman The cable tester was not implemented at the time this vehicle was assembled. The travelers show the cables in question (Fuse signal and Nose signal) passed all functional checks including Ironbird testing. From the damage seen in those harnesses and the avionics box the running theory is a power short possibly in either side of the 16pos ODU.

### Ben Norris, 2025-09-11

@Lauren Velasquez Recommending replacement of Nose Cone assembly (old assembly parts unavailable), Fuselage harness, and Avionics Box. Silvus Radio was checked and no damage to Auxiliary power line so no need to replace branch cable or fuse payload harness.

### Lauren Velasquez, 2025-09-12

@Gary Passanisi @Ben Norris @Cameron Chapman  Thank you all for your help through this one!
@Drew Hildreth  I'll get the quote drawn up on this one.

### Cameron Chapman, 2025-09-12

@Ben NorrisI meant did you run it through the cable tester recently after it was returned? Did it record any faults if so?

### Cameron Chapman, 2025-09-12

@Gary Passanisi Sounds good. I was told that the aircraft is out of warranty and I think the customer was known to use experimental payloads, so we do not need to/I don’t think we are authorized to spend much time identifying the cause of the damage. I think Just identify and replace damaged components and retest. @Lauren Velasquez and @Drew Hildreth  would know the plan best.

### Ben Norris, 2025-09-12

@Cameron Chapman Gary ran the Fuse signal harness through the cable tester and found the one fault but that is much more likely a symptom of the failure not the cause. The nose harnessing can’t be run through the cable tester due to the damage caused by the short as well as that assembly generally not lending itself to the cable tester due to the board attachments. I think the most likely location of the instigating short is in the 16pos nose ODU.

### Drew Hildreth, 2025-09-12

@Cameron Chapman Spot on! Identify what is damaged and move on. No need for a RCCA on this Aircraft. 

Thank you everyone for your attention on this.

## Attachments (0)
