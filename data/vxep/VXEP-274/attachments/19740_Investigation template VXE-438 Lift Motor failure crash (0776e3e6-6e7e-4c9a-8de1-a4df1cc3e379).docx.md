# Investigation template VXE-438 Lift Motor failure crash (0776e3e6-6e7e-4c9a-8de1-a4df1cc3e379).docx

Attachment 19740, docx, 1686 KB, added 2024-03-28 by Rajesh Budhabhatti.

|  |
|  |
| Incident Number:  Revision:  Author: Raj Budhabhatti Date: |
| CONFIDENTIAL AND PROPRIETARY DATA: Portions of this document contain proprietary technical data pertaining to items, or components, or processes, or other matter developed or acquired at the private expense of Edge Autonomy and is restricted to use only by Edge Autonomy employees or other persons authorized by Edge Autonomy in writing to use it. Neither said document nor said technical data shall be furnished or disclosed to, or copied or used by, persons outside Edge Autonomy, without the express written approval of Edge Autonomy. Markings on this page regarding confidentiality and proprietary information apply to this entire document.  EXPORT CONTROL WARNING NOTICE: WARNING – this document may contain technical data whose export is restricted by the Arms Export Control Act (Title 22, U.S.C. Sec 2751 et seq) or the Export Administration Act of 1979 (Title 50, U.S.C., App. 2401, et seq) as amended.  Violations of these export laws are subject to severe criminal penalties.  Disseminate in accordance with provisions of DoD Directive 5230.25.   Contains Export Controlled Information Not releasable to Foreign Persons unless authorized by 22 C.F.R. 120-130 or 15.C.F.R. 730-774. |

List of Figures

No table of figures entries found.

List of Tables

No table of figures entries found.

## Introduction

## Template Notes

Save files here EE Updates-Vehicle Investigation Example Template.pptx and link location in JIRA description.

## Links and References

## General

Incident Troubleshooting and Resolution Tracking. - Engineering Function - Confluence

Flight Data Processing and Review - Engineering Function - Confluence

FDR Tool

How to use FDR Tool Automated Flight Data Processing - Engineering Function - Confluence

## This Investigation

Past JIRA link here: VXE All Efforts - Agile board - Jira (atlassian.net)

SharePoint folder link: Flight Safety - VXE-438 Lift motor failure resulting in crash - All Documents (sharepoint.com)

Investigation (this document). Listing here makes the link easier to send.

## Key Process Steps

More detailed process guide. https://jenaero.atlassian.net/wiki/spaces/EF/pages/23363854/Incident+Troubleshooting+and+Resolution+Tracking.

Fields that are in this doc and JIRA (such as investigation plan) should always match. JIRA is more efficient for viewing quick status and next actions, so it is important to always keep the key fields updated. When you update one, please update the other. JIRA should be the most recent. Please fill out the following and keep them updated as you continue troubleshooting. Some of the fields have the circled i icon. More info can be seen by hovering over it.

Assignee-if you are assigned a high priority issue. It is your responsibility to keep the troubleshooting moving and updated, either by performing the steps requested, listing additional steps, and/or finding someone else who would be better suited to identify or perform the next steps, then assign it to them.

Investigation plan: Investigation steps planned. These can be deleted when the steps have been performed and findings added. New steps should be added as the investigation continues.

Investigation status: Status of testing. Important information discovered. Potential causes. Factors determined not to be potential causes.

Create folders and add links according to 1.2.2.

Create a copy of this document in the sharepoint folder created before making any changes. Please do not add investigation information to the template file.

Paste those links to the top of the JIRA description field as well.

Make a copy of this document in the sharepoint folder. Title according to incident name and description.

Proceed with Investigation in Order Listed Below

Investigation Overview

Fill out as investigation progresses.

Each investigation is different, so the process is unique to each. In general, they often start with data review to identify possible causes. If cause is not clear, the next step will often be equipment inspection and test.

If submitting this document to an outside party, delete sections 1.1-1.3.

## Summary

Limited information as stated by customer:
A lift motor failed that resulted in significant damage to the AV

AAR files attached: VXE-438

Working with customer on potential return of ACFT for investigation

## Status (should match JIRA field exactly)

Initial insights, it looks like landing was paused continuously from the start of the descent to the moment the VTOL system failed. About 6 seconds before the VTOL AP stopped logging data the landing pauses were ignored due to low energy. Unfortunately, the datalog stopped about 10 seconds earlier, so I don’t know what the voltage was at that time. It had been at ~25V for a while during the pause.

We do have logic that aborts a pause if the battery gets too low. Log says it is ignoring the last couple pauses, then log ends. 6 seconds before impact. VTOL log Data log is ~10 seconds behind. XCOM log is all there.

but I recommend zooming into the pause timeframe and plotting current, throttles vs expected current, etc. Does it seem like the battery died or that a motor assembly gave out?

## Plan (should match JIRA field exactly)

Create sharepoint folder, investigation word doc. Link to description. VXE-438

Upload to doc the following plots.

Zoom into power fault section. Plot current and throttles as well. 24V is low, but should not be low enough to lead to a lift failure. Oscillation is concerning.

I recommend zooming into the pause timeframe and plotting current, throttles vs expected current, etc. Does it seem like the battery died or that a motor assembly gave out.

While logged battery pack voltage was not low enough to cause an issue, an individual weak cell could be lower and have emptied sooner. Check cell voltages in log.

ESC overheat during extended pause. ESCs can usually handle extended hover times, but one with high resistance connections or FETs might not. Review throttle vs current to see if specific ESCs were failing, or due to power fault.

## Root Cause (should match JIRA field exactly)

Hypotheses

While logged battery pack voltage was not low enough to cause an issue, an individual weak cell could be lower and have emptied sooner. Check cell voltages in log.

ESC overheat during extended pause. ESCs can usually handle extended hover times, but one with high resistance connections or FETs might not. Review throttle vs current to see if specific ESCs were failing, or due to power fault.

## Corrective Actions (should match JIRA field exactly)

None

Need to resolve to close this investigation

CA 1 (each of these should be a link to an associated JIRA task.

Related improvements. Closure not required to close this investigation.

CA 2 (each of these should be a link to an associated JIRA task.

## Investigation Overview

Format (replicate the fishbone image below in a numbered list.

Potential Cause 1

Potential Cause 1 Detail 1

Potential Cause 1 Detail 2

Potential Cause 2

Potential Cause 3

## Timeline

Plots and event logs in sequential order describing the order of events and supporting data. Label stages and key events.

## Investigation Details

## Potential cause 1

## Potential Cause 1 Detail 1 Information under here should relate to 1.1 on the fishbone list

Battery Vmin is about 23.71V. This should be fine.

Next we looked at cell voltages. Cell voltages, with slight variations; look ok. Individual cell voltages are consistent indicating that there does not exist a weak cell that brings down the battery voltage. It is unlikely that this would cause a failure.

However, the current plot below shows some disturbing data. A 210A current peak seems very high for a descent. We should compare this reading to existing profiles to see if this is ok.

Compare commanded to expected (using throttle) power

It also seems that Throttle 2 remained ON while the throttle to other three motors was low, this could have caused the craft to crash.

Below is the plot for Ibat and altitude. Had to plot them separately because of scaling issues.

Power expected (based on throttle) vs actual comparison.

X= PWM

Y= power out (watts)
y = 0.0023x2 - 4.7378x + 2452.9

To covert from throttle value in vtol log to PWM

PWM = (Throttle value) * 855 + 1000

Plots for above calculations:

## Interim notes

Some observations follow:

Aircraft was badly damaged. Both front motors were damaged and one VTOL prop (Right Front) was broken.

It seems that some unauthorized work was done on the aircraft apparent from non-standard tape used.

Nose cone was also damaged and was difficult to remove after removing the 5 screws. We did not open the nose cone.

Front Right ESC was opened. Everything looked good, no loose wiring, no burn smell. We tugged on each wires to connectors, no loose connections found.

We opened the center wing lid. Again, everything looked ok, however when we tried to connect to the VXE-438 aircraft on 10.129.182.10 address (we also tried .181 and .183 addresses) we got no response. We were planning to use a different fuselage since we could not open the nosecone of this one but stopped there.

At this point, Garrett and I got pulled into other project so I closed various parts and packed the aircraft in cases.

## Further investigation

Managed to connect to center wing as well as the fuselage XCOMM. Our earlier problem with connecting to center wing came due to this center wing being a replacement wing and had a different IP address (10.143.191.10) Once we tried there, we were able to connect to the XCOMM. We ran all 4 motors and they seem to work fine. Fuselage was badly damaged. It seemed to have suffered an impact on spinner (Prop blades were not damaged) Even with this, we were able to connect to the XCOMM computer on IP address 10.129.182.3.

## Further investigation 3/21/24

Plotted graphs of few more variables and looked at a few suspects. There seems to be a lot of current spikes on 12V supply.

Looking further at spikes in vtThr2 and I12V they don’t seem to be related.

Returning to the main power, the current spikes are about .9-2 sec wide and lowest dip in battery voltage is about 23.6V, recovering back to about 26V. This is unlikely to be the cause.

My next steps in the investigation will be to run a similar power profile on a normal EXC and the one from VXE-438 using a Dyno to see if this could have caused any solder failure.

## Suspect conditions requiring further investigation.

Following is a list of parameters that need further investigation.

## apIbatt, apPower swings. apIbatt peaks of 45amps, power peaks of 1158W during takeoff. While these seem like high current states, the problem only seems to occur during the takeoff so this may not be a problem.

## vtIBatt peaks at takeoff and landing.

Here is the zoomed in view of power activities during these times.

Further investigation is done for Current and power during these periods

<<power and Energy calculations>>

## vtThr2 remaining high during landing

If Throttle 2 remains high while other three are low, it is likely the reason that the aircraft toppled and lost control. This is really a suspect parameter and may indicate something wrong with the Autopilot. Here is the zoomed view:

This is indicated by Autopilot GPS Vertical speed apgpsVs below:

## I12V transients following spike in I12Vaux current.

There is a suspicious oscillation on I12V and it seems like it is followed by high current spikes in I12V Aux. Here is the zoomed view:

## apEr swings

This parameter is for the craft attitude and seems to indicate that the aircraft tumbled after the Throttle 2 remained high. Here is the zoomed view:

## Conclusion.

I haven’t found anything in the aircraft to point to why it failed. All I can see from the logs is:

There was a narrow, huge spike of 210A

While landing, three throttle signals were low but forth (Front Right) throttle was high.

12V switched and Aux seem to be unstable
