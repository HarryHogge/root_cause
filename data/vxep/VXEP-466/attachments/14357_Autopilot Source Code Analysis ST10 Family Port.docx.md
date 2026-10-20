# Autopilot Source Code Analysis ST10 Family Port.docx

Attachment 14357, docx, 46 KB, added 2023-05-03 by John Clark.

Autopilot and XComm Source Code Analysis

Project Number: N/A

Key Players/Roles:

| Project Lead |  |
| Mechanical Design/Testing |  |
| Wire Harness/EMI Testing |  |
| Technical QA / Feedback |  |

Job Number:

| Design/Meetings/Purchasing |  |

Description

Provide a breakdown of Porting ST10 Code VXE30.

Scope of Work

Objective and Deliverables:

This document

Block diagrams of Interfaces and Modules and Functions

Possible Flow Charts or Flow Block analysis of program variables associated with operation

Active Tasks:

| Action | Owner |
| Code Analysis | John Clark |
|  |  |
|  |  |
|  |  |

## Introduction

The ST10 is the Fixed Wing Autopilot micro controller, specifically an ST10F168 running at 20 Mhz. The target microcontroller is a PIC32MZ with a maximum clock of 250Mhz. This document is a high-level examination of porting this source code to PIC32MZ as is used in both the current XComm and VTOL AP’s. If the Fixed Wing Autopilot is a true bare metal program, then there are certain assumptions we can make.

Its primary construct is a simple primary loop and that any modular priority within the loop is a function of some round robin mechanism that would assign multiple iterations within the primary loop.

Memory management is entirely predefined within a single environment (Stack) and global memory. Any dynamic allocation would be within the single environment (Heap) through malloc() and free().

Interrupts, while having priority and environments (Stack) defined by the microcontroller architecture are asynchronous and run ‘mostly’ independently of the primary loop. The exception would be control or possible ‘reenable’ after an ISR.

The strategy would be to fully abstract the primary loop from the architectural portion (interrupts) and hardware interfaces (I/O) to isolate it. The primary loop may then be considered at its ‘edges’ where requirements are defined as inputs and outputs into a black box.

## Hardware Interfaces Outputs/Inputs

Planned reuse drivers from Red Board

Act1-8, GP I/O (PWM bit banged)

ACT_1 – Right Aileron

ACT_2 – Elevator

ACT_3 – Retract

ACT_4 – Right Flap (Block 25)

ACT_5 – Left Aileron

ACT_6 – Rudder

ACT_7 – Left Flap

ACT_8 – ECS Signal

Beep, GP I/O - Speaker

RAD_CH0-2, GP I/O (appears Bit banged)

IMU – CS

IMU – SCLK

IMU – MOSI

IMU – MISO

P7 0-3

P7.0 – Aux 0 - Blink

P7.1 – Aux 1 – TP8 (unused?)

P7.2 - GPS Reset

P8 4-7 NEO-M8 GPS BOARD (I believe this to be the SW Uart)

P8.5 – TIMEPULSE

P8.6 – Rx0

P8.7 – Tx0

XComm UART - PRIBAUD 125000L

ASC0_Rx

ASC0_Tx

AP_VBUS (unused?)

CMD_Tx

CMD_Rx

SP_ENABLE – I/O

ST2 – AD_GYRO (not used?)

LEDs -I/O

P2.10 – RED

P2.11 - GREEN

## Hardware Interrupts

## Timer 1

Timer 1 free runs and is used by the RTC, rc input, and servo outputs. At this time I believe the Servo PWM pulses are generated through bit banging the ports identified above and that the PWM channels native to the microcontroller are not used

AD (Analog to digital conversion?)

RC (Realtime Clock?)

SWUART(GPS?)

UART – I suspect this uses a clock divisor. But that the interrupt itself is asynchronous

Clk (System)

## Description of Overall Architectural Incompatibilities

## Bootloader

The PIC32 uses a Bootloader as an entry-point and for reprogramming. The ST10 does not have a Bootloader. Recommend using a port of PIC32 Autopilot/XComm Bootloader.

## FPU

The PIC32 uses an on-board floating-point unit. Recommend disabling that.

## Memory Model

The PIC32 has an on-board MMU mapping a multi-segmented cacheable/non-cacheable memory space. Recommend a simple write through cache implementation, or complete disable. Run the FW AP from a single segment.

## NVM

The ST10F168 uses a 256-word page NVM structure that consists of 4 pages of ‘Gains’ shared throughout the system. The general structure would need to be maintained while providing a local implementation and mapping. Sufficient space exists in PIC32 Program/Boot Flash and it appears that certain Pages could be unprotected for modification.

## PWM

The ST10F168 appears to use a ‘bit banged’ PWM model regardless of approach a method must be created to generate PWM to the ‘ACT_X’ interfaces.

## UART Interface (To XComm)

The ST10F168 uses a 125K Bps interface to the XComm. To preserve that a hardware interface would need to be selected and configured. A driver would be necessary.

## Discussion of Architectural Compatibilities

## IMU

Both PIC32 and ST10F168 utilize the 9250 IMU over a SPI interface.

## GPS

Both PIC32 and ST10F168 utilize the same GPS protocol. The ST10F168 is using a soft UART, I think. That can be ported to a hardware UART using the driver from 2.6.
