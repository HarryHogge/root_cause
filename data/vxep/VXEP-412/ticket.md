# VXEP-412: VXE 426 Overshoot on landing, becoming progressively worse

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-05-17
- **Updated:** 2026-08-14
- **Resolved:** 2024-08-23
- **Reporter:** Pat Wells
- **Assignee:** David Grosher
- **Creator:** Pat Wells
- **Labels:** GNSS-Rate, MARSOC, Software, Weekly-incident-tracker
- **Links:** relates to VXEP-365 (VXE 426 Slow descent on VTOL landing, crash landing into a fence); relates to FS2-1753 (v426 Investigation (Slow descent, land on fence)); relates to VXEP-315 (VXE 459 Overshoot of LZ Mishap on landing, operator unable to nudge); relates to VXEP-427 (VXE 430 abnormal landing behavior)
- **Customer:** MARSOC
- **Vehicle Tail Number:** 426
- **Plan:** Software update upcoming.
- **Issue Status:** Software update in work.
- **Severity:** 1 - Flight Critical

## Description

Aircraft is overshooting LZ by over 150 meters, getting progressively worse over time.

AAR attached

## Corrective Action

Software update being rolled into next upcoming release to address GPS update rate.
To allow for better lateral convergence, consider increasing the size of the landing pattern.  This will allow more time for the controller to converge before transition occurs.

## Root Cause

Created powerpoint here.  Overshoot for this flight appears to be caused in part by attitude estimation errors.  Pitch estimation error is ~10 degrees during approach transition when pitch up should arrest forward velocity.
Root cause was found to be a reduction in GPS rate on the ublox receiver.  See investigation here.

## Comments (9)

### Cameron Chapman, 2024-05-17

@David Grosher

### Eric Brewer, 2024-05-20

@Cameron Chapman @David Grosher @Greg Fryer See above.  It looks to me like there are significant heading differences between the fixed-wing and vtol ap’s.  The calibration procedure will not reveal this fact to the operator since they only have access to fixed-wing heading.  I think in this case it may be worth giving the customer access to the VTOLAP web page telemetry so they can manually check the vtol heading against the fixed-wing heading and recal if necessary.
I suspect that the heading errors are causing significant pitch errors which are impacting their ability to do a successful approach.

### Greg Fryer, 2024-05-21

@Pat Wells Please see corrective action from @Eric Brewer 
(@David Grosher Feels safe to do the plan without further review, since it’s normal procedures.)
@Eric Brewer Seems like a deliberate check that the headings align would be a good automated function as well? We are also trying to keep folks out of the web pages (can cause issues), so more likely would want to update FW to deliver VTOL heading to ground station in cal check as well? (Will take longer to implement)

### Eric Brewer, 2024-05-21

@Greg Fryer completely agree long term we should handle this automatically as part of the calibration check and/or reveal both sets of heading to the operator.
That said - short term I believe they have already been doing the calibrations and since the checks currently pass they may think the calibration worked successfully, not realizing the vtolap still has a bad cal.  Without this extra step I’m not sure how we’d ensure the issue is resolved near term.

### David Grosher, 2024-05-21

@Pat Wells @Eric Brewer @Greg Fryer We should also inform them to not operate around or near any ferrous objects. I would suggest changing their operational area to some place they are confident does not contain interference.  It seems to me that they are calibrating for the ground conditions and they are not accurate up and away in flight.

### David Grosher, 2024-05-21

@Pat Wells @Eric Brewer @Greg Fryer I am very hesitant with the webpages. Right now there is a known bug on the VTOL GPS status web page that will reset the VTOL AP when there are 30 or more satellites. 
Let’s show them exactly what to check on the XCOMM. I don’t think we can provide access to the VTOL.

### Eric Brewer, 2024-05-22

@Pat Wells @David Grosher @Greg Fryer , I uploaded a document here with instructions on how to compare the heading values on VTOL and FWAP from the xcomm webpage.  After comparing several flights from the database, I’m worried there may be some systematic problems with the way we calibrate the VTOL mag.  The differences between fixed-wing and vtol heading estimates are typically quite large (5-20+ degrees in the logs I looked at).  Is it possible that installation of the wing potentially changes the cal from flight to flight?
It’s probably worth having our operators run through this check and a recalibration of the mag to see if it’s possible to get the differences much smaller before we recommend the procedure to the customer.
In the meantime I will also take a look at the software to see about potential longer term fixes to our susceptibility to heading errors.

### Cameron Chapman, 2024-05-28

Questions and answers from call. 
- Do we have evidence of a calibration being accurate at calibration time, then being inaccurate during that flight or later? No. No data from that collected in AAR. Verbal reports of needing to recalibrate a lot that supports.
- Can we compare and flag offsets with the GCS? How long feasible and preferred is that vs a GCS update? May not be useful for average operator.
- Plan for testing for magnetometer interference/site appropriateness? Eventually we do want to operate in such environments, but could have calibration location requirements. Operators cannot accurately evaluate.

Plan needs an update. Based on discussion, we will not do some of the listed actions. See comments below.

### Eric Brewer, 2025-02-28

@David Grosher @Pat Wells report updated to new template to reflect root cause.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| IMG_8162 (1) (2).jpg | image | 4841 | 2024-05-17 | listed only |
| IMG_8164 (2).jpg | image | 4573 | 2024-05-17 | listed only |
| T95_V426_240417_032128_pack (2).zip | archive | 3974 | 2024-05-17 | listed only |
