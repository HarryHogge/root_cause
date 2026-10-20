# XKIT-5557: B35/40 Lift Motor Wire Testing

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2026-07-28
- **Updated:** 2026-09-01
- **Resolved:** 2026-09-01
- **Reporter:** Jeremy Kostel
- **Assignee:** Matthew Aguirre
- **Creator:** Jeremy Kostel
- **Links:** relates to VXEP-1933 (VXE 1038 VTOL motors failed to shut off after transition to fixed wing flight)

## Description

Investigation of the V1038 aircraft identified catastrophic damage to a single front-left motor phase lead (see linked ticket). The damaged conductor appears to have contacted the carbon boom structure after insulation failure, resulting in arcing and potentially contributing to the CAN communication issues observed in flight.
The root cause of the insulation failure remains unknown. One possible mechanism is that an aggressive bend/kink in the phase lead created additional resistance and localized heating, eventually degrading the insulation and allowing conductor-to-carbon contact. Another possibility is that the wire was mechanically damaged during installation or maintenance and degraded over time until final failure.
To evaluate this, multiple motor phase lead samples were bent at angles ranging from 90° down to 15° and tested under a representative launch‑abort current profile. Temperatures were monitored at the bend point using a thermocouple, and tests were stopped if any signs of insulation degradation appeared. Across all samples and bend angles, the maximum temperature rise at ambient conditions (22-24°C) was approximately 6°C. When adjusted for potential solar loading (~60°C), the estimated temperature rise increased modestly to about 6.95°C—still far below the silicone insulation’s continuous operating limit of 200°C.
Results showed consistent behavior across samples, with no evidence that kinking alone could generate temperatures high enough to damage the insulation. However, secondary findings revealed that the presence of motor‑winding enamel on the crimped section of the wire can drastically increase heating, with temperature rises exceeding 100°C in cases where enamel was fully left on. Although no known aircraft have flown with enamel present in the crimped region, this outcome highlights a critical manufacturing and installation consideration. Overall, the testing strongly indicates that the kinked wire was not the root cause of the phase‑lead failure on V1038, and that other mechanisms—such as mechanical damage or improper stripping of enamel—would be more plausible contributors.

## Plan

- Obtain a representative production motor phase wire and use a protractor to bend the sample to the designated test angle; 0 degrees references one end of the phase‑lead sample.
- Introduce a kink representative of, or more severe than, the condition observed on the returned aircraft, then capture photos of the sample prior to testing.
- Connect the motor phase lead to the electronic load and place a thermocouple at the bend; record starting ambient temperature.
- Run a representative launch‑abort current profile derived from ESC‑logged phase‑current data for at least the maximum expected event duration, reproducing expected thermal loading.
- Monitor and log kink‑location temperature, current profile, test duration, ambient conditions, and any indications of wire damage (such as smoking, off‑odor, discoloration, insulation softening/melting, burn‑through, or conductor exposure). Stop testing immediately if smoking occurs.
- Remove the phase lead from the setup, capture post‑test photos, and inspect the wire for all forms of thermal degradation.
- Allow the wire to cool for approximately 5–10 minutes or until near ambient temperature.
- Repeat steps 1–7 for bend angles decreasing from 90 degrees in 15‑degree increments down to 15 degrees.
- Perform the full sequence for three separate samples.
- Compare measured temperatures and insulation condition against expected operating limits and document whether the observed aircraft failure could reasonably be reproduced through thermal effects associated with a kinked phase lead.

## Issue Status

Closed?
Investigation determined that the initially suspected kink‑induced overheating of the V1038 front‑left motor phase lead was not the primary cause of the observed insulation failure. Testing across multiple bend angles (15°–90°) showed only minor temperature increases of roughly 5–6°C under representative launch‑abort current profiles, and even with estimated solar loading, temperatures remained far below the silicone insulation’s 200°C rating, indicating that wire kinking alone could not have generated sufficient heat to cause damage.
A separate finding identified that residual enamel on the crimped connector portion of the phase lead can create extreme localized heating, with temperature rises exceeding 100°C when enamel is left fully intact—far beyond normal operational conditions. Although no flown aircraft are known to have connectors crimped over enameled wire, this mechanism presents a credible path to insulation degradation if improper stripping were to occur.
Testing results therefore rule out bend‑related heating and instead point to improper enamel removal (highly unlikely) or other mechanical/installation damage (highly likely) as the more probable root causes.

## Comments (6)

### Jeremy Kostel, 2026-07-28

Linking a good launch abort example here. Notice Phase Current is logged via the ESC at 100Hz here [embedded: 2025-10-28_15-15-VH_CID-2-log_first_flight (1).csv]

### Matthew Aguirre, 2026-08-12

Ran some initial tests, depending on the angle of bend (or “aggressiveness” of kink) the motor phase lead could handle a launch abort cycle with no issues, or lead to smoking and slight discoloration of the phase lead insulation. Next course of action is to rerun tests with 3 different samples following this procedure (more or less):

- Connect lead to test setup starting out at 90 deg bend. (0 deg referencing one end of the phase lead)
- Run current profile
- Measure temperature profile at bend
- Document before and after photos of phase lead.
- Reduce angle of bend by 15-20 deg.
- Repeat steps 1-4.

### Matthew Aguirre, 2026-08-24

Summary table from tests below. First draft report can be found here https://jenaero.sharepoint.com/:f:/s/EngineeringTeam/IgAkT-p6JT6tTJ5VrPNBA8dHAZSUUdVYDNsvZPnhHO01shQ?e=fcu1Qh. Overall finding is that it is highly unlikely that localized heating from a kink in the lift motor lead caused an insulation failure, room temp (20-24 degC) seen a max of 6.01 degC temp rise, rough calculations at solar loading (60 degC) yields an approximate max degC temp rise of 6.95 degC. Insulation on wire rated for 200degC continuous operation. 
| Parameter | 15 Degree Bend | 30 Degree Bend | 45 Degree Bend | 60 Degree Bend | 75 Degree Bend | 90 Degree Bend |
| Average Maximum Measured Current (A) | 43.22 | 44.23 | 41.82 | 40.93 | 45.14 | 42.51 |
| Average Maximum Recorded Temperature (°C) | 29.67 | 30.08 | 29.92 | 29.96 | 29.95 | 29.60 |
| Average Minimum Recorded Temperature (°C) | 23.66 | 24.74 | 24.64 | 24.42 | 24.48 | 24.10 |
| Average Temperature Rise (°C) | 6.01 | 5.34 | 5.28 | 5.54 | 5.47 | 5.50 |

### Matthew Aguirre, 2026-08-24

report

### Matthew Aguirre, 2026-09-01

@Matthew Aguirre new link to report (after tenant migration): https://redwireglobal.sharepoint.com/:w:/r/sites/EngineeringTeam/Shared%20Documents/Electrical/Test%20Data/(XKIT-5557)%20B35-40%20Lift%20Motor%20Wire%20Testing/Motor%20Phase%20Lead%20Testing.docx?d=wf5550e33665a42f8abe7a42a28f431bf&csf=1&web=1&e=nxiOfb

### Matthew Aguirre, 2026-09-01

@Matthew Aguirre new link to files related to this testing: https://redwireglobal.sharepoint.com/:f:/r/sites/EngineeringTeam/Shared%20Documents/Electrical/Test%20Data/(XKIT-5557)%20B35-40%20Lift%20Motor%20Wire%20Testing?d=w7aea4f243e254cad9e55acf34103c747&csf=1&web=1&e=3JcNfd

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [2025-10-28_15-15-VH_CID-2-log_first_flight (1).csv](attachments/63743_2025-10-28_15-15-VH_CID-2-log_first_flight%20(1).csv.md) | csv | 58215 | 2026-07-28 | converted |
| [microDRIVE_LP_Datasheet_V1_0 (2).pdf](attachments/63741_microDRIVE_LP_Datasheet_V1_0%20(2).pdf.md) | pdf | 1892 | 2026-07-28 | converted |
