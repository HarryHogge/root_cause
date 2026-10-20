# Heated Pitot Tube Review process.docx

Attachment 18993, docx, 18 KB, added 2024-02-27 by Rajesh Budhabhatti.

## Heated Pitot Tube Review process

## Introduction

This is a review process document for offering a heated pitot tube and is compiled from inputs from several people.

Targe due date is tied to TIQUILA aircraft or around occur in late June/July along with the MCMAGNSS updates starting (e.g. one configuration change). Sooner may be allowed and based on TIQ behavior/requirements we would need to have successful test reports prior to that.

There is no measurable requirement (still), just to provide some amount of heating so that any snowfall can be tolerated. There is no specific measure to level of snowfall, FAA often refers it as light, medium or heavy snowfall so our requirement is to add a reasonable amount of heating with limited scope.

We want heating elements to be switchable based on temperature automatically, and if easy/possible, provide a provision for a future SW command. SW command would only turn on/auto (no off). e.g. the aircraft would protect itself.

## Specifications

## Operating temperature

## Humidity

## Operating environment

## Switching mode-Automatic or software controlled.

Switching mode automatic based on ambient temperature with provision for future software control; Software command will only have option of Auto and On and no option to turn it off, ie the aircraft to protect itself if operating in low temperatures.

## Testing: Environmental and others

## Target schedule

Late June/July or sooner. Will need successful test report prior to that.

## Previous efforts

## Design

Earlier design involved a pad heater and a foil heater. There has been changes, now both tubes have to be heated. ME team is considering making a metallic bridge between the two tubes incorporating a heating element and a temperature sensor/power shut-off device mounted on top. Power requirements may rise because of this from earlier estimates of 19.5W.

SA camera power supply cable will have to be reviewed for power capacity.

## Power required: Preliminary  tests conducted by Laszlo consumed 22.3W as below

560mA @5V = 2.8W

1560mA@12V = 19.5W

Total 22.3W

## Available power

## Environmental testing performed.

## Recommended Improvements

Links:

https://www.cantherm.com/wp-content/uploads/2017/05/Bseries_NOVEMBER_2015.pdf

Sensing and switching in one device. Eg. PN 66L020-xxxx will open when temperature rises above 20 degrees C.

sensata-6600-series-subminiature-bimetal-disc-thermostat-datasheet.pdf

Other options to consider:

## DERNORD Cartridge Heater 12V 100W Electric Hot Rod Stainless Steel Heating Element Replacement(Tube Diameter:8mm)

Amazon.com: DERNORD Cartridge Heater 12V 100W Electric Hot Rod Stainless Steel Heating Element Replacement(Tube Diameter:8mm) : Tools & Home Improvement

Thermocouple modules with SPI. I have used these before and have some spares:

Weewooday 4 Sets Direct Current 3-5v Max6675 Themocouple Module and K Type Thermocouple Temperature Sensor Thermocouple Sensor Set M6 Screw with Cable Cord Compatible with Arduino/Raspberry Pi: Amazon.com: Industrial & Scientific

ULN2003 Heater driver circuit. We can use all 4 channels to get upto 2A @12.5V = 25W. Also available in module form. I have used these modules and have some spares.

ULN2003 Datasheet(PDF) - STMicroelectronics (alldatasheet.com)

Inexpensive modules here: Amazon.com : Longruner 5X Geared Stepper Motor 28byj 48 Uln2003 5v Stepper Motor Uln2003 Driver Board with ArduinoIDE (no Wire) : Electronics
