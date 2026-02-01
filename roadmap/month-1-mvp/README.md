# Month 1: MVP Sprint

**Goal:** Ship a working MVP in 4 weeks. Validate the core hypothesis.

---

## The Hypothesis

> "Entrepreneurs using a unified AI-first platform with an opinionated, context-aware co-founder outperform those using generic AI tools."

---

## Weekly Breakdown

| Week | Version | Focus | Deliverable | Lines of Code |
|------|---------|-------|-------------|---------------|
| **1** | v0.1 | Foundation + Memory | CLI that remembers | ~350 |
| **2** | v0.2 | Personality | Opinionated mentor | ~150 |
| **3** | v0.3 | Intelligence | Context extraction + first-session value | ~400 |
| **4** | v0.4 | Launch | Bug fixes, 5 users, SHIP | ~100 |
| | | **Total** | | **~1,000** |

---

## Week 1: Foundation + Memory (v0.1)

**Ship by:** End of Week 1

**What We Build:**
- CLI that accepts user input
- Sends to OpenAI-compatible API
- Displays response
- Saves conversation to JSON
- Loads history on startup
- Commands: `/clear`, `/history`, `/help`

**Success Criteria:**
- ✅ User types → AI responds
- ✅ Close and reopen → AI remembers
- ✅ Works with OpenAI and Kimi K2.5

**[Detailed Week 1 Plan →](./week-1/README.md)**

---

## Week 2: Personality (v0.2)

**Ship by:** End of Week 2

**What We Build:**
- System prompt with mentor personality
- First-principles thinking embedded
- "Delete before optimize" philosophy
- Challenges weak thinking
- Direct, concise responses

**Success Criteria:**
- ✅ AI responds with opinion, not neutrality
- ✅ Challenges bad ideas
- ✅ Asks "can we delete this?" first

**[Detailed Week 2 Plan →](./week-2/README.md)**

---

## Week 3: Intelligence (v0.3)

**Ship by:** End of Week 3

**What We Build:**
- Auto-extract business info from conversation
- Build structured business context
- Guided first-session onboarding
- Deliver actionable insight in 5 minutes
- Create business snapshot

**Success Criteria:**
- ✅ AI knows business without 20 questions
- ✅ First session delivers tangible value
- ✅ User wants to come back

**[Detailed Week 3 Plan →](./week-3/README.md)**

---

## Week 4: MVP Launch (v0.4)

**Ship by:** End of Week 4

**What We Do:**
- Bug fixes from internal testing
- Polish rough edges
- Find 5 real users
- SHIP IT

**Daily Breakdown:**
| Day | Focus |
|-----|-------|
| 1-2 | Internal testing, bug fixes |
| 3-4 | 5 user beta tests |
| 5-6 | Iterate on feedback |
| 7 | **Public launch** |

**Validation Criteria:**
- ✅ 5 users complete first session
- ✅ At least 1 user returns for session 2
- ✅ Zero critical bugs

**[Detailed Week 4 Plan →](./week-4/README.md)**

---

## Tech Stack (MVP)

| Component | Technology | Why |
|-----------|------------|-----|
| Runtime | Node.js 20+ | Fast iteration, rich ecosystem |
| CLI Framework | Commander.js | Industry standard, great docs |
| User Input | Inquirer.js | Interactive prompts |
| LLM API | OpenAI SDK | Works with OpenAI, Azure, compatible APIs |
| Storage | JSON files | No database complexity yet |
| Config | dotenv | Environment variables |

---

## File Structure (End of Month 1)

```
business-os/
├── src/
│   ├── index.js              ← Entry point
│   ├── cli.js                ← CLI setup and commands
│   ├── api.js                ← LLM API wrapper
│   ├── memory.js             ← JSON persistence
│   ├── context/
│   │   └── extractor.js      ← Business context extraction
│   ├── prompts/
│   │   ├── mentor.js         ← System prompt
│   │   └── principles.js     ← First principles framework
│   └── onboarding/
│       └── first-session.js  ← Guided onboarding flow
├── data/
│   ├── context.json          ← Conversation history
│   └── business.json         ← Extracted business context
├── package.json
├── .env.example
└── README.md
```

---

## Risk Mitigation

| Risk | Mitigation |
|------|------------|
| API costs too high | Token counting, caching, prompt optimization |
| Users don't return | First-session value delivery (Week 3) |
| Scope creep | Weekly ship deadline = forced prioritization |
| Technical blockers | Use proven libraries, avoid custom solutions |

---

## Daily Standup Questions

Every day, answer:
1. What did I ship yesterday?
2. What will I ship today?
3. What's blocking me?

---

## End of Month Decision

**At the end of Week 4:**

| Result | Action |
|--------|--------|
| 0 users return | Pivot or kill |
| 1-2 users return | Investigate why, iterate |
| 3+ users return | **Continue to v0.5** |

---

## Quick Links

- [Week 1: Foundation + Memory](./week-1/README.md)
- [Week 2: Personality](./week-2/README.md)
- [Week 3: Intelligence](./week-3/README.md)
- [Week 4: Launch](./week-4/README.md)
- [Back to Roadmap](../README.md)
