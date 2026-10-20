# VXEP-703: 2118737-01, VXE30 Std Config, Wing Utility Drop Kit - Engineering Drawing

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2024-10-02
- **Updated:** 2025-01-06
- **Resolved:** 2025-01-06
- **Due:** 2024-12-19
- **Reporter:** Matt Philley
- **Assignee:** Gerrit Sperling
- **Creator:** Matt Philley
- **Labels:** Gen1-Utility-Dropper
- **Parent:** VXEP-697 Practice Build - 2118737-01, VXE30 Std Config, Wing Utility Drop Kit
- **Epic Link:** VXEP-697
- **Start date:** 2024-12-06
- **Issue color:** purple

## Description

Update to 2118720 dwg:
We would like an internal PN created for the case plates that are used to make 2118725-01 transit case label (description: 6.0" x 3.0"; .005" satin photosensitive anodized aluminum foil; 3M 467MP adhesive back; solid black surface (no image); radius corners). 
One option is to make an entire drawing for the label and then call out the material IPN in that label BOM. I think an easier option that would work just as well is to add the case plate mat’l to the Transit Case BOM 2118720-01, and then add a dwg note that says the case plate will be engraved to make 2118725-01.
If we end up using similar labels in the future, it would be handy to make a reference document/spec sheet for the different aluminum plates. 
This change will be added to the Wing Dropper Collector Jira when its ready for CCB https://jenaero.atlassian.net/browse/ENG-2799

## Comments (5)

### Nina Menon, 2024-12-13

@Gerrit Sperling do you have time to look at this request for Wing Dropper? If there are any questions let me know.

### Gerrit Sperling, 2024-12-16

@Nina Menon I am working on a burndown list for releasing drop payload documents right now. I should be able to get to this.

### Gerrit Sperling, 2024-12-16

@Nina Menon do you have any vendor info for 6.0" x 3.0"; .005" satin photosensitive anodized aluminum foil; 3M 467MP adhesive back; solid black surface (no image); radius corners ?

### Gerrit Sperling, 2024-12-16

Created PN 2121111-01 for the COTS part from PHOTO-GRAPHICS
I made a drawing for the 2118725-01 with a note saying to engrave using the word doc file under the same PN. 

FYSA @Nina Menon

### Gerrit Sperling, 2025-01-06

@Nina Menon I am closing this ticket and adding 211875-01 to the CCB release ticket linked above

## Attachments (0)
