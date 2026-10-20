# VXEP-978: VXE 500 Freezing fog caused issues with ADP LRF

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2025-02-05
- **Updated:** 2025-08-15
- **Resolved:** 2025-08-15
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Ben Triplett
- **Creator:** Alexander Alan Arnold
- **Labels:** Edge_Asset, Weekly-incident-tracker
- **Links:** is duplicated by FS2-2851 (VXE 500 Freezing fog caused issues with ADP LRF); relates to FS2-2852 (CA for excluding erroneous LRF measurements); relates to VXEP-976 (VXE 500 Reports large negative AGL after landing )
- **Vehicle Tail Number:** VXE 500
- **Vehicle Configuration:** fuel cell, heated pitot prototype.
- **Issue Status:** Closed
- **Root Cause:** Freezing fog impacting laser altimeter measurement causing artificially low readings.
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

EDGE ASSET
Ruysser: During 2/3 landing freezing fog (FZFG) had rolled through the landing location all the way up to about 300-400AGL. Transition started 500Agl ish to stay out of FZFG in fixed wing flight. Upon descending into the FZFG the aircraft seemed to slow its decent rate drastically. The aircraft took almost all of its battery to decent through the FZFG landing at 36% remaining. It is assumed that the LRF was picking up reflections from the FZFG and telling the VTOL that it was close to the ground. 
-Both Billy and Calvin noted that the decent took forever 
- Sent data to Eric to look for potential VTOL issues before flying again and his first impressions seemed to align with that assumption when looking at the data.

-Ruysser: During 2/4 landing FZFG was rolling in during landing, at about 100 or so ft AGL the aircraft slowed to a snail pace decent again and did it all the way to the ground. Likely the same thing occurring. Once landing the wings had frost on the tops but no other ice. ** The second landing issue may very well be due to the VTOL altitude though and not FZFG. See other VTOL altitude issue

## Corrective Action

Short term - don’t fly in this weather.
Long term - investigate improvements to allow flying in this weather. FS2-2851

## Comments (5)

### Greg Fryer, 2025-02-05

@Eric Brewer looks like you looked at this already, and I don’t think Freezing Fog is a supported environment. This capability might be in the broader “full cold weather ops” project that is lower priority. Feel free to close and notify Ruysser if so.

### Eric Brewer, 2025-02-05

@Greg Fryer confirmed.  I just moved this to ‘canceled’ with resolution ‘Known issue that we can’t fly in this type of weather.’

### David Grosher, 2025-02-11

@Scott Whitney @Eric Brewer @Ben Triplett Please create an issue to capture the CA for excluding erroneous LRF measurements. Then we can close this issue.

### Scott Whitney, 2025-02-11

@David Grosher - Created https://jenaero.atlassian.net/browse/FS2-2851  and https://jenaero.atlassian.net/browse/FS2-2852

### David Grosher, 2025-08-15

Closed - Will track as a project for Blk Upgrade to enable operation in Artic conditions.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [Mishap Reporting FZFG LRF.docx](attachments/25980_Mishap%20Reporting%20FZFG%20LRF.docx.md) | docx | 53 | 2025-02-05 | converted |
| T95_V500_250203_111706_pack.zip | archive | 7508 | 2025-02-05 | listed only |
| T95_V500_250204_111241_pack.zip | archive | 4195 | 2025-02-05 | listed only |
