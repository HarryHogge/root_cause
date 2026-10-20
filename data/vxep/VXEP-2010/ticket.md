# VXEP-2010: Next Gen HIL Sim

- **Issue type:** Minor Project
- **Status:** New
- **Priority:** Low
- **Created:** 2026-10-01
- **Updated:** 2026-10-02
- **Reporter:** Levi Purdy
- **Assignee:** Levi Purdy
- **Creator:** Levi Purdy
- **Links:** is implemented by FS2-5172 (HIL Sim MVP); is implemented by FS2-5210 (HIL Sim Reach Goals)

## Description

**Justification**

- John Clark is retiring, so HIL 1.1 / HIL 1.2 will no longer receive updates.
- HIL sim must keep supporting upcoming projects and the continual release of new sim models from Ben Triplett.
- This is an opportunity to rearchitect HIL 1.1 into something maintainable and extensible that runs on the MCM / Linux first (Windows possibly later).

**Approach**

Replace the existing infrastructure with more maintainable infrastructure, modeled on Training SIL (VXEP-1231):
- Container-based builds
- Build infrastructure like sil / training-sil
- Migrate from Bitbucket to GitHub (Edge-Autonomy org)

Work is tracked in FS2 epics linked to this project ("implements"). Task summaries use the hil-sim: prefix.
**Repos**

- Edge-Autonomy/hil-sim
- Edge-Autonomy/hil-sim-model-repo (Ben Triplett's models, consumed as a submodule)

**Scope**

**MVP: FS2-5172 HIL Sim MVP**

Done when:
- Another developer can support the project using only the repo and docs.
- Every release comes out of a defined build process (containerized CI).
- The released product can run any aircraft that Ben's current model supports.

Scope:
- Ben Triplett's sim models as a git submodule
- GitHub repo with containerized GitHub Actions build and test pipeline
- Web GUI: select aircraft, start/stop, override key values, issue HIL commands
- Installable package (.deb or self-contained .tar.gz)
- Runs on MCM / Linux

**Ongoing**

- Onboard new sim models from Ben Triplett as they are released

**Reach goals: FS2-5210 HIL Sim Reach Goals**

- Windows host support
- Run on an RT (PREEMPT_RT) kernel
- DTED terrain elevation. Today HIL 1.1 uses a fixed 926 ft ground and Speedgoat models use a flat plane at takeoff altitude. Candidate sources: Edge-Autonomy/sil-dted or the DTED already on the MCM (watch for circular dependency).
- Extensibility for new features and contributors (Wesley Reynolds offered to help once the container pipeline exists)

**Known problems with current infrastructure**

- hil-1.2 stores aircraft models on orphaned branches (8 unrelated root commits: VXE, Havoc, B30, B40, ...), so there is no shared history to diff or merge across models.
- HIL 1.1 is a Windows-only C# app + Simulink DLL, distributed from \\condor\Software\hil-1.1\build, configured through C:\Users\Public\HILStuff.txt, with pitot press triggered by a PitotPress.txt file.

**Context links**

Legacy repos (Bitbucket)
- hil-1.1
- hil-1.2
- useful-scripts/hil-1.1-gui
- xpi / xplane-plugin

Reference repos (GitHub)
- Edge-Autonomy/sil
- Edge-Autonomy/dynamic-sim
- Edge-Autonomy/sil-dted

Confluence
- HIL 1.1 GUI
- HIL 1.1 - Simulink Integration with HIL
- HIL Host Cheat Sheet
- XPlane HIL 1.0 Update
- How to Remotely Connect to the HIL Hosts
- Customer HIL Box Details
- Training SIL

Related Jira
- VXEP-1231 Training SIL (structure reference)
- FS2-5125 / FS2-5126 / FS2-4867 SIL GitHub CI
- FS2-4596 SIL migration to GitHub
- FS2-5027 Build UAP B30 HIL 1.1
- FS2-5109 B40 model flight tested
- FS2-2619 Simulink model tested
- FS2-2503 Aborts in SG HIL with VXE30 models

## Comments (0)

## Attachments (0)
