# Busidom Product Strategy

> Two-tier strategy: Open Source CLI → Paid Cloud Web/Mobile

---

## Product Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    CORE ENGINE (Shared)                      │
│  ┌──────────┬──────────┬──────────┬──────────┬──────────┐  │
│  │  Chat    │  Agents  │ Workflows│ Memory   │  Intel   │  │
│  └──────────┴──────────┴──────────┴──────────┴──────────┘  │
└─────────────────────────────────────────────────────────────┘
           │                                    │
           │                                    │
    ┌──────▼──────┐                      ┌─────▼──────┐
    │  CLI v1.0   │                      │  Web/Mobile │
    │ (Open Source)│                      │    v2.0     │
    │             │                      │   (Paid)    │
    ├─────────────┤                      ├─────────────┤
    │ • Terminal  │                      │ • Browser   │
    │ • SQLite    │                      │ • Mobile    │
    │ • Local     │                      │ • Cloud DB  │
    │ • BYOK      │                      │ • Sync      │
    └─────────────┘                      └─────────────┘
```

---

## Feature Comparison

| Feature | CLI v1.0 (Free) | Web/Mobile v2.0 (Paid) |
|---------|-----------------|------------------------|
| **Core** |
| AI Chat | ✅ | ✅ |
| Opinionated Mentor | ✅ | ✅ |
| Multi-Agent System | ✅ | ✅ |
| Context Extraction | ✅ | ✅ |
| Semantic Memory | ✅ (local) | ✅ (cloud) |
| **Automation** |
| Workflows | ✅ (manual trigger) | ✅ (auto-trigger) |
| Cron Jobs | ✅ (local) | ✅ (cloud) |
| Event Triggers | ✅ | ✅ |
| Reminders | ⚠️ (terminal only) | ✅ (push notifications) |
| **Storage** |
| Conversations | ✅ (SQLite) | ✅ (PostgreSQL + sync) |
| Vector DB | ✅ (ChromaDB) | ✅ (pgvector) |
| Multi-Device | ❌ | ✅ |
| **Interface** |
| Terminal/CLI | ✅ | ❌ |
| Web App | ❌ | ✅ |
| Mobile App | ❌ | ✅ |
| **Collaboration** |
| Single User | ✅ | ✅ |
| Team Access | ❌ | ✅ (v2.1) |
| **Other** |
| API Keys | You provide | We manage (credits) |
| Setup | Manual install | Sign up + go |
| Support | Community | Priority |
| Cost | Free | $25-999/mo |

---

## Core Philosophy: Ambient Computing

**Traditional AI**: A tool you visit when you need help
**Busidom**: An AI that lives with you, anticipating needs

### Ambient Computing Principles

1. **Proactive, Not Reactive**
   - Don't wait for users to ask - anticipate needs
   - Track commitments, follow up intelligently
   - Example: "You said you'd talk to 10 customers this week - how's that going?"

2. **Background, Not Foreground**
   - Always-on monitoring (resource-efficient, task-based)
   - Works while you work, not when you remember to check
   - Example: Monitor competitor pricing, alert on changes

3. **Context-Aware, Not Context-Free**
   - Remembers business stage, goals, past conversations
   - Semantic memory across all interactions
   - Example: Different advice for idea stage vs growth stage

4. **Autonomous, Not Manual**
   - Dynamic agent skills generated on-the-fly
   - Workflows execute without hand-holding
   - Example: "Research 20 SaaS competitors" → auto-generates research agent

**Sources:**
- [Ambient Agents: The Next Frontier in Context-Aware AI](https://www.digitalocean.com/community/tutorials/ambient-agents-context-aware-ai)
- [Proactive AI Agents: Anticipating Needs Before You Do](https://www.hey-steve.com/insights/proactive-ai-agents-anticipating-needs-before-you-do)

---

## Value Proposition

### CLI v1.0 (Open Source)
**For:** Technical founders, developers, early adopters
**Value:** Ambient AI co-founder that runs locally, proactively guides your startup
**Unique:** Tracks commitments, monitors progress, generates skills on-demand
**Cost:** Free (BYOK)
**Setup:** 10 minutes (npm install)

### Web/Mobile v2.0 (Paid SaaS)
**For:** Non-technical founders, busy entrepreneurs, teams
**Value:** Same proactive AI + mobile access + team collaboration + managed infrastructure
**Unique:** Push notifications for check-ins, cloud-based always-on monitoring
**Cost:** $25-999/mo (includes API credits)
**Setup:** 30 seconds (sign up)

---

## Go-to-Market

### Phase 1: CLI Launch (Week 12)
```
Target: 1,000 users in 3 months
Channels:
- GitHub (stars, trending)
- Hacker News launch
- Developer communities (Reddit, Discord)
- Twitter/X (build in public)
- Product Hunt

Success Metric: 100+ weekly active users
```

### Phase 2: Web Launch (Week 20)
```
Target: 100 paying customers in 3 months
Channels:
- Upgrade existing CLI users
- Indie Hackers, Startup School
- YouTube (founder content)
- Paid ads (Google, Meta)

Success Metric: $10K MRR
```

---

## Conversion Funnel

```
10,000 CLI users (free)
    ↓ 5% try web
  500 create account
    ↓ 40% activate
  200 complete onboarding
    ↓ 25% convert
   50 paying customers

   = $10K MRR (at $199/mo avg)
```

---

## Monetization Strategy

### CLI (Open Source)
- **Revenue:** $0 (acquisition channel)
- **Cost:** GitHub hosting + support (community)
- **Goal:** Build brand, community, social proof

### Web/Mobile (SaaS)
- **Revenue:** Subscriptions ($25-999/mo)
- **Cost:** Infrastructure + AI credits + support
- **Margin:** 20-30% (after AI costs)
- **Goal:** Sustainable business

---

## Competitive Moat

### vs General AI Assistants (ClawdBot, OpenClaw, ChatGPT)
**Their strength:** Horizontal (works for everyone), viral ("Jarvis IRL!")
**Their weakness:** Generic advice, no domain expertise

**Our advantage:**
- **Vertical Focus:** Startup-specific intelligence (stage-aware, founder personality)
- **Proactive Accountability:** Tracks what you said you'd do, follows up intelligently
- **Business Context:** Remembers your customers, challenges, goals - not just conversations
- **Opinionated Guidance:** Gives tough love and specific playbooks, not neutral responses

### vs Business Tools (Notion AI, custom GPTs, coaches)
**Their strength:** Integration with existing workflows
**Their weakness:** Reactive, no autonomous execution

**Our advantage:**
- **Ambient Computing:** Always-on monitoring, proactive check-ins
- **Autonomous Execution:** Dynamic skill generation, workflow automation
- **Unified Platform:** Chat + workflows + automation + memory in one place

### vs Human Coaches/Advisors
**Their strength:** Deep experience, relationships
**Their weakness:** Expensive ($5K-50K/year), limited availability

**Our advantage:**
- **24/7 Availability:** Never sleeps, instant responses
- **Scalable:** Same quality for 1 user or 10,000
- **Affordable:** $300-1,200/year vs $5K-50K
- **Execution Support:** Not just advice - automates workflows too

**Unique Position:** Only AI co-founder combining vertical startup expertise + ambient computing + open source trust

---

## Technology Stack

### Shared Core (TypeScript)
- LLM: OpenAI/Anthropic/Kimi (pluggable)
- Agent Framework: Custom (tool use + orchestration)
- Workflow Engine: State machine (YAML definitions)
- Scheduler: node-cron
- Event Bus: EventEmitter → Redis (web)

### CLI Specific
- Interface: Node.js readline
- Storage: SQLite (better-sqlite3)
- Vector: ChromaDB or local pgvector
- Package: npm (global install)

### Web/Mobile Specific
- Frontend: Next.js 14 (App Router)
- Mobile: React Native
- Backend: Next.js API routes
- Database: PostgreSQL (Supabase or Railway)
- Vector: pgvector
- Cache: Redis (Upstash)
- Auth: NextAuth.js
- Payments: Stripe
- Hosting: Vercel + Supabase

---

## Development Timeline

### CLI v1.0 (Weeks 1-12)
| Week | Phase | Deliverable |
|------|-------|-------------|
| 1-2 | Foundation | Project setup, architecture |
| 3-4 | MVP Core | Chat + personality + memory |
| 5-6 | Intelligence | Vector search + context |
| 7-8 | Multi-Agent | Agent framework + specialists |
| 9-10 | Automation | Workflows + cron + events |
| 11-12 | Polish | CLI v1.0 launch |

### Web/Mobile v2.0 (Weeks 13-20)
| Week | Phase | Deliverable |
|------|-------|-------------|
| 13-14 | Cloud Infra | PostgreSQL + auth + API |
| 15-16 | Web App | UI + features parity |
| 17-18 | Mobile | React Native app |
| 19-20 | Launch | Marketing + onboarding |

---

## Success Metrics

### CLI v1.0 (Week 12)
- ✅ 500+ GitHub stars
- ✅ 100+ weekly active users
- ✅ 20+ open source contributors
- ✅ Featured on Hacker News

### Web v2.0 (Week 20)
- ✅ 100+ signups in first week
- ✅ 25+ paying customers
- ✅ $5K MRR
- ✅ 40%+ activation rate

### Month 6 (Week 36)
- ✅ 2,000+ CLI users
- ✅ 200+ paying customers
- ✅ $40K MRR
- ✅ Product Hunt #1 product of the day

---

## Risk Mitigation

| Risk | Mitigation |
|------|------------|
| CLI too good, no conversions | Add convenience features to web (mobile, teams, managed keys) |
| Open source fork competition | Core engine stays MIT, cloud infra proprietary |
| High AI costs | Token optimization (50% savings), model routing |
| Low activation | Onboarding workflow, first-session value guarantee |
| Churn | Weekly engagement automations, mentor check-ins |

---

## Long-term Vision (Year 2-3)

**CLI:**
- Community plugins
- Agent marketplace
- Workflow templates library

**Web/Mobile:**
- Team collaboration
- API for integrations
- White-label for accelerators
- Enterprise tier (custom models, on-prem)

