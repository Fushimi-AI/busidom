# Busidom Roadmap Summary

> **Strategy:** Open Source CLI → Paid Cloud Web/Mobile

---

## Overview

Busidom is built as **two products sharing one core engine**:

1. **CLI v1.0 (Open Source)** — Full-featured local tool (Week 14)
2. **Web/Mobile v2.0 (Paid SaaS)** — Cloud-based convenience layer (Week 22)

### Core Philosophy: Ambient Computing

Busidom isn't just a chat interface you visit - it's **an AI that lives with you**, proactively anticipating needs:

- **Proactive, Not Reactive** — Tracks commitments, follows up intelligently
- **Background, Not Foreground** — Always-on monitoring (resource-efficient, task-based)
- **Context-Aware, Not Context-Free** — Remembers business stage, goals, past conversations
- **Autonomous, Not Manual** — Dynamic skills generated on-the-fly, workflows execute without hand-holding

**Key Differentiator vs ClawdBot/OpenClaw**: Business-specific intelligence (stage-aware, founder-focused) + proactive accountability vs generic horizontal AI.

---

## Shared Core Engine

Both products share the same TypeScript codebase for:

- ✅ Chat interface
- ✅ LLM integration (OpenAI, Kimi, Anthropic)
- ✅ Mentor personality system
- ✅ Multi-agent framework (Mentor, Research, etc.)
- ✅ Workflow engine (state machine + **dynamic skills**)
- ✅ Automation scheduler (cron jobs + **proactive patterns**)
- ✅ Event-driven triggers (+ **commitment tracking**)
- ✅ Semantic memory & intelligence
- ✅ Context extraction
- ✅ Token optimization
- ✅ **Proactive Accountability System** (commitment tracking + intelligent follow-ups)
- ✅ **Always-On Monitoring Engine** (task-based, resource-efficient)
- ✅ **Dynamic Agent Skills** (runtime skill generation)
- ✅ **Project File Access** (sandboxed to project folder)

**This is the "business logic" — 80% of the codebase.**

---

## Product-Specific Layers

### CLI v1.0 (Weeks 1-14)

**Interface:**
- Terminal/REPL (Node.js readline)
- Command-line arguments
- Colorized output (chalk)

**Storage:**
- SQLite (local file: `~/.busidom/data.db`)
- sqlite-vec or ChromaDB (local vector search)
- JSON files for config

**Deployment:**
- npm global install (`npm install -g business-os`)
- Runs on user's machine
- No cloud dependencies

**Target Users:**
- Developers
- Technical founders
- Privacy-conscious users
- Early adopters

---

### Web/Mobile v2.0 (Weeks 15-22)

**Interface:**
- Next.js 14 web app (React)
- React Native mobile app (iOS + Android)
- REST API

**Storage:**
- PostgreSQL (Supabase)
- pgvector (cloud vector search)
- Real-time sync across devices

**Deployment:**
- Vercel (web frontend)
- Supabase (backend + DB)
- App Store + Google Play (mobile)

**Target Users:**
- Non-technical founders
- Busy entrepreneurs
- Teams
- Mobile-first users

---

## Timeline & Milestones

```
Week 1-2:   Foundation (setup, architecture, CLI basics)
Week 3-4:   MVP Core (chat, personality, memory)
Week 5-6:   Local Storage (SQLite, persistence)
Week 7-8:   Intelligence (vector search, semantic memory)
Week 9-10:  Multi-Agent (agents, orchestration)
Week 11-12: Automation (workflows, cron, events)
Week 13-14: CLI Polish & Launch
            ────────────────────────────────
            🚀 CLI v1.0 LAUNCH (Open Source)
            ────────────────────────────────
Week 15-16: Cloud Infrastructure (PostgreSQL, auth, sync)
Week 17-18: Web Application (Next.js UI)
Week 19-20: Mobile Application (React Native)
Week 21-22: Launch & Growth (Stripe, onboarding, marketing)
            ────────────────────────────────
            🚀 Web/Mobile v2.0 LAUNCH (SaaS)
            ────────────────────────────────
```

---

## Feature Delivery

### CLI v1.0 Features (42 features)

| Phase | Features | What Users Get |
|-------|----------|----------------|
| **0** | 5 | Project setup, architecture, CLI foundation |
| **1** | 5 | Chat with AI, mentor personality, memory |
| **2** | 5 | SQLite storage, conversations, export |
| **3** | 5 | Semantic search, context scoring |
| **4** | 7 | Multi-agent system, specialists, **dynamic skills**, **file access** |
| **5** | 7 | Workflows, automations, cron jobs, **proactive accountability**, **monitoring** |
| **6** | 5 | Polish, docs, v1.0 release |

**Total:** 42 features in 14 weeks (including 7 ambient computing features)

---

### Web/Mobile v2.0 Features (20 features)

| Phase | Features | What Users Get |
|-------|----------|----------------|
| **7** | 5 | Cloud database, auth, multi-device sync |
| **8** | 5 | Web application, UI components |
| **9** | 5 | Mobile apps (iOS + Android) |
| **10** | 5 | Payments, onboarding, launch |

**Total:** 20 features in 8 weeks

**Grand Total:** 62 features in 22 weeks (~5.5 months) + Phase 11 future features

---

## Documentation Structure

```
/roadmap/
├── MASTER_TRACKER_V2.md          ← Main tracking (use this!)
├── PRODUCT_STRATEGY.md            ← Strategy overview
├── ROADMAP_SUMMARY.md            ← This file
├── TEST_PLAN.md                   ← Comprehensive testing
├── DEVELOPMENT_FRAMEWORK.md       ← GitHub integration
│
├── /phase-0-foundation/           (Shared)
├── /phase-1-mvp-core/             (Shared)
├── /phase-4-multi-agent/          (Shared)
├── /phase-4.5-automation/         (Shared)
├── /phase-6-polish/               (Shared)
│
├── /cli-v1/
│   ├── /phase-2-storage/          (SQLite)
│   ├── /phase-3-intelligence/     (Local vector DB)
│   ├── /phase-5-automation/       (CLI scheduler)
│   └── /phase-6-launch/           (CLI docs)
│
└── /web-v2/
    ├── /phase-7-cloud/            (PostgreSQL, auth)
    ├── /phase-8-webapp/           (Next.js)
    ├── /phase-9-mobile/           (React Native)
    └── /phase-10-launch/          (Stripe, onboarding)

└── /phase-11-future/              (AI Employees & Advanced Automation)
    ├── 11.1-browser-automation.md  (AI employee for web tasks)
    ├── 11.2-research-employee.md   (Autonomous research)
    ├── 11.3-skills-marketplace.md  (Community skills)
    ├── 11.4-team-collab.md         (Team features)
    └── 11.5-enterprise.md          (On-prem deployment)
```

---

## Phase 11: Future Features (Post v2.0 Launch)

These features are planned for future releases after v2.0 launches:

| # | Feature | Description | Priority |
|---|---------|-------------|----------|
| 11.1 | Browser Automation Agent | AI employee for web tasks (scraping, form filling, research) | Medium |
| 11.2 | Research Employee Agent | Autonomous deep research and synthesis | Medium |
| 11.3 | Agent Skills Marketplace | Community-contributed agent skills | Low |
| 11.4 | Team Collaboration | Multi-user features, shared context | High |
| 11.5 | Enterprise Tier | On-prem deployment, custom models, SSO | Low |

**Design Philosophy:**
- Browser automation delegated to AI employees, not general tool
- Task-based monitoring (not high-frequency polling)
- Community-driven skills marketplace
- Focus on specialized AI agents vs monolithic tool

---

## Key Decisions Made

### ✅ Ambient Computing (Not Chat-Only)
**Why:** Proactive AI that anticipates needs is the key differentiator vs ClawdBot/OpenClaw/ChatGPT. Commitment tracking + monitoring + autonomous execution = competitive moat.

### ✅ Automation is Core (Not Web-Only)
**Why:** It's a competitive differentiator. CLI users get full workflows + cron jobs locally.

### ✅ SQLite for CLI (Not PostgreSQL)
**Why:** Zero config, portable, fast for local use. PostgreSQL only for cloud sync.

### ✅ Local Vector Search (Not Cloud)
**Why:** Privacy, speed, no API calls. Uses sqlite-vec or ChromaDB embedded.

### ✅ CLI First, Then Web
**Why:** Validate core value faster (14 weeks vs 22). Build community. Then monetize.

### ✅ Shared Core Engine
**Why:** Don't build features twice. CLI and Web use same business logic, different storage/UI.

### ✅ Dynamic Skills (Not Skills Marketplace)
**Why:** Generate skills on-the-fly as needed vs maintaining library. Infinite extensibility without pre-programming every capability.

### ✅ Browser Automation via AI Employees (Future)
**Why:** Delegate to top orchestrator, not general-purpose tool. Safer, more intelligent, aligned with ambient computing vision.

---

## Success Metrics

### CLI v1.0 (Week 14)
- ✅ 500+ GitHub stars
- ✅ 100+ weekly active users
- ✅ 10+ contributors
- ✅ Featured on Hacker News front page

### Web v2.0 (Week 22)
- ✅ 100+ signups (first week)
- ✅ 25+ paying customers
- ✅ $5K MRR
- ✅ 40%+ activation rate

### Month 6
- ✅ 2,000+ CLI users
- ✅ 200+ paying customers
- ✅ $40K MRR

---

## What's Next?

1. **Review** `MASTER_TRACKER_V2.md`
2. **Approve** features by marking `[x]`
3. **Start** with Phase 0 (Foundation)

All PRDs are detailed with:
- Technical specifications
- Code examples
- Task breakdowns
- Acceptance criteria
- Integration points

Ready for AI-assisted development!

