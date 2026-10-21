"""Export shrunk copies of the images named in root cause results.

Runs on the local machine, like export_jira.py. For each ticket key given, it
takes the first image listed in that result's would_settle_it, downloads it
from Jira and writes a shrunk copy next to the ticket:

    data/vxep/VXEP-123/images/<attachment id>_<name>.png|jpg

Plots and screenshots stay PNG so their text stays sharp; photos become JPEG.
The long side is cut to MAX_SIDE pixels and all metadata (camera, GPS
location) is dropped. data/images_manifest.json records every image asked
for and what happened, including the ones that failed.

    .venv/bin/python scripts/export_images.py --env ../jira-dash/.env \\
        --cache ../root_cause_local/attachments \\
        --results results/02_all.jsonl --keys VXEP-1974,VXEP-1488

Re-running adds to the manifest; images already written are kept.
"""
import argparse
import io
import json
import os
import sys
from datetime import datetime, timezone

from PIL import Image, ImageOps

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from export_jira import Jira, fetch_attachment, safe_name  # noqa: E402

# Longest side, in pixels. Larger images are scaled down by the model anyway,
# so anything bigger only costs more to commit and to read.
MAX_SIDE = 1568
JPEG_QUALITY = 85
# A PNG bigger than this after shrinking is a photo, not a plot: write JPEG.
PNG_MAX_BYTES = 800 * 1024
PHOTO_KINDS = ('.jpg', '.jpeg', '.jfif', '.heic', '.tif', '.tiff', '.bmp', '.webp')


def shrink(data, filename):
    """Returns (bytes, extension, (width, height) before, (width, height) after)."""
    img = Image.open(io.BytesIO(data))
    img = ImageOps.exif_transpose(img)          # phone photos are often stored sideways
    before = img.size
    img.thumbnail((MAX_SIDE, MAX_SIDE))
    out = io.BytesIO()
    if filename.lower().endswith(PHOTO_KINDS):
        img.convert('RGB').save(out, 'JPEG', quality=JPEG_QUALITY, optimize=True)
        ext = '.jpg'
    else:
        if img.mode not in ('RGB', 'RGBA', 'L', 'P'):
            img = img.convert('RGBA')
        img.save(out, 'PNG', optimize=True)
        ext = '.png'
        if out.tell() > PNG_MAX_BYTES:          # a photo saved as PNG
            out = io.BytesIO()
            img.convert('RGB').save(out, 'JPEG', quality=JPEG_QUALITY, optimize=True)
            ext = '.jpg'
    return out.getvalue(), ext, before, img.size


def first_image(result):
    for item in result.get('would_settle_it') or []:
        if item.get('kind') == 'image' and item.get('file'):
            return item['file']
    return None


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('--env', required=True, help='dotenv file with JIRA_URL, JIRA_EMAIL, JIRA_API_TOKEN')
    ap.add_argument('--cache', required=True, help='folder outside the repo for downloaded originals')
    ap.add_argument('--results', required=True, help='results file with would_settle_it, e.g. results/02_all.jsonl')
    ap.add_argument('--keys', required=True, help='comma-separated ticket keys')
    args = ap.parse_args(argv)

    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if os.path.abspath(args.cache).startswith(repo + os.sep):
        sys.exit('--cache must be outside the repository: originals are never committed')
    with open(args.results, encoding='utf-8') as fh:
        results = {r['key']: r for r in map(json.loads, fh)}
    manifest_path = os.path.join(repo, 'data', 'images_manifest.json')
    manifest = {'images': []}
    if os.path.exists(manifest_path):
        with open(manifest_path, encoding='utf-8') as fh:
            manifest = json.load(fh)
    done = {(m['ticket'], m['filename']) for m in manifest['images'] if m.get('result') == 'written'}

    jira = Jira(args.env)
    for key in [k.strip() for k in args.keys.split(',') if k.strip()]:
        entry = {'ticket': key, 'asked_at': datetime.now(timezone.utc).isoformat(timespec='seconds')}
        name = first_image(results[key]) if key in results else None
        if not name:
            entry.update(result='failed', error='no result, or its would_settle_it names no image')
            manifest['images'].append(entry)
            print('%s: %s' % (key, entry['error']), file=sys.stderr)
            continue
        # A file on a linked ticket is written "name (on RMA-745)"
        owner = key
        if name.endswith(')') and ' (on ' in name:
            name, owner = name[:-1].rsplit(' (on ', 1)
        entry.update(filename=name, attachment_on=owner)
        if (key, name) in done:
            continue
        try:
            atts = jira.get('/rest/api/3/issue/%s' % owner, fields='attachment')['fields']['attachment'] or []
            matches = sorted((a for a in atts if a['filename'] == name), key=lambda a: a['created'])
            if not matches:
                raise ValueError('no attachment named %r on %s' % (name, owner))
            att = matches[-1]                   # if a name repeats, the newest copy
            data, ext, before, after = shrink(fetch_attachment(jira, att, args.cache), name)
            folder = 'linked' if not owner.startswith('VXEP-') else 'vxep'
            rel = os.path.join('data', folder, owner, 'images', '%s_%s%s' % (
                att['id'], safe_name(os.path.splitext(name)[0]), ext))
            os.makedirs(os.path.dirname(os.path.join(repo, rel)), exist_ok=True)
            with open(os.path.join(repo, rel), 'wb') as fh:
                fh.write(data)
            entry.update(result='written', file=rel, attachment_id=att['id'],
                         same_name_copies=len(matches), pixels_before=before, pixels_after=after,
                         kb=round(len(data) / 1024))
            print('%s: %s (%d KB)' % (key, rel, entry['kb']), file=sys.stderr)
        except Exception as e:                   # recorded, never silent
            entry.update(result='failed', error='%s: %s' % (type(e).__name__, str(e)[:300]))
            print('%s: %s' % (key, entry['error']), file=sys.stderr)
        manifest['images'].append(entry)

    with open(manifest_path, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(manifest, fh, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    main()
