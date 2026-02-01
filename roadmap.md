# Roadmap

## Philosophy

**Ship fast. Learn faster. Cut timeline in half, then half again.**

This roadmap is **aggressive**—designed for speed, not comfort. MVP in 1 month.

**For detailed technical breakdown, see [ROADMAP_DETAILED.md](./ROADMAP_DETAILED.md)**

---

## The Vision

**One AI-first platform that replaces 10+ tools. YC-quality co-founder built in.**

| Problem | Solution |
|---------|----------|
| 10+ tools don't talk | One unified platform |
| AI bolted onto old software | AI-first architecture |
| 90% of startups fail | Honest, aligned guidance |
| Guidance is gatekept | Accessible to all |

Where you're born and who you know should not determine if your business succeeds.

---

## Core Principles

| Principle | What It Means |
|-----------|---------------|
| **Speed** | If timeline is long, it's wrong. Ship. |
| **AI-First** | Not AI added. Built for intelligence. |
| **Honest** | Truth over comfort. Challenge bad ideas. |
| **Founder-Aligned** | Right business for THIS founder |
| **Validate First** | 5 users > 500 features |

---

## Version Strategy: 1 Month to MVP

### MVP Sprint (4 Weeks)

**Goal:** Launchable product with 5+ real users

| Week | Version | Focus | Deliverable |
|------|---------|-------|-------------|
| **1** | v0.1 | Foundation + Memory | CLI chat that remembers |
| **2** | v0.2 | Personality | Opinionated mentor with first principles |
| **3** | v0.3 | Intelligence | Auto-extract business context + first-session value |
| **4** | v0.4 (MVP) | Polish + Launch | User testing, bug fixes, SHIP IT |

### Post-MVP Phases

| Phase | Versions | Focus | Timeline |
|-------|----------|-------|----------|
| **Foundation** | v0.5-v0.6 | Database + Vector DB | 3 weeks |
| **Optimization** | v0.7 | Cost efficiency | 1 week |
| **Intelligence** | v0.8-v0.9 | Multi-agent + Stages | 3 weeks |
| **Experience** | v0.10-v0.11 | GUI + Mentors | 3 weeks |
| **Complete** | v1.0 | Integration + Polish | 2 weeks |

**Total to v1.0: ~4 months** (not 1 year)

---

## Week 1: Foundation + Memory (v0.1)

**Ship by:** End of Week 1

**Scope:**
- CLI that accepts user input
- Sends to OpenAI-compatible API
- Displays response
- Saves conversation to JSON
- Loads history on startup
- Commands: `/clear`, `/history`

**Deliverables:**
- `src/cli.js` — Input/output + commands
- `src/api.js` — LLM API wrapper
- `src/memory.js` — JSON persistence
- Working prototype you can demo

**Success Criteria:**
- ✅ User types → AI responds
- ✅ Close and reopen → AI remembers
- ✅ Works with OpenAI and alternatives

**Lines of Code:** ~350

---

## Week 2: Personality (v0.2)

**Ship by:** End of Week 2

**Scope:**
- System prompt with mentor personality
- First-principles thinking embedded
- "Delete before optimize" philosophy
- Challenge weak thinking behavior
- Concise, direct communication style

**Core Principles Encoded:**
1. First Principles — Break to fundamentals
2. Delete First — Remove before optimize
3. Simplify Before Automate — Don't automate complexity
4. Question Assumptions — Challenge "that's how it's done"
5. Idiot Index — Cost vs. value thinking

**Deliverables:**
- `src/prompts/mentor.js` — System prompt
- `src/prompts/principles.js` — Framework
- AI that pushes back on bad ideas

**Success Criteria:**
- ✅ AI has opinion, not neutral
- ✅ Challenges bad ideas
- ✅ Asks "can we delete this?" first

**Lines of Code:** ~150 new

---

## Week 3: Intelligence (v0.3)

**Ship by:** End of Week 3

**Scope:**
- Auto-extract business info from conversation
- Build structured business context
- First-session guided onboarding
- Guarantee value in session 1

**Auto-Extracted Context:**
- Business name, stage, industry
- Current challenges
- Goals and constraints
- Founder background

**First-Session Flow:**
1. Quick assessment (3 questions)
2. Challenge one assumption
3. Deliver one actionable insight
4. Create business snapshot

**Deliverables:**
- `src/context/extractor.js` — Auto-extraction
- `src/onboarding/first-session.js` — Guided flow
- `data/business.json` — Structured context

**Success Criteria:**
- ✅ AI knows business without asking 20 questions
- ✅ First session delivers tangible value
- ✅ User wants to come back

**Lines of Code:** ~300 new

---

## Week 4: MVP Launch (v0.4)

**Ship by:** End of Week 4

**Scope:**
- Bug fixes from user testing
- Polish rough edges
- README and setup docs
- Find 5 real users
- LAUNCH

**Activities:**
- Days 1-2: Internal testing, bug fixes
- Days 3-4: 5 user beta tests
- Days 5-6: Iterate on feedback
- Day 7: Public MVP launch

**Validation Criteria:**
- ✅ 5 users complete first session
- ✅ At least 1 user returns for session 2
- ✅ Zero critical bugs

**MVP Definition:**
> A CLI tool where entrepreneurs get opinionated, context-aware guidance from an AI co-founder that remembers everything and challenges weak thinking.

---

## Post-MVP: Version Reference

### Core Versions

| Version | Focus | Post-MVP Week |
|---------|-------|---------------|
| **v0.5** | PostgreSQL + User accounts | Week 5-6 |
| **v0.6** | Vector DB + Semantic memory | Week 7 |
| **v0.7** | Cost optimization + Token tracking | Week 8 |
| **v0.8** | Multi-agent orchestration | Week 9-10 |
| **v0.9** | Business stages + Quality gates | Week 11 |
| **v0.10** | Desktop GUI | Week 12-13 |
| **v0.11** | Multiple mentor personalities | Week 14 |
| **v1.0** | Complete integrated product | Week 15-16 |

### Key Sub-Versions (Post-MVP)

| Version | Focus | Priority |
|---------|-------|----------|
| **v0.5.1** | Privacy + Encryption | P0 |
| **v0.5.2** | Kimi Agent SDK Integration | P0 |
| **v0.6.1** | Hierarchical Memory (token reduction) | P0 |
| **v0.7.1** | Progressive Loading | P1 |
| **v0.8.1** | Agent Abstraction | P1 |
| **v0.8.2** | Research Agent | P1 |
| **v0.8.3** | Kimi Code (default) + Claude Code (alt) | P1 |
| **v0.8.4** | Scheduled Automation | P1 |
| **v0.8.5** | Agents Management (confidence 8.5+) | P1 |
| **v0.9.1** | Skills/SOPs | P2 |
| **v0.13** | Mobile App (Pro+ only) | Post-v1.0 |

### Coding Agent Strategy

**Default:** Kimi Code (Parallel Agents)  
**Alternative:** Claude Code

| Factor | Kimi Code | Claude Code |
|--------|-----------|-------------|
| **Cost** | ~10x cheaper | Premium |
| **Parallel Agents** | Up to 100 | Sequential |
| **Speed (Complex)** | 4.5x faster | Baseline |

```bash
bos refactor src/ --agent=kimi   # Default
bos refactor src/ --agent=claude # Alternative
```

See [coding-agents.md](./ideation/tech-stack/coding-agents.md) for details.

---

## Timeline Summary

```
MONTH 1: MVP
├── Week 1: v0.1 (Foundation + Memory)
├── Week 2: v0.2 (Personality)
├── Week 3: v0.3 (Intelligence)
└── Week 4: v0.4 (MVP LAUNCH) ← YOU ARE HERE

MONTHS 2-4: v1.0
├── Weeks 5-7: v0.5-v0.6 (Database + Vector)
├── Week 8: v0.7 (Cost Optimization)
├── Weeks 9-11: v0.8-v0.9 (Agents + Stages)
├── Weeks 12-14: v0.10-v0.11 (GUI + Mentors)
└── Weeks 15-16: v1.0 (Complete)
```

**Total: 4 months to v1.0** (was 1 year)

---

## Dependency Graph

```
Week 1      Week 2      Week 3      Week 4
v0.1    →   v0.2    →   v0.3    →   v0.4 (MVP)
                                        ↓
                                   [VALIDATE]
                                        ↓
         v0.5 → v0.6 → v0.7 → v0.8 → v0.9 → v0.10 → v0.11 → v1.0
```

---

## Decision Points

| After | Decision |
|-------|----------|
| **v0.4 (MVP)** | Continue, pivot, or kill? |
| v0.6 | Which agents matter most? |
| v0.9 | GUI priority vs. features? |
| v1.0 | Growth strategy, funding? |

---

## Key Principles

1. **Ship in 1 month** — No excuses
2. **5 users > 500 features** — Validate with real people
3. **Cut scope ruthlessly** — Delete before adding
4. **Speed is a feature** — Slow = death
5. **Build → Measure → Learn** — Don't guess, test

---

## Current Status

**Week:** 1 of 4  
**Target:** v0.4 (MVP) in 4 weeks

| Milestone | Status |
|-----------|--------|
| v0.1 (Foundation + Memory) | 🔄 In Progress |
| v0.2 (Personality) | ⏳ Week 2 |
| v0.3 (Intelligence) | ⏳ Week 3 |
| v0.4 (MVP Launch) | ⏳ Week 4 |

**Next action:** Finish v0.1 by end of this week.
