Integrated Project Concept, Security Configuration Assessment, Agentic AI Workflow & Human Incident-Response Handoff

Byte into the Future \| IBM SkillsBuild AI Experiential Learning Lab \| Working concept • October 2026

Purpose: consolidate the full proposed solution into one document for team discussion, design decisions, and proof-of-concept planning. This is a proposed design, not an implemented or validated system.

# 1. Executive overview

The Public Service Risk Dashboard is a proposed agentic AI-assisted platform for government IT and cybersecurity teams. It would detect potential security misconfigurations and suspicious activity, compare configuration states with approved baselines, analyze dependencies between technical assets and essential public services, and prioritize findings according to risk and citizen impact. It would complete permitted, low-risk tasks autonomously, verify results, and transfer unresolved work to qualified personnel through a structured, evidence-based handoff. Human responders retain authority over critical actions, incident classification, recovery approval, and closure.

# 2. Alignment with IBM Track \#4

Track \#4 asks how agentic AI can help governments deliver more efficient, transparent, citizen-centric public services. The proposed dashboard supports this by aiming to reduce analyst workload, improve visibility into threats to service continuity, make prioritization explainable, and preserve human accountability. The IBM guide requires IBM Bob in the prototype; it recommends watsonx.ai and watsonx Orchestrate, allows open-source technologies, requires teams to provide compliant datasets, and calls for documentation and a three-minute YouTube video.

# 3. Problem statement and intended users

Proposed problem statement: How might we use Agentic AI to help government agencies proactively identify security misconfigurations, assess vulnerabilities and incidents, understand technical dependencies, prioritize threats to essential public services, and complete authorized response work before handing unresolved tasks to human cybersecurity professionals?

- Primary users to validate: government SOC analysts, IT operations personnel, incident responders, and security managers.

- Secondary stakeholders: department leaders, service owners, compliance personnel, and citizens who depend on reliable public services.

- Example setting: a simulated county government operating public-facing applications, internal identity services, and emergency-related systems.

# 4. Empathy map: hypotheses to validate

| Area         | Hypothesized user experience                                                            | Solution opportunity                                                               |
|--------------|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| Think / Feel | Pressure to make accurate decisions quickly with limited resources.                     | Clear, evidence-backed risk recommendations and workload reduction.                |
| See          | Fragmented monitoring tools and inconsistent configuration visibility.                  | Unified view of assets, findings, dependencies, and response progress.             |
| Hear         | Requests for fast restoration, accountability, and auditability.                        | Traceable prioritization and incident-status reporting.                            |
| Say / Do     | Review alerts, compare logs, inspect settings, escalate cases, and write tickets.       | Automate authorized analysis and produce actionable handoffs.                      |
| Pains        | Alert overload, hidden misconfigurations, uncertain ownership, incomplete context.      | Baseline checks, prioritization, documented decisions, continuity across handoffs. |
| Gains        | Reliable services, fewer repetitive tasks, quicker investigation, defensible decisions. | More consistent workflows and improved service-continuity planning.                |

These are design assumptions, not verified interview results. The team should validate them with appropriate user research or mentor feedback.

# 5. Core system capabilities

1.  Configuration assessment: ingest permitted configuration snapshots; compare actual states against documented security baselines; identify deviations and supporting evidence.

2.  Risk and incident detection: ingest simulated alerts and contextual asset information; distinguish configuration findings from suspected or confirmed incidents.

3.  Dependency and service-impact analysis: map technical components to applications and government services; use OSI layers where useful for network diagnosis, without treating OSI as a risk-ranking standard.

4.  Risk prioritization: evaluate exposure, potential exploitability, asset criticality, service impact, confidence, and compensating controls; show why a recommendation was made.

5.  Authorized AI action: execute only allowlisted, reversible, appropriately scoped activities with logging and policy checks; preserve evidence before changing state.

6.  Verification: check whether authorized actions worked and identify residual risk.

7.  Human escalation and continuity: prepare structured handoff instructions and evidence when human authority, expertise, or intervention is required.

8.  Lifecycle tracking: support investigation, response, recovery, review, and closure under human oversight.

# 6. Illustrative configuration risks

| Example                            | Why it matters                                | Proposed assessment                                                                      |
|------------------------------------|-----------------------------------------------|------------------------------------------------------------------------------------------|
| Overly broad firewall rule         | May expose unnecessary network services.      | Compare allowed ports and sources with baseline and approved exceptions.                 |
| MFA disabled on privileged account | Increases account compromise risk.            | Check policy applicability, account role, and exception status.                          |
| Public cloud storage access        | May expose data.                              | Check access settings and authorized publication purpose; avoid ingesting personal data. |
| Missing security patches           | May leave exploitable weaknesses.             | Correlate patch status with asset criticality and maintenance constraints.               |
| Excessive privileges               | Expands potential misuse or lateral movement. | Review role permissions against least-privilege policy.                                  |
| Logging disabled                   | Weakens detection and investigation.          | Check required audit settings and log-delivery health.                                   |

# 7. AI-first workflow and escalation decision

9.  Observe: collect permitted alerts, configuration states, baseline rules, asset inventory, and service dependencies.

10. Classify: identify whether the item is a configuration deviation, vulnerability, anomaly, or suspected incident; attach uncertainty and evidence.

11. Prioritize: calculate a transparent preliminary risk assessment and evaluate potential public-service disruption.

12. Act within boundaries: perform only preapproved diagnostics or low-risk remediation when policy, permissions, and confidence permit.

13. Verify and document: record actions, timestamps, results, evidence references, and any remaining work.

14. Escalate without delay when required: trigger human notification for high-severity events, ambiguous findings, possible data exposure, missing permissions, failed actions, or unsafe uncertainty.

15. Hand off: provide a concise situation summary, completed tasks, open questions, remaining steps, suggested owners, and any decision approvals needed.

16. Continue support: AI may gather additional approved evidence, update case status, and assist with documentation while humans direct the response.

17. Close only after human validation: ensure recovery checks, required reporting, lessons learned, and authorized case closure.

Critical guardrail: a severe incident must be escalated immediately; the AI may continue approved support in parallel but must not delay notification while trying to finish its own tasks. A misconfiguration does not automatically constitute an incident: non-incident findings can follow vulnerability or change management.

# 8. Human handoff package: required fields

| Field                | Contents                                                                                                         |
|----------------------|------------------------------------------------------------------------------------------------------------------|
| Case identity        | Incident/finding ID, timestamps, detection source, current owner, urgency.                                       |
| Situation and impact | Affected assets, relevant services, risk basis, incident status, confidence and uncertainty.                     |
| Evidence             | Configuration differences, event references, logs or hashes where permitted, provenance and preservation status. |
| Completed AI work    | Commands or tools used, policy authorizations, action outcomes, verification and rollback details.               |
| Outstanding work     | Specific uncompleted tasks, prerequisites, ordered human instructions and safety cautions.                       |
| Decision points      | Actions requiring authorization, potential reporting obligations, escalation contacts.                           |
| Lifecycle status     | Current response stage, assigned responder, next checkpoint, recovery and closure criteria.                      |

# 9. Human-led incident response lifecycle

The project can map the response process to NIST Cybersecurity Framework 2.0 functions and contemporary incident-response practices. Preparation and governance are continuous, not a one-time stage. The operational case should cover detection/analysis, response activities such as containment and eradication, recovery, and post-incident review. The exact agency playbook governs implementation.

| Stage            | AI contribution                                                            | Human responsibility                                           |
|------------------|----------------------------------------------------------------------------|----------------------------------------------------------------|
| Prepare / Govern | Baseline checks, readiness reports, evidence templates.                    | Approve policies, scope, authorities, response plans.          |
| Detect / Analyze | Correlate observations, triage, enrich findings.                           | Confirm incident status and impact where required.             |
| Respond          | Suggest containment, collect approved evidence, execute allowlisted tasks. | Authorize and execute high-impact containment and eradication. |
| Recover          | Track restoration checks, monitor residual findings.                       | Approve restoration and validate service integrity.            |
| Review / Close   | Draft timeline, summarize lessons, retain case record.                     | Complete reporting, approve improvements and formal closure.   |

# 10. Proposed multi-agent architecture

| Agent / module | Responsibility | Key decision |
|---|---|---|
| Orchestrator | Tracks case state, plans tasks, routes work, preserves audit history | What should happen next? |
| Security Investigator | Validates configuration findings against approved baselines | Is this a confirmed finding? |
| Risk & Dependency Analyst | Maps affected assets to public services and estimates impact | What needs attention first? |
| Response Agent | Proposes or executes only explicitly authorized sandbox actions | Is this action permitted and safe? |
| Verification & Handoff | Independently checks results and prepares the analyst handoff | Resolved, retry safely, or escalate? |

Policy and human-approval gates apply across all five modules. The dashboard and case store support the workflow; they are not additional agents. Intake and configuration assessment belong to the Security Investigator; dependency analysis and prioritization belong to the Risk & Dependency Analyst. Verification & Handoff independently checks the Response Agent's results.

IBM archetype alignment: Cognitive Load Reducer (analysis and prioritization); Decision Gatekeeper (whether an action may proceed); Invisible Coordinator (multi-step coordination); Human–AI Boundary Manager (when to stop or escalate). These are proposed selections from the IBM guide.

# 11. Example end-to-end scenario (simulated)

A county cloud storage container is unexpectedly publicly readable. The AI reads a synthetic configuration record, compares it with an approved baseline, links the storage resource to a public-service application, and records the mismatch. It runs permitted non-destructive checks and documents the result. Because potential sensitive-data exposure requires human judgment and may have reporting implications, it immediately escalates. The handoff lists what was checked, what remains unknown, how to preserve evidence, and recommended human steps: verify data classification, review access history, approve access changes, determine incident status, and complete response and recovery if warranted. The AI tracks progress; a human signs off on closure.

# 12. Proof-of-concept scope

- Use synthetic government asset inventory, configuration snapshots, approved baselines, dependency mappings, and incident records.

- Demonstrate one lower-risk misconfiguration that AI can analyze and fully document using approved simulated actions.

- Demonstrate one high-impact scenario that triggers immediate human escalation with a complete handoff packet.

- Show a dashboard with severity, affected public services, rationale, AI work completed, remaining human tasks, and lifecycle status.

- Use IBM Bob as a mandatory development component; evaluate whether watsonx.ai or watsonx Orchestrate is available and useful before committing to them.

- Avoid live production changes, real government credentials, personal information, or sensitive operational data.

# 13. Cloud and technical setup decisions

18. Verify IBM Bob access for each active team member and document how it will be used.

19. Confirm IBM Cloud account, service entitlements, quotas, region, cost limits, and project permissions.

20. Choose a simple architecture: synthetic JSON/CSV inputs, rule-based baseline comparison, agent orchestration, case store, and dashboard.

21. Establish a Git repository, branch conventions, issue tracking, and secrets-handling rules.

22. Define agent tool permissions, audit logging, sandboxing, and human approval interfaces.

23. Run an end-to-end test with one synthetic record before adding more services.

# 14. Team roles and immediate decisions

| Responsibility                                             | Suggested owner                 | Decision needed                           |
|------------------------------------------------------------|---------------------------------|-------------------------------------------|
| Project coordination, cybersecurity criteria, user problem | Nyasha                          | Confirm scope and deliverables.           |
| Cloud / development environment, prototype integration     | Ghazal              | Development owner; confirm service access. |
| AI logic, dataset preparation, testing                     | Shared initially                | Divide concrete work items.               |
| QA, documentation, presentation support                    | Nyasha / shared | Assign specific QA and presentation tasks.   |

# 15. Validation metrics and acceptance criteria

- Detection quality: percentage of seeded misconfigurations correctly flagged; false-positive rate.

- Priority quality: agreement with a documented human-reviewed reference ranking and clear explanation for each score.

- Escalation quality: all seeded critical scenarios trigger timely human notification.

- Handoff completeness: all mandatory case fields are populated and actionable.

- Safety: no unapproved or destructive changes occur; all actions are auditable.

- Continuity: a human can resume work from the handoff without repeating completed steps unnecessarily.

- Service relevance: each critical finding identifies the potentially affected public service or explicitly states when impact is unknown.

# 16. Open questions for team and coach

24. Which government service and primary user will anchor the demonstration?

25. What security baseline and prioritization rubric will be used?

26. Which actions, if any, should the AI be permitted to perform in the POC?

27. What specific events require immediate human escalation?

28. Which IBM services are accessible, and how will IBM Bob be visibly used?

29. Who approves incident classification, containment, recovery, and closure?

30. How will synthetic data be generated and documented?

31. How will the team demonstrate value within a three-minute video?

# 17. Expected organizational value

If validated, the design could reduce repetitive triage work, reveal misconfigurations earlier, support more consistent risk-based resource allocation, preserve investigation context during handoffs, improve traceability, and help government agencies protect continuity of essential public services. These are hypotheses to test, not demonstrated outcomes.

# 18. Source and design-status notes

Source basis: IBM SkillsBuild, “US Fall 2026 - Industry Challenges AI Experiential Learning Lab with Bob,” pp. 3, 5–8 (provided by the user). The challenge statement, Bob requirement, data restrictions, deliverables, and archetype descriptions derive from that guide. The dashboard architecture, empathy-map hypotheses, OSI dependency application, AI-to-human continuity workflow, role proposals, metrics, and example scenarios are team design proposals developed in this discussion. NIST references are conceptual alignment rather than a verified quotation of an agency-specific incident-response playbook.

Current implementation evidence is tracked in [Milestones and progress](milestones.md). This document describes the proposed design; reported prototype completion is not yet supported by uploaded source code. Historical Word copies in `original/` are retained as source records; use the maintained Markdown documents for current names, architecture, and status.
