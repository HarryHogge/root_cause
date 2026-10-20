# VXEP-596: Review and improve launch wizard criteria and checks to identify faulty motor/ESCs before launch.

- **Issue type:** Corrective Action
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2024-09-03
- **Updated:** 2025-08-05
- **Resolved:** 2025-08-05
- **Reporter:** Cameron Chapman
- **Assignee:** Rajesh Budhabhatti
- **Creator:** Cameron Chapman
- **Parent:** VXEP-384 VXE 545 Commanded aborted launch due to unusual behavior on ascent

## Plan

@Rajesh Budhabhatti the document and analysis looks good. Can you please summarize the following in the conclusion.
Your recommendations for the following:
- PWM to run the rest
- Duration
- Measurement point in the test (when to start and end measurement. Average?)
- max and min power. (pass/fail ranges)
- Validate those measurements on a variety of ESCs in passing condition (vary age, performance, etc).

## Comments (7)

### Rajesh Budhabhatti, 2024-09-19

I am deriving a set of formulas that software can use to compare the expected current for various SOC and throttle values. I generated a set of readings for SOC 24V-30V for various throttle values. Now I am checking if using these check the software could have detected the issue with VXE545. I will upload the spreadsheets and white paper when done.

### Rajesh Budhabhatti, 2024-09-20

Here is a method to evaluate the ESC health based on current measurements. A method for evaluating ESC health through current measurement.docx

### Cameron Chapman, 2024-09-20

@Rajesh Budhabhatti the document and analysis looks good. Can you please summarize the following in the conclusion. 
Your recommendations for the following:
- PWM to run the rest
- Duration
- Measurement point in the test (when to start and end measurement. Average?)
- max and min power. (pass/fail ranges)
- Validate those measurements on a variety of ESCs in passing condition (vary age, performance, etc).

### Rajesh Budhabhatti, 2024-09-20

Excellent input. Yes, will do. Thanks.
Get Outlook for iOS<https://aka.ms/o0ukef>

### Rajesh Budhabhatti, 2024-09-23

9/23/24: 
Simplified the pass/fail criteria and motor fault detection based on the recommendations above. I used an old motor to take my readings. Tomorrow I would like to try out a brand new motor-esc pair and check if there is a difference. I would also like to take an EOL motor and force a soft-start circuit fail to generate the readings in case of such a fault and using these readings refine my pass/fail criteria. Updated doc here: A method for evaluating ESC health through current measurement.docx

### Pat Wells, 2024-09-26

@Cameron Chapman Just completed the customer meeting that we discussed.
A small list of questions was generated:
1. Have we previously investigated a soft start issue with the ESC’s?  Matt Curran @LM thought he recolected that we did.
- In the report under Corrective actions we list Remove or bypass soft start circuit.  Are we considering this? Would it require new hardware or a software change?
- Which CA are we chosing to implement?
- Are there any work arounds from an operator’s perspective.  What should they be looking for? Anything to do special or not do?

### Cameron Chapman, 2024-09-26

Responding to Pat in parent ticket

## Attachments (0)
