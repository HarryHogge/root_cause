# VXEP-267: 107-107735 VTOL GPS Assy Repeat Failures for Low C/No

- **Issue type:** Problem
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2024-02-05
- **Updated:** 2026-03-30
- **Resolved:** 2026-03-30
- **Reporter:** Matt Philley
- **Assignee:** Matt Philley
- **Creator:** Matt Philley
- **Production Stakeholder:** Trevor Gronner
- **Other Stakeholder (as required):** Wesley Lilienthal

## Description

Inconsistent results and batches of failures have been a periodic and recurring issue on VTOL GPS Assy 107-107735.
We have a build & test procedure with acceptance range in Electronics Shop [>40 per Traveler]
We have a check with acceptance range in SCO [>40 per Traveler for LW, but actually use 43.5 -50]
We have a check with acceptance range in Flight Test [43.5-50]

However, we are currently (late Jan/early Feb 2024) in a wave of CNO failures where they pass in Electronics, pass in SCO, then fail in Flight Test, then when we check back in SCO they fail.
Now additional GPS’s are failing in SCO.

Unsure if this just tends to be a bad batch kind of thing or perhaps weather is playing a larger factor than we account for? 
Current rework is just to swap in a new VTOL GPS Assy in SCO and keep swapping until we find ones that pass.

| NCR/AC# | VTOL GPS Assy SN  (107-107735) | VTOL GPS SN  (1807P01C) | EShop C/No VTOL [Pass > 40] | SCO C/No VTOL [Pass > 40] | SCO C/No Fwd [Pass > 40] | Flight Test VTOL Satellites & C/No [Sat 10-18] [C/No 43.5-50] | Flight Test Fwd Satellites & C/No [Sat 9-17] [C/No 40-50] |
| 2119 / 589 (FAIL) | T-S100204 |  | Sat: C/No: | Sat: C/No: | Sat: C/No: | Sat: C/No: | Sat: C/No: |
| 2119 / 589 (PASS) | T-S100435 |  | Sat: C/No: | Sat: C/No: | Sat: C/No: | Sat: C/No: | Sat: C/No: |
| 2364 / 602 (FAIL) | T-S100559 |  | Sat: C/No: | Sat: C/No: | Sat: C/No: | Sat: 15 C/No: 42.3 | Sat: 12 C/No: 44 |
| 2364 / 602 (FAIL) | T-S100319 |  | Sat: C/No: | Sat: C/No: | Sat: C/No: | N/A | N/A |
| 2364 / 602 (PASS) | T-S100316 |  | Sat: 9 C/No: 42.3 | Sat: 16 C/No: 46 | Sat: 13 C/No: 46.7 | N/A | N/A |
| 2390 / 610 (FAIL) | T-S100324 |  | Sat: C/No: | Sat: C/No: | Sat: C/No: | Sat: C/No: | Sat: C/No: |
| 2390 / 610 (FAIL) | T-S100317 |  | Sat: C/No: | Sat: C/No: | Sat: C/No: | Sat: C/No: | Sat: C/No: |
| 2390 / 610 | TBD |  | Sat: C/No: | Sat: C/No: | Sat: C/No: | Sat: C/No: | Sat: C/No: |
| 2393 / 611 | T-S100323 |  | Sat: 12 C/No: 43 | Sat: 18 C/No: 44.6 | Sat: 15 C/No: 45.3 | Sat: 16 C/No: 45.0 | Sat: 13 C/No: 45.0 |
| 2393 / 612 | T-S100322 |  | Sat: 11 C/No: 44 | Sat: 14 C/No: 45 | Sat: 11 C/No: 47 | Sat: 17 C/No: 44.6 | Sat: 14 C/No: 44.3 |
| 2393 / 613 | T-S100318 |  | Sat: 11 C/No: 44.3 | Sat: 13 C/No: 43.6 | Sat: 10 C/No: 46.3 | Sat:15 C/No: 44.6 | Sat: 12 C/No: 48 |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |


107-107735 Batch info:
| Batch # | Date of Final Insp | SNs |
|  | 2/2/24 | T-S100574 |
|  | 1/26/24 | T-S100316 thru T-S100324 |
|  | 1/18/24 | T-S100556 thru T-S100565 |
|  | 1/8/24 | T-S100438 thru T-S100442 |
|  | 1/5/24 | T-S100433 & T-S100434 |
|  | 1/4/24 | T-S100443 |
|  | 12/26/23 | T-S100432, T-S100435, T-S100437 |
|  |  |  |
|  |  |  |

## Plan

Proposal based on discussion with SCO and Flight Test. These ranges are not fundamentally defined anywhere in a released Enginering document. These are values based on past experience and past data. Therefore, the following is being proposed as an interim solution until the 2024 GPS development projects are able to bring in new equipment and testing capabilities.
The proposal is based on acceptance ranges based on previous data and potential risk to the Customer:
| C/No Range | Response | Rationale |
| <40 | Electronics Shop, SCO, & Flight Test: Reject - NCR and GPS replacement is needed | This is getting close to the ~38.5-ish lower limit where Launch Wizard would prevent the aircraft from taking off. Anything below 40 has historically never been accepted. |
| 40-44 | Electronics Shop & SCO: Pass, but with comment to be checked in Flight Test  Flight Test: Complete Flight Test, but generate NCR for evaluation with reference to this Jira ticket. Tag Quality Engineering & Production Engineering for dispo. | This is our range that is technically acceptable and will not actively cause a problem with Flight Test, but is below the average range and has us concerned the GPS might degrade and cause problems for the Customer.  This also gets into the territory where the Fixed Wing GPS might have close or better signal which is not normal and where a second opinion is preferred before just sending it out as-is. This would be accepted at some risk. The closer the value to 40 the higher the risk. Consider leaving GPS on for a short amount of time 10-15 minutes before establishing value in case the value dips while testing. |
| 44+ | Electronics Shop, SCO, & Flight Test Pass - No issue this is the desired and expected result | Based of historical data this range is fully acceptable and what “normal” should look like especially out at flight test. |

## Issue Status

Dave approved. @Matt Philley let us know additional requests for engineering for this (I have not yet read all comments).

## Comments (12)

### Matt Philley, 2024-02-05

@Carson Buckley @Artis Bertulis @Ryan Ferguson @Kelly J Furlong @Trevor Gronner @Brad Crampton 
This Jira has been created to capture the repeated issue of VTOL GPS C/No failures in SCO and Flight Test. If there are failures in the shop that are relevant they can be added here as well

### Carson Buckley, 2024-02-05

@Matt Philley I’d like to add that the GPS failures we’ve been capturing in SCO do not occur immediately on power on. Electronics may want to run these for 5 or 10 minutes, checking signal values during this time. It seems once they ‘warm up’ they begin to show degredation, even if the signal was strong initially.

### Artis Bertulis, 2024-02-05

@Matt Philley @Carson Buckley we also might want to look into our indoor GPS boosters, they often seem to show different results than aircraft being outside. Maybe there’s another, more calibrated way of measuring signal indoors?

### Ryan Ferguson, 2024-02-05

We have projects in the works to get a better GPS testing setup in Electronics which uses RF hats and known calibrated sources.  The “live sky” data from a repeater will never be sufficient to make a judgement call on whether or not the GPS system is functioning based purely on C/n0 values.  This project however will have to remain on hold until MCMAGNSS is mature enough to determine what the GPS test hardware needs to support.  In the meantime we will continue to see failures like this in SCO and test flight.

We had a large group of failures in the past 30 days on this assembly.  This hints to one of three failure modes -
A) Weather related failures.  The additional moisture in the atmosphere will reduce the carrier signal from the GPS satellites.  This will result in a reduced C/n0 value as many noise sources are terrestrial.  To test if this is the case, the defective GPS units from NCR-2381 and NCR-2393 will be retained and tested in a week or two when the storms have cleared up.  If it was weather related, we will see the C/n0 values return to stronger values.
B) In-house batch related failures.  These could be related to technicians using different techniques or defects introduced under the GPS can causing a reduction in RF signal.  There is currently no non-destructive method to test for this as our cans are fully soldered units rather than clip-ons.
C) Supplier batch related failures.  U-blox is a consumer-grade GPS manufacturer with a reasonable quality record.  This does however mean that with a standard distribution of C/n0 values we might be cherry-picking GPS units which would drive our fallout rates up.  To find this one out, we would have to investigate all of the NCRs related to GPS failures (of both center wing and avi box GPS) and determine if there is a common batch source.

The part which will require some more investigation is why it takes several minutes to fail.  If this is the case, it might be possible something on the aircraft is causing noise that is being picked up by the receiver.  This could be tested by using a VTOL AP connected to nothing but a battery for power and a computer to read the C/n0 values.  If the values are good here but not in a plane, that would hint at things inside the aircraft causing issues.

### Matt Philley, 2024-02-06

@Ryan Ferguson @Carson Buckley @Artis Bertulis @Ruysser Gabler 
In the “Plan” section of this Jira I created a table with some draft info on C/No ranges, proposed response, and rationale for those ranges and response. 
Please review this when you are able and I would like to round up the team to discuss and see if we can all get on the same page about what values are acceptable, questionable, and not acceptable.
I imagine this is just an interim plan until we have the improved equipment later this year. 
@Trevor Gronner FYSA

### Matt Philley, 2024-02-07

@Barry Mendez @David Grosher Can you help us with some Engineering point of contact for GPS stuff?
We need Engineering’s input in trying to establish acceptance criteria based on the proposal in the “Plan” section of this Jira ticket based off historical data since we dont have the equipment and bandwidth to really perform a study at this time.
My request is an Engineer who is familiar with our system GPS requirements to review the proposal and participate in a group alignment discussion (hopefully less than an hour) for SCO, Flight Test, Electronics, Quality Engineering, Production, and Production Engineering that I will facilitate to come up with an immediate path forward on this topic. 
If you have any questions let me know and we can discuss. @Marc Richardson FYSA

### Barry Mendez, 2024-02-07

@Wesley Lilienthal - Can you please help with this?

### David Grosher, 2024-02-07

@Matt Philley Yes, I think the proposed plan is good, it is inline with thresholds in the SW that abort a launch based on GPS quality.  If you need further clarification or documentation from our side, @Eric Brewer would be able to help there, he is the Flight Science engineer working on AGNSS.

### Matt Philley, 2024-02-08

@David Grosher @Wesley Lilienthal @Eric Brewer @Ryan Ferguson @Carson Buckley @Artis Bertulis @Ruysser Gabler @Kelly J Furlong @Ben Norris 
Based on individual conversations I have had with most of you we are going to go ahead and proceed with Flight Test following the proposed table above for the next several aircraft.
Due to weather an other factors we have a bit of a pile of several Production aircraft ready for flight test, so these will give us a good sample of data to test out the guidance above. 
Once we get through this batch I will then call an actual meeting for us all to have a quick chat… probably late next week.

### Matt Philley, 2024-02-26

@David Grosher @Eric Brewer it looks like the proposed criteria is working for Flight Test and SCO. If yall are good with it I am going to schedule a meeting for SCO, Flight Test, Production, Production Engineering, and QA to all adopt this into procedures and travelers. 
Would yall like to be included on that discussion or just kept aware here in this Jira ticket?

### David Grosher, 2024-02-26

@Matt Philley That works for me. Depending on my availability I will attend, but if not I will track it here. 
Just an FYI, with the upcoming software release that will utilize additional constellations we will be seeing upwards of 30 satellites with an unobstructed view of the sky and in initial tests generally higher and more consistent CNo.

### Matt Philley, 2024-02-26

@David Grosher thats fantastic! Hopefully that will let us put a nice bow on this issue and never have to think about it again.
Alright I will include you on the invite for your awareness and if you can make it that's great, but no hard feelings if not.

## Attachments (0)
