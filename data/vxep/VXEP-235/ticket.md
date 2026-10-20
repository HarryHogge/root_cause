# VXEP-235: Source new version of PN 100-104382 SD Card, current version is expiring

- **Issue type:** Problem
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-07-31
- **Updated:** 2025-02-28
- **Resolved:** 2025-02-28
- **Reporter:** Former user
- **Assignee:** David Grosher
- **Creator:** Former user
- **Links:** relates to VXEP-236 (Systemic SD card Investigation VXE-522 XCOM board failures at LM Source inspection)
- **Part Number(s):** 100-104382
- **Production Stakeholder:** Emalee Johnson
- **Problem Type:** Part Obsolescence

## Description

Current SD card 64GB is becoming obsolete, need to source newer version SDSQUNC-064G-GN6MA (MFG PN)  100-104382 (IPN).  We have 30 on hand (vending machine) and 40 on hand with current supplier, as safety stock in their store.

Vault version is old. Is: Sandisk - SDSQUAB-064G-GN6MA [we may have been using this since Jan 2023?? found in AC 508’s XCOMM]
Was (still currently shown in vault): Sandisk - QUNC-064G-GN6MA

## Comments (19)

### Greg Fryer, 2023-08-02

@Former user Do we have a run-out date for these (e.g. a deadline)? Also, obsolescence issues need to be a “Problem” not an “Improvement” - we fixed this one, but we’ll see problems faster than improvements.

### Former user, 2023-08-02

@Greg Fryer we have 30 in house and 40 at Fastenal, I can still get more through Fastenal, so at this time I do not have a run-out date.  I will speak with Blair to find out when his hard date ends for procurement.  I should have an answer by Friday 8/4/23

### John Clark, 2023-08-03

@Former user @Former user I assigned this to Logan, but either or both of you may do this. I need some alternative 64 GB or larger with the same read/write speeds and form factors. Thanks!!

### Former user, 2023-08-03

Part Code: SDSQUNC-064G-GN6MA
Things we need to know
- Life cycle
- Read/write max/min speeds
- Operable temperatures

I found a single resource in decoding SanDisk identification codes, but they do not completely describe our specific component. SanDisk does not seem to have an easy-to-find method of stripping and decoding their unique ID’s for their SD cards. I attached screenshots of the support items that I could find that helped me arrive to this understanding. More digging required, but I will be working on a Python script for testing. If you have questions to pick up where I left off, message me on teams!
Decipher SanDisk ID’s (IMG name:  sandisk_read_code.png): https://forums.sandisk.com/t/questions-about-uhs-i-and-sandisk-part-numbers/34879 
Extremely similar part (I highlighted the difference in the image: sandisk_similar.png): https://www.westerndigital.com/products/memory-cards/sandisk-extreme-pro-uhs-i-microsd#SDSQXCU-064G-GN6MA 
A standard way to decode SD card ID’s: https://www.the-digital-picture.com/News/News-Post.aspx?News=30207&Title=What-do-the-Numbers-and-Symbols-on-SD-SDHC-and-SDXC-Memory-Cards-mean 
Nearly exact copy, off by one letter which I also highlighted (IMG name: nearly_exact.png): https://www.zoro.com/sandisk-64gb-an6ma-ultra-usd-sdsqunc064gan6m-sdsqunc-064g-an6ma/i/G5446638/?utm_source=google&utm_medium=surfaces&utm_campaign=shopping%20feed&utm_content=free%20google%20shopping%20clicks&gclid=EAIaIQobChMIsLuqgPDAgAMVitHCBB3Ojwl2EAQYBSABEgK95_D_BwE 
General SanDisk SD resource (most in this category have similar characteristics for details we are interested in): https://documents.westerndigital.com/content/dam/doc-library/en_us/assets/public/sandisk/product/memory-cards/extreme-uhs-i-microsd/data-sheet-extreme-uhs-i-microsd.pdf

### Former user, 2023-08-03

The image, sandisk1.png, comes from my last link **

### Former user, 2023-08-03

To compound on what Logan said, the official SanDisk website (Western Digital) doesn’t seem to have the original SD card or its specs. I did find three external sites that offer the SD card that matches exactly the code SDSQUNC-064G-GN6MA, which at least gives a good baseline for the specs. 
  
https://www.amazon.com/SanDisk-microSDXC-Standard-Packaging-SDSQUNC-064G-GN6MA/dp/B010Q588D4?th=1 
Newegg microSDXC SDSQUNC-064G-GN6MA  
SDSQUNC-064G-GN6MA SanDisk Flash Memory Card (memory4less.com)

The links are for Amazon, Newegg, and memory4less respectively. These sites, (especially memory4less) aren’t for purchasing the product, just to serve as a launch point for comparing new SD cards since the official SanDisk website doesn’t seem to have SDSQUNC-064G-GN6MA listed.

To the best of my knowledge from the external sites, the important specs to compare are ~80MB/s transfer speed and an operating temperature of -25C-85C. The only info about life cycles (that I could find) are the warranties offered.
I compiled a small sheet that has a few alternatives, which I did manually. Logan can probably find better alternatives but it’s a start. Most likely it will be useful to just look through the SanDisk alternatives, but I put a few microSD’s from other manufacturers just in case.
[embedded: Microsd Comparisons.xlsx]
Just a few things to note about the sheet, most, if not all, of the SD’s listed offer a larger storage. Also, I did not include a price column since I can’t compare the pricing to the original, but I can add it later if that would be of use. The test function in the top right corner is just a more reliable way than comparing by eye to check two ID’s, you can just copy and paste a SanDisk part ID in the Test column and it will compare the two values.
I will continue trying to dig a little deeper and find the original part data sheet, but I hope this can help further things along.

### Former user, 2023-08-08

@Former user I was able to reach out to a representative from Western Digital and this was the response, in essence this product will not have an end of life, the distributor that communicated this with us was incorrect.  “Thank you for contacting Western Digital Customer Service and Support.  My name is Ronnie K.  I understand that you want to know the availability of the SanDisk Ultra Micro SDXC C10 64GB memory card. We would like to inform you that, we do not have any End Of Life(EOL) notification for these memory cards.”  I have the email saved and can communicate any future queries to Western Digital if further clarification is needed.  
Researching a backup option is great, but moving forward this product should continue to be available per the manufacturer.

### Emalee Johnson, 2024-01-10

@Greg Fryer Can we get this reprioritized? I think its slipping through the cracks because the assignee is deactivated. @Spenser Bracken said we are having a lot of difficulty procuring and now we are running into shortages for XCOMM and red AP.

### Spenser Bracken, 2024-01-10

@Greg Fryer, @Emalee Johnson is correct, Fastenal is the only vendor that can source these cards for us anymore and I know their supply is finite as we are more than a generation or two behind what is current on the market. We’ll need to update sooner than later, but I will reach out to Fastenal to see if I can quantify “finite” in the meantime. Thanks!

### Greg Fryer, 2024-01-10

@David Grosher Looks like this didn’t close before the interns left. Likely this is blowing up given the time lag. Need to figure out if your folks or if @Cameron Chapman can find someone?

### Greg Fryer, 2024-01-10

@Spenser Bracken @Emalee Johnson Re-done, your assessment is correct,

### Cameron Chapman, 2024-01-10

@David Grosher or @John Clark are you able to list any requirements from a software/embedded perspective? 
Are the requirements just as good/better than the existing? 
We might be able to derive requirements from the schematic if you do not know/have any.

### David Grosher, 2024-01-10

@Cameron Chapman Yes as good as or better than current is essentially the requirement. Something to check explicitly is the write fatigue to ensure the life is long enough.

### Matt Philley, 2024-04-08

@Greg Fryer @David Grosher @Cameron Chapman 
I posted more info in the AC522 & 529 investigation, but adding comments here since there is overlap and this ticket has not been resolved.
This new SD card has been used in Production in aircraft as early as AC 508 which had its XCOM produced back in Jan 2023… Vault still calls out the old SD card. 
Can we get this one across the finish line?

### Matt Philley, 2024-04-08

Duplicating this comment since I am not sure if its related to investigation or just the approval of this yet…
Ryan and I did a spot-check on some old problem XCOM and red AP boards hes been collecting and it looks like for some period of time… maybe mid-2022 to mid-2023(?) we were using a mixture of both SD cards. No idea if this relates to our SD card corruption issue, but worth knowing either way. 
We found “new” SDSQUAB-064G-GN6MA SD cards in boards from 2022.
We also found “old” QUNC-064G-GN6MA SD cards in boards from mid-2023.

### Matt Philley, 2024-06-14

@John Clark here is the Jira ticket that had info on current spec of SD card we are using. It also has PN for the card. There might be more info in the vault datacard, but im not confident on that. 
@Ryan Ferguson FYSA

### John Clark, 2024-06-14

@Scott Hunter , this is what you are looking for, I think let me know if it isnt.

### Scott Hunter, 2024-06-14

@John Clark - That’s what I’m looking for, thanks.

### Matt Philley, 2025-02-28

@David Grosher FYSA moving this to complete based on the completion of the SD Card Replacement project for some Jira cleanup.

## Attachments (6)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [Microsd Comparisons.xlsx](attachments/15678_Microsd%20Comparisons.xlsx.md) | xlsx | 15 | 2023-08-03 | converted |
| nearly_exact.PNG | image | 188 | 2023-08-03 | listed only |
| possibly_useful.PNG | image | 197 | 2023-08-03 | listed only |
| sandisk1.PNG | image | 106 | 2023-08-03 | listed only |
| sandisk_read_code.PNG | image | 55 | 2023-08-03 | listed only |
| sandisk_similar.PNG | image | 41 | 2023-08-03 | listed only |
