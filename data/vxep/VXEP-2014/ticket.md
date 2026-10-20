# VXEP-2014: VXE 967 had an issue when upgrading to FW 6.7.1

- **Issue type:** Incident (8D)
- **Status:** D2 - Gathering Information
- **Priority:** High
- **Created:** 2026-10-06
- **Updated:** 2026-10-20
- **Reporter:** Stephan Johnson
- **Assignee:** Alexander Alan Arnold
- **Creator:** Stephan Johnson
- **Labels:** RCCA, Software, USAACE_(2-13th), Weekly-incident-tracker
- **Links:** Cannot finish until linked issue is finished. RMA-1114 (VXE-967 RMA 260923-1); relates to VXEP-2015 (VXE 635 Would not connect to VTOL AP following upgrading to FW 6.7.1)
- **Customer:** USAACE
- **Vehicle Tail Number:** VXE 967
- **Vehicle Configuration:** VXE30 Adv Nav
- **Problem Type:** Other (explain in description)
- **Incident Type:** Other (Record"Event Type: XXXXXX" in the description)
- **Severity:** 4 - Annoyance
- **Executive Summary:** A/C returned for RMA

## Description

After VXE 967 was upgraded to 6.7.1 firmware and after power cycling after updating the Xcomm, they could no longer connect to the aircraft in SUAV, and the OGCS page would not open. 
They were able to ping and log into the .3 and .10 addresses on the aircraft. In SUAV the tail number displayed but when attempting to connect they received the error message "vehicle not on network". When attempting to connect in OGCS the webpage would time out and not open. The .30 and .2 were not responsive to ping commands. I had them attempt on the default MCM addresses but it was also unresponsive. This behavior was seen after three power cycles and two separate GCS laptops.

## Comments (14)

### Alexander Alan Arnold, 2026-10-06

@Eric Brewer @Ryan Smith this was one of the customer reported failures after updating to 6.7.1, aircraft is in SLO

### Ryan Smith, 2026-10-06

@Alexander Alan Arnold Did you attempt to recover the xcomm through the apbl application? The xcomm is on the 192.168.10.72 address so the network would have to be configured for such. Another item to check would be the 10.128.1.2 address if the aircraft returned to factory default (which would happen if fwap gains upload didn’t work as expected). Odd the vtol system is accessible but not the mcm…

### Alexander Alan Arnold, 2026-10-06

I am not in SLO and cannot attempt the recovery. We also do not have apbl application. We can have the RMA team work with Carson to attempt these steps I believe @Ryan Smith

### Alexander Alan Arnold, 2026-10-06

@Lauren Velasquez can you see if Carson or an SCO personnel member can assist with Ryans troubleshooting?

### Ryan Smith, 2026-10-06

@Alexander Alan Arnold I just realized you said aircraft in slo previously, thank you! I for some reason read aircraft is in transit

### Mathew Papaleo, 2026-10-08

@Alexander Alan Arnold i invoked the bootloader and was able to get the xcomm online. then i was able to connect to suav. i updated the xcomm to 4.72 on my suav running 6.5. 
then i grabbed a rugged laptop running 6.7.1.  xcomm updated without a hiccup. fwd ap was up to date. vtol controller was on 1.58, new version is 1.60-- update completed. 
performed all actions with avionics box open, to observe standby lights or whatever they are called to look for certain behaviors. 
im ready to close the box back up. please advise next steps @Ryan Smith @Lauren Velasquez

### Alexander Alan Arnold, 2026-10-08

@Mathew Papaleo Can you provide the software and steps to @Zachary Mann in the event we have this happen again? also does this require the avioincs to be opened for the rework?

### Alexander Alan Arnold, 2026-10-08

@Ryan Smith Do we understand why the failure happened? and do you think we should replace any of the board before sending this to back to the customer? @David Grosher FYSA

### Mathew Papaleo, 2026-10-08

@Alexander Alan Arnold ill work with zach; 
yea we need to reach a header on the xcomm. ill give him a jingle and see how we can help

### Ryan Smith, 2026-10-15

@Alexander Alan Arnold @David Grosher @Lauren Velasquez @Mathew Papaleo Full report is posted at the confluence below but summary conclusions are here:
- Pull data from SD card and grep for systemic issues for resets or CAN bus issues: None observed through entire SD card
- Upgrade downgrade many times: Performed 5 cycles due to time on 10/9/2026 and no issues seen
- Inspect MCM not reachable: Could not reproduce, ogcs v1.3.3 is operating as expected.
- Examine logs for what aircraft was doing/how got into state. Appears there was a bootloop state of the xcomm where it was not operating but the vtol was active.

https://jenaero.atlassian.net/wiki/x/KQDCU

### Alexander Alan Arnold, 2026-10-15

@Ryan Smith thank you Ryan! So, the boot loop state caused the issue? I guess we need Daves final approval before sending this back to the customer?

### Ryan Smith, 2026-10-15

@Alexander Alan Arnold  yes and that bootloop is what prevented connection to the aircraft through GCS.

### Drew Hildreth, 2026-10-20

@Alexander Alan Arnold Was this on your list for Dave to look at this week?

### Alexander Alan Arnold, 2026-10-20

@Drew Hildreth yes I believe we needed him to review Ryans data before releasing aircraft back to customer

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| (2026-10-09)_v967_xcomm_sd_card.zip | archive | 29882 | 2026-10-09 | listed only |
