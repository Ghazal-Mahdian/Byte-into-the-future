# Milestones and Progress

**Next IBM milestone deadline recorded by the team: October 23, 2026**  
**Repository review: October 21, 2026**

This checklist compares the files in the repository with the team's documented deliverables. The original IBM assignment guide and submission slides are not included, so full alignment with the official rubric and deadline has not been independently verified.

## Status meanings

- **Included — draft:** the document exists; approval, validation, or submission may still be needed.
- **Reported complete — evidence missing:** the team reports work is complete, but supporting code or results are not uploaded.
- **Partial:** some supporting material exists; specific gaps remain.
- **Missing:** the required artifact or evidence is absent from this repository; it may exist elsewhere.

## IBM SkillsBuild deliverables

| Deliverable | Included evidence | Status | Still needed |
|---|---|---|---|
| Problem statement and empathy map | [Project concept §3–4](project-concept.md) | Included — draft | Team review; validate empathy-map hypotheses with user or mentor feedback |
| AI Agent Architecture — slide 17 | [Week 4 §1](week-4-deliverables.md) | Included — draft | Review against implementation and update the actual submission slide |
| AI Agent Workflow — slide 18 | [Week 4 §2](week-4-deliverables.md) | Included — draft | Confirm approval conditions, retry limits, escalation triggers, and closure authority; update submission slide |
| Tools & Integrations — slide 19 | [Week 4 §3](week-4-deliverables.md) | Included — draft | Confirm actual tools and service access; distinguish optional services in submission slide |
| MVP scope — slide 22 | [Week 4 §4](week-4-deliverables.md), [concept §12](project-concept.md) | Included — draft | Demonstrate successful authorized sandbox handling and critical-case human escalation |
| GitHub repository | README, contributing guide, configuration template, ignore rules, documentation | Included | Upload implementation and evidence listed below |
| Working prototype using IBM Bob | Development reported; [source upload instructions](../src/README.md) only | Reported complete for agents/dashboard — evidence missing | Upload source, dependency manifest, startup instructions, and an end-to-end demonstration; document IBM Bob use |
| Compliant dataset | [12-case synthetic dataset and guide](../data/samples/README.md), baseline, assets/services, mock authorizations, and evaluator-only expected outcomes | Included — v1 development fixture; consistency check passed | Team review of scenario, baseline/scoring/policy; adapt to prototype input and verify assignment requirements |
| Project documentation | Concept, Week 4 design, README, contributing guide, test plan | Partial | Installation, confirmed integrations, final decisions, test results, and submission-ready slide deck |
| Three-minute YouTube video | No link included | Missing; previously recorded as not started | Record demonstration, verify duration/accessibility, and add YouTube link |

## Technical progress and evidence

| Item | Owner | Repository status | Evidence needed to mark complete |
|---|---|---|---|
| AI agents assembled in VS Code | Ghazal | Reported complete — evidence missing | Agent source code and runnable example |
| Dashboard interface | Ghazal | Reported complete — evidence missing | Dashboard source and demonstration |
| Agents connected to dashboard | Ghazal | Reported complete — evidence missing | Integration code and end-to-end run |
| Initial system test without dataset | Ghazal | Reported complete — evidence missing | Dated command, environment, output, and result |
| VS Code project added to GitHub | Ghazal | Missing; `src/` contains only a README | Upload existing project, excluding credentials |
| Installation instructions | Ghazal | Missing; root README has a placeholder | Runtime version, dependencies, environment variables, and launch commands |
| IBM Bob use | Ghazal; Nyasha documents evidence | Missing | Description of actual use and suitable screenshots, logs, or demonstration references |
| Synthetic dataset | Shared | Included — 12 cases, schema documentation, provenance, and expected outcomes | Team review and prototype input adapter |
| Dataset-based testing | Shared | Fixture consistency validator passed; dashboard execution evidence missing | Run the prototype against cases; save actual outputs and comparisons in `data/results/` |
| Acceptance-criteria validation | Shared | Criteria drafted; results missing | Detection/false-positive metrics, priority rationale, escalation evidence, handoff completeness, and approval/verification checks |
| Submission slides | Nyasha / shared | Missing from repository | Completed deck or accessible link mapped to required guide sections |
| Video | Nyasha / shared | Missing | Three-minute YouTube link |

`data/samples/` now contains the v1 fixture and guide. No actual dashboard outputs have been committed to `data/results/`. A folder name or README does not establish that implementation, data, or testing is complete.

## Completion checklist

- [x] Establish repository and include project/design drafts.
- [x] Include contribution instructions, data rules, configuration template, and test plan.
- [ ] Ghazal: upload agents, orchestration, dashboard, and dependency files.
- [ ] Ghazal: replace installation placeholder with verified setup and launch instructions.
- [ ] Confirm IBM Bob access and document its actual use.
- [ ] Confirm which watsonx services and IBM Cloud resources are available and adopted.
- [ ] Choose the public-service scenario, baseline, and prioritization rubric.
- [x] Upload documented synthetic data and evaluator-only expected outcomes (v1; consistency check passed).
- [ ] Review v1 scenario, baseline/scoring/policy and adapt it to the prototype.
- [ ] Define allowed actions, human-approval conditions, retry limits, escalation triggers, and human closure authority.
- [ ] Assign remaining security-rule, dataset, QA, slide, and video tasks.
- [ ] Run dataset-based tests and record results against acceptance criteria.
- [ ] Include example verified resolution and complete unresolved-case handoff.
- [ ] Review the actual IBM guide and finish the required submission slides.
- [ ] Add the three-minute YouTube video link.
- [ ] Confirm deadline, submission location, and that all linked artifacts are accessible.

## Documentation conventions

Use **Ghazal** consistently. The maintained design uses five modules: Orchestrator, Security Investigator, Risk & Dependency Analyst, Response Agent, and Verification & Handoff. Policy gates apply across them; the dashboard and case store are supporting components.

IBM watsonx Orchestrate is optional, watsonx.ai / Granite and IBM Cloud are candidates, and adoption/access remain to be confirmed. IBM Bob is required according to the team's documented brief; evidence of use remains outstanding.

The Markdown documents are maintained for current use. Word files in `original/` are historical source copies and may contain earlier names or designs. Update this checklist when new evidence is committed; do not mark reported work as verified solely from a progress statement.
