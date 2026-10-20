# FS2-1862: VXEP-315 Landing Performance Improvements

- **Issue type:** Epic
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-05-14
- **Updated:** 2026-02-09
- **Resolved:** 2026-02-09
- **Reporter:** Scott Whitney
- **Assignee:** Eric Brewer
- **Creator:** Scott Whitney
- **Labels:** sw_inReview
- **Links:** relates to VXEP-315 (VXE 459 Overshoot of LZ Mishap on landing, operator unable to nudge)

## Comments (1)

### Eric Brewer, 2024-05-22

Checked in prototype c-code here.  Tested on HIL, it limits use of fixed-wing helper forward throttle as expected, but performance testing is limited due to limitation of HIL environment.  Test results captured here.
[embedded: WindTesting.docx]
A couple notes:
- The branch has some test code to offset the vehicle pitch angle estimate in HIL mode.  This would be removed for production
- Based upon Simulink testing, I’d also recommend reducing max fixed-wing helper throttle to 0.4 (currently 0.6).
- Recommend we also extend the parameter for minimum landing distance. This will allow the vehicle to converge out crosstrack error in the case of any crosswind.  We should also update the user manual to recommend avoiding an landings in crosswind.  From testing on xkit, it was extended by a factor of a little over 2 (artis eyeballing the changes he made extended from 180m to 400m)
- Really need speedgoat to test this properly in the HIL.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [WindTesting.docx](attachments/20639_WindTesting.docx.md) | docx | 1499 | 2024-05-22 | converted |
