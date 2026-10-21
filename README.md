# Public Service Risk Dashboard

**Team Byte into the Future** | IBM SkillsBuild AI Experiential Learning Lab | Track #4: Government & Public Services

A multi-agent AI system that helps government IT and cybersecurity teams detect security misconfigurations, understand how affected systems connect to essential public services, prioritize risks by citizen impact, and hand unresolved work to human responders with a complete, evidence-based case packet.

> **Design principle:** the AI handles permitted, low-risk analysis and documentation. Humans keep authority over critical actions, incident classification, recovery approval, and closure.

---

## The problem

Government security teams face alert overload, fragmented tools, hidden misconfigurations, and incomplete context when work changes hands. Our guiding question:

*How might we use agentic AI to help government agencies proactively identify security misconfigurations, assess vulnerabilities and incidents, understand technical dependencies, prioritize threats to essential public services, and complete authorized response work before handing unresolved tasks to human cybersecurity professionals?*

**Primary users:** government SOC analysts, IT operations staff, incident responders, and security managers.
**Example setting:** a simulated county government running public-facing applications, internal identity services, and emergency-related systems.

## Agent architecture

| Agent / module | Responsibility | Key decision |
|---|---|---|
| Orchestrator | Tracks case state, plans tasks, routes work, preserves audit history | What should happen next? |
| Security Investigator | Validates configuration findings against approved baselines | Is this a confirmed finding? |
| Risk & Dependency Analyst | Maps affected assets to public services and estimates impact | What needs attention first? |
| Response Agent | Proposes or executes only explicitly authorized sandbox actions | Is this action permitted and safe? |
| Verification & Handoff | Independently checks results and prepares the analyst handoff | Resolved, retry safely, or escalate? |

### Data flow

```
Input / Perception      Synthetic alerts, configuration snapshots, asset inventory, service-dependency map
        ↓
Orchestrator / Planning Assigns agents, tracks workflow state, enforces authorization gates
        ↓
Memory / Knowledge      Approved baselines, response procedures, validated prior cases, audit trail
        ↓
Tools / Interfaces      Python validation functions, simulated APIs, SQL records, optional model service
        ↓
Execution               Read-only investigation, prioritization, authorized sandbox actions, handoff creation
        ↓
Verification / Feedback Deterministic tests; results and analyst corrections recorded for future cases
```

## Workflow

1. Receive a simulated alert or configuration finding and create a case record.
2. Validate evidence and compare the configuration with an approved baseline.
3. Assess severity, dependencies, and likely impact on public-service continuity.
4. Choose next action: gather evidence, recommend remediation, perform an authorized sandbox step, or escalate.
5. Check authorization and safety before any action. **Critical findings trigger immediate human notification.**
6. Execute the permitted action and independently verify the result.
7. If verification fails, retry only within bounded rules; otherwise stop and escalate with evidence.
8. Record outcome, analyst feedback, remaining tasks, and case status.

## Technologies

| Tool | Purpose |
|---|---|
| IBM Bob | Required IBM development workflow |
| IBM watsonx Orchestrate | Agent workflow orchestration |
| IBM watsonx.ai / Granite (candidate) | Language reasoning, summarization, planning support |
| IBM Cloud | Hosting and IBM service access |
| Python | Baseline comparisons, simulated actions, validation, scoring |
| Synthetic JSON / CSV | Alerts, configurations, assets, service dependencies |
| SQLite | Case status, event logs, audit trail |
| Dashboard | Risk ranking, evidence, approval requests, handoffs |
| VS Code + GitHub | Development and team collaboration |

## MVP demonstration

Detect a misconfigured government cloud-storage resource in synthetic data, identify the affected public service, prioritize the finding, recommend or simulate an authorized correction, verify the state, and generate a structured human handoff when unresolved.

| Priority | Acceptance check |
|---|---|
| 1. Detect & validate | A known misconfiguration is flagged with evidence and a baseline reference |
| 2. Prioritize by service impact | The dashboard explains why the affected public service changes priority |
| 3. Verify & hand off | A successful sandbox action is verified; a failed or unsafe action produces a complete handoff |

## Development status

| Area | Status |
|---|---|
| Project concept and agent design | ✅ Complete (see `docs/`) |
| AI agents built in VS Code | ✅ Complete (Ghazal) — code being added to `src/` |
| Dashboard interface | ✅ Complete (Ghazal) |
| Agents connected to dashboard | ✅ Complete (Ghazal) |
| Initial system test without dataset | ✅ Complete |
| Synthetic dataset collection and preparation | 🔄 In progress |
| Dataset-based testing and validation | ⏳ Not started |

## Repository structure

```
├── README.md            You are here
├── CONTRIBUTING.md      Team workflow and how to add code safely
├── .gitignore           Keeps keys, credentials, and large files out
├── .env.example         Template for local secrets (copy to .env, never commit .env)
├── docs/
│   ├── project-concept.md      Full integrated project concept
│   ├── week-4-deliverables.md  Architecture, workflow, tools (guide slides 17–19)
│   ├── milestones.md           Deliverables and progress tracker
│   └── original/               Original Word documents
├── src/                 Agent, orchestration, and dashboard code (Ghazal's VS Code project)
├── data/
│   ├── samples/         Small synthetic datasets only
│   ├── results/         Test outputs
│   └── README.md        Data rules and documentation
└── tests/               Test plan and test scripts
```

## Installation

_To be completed once the VS Code project is added to `src/`. Ghazal: please fill in the setup steps, required Python version, how to install dependencies, how to configure `.env`, and how to start the agents and dashboard._

## Data and safety rules

- Synthetic or properly authorized public data only. No real citizen data, personal information, or live government systems.
- No real credentials in the repo. API keys and IBM Cloud credentials live in a local `.env` file, which Git ignores.
- No live production changes. All actions run in a sandbox and are logged.

## Team

| Member | Role |
|---|---|
| Nyasha | Team lead: project coordination, cybersecurity criteria, user problem, documentation |
| Ghazal | Development: AI agents, orchestration, dashboard, prototype integration |

## Documentation

- [Project concept](docs/project-concept.md)
- [Week 4 deliverables: architecture, workflow, tools](docs/week-4-deliverables.md)
- [Milestones and progress](docs/milestones.md)
- [Contributing guide](CONTRIBUTING.md)
