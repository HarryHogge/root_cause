# VXEP-450: Update AHRS production configuration procedure p/n: 111-105595

- **Issue type:** Task
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2024-06-27
- **Updated:** 2026-03-30
- **Resolved:** 2026-03-30
- **Reporter:** Hayden Jeanor
- **Assignee:** Nina Menon
- **Creator:** Hayden Jeanor
- **Links:** relates to VA-2143 (2119841-01 MOD Payload Short Term Retrofit Kit BOM)

## Description

Todo:
- follow procedure yourself to program a unit
- add any of your own redlines
- rev doc with updates
- pass to HJ for peer review

## Issue Status

Needs updates to config procedure and assembly procedure to reflect changes captured in https://jenaero.atlassian.net/browse/VA-2143

## Comments (10)

### Adrian Garcia, 2024-07-02

@Cameron Chapman

### Adrian Garcia, 2024-07-03

@Connor Peebles @Garrett O'Neill or @Emalee Johnson are you able to peer review this: 111-105595 AHRS Configuration Procedure in the Vault

### Emalee Johnson, 2024-07-05

@Adrian Garcia I will have production review it and let you know if there is any feedback.

### Emalee Johnson, 2024-07-09

@Adrian Garcia I shared this with the production team and it looks like the only note is that the formatting is not updated to what we currently use in production for procedures. I think the content looks good though.
@Royce Ferriday Please feel free to add any more details from your review.

### Adrian Garcia, 2024-07-09

@Emalee Johnson are you able to provide the correct formatting? Thank you

### Royce Ferriday, 2024-07-10

@Adrian Garcia An example could be any powerpoint procedure we have in the vault, aside from it not matching it looks fine to me. Since there are several formats, I would reach out to Sam O. for formatting help. Unfortunately, I can’t tell what has been changed, so once an AHRS kit is requested I’ll let you know if there is any confusion.

### Emalee Johnson, 2024-07-10

@Adrian Garcia Our template is located here: "C:\JAI Vault 1\Production eng\0 - Templates\PN - Area - Description - Procedure (TEMPLATE).pptx"

### Adrian Garcia, 2024-07-11

@Emalee Johnson Updated to PPT format. Ready for review/release 
"C:\JAI Vault 1\Projects\111 - MOD Payload\Electrical Design\111-105595 AHRS Configuration Procedure.pptx"

### Hayden Jeanor, 2024-12-24

@Nina Menon this procedure needs to be updated to reflect the latest firmware release and configuration changes. Changes tracked here AHRS Design Consideration table.xlsx. New configuration and firmware has been uploaded to the vault C:\JAI Vault 1\Projects\111 - MOD Payload\Electrical Design\111-104685 AHRS Resources but not yet released. I ran into an issue yesterday where some configurations, that @Kurt Burian and i had previously specified, were unconfigurable with the current firmware. once we get approval from Kurt, we are good to solidify the production config and fw
[embedded: image-20241223-235909.png]
Posting me and Kurt’s conversation for context: 
another thing we have to determine: 
 
[embedded: image-20241224-182339.png]

[embedded: image-20241224-182347.png]
we approved the configuration in green, but the current firmware wont let the use configure the polarity and duration if direct pps mode is selected. The standard is weird because this is what it specifies, so not sure how that correlates to the configs options
 
[embedded: image-20241224-182357.png]
also were able to config those with mode set to "event in A"
 
[embedded: image-20241224-182408.png]
also, these two configs only have the options of "on new data" and "disabled"

[embedded: image-20241224-182416.png]

that one im alot more comfortable just changing back to 'on new data'

### Hayden Jeanor, 2025-01-21

Discussed with @Kurt Burian, locked down config file and firmware. Released to vault

## Attachments (6)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20241223-235909.png | image | 19 | 2024-12-24 | listed only |
| image-20241224-182339.png | image | 1 | 2024-12-24 | listed only |
| image-20241224-182347.png | image | 14 | 2024-12-24 | listed only |
| image-20241224-182357.png | image | 13 | 2024-12-24 | listed only |
| image-20241224-182408.png | image | 3 | 2024-12-24 | listed only |
| image-20241224-182416.png | image | 8 | 2024-12-24 | listed only |
