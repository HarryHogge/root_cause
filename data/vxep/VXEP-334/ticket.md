# VXEP-334: Silvus SS4 Interim (4.0.4.1) Configuration File Creation Needed

- **Issue type:** Problem
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2024-04-08
- **Updated:** 2026-03-30
- **Resolved:** 2026-03-30
- **Reporter:** Matt Philley
- **Assignee:** Wesley Lilienthal
- **Creator:** Matt Philley
- **Links:** relates to VXEP-187 (Plan for Silvus Streamscape 5 rollout/compatibility. )
- **Part Number(s):** 100-107929, 96X-3-14-1014, 100-100879

## Description

We have a configuration file that was created for the last approved version of Silvus Firmware 4.0.3.14, but not a config file for the latest approved 4.0.4.1.
The config file has all the settings saved so all radios are configured with equivalent settings and we can quickly upload that to the radio rather than manually applying settings for each radio.
We have been using the 4.0.3.14 config file so far, however it appears to be causing radios to fall into Diagnostic mode for some reason which is taking extra steps to reboot radio and resolve that.
This will be the first time we have an Engineering controlled config file for the Silvus radio, however we have discussed the need for the SS5 rollout since SS5 may have different configs per Customer. This will be a good opportunity to try and figure it out before that rollout when it will get more complicated.

## Plan

@Matt Philley (during PTO of @Wesley Lilienthal) is sending a note to Silvus to determine if the config file could be causing the issue of the radio coming up in diagnostic mode.
@Carson Buckley has made a quick config file from the new firmware, to see if that helps.

## Comments (3)

### Matt Philley, 2024-04-08

@Carson Buckley @Trevor Gronner @Wesley Lilienthal @Greg Fryer 
Jira to get support to help create and troubleshoot config file for Silvus Radios 4.0.4.1 Firmware for SCO to use when configuring Silvus Radios.

### Matt Philley, 2024-04-10

Carson created a config file based on the 4.0.3.14 config file and will be using that in SCO for the time being
We still have the issue with it falling into diagnostic mode, but I am trying to get an email to Silvus today on that.

### Matt Philley, 2024-05-07

Housekeeping…
Config file that Carson made was not successful, so we reverted back almost immediately to the 4.0.3.14 config file for Production use.
A couple TIQUILA deliveries made it through with the Carson-made config file, but we had to revert back to the 4.0.3.14 after they were squawked in source inspection

## Attachments (0)
