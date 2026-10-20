# XComm MAVlink-Retransmit-Overview.pptx

Attachment 23480, pptx, 774 KB, added 2024-09-25 by Jason Scherer.

## Slide 1

XComm MAVlinkRetransmission of Unacknowledged Messages
Overview & Change Proposals Presentation
[picture]
[picture]
[picture]

## Slide 2

Background
[picture]
[picture]
[picture]
Existing CAN Implementation on XComm, does not validate successful delivery of messages.

This can lead to situations where a state machine (e.g. launch) can continue without delivery of a critical message.

This was discovered when the SAFE Off message was not received by the VTOL autopilot prior to launch which resulted in an ARMed but SAFE state that prevented launch.

Imagine if the Operator tried to safe the motors, but the message never got to the VTOL… Maybe the blinking light of danger would prevent approach, but this could very easily be a safety issue.

## Slide 3

[picture]
[picture]
[picture]
[picture]
[picture]
[picture]
XComm receives a RCS_LAUNCH command from fixed wing
Next Slide
ApmParser::Poll() runs at 10Hz
XComm Launch State MachineHow XComm starts the launch state machine

## Slide 4

[picture]
[picture]
[picture]
[picture]
XComm CycleLaunch() State Machine
Sends Mavlink Messages from each state. Then advances without confirmation.

## Slide 5

Current Design (existing code) 1How Xcomm Sends Mavlink Messages
[picture]
[picture]
[picture]
[picture]
[picture]
Example: A function (SendSafteySwitch) that sends a mavlink message
Each MAVlink message has an incrementing sequence number in the header
Next Slide
[picture]
[picture]
[picture]

## Slide 6

Current Design (existing code) 2How Xcomm Sends Mavlink Messages
[picture]
[picture]
[picture]
[picture]
[picture]
[picture]
Next Slide

## Slide 7

Current Design (existing code) 3How Xcomm Sends Mavlink Messages
[picture]
[picture]
[picture]
[picture]
[picture]
[picture]
Data Queued For Tx

## Slide 8

Current Design (existing code) 4How Xcomm Sends Mavlink Messages
[picture]
[picture]
[picture]
[picture]
[picture]
Data Dequeued For Tx

## Slide 9

Design Change Proposals
[picture]
[picture]
[picture]
Modify State Machine to prevent state advancement until SAFE Off state is achieved.
Small change, add another state after sending SAFE Off that checks gApmStatus.Options

Implement retransmit, for all CAN messages, if no acknowledgement is received.
Initial concept: Create a new queue (or rework the existing one) to hold messages that have not been acknowledged using the sequence number. Then have the transmit task periodically check to see if sufficient time has passed with no acknowledgement. If so, resend the message with a new sequence id in the header.
Could have a hybrid approach that only checks for retransmit of important messages.
Big change.
Effects all Mavlink messages transmitted from Xcomm
Could add congestion to the CAN bus with retransmits. Might need MAX_TRANSMIT = 3?
What happens if retransmits fail. How do we stop state machines from advancing?
