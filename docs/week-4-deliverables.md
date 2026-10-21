IBM SkillsBuild AI Experiential Learning Lab • Byte into the Future

Project: Public Service Risk Dashboard \| Track: Government & Public Services

Team Lead: Nyasha \| Status: Proposed design for team review

Purpose: Document the proposed agent architecture, operating workflow, and tools/integrations for IBM Solution Design Guide slides 17–19 (recommended completion during Weeks 4–5). This is a design proposal, not a claim that the prototype is already implemented.

# 1. AI Agent Architecture \| Guide slide 17

## Agent overview

The Public Service Risk Dashboard is a multi-agent AI system intended to help government cybersecurity teams identify security misconfigurations, validate findings, assess dependencies and impact on essential public services, prioritize risks, and coordinate authorized responses with human oversight.

| Agent / module            | Responsibility                                                                      | Key decision                         |
|---------------------------|-------------------------------------------------------------------------------------|--------------------------------------|
| Orchestrator              | Tracks case state, plans tasks, routes work and preserves audit history.            | What should happen next?             |
| Security Investigator     | Validates configuration findings against baselines and examines simulated evidence. | Is this a confirmed finding?         |
| Risk & Dependency Analyst | Maps affected assets to public services and estimates operational impact.           | What needs attention first?          |
| Response Agent            | Proposes or executes only explicitly authorized actions in the POC sandbox.         | Is action permitted and safe?        |
| Verification & Handoff    | Runs independent checks, records outcomes, prepares analyst handoff.                | Resolved, retry safely, or escalate? |

Policy and human-approval gates apply across all five modules. The dashboard and case store support the workflow. Verification & Handoff independently checks the Response Agent's results.

## Component architecture and data flow

↓ INPUT / PERCEPTION: Synthetic alerts, configuration snapshots, asset inventory, service-dependency map

↓ ORCHESTRATOR / PLANNING: Assigns specialized agents, tracks workflow state, enforces authorization gates

↓ MEMORY / KNOWLEDGE: Approved security baselines, response procedures, validated prior cases, audit trail

↓ TOOLS / INTERFACES: Python validation functions, simulated APIs, SQL records, optional model service

↓ EXECUTION: Read-only investigation, prioritization, authorized sandbox actions, ticket/handoff creation

↓ VERIFICATION / FEEDBACK: Deterministic tests; record results and analyst corrections for future retrieval

Design rationale: Separate investigation, risk assessment, action, and verification so each stage can be tested and audited. The language model may help interpret evidence and plan tasks; deterministic controls determine permissions and verify outcomes.

# 2. AI Agent Workflow \| Guide slide 18

## Step-by-step workflow

1\. Receive simulated alert or configuration finding and create a case record.

2\. Validate evidence and compare the configuration with an approved baseline.

3\. Assess severity, dependencies, and likely impact on public-service continuity.

4\. Choose next action: gather evidence, recommend remediation, perform an authorized sandbox step, or escalate.

5\. Check authorization and safety before any action; critical findings trigger immediate human notification.

6\. Execute permitted action and independently verify resulting state.

7\. If verification fails, retry only within bounded rules; otherwise stop and escalate with evidence.

8\. Record outcome, analyst feedback, remaining tasks, and case status for future retrieval.

## Decision points and failure strategy

| Decision / failure                   | Expected handling                                                               |
|--------------------------------------|---------------------------------------------------------------------------------|
| Insufficient or conflicting evidence | Request additional data; mark uncertainty; do not assert resolution.            |
| High-impact or unauthorized action   | Do not execute; request explicit human approval or hand off.                    |
| Confirmed critical incident          | Notify human immediately; continue only safe, authorized support.               |
| Tool failure or failed verification  | Log error, use limited retry if safe, then escalate.                            |
| Successful verification              | Store evidence, outcome, and approved procedure; close only per defined policy. |

## Feedback and learning loop

Observe → Plan → Act → Verify → Record validated outcome → Retrieve relevant experience in later cases. This is a feedback-driven agentic workflow with memory, not by itself reinforcement learning. Optional future reinforcement learning would train a policy against reward signals in a controlled simulation, with separate testing and approval before operational use.

# 3. Tools & Integrations \| Guide slide 19

| Tool / data source                   | Purpose                                                       | Integration / control                       |
|--------------------------------------|---------------------------------------------------------------|---------------------------------------------|
| IBM Bob                              | Required IBM development workflow for the project.            | Development tool; confirm team access.      |
| IBM watsonx.ai / Granite (candidate) | Language reasoning, summarization, planning support.          | Model/API; outputs subject to checks.       |
| IBM watsonx Orchestrate (optional)   | Potential workflow orchestration.                             | Use only if available and useful.           |
| IBM Cloud (candidate) | Potential hosting and IBM service access. | Availability and adoption to be confirmed. |
| Python                               | Baseline comparisons, simulated actions, validation, scoring. | Local sandbox functions with permissions.   |
| Synthetic JSON / CSV                 | Alerts, configurations, assets, service dependencies.         | Local data ingestion; no real citizen data. |
| SQLite                               | Case status, event logs, audit trail, validated resolutions.  | Parameterized SQL and controlled writes.    |
| Document retrieval / RAG (optional)  | Approved runbooks and validated previous incidents.           | Read-only retrieval with source tracking.   |
| Dashboard / case view                | Present risk ranking, evidence, approval requests, handoffs.  | Human-facing interface.                     |

## Constraints and safeguards

Use synthetic or properly authorized public data. No access to live government networks. Enforce least privilege, approval gates, bounded retries, independent verification, data provenance, and auditable decisions. Treat model confidence as a signal requiring validation, not proof of correctness. Tool selection and IBM service availability remain to be confirmed.

# 4. MVP Boundary and Validation Plan

Proposed single demonstration: detect a misconfigured government cloud-storage resource in synthetic data; identify the affected service dependency; prioritize the finding; recommend or simulate an authorized correction; verify the state; and generate a structured human handoff when unresolved.

| MVP priority                     | Acceptance check                                                                       |
|----------------------------------|----------------------------------------------------------------------------------------|
| 1\. Detect & validate            | A known misconfiguration is flagged with evidence and baseline reference.              |
| 2\. Prioritize by service impact | Dashboard explains why the affected public service changes priority.                   |
| 3\. Verify & hand off            | Successful sandbox action is verified; failed/unsafe action produces complete handoff. |

Out of scope for Week 4: live remediation, production deployment, autonomous model retraining, and a trained reinforcement-learning policy. These can be considered later only after simulation, testing, and governance review.

# 5. Open Decisions for the Team

□ Confirm access to IBM Bob and any watsonx services.

□ Choose the synthetic configuration dataset and one public-service dependency scenario.

□ Assign ownership for orchestration, security rules, UI, tests, and documentation.

□ Set explicit human-approval conditions and verification criteria.

□ Review the design with the team and update slides 17–19 before weekly submission.

# Source alignment

IBM SkillsBuild AI Experiential Learning Lab, Solution Design Guide for Participants, slides 17–19 (AI Agent Architecture, AI Agent Workflow, Tools & Integrations), plus slide 22 (MVP scope). Professor Liang Li, Architecture of Intelligence, Part VII (Autonomous Agency), used as conceptual inspiration for agent roles and the plan–execute–evaluate–reflect loop. The project-specific choices in this document are proposed by the team for validation.

Current repository evidence and remaining deliverables are tracked in [Milestones and progress](milestones.md). Historical Word copies in `original/` may reflect earlier designs; the Markdown documentation is maintained for current use.
