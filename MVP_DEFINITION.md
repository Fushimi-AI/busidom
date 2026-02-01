# MVP Definition: 1 Month Sprint

**Philosophy:** Ship in 1 month. No excuses. Cut timeline in half, then half again.

---

## What We're Proving

**Business-OS is an AI-first operating system** — one platform that replaces Notion, Jira, Slack, and others. With an honest AI co-founder that:
- Challenges weak ideas (no false hope)
- Aligns with founder skills and strategy
- Enforces quality gates before progression

---

## The Hypothesis

**"Entrepreneurs using a unified AI-first platform outperform those juggling fragmented tools with bolted-on AI."**

---

## MVP = 4 Weeks

| Week | Version | Focus | Ship By |
|------|---------|-------|---------|
| **1** | v0.1 | Foundation + Memory | End of Week 1 |
| **2** | v0.2 | Personality | End of Week 2 |
| **3** | v0.3 | Intelligence | End of Week 3 |
| **4** | v0.4 | Launch | End of Week 4 |

---

## Week 1: v0.1 — Foundation + Memory

**Ship by:** End of Week 1

**Goal:** CLI chat that remembers conversations

**Scope:**
- CLI accepts user input
- Sends to OpenAI-compatible API
- Displays AI response
- **Save conversation to JSON**
- **Load history on startup**
- **Include history in context**
- Commands: `/clear`, `/history`

**Deliverables:**
- `src/cli.js` — Input/output + commands
- `src/api.js` — LLM wrapper
- `src/memory.js` — JSON persistence
- `data/context.json` — Storage
- `package.json`

**Success Criteria:**
- ✅ User types → AI responds
- ✅ Close app → Reopen → AI remembers
- ✅ Works with OpenAI and alternatives

**Lines of Code:** ~350

---

## Week 2: v0.2 — Personality

**Ship by:** End of Week 2

**Goal:** AI has distinct mentor personality grounded in first principles

**Depends on:** v0.1

**Scope:**
- System prompt with mentor personality
- First-principles thinking embedded
- Delete before optimize philosophy
- Simplify before automate approach
- Challenges weak thinking
- Direct, concise responses

**Core Principles Encoded:**
1. Question assumptions ("Why does it cost this much?")
2. Delete unnecessary before optimizing
3. Simplify before automating
4. Idiot Index awareness (cost vs. value)

**Deliverables:**
- `src/prompts/mentor.js`
- `src/prompts/principles.js`

**Success Criteria:**
- ✅ AI responds with opinion, not neutrality
- ✅ Challenges bad ideas with first principles
- ✅ Asks "can we delete this?" first

**Lines of Code:** ~150

---

## Week 3: v0.3 — Intelligence

**Ship by:** End of Week 3

**Goal:** Auto-extract business context + guarantee first-session value

**Depends on:** v0.2

**Scope:**
- Extract business name, stage, industry from conversation
- Detect challenges and goals
- Guided first-session onboarding
- Deliver actionable insight in first 5 minutes
- Create business snapshot

**First-Session Flow:**
1. Quick assessment (3 smart questions)
2. Challenge one assumption
3. Deliver one actionable insight
4. Create business snapshot

**Deliverables:**
- `src/context/extractor.js`
- `src/onboarding/first-session.js`
- `data/business.json`

**Success Criteria:**
- ✅ AI knows business without 20 questions
- ✅ First session delivers tangible value
- ✅ User wants to come back

**Lines of Code:** ~400

---

## Week 4: v0.4 — MVP Launch

**Ship by:** End of Week 4

**Goal:** Polish, test with real users, SHIP IT

**Depends on:** v0.3

**Daily Breakdown:**

| Day | Focus |
|-----|-------|
| 1-2 | Internal testing, bug fixes |
| 3-4 | 5 user beta tests |
| 5-6 | Iterate on feedback |
| 7 | **PUBLIC LAUNCH** |

**Deliverables:**
- `README.md` — Setup instructions
- Bug fixes from testing
- 5 real users onboarded
- Public announcement

**Validation Criteria:**
- ✅ 5 users complete first session
- ✅ At least 1 user returns for session 2
- ✅ Zero critical bugs
- ✅ Setup takes < 5 minutes

---

## MVP Definition

> A CLI tool where entrepreneurs get opinionated, context-aware guidance from an AI co-founder that remembers everything and challenges weak thinking.

---

## What Makes This Different

| Generic AI (ChatGPT) | Business-OS MVP |
|----------------------|-----------------|
| Neutral, agrees | **Opinionated** — challenges you |
| Forgets everything | **Remembers** — context persists |
| Generic advice | **Contextual** — knows your business |
| Static | **Adaptive** — guides now, autonomous later |

---

## Tech Stack (MVP)

- **Node.js** — Simple, fast iteration
- **OpenAI-compatible API** — Works with GPT-4, Kimi K2.5
- **JSON file** — Context storage (no database yet)
- **CLI** — No UI complexity

---

## Coding Agent Strategy (Post-MVP)

**Default:** Kimi Code (Parallel Agents)  
**Alternative:** Claude Code

### Why Kimi Code as Default

| Factor | Kimi Code | Claude Code |
|--------|-----------|-------------|
| **Cost** | ~10x cheaper | Premium |
| **Parallel Agents** | Up to 100 | Sequential |
| **Speed (Complex Tasks)** | 4.5x faster | Baseline |
| **Node.js SDK** | Native | CLI wrapper |

### Integration Timeline

| Version | Milestone |
|---------|-----------|
| v0.5 | Add Kimi Agent SDK |
| v0.8 | Full Kimi Code integration |
| v0.8.1 | Claude Code alternative |

### CLI Flag

```bash
bos refactor src/ --agent=kimi   # Default
bos refactor src/ --agent=claude # Alternative
```

See [coding-agents.md](./ideation/tech-stack/coding-agents.md) for full strategy.

---

## What's NOT in MVP

| Feature | Version | Week |
|---------|---------|------|
| User accounts + Subscriptions | v0.5 | 5-6 |
| PostgreSQL | v0.5 | 5-6 |
| Vector database | v0.6 | 7 |
| Cost optimization | v0.7 | 8 |
| Multi-agent orchestration | v0.8 | 9-10 |
| Stage tracking + Quality gates | v0.9 | 11 |
| GUI | v0.10 | 12-13 |
| Multiple mentors | v0.11 | 14 |

**Rule:** If it's not chat, memory, personality, or context extraction — it waits until after MVP.

---

## Success Metric

**One question:** Did someone use it twice?

One person voluntarily returns = hypothesis validated.

---

## Decision Point (End of Week 4)

**Continue, pivot, or kill?**

| Result | Action |
|--------|--------|
| 0 users return | Pivot or kill |
| 1-2 users return | Investigate why, iterate |
| 3+ users return | **Continue to v0.5** |

---

## After MVP Validation (Months 2-4)

| Week | Version | Focus |
|------|---------|-------|
| 5-6 | v0.5 | PostgreSQL + User accounts |
| 7 | v0.6 | Vector DB + Semantic memory |
| 8 | v0.7 | Cost optimization |
| 9-10 | v0.8 | Multi-agent orchestration |
| 11 | v0.9 | Business stages + Quality gates |
| 12-13 | v0.10 | Desktop GUI |
| 14 | v0.11 | Multiple mentors |
| 15-16 | **v1.0** | **Complete product** |

**Total: v1.0 in 4 months** (not 1 year)

---

## Version Dependencies

```
Week 1      Week 2      Week 3      Week 4
v0.1    →   v0.2    →   v0.3    →   v0.4 (MVP)
                                        ↓
                                   [VALIDATE]
                                        ↓
         v0.5 → v0.6 → v0.7 → v0.8 → v0.9 → v0.10 → v0.11 → v1.0
```

---

## Current Status

| Week | Version | Status |
|------|---------|--------|
| 1 | v0.1 (Foundation + Memory) | 🔄 In Progress |
| 2 | v0.2 (Personality) | ⏳ Upcoming |
| 3 | v0.3 (Intelligence) | ⏳ Upcoming |
| 4 | v0.4 (MVP Launch) | ⏳ Upcoming |

**Next action:** Ship v0.1 by end of this week.

---

See [ROADMAP_DETAILED.md](./ROADMAP_DETAILED.md) for full breakdown.
