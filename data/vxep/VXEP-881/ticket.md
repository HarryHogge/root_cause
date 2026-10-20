# VXEP-881: MAIM Firmware - Generate Static MAIM IP Address From AP Discovery Message

- **Issue type:** Sub-task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2025-01-07
- **Updated:** 2025-02-07
- **Resolved:** 2025-02-07
- **Reporter:** Kurt Burian
- **Assignee:** Kurt Burian
- **Creator:** Kurt Burian
- **Parent:** VXEP-880 MAIM v4 Software Release

## Description

MAIM should listen for tail number discovery messages during the first 30seconds of startup to calculate a unique IP associate with the tailnumber. Eg) Vehicle 123 = 10.128.123.11 12
MAGNUSS will need to expect a installed MAIM board would reside at this address. Need to verify it has knowledge of the tail number.

## Issue Status

IN REVIEW
Pull Request https://bitbucket.org/edgeautonomy/maim/pull-requests/10

## Comments (2)

### Kurt Burian, 2025-02-05

Changing ip from 10.*.*.11 to 10.*.*.12

[embedded image-20250205-182827.png]

### Kurt Burian, 2025-02-05

Pull Request Opened

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20250205-182827.png | image | 20 | 2025-02-05 | listed only |
