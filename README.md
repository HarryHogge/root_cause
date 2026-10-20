# root_cause

Claude Code reads the VXEP Jira tickets, their comments and the text of their
attachments, and narrows each incident's root cause as far as the evidence
allows: "right front ESC", not "hardware".

## How work runs

1. A prompt is written and committed as `prompts/NN_<name>.md`.
2. In the sandbox, Claude Code is told: "Work on branch <name>. Pull it, then
   read and carry out `prompts/NN_<name>.md`."
3. Claude Code writes `reports/NN_<name>.md` (and anything under `results/`
   the prompt asks for), commits and pushes.
4. Scott pulls and reviews the report.

Working rules are in `CLAUDE.md`; decisions in `docs/decisions.md`.

## The data

The sandbox cannot reach Jira, so the tickets are exported on the local
machine and committed as text under `data/vxep/`: one folder per ticket with
`ticket.md` and the converted text of its documents in `attachments/`.

To refresh it (local machine only):

```
python -m venv .venv
.venv/bin/pip install -r requirements-local.txt
.venv/bin/python scripts/export_jira.py --env <dotenv with JIRA_URL, JIRA_EMAIL, JIRA_API_TOKEN> \
    --cache ../root_cause_local/attachments --project VXEP
```

On Windows use `.venv\Scripts\pip` and `.venv\Scripts\python`.

Downloaded originals go in `--cache`, which must be outside the repository, so
a re-run only downloads new attachments. `data/vxep/manifest.json` records
when the export ran and every attachment that could not be converted.
