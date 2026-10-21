# Prompt 03: Image trial on 10 tickets

Runs in: Sandbox
Type: Analysis, small. Change nothing outside `reports/`, `results/` and `scripts/check_results.py`.
Output: `results/03_image_trial.jsonl` and `reports/03_image_trial.md`, committed with the message "Prompt 03: image trial" and pushed.

Read `CLAUDE.md` and the October 21 section of `docs/decisions.md` first.

## Purpose

Report 02, section 9, named one image on each of 75 open tickets that would most likely settle the result. Before exporting all of them, find out on 10 whether looking at the image actually changes results.

**Keep this session small.** The sandbox account has tight usage limits. Do the work yourself in this session, without sub-agents. For each ticket, start from its result in `results/02_all.jsonl`, which already holds the reasoning and the evidence. Re-read the ticket or an attachment only where the image raises a question the result does not answer. Keep the report short.

## The images

`data/images_manifest.json` lists the 10 images. Each one is the first image named in that result's `would_settle_it`. It sits in the ticket's `images/` folder, shrunk to at most 1568 pixels on its long side.

| Ticket | Image | What report 02 said to look for |
| --- | --- | --- |
| VXEP-1974 | `images/63875_image (1).png` | HLB per-cell voltages, which cell dropped |
| VXEP-1488 | `images/31781_vxe-499takeoff.png` | cell voltages at takeoff, which cell |
| VXEP-1965 | `images/63541_image-20260717-025312.png` | HLB cell voltages during landing |
| VXEP-231 | `images/17998_image-20231220-231347.png` | BMS voltage against VTOL measured voltage |
| VXEP-1489 | `images/31853_image-20250828-155107.png` | HLB voltage and current at transition |
| VXEP-426 | `images/33486_image-20250919-190452 (9c8ca7cf-53e2-4748-af48-6cafbe1da696).png` | VTOL FW flag forcing motor 3 to idle against motor 3 current |
| VXEP-1977 | `images/63916_image-20260806-161340.png` | lift throttles, motor 3 saturated at the upset |
| VXEP-279 | `images/18813_image-20240217-054529.jpg` | fire damage: burn origin in ESC or current sense board |
| VXEP-1458 | `images/31078_MAIN fire (1).jpg` | where the fire started |
| VXEP-538 | `images/22414_QORASWCAWE-744NAS2024002 Tile 2 - Broken snips - break.jpg` | fracture location and surface |

They are a mix on purpose: five battery and power plots, two propulsion plots, three photos.

## What to do

For each of the 10 tickets:

1. Look at the image. Describe what it shows in one or two plain sentences: what is plotted or pictured, axes and units if a plot, and anything that bears on the cause.
2. Decide whether it changes the result from report 02. Write the full result again, in the report 02 format, to `results/03_image_trial.jsonl`. Add:
   - `images_read`: the image file paths.
   - `image_finding`: what the image showed, in your words.
   - `image_effect`: one of `settled` (the open question is answered), `narrowed_further`, `supports` (no change, but backs the result), `contradicts` (the image disagrees with the result; explain), or `no_help` (unreadable, or does not bear on the cause).
   - `changed_from_02`: what changed from report 02, or empty.
3. Evidence from an image is cited as `{"file": "<image path>", "quote": "<what is visible, in your words>"}`. Mark these clearly as your reading of the image, not text quoted from it. If the image has text on it (a legend, a label, an error message), quote that text exactly.
4. Be strict. A plot that shows a symptom more clearly is `supports`, not `settled`. A photo where you cannot tell the burn origin is `no_help`. Positions follow the agreed convention, for example "motor 3 (rear right)". On battery plots, say which cell by the plot's own label (for example `bmsV7`), and do not assume that label matches the cell numbering engineers use in the text unless the ticket says so.

Then check the new file with `scripts/check_results.py`. The script cannot find an image quote as text, so extend it:
- for evidence whose file is under an `images/` folder, check only that the file exists;
- accept the four new fields above.

Every other check must stay as it is, and the script must still pass on `results/02_all.jsonl`.

## Report

`reports/03_image_trial.md`, short, in plain language:

1. The branch and the commit the work started from.
2. A table: ticket, what the image showed (one line), `image_effect`, outcome before and after.
3. Counts by `image_effect`, and separately for plots and photos.
4. Anything learned that changes an earlier finding, for example on the cell numbering in report 02, section 3.
5. A recommendation: is it worth doing the other 65, all of them or only some kinds (for example plots only)? Base it on these 10.
6. About how much of the session the 10 used, so Scott can judge the cost of the other 65.
