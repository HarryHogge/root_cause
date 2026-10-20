# FS2-3286: Review and update max pause duration during descent. Coordinate with software to implement.

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-04-23
- **Updated:** 2025-09-10
- **Resolved:** 2025-09-10
- **Reporter:** Cameron Chapman
- **Assignee:** David Grosher
- **Creator:** Cameron Chapman
- **Links:** relates to VXEP-415 (VXE 538 Altitude Drop During Landing); relates to VXEP-274 (VXE 438 Lift motor failure resulting in crash)

## Plan

- @David Grosher there are still some remaining actions to identify root cause and report cleanup, but I think we are ready to start implementing the main CA. Are you able to assign someone to plan/implement the max pause durations listed in this report? https://jenaero.sharepoint.com/:w:/r/sites/FlightSafety/Shared%20Documents/Incident%20Reports/VXE-438%20Lift%20motor%20failure%20resulting%20in%20crash/VXE-30%20Absolute%20maximum%20Pause%20duration.docx?d=w80e33a178fcc489495bd50d5da322b56&csf=1&web=1&e=0qZXg4   Section Extended Pause Guideline
- Raj “Landing and take-off should be limited to 45s and 30s respectively. If the operator issues extended pauses, the motors should run at PWM value of about 1300-1350. This PWM value translates to motor force needed to counter the gravitational force exerted on a 55lbs drone. Motors can be operated at 50% throttle for 100s max. Operating ESCs above 95% throttle (PWM=1812) for extended periods (20s+) should be avoided. VTOL PID control routine could use some damping.”

## Issue Status

VXE-438 crashed because the operator issued extended pauses until some of the ESCs overheated and failed. We want to quantify the maximum pause duration and condition. See related conditions here: T95_V438_240209_Relavent data.xlsx

## Comments (10)

### Rajesh Budhabhatti, 2024-05-08

I did some calculations on power required to operate VTOL motors under various states-lift-off, position-hold and landing. Assuming that a pause involves cruise motor off and holding the 55lbs VXE30 stationary, ie. countering gravitational force, it would require VTOL motors to operate at PWM between 1350-1400. See the calculations here: Lift motor power calcs.xlsx
Next, I ran an ESC-Motor combination on Dyno at PWM=1500 for 100 seconds. PWM=1500 was chosen to take into account wind conditions etc.
I measured temperature rise of about 55 degrees C after 100 seconds of operation. (Ambient temperature was 20 degrees C, ESC temperature rose to 75 degrees C.)
This tells us that under the worst case scenario ie 50C ambient temperature, the maximum pause duration should be less than 100 seconds, and pause PWM must be limited to PWM =< 1500. See figure 25 for more details here: Investigation Summary VXE-438 Lift Motor failure crash.docx

### Rajesh Budhabhatti, 2024-05-20

Shared Max pause reading for different throttle levels and guidelines with Everette.

### Rajesh Budhabhatti, 2024-05-20

@Cameron Chapman @Everett Werner Completed report and data on absolute maximum pause duration here: VXE-30 Absolute maximum Pause duration.docx

### Cameron Chapman, 2024-05-22

@Rajesh Budhabhatti I reviewed the document. Thank you for creating it and the detailed and professional analysis. Questions
- Can/have you verified the Catastrophic condition with actual dyno testing and measurements? You could heat the ESC to 50C internal with current, then perform the profile to verify. Please monitor and set abort temperature limits to stop the test if a limit is reached, to attempt to prevent damage.
- What is a typical and max VTOL throttle to maintain a pause? Everett could help with this.
- Have you confirmed if pause at 1650 PWM is realistic (conditions are so bad that 1650PWM would be required to maintain altitude, not climb).
- Max cruise time in table 4 does not make sense. We are looking for the maximum pause duration.

### Rajesh Budhabhatti, 2024-05-22

@Cameron Chapman Thank you for pointing out, Cameron. It was a typo. The table 4 indicates maximum pause time under various conditions. I made the correction, both in excel and word doc.

### Rajesh Budhabhatti, 2024-05-29

Updated max pause duration based on 105 degrees C limit.

### Rajesh Budhabhatti, 2024-06-03

I tested ESC to catastrophic conditions. While the MOSFETs sustained the test, the electrolytic caps that are rated at 105C popped and the ESC died. This confirms our stated limitation in the max pause duration report: VXE-30 Absolute maximum Pause duration.docx
I am waiting on input from software team regarding the typical throttle setting for a pause. per my calculations, a 40% throttle (PWM-1350) will be sufficient to overcome the gravity of a 55lbs AV. I do not believe there could be a situation needing anything beyond 60% throttle (PWM=1525) except for momentary need for stabilizing against wind turbulence.

### Rajesh Budhabhatti, 2024-06-04

Max pause duration report and recommendations shared with software team.

### Rajesh Budhabhatti, 2024-06-17

@Cameron Chapman @Pat Wells 
Answers and findings to list of questions in Plan section:
i. I have not been able to accurately replicate the catastrophic condition. I cannot replicate the 50C ambient by heating the ESC to 50C. For this reason, I have provided theoretical calculations based on temperature build-up at ambient temperature of 20C and absolute maximum rating of components that fail. 
ii. Based on my calculations, a 55lbs AV will need PWM = 1356 or throttle of about 42% to hold position in steady state. Factoring in wind disturbance and need to stabilize the craft, I estimate maximum throttle needed to be under 50% or PWM=1427. I have asked Everett but have not received a response. 
iii. No, Pause condition would not need PWM of 1650 (75% throttle). 
iv. Thank you for pointing out. I have made correction and calculated for maximum pause time instead of maximum cruse time.
Item 2-5 implemented in the report and submitted to software team (Everette, John Clark, Michael Berger) I will follow up with them to see if they have any questions.

### Cameron Chapman, 2024-08-27

Moving previous questions from the plan. See answers below. 
- Review report and answer questions.
- @Rajesh Budhabhatti I reviewed the document. Thank you for creating it and the detailed and professional analysis. Questions
- Can/have you verified the Catastrophic condition with actual dyno testing and measurements? You could heat the ESC to 50C internal with current, then perform the profile to verify. Please monitor and set abort temperature limits to stop the test if a limit is reached, to attempt to prevent damage.
- What is a typical and max VTOL throttle to maintain a pause? Everett could help with this.
- Have you confirmed if pause at 1650 PWM is realistic (conditions are so bad that 1650PWM would be required to maintain altitude, not climb).
- Max cruise time in table 4 does not make sense. We are looking for the maximum pause duration.
- Determine the maximum pause time under worst case scenario.
- Provide a report for software team for safely handling extended pause commands from the operator.
- Share the corrective actions with Everett and come up with recommendations to software team for maximum safe pause time.
-

## Attachments (0)
