# VA-2937: Update Mag/Accel Build Procedure to prevent use of excessive flux when soldering RF shield cover.

- **Issue type:** Improvement
- **Status:** New
- **Priority:** Medium
- **Created:** 2026-10-12
- **Updated:** 2026-10-14
- **Reporter:** Samuel Lopez
- **Creator:** Samuel Lopez
- **Links:** relates to VXEP-1971 (VXE 885 Erratic behavior in flight caused crash)

## Description

VXE-885 was returned to redwire as an RMA in September 2026.  The investigation concluded that an excess of flux on the Mag/Accel board applied during the soldering of the RF shield cover burned up at high temperatures and caused a short circuit as shown in the images below.

To prevent this from happening again, the build procedure for the Mag/Accel board 107-103101 shall be updated to include the statement:
““Do not use excessive flux. At high temperatures, it can burn and cause leakage currents which create short circuits.”
Propose to add this change on Step 20 of the procedure on the second bullet point.

## Comments (2)

### Samuel Lopez, 2026-10-12

As seen on right side of board, excessive flux burns up at high temperatures.  On this board, the burned flux caused a short circuit.  When the board was wiped clean with isopropyl alcohol, the board worked normally.
[embedded: Image (1).jpg]

### Samuel Lopez, 2026-10-13

@Daniel Mckeon  and @Michelle Greenwald 

Can we update the procedure 107-103101 on Step 20, bullet point 2.  After the line that says, “Do not use excessive solder! This could bridge components under the shield.”
Add another line that says
“Do not use excessive flux!  Heated flux can burn up and cause leakage currents and short circuits.”

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| Image (1).jpg | image | 1929 | 2026-10-12 | listed only |
