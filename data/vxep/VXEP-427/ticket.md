# VXEP-427: VXE 430 abnormal landing behavior

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-06-07
- **Updated:** 2026-03-02
- **Resolved:** 2024-08-23
- **Reporter:** Pat Wells
- **Assignee:** David Grosher
- **Creator:** Pat Wells
- **Labels:** GNSS-Rate, RPGS, Romania, Weekly-incident-tracker
- **Links:** relates to FS2-1951 (Investigation - VXE 430 abnormal landing behavior); relates to VXEP-315 (VXE 459 Overshoot of LZ Mishap on landing, operator unable to nudge); relates to VXEP-412 (VXE 426 Overshoot on landing, becoming progressively worse)
- **Customer:** RPGS, Romania
- **Vehicle Tail Number:** 430
- **Issue Status:** Still investigating.  See latest summary slides here.
- **Incident Type:** Mission Failure/Abort
- **Severity:** 1 - Flight Critical

## Description

Received from Romanian customer: 
I am writing to you because we experienced an abnormal landing behavior with one of our birds. So, during the landing, after starting the descent, the bird command “Climb abord, lift system fault” and after that the bird started to fly at the altitude it was at that moment in a random direction about 500 m with the VTOL and Forward motors running. We command again RTB (the primary LZ was not followed instead the bird started heading towards the lunch point) and also after control activation we try to manualy bring back the bird (we couldn't figure out in those moments if the manual control worked). In the end we managed to land the bird, but we did not manage to understand this abnormal behavior and the error “Climb abord, lift system fault” (the bird was in the landing sequence, not the takeoff). Please help us to understand and for this I send to you some picture and the FDR with bought flights from that day.
AAR attached

Additional information received from customer on 6/11:

While the UAV was on the landing pattern, after passing IP5 and descending to 300ft, the VTOL system started, payload was retracted and then the UAV started to shift towards an uncontrolled direction, without being able to manually overtake the controls. The UAV drifted about 2 kilometers while gradually losing altitude and in the end we managed to activate User Landing Control and adjusted with small inputs to land on a sunflower field in order to avoid an accident. After landing, the UAV suffered small damages (broken transponder cable and light visible damage on the left Wing Tip). We have to mention that from takeoff to final touchdown, no errors were shown on the GCS.
 
We do not understand this behavior and between this flight and the last incident we did manage to take this UAV for a flight and everything went normal.
Please help us understand this behavior as soon as possible since todays incident resulted in damage to the UAV. We have attached some photos and FDR files, for a better understanding of the incident.

## Corrective Action

Long term:
Update software to ensure correct rate is used in GPS acceleration calculation.
Short term message for customers:
We have discovered a software issue where sometimes the GPS update rate to the VTOL autopilot is too low - 5hz vs. 10hz expected.  If this occurs, there is an increased risk of overshoot and poor tracking during landing.
In the case of 5hz updates, risk can be reduced, but not eliminated, by avoiding a long orbiting descent before the approach begins - i.e. fly a large figure 8 while descending toward the transition altitude before engaging autoland.  Minimizing vehicle bank angle during the figure 8 will help to reduce the impact of the slow GPS updates.
In the meantime, Edge Autonomy is working on a short-term software fix for the issue.

## Plan

Continue testing with autopilot software and ublox receiver to identify how GPS update rate can be reduced to 5hz inadvertently.
In the interim identify if there is a way to correct 5hz rate issue with existing software to allow customers to safely fly.

## Root Cause

Root cause of overshoot is a lower than expected GPS update rate.  This low update rate causes the GPS acceleration corrections to the INS to be incorrect, which in turn causes the vehicle to not pitch up enough during transition.

## Comments (22)

### Pat Wells, 2024-06-12

@Eric Brewer @David Grosher @Jason Scherer  Added another incident experienced by the customer on 6/11 to the description above.  Additionally added AAR and two GCS screenshots from this new report.

### Pat Wells, 2024-06-12

@Eric Brewer @David Grosher @Jason Scherer 
What does your preliminary slides translate to in terms of a message to the customer. They are very concerned at the moment and would like some type of feedback ASAP.
Are there any questions you would like me to ask the customer?

### Eric Brewer, 2024-06-12

@Pat Wells @David Grosher I put some suggested wording above.  I added a plot on slide 12 with a more shallow figure 8 before the approach, attitude errors are reduced some but still not great.  There is definitely increased risk to any asset that has this present, and we should be sure to communicate that to customers.  
We’re working to identify short-term workarounds to the issue.

### Pat Wells, 2024-06-12

@Eric Brewer @David Grosher just be sure that I understand this correctly.  Are you saying that once GPS update rate has dropped to 5hz it is that way permanently or is it random?

### Eric Brewer, 2024-06-12

@Pat Wells @David Grosher we’re still working to fully characterize the issue.  We have seen some cases where it starts at 10 and the rate will drop to something lower than 10, and in other cases it’s a consistent 5hz.

### Eric Brewer, 2024-06-12

@Pat Wells @David Grosher our recommendation is to roll out a config change ASAP to update the VTOL configuration settings to 5hz GPS.  This should ensure that the accel correction used is much closer to correct.  
We will need to implement this and test it on our end before rolling out to customers.
Longer term we will work on a software fix to ensure the update rate is calculated correctly in the accel correction.

### Eric Brewer, 2024-06-13

We also found some information on a ublox forum that indicates there may be an issue with the M8N where it automatically falls back to 5hz.  We did turn on more GNSS signals in the latest software so this issue is likely more prevalent with 1.54.02 but given it’s inside the receiver we won’t know exactly what triggers it.

### Pat Wells, 2024-06-17

@Eric Brewer @David Grosher as this issue seems to be linked to several other similar events I’m looking for some help on messaging to the customer.  This is our Romanian customer and they only have 2 aircraft, one of them being the aircraft involved in this mishap.  I’m not sure the suggested workaround is feasible since it involves them reading logs.

### David Grosher, 2024-06-17

@Pat Wells @Eric Brewer Given the number of related issues I think we should come up with a slide or two that describes the problem at a high technical level that will help the customer understand why changing a mission profile will help mitigate the impact of the bug. It will also help to keep the communication consistent between the different impacted groups.

### Eric Brewer, 2024-06-17

@Pat Wells @David Grosher I added a slide to the end of this presentation, pasted here for convenience.  Please review.
AV459_LandingOvershoot.pptx (sharepoint.com)

[embedded image-20240617-231258.png]

### David Grosher, 2024-06-18

@Pat Wells @Eric Brewer That slide is perfect. Pat, I think that slide along with the plan to produce the two updates (patch for 6.2.9 and structural solution in 6.3.X) should be the communication strategy. The reason we will do both is because some customers take a significant amount of time to upgrade.

### Pat Wells, 2024-06-24

@David Grosher 
Adding additional customer questions/ feedback after sharing the GNSS Rate issue slide with them.


- Considering the fact that in the last specific case that occurred during our landing procedure, the low rate GPS was the problem, as you indicated, could you please include into your graphs the date and the time series associated with our specific last flight and more importantly when we faced with that deviation? This would be helpful to include these graphs afterwards in our investigation;
- Taking into consideration that the aircraft has, in both cases, descended in orbits in the way that was programmed, taking the landing pattern as it should be, and in the end arriving at the vertical point designed right before the descending action, could this mean that the low rate of GPS has been over passed? Also, what GPS receiver have been analyzed, the one from the autopilot module or the one from the center wing? At that vertical point, the aircraft had a non-moving moment and even in case of its very low vertical speed, we think that a low rate of GPS shouldn’t have such impact in affecting the position… approx. 2 km away, like in our last case. At a cruise speed or dash speed we understand that the impact could affect the flight routes, but why for this last part of flight where we cannot talk about important movements/speeds? Do you take into consideration also other causes as well, or multiple causes that concurred in this specific situations?
- Why, in the first case on May 31, after activating the landing override we were unable to use the joystick commands and why, in the second case on June 11, we where unable to activate the landing override for long time even though the VTOL system has engaged and the aircraft was at the right vertical landing position?
- Why we received, in the fist case, the message “Climb abort, lift system fault” being in landing stage and not in launch stage and why we received, in the second case, no messages (even regarding the GPS)?!
- Why, in the first case, RTB was the solution and why, in the second case with no override control landing activated, commands like RTB, GO TO and U-drive was without response?
- It is possible to include with your next update software the possibility to use U-drive slider during the VTOL phases (attitude nudge was not possible in our last case), for descending and ascending, in order to take control of the drone no matter what the cause is and cancel the automatic paths, even at a low rate GPS or even from other causes that you might find. We need to be able to take control of the drone in any stages of flights as these situations could end wounding people not involved in these flights or even worse. Do you agree with this recommendation? Also, please include in your update the decimal degree option that should be shown in the bottom bar information (even it is as option for conversion, in the bar remains your US coordinates). We need our coordinates to make it easily finding the aircraft and not only.
- We understand your recommendations regarding orbits and racetracks for landing patterns, but what are the specific recommendations during the descending segment of the flight (when we were unable to take control using landing override window)? Is the Land Immediately an option in this specific situation to oblige the aircraft to start to descend and to take back the controls after applying this command? Please advise. What is your best course in this situations?
- Are you taking into consideration to eliminate also other causes that are not necessarily related to the aircraft itself, as for example a flight, a take-off or a landing that could have the same deviation into a suddenly spoofing area? Will be better as in the future to have a hardware update, hardware dedicated for anti-spoofing or even anti-jamming. I have seen your partnership with Safran, a company that has these types of solutions, but for sure in USA there are companies that can support you with this type of upgrade. How would be equipped the future Stalker or could be equipped the current birds with such of solutions?
- When are you going to release the new version of software  that could solve this GPS low rate? and are you intend to include also the possibility to use the new Forward Cruise Motor ESCs with improved heatsink (500-113205)?

### David Grosher, 2024-06-24

@Eric Brewer Can you address the technical questions below on this incident?

### Eric Brewer, 2024-06-25

@Pat Wells @David Grosher please review updated slide deck.  If you are OK with what’s in here we can package up the slides (excluding backup) and send to the customer.  
@David Grosher I’d like to make sure you’re comfortable with my wording around MAGNSS and the software delivery timeline on the last two questions on slide 2.

### Eric Brewer, 2024-06-25

@Pat Wells , Dave and I discussed briefly and the slide deck (excluding backup) should be good to go.
Let me know if you have any questions.

### Eric Brewer, 2024-06-26

@Pat Wells @David Grosher @Sam Miller see updated charts, let me know if you need anything else.

### David Grosher, 2024-06-26

@Pat Wells @Sam Miller @Eric Brewer It looks good to me.

### Pat Wells, 2024-06-26

@David Grosher @Eric Brewer @Sam Miller 
Looks good on my end as well. 
I’ve edited a bit to include all 12 Q&A’s from the customer. 
Still outstanding on an answer to question number 2.

### Eric Brewer, 2024-06-26

@Pat Wells @David Grosher @Sam Miller I put some suggested wording in the powerpoint, please review.  
“Until the GPS update rate issue is resolved in software there is risk of an overshoot occurring.  This risk can be reduced by modifying the approach procedures as described below, but not fully eliminated.  Since large overshoots such as this are still relatively rare, we have not issued a grounding order for the fleet.  The associated risk will vary according to the landing site and surroundings so we leave this to each user to determine their risk tolerance.”
It’s also worth noting that we have not seen this level of overshoot on any of our SCO flights. The main difference is that they fly at low altitudes so there are very few orbits before the approach.

### Pat Wells, 2024-07-08

Report sent to customer on 7/8

### Eric Brewer, 2024-06-26

@Pat Wells @David Grosher @Sam Miller I put some suggested wording in the powerpoint, please review.  
“Until the GPS update rate issue is resolved in software there is risk of an overshoot occurring.  This risk can be reduced by modifying the approach procedures as described below, but not fully eliminated.  Since large overshoots such as this are still relatively rare, we have not issued a grounding order for the fleet.  The associated risk will vary according to the landing site and surroundings so we leave this to each user to determine their risk tolerance.”
It’s also worth noting that we have not seen this level of overshoot on any of our SCO flights. The main difference is that they fly at low altitudes so there are very few orbits before the approach.

### Pat Wells, 2024-07-08

Report sent to customer on 7/8

## Attachments (7)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 1.jpg | image | 645 | 2024-06-07 | listed only |
| 2.jpg | image | 280 | 2024-06-07 | listed only |
| T95_V430_240531_142114_pack.zip | archive | 5175 | 2024-06-07 | listed only |
| 1 (58c28082-0e94-433b-a48c-87b33ee78ad7).jpg | image | 435 | 2024-06-12 | listed only |
| 1.1.jpg | image | 492 | 2024-06-12 | listed only |
| T95_V430_240611_093609_pack.zip | archive | 5838 | 2024-06-12 | listed only |
| image-20240617-231258.png | image | 422 | 2024-06-17 | listed only |
