# ExperimentOne 8-22-24.docx

Attachment 22566, docx, 16 KB, added 2024-08-22 by Brad Crampton.

Summary: As a result of Haydon Jeanor’s report it was deemed important to determine at what point the lack of engagement of the AS150 power connector becomes a problem.

Description:  Aircraft 692 had an overheated battery and a battery during engineering testing was noticed to over heat when the connector was not fully engaged during testing,  see JIRA VXEP-540. Because of this observation I was asked to look into it and gain some insight as to why the power connector gets very tight as one proceeds to depress it.

Abstract: The root cause of why the connector is stiff is a lack of precision between the male pin and the female receptacle. The pin diameter is too large for the receptacle diameter. The root cause of increased resistance and subsequent overheating is the connector sits too high above the plug and does not fully engage.

Procedure: In order to determine if this problem is severe or inconsequential. We (Heyden Jeanor and Brad Crampton) took 5 main batteries (PN: 107-101050) and hooked them up to the BK Precision Electronic Load, observed the voltage from the battery to be 26.08, applied a 1 amp load and then proceeded to move the connector in and out noting when the voltage dropped to 20V.   3 out pf 5 batteries exhibited a voltage drop of 6V when the bottom of the connector was .05” from the top of the battery.

Conclusions:

Improving the connector is quite simple. Specify on the pin and receptacle drawings the outer diameter of the pin and the inner diameter of the receptacle so that the pin will fit into the receptacle with about a .001” gap. These pins are made on a CNC lathe so this is not overly difficult. The proper gap results in a very nice fit and feel.

The overheating problem is considered severe because an intermittent voltage drop during flight results in failure. Because the gap is so small that results in a voltage drop, a fairly slight lack of  engagement on the  plug could work its way out from vibration and other possible forces during fight.

Summary: A fifty thou gap represents a formidable risk that needs to be addressed. Fixing this problem in the future does not seem technically difficult.
