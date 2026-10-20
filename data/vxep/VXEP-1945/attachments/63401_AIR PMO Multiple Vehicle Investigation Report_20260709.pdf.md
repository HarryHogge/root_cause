# AIR PMO Multiple Vehicle Investigation Report_20260709.pdf

Attachment 63401, pdf, 1142 KB, added 2026-07-09 by Alexander Alan Arnold.

## Page 1

1
Title: AIR PMO Multiple Vehicle Investigation ReportVehicle: VXE-845 / VXE-958 / VXE-721 / VXE-640 / VXE-8698 July 2026

## Page 2

2
ProprietaryVXE30 - Issue Resolution Process
D7 – Prevention
D8 - DoneYesAdd to LessonsLearnedDocument
Debrief CustomersClosedWithUFRsUFRAdded?NoSend UFR DescriptionTo CustomerClosedUserCreates Incident Report (IR)User Assembles After Action Report (AAR)EA Assembles Incident Response Team (IRT)User Secures AircraftUser Packages Aircraft and Ships to EA DepotEA Receives AircraftIRT reviews IR and AARIRT Inspects AircraftIRT requests additional info from customer(phone, email, zoom, etc.)IRT releases first-look report (FRP)
D1 – Form Team
D2 – Define The Problem
D3
Investigate Root Cause
D4 – Find Root CauseD5Verify Root CauseRCIT Releases Root Cause Report (RCR)EA Assembles Root Cause Investigation Team (RCIT)Alert UsersIRT creates Airworthiness Safety Alert (ASA)IRT publishes ASAAffected customers are alerted to ASAIs ASA Required?Yes
D3 – Interim Containment
D4NoD4Is Advisory Notice Required?IRT createsAdvisory NoticeIRT publishes Advisory NoticeAlert UsersVia ICRIRT creates list of aircraft tail-numbers affected by the incidentsIRT creates list of affected customersIRT creates Interim Containment Report (ICR)YesNoEA Assembles Corrective Action Team (CAT)CAT Creates List of Corrective ActionsFundedFixesUnfundedFixesAdd to Prioritized UFR ListEstimate Cost & ScheduleD6
D5 – Define Corrective ActionD8Brief Customer on UFRAre Fixes Required?CAT Creates Corrective Action Plan and Releases Corrective Action Report (CAR)YesNoNoYesAlert UsersFunding Available to Fix IssueSoftwareIssueHardwareIssueTrainingIssueMaintIssueQAIssueFix CodeBenchTestHIL TestFlightTestReleaseSoftwareUpgradeCreate Service BulletinAlert UsersPublish Service Bulletin & SWPrelimDesignFinalDesignBuildPrototypeBench TestPrototypeFlight TestPrototypeCreate Service BulletinShip to CustomersPublishServiceBulletinProductionDesignProduction SCM PlanBuildKitsIdentify Training GapUpdate Training CurriculumUpdate User ManualAlert UsersIdentify MTBF GapsUpdate Sparing PlanUpdate MxManualCreate Service BulletinRelease UpdatedMxManualPublishServiceBulletinCreate Correction Action Plan (CAP) for SCM and ProductionImplement CAP in SCM and Production
D6 – Implement and Verify Corrective Action
Alert UsersCreate HIL/Flight Test CardsUpdate Regression Tests for HIL and Flight TestD7
Alert User of Preliminary Assessment(known causes / mitigations)CreateOperational SupplementPublish OperationalSupplementAlert UsersVersion: Feb 2025

## Page 3

© 2026 Redwire. Proprietary, Not for Public Release.
Investigation OverviewGNSS IssuesMultiple aircraft exhibit loss of GPSFrequency management issue
Investigated but inconclusiveNot the root cause or contributing factorRoot cause or contributing factorNext Steps:1 . E n s u re  l o st  c o m m s  s e t t i n g s  a r e  s e t  t o  d e s i r e d  b e h a v i o r  b efo r e  l o a d i n g  m i s s i o n2 . E n s u re  P L Z  i s  a c c u ra t e  b e fo r e  l o a d i n g  m i s s i o nConclusion & Corrective Action:1. Frequency and RF issues attributed to odd behavior for aborts and fly aways2. Loss of GPS results in degraded performance when aircraft is RTB leading to not recovering at desired location3. LO S Comms behavior  and PLZ should be verified before loading mission
Evidence To DisproveEvidence To SupportEvidence To ProveSpectrum scan revealed possible RF issues in area

## Page 4

© 2026 Redwire. Proprietary, Not for Public Release.
Incident Summaries Reporter: Severity: Near MissVXE 845- VTOL error appeared on launch and aircraft auto aborted- Logs display loss of GPS, aircraft then executed performed abort logic after loss of GPS and returned to ground.VXE 958- Overshot PLZ. Aircraft returned and landed successfully. Based on the aircraft behavior the PLZ appeared to be oriented into a tail or cross wind, the aircraft returned to intended touchdown point and then began descent.VXE 721- Aircraft fly away after lost comms. The PLZ in the mission file was 10 kilometers away from the takeoff location. LOS mission settings were set to RTB and aircraft flew to PLZ after losing link landed at the location set during the launch wizard.VXE 640- Flyaway. Unable to provide root cause analysis due to incomplete data. It is suspected that the aircraft lost GPS and link at the same resulting in degraded navigational performance leading to aircraft not returning to desired RTB location. VXE 869-Flyaway. Unable to provide root cause analysis due to incomplete data. It is suspected that the aircraft lost GPS and link at the same resulting in degraded navigational performance leading to aircraft not returning to desired RTB location.

## Page 5

© 2026 Redwire. Proprietary, Not for Public Release.
DiscoveriesReporter: Severity: Near MissThe Silvus comms contention appears to have been caused by conflicting frequency profiles:USMC was allocated 2210 MHz and 2280 MHz center frequencies, each at 5 MHz bandwidth.USMC operated one vehicle at 2210 MHz frequency but at 20 MHz bandwidth, citing that the Stalker operator manual directed 20 MHz bandwidth, and disregarding the frequency manager's 5 MHz bandwidth restriction.USMC operated three other vehicles at 5 MHz bandwidth, but at frequencies other than the allocated 2210 or 2280 MHz.This resulted in contention with neighbors correctly operating within their own allocated frequency ranges and bandwidths.During FSR data collection, it was noted that there were several instances of VXE SUAV GCS software and aircraft firmware mismatches.
