# WindTesting.docx

Attachment 20639, docx, 1499 KB, added 2024-05-22 by Eric Brewer.

Set landing zone as short as possible with pure crosswind, in this case wind from the north at 20fps (~12 knots)

Vehicle comes in with crab angle and experiences significant roll/pitch disturbance on transition.  Vehicle starts approach with about 50ft of crosstrack error.  The vehicle misses the touchdown point by ~150ft crosstrack and ~100ft alongtrack.  Note: pitch/roll disturbance are likely due to simulated stall (model is not great for this regime).

Extending the landing zone further allows crosstrack error on transition to be reduced.  Sim issues result in some large oscillations in pitch/roll after touchdown (believed to be due to simulated stall).

To test overshoot, made test build with 5 degree pitch error hard coded into VTOL AP.  Tested approach west with 15fps headwind.

With original software:

With updated FWH:

It’s really hard to draw any conclusions due to the sim performance, but we can see that the new software does limit use of FWH when pitch angle command is high as expected.

Side Note: Orbit tracking is really sloppy in wind.  Operators (Artis, Cody, Ruysser) think that is typical.
