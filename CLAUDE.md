# root_cause: Working Rules for Claude Code

Read this file at the start of every session.

## What this project is

Claude Code reads the VXEP Jira tickets, with their comments and the text of their attachments, and works out each incident's root cause as specifically as the evidence allows: "right front ESC", not "hardware". The results are written up as reports.

The sandbox cannot reach Jira. The tickets are exported on the local machine by `scripts/export_jira.py` and committed as text under `data/`. Treat `data/` as read only: never edit it. It is replaced by re-running the export.

## How work runs

1. Scott names a branch and one prompt file, for example: "Work on branch <name>. Pull it, then read and carry out prompts/01_corpus_survey.md." Carry out that prompt only.
2. Work on the branch Scott named. If none was named, ask before committing. Never push to `main` unless Scott says so.
3. Write the output where the prompt says, normally `reports/NN_<name>.md`, numbered to match the prompt. Start every report with the branch and the commit the work started from.
4. Commit and push, naming the prompt number in the commit message.

Each prompt says where it runs: `Sandbox` or `Local machine`.

## Chat replies

- When a prompt completes and its report is committed, reply with exactly: "Prompt run successfully, report authored and committed."
- If a prompt cannot be completed, reply in one line: "Prompt stopped: <reason in under 20 words>. Details in <report path>."
- Ask a question in chat only when the work cannot continue without Scott's answer.

## Rules

1. **Evidence, not guesses.** Every root cause names the ticket text it rests on: the file (`ticket.md` or an attachment) and a short quote. If the evidence does not support a specific component, say how far it does narrow things and what would settle it. A confident wrong answer is worse than "not determined".
2. **Keep the team's words separate from yours.** The Root Cause field and comments are what engineers wrote. Your conclusions are yours. Never present one as the other.
3. **`data/` is read only.** Never edit, move or delete anything under `data/`.
4. **Read only towards Jira.** Nothing in this project writes to Jira or any other company system.
5. **No secrets in the repo.** No tokens or passwords in any file, report or commit.
6. **Never fail silently.** Tickets you could not read or did not get to are listed as such, never left out quietly. A partial run is reported as partial.
7. **Product decisions belong to Scott.** The vocabulary of components, what counts as "determined", and what the reports show: propose and ask. Technical choices are yours; explain them in plain terms.
8. **Diagnostics are read only.** When a prompt says it is a diagnostic, report findings and change nothing outside `reports/`.

## Writing style

Plain language for a mechanical engineer, not a software engineer. No em dashes in any document or commit message. Be specific: ticket keys, numbers, names, file paths.

## Where things are

| Path | Contents |
| --- | --- |
| `data/vxep/<KEY>/ticket.md` | One ticket: fields, every comment, a table of attachments |
| `data/vxep/<KEY>/attachments/*.md` | Text pulled from one attachment |
| `data/vxep/index.jsonl` | One line per ticket: key, summary, status, dates, labels, attachment counts |
| `data/vxep/manifest.json` | When the export ran, attachment results, every conversion failure |
| `data/linked/<KEY>/` | Tickets in other projects (VA, FS2, RMA, ENG, XKIT ...) that VXEP incidents point to, written the same way. `data/linked/index.jsonl` gives `referenced_by` for each; `manifest.json` lists any Jira did not return |
| `docs/decisions.md` | Scott's decisions, with reasons |
| `prompts/` | Numbered task prompts |
| `reports/` | Numbered outputs, one per prompt |
| `results/` | Structured results produced by prompts |
| `scripts/export_jira.py` | The exporter (local machine only) |
