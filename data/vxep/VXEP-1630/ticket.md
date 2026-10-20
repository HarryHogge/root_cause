# VXEP-1630: VXE-920 Two separate incidents of near miss during fixed wing to Vtol recovery transition. Seemingly due to motor/ESC assembly-No investigation planned

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2025-12-09
- **Updated:** 2026-07-20
- **Resolved:** 2026-07-20
- **Reporter:** Michael Mohr
- **Assignee:** Scott Lovett
- **Creator:** Michael Mohr
- **Labels:** GS_Closed, NSW, RCCA, Weekly-incident-tracker
- **Links:** relates to VXEP-628 (Systemic VXE30 VTOL ESC Reliability Issues ); relates to RMA-859 (VXE-920 RMA 251209-2)
- **Customer:** NSW
- **Vehicle Tail Number:** VXE-920
- **Incident Type:** Near Miss
- **Severity:** 1 - Flight Critical
- **Components (EA Aircraft):** Aircraft, full assembly

## Description

On two separate days during two separate flights, VXE-920, while transitioning to VTOL for recovery, abruptly nosedived during the transition from fixed wing flight to VTOL. Minimal winds were present both days with a 200 foot transition altitude. 
Video corresponds to first flight

## Vehicle Configuration

Advanced Nav
VXESUAV
Battery 
E95 gimbal

## Plan

2026-04-24 Customer is not interested in C/CA. We likely don’t have bandwidth to troubleshoot ESCs that we are trying to replace with more reliable designs. Closing this issue.  @Scott Lovett ok to close this issue?

## Comments (34)

### Michael Mohr, 2025-12-09

We are on site with customer conducting IQT for today and tomorrow. Would really appreciate a quick diagnosis and resolution. @Drew Hildreth @David Grosher @Jeremy White

### David Grosher, 2025-12-09

@Eric Brewer Can you take a look at this?

### Alexander Alan Arnold, 2025-12-09

[embedded: image-20251209-200502.png]
from the 9DEC AAR, apAgl looks out of sync, wondering if this is normal or if I am interpreting the data correctly. @Eric Brewer

### David Grosher, 2025-12-09

@Alexander Alan Arnold It looks like there was an issue loading data to/from the database. The CSV data looks fine.

### David Grosher, 2025-12-09

It is really hard to visualize in Excel, but it appears that the Lift system doesn’t start pulling current for about 2-3 seconds after non-zero lift system commands are being sent. @Eric Brewer

### Alexander Alan Arnold, 2025-12-09

in the xc251209 log there is no serial number or tail number present in the start up, is that indicating a fault of anything? I only ask because the 12/8 startup has tail number and SN present. @David Grosher

### Alexander Alan Arnold, 2025-12-09

[embedded: image-20251209-203635.png]

### Cody Smisek, 2025-12-09

@David Grosher Jeremy and I were sniffing around same thing, primarily looking at M3 given the video. Hard to tell what’s going on there.

### Cody Smisek, 2025-12-09

@David Grosher 
[embedded: image-20251209-204155.png]

### Jackson Riley Curvin, 2025-12-09

@David Grosher @Cody Smisek I'm not sure if this is relevant but on the previous XCEVLOG the Novatel resets
[embedded: image-20251209-211624.png]

### David Grosher, 2025-12-09

@Michael Mohr This vehicle should be grounded. The RR motor/ESC has a significant lag.

### Michael Mohr, 2025-12-09

@David Grosher We grounded it after the incident today. Is there grounds for RMA? Aircraft is currently near Paso Robles.

### Alexander Alan Arnold, 2025-12-09

is this caused by the ESC or the motor. Would a motor replacement be viable or do we need to send it in?  These are brand new aircraft @David Grosher

### David Grosher, 2025-12-09

@Michael Mohr Yes, it should be RMAd

### David Grosher, 2025-12-09

@Alexander Alan Arnold That is unclear at the moment. I think it should be sent it because it will require some level of test and validation that would be best to be performed without a customer around. I don’t think the fact that they are new is going to impact the path forward.

### David Grosher, 2025-12-09

@Jackson Riley Curvin That is an intentional reset that happens when the FW AP is reset during the Launch Wizard.

### Michael Mohr, 2025-12-09

@David Grosher We’ll start the RMA process through @Lauren Velasquez and either myself or @Jeremy White will deliver to SLO.

### Michael Mohr, 2025-12-10

Aircraft delivered to SLO on 12/09/2025 in the afternoon.

### Cody Smisek, 2025-12-10

@Rajesh Budhabhatti

### John Clark, 2025-12-10

image image-20251209-211624.png may not pertain to the problem @Michael Mohr @Cody Smisek  Reset originated from GCS
[embedded: image-20251210-201132.png]
[embedded: image-20251210-201211.png]

### John Clark, 2025-12-10

Gosh I hate these. I’ve asked Eric Brewer for help.[embedded: Vt00027.docx]

### John Clark, 2025-12-17

Steps performed by Software Engineering to validate the esc firmware.
- Compare the original files. - All 4 files compare identical
- Compare the JaiVtolEsc_050220.hex to one translated file.
- The first file line differs - That is a record type field and is an artifact of the avrdude down load using an extended address. (Why it had to be translated)
- The line at address 0x11F0 differs in that the avrdude read file contains some unwritten flash. The written lines match
- The block of memory from address 0x1200-0x1BF0 included in the avrdude read file shows as unwritten flash. That memory is not included in JaiVtolEsc_050220.hex

None of the items mentioned indicate any differences or corruption of the flash

### Michael Mohr, 2026-01-02

@John Clark @David Grosher Are we any closer to finding a root cause and corrective action on this? The unit is scheduled to fly on 9 January and is wondering the status of the aircraft?

### John Clark, 2026-01-02

@Michael Mohrthe analysis of the esc motors is ongoing by hardware. @Rajesh Budhabhatti is leading that effort. The motor software was established not to be at fault. Can you reach out to the hardware team to get their status? Technically I am OoO today. But if I can help, please let me know.

### John Clark, 2026-01-02

@Michael Mohr I pinged @Rajesh Budhabhatti to update the ticket.

### Rajesh Budhabhatti, 2026-01-06

After extensive testing on dyno I found motor/ESC in position 1 to be faulty. Occasionally the motor would not respond to the PMW command with appropriate rotation RPM during the second start (Landing phase) This fault, ie. motor not turning when PWM command issued will last for a short while 1-3 seconds. Thereafter the motor will respond to PWM command normally. It was noticed that the fault primarily happened when motor was cooled down but not on power up. Motor/ESCs in position 2-4 did not have this problem. I also ran the motor 1 profile on other motors as well as motor 2-4 profiles on motor 1. In each case, it was the motor/ESC position 1 that displayed this fault so it was decided that the fault was caused by the motor/ESC and not the flight profile. Here are two spreadsheets with testing data. 920 incident VXEP-1630

### Cameron Chapman, 2026-01-06

@Rajesh Budhabhatti  will red tag and keep motor+ESC1 in case more investigation is needed and to make sure it is not mixed up with other equipment.

### Lauren Velasquez, 2026-01-22

@Cameron Chapman  We are eager to get this repaired- Nothing is red tagged on this AC. @Rajesh Budhabhatti Are you able to come down and identify which motor needs to be replaced as there are several loose in the transit case.
Thanks! @Ronnie Baker  @Drew Hildreth FYSA

### Rajesh Budhabhatti, 2026-01-23

Motor 1 needs to be replaced. Loose motors were tagged Right/left boom I’ll go to RMA and sort this out.

### Rajesh Budhabhatti, 2026-01-23

OK, sorry about not entering more details. Here is it.
Motor/ESC position 1, Left Front, CW S# C-S110569 Faulty. I have this motor/ESC. Replace it with a new Motor/ESC P# 107-101631-1
Motor/ESC position 2, Right Front, CCW S# C-S110595 good. Currently in the case.
Motor/ESC position 3, Right Front, CW S# C-S110572 good. Currently in the case.
Motor/ESC position 2, Right Front, CCW S# C-S110594 good. Currently in the case.
Please ensure that all motors have bushings in place. These have tendency to fall off.

### Cameron Chapman, 2026-04-23

@Lauren Velasquez  do you know if RMA, NCR cage, or engineering has this faulty motor/ESC?

### Lauren Velasquez, 2026-04-23

@Cameron Chapman Just checked our scrap bin- Nothing with the Removed SN. Maybe NCR Cage?

### Alexander Alan Arnold, 2026-07-20

This aircraft was RMAd and reworked, aircraft then experienced a separate issue resulting in crash. 920 is being replaced by entirely new airframe. closing ticket.

### Alexander Alan Arnold, 2026-07-20

motor/esc was swapped aircraft crashed for different issue

## Attachments (10)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T115_V920_251208_123657_pack.zip | archive | 2417 | 2025-12-09 | listed only |
| T115_V920_251209_095013_pack.zip | archive | 2345 | 2025-12-09 | listed only |
| VXE-920 video 12082025.mp4 | video | 4535 | 2025-12-09 | listed only |
| image-20251209-200502.png | image | 42 | 2025-12-09 | listed only |
| image-20251209-203635.png | image | 25 | 2025-12-09 | listed only |
| image-20251209-204155.png | image | 113 | 2025-12-09 | listed only |
| image-20251209-211624.png | image | 63 | 2025-12-09 | listed only |
| [Vt00027.docx](attachments/36681_Vt00027.docx.md) | docx | 706 | 2025-12-10 | converted |
| image-20251210-201132.png | image | 16 | 2025-12-10 | listed only |
| image-20251210-201211.png | image | 16 | 2025-12-10 | listed only |
