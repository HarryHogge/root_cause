# ModA_Issues_DamNeck 1 (1).pdf

Attachment 26875, pdf, 386 KB, added 2025-03-06 by Mike DeJesus.

## Page 1

Dam Neck BH/Mod-A Testing Notes
• SASIL brought an “Edge-Fixed” Mod-A kit from their lab to Dam Neck for BH testing
• Problems experienced
• RF performance Issues
• RF cabling issues
• MAIM/AHRS issues
• PPS fail
• uD hardware screws not fully captive
• Summary: 
• “Edge-Fixed” equipment required field modification resulting in a partially mission capable system. As 
delivered, the Bloodhound required significant troubleshooting, removal/replacement of components, 
discovery learning, and a large quantity of spares. 
3/6/2025 1

## Page 2

RF performance Issues
• CDIPT team spent at least 30 minutes troubleshooting and unsuccessfully resolving 
significant RF performance issue to the BH QB antenna array. The wing hard point had 
small yellow shims installed during the Edge Fix. These shims did not ensure a solid 
connection from the antenna to the hard point. Small pieces of gaffers tape were used to 
extend the shimming, improving the right antenna performance, but not bringing it to the 
level of the left and center antennas. This reduced right antenna performance may be 
attributed to inadequate/failed shimming of the wing hard point mount or some other 
coax fail point in that chain. 
• Test metrics and results provided in following slides
• Summary: right antenna reported between 30-56 dB difference from center and left 
antennas in BH.
• Despite 4 SMEs working on the issue we were unable to resolve with the existing material provided 
in the Mod-A kit
3/6/2025 2

## Page 3

Field Modifications
3/6/2025 3
Tape Shims
Dismantling the Hardpoint

## Page 4

AV Loc
Test parameters
• HH freq: 151.819 MHz, 12.5 kHz BW
• HH power level: 1W
• Max BH attenuation set to 66 dB, -120 dB 
noise floor
3/6/2025 4
Left Center Right Delta
“Fixed” Coax, 20M -56 -56 -112 56 dB
“Fixed” Coax, 135M -86 -86 -130 44 dB
“Fixed” Coax, 260M -100 -100 -130 30 dB
Validation Coax, 20M -57 -61 -67 10 dB
Validation Coax, 135M -84 -85 -93 9 dB
Validation Coax, 260M -99 -98 -109 10 dB

## Page 5

Other Issues with the “Edge-Fixed” Mod-A Kit
• RF cabling: The DSUB RF interconnects used to install the QB array had the 4-40 hardware 
installed backwards – i.e. the screws could not install to the jack posts. This makes this 
unusable unless field modified.
• MAIM issues: Screws in Micro-D fasteners are not truly captive and can be unscrewed 
with little effort. CDIPT provided alternate part number with native captive hardware that 
will reduce this risk to near zero. 
• MAIM issues: PPS failure on one of the MAIMs necessitated a remove and replace as one 
of the new BH operating profiles requires PPS. 
3/6/2025 5
