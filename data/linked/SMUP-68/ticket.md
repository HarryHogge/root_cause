# SMUP-68: Any time the launch wizard is opened it will disable the ‘Land at ELZ’ behavior and select ‘Land at PLZ’.  Operators should always re-select ‘Land at ELZ’ after opening the launch wizard.

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2024-12-10
- **Updated:** 2025-03-16
- **Resolved:** 2025-01-30
- **Reporter:** David Grosher
- **Assignee:** Dana Holley
- **Creator:** David Grosher
- **Fix versions:** New beginnings!
- **Links:** relates to VXEP-604 (VXE 600 Land at ELZ was un-enabled)

## Comments (3)

### Josh Burrell, 2025-01-30

@Dana Holley this looks and sounds like an OPS change so I’m assigning it to you. FYSA

### Dana Holley, 2025-01-30

@David Grosher I’m not quite understanding why the operator would plan a mission using the ELZ in preflight. It seems like this is a safety feature that was built in to reactivate PLZ as the aircraft will most likely become non mission capable after an ELZ landing. However, the information is still relevant to know that this is a feature in the software that’s not documented. I can input a NOTE that states the following, let me know if this works. 
“If planning a mission using the ELZ as the active landing pattern, opening the Launch Wizard will cause the VXE SUAV software to automatically activate the PLZ landing pattern.” @Josh Burrell

### David Grosher, 2025-01-30

@Dana Holley The UK MoD is currently using glide landings as their primary landing method, which is where this observation came from.  I agree that this behavior is probably desired generally and instead of changing anything in the software logic we think just documenting it in the manual would be adequate to address all of the concerns. I think your addition is fine.

## Attachments (0)
