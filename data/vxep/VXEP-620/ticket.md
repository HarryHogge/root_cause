# VXEP-620: Metallic D369 connectors to replace current plastic D369s

- **Issue type:** Improvement
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** High
- **Created:** 2024-09-06
- **Updated:** 2025-12-09
- **Resolved:** 2025-12-09
- **Reporter:** Giovanni Gonzalez
- **Assignee:** Giovanni Gonzalez
- **Creator:** Giovanni Gonzalez
- **Links:** relates to VXEP-337 (Create, Test, and Release VXE30 Standard Config Wing Utility Drop)
- **Issue color:** purple

## Description

Replacing plastic D369 connectors for metal ones as the current plastic ones have a tendency to fall apart. Metallic D369 connectors could be a drop-in replacement and are more rugged. Will have to manually check if metal connector connects to a plastic one.
Updates:
Metallic connectors have been ordered and are expected to arrive Monday 9/9/24
Fed-Ex Tracking Number: 415544257652

## Plan

@Giovanni Gonzalez thank you for updating. Can you please create and link an excel sheet here with the following information in .
- Rows
- Existing EA D369s in inventory and use (not always the same list). . List EA and mfr PN. See transponder, AHRS, fuel cell, some payload cables that may be obsolete etc.
- Columns
- Metallic version equivalent PN.
- Cost and lead time for both plastic and metal options (if stocked, can list stocked and the TE lead time if not stocked)
- Dimension and weight differences for each

If unsure of the format, you can give it a shot and send to me for review. 
Thank you.

## Issue Status

Waiting for TE Connectivity to get back with prices and lead times for some metallic connectors. Mostly complete excel sheet with connectors comparison is linked below.
Replacement D369 Connectors.xlsx

## Comments (12)

### Cameron Chapman, 2024-09-14

@Giovanni Gonzalez how is this going? Can you please keep it a high priority?
- Test if they can mate with plastic ones.
- Give me a mating sample to compare
- Confirm with TE engineer if they are acceptable to mate with plastic connectors or not.

### Matt Philley, 2024-09-16

@Cameron Chapman @Grant Goodman gents we will need a decision if we will be incorporating these metal D369s as part of the Utility Wing Dropper Project or not. These are used on the following harnesses:
[embedded image-20240916-142640.png]

### Cameron Chapman, 2024-09-16

@Matt Philley @Grant Goodman for now they are separate efforts. The builds should use the plastic ones until we have evaluated and implemented metallic ones. I would like to complete that evaluation soon. @Giovanni Gonzalez please make this one of your top priorities.

### Giovanni Gonzalez, 2024-09-17

@Cameron Chapman I am back in office today and will evaluate the connectors.

### Giovanni Gonzalez, 2024-09-17

@Cameron Chapman Just confirmed through physical inspection that a metal connector is not compatible with a plastic one.

### Cameron Chapman, 2024-09-17

To clarify. N key is not compatible with the B key blue plastic one. Need to check with an N key (black plastic) and confirm with TE the risk of mixing types.

### Giovanni Gonzalez, 2024-09-17

N key plastic connects to N key metallic. Still need to confirm the risks of mixing the two with TE.

### Giovanni Gonzalez, 2024-09-18

Contacted TE Connectivity, they stated that as long as the connectors have the same keying and audibly click when connected together the connection is secure and there should be no issues. The N key metal connectors and plastic connectors audibly click when I interconnected them.

### Giovanni Gonzalez, 2024-10-02

Definitive Answer: The metallic D369 connectors are compatible with the plastic D369s as long as the connectors have the saying keying. As long as we ensure the connectors are of the same keying there should be no issues with connection. This information was confirmed with TE.

### Cameron Chapman, 2024-10-02

@Giovanni Gonzalez thank you for updating. Can you please create and link an excel sheet here with the following information in .
- Rows
- Existing EA D369s in inventory and use (not always the same list). . List EA and mfr PN. See transponder, AHRS, fuel cell, some payload cables that may be obsolete etc.
- Columns
- Metallic version equivalent PN.
- Cost and lead time for both plastic and metal options (if stocked, can list stocked and the TE lead time if not stocked)
- Dimension and weight differences for each

If unsure of the format, you can give it a shot and send to me for review. 
Thank you.

### Matt Philley, 2025-01-30

@Cameron Chapman doing a little cleanup. Do you think we still want to explore this for some future iteration of Dropper or should we cut this off?

### Cameron Chapman, 2025-01-30

@Matt Philley 
- We plan to remove D369s from the drop payload for the LRR deliveries at least. TBD if we will support separate configs after this. I think we will likely/hopefully move toward anyone wanting drop payload to order the new LRR wings. We will still need the external option to retrofit existing aircraft. Dual Radio Payload Block Diagrams.vsdx
- I think the metallic D369s would be an important reliability improvement for anywhere we use D369s (drop payload, transponder, mod payload, etc). There is not much work left, mainly just fit checks and updating drawings. I think we should keep this open. We could target prototype builds next time we have to build any of these.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20240916-142640.png | image | 139 | 2024-09-16 | listed only |
