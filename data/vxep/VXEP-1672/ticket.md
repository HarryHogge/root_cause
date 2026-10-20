# VXEP-1672: Status and POC of Colbourne Projects

- **Issue type:** Major Project
- **Status:** New
- **Priority:** High
- **Created:** 2026-01-29
- **Updated:** 2026-08-24
- **Reporter:** Cameron Chapman
- **Assignee:** Scott Gordon
- **Creator:** Cameron Chapman
- **Links:** relates to VXEP-1855 (APD ESCs connect CAN RTN to 56V RTN and should not.)

## Description

Updated 2026-08-24
 @Scott Lovett please update each of these as we progress and statuses change. FYI @Nigel Goodison @Jason Colbourne 
| Colbourne Priority | Item | Date Updated | Status | Plan | POC | Link(s) |
| 1 | EMI : B35 461 Test Planning execution | 2026-08-24 | Beginning Day 7 - most parts have arrived.  To date, no red flags. | Begin chamber work this week. | Jason, Fernando, John F. , Daryl |  |
| 1 | BATTERY  electronics review and roadmap - Specifically 28V capacity and other issues. | 2026-08-24 | Cliff is finalizing the rework on Rev 3 boards and hoping to have them back to Stephen Peters tmrw.   Abel has begun endurance testing, and identified an issue with the output switches.  They are shutting off at 3 amps (designed to limit at 7 amps).  This does not appear to be a hardware issue; exploring if it is a software control.  Cliff has documented revisions to be applied to Rev 4. | Complete Rev 3 and finalize design Rev 4 | Cliff , Fernando, Jason, John |  |
| 1 | Gimbal | 2026-08-17 | Tracing issues from the Novatel which is impacting the Mani. | Troubleshoot and resolve issues with Gimbal. | Abel, John |  |
| 4 | CAN noise reduction/isolation | 2026-06-30 | Unable to replicate failure.  Hotswapping does not appear to be the issue.  Potentially an issue with the diodes.    Testing continues. | Continue to test, adding additional components to ensure efficacy and consistent behavior. | Abel, Cliff, Jason, Frank, John |  |
| 5 | Riga team payload support. |  | See roadmap | See roadmap | Abel, Grant G | https://jenaero.atlassian.net/wiki/spaces/PDAO/pages/edit-v2/1013907463 |
| Hold | Discuss UAP project |  | Hold |  |  | 1 |

| Done | SSR boards | Moving to limited production.  All Rev D issues resolved.  No open actions. | Colbourne hopefully done. |  |  |  |
| Done | Advanced network board (Plan A). | 2026-06-25 | - All operable Rev D boards have been shipped to RW SLO.  Remaining boards at CC have data output anomaly which CC will continue to troubleshoot. - CC has finalized build of test setup. |  |  | https://jenaero.atlassian.net/browse/XKIT-4502 |
| Paused | BATTERY : Help Define operational range of batteries | 2026-08-09 | Fernando has pulled together multiple requirements sources, and is consolidating them into a single document.  Next step is to review, triage, then present to broader group. | Comprehensive performance evaluation of batteries, including bench testing  and requirements documentaiton. |  | [BAT-953] Define operational range of B40 batteries and 28V converter (power limits over expected temp range, CAWs, automatic behavior, etc). - Jira |
| Done | Simplified Network Board (plan B) | 2026-03-18 | @Frank Sundell can you please link requirements for this board. KMS will have remaining 30 boards ready for shipment by Friday 3/13. | Delivered to RW SLO. | Jason C | https://jenaero.atlassian.net/browse/XKIT-5240 |
| 3 | BATTERY: SOC support | 2026-07-21 | SOC Algorithm appears to be stable.  Recommend bench test to confirm SOC algorithm is working correctly. Coordinating planning for SOC support, as needed.  Fernando, Frank, and Abel continues to support . | Fernando has put together several ideas for battery optimization + weight reduction | Abel and Fernando | https://jenaero.atlassian.net/wiki/spaces/PDAO/pages/edit-v2/998080555 |

## Comments (0)

## Attachments (0)
