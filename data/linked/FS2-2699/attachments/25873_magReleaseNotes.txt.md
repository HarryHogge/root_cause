# magReleaseNotes.txt

Attachment 25873, text, 5 KB, added 2025-02-03 by Scott Hunter.

b874ec3f - (tag: v1.56.00-pr-08) Merged in bugfix/shunter_FS2-2792-vtol-system-clock-not-setting (pull request #228) (5 days ago) <Scott Hunter>
      During Speedgoat testing we found the VTOL's system clock was not being set rom the onboard real time clock (RTC). This code change restores the 
      setting of the VTOL system clock from the RTC.
104e496d - (tag: v1.56.00-pr-01, tag: v1.56-pr-01) Merged in bugfix/FS2-2676-mag-healing-fix (pull request #219) (3 weeks ago) <Scott Hunter>
      During Speedgoat testing a problem was discovered where a mag sensor failure did not properly recover when the sensor values returned
      to their acceptable values. This code change corrects that bug.
4d02ac99 - Merged in feature/shunter_FS2-2141-vtol-limit-setting-of-rtc-to-postlaunch (pull request #211) (6 weeks ago) <Scott Hunter>
      We've found there's some risk associated with setting the VTOL's real time clock (RTC). We've seen the I2C interface fail and contribute to 
      VTOL resets. When the time stored in the RTC differs from what's reported from the GNSS receiver the VTOL updates the value stored in the 
      RTC. This code change limits when the RTC chip can be reset to AFTER a landing when the consequence of a VTOL reset is minimal.
aabe334d - Merged in feature/FS2-2097-vtol-mag-fault-logging (pull request #184) (4 months ago) <Scott Hunter>
      Problems with magnetometer faults being recorded in the field with impossible readings. Impossible because the magnitude of the sensed mag field
      exceeded the capability of the sensor. The sensed value was being corrupted because the floating-point registers weren't saved/restored when interrupted.
      This code change adds FPU support when the task is created.
cf3f38bb - Merged in feature/shunter_FS2-2407-evaluate-resource-hit-for-FPU_Enable (pull request #195) (8 weeks ago) <Scott Hunter>
      In light of the findings for FS2-2097 (PR #184) we made the call to add FPU to all tasks in the VTOL. The extra resources required for FPU
      support is small.
88f551dd - Merged in bugfix/FS2-2406-vtol-log-good-bad-transition-of-maghealth (pull request #201) (7 weeks ago) <Scott Hunter>
      The baseline software recorded the first transition of bad to good magnetometer sensor to the event log. This code change extends
      the logic to record all good to bad transitions and all bad to good transitions.
973db641 - Merged in feature/shunter_FS2-2412-vtol-mag-on-fwap (pull request #207) (7 weeks ago) <Scott Hunter>
      A requirement emerged where we need the magnetometer data from the VTOL forwarded to the FWAP. This code change publishes the "external mag"
      data, health and status to the CAN bus for the XCOMM to read and forward along to the FWAP.
52ffb79b - Merged in feature/shunter_FS2-2302-add-isr-event-history-to-vtol (pull request #171) (4 months ago) <Scott Hunter>
      In recent releases we've added a feature that records a history of what tasks were active. When the processor is reset that history is recorded
      to the event log for post processing to help figure out what code was active when the reset happened. We discovered it would be useful to add
      a record of what interrupt service routines (ISR) were active in that recorded history. This code change adds that ISR history.



a361f90 - Merged in feature/FS2-2544-xcomm-retrieve-the-external-mag (pull request #111) (7 weeks ago) <Scott Hunter>
      Per FS2-2412, PR #207 the XComm the XComm has a new requirement to read "external mag" sensor data from the CAN bus and forward
      that data to the FWAP. 
e82c720 - Merged in feature/shunter_FS2-2407-evaluate-resource-hit-for-FPU_Enable (pull request #97) (8 weeks ago) <Scott Hunter>
25fef53 - Merged in feature/shunter_FS2-2610-xcomm-add-fpu-support (pull request #109) (7 weeks ago) <Scott Hunter>
      Based on lessons learned with FS2-2097 and FS2-2407 we added FPU support to all tasks in the XComm.
639eb38 - Merged in feature/shunter_FS2-1885-xcomm-add-isr-event-history_take2 (pull request #79) (4 months ago) <Scott Hunter>
      Based on work for FS2-2302 in the VTOL the same capability was added to XComm
f688d0c - Merged in bugfix/FS2-2143-xcomm-eliminate-unterminated-while (pull request #76) (4 months ago) <Scott Hunter>
      Based on work for FS2-2302 in the VTOL the same capability was added to XComm
e3fbd75 - Merged in shunter_FS2-2025-capture-xcomm-config (pull request #70) (5 months ago) <Scott Hunter>
      We tracked down an XComm watch-dog timer reset to an unterminated while loop in the I2C device driver. A timout was put on that while loop to prevent
      unwanted system resets. We also added metrics to the event log capturing how many times the I2C driver resets and how many times this new timeout is
      invoked.
