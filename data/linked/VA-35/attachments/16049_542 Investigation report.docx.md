# 542 Investigation report.docx

Attachment 16049, docx, 6605 KB, added 2023-08-29 by Adrian Garcia.

542 Investigation

The Current Sense Board was connected to the high current transformer. The connector of the board was put into a vice to be able to have a controlled and precise way to connect and disconnect the connectors. The other lead to the high current transformer is connected to the other connector. Different currents were ran through the connector at different lengths to measure how long the connectors would take to heat up to > 180 C°. 7 different tests were conducted to determine which state the connector heats up the most.

I then used the logger to measure the temperature, current, and voltage of the system. The data was exported to Excel to make temperature vs time graphs to see how long it takes to reach >180 degrees C, that is the typical reflow point for solder.

Test 1:

The connector was fully engaged, and a constant 150 A was applied. There was nothing abnormal with this test. It took about 6 minutes for the temperature to reach 200 degrees C and about 4.7 min to reach 180 degrees C.

Test 2:

The distance between the male and female connector was now 0.075” at a constant 150 A. The rate the temperate rises over time increased. The graph shows at about 3.7 min the connector reaches 180 degrees C and at about 5 min the temperature is at 200 degrees C. This shows that having a small about of gap in the connectors increases the rate of change.

Test 3:

Remaining the same length as test 2, 0.075”, the current was increased to 170 A. This is because the current reading from test flights state that the average current in the lift motors is between 150 A and 170 A. Here we can see at this current the connector heats up much faster. At 2.5 min the temperature is about 180 degrees C and by 3 min the connector is at 200 degrees C.

Test 4:

With the connector fully engaged with a constant 170 A applied the amount of time to reach 180 C° is around 4.25 min and to reach 200 C° is around 4.5 min. This is faster than test 2, which could be because more amperage is applied, however, in test 2 there was a 0.075” gap. Also, this test was concluded 5 different times. The first few times the thermocouple was not secured properly and each time the temperature reached around 160 C° the voltage waveform in the oscilloscope became unstable. This was only true in the first 4 tests. After that I fixed the thermocouple connection and secured the connector in the vice. In between tests the connector was checked to see if solder reflowed and there was a large blob.

Test 5:

The gap between the male and female connector increased to 0.1” with a constant 170 A applied. It is shown that once the connector reaches 150 C° the rise to 200 C° is exponential. It takes 3 min to reach 200 C° and around 2.5 min to get to 180 C°.

Test 6:

For this test the connector was not fully engaged and 150-170 A were applied. Then tapping was applied to connector to mimic vibration from a drone. From the data we can see that the current drops during vibration.

Conclusion:

In conclusion, the data shows that as the gap increases the rate heats up increases. The same can be said when the current increases. The temperature did not reach 180 C° in under 1.5 min but over time the connector did begin to deteriorate. After multiple tests the connector fuse seemed blow up as seen in the photo below. Also, when there is a gap and vibration is applied the current drops which can also lead to bad take off and landing.
