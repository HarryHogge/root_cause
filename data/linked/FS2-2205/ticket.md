# FS2-2205: Make the 'safelast' variable static in the SendSafteySwitch function in the ApmParser.cpp file

- **Issue type:** Bug
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2024-08-27
- **Updated:** 2024-10-10
- **Resolved:** 2024-09-25
- **Reporter:** Jason Scherer
- **Assignee:** Jason Scherer
- **Creator:** Jason Scherer
- **Environment:** Since the safelast variable isn’t static we will never see the “SAFE OFF” message in the debug logs to know if the safe off message was sent to VTOL. We need to make this variable static to fix the debug message functionality.
[embedded: image-20240827-220851.png]
- **Parent:** FS2-1993 VXEP-416 Failure to Launch - Vehicle Investigation
- **Epic Link:** FS2-1993
- **Sprint:** FS2 Sprint 24

## Comments (1)

### Gabriel Zolot, 2024-10-10

I tested the code and found that the “SAFE OFF” message appears in the AAR twice. Attached is the AAR for reference.
[embedded: T95_V115_241010_123728_debuglog.txt]

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20240827-220851.png | image | 31 | 2024-08-27 | listed only |
| [T95_V115_241010_123728_debuglog.txt](attachments/23919_T95_V115_241010_123728_debuglog.txt.md) | text | 57 | 2024-10-10 | converted |
