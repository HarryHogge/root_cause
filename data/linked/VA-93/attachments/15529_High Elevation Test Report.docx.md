# High Elevation Test Report.docx

Attachment 15529, docx, 2238 KB, added 2023-07-20 by Cody Smisek.

High Elevation Flight Test Report

Conducted: 8/22/22 – 8/25/22

Location: Marine Corp Mountain Warfare Training Center (MWTC)

Test Engineers: Theo Coetzee, Enoch Nicholson, Ryan Christino

RC Pilot: Brendan Lugo

Summary:

A series of 19 flights were conducted over the period of one week at the MWTC to analyze the performance of the VXE30 VTOL system. The aircraft was tested with varying weights, lateral imbalance, and gain configurations. Early test points were chosen within the listed flight envelope to build out the performance estimates for the vehicle at heavy weight. Multiple heavy weight flights were then conducted with standard gains to better assess the current limitations of the system at 10,000ft DA. Flights were then conducted with modified gains to increase performance of the system. Once the limitations were assessed with modified gains at 10,000ft DA, the aircraft was flown at a slightly lower DA and flown with various levels of tip weight to further investigate the impact of lateral imbalance on the system. Several recommendations for the VXE30 flight envelope are discussed throughout the result sections for current and specially configured system limitations. Key recommendations include increasing to a 49 lb. Max Gross Take Off Weight (MGTOW) for standard configuration, 50 lb. MGTOW with modified gains, and a 52 lb. MGTOW is open for discussion at a lower DA with modified gains.

Methodology:

Engineering flights were conducted on vehicle 371 in various configurations. The overall weight of the vehicle and the lateral imbalance were incremented using small weights. Values for gross vehicle weight, center of gravity, and tip weight were recorded for each flight. GVW was measured with the shop scale hooked up to a portable power station, CG was measured with the CG tool, and tip weight was recorded with small electronic scale.

Figure 1. High Elevation Test Set Up; Asset 371 with CG Tool, Electronic Scale, Small Weights, and Kestrel Weather Station.

Location: LZ Grouse Meadow

Both standard configuration and adjusted gains were used across flights. Adjusted gains included the vehicle airspeed setpoint, VTOL system climb rate (m_alt.outmax), and the transition altitude. Flights were either done with the typical airspeed setpoint at 53 ft/s or increased to 56 ft/s. The VTOL system climb rate was mostly toggled between either 6 ft/s or 10 ft/s depending on the flight objectives. One flight was conducted with the climb rate at 8 ft/s. Transition altitude was toggled between 200 ft and 300 ft.

Flight conditions including density altitude, wind speed, and temperature were recorded with the Kestrel weather station.

Data from the VTOL page was viewed on a secondary laptop. Climb rate from the VTOL page was used as an indicator for aborting the flight. Failure to visually maintain the set climb rate resulted in aborting the flight. Flight 19 was aborted because of failure to maintain climb rate.

Flight data was packaged and recorded via FDR. Parameters that were used in analysis post flight included VTOL Power, Throttle, Current, and Barometer Climb Rate. Graphs of these parameters are displayed in the result section for relevant flights.

Additional testing included dyno data for performance values for both forward propulsion cruise blades and lift blades at 10,000ft DA.

Results:

Overall, several limitations for the VTOL system are discussed based on flights targeting specific data points and configurations. All fights are represented in one table in the appendix. Flights that were used to draw conclusions as follows:

Flights 1-7 were flown to create a performance model curve for weight vs. power. Weight was recorded for each flight and average lift system power was approximated by taking the average power value over the period from 5.25 seconds to 15 seconds into climb. The higher density altitude and slight breeze that picked up for the flights later in the morning appear to produce noise in the data. Forming a trend based on the entire data set gives poor results. Limiting the data set to the first three flights seems to remove a substantial amount of the noise from the data, at the expense of weakening the sample size, but provided a best guess for weight vs. power at high altitude. Both data sets with corresponding trendlines are included in the appendix as well as the predictive curve.

Flights 3 and 8 appear to indicate 49 lbs. with standard configuration gains appears to be the limit for the VTOL system at 10,000 ft DA. When looking at motor throttle values, flight 3 appeared to be right at the limit while flight 8 was clearly just past the limit with very defined motor saturation.

Flights 9 to 12 appear to indicate that with a modified configuration with climb rate at 6 ft/s and a lower transition altitude at 200 ft allows for an additional pound to be added for a MGTOW of 50 lbs. at 10,000 ft DA.

Flights 14 to 16 help to define the lateral imbalance criteria and effects on the VTOL system at high weight. The actual current sharing limitation is loosely defined but based on power levels per motor as a proportion of throttle signal; a peak power value was calculated for the different quantities of lateral imbalance. This was compared to prior lift motor / ESC combo testing. Additionally, a recommendation to maintain about / below 10% on the current sharing was made by Gordon.

Flight 3:

Weight (lbs.): 49.10			CG (in):	4.95

Wind (mph): Light			DA (ft): 10,300

Max Power (W): 4800			Approx. Sustained Power (W): 4750

Gains: (Standard Configuration)

Climb Rate: 10 ft/s		Transition Altitude: 300 ft

Figure 2. Very close to early motor saturation; throttle approaches the saturated value of 93%.

Figure 3. ROC appears met for duration of climb.

Flight 8:

Weight (lbs.): 49.45			CG (in):	4.95

Wind (mph): Light			DA (ft): 9,940

Max Power (W): 4900			Approx. Sustained Power (W): 4800

Gains: (Standard Configuration)

Climb Rate: 10 ft/s		Transition Altitude: 300 ft

Figure 4. Consistent signs of motor saturation / limiting at the max value of .93%

Figure 5. ROC still appears met.

Limitation 1: 49 lbs. with standard configuration gains appears to be the limit for the VTOL system at 10,000 ft DA in calm conditions.

Flight 9:

Weight (lbs.): 49.45			CG (in):	4.95

Wind (mph): Light			DA (ft): 10,050

Max Power (W): 4780			Approx. Sustained Power (W): 4400

Gains: (Modified Configuration)

Climb Rate: 6 ft/s		Transition Altitude: 200 ft

Figure 6. Motors throttle appears high but not saturated.

Figure 7. ROC appears met at 6 ft/s.

Flight 10:

Weight (lbs.): 49.10			CG (in):	4.95

Wind (mph): Light			DA (ft): 10,100

Max Power (W): 4790			Approx. Sustained Power (W): 4500

Gains: (Modified Configuration)

Climb Rate: 6 ft/s		Transition Altitude: 200 ft

Figure 8. Motor throttle appears high but not saturated.

Figure 9. ROC appears met at 6 ft/s.

Flight 11:

Weight (lbs.): 49.45			CG (in):	4.95

Wind (mph): Light			DA (ft): 10,230

Max Power (W): 4820			Approx. Sustained Power (W): 4700

Gains: (Modified Configuration)

Climb Rate: 8 ft/s		Transition Altitude: 200 ft

Figure 10. Motor throttle values are high, and one motor is consistently saturated while climbing.

Figure 11. ROC is not met and appears to average at about 6 ft/s.

Conclusion: The system cannot support an 8 ft/s climb rate at 49.45 lbs. at 10,000 ft DA.

Flight 12:

Weight (lbs.): 50.30			CG (in):	4.60

Wind (mph): 3-5			DA (ft): 10,380

Max Power (W): 4750			Approx. Sustained Power (W): 4600

Gains: (Modified Configuration)

Climb Rate: 6 ft/s		Transition Altitude: 200 ft

Figure 12. Two motors show signs of slight saturation at two different point in climb.

Figure 13. ROC appeared impacted for a small portion of the climb.

Limitation 2: 50 lbs. at 10,000 ft DA appears to be the limit for the aircraft with adjusted gains.

Flight 14:

Weight (lbs.): 50.80			CG (in):	4.80

Wind (mph): 1-2			DA (ft): 8,520

Max Power (W): 4600 (4800 Dec.)	Approx. Sustained Power (W): 4230

Tip Weight (lbs.): .50			Approx. Lateral Imbalance (in-lbs.): 35

Gains: (Modified Configuration)

Climb Rate: 6 ft/s		Transition Altitude: 200 ft

Figure 14. Throttle appears high but not saturated.

Figure 15. ROC appears met at 6 ft/s.

Figure 16. Approximate 3% current sharing between sides.

Figure 17. High values for motor throttle upon descent.

Flight 15:

Weight (lbs.): 51.05			CG (in):	4.80

Wind (mph): 1-2			DA (ft): 8,700

Max Power (W): 4650 (5080 Dec.)	Approx. Sustained Power (W): 4325

Tip Weight (lbs.): .65			Approx. Lateral Imbalance (in-lbs.): 48

Gains: (Modified Configuration)

Climb Rate: 6 ft/s		Transition Altitude: 200 ft

Figure 18.Throttle appears high but not saturated.

Figure 19. Approximate 6% current sharing between sides.

Flight 16:

Weight (lbs.): 51.15			CG (in):	4.80

Wind (mph): 1-2			DA (ft): 9,300

Max Power (W): 4780 (4900 Dec.)	Approx. Sustained Power (W): 4500

Tip Weight (lbs.): .75			Approx. Lateral Imbalance (in-lbs.): 57

Gains: (Modified Configuration)

Climb Rate: 6 ft/s			Transition Altitude: 200 ft

Cruise Power: 385 W			Dash Power: 880 W

Cruise Speed Set Point: 56 ft/s		Dash Speed Set Point: 85 ft/s

Figure 20. Motor throttle values appear high but not saturated.

Figure 21. Increased to upper limitation of approximately 10% current sharing.

Figure 22. Motor throttle slightly saturated upon start of decent.

Figure 23. Several extra orbits were conducted including at dash to approximate power consumption.

Tip Weight Validation Results:

| Flight # | VW (lbs.) | Tip Weight (lbs.) | Moment (in-lbs.) | Approx. Current Difference (%) | Approx. Peak Power (W) Per Motor | Approx Sustained Power (W) Per Motor |
| 14 | 50.80 | .5 | 35 | 3 | 1360 | 1200 |
| 15 | 51.05 | .65 | 48 | 6 | 1480 | 1260 |
| 16 | 51.15 | .75 | 57 | 10 | 1480 | 1360 |
| 18 | 52.00 | .4 | 26 | 4 | 1365 | 1300 |

* Peak power per motor was not measured directly. It is approximated by first splitting the max peak power on the system according to the current sharing. This value is then taken and a 10% throttle difference between motors is assumed as a “worst case” difference on that side. Power is then split by that 10% assuming a linear relationship between throttle and power at high values on the curve. A similar process is applied for approximate sustained power.

Flight 17:

Weight (lbs.): 52			CG (in):	4.80

Wind (mph): 1-2			DA (ft): 9,400

Max Power (W): 4970			Approx. Sustained Power (W): 4700

Gains: (Modified Configuration)

Climb Rate: 6 ft/s		Transition Altitude: 200 ft

Forward Flight:

Cruise Power: 375 W

Cruise Speed Set Point: 	56 ft/s

Figure 24. Motor throttle values are high, approaching saturation.

Figure 25. ROC appears to be met at 6 ft/s.

Figure 26. Motor throttle value was slightly saturated at the start of descent.

Figure 27. Power was averaged across the relatively calm cruise portion of the flight.

Flight 18:

Weight (lbs.): 52			CG (in):	4.65

Wind (mph): 2-3			DA (ft): 9,350

Max Power (W): 5050			Approx. Sustained Power (W): 4800

Tip Weight (lbs.): .4			Approx. Lateral Imbalance (in-lbs.): 26

Gains: (Modified Configuration)

Climb Rate: 6 ft/s		Transition Altitude: 200 ft

Figure 28. High vibration was observed early on and appears to have an effect on motor throttle.

Figure 29. ROC impacted during ascent. Operator triggered abort at roughly 21 seconds into takeoff.

Dyno Testing:

An additional test that was conducted while at high elevation was a static dyno test for both forward cruise propeller blades and lift blades. While the results of this testing are largely as expected, and cannot be easily correlated to the exact limitations on the system, the quantified difference in propeller efficiencies may be helpful for future evaluations of high elevation system performance.

Figure 30. High elevation yields an approximate 10% increase in power when producing high thrust values.

Figure 31. High elevation yields an approximate 8% decrease in propeller efficiency when producing high thrust values.

Figure 32. High elevation yields an approximate 15% increase in power at low thrust values (Cruise) and an approximate 20% increase in power then producing high thrust values (Climb).

Figure 33. High elevation yields an approximate 15% decrease in propeller efficiency when producing high thrust values.

Conclusion:

A large quantity of valuable data that can be used to validate the VXE30 performance envelope was collected over the course of high elevation testing. The limitations for MGTOW at 10,000 ft DA in standard configuration are best represented by flight 3. The aircraft appears to be on the edge of lift system saturation while still being able to maintain a climb rate of 10 ft/s. Either increasing the weight in flight 8 or increasing the DA in flights 6 and 7 pushes the system to saturate on climb. By modifying the climb rate to 6 ft/s and reducing the transition altitude to 200 ft, margin is added that allows the aircraft to reach 50lbs. shown by flight 12. Flight 12 shows some signs of saturation showing the system has approached its limit but is both a little over on weight at .30 lbs. and a little over on DA at 400 ft which should be considered when evaluating the severity of the saturation.

At a lower DA, roughly 9400 ft., the aircraft was flown several times at 52 lbs. Flight 17 appeared to push the aircraft back to the limit of almost saturating the motors with the modified gains.  Lowering DA appears to buy back some margin on the weight allowance although the system still performed better than anticipated at this weight value. Additionally, 52 lbs. with tip weight, failed in making climb rate and was aborted. All data collected is summarized in the appendix.

Tip weight and the associated lateral imbalance was investigated separately in several flights with a MGTOW around 51 lbs. Tip weight was shown to increase current sharing and at higher values, with heavier tip weight starting to saturate values upon the start of descent. .50 lbs. of tip weight appeared to not stress the system too much on landing and maintain current sharing between both sides of about 3%. Desired antennas for MOD payload at approximately .50 lbs. may necessitate increasing the lateral imbalance limitations currently called out in the manual. It would be recommended to increase these limitations to .50 lbs. capability but define a lower MGTOW or DA that can be operated at versus the standard configuration.

Flight Appendix:

| Flight # | MGTOW (lbs.) | CG (In) | DA (Ft) | Tip W (lbs.) | Gains | Flight Data |
| 1 | 45.10 | 4.55 | 9,930 | - | STD | T95_V371_220823_073637_pack |
| 2 | 47.05 | 4.35 | 10,180 | - | STD | T95_V371_220823_075931_pack |
| 3 | 49.10 | 4.95 | 10,300 | - | STD | T95_V371_220823_082443_pack |
| 4 | 44.15 | 4.35 | 10,420 | - | STD | T95_V371_220823_085133_pack |
| 5 | 46.00 | 4.65 | 10,560 | - | STD | T95_V371_220823_091333_pack |
| 6 | 48.25 | 5.00 | 10,700 | - | STD | T95_V371_220823_093443_pack |
| 7 | 48.35 | 5.00 | 10,850 | - | STD | T95_V371_220823_100011_pack |
| 8 | 49.45 | 4.95 | 9,940 | - | STD | T95_V371_220824_071121_pack |
| 9 | 49.95 | 4.95 | 10,050 | - | MOD | T95_V371_220824_073015_pack |
| 10 | 49.95 | 4.95 | 10,100 | - | MOD | T95_V371_220824_075200_pack |
| 11 | 49.95 | 4.95 | 10,230 | - | MOD | T95_V371_220824_080652_pack |
| 12 | 50.30 | 4.60 | 10,380 | - | MOD | T95_V371_220824_083013_pack |
| 13 | 50.35 | 4.80 | 7,760 | - | MOD | T95_V371_220825_064750_pack |
| 14 | 50.80 | 4.80 | 8,520 | 0.50 | MOD | T95_V371_220825_071933_pack |
| 15 | 51.05 | 4.80 | 8,700 | 0.65 | MOD | T95_V371_220825_074038_pack |
| 16 | 51.15 | 4.80 | 9,300 | 0.75 | MOD | T95_V371_220825_080627_pack |
| 17 | 52.00 | 4.65 | 9,400 | - | MOD | T95_V371_220825_084417_pack |
| 18 | 52.00 | 4.65 | 9,350 | 0.40 | MOD | T95_V371_220825_091935_pack |
| 19 | 44.95 | 4.50 | 9,840 | - | STD | T95_V371_220825_095005_pack |

Figure 34. Estimated Weight vs. Power Curve Created by Limited Data Set with Incremented Weight.

Figure 35. Good Trendline Created by Limited Data Set.

Figure 36. Poor Trendline Created by Complete Data Set.

Additional Info:

Grouse Meadow: 38.405416, -119.484078

Sweetwater Strip: 38.505895, -119.218797

MARINE CORP POC: Major. Andrew Dunbeck

andrew.dunbeck@usmc.mil 	Cell Phone: 760-402-0359

MARINE CORP Guide: Capt. Cornes

All data analysis was done via MATLAB and added to CONDOR at \\CONDOR\Users\Ryan\Matlab\High Elevation Testing

Summary of Battery Health from Hybrid Packs Brought to High Elevation Testing:

Figure 37. Capacitance testing conducted after high elevation testing. Hybrid packs were not tracked for individual flights.
