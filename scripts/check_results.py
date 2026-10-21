"""Check prompt 02 and 03 result files. Reads data/ and results/, writes nothing.

    python scripts/check_results.py                 every results/02/batch_*.jsonl, and results/02_all.jsonl if present
    python scripts/check_results.py 001 002         only those batches
    python scripts/check_results.py results/02_all.jsonl
    python scripts/check_results.py results/03_image_trial.jsonl

Checks, from report 01 D2:
  - every line parses as JSON and has every field, in order
  - fixed-vocabulary fields hold an allowed value
  - every evidence quote is found word for word in the file it cites
  - no em dashes anywhere
  - each batch file has exactly one line per key in its batch (02_all.jsonl: every key, in order;
    any other file: Incident (8D) keys, each once)
  - a position naming a motor number uses the agreed words (VXEP-272 numbering)

Prompt 03 additions:
  - a line may carry the four image fields after the report 02 fields
  - evidence citing a file under an images/ folder is a reading of the image, not a quote,
    so only the file's existence is checked

Exit code 0 when everything passes, 1 otherwise.
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FIELDS = [
    'key', 'event', 'tail', 'outcome', 'system', 'component', 'position', 'position_as_written',
    'failure_mode', 'initiating_cause', 'contributing', 'confidence', 'evidence', 'team_root_cause',
    'team_view_in_comments', 'agrees_with_team', 'disagreement', 'would_settle_it', 'attachments_read',
    'linked_read', 'reasoning', 'notes',
]
IMAGE_FIELDS = ['images_read', 'image_finding', 'image_effect', 'changed_from_02']
IMAGE_EFFECTS = {'settled', 'narrowed_further', 'supports', 'contradicts', 'no_help'}
ALLOWED = {
    'outcome': {'determined', 'narrowed', 'not_determined', 'no_fault_found'},
    'system': {'', 'propulsion', 'power_connector', 'battery', 'fuel_cell', 'harness', 'avionics_hw',
               'sensors_air_data', 'gps', 'radio_link', 'vehicle_software', 'ground_software',
               'operator_procedure', 'environment', 'manufacturing_quality', 'airframe', 'payload',
               'ground_equipment'},
    'initiating_cause': {'design', 'manufacturing_quality', 'maintenance_or_assembly', 'operator_action',
                         'outdated_software_or_ads_not_applied', 'environment', 'wear_or_age', 'unknown'},
    'confidence': {'high', 'medium', 'low'},
    'agrees_with_team': {'yes', 'more_specific', 'differs', 'no_team_answer'},
}
SETTLE_KINDS = {'image', 'csv', 'aar_or_archive', 'video', 'other_attachment', 'linked_ticket',
                'external_document', 'physical_inspection'}
LIST_FIELDS = {'contributing', 'evidence', 'would_settle_it', 'attachments_read', 'linked_read', 'images_read'}
MOTOR_WORDS = {'1': 'front left', '2': 'front right', '3': 'rear right', '4': 'rear left'}
EM_DASH = '—'

_file_cache = {}


def squash(s):
    return re.sub(r'\s+', ' ', s).strip()


def file_text(rel):
    if rel not in _file_cache:
        path = os.path.join(ROOT, rel)
        try:
            with open(path, encoding='utf-8') as fh:
                t = fh.read()
            _file_cache[rel] = (t, squash(t))
        except OSError:
            _file_cache[rel] = None
    return _file_cache[rel]


def check_record(r, where):
    errs = []
    has_image = list(r.keys()) == FIELDS + IMAGE_FIELDS
    if list(r.keys()) != FIELDS and not has_image:
        missing = [f for f in FIELDS if f not in r]
        extra = [f for f in r if f not in FIELDS]
        errs.append('%s: fields wrong (missing %s, extra %s, or out of order)' % (where, missing, extra))
        return errs
    for f, ok in ALLOWED.items():
        if r[f] not in ok:
            errs.append('%s: %s has value %r' % (where, f, r[f]))
    if has_image:
        if r['image_effect'] not in IMAGE_EFFECTS:
            errs.append('%s: image_effect has value %r' % (where, r['image_effect']))
        for p in r['images_read'] if isinstance(r['images_read'], list) else []:
            if not os.path.isfile(os.path.join(ROOT, p)):
                errs.append('%s: image in images_read not found: %s' % (where, p))
    for f in FIELDS + (IMAGE_FIELDS if has_image else []):
        if f in LIST_FIELDS:
            if not isinstance(r[f], list):
                errs.append('%s: %s should be a list' % (where, f))
        elif not isinstance(r[f], str):
            errs.append('%s: %s should be text' % (where, f))
    if EM_DASH in json.dumps(r, ensure_ascii=False):
        errs.append('%s: contains an em dash' % where)
    if isinstance(r['evidence'], list):
        if not r['evidence']:
            errs.append('%s: evidence is empty' % where)
        for e in r['evidence']:
            if not isinstance(e, dict) or set(e) != {'file', 'quote'}:
                errs.append('%s: evidence item should be {file, quote}: %r' % (where, e))
                continue
            if not e['file'].startswith('data/'):
                errs.append('%s: evidence file not under data/: %s' % (where, e['file']))
                continue
            if '/images/' in e['file']:
                # A reading of an image, in the analyst's words: only the file must exist.
                if not os.path.isfile(os.path.join(ROOT, e['file'])):
                    errs.append('%s: image evidence file not found: %s' % (where, e['file']))
                elif not squash(e['quote']):
                    errs.append('%s: empty image reading' % where)
                continue
            t = file_text(e['file'])
            if t is None:
                errs.append('%s: evidence file not found: %s' % (where, e['file']))
            elif e['quote'] not in t[0] and squash(e['quote']) not in t[1]:
                errs.append('%s: quote not found in %s: %r' % (where, e['file'], e['quote'][:80]))
            elif not squash(e['quote']):
                errs.append('%s: empty quote' % where)
    if isinstance(r['would_settle_it'], list):
        for w in r['would_settle_it']:
            if not isinstance(w, dict) or set(w) != {'file', 'kind', 'what'} or w.get('kind') not in SETTLE_KINDS:
                errs.append('%s: would_settle_it item should be {file, kind, what} with a known kind: %r' % (where, w))
    if r['disagreement'] and r['agrees_with_team'] != 'differs':
        errs.append('%s: disagreement filled but agrees_with_team is %s' % (where, r['agrees_with_team']))
    if r['agrees_with_team'] == 'differs' and not r['disagreement']:
        errs.append('%s: differs without a disagreement paragraph' % where)
    for m in re.finditer(r'motor (\d)\b(?: \(([^)]*)\))?', r['position']):
        num, words = m.group(1), m.group(2)
        if num not in MOTOR_WORDS:
            errs.append('%s: position names motor %s' % (where, num))
        elif words is None or words != MOTOR_WORDS[num]:
            errs.append('%s: position %r should read "motor %s (%s)"' % (where, r['position'], num, MOTOR_WORDS[num]))
    return errs


def short(keys):
    return '%s (%d)' % (keys[:10] + (['...'] if len(keys) > 10 else []), len(keys))


def read_lines(path):
    recs, errs = [], []
    with open(path, encoding='utf-8') as fh:
        for n, line in enumerate(fh, 1):
            if not line.strip():
                continue
            try:
                recs.append(json.loads(line))
            except ValueError as ex:
                errs.append('%s line %d: does not parse: %s' % (os.path.relpath(path, ROOT), n, ex))
    return recs, errs


def check_file(path, expected_keys):
    recs, errs = read_lines(path)
    rel = os.path.relpath(path, ROOT)
    keys = [r.get('key') for r in recs if isinstance(r, dict)]
    if isinstance(expected_keys, set):
        # Not a batch or the full run: keys must be incident keys, each once, any number.
        unknown = [k for k in keys if k not in expected_keys]
        dup = sorted({k for k in keys if keys.count(k) > 1})
        if unknown or dup:
            errs.append('%s: keys not in the incident list %s, or repeated %s' % (rel, short(unknown), short(dup)))
    elif keys != expected_keys:
        missing = [k for k in expected_keys if k not in keys]
        extra = [k for k in keys if k not in expected_keys]
        dup = sorted({k for k in keys if keys.count(k) > 1})
        errs.append('%s: keys do not match the batch list (missing %s, extra %s, repeated %s, or out of order)'
                    % (rel, short(missing), short(extra), short(dup)))
    for r in recs:
        if isinstance(r, dict):
            errs += check_record(r, '%s %s' % (rel, r.get('key')))
        else:
            errs.append('%s: a line is not a JSON object' % rel)
    return len(recs), errs


def main(argv):
    with open(os.path.join(ROOT, 'results', '02_batches.json'), encoding='utf-8') as fh:
        batches = {b['batch']: b['keys'] for b in json.load(fh)['batches']}
    all_keys = [k for b in sorted(batches) for k in batches[b]]
    targets = []
    if argv:
        for a in argv:
            if re.fullmatch(r'\d{1,3}', a):
                b = '%03d' % int(a)
                targets.append((os.path.join(ROOT, 'results', '02', 'batch_%s.jsonl' % b), batches.get(b)))
            else:
                p = os.path.abspath(a)
                if not os.path.exists(p) and os.path.exists(os.path.join(ROOT, a)):
                    p = os.path.join(ROOT, a)
                m = re.search(r'batch_(\d{3})\.jsonl$', p)
                if m:
                    targets.append((p, batches.get(m.group(1))))
                elif os.path.basename(p) == '02_all.jsonl':
                    targets.append((p, all_keys))
                else:
                    targets.append((p, set(all_keys)))
    else:
        for p in sorted(glob.glob(os.path.join(ROOT, 'results', '02', 'batch_*.jsonl'))):
            targets.append((p, batches.get(re.search(r'batch_(\d{3})', p).group(1))))
        allp = os.path.join(ROOT, 'results', '02_all.jsonl')
        if os.path.exists(allp):
            targets.append((allp, all_keys))
    if not targets:
        print('No result files to check.')
        return 1
    problems = 0
    for path, expected in targets:
        rel = os.path.relpath(path, ROOT)
        if expected is None:
            print('FAIL %s: not a batch in results/02_batches.json' % rel)
            problems += 1
            continue
        if not os.path.exists(path):
            print('FAIL %s: file not found' % rel)
            problems += 1
            continue
        n, errs = check_file(path, expected)
        print('%s %s: %d lines, %d problems' % ('ok  ' if not errs else 'FAIL', rel, n, len(errs)))
        for e in errs:
            print('     ' + e)
        problems += len(errs)
    done = sum(1 for b in batches if os.path.exists(os.path.join(ROOT, 'results', '02', 'batch_%s.jsonl' % b)))
    print('Batch files present: %d of %d.' % (done, len(batches)))
    return 0 if problems == 0 else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
