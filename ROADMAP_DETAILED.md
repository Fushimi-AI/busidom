# Detailed Roadmap: MVP in 1 Month → v1.0 in 4 Months

## Philosophy

**Ship fast. Learn faster. Cut timeline in half, then half again.**

> "If a timeline is long, it's wrong." — Elon Musk

Each version is designed to:
- Ship within 1 week (MVP phase) or 1-2 weeks (post-MVP)
- Be implementable with < 20% context window
- Document knowledge that carries forward
- Be independently testable

**MVP = 1 Month. v1.0 = 4 Months.** (Not 1 year.)

---

## Timeline Overview

### Month 1: MVP Sprint (4 Weeks)

| Week | Version | Focus | Deliverable |
|------|---------|-------|-------------|
| **1** | v0.1 | Foundation + Memory | CLI chat that remembers |
| **2** | v0.2 | Personality | Opinionated mentor |
| **3** | v0.3 | Intelligence | Context extraction + first-session value |
| **4** | v0.4 (MVP) | Polish + Launch | 5 users, bug fixes, SHIP |

### Months 2-4: Post-MVP to v1.0

| Week | Version | Focus |
|------|---------|-------|
| 5-6 | v0.5 | PostgreSQL + User accounts |
| 7 | v0.6 | Vector DB + Semantic memory |
| 8 | v0.7 | Cost optimization |
| 9-10 | v0.8 | Multi-agent orchestration |
| 11 | v0.9 | Business stages + Quality gates |
| 12-13 | v0.10 | Desktop GUI |
| 14 | v0.11 | Multiple mentors |
| 15-16 | v1.0 | Complete product |

---

## Version Overview

### Core Versions (Compressed)

| Version | Name | Focus | Week |
|---------|------|-------|------|
| **0.1** | Foundation | CLI + Memory | 1 |
| **0.2** | Personality | Mentor + First Principles | 2 |
| **0.3** | Intelligence | Context extraction + First-session | 3 |
| **0.4** | **MVP** | Polish + Launch | 4 |
| 0.5 | Database | User accounts + PostgreSQL | 5-6 |
| 0.6 | Semantic | Vector DB + embeddings | 7 |
| 0.7 | Optimization | Cost tracking + efficiency | 8 |
| 0.8 | Orchestration | Multi-agent foundation | 9-10 |
| 0.9 | Stages | Stage tracking + Quality gates | 11 |
| 0.10 | GUI | Desktop app | 12-13 |
| 0.11 | Mentors | Multiple personalities | 14 |
| **1.0** | **Complete** | Full integrated product | 15-16 |

### Enhancement Sub-Versions (Post-MVP)

| Version | Name | Focus | Priority |
|---------|------|-------|----------|
| 0.5.1 | Privacy | Encryption, export | P0 |
| 0.5.2 | Kimi SDK | Kimi Agent SDK integration | P0 |
| 0.6.1 | Hierarchical Memory | 52% token reduction | P0 |
| 0.7.1 | Progressive Loading | Semantic compression | P1 |
| 0.8.1 | Agent Abstraction | Single-purpose agents | P1 |
| 0.8.2 | Isolated Contexts | Per-agent context windows | P1 |
| 0.8.3 | Parallel + Coding Agents | Kimi Code (default) + Claude Code | P1 |
| 0.8.3.1 | Kimi Swarm | Agent Swarm orchestration | P1 |
| 0.8.4 | Plan Mode | Approve before execute | P1 |
| 0.8.5 | MCP Support | Model Context Protocol | P1 |
| 0.8.6 | Research Agent | Market analysis | P1 |
| 0.8.7 | Scheduled Automation | Cron, proactive agents | P1 |
| 0.8.8 | Agents Management | Confidence 8.5+, meta-agents | P1 |
| 0.9.1 | Skills/SOPs | Reusable procedures | P2 |
| 0.13 | Mobile App | Premium (Pro+ only) | Post-v1.0 |

---

# MONTH 1: MVP SPRINT

---

## Week 1: v0.1 — Foundation + Memory

**Ship by:** End of Week 1

**Goal:** CLI chat that remembers conversations

### Scope (Combined v0.1 + v0.2 from old roadmap)
- CLI that accepts user input
- Sends to OpenAI-compatible API
- Displays response
- **Saves conversation to JSON**
- **Loads history on startup**
- **Include history in API context**
- Commands: `/clear`, `/history`
- Basic error handling

### Deliverables
- `src/cli.js` — Input/output + commands
- `src/api.js` — LLM API wrapper
- `src/memory.js` — JSON persistence
- `data/context.json` — Storage file
- `package.json` — Dependencies
- `.env.example` — API key template

### Tech
- Node.js
- OpenAI API (or compatible)
- readline for CLI
- fs for JSON storage

### Success Criteria
- ✅ User types message → AI responds
- ✅ Close and reopen → AI remembers conversation
- ✅ `/clear` resets memory
- ✅ Works with OpenAI and alternatives

### Knowledge Carries Forward
- API wrapper pattern
- CLI input/output pattern
- Context structure schema
- Memory interface (save/load/clear)

### Estimated Scope
~350 lines of code

---

## Week 2: v0.2 — Personality

**Ship by:** End of Week 2

**Goal:** AI has distinct mentor personality grounded in first principles

**Depends on:** v0.1

### Scope
- System prompt with mentor personality
- First-principles thinking embedded in responses
- "Delete before optimize" philosophy
- Simplification prompts before automation suggestions
- Concise, direct communication style
- Challenge weak thinking behavior

### Core Principles Encoded
1. **First Principles Thinking** — Break problems to fundamentals
2. **Delete First** — Remove unnecessary before optimizing
3. **Simplify Before Automate** — Don't automate complexity
4. **Question Assumptions** — Challenge "that's how it's done"
5. **Idiot Index Awareness** — Cost vs. value thinking

### Deliverables
- `src/prompts/mentor.js` — System prompt with principles
- `src/prompts/principles.js` — First principles framework
- Update API calls to include system prompt

### Tech
- System prompt engineering
- Prompt template structure
- Principles-based response patterns

### Success Criteria
- ✅ AI responds with opinion, not neutrality
- ✅ Challenges bad ideas with first principles
- ✅ Asks "can we delete this?" before "how to improve?"
- ✅ Pushes for simplification before automation

### Knowledge Carries Forward
- Prompt template pattern
- Personality encoding approach
- First principles framework
- How to swap/extend personalities

### Estimated Scope
~150 lines code, ~300 lines prompt

---

## Week 3: v0.3 — Intelligence

**Ship by:** End of Week 3

**Goal:** Auto-extract business context + guarantee first-session value

**Depends on:** v0.2

### Why This Matters
Research shows AI tool users who don't extract value in Day 1 churn. "First week" is too late—must be first session. AND the AI shouldn't ask 20 questions to understand your business.

### Scope (Combined Context Intelligence + First-Session Value)
- Auto-extract business info from conversation
- Build structured business context
- Guided first conversation flow
- Immediate deliverable (business snapshot)
- Quick win: one actionable insight in first 5 minutes

### Auto-Extracted Context
- Business name, stage, industry
- Current challenges
- Goals and constraints
- Founder background
- Key assumptions to challenge

### First-Session Flow
1. Quick assessment (3 smart questions)
2. Challenge one assumption
3. Deliver one actionable insight
4. Create business snapshot

### Deliverables
- `src/context/extractor.js` — Auto-extraction logic
- `src/onboarding/first-session.js` — Guided flow
- `src/templates/business-snapshot.md` — Snapshot template
- `data/business.json` — Structured context storage

### Tech
- JSON schema for business context
- Extraction prompts
- Guided conversation state machine

### Success Criteria
- ✅ AI knows business without asking 20 questions
- ✅ 80%+ users get actionable insight in first 5 minutes
- ✅ Business snapshot generated after first conversation
- ✅ User explicitly confirms value received

### Knowledge Carries Forward
- Context extraction patterns
- Onboarding flow pattern
- Business context schema
- Value delivery metrics

### Estimated Scope
~400 lines code

---

## Week 4: v0.4 — MVP Launch

**Ship by:** End of Week 4

**Goal:** Polish, test with real users, and LAUNCH

**Depends on:** v0.3

### This Week's Focus
No new features. Only:
- Bug fixes from internal testing
- Polish rough edges
- Documentation
- Find and onboard 5 real users
- SHIP IT

### Daily Breakdown

| Day | Focus |
|-----|-------|
| 1-2 | Internal testing, bug fixes |
| 3-4 | 5 user beta tests |
| 5-6 | Iterate on user feedback |
| 7 | Public MVP launch |

### Deliverables
- `README.md` — Setup instructions
- Bug fixes from testing
- 5 real users onboarded
- Public announcement

### Validation Criteria
- ✅ 5 users complete first session
- ✅ At least 1 user returns for session 2
- ✅ Zero critical bugs
- ✅ Setup takes < 5 minutes

### MVP Definition
> A CLI tool where entrepreneurs get opinionated, context-aware guidance from an AI co-founder that remembers everything and challenges weak thinking.

### Decision Point
After v0.4: **Continue, pivot, or kill?**

- If 0 users return → Pivot or kill
- If 1-2 users return → Investigate why, iterate
- If 3+ users return → Continue to v0.5

### Knowledge Carries Forward
- What users actually want (vs. what we assumed)
- First real user feedback
- Setup friction points
- Value propositions that resonated

---

# POST-MVP: MONTHS 2-4

---

## v0.4.1 — Context Files (Post-MVP Enhancement)

**Goal:** User-editable context files

**Depends on:** v0.4 (MVP validated)

---

## v0.4 — Context Intelligence

**Goal:** Auto-extract business info from conversation

**Depends on:** v0.3

### Scope
- Extract business name when mentioned
- Detect business type/stage from context
- Track key challenges discussed
- Update context automatically

### Deliverables
- `src/extractor.js` — Info extraction logic
- Update context schema with business fields
- `src/prompts/extraction.js` — Extraction prompt (if using LLM)

### Tech
- Pattern matching OR
- LLM-based extraction (structured output)

### Success Criteria
- User mentions "I'm building a SaaS called X" → context.business_name = "X"
- Context enriches over conversations

### Knowledge Carries Forward
- Context schema (business fields)
- Extraction patterns
- How to extend extractors

### Estimated Scope
~200 lines code, ~50 lines documentation

---

## v0.4.1 — Business Context Files (.bos.md)

**Goal:** User-editable, hierarchical context files for transparency and control

**Depends on:** v0.4

### Why This Matters
Power users want control over what the AI "knows." Editable files build trust and allow deep customization. Inspired by Claude Code's `clode.md` approach.

### Scope
- `.bos.md` in project/business root = business-level context
- Hierarchical inheritance (subfolders inherit parent)
- User can edit directly (transparent, not black-box)
- Auto-read on session start
- Merge with auto-extracted context

### File Structure
```
business/
├── .bos.md              # Business-level context
├── product/
│   └── .bos.md          # Product-specific context (inherits parent)
├── marketing/
│   └── .bos.md          # Marketing context (inherits parent)
└── finance/
    └── .bos.md          # Finance context (inherits parent)
```

### Deliverables
- `src/context/bos-files.js` — File reading/parsing
- `src/context/hierarchy.js` — Inheritance logic
- `docs/bos-file-format.md` — User documentation
- CLI command: `/context edit` — Open context file

### Success Criteria
- User edits `.bos.md` → AI immediately uses updated context
- Hierarchy works correctly
- No conflicts with auto-extraction

### Knowledge Carries Forward
- Hierarchical context pattern
- User-editable config approach
- Transparency philosophy

### Estimated Scope
~250 lines code, ~150 lines documentation

---

## v0.4.2 — Churn Signal Detection

**Goal:** Detect pre-churn signals before users leave

**Depends on:** v0.4.1

### Why This Matters
AI tools face 40% median gross retention. Traditional metrics only reveal churn after it happens. We need leading indicators.

### Scope
- Track prompt complexity over time (declining = pre-churn)
- Monitor AI output editing ratio (high editing = losing trust)
- Session depth tracking (shallow vs. deep)
- 30-day churn prediction model
- Alert system for at-risk users

### Metrics Tracked
| Metric | Pre-Churn Signal |
|--------|------------------|
| Prompt complexity | Declining over time |
| Output editing ratio | > 50% edits |
| Session depth | Increasingly shallow |
| Feature usage | Decreasing |
| Time between sessions | Increasing |

### Deliverables
- `src/metrics/churn-signals.js` — Signal tracking
- `src/metrics/churn-prediction.js` — Prediction model
- `src/alerts/churn-alert.js` — Alert system
- Dashboard data for churn visibility

### Database Addition
```sql
churn_signals (id, user_id, business_id, signal_type, value, recorded_at)
```

### Success Criteria
- Identify at-risk users 30 days before churn
- 70%+ prediction accuracy
- Intervention reduces churn by 20%+

### Knowledge Carries Forward
- Churn signal patterns
- Prediction model approach
- Intervention timing

### Estimated Scope
~300 lines code, ~100 lines documentation

---

## v0.5 — Accounts & Database

**Goal:** User accounts + PostgreSQL + Subscription tiers

**Depends on:** v0.4

### Scope
- User registration/login (email + password)
- PostgreSQL database setup
- Subscription tier management (Starter/Pro/Power)
- Multi-business support per tier limits
- Multi-user support (add stakeholders to businesses)
- Migrate JSON context to database

### Deliverables
- `src/db/schema.sql` — Database schema
- `src/db/client.js` — Database connection
- `src/auth/` — Authentication module
- `src/subscriptions/` — Tier management
- `src/members/` — Multi-user management
- `src/models/` — User, Business, Subscription, Member models
- Migration script from JSON

### Database Schema
```
users (id, email, password_hash, created_at)
subscriptions (id, user_id, tier, business_limit, credits_remaining, status)
businesses (id, owner_id, name, type, stage, created_at)
business_members (id, business_id, user_id, role, onboarded_at)
conversations (id, business_id, messages JSONB, created_at)
context (id, business_id, data JSONB, updated_at)
```

### Subscription Tiers
| Tier | Price | Businesses | Credits (90%) | Value Comparison |
|------|-------|------------|---------------|------------------|
| Free (CLI) | $0 | Unlimited | BYOK | — |
| Starter | $25/mo | 1 | ~$22.50 | < 1 business book |
| Pro | $199/mo | 3 | ~$179 | < 1 hr consultant |
| Founder | $999/mo | 10 | ~$899 | < 1 day fractional exec |

### ROI Perspective
**What you're replacing:**
- Part-time consultant: $2,000-5,000/mo
- Market research tools: $200-500/mo
- Business coach: $500-2,000/mo
- Notion + Jira + Slack: $50-200/mo
- **Total: $2,750-7,700/mo**

**One resource mindset:** If a part-time co-founder costs $5K/mo, Business-OS is a fraction.

### Multi-User Roles
- **owner** — Full control, billing
- **cofounder** — Full access, can invite
- **advisor** — Full access, read-heavy
- **team** — Task-focused access
- **viewer** — Read-only

### Tech
- PostgreSQL
- bcrypt for passwords
- pg or Prisma

### Success Criteria
- User can register/login
- Subscription limits enforced
- Can add team members to business
- Context persists in database

### Knowledge Carries Forward
- Database schema design
- Auth patterns
- Subscription management
- Multi-user patterns

### Estimated Scope
~600 lines code, ~150 lines documentation

### Breaking Change
- Context storage moves from JSON to PostgreSQL
- Requires migration path

---

## v0.5.1 — Pricing Model Validation

**Goal:** A/B test and validate pricing strategy

**Depends on:** v0.5

### Why This Matters
Our 10% margin model may be unsustainable. Credit-based pricing creates customer confusion. Need data to optimize.

### Scope
- A/B test credit-based vs. tiered flat-rate
- Track cost-per-successful-outcome (not just tokens)
- Margin buffer testing (15-20%)
- Usage pattern analysis
- Price sensitivity measurement

### Deliverables
- `src/pricing/ab-test.js` — A/B test framework
- `src/pricing/outcome-tracking.js` — Outcome metrics
- `src/pricing/analysis.js` — Price analysis
- Dashboard for pricing experiments

### Database Addition
```sql
pricing_experiments (id, user_id, variant, conversion, ltv, created_at)
```

### Success Criteria
- Identify optimal pricing model
- Maintain 15%+ margin
- User satisfaction stable

### Knowledge Carries Forward
- Pricing experiment patterns
- Outcome-based metrics
- Margin sustainability

### Estimated Scope
~200 lines code, ~50 lines documentation

---

## v0.5.2 — Privacy & Security Foundation

**Goal:** Build trust through security and data control

**Depends on:** v0.5

### Why This Matters
- 95% of customers won't buy if data isn't protected
- 57% of consumers believe AI threatens privacy
- Business data is sensitive—we must treat it that way

### Scope
- End-to-end encryption for cloud sync
- "Export all my data" feature
- "Delete all my data" feature
- Clear data retention policies
- No training on user data without consent
- SOC 2 compliance roadmap documentation

### Data Principles
1. Your data is yours. Export anytime.
2. Local-first option. Data can stay on device.
3. Encrypted in transit and at rest.
4. No training on your data without explicit consent.
5. Clear path to compliance: SOC 2, GDPR.

### Deliverables
- `src/security/encryption.js` — Encryption layer
- `src/data/export.js` — Full data export
- `src/data/delete.js` — Data deletion
- `docs/privacy-policy.md` — Clear policies
- `docs/security-architecture.md` — Security documentation
- `docs/compliance-roadmap.md` — SOC 2, GDPR path

### Success Criteria
- Users can export all data in JSON/Markdown
- Users can delete all data
- Encryption implemented and verified
- Privacy policy published

### Knowledge Carries Forward
- Encryption patterns
- Data portability approach
- Compliance requirements

### Estimated Scope
~350 lines code, ~300 lines documentation

---

## v0.6 — Semantic Memory

**Goal:** Vector database for intelligent context retrieval

**Depends on:** v0.5

### Scope
- Embed conversation chunks
- Store in vector database
- Semantic search for relevant context
- Smart context window management

### Deliverables
- `src/embeddings/` — Embedding generation
- `src/vector/` — Vector DB client
- Update context retrieval to use semantic search
- `docs/context-architecture.md` — How memory works

### Database Addition
```
embeddings (id, business_id, content, embedding vector, metadata, created_at)
```
Using pgvector extension OR separate Pinecone/Qdrant

### Tech
- OpenAI embeddings API (or local)
- pgvector OR Pinecone
- Chunking strategy

### Success Criteria
- Ask about something from 50 messages ago → AI retrieves relevant context
- Context window stays manageable

### Knowledge Carries Forward
- Embedding pipeline
- Chunking strategy
- Retrieval patterns
- Vector DB interface

### Estimated Scope
~350 lines code, ~150 lines documentation

---

## v0.6.1 — Local-First Mode

**Goal:** Full functionality without cloud dependency

**Depends on:** v0.6

### Why This Matters
- Target audience includes global entrepreneurs (unreliable internet)
- Privacy-conscious users want zero cloud dependency
- CLI users (BYOK) may want local-only operation

### Scope
- SQLite option for local storage
- Offline conversation mode
- Sync when online (optional)
- Local embedding storage
- Optional: local LLM support (Ollama, llama.cpp)

### Deliverables
- `src/db/sqlite.js` — SQLite client
- `src/db/sync.js` — Online sync logic
- `src/offline/mode.js` — Offline mode handling
- `src/embeddings/local.js` — Local embedding storage
- Configuration: local vs. cloud mode

### Tech
- better-sqlite3 or sql.js
- Optional: Ollama integration
- Conflict resolution for sync

### Success Criteria
- Full functionality with no internet
- Seamless sync when back online
- No data loss in offline mode

### Knowledge Carries Forward
- Local-first architecture
- Sync patterns
- Offline-first thinking

### Estimated Scope
~400 lines code, ~100 lines documentation

---

## v0.6.2 — Context Version History

**Goal:** Time machine for business context

**Depends on:** v0.6.1

### Why This Matters
Businesses evolve. Being able to see history of how understanding changed is valuable for reflection and debugging AI behavior.

### Scope
- Track changes to business context over time
- "What did the AI know 3 months ago?"
- Revert to previous context states
- Diff view of context changes
- Optional: Git-based storage for power users

### Deliverables
- `src/context/history.js` — Version tracking
- `src/context/diff.js` — Context diffing
- `src/context/revert.js` — Revert functionality
- CLI commands: `/context history`, `/context revert`
- GUI: Timeline visualization

### Database Addition
```sql
context_history (id, business_id, data JSONB, version, created_at)
```

### Success Criteria
- View context at any point in time
- Understand what changed and when
- Revert without data loss

### Knowledge Carries Forward
- Version control patterns
- Diff/merge approaches
- Time-based data retrieval

### Estimated Scope
~250 lines code, ~75 lines documentation

---

## v0.6.3 — Hierarchical Memory (TiMem-Inspired)

**Goal:** Temporal-hierarchical memory consolidation for 52% token reduction

**Depends on:** v0.6.2

### Why This Matters
Research shows temporal-hierarchical frameworks achieve 75% accuracy with 52% memory reduction. This is critical for long-horizon conversations and cost optimization.

### Memory Hierarchy
```
Level 0: Raw Observations
    ↓ Consolidate daily
Level 1: Episode Summaries (Session-level)
    ↓ Consolidate weekly
Level 2: Semantic Clusters (Topic-based)
    ↓ Consolidate monthly
Level 3: Business Persona (Core identity, values, goals)
```

### Consolidation Rules
| Level | Retention | Trigger | Output |
|-------|-----------|---------|--------|
| L0 → L1 | 24 hours | Daily | Session summary |
| L1 → L2 | 7 days | Weekly | Topic clusters |
| L2 → L3 | 30 days | Monthly | Persona update |

### Scope
- Implement Temporal Memory Tree (TMT)
- Daily/weekly/monthly consolidation jobs
- Smart memory retrieval across levels
- Relevance-based recall
- Token budget awareness

### Deliverables
- `src/memory/hierarchy.js` — Memory tree structure
- `src/memory/consolidation.js` — Consolidation logic
- `src/memory/retrieval.js` — Multi-level retrieval
- `src/jobs/memory-consolidation.js` — Background jobs
- `docs/memory-architecture.md` — Memory system docs

### Database Addition
```sql
memory_tree (id, business_id, level, content, parent_id, created_at, expires_at)
consolidation_log (id, business_id, from_level, to_level, tokens_before, tokens_after, consolidated_at)
```

### Success Criteria
- 50%+ token reduction in context
- No loss of critical business information
- Retrieval accuracy > 75%
- Background consolidation runs reliably

### Knowledge Carries Forward
- Hierarchical memory patterns
- Consolidation strategies
- Multi-level retrieval

### Estimated Scope
~500 lines code, ~200 lines documentation

---

## v0.7 — Cost Optimization

**Goal:** API cost tracking with feedback loop for optimization

**Depends on:** v0.6

### Scope
- Track API costs per conversation/business
- Token usage monitoring
- Cost-per-outcome metrics
- Feedback loop for prompt optimization
- Model selection intelligence (use cheaper models when appropriate)
- Context compression before API calls

### Core Mechanisms

**Cost Tracking:**
- Tokens used per API call
- Cost per conversation
- Cost per business per month
- Cost vs. subscription credits

**Feedback Loop:**
- Track which prompts generate useful responses
- Measure response quality vs. cost
- Auto-suggest prompt improvements
- A/B test prompt variants

**Optimization Strategies:**
- Use smaller models for simple queries
- Compress context before sending
- Cache common patterns
- Batch similar requests

### Deliverables
- `src/costs/tracker.js` — Cost tracking
- `src/costs/optimizer.js` — Optimization logic
- `src/costs/feedback.js` — Feedback collection
- `src/prompts/compression.js` — Context compression
- Dashboard data for cost visibility

### Database Addition
```sql
api_usage (id, business_id, model, tokens_in, tokens_out, cost, quality_rating, created_at)
prompt_performance (id, prompt_hash, avg_quality, avg_cost, usage_count)
```

### Tech
- Token counting (tiktoken)
- Cost calculation per model
- Rating/feedback collection
- Caching layer

### Success Criteria
- Know exact cost per business
- 20%+ cost reduction through optimization
- Quality maintained or improved
- Users see cost transparency

### Knowledge Carries Forward
- Cost tracking patterns
- Optimization strategies
- Feedback loop architecture
- Model selection logic

### Estimated Scope
~400 lines code, ~100 lines documentation

---

## v0.7.1 — Dynamic Pricing Intelligence

**Goal:** Value-based pricing optimization

**Depends on:** v0.7

### Why This Matters
Not all queries cost the same or deliver the same value. Quick questions should cost less than deep strategy sessions.

### Scope
- Classify query complexity/value
- Adjust pricing based on actual usage patterns
- Implement "value tiers" (quick vs. deep)
- Credit consumption transparency
- Smart model routing based on query type

### Value Tiers
| Tier | Example | Model | Credit Cost |
|------|---------|-------|-------------|
| Quick | "What's my next step?" | Fast model | 1 credit |
| Standard | "Review my pitch deck" | Standard model | 5 credits |
| Deep | "Full market analysis" | Premium model | 20 credits |

### Deliverables
- `src/pricing/classifier.js` — Query classification
- `src/pricing/tiers.js` — Tier definitions
- `src/pricing/router.js` — Model routing
- Credit usage transparency in UI

### Success Criteria
- 30%+ cost reduction for simple queries
- Users understand credit consumption
- Quality maintained across tiers

### Knowledge Carries Forward
- Query classification
- Value-based routing
- Dynamic pricing patterns

### Estimated Scope
~300 lines code, ~100 lines documentation

---

## v0.7.2 — Progressive Context Loading

**Goal:** Load context on-demand for efficiency, including .md file progressive disclosure

**Depends on:** v0.7.1

### Why This Matters
As businesses grow, context grows. Without progressive loading, the system hits limits and degrades. Inspired by Claude Code's "progressive disclosure" approach.

### Scope
- Load context on-demand, not all at once
- Summarize old conversations, detail recent ones
- Lazy-load business history
- Track context window usage per session
- Smart chunking based on relevance
- **Progressive disclosure for .md files**

### Loading Strategy
```
Recent (7 days)     → Full detail
Recent (30 days)    → Summarized
Older               → Key points only
Relevant (semantic) → Full detail regardless of age
```

---

### .md File Progressive Disclosure System

#### The Problem
A typical `.bos.md` file might be 2000+ tokens. Loading 10 files = 20,000+ tokens wasted before conversation even starts.

#### The Solution: 4-Level Disclosure

```
Level 0: Index Only
  └── File names + 1-line description
  └── ~10 tokens per file

Level 1: Headers + Summary
  └── H1, H2 headers + brief summary
  └── ~50-100 tokens per file

Level 2: Key Sections
  └── Relevant sections expanded
  └── ~200-500 tokens per file

Level 3: Full Content
  └── Complete file when needed
  └── All tokens
```

#### Example: Progressive Loading of `vision.bos.md`

```
─────────────────────────────────────────────────────────
LEVEL 0 (Index)                              ~10 tokens
─────────────────────────────────────────────────────────
vision.bos.md: Company vision and mission

─────────────────────────────────────────────────────────
LEVEL 1 (Headers + Summary)                  ~80 tokens
─────────────────────────────────────────────────────────
# vision.bos.md
## Mission
## Vision  
## Values
## 5-Year Goals
Summary: B2B SaaS helping SMBs automate operations.
Target: 10K customers by 2028.

─────────────────────────────────────────────────────────
LEVEL 2 (Key Sections)                       ~300 tokens
─────────────────────────────────────────────────────────
# vision.bos.md
## Mission
Empower small businesses with enterprise-grade automation.

## Values
- Customer obsession
- Move fast, break nothing
- Data-driven decisions

## 5-Year Goals
[Summary: Revenue targets, customer count, market share]

─────────────────────────────────────────────────────────
LEVEL 3 (Full Content)                       ~1500 tokens
─────────────────────────────────────────────────────────
[Complete file content]
```

#### Smart Expansion Rules

```javascript
function determineDisclosureLevel(file, query, context) {
  // Always Level 0 for unrelated files
  if (relevanceScore(file, query) < 0.3) return 0;
  
  // Level 1 for potentially relevant
  if (relevanceScore(file, query) < 0.6) return 1;
  
  // Level 2 for likely relevant
  if (relevanceScore(file, query) < 0.85) return 2;
  
  // Level 3 only when:
  // - Directly mentioned by user
  // - High semantic match
  // - Agent explicitly requests
  if (relevanceScore(file, query) >= 0.85 || 
      userMentioned(file, query) ||
      agentRequested(file)) return 3;
      
  return 1; // Default to headers
}
```

#### File Index Structure

```yaml
# .bos-index.yaml (auto-generated)
files:
  - path: vision.bos.md
    description: "Company vision, mission, 5-year goals"
    keywords: [mission, vision, goals, values, strategy]
    tokens: 1523
    last_updated: 2026-01-15
    sections:
      - name: Mission
        keywords: [purpose, why]
        tokens: 120
      - name: Vision
        keywords: [future, 2028, growth]
        tokens: 340
      - name: Values
        keywords: [culture, principles]
        tokens: 180
        
  - path: competitors.bos.md
    description: "Competitor analysis and positioning"
    keywords: [competitors, market, differentiation]
    tokens: 2100
    sections:
      - name: Direct Competitors
        keywords: [competitor names, features]
        tokens: 800
      - name: Our Advantages
        keywords: [differentiation, moat]
        tokens: 450
```

#### Token Budget Management

```
Session Start:
  ├── Index all .bos.md files (Level 0)     ~50 tokens
  ├── System context                        ~500 tokens
  ├── Conversation history                  ~varies
  └── Available for query                   ~remaining

On Query:
  ├── Analyze relevance of each file
  ├── Expand relevant files to Level 1-2
  ├── Reserve tokens for response
  └── Only expand to Level 3 if essential

Token Budget Example (8K context window):
  ├── System prompt:        1,000 tokens
  ├── File index (L0):        100 tokens
  ├── Expanded files (L1-2): 1,500 tokens
  ├── Conversation:         2,000 tokens
  ├── Query:                  200 tokens
  └── Response budget:      3,200 tokens
```

#### Progressive Expansion Commands

```bash
# CLI commands for users to control disclosure
bos context show                    # Show current context usage
bos context expand vision.bos.md    # Force expand to Level 3
bos context collapse all            # Reset to Level 0
bos context budget                  # Show token budget status
```

#### Agent-Requested Expansion

```
Agent: "I need more details about your competitors to answer this."
       [Requesting expansion: competitors.bos.md → Level 3]
       
System: Expanded competitors.bos.md (800 → 2100 tokens)

Agent: [Now has full context to provide detailed answer]
```

---

### Deliverables
- `src/context/progressive.js` — Progressive loading
- `src/context/summarizer.js` — Auto-summarization
- `src/context/relevance.js` — Relevance scoring
- `src/context/md-disclosure.js` — .md file disclosure levels
- `src/context/index-generator.js` — Auto-generate .bos-index.yaml
- `src/context/token-budget.js` — Token budget management
- Context window usage metrics

### Database Addition
```sql
file_disclosure_state (
  id UUID PRIMARY KEY,
  session_id UUID,
  file_path VARCHAR(500),
  current_level INTEGER DEFAULT 0,
  tokens_loaded INTEGER,
  expanded_at TIMESTAMP,
  reason VARCHAR(100) -- 'user_request', 'relevance', 'agent_request'
)

context_budget_log (
  id UUID PRIMARY KEY,
  session_id UUID,
  total_budget INTEGER,
  system_tokens INTEGER,
  file_tokens INTEGER,
  conversation_tokens INTEGER,
  remaining INTEGER,
  logged_at TIMESTAMP
)
```

### Success Criteria
- 50%+ reduction in context tokens used
- No loss of relevant information
- Faster response times
- **70%+ of queries answered with Level 0-2 (no full file load)**
- **User can manually control disclosure level**

### Knowledge Carries Forward
- Progressive loading patterns
- Summarization approaches
- Context window management
- **Markdown parsing and sectioning**
- **Relevance-based expansion**

### Estimated Scope
~500 lines code, ~150 lines documentation

---

## v0.8 — Orchestration

**Goal:** Multi-agent foundation with routing

**Depends on:** v0.7

### Scope
- Agent abstraction layer
- Orchestrator to route requests
- Mentor agent (existing, refactored)
- Agent state management
- Inter-agent communication pattern

### Deliverables
- `src/agents/base.js` — Base agent class
- `src/agents/mentor.js` — Mentor agent (refactored)
- `src/orchestrator/` — Routing and coordination
- `src/agents/registry.js` — Agent registration
- `docs/agent-architecture.md` — How to create agents

### Architecture
```
User Input
    ↓
Orchestrator (routes based on intent)
    ↓
Agent (Mentor, Research, etc.)
    ↓
Context Layer (shared)
    ↓
Response
```

### Tech
- Agent pattern/interface
- Intent classification (simple rules or LLM)
- State machine for conversations

### Success Criteria
- Mentor agent works through orchestrator
- Foundation ready for additional agents
- Agents share context

### Knowledge Carries Forward
- Agent interface/contract
- Orchestration patterns
- How to add new agents
- Inter-agent communication

### Estimated Scope
~500 lines code, ~200 lines documentation

---

## v0.8.1 — Agent Abstraction Layer

**Goal:** Single-purpose, well-defined agent interfaces

**Depends on:** v0.8

### Why This Matters
Best practices show: keep agents focused and single-purpose rather than building "do-everything" agents. Narrow scopes ensure consistent performance.

### Scope
- Define clear agent interface contract
- Single-responsibility principle for agents
- Agent capability declaration
- Standard input/output formats
- Agent lifecycle management

### Agent Interface
```javascript
interface Agent {
  name: string;
  capabilities: string[];
  inputSchema: Schema;
  outputSchema: Schema;
  
  canHandle(intent: Intent): boolean;
  execute(input: AgentInput): Promise<AgentOutput>;
  getStatus(): AgentStatus;
}
```

### Deliverables
- `src/agents/interface.js` — Agent contract
- `src/agents/base.js` — Base implementation
- `src/agents/capability.js` — Capability system
- `docs/creating-agents.md` — Agent development guide

### Success Criteria
- All agents follow standard interface
- Easy to add new agents
- Clear capability boundaries

### Knowledge Carries Forward
- Agent interface pattern
- Capability-based design
- Single-responsibility architecture

### Estimated Scope
~200 lines code, ~150 lines documentation

---

## v0.8.2 — Isolated Agent Contexts

**Goal:** Each agent gets its own context window

**Depends on:** v0.8.1

### Why This Matters
Without isolation, multi-agent systems degrade main conversation quality. Each agent should work in its own "sandbox" and return summaries, not full dumps.

### Scope
- Per-agent context windows (isolated)
- Main conversation stays clean
- Agents return summaries to orchestrator
- Context doesn't "leak" between agents
- Memory management per agent

### Architecture
```
Main Context (User + Orchestrator)
    │
    ├── Mentor Agent Context (isolated 200k tokens)
    ├── Research Agent Context (isolated 200k tokens)
    └── Finance Agent Context (isolated 200k tokens)
```

### Deliverables
- `src/agents/context-isolation.js` — Isolation layer
- `src/agents/summarizer.js` — Agent-to-main summarization
- `src/orchestrator/context-manager.js` — Context coordination
- Memory tracking per agent

### Success Criteria
- Main context stays under 50k tokens
- Agent results don't bloat main conversation
- Clear separation of concerns

### Knowledge Carries Forward
- Context isolation patterns
- Summarization for handoff
- Memory management

### Estimated Scope
~300 lines code, ~100 lines documentation

---

## v0.8.3 — Parallel Agent Execution + Kimi Code Integration

**Goal:** Run multiple agents/tools simultaneously, with Kimi Code as default coding sub-agent

**Depends on:** v0.8.2

### Why This Matters
Sequential execution feels slow. Parallel execution feels like having a team. Speed is a major differentiator. Kimi K2.5's Agent Swarm provides native parallel execution at 10x lower cost.

### Scope
- Concurrent tool calls (web search + competitor analysis simultaneously)
- Parallel sub-agent invocation
- **Kimi Code integration** (default coding sub-agent)
- **Claude Code as alternative** (`--agent=claude`)
- Async result aggregation
- Dependency-aware scheduling (some things must be sequential)
- Progress reporting for parallel tasks

### Kimi Code Agent Swarm
Kimi K2.5 uses **Parallel-Agent Reinforcement Learning (PARL)**:
- Up to **100 sub-agents** working in parallel
- Up to **1,500 tool calls** simultaneously
- **4.5x faster** execution vs sequential
- **10x cheaper** than Claude Code
- Self-organizing orchestrator (no predefined workflows)

### Execution Model
```
Intent: "Research my competitors and analyze market size"
    │
    ├── [Parallel] Competitor Research Agent
    │       └── [Parallel] Search Tool × 3
    ├── [Parallel] Market Analysis Agent
    │
    └── [Aggregate] Combine results

Intent: "Refactor src/ with error handling"
    │
    ├── [Kimi Code Agent Swarm]
    │   ├── Sub-Agent: File 1 refactor
    │   ├── Sub-Agent: File 2 refactor
    │   ├── Sub-Agent: File 3 refactor
    │   └── Sub-Agent: Test generation
    │
    └── [Aggregate] Combined changes
```

### Coding Agent Selection
| Task Type | Default Agent | Alternative | Rationale |
|-----------|---------------|-------------|-----------|
| Multi-file refactor | **Kimi Code** | Claude Code | Parallel agents excel |
| Codebase analysis | **Kimi Code** | Claude Code | Parallel scanning |
| Test generation | **Kimi Code** | Claude Code | Fully parallelizable |
| Complex debugging | Claude Code | Kimi Code | Deep reasoning |
| Time-critical fix | Claude Code | Kimi Code | Faster tokens |

### Deliverables
- `src/orchestrator/parallel.js` — Parallel execution engine
- `src/orchestrator/scheduler.js` — Dependency scheduling
- `src/orchestrator/aggregator.js` — Result aggregation
- `src/agents/coding/kimi-code.js` — Kimi Code agent (default)
- `src/agents/coding/claude-code.js` — Claude Code agent (alternative)
- `src/agents/coding/router.js` — Coding agent selection logic
- Progress UI for parallel tasks
- CLI flag: `--agent=kimi` (default) | `--agent=claude`

### Integration
```javascript
// Kimi Agent SDK (Node.js native)
import { KimiAgent } from 'kimi-agent-sdk';

const agent = new KimiAgent({
  apiKey: process.env.KIMI_API_KEY,
  model: 'k2.5',
  agentSwarm: true,
  maxAgents: 50
});

await agent.execute({
  task: 'refactor',
  files: ['src/api.js', 'src/memory.js'],
  parallelism: 'auto'
});
```

### Success Criteria
- 4.5x+ speedup for multi-file coding tasks (via Kimi Code)
- 3x+ speedup for multi-step research tasks
- Correct handling of dependencies
- Clear progress visibility
- `--agent=claude` works as alternative

### Knowledge Carries Forward
- Parallel execution patterns
- Kimi Agent SDK integration
- Coding agent abstraction
- Dependency management
- Result aggregation

### Estimated Scope
~500 lines code, ~200 lines documentation

---

## v0.8.3.1 — Kimi Code Deep Integration

**Goal:** Full Kimi Code capabilities with Agent Swarm optimization

**Depends on:** v0.8.3

### Scope
- Agent Swarm orchestration for complex tasks
- Dynamic agent creation based on task type
- Cost tracking per coding operation
- Fallback to Claude Code on Kimi failures
- Task-based auto-selection (smart routing)

### Deliverables
- `src/agents/coding/kimi-swarm.js` — Agent Swarm orchestration
- `src/agents/coding/cost-tracker.js` — Per-operation cost tracking
- `src/agents/coding/auto-select.js` — Smart agent routing
- Configuration: `bos.config.js` coding section

### Success Criteria
- Complex refactors use 50+ parallel agents
- 90%+ cost savings vs Claude Code default
- Automatic fallback works reliably
- Task auto-selection matches manual selection 90%+

### Estimated Scope
~300 lines code, ~100 lines documentation

---

## v0.8.4 — Plan Mode (Safety & Control)

**Goal:** Propose plan before executing for user approval

**Depends on:** v0.8.3

### Why This Matters
Trust and control are essential. Users need to feel safe before the AI takes autonomous actions. For complex/risky operations, AI should propose, human should approve.

### Scope
- For complex operations, AI proposes plan first
- User reviews and approves before execution
- Execution only after confirmation
- Audit trail of planned vs. executed
- Rollback capability where possible

### Plan Mode Flow
```
User: "Restructure my business model"
    │
    ▼
AI: "Here's my plan:
    1. Analyze current model (5 min)
    2. Research alternatives (10 min)
    3. Propose 3 options (5 min)
    4. Detail implementation for chosen option
    
    Proceed? [Yes/No/Modify]"
    │
    ▼
User: "Yes"
    │
    ▼
AI: [Executes plan with progress updates]
```

### Deliverables
- `src/modes/plan-mode.js` — Plan mode logic
- `src/modes/plan-approval.js` — Approval flow
- `src/modes/execution-tracker.js` — Execution tracking
- `src/audit/plan-history.js` — Audit trail
- UI for plan review/approval

### Database Addition
```sql
plan_history (id, business_id, plan JSONB, status, approved_at, executed_at)
```

### Success Criteria
- Users feel in control
- No unexpected autonomous actions
- Clear audit trail

### Knowledge Carries Forward
- Plan-then-execute pattern
- Approval workflows
- Audit trail design

### Estimated Scope
~300 lines code, ~100 lines documentation

---

## v0.8.5 — MCP Protocol Support

**Goal:** Standard integration protocol for external tools

**Depends on:** v0.8.4

### Why This Matters
MCP (Model Context Protocol) is becoming the standard for AI tool integration. Supporting it future-proofs the architecture and enables ecosystem growth.

### Scope
- Support Model Context Protocol standard
- Pre-built MCP integrations
- Community integration marketplace (future)
- Easy MCP server installation

### Pre-built MCPs
| MCP | Function |
|-----|----------|
| Playwright | Browser automation, screenshots |
| Notion | Document management |
| Google Sheets | Spreadsheet operations |
| Gmail | Email operations |
| CRM (generic) | Customer management |

### Deliverables
- `src/mcp/client.js` — MCP client
- `src/mcp/registry.js` — Integration registry
- `src/mcp/installer.js` — MCP installation
- `src/mcp/integrations/` — Pre-built integrations
- `docs/mcp-integration.md` — Integration guide

### Success Criteria
- Easy to add new MCPs
- Pre-built MCPs work reliably
- Clear integration documentation

### Knowledge Carries Forward
- MCP protocol patterns
- Integration architecture
- Tool extensibility

### Estimated Scope
~400 lines code, ~200 lines documentation

---

## v0.8.6 — Research Agent

**Goal:** Market research and competitive analysis capabilities

**Depends on:** v0.8.5

### Why This Matters
Competitors offer instant market sizing, competitive analysis. We need feature parity plus our contextual advantage.

### Scope
- Market size estimation (TAM/SAM/SOM)
- Competitor identification and analysis
- Customer segment research
- Web research integration (search, scrape)
- Research report generation

### Capabilities
| Capability | Description |
|------------|-------------|
| Market Sizing | TAM/SAM/SOM estimation with sources |
| Competitor Analysis | Find and analyze competitors |
| Customer Research | Identify target segments |
| Trend Analysis | Industry trends and timing |
| SWOT Generation | Automated SWOT analysis |

### Deliverables
- `src/agents/research/` — Research agent
- `src/agents/research/market-size.js` — Market sizing
- `src/agents/research/competitors.js` — Competitor analysis
- `src/agents/research/customers.js` — Customer research
- Research report templates

### Success Criteria
- Market sizing within 20% of professional estimates
- Identify 80%+ of major competitors
- Research reports are actionable

### Knowledge Carries Forward
- Research methodology
- Data source integration
- Report generation

### Estimated Scope
~500 lines code, ~200 lines documentation

---

## v0.8.7 — Scheduled Automation (Cron System)

**Goal:** Background task scheduling for autonomous agent actions

**Depends on:** v0.8.6

### Why This Matters
Users want "set it and forget it" automation. Proactive agents that work in the background reduce manual trigger fatigue and enable insights delivery before users ask.

### Scope
- Cron-style scheduling (daily, weekly, custom expressions)
- Scheduled skill execution
- Proactive insights generation
- Digest/report generation
- Reminder and follow-up automation
- Durable execution (survives crashes)

### Schedule Types
| Type | Example | Use Case |
|------|---------|----------|
| **Recurring** | "Every Monday 9am" | Weekly planning |
| **Daily** | "Every day 6pm" | End-of-day summary |
| **Conditional** | "If no activity 3 days" | Re-engagement |
| **Event-based** | "After stage change" | Progression celebration |
| **One-time** | "On Jan 15 at 10am" | Deadline reminder |

### Example Schedules
```javascript
{
  name: "weekly-planning",
  schedule: "0 9 * * 1",  // Every Monday 9am
  skill: "skill:weekly-planning",
  notify: ["push", "email"]
}

{
  name: "daily-digest",
  schedule: "0 18 * * *",  // Every day 6pm
  action: "generate-digest",
  notify: ["push"]
}

{
  name: "re-engagement",
  condition: "no_activity_days > 3",
  action: "send-checkin",
  notify: ["push"]
}
```

### Proactive Behaviors
| Behavior | Trigger | Action |
|----------|---------|--------|
| Strategic Drift Alert | 3+ days low-value activity | Push + suggestion |
| Weekly Digest | Sunday evening | Summary + priorities |
| Competitor Alert | New competitor detected | Notification + analysis |
| Stage Nudge | Confidence threshold met | Prompt to advance |
| Re-engagement | 5+ days no activity | Gentle check-in |

### Deliverables
- `src/scheduler/engine.js` — Cron engine
- `src/scheduler/jobs.js` — Job definitions
- `src/scheduler/conditions.js` — Conditional triggers
- `src/scheduler/notifications.js` — Notification dispatch
- `src/scheduler/durable.js` — Durable execution
- `docs/scheduling.md` — Scheduling documentation

### Database Addition
```sql
schedules (id, user_id, business_id, name, cron_expr, skill_id, config JSONB, last_run, next_run, status)
schedule_history (id, schedule_id, result JSONB, executed_at, duration_ms)
proactive_actions (id, business_id, action_type, triggered_by, delivered_at, user_response)
```

### Tech
- node-cron for simple scheduling
- Optional: Temporal.io for durable execution
- Push notification service integration
- Background job queue (Bull/BullMQ)

### Success Criteria
- Scheduled jobs run reliably (99%+ uptime)
- Users receive proactive insights
- Re-engagement improves retention by 15%+

### Knowledge Carries Forward
- Scheduling patterns
- Proactive agent design
- Notification systems

### Estimated Scope
~600 lines code, ~200 lines documentation

---

## v0.8.8 — Agents Management System

**Goal:** User-friendly agent management with confidence scoring and meta-agent capabilities

**Depends on:** v0.8.7

### Why This Matters
As Business-OS grows, users need to manage multiple "agentic employees." Each agent needs:
- Clear visibility into what it does
- Confidence scoring to ensure quality
- Iteration loops until satisfaction (8.5+)
- Ability to create and train new agents

### Agent Management Concepts

**Agentic Employees:**
Think of agents as specialized team members, not just code. Users should:
- See what each agent is good at
- Understand agent limitations
- Monitor agent performance
- Train/improve agents over time

---

### Agent Team Examples by Company Stage

Different stages need different agent teams:

#### 🌱 IDEA STAGE
| Agent | Role | Key Tasks |
|-------|------|-----------|
| **Mentor Agent** | Strategic advisor | Challenge assumptions, first principles thinking |
| **Research Agent** | Market intelligence | Market size, competitor analysis, trend research |
| **Validation Agent** | Idea tester | Customer interview scripts, survey design, validation experiments |

```
Example Team for Idea Stage:
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│ 🧠 MENTOR   │  │ 🔍 RESEARCH │  │ ✓ VALIDATION│
│ "Is this    │  │ "Market is  │  │ "Interview  │
│  worth      │  │  $50B, 3    │  │  20 users   │
│  pursuing?" │  │  competitors"│  │  this week" │
└─────────────┘  └─────────────┘  └─────────────┘
```

#### 🚀 MVP STAGE
| Agent | Role | Key Tasks |
|-------|------|-----------|
| **Mentor Agent** | Strategic advisor | Prioritization, scope decisions |
| **Product Agent** | Product manager | Feature specs, user stories, roadmap |
| **Customer Agent** | Customer success | User feedback, support, onboarding |
| **Dev Advisor Agent** | Technical guide | Architecture advice, tech stack decisions |

```
Example Team for MVP Stage:
┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│ 🧠 MENTOR   │  │ 📦 PRODUCT  │  │ 👥 CUSTOMER │  │ 💻 DEV      │
│ "Focus on  │  │ "MVP scope: │  │ "Users want │  │ "Use this   │
│  one thing" │  │  3 features" │  │  X feature" │  │  stack"     │
└─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘
```

#### 📈 GROWTH STAGE
| Agent | Role | Key Tasks |
|-------|------|-----------|
| **Mentor Agent** | Strategic advisor | Growth strategy, scaling decisions |
| **Marketing Agent** | Growth marketer | Campaign ideas, content strategy, SEO |
| **Sales Agent** | Sales development | Lead qualification, outreach scripts, objection handling |
| **Analytics Agent** | Data analyst | Metrics tracking, cohort analysis, funnel optimization |
| **Finance Agent** | CFO assistant | Cash flow, unit economics, fundraising prep |

```
Example Team for Growth Stage:
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│ 📣 MARKETING│  │ 💰 SALES    │  │ 📊 ANALYTICS│
│ "Launch    │  │ "Qualify    │  │ "CAC is    │
│  campaign X"│  │  these leads"│  │  $45, LTV   │
│             │  │             │  │  is $180"   │
└─────────────┘  └─────────────┘  └─────────────┘
        ↓               ↓               ↓
    ┌─────────────────────────────────────────┐
    │ 🧠 MENTOR: "Focus on channel X, double  │
    │    down before diversifying"            │
    └─────────────────────────────────────────┘
```

#### 🏢 SCALE STAGE
| Agent | Role | Key Tasks |
|-------|------|-----------|
| **Mentor Agent** | Strategic advisor | Org design, culture, long-term strategy |
| **Operations Agent** | COO assistant | Process optimization, vendor management |
| **HR Agent** | People operations | Hiring plans, culture docs, team health |
| **Legal Agent** | Legal advisor | Contract review, compliance, IP protection |
| **Finance Agent** | CFO assistant | Financial planning, investor relations |

---

### Agent Team Examples by Business Strategy

Different strategies need specialized agents:

#### B2B SaaS Strategy
| Agent | Focus |
|-------|-------|
| **Sales Dev Agent** | Outbound sequences, lead scoring, demo prep |
| **Customer Success Agent** | Onboarding, health scores, expansion opportunities |
| **Product Marketing Agent** | Positioning, competitive battlecards, case studies |
| **Pricing Agent** | Pricing optimization, packaging, tier analysis |

#### E-Commerce Strategy
| Agent | Focus |
|-------|-------|
| **Inventory Agent** | Stock levels, reorder points, supplier management |
| **Merchandising Agent** | Product descriptions, categorization, upsells |
| **Ads Agent** | Ad copy, audience targeting, ROAS optimization |
| **Fulfillment Agent** | Shipping optimization, returns analysis |

#### Content/Creator Strategy
| Agent | Focus |
|-------|-------|
| **Content Agent** | Content calendar, topic research, drafts |
| **Engagement Agent** | Community management, comment responses |
| **Sponsorship Agent** | Brand partnerships, rate cards, outreach |
| **Monetization Agent** | Revenue streams, product ideas, pricing |

#### Service Business Strategy
| Agent | Focus |
|-------|-------|
| **Booking Agent** | Scheduling, availability, client matching |
| **Proposal Agent** | Scope documents, pricing, contracts |
| **Delivery Agent** | Project tracking, client updates, quality checks |
| **Referral Agent** | Testimonial collection, referral programs |

#### Marketplace Strategy
| Agent | Focus |
|-------|-------|
| **Supply Agent** | Seller acquisition, onboarding, quality |
| **Demand Agent** | Buyer acquisition, matching, conversion |
| **Trust & Safety Agent** | Fraud detection, dispute resolution, policies |
| **Liquidity Agent** | Supply-demand balance, pricing dynamics |

---

### Pre-Built Agent Templates

Business-OS includes pre-configured agent templates:

```yaml
# Example: Research Agent Template
name: research-agent
category: intelligence
description: "Market research and competitive intelligence"
capabilities:
  - market_sizing
  - competitor_analysis
  - trend_research
  - customer_research
system_prompt: |
  You are a research analyst. Your job is to provide
  data-driven insights about markets, competitors, and customers.
  Always cite sources. Quantify when possible.
recommended_stages: [idea, mvp, growth]
recommended_strategies: [b2b_saas, marketplace, ecommerce]
```

```yaml
# Example: Sales Agent Template
name: sales-agent
category: revenue
description: "Sales development and deal support"
capabilities:
  - lead_qualification
  - outreach_sequences
  - objection_handling
  - demo_prep
  - proposal_writing
system_prompt: |
  You are a sales development representative. Your job is to
  qualify leads, craft compelling outreach, and help close deals.
  Be consultative, not pushy. Focus on customer problems.
recommended_stages: [growth, scale]
recommended_strategies: [b2b_saas, service]
```

### Stage-Aware Agent Recommendations

When user onboards, Business-OS recommends agents based on their stage:

```
User: "I'm at the idea stage for a B2B SaaS"

Business-OS:
  Recommended Agent Team:
  
  ┌─ ESSENTIAL ────────────────────────────────────┐
  │ ✓ Mentor Agent — Strategic guidance            │
  │ ✓ Research Agent — Market validation           │
  │ ✓ Validation Agent — Customer discovery        │
  └────────────────────────────────────────────────┘
  
  ┌─ ADD LATER (MVP Stage) ────────────────────────┐
  │ ○ Product Agent — Feature prioritization       │
  │ ○ Customer Agent — Early user support          │
  └────────────────────────────────────────────────┘
  
  ┌─ ADD LATER (Growth Stage) ─────────────────────┐
  │ ○ Sales Dev Agent — Outbound sequences         │
  │ ○ Marketing Agent — Content & campaigns        │
  │ ○ Analytics Agent — Metrics & optimization     │
  └────────────────────────────────────────────────┘
  
  [Create Recommended Team] [Customize]
```

---

### Confidence Scoring System

Every agent output includes a confidence score (1-10):

```
Confidence Levels:
  1-3:  Low confidence — Needs human review
  4-6:  Medium confidence — Proceed with caution
  7-8:  High confidence — Likely correct
  8.5+: Satisfaction threshold — Auto-approved
  9-10: Very high confidence — Highly reliable
```

### Iteration Loop (Until 8.5+ Satisfaction)

```
User Request
    ↓
Agent Generates Response
    ↓
Confidence Score Calculated
    ↓
Is Confidence >= 8.5?
    ├── YES → Deliver to user
    └── NO → Iterate:
            ├── Agent self-reviews
            ├── Requests clarification
            ├── Tries alternative approach
            └── Repeat until 8.5+ OR max iterations
```

### User-Facing Agent Dashboard

```
┌─────────────────────────────────────────────────────────────────┐
│  YOUR AGENTS                                        [+ Create]  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────┐  ┌─────────────────────┐              │
│  │ 🧠 MENTOR AGENT     │  │ 🔍 RESEARCH AGENT   │              │
│  │                     │  │                     │              │
│  │ Status: Active      │  │ Status: Active      │              │
│  │ Confidence: 8.7/10  │  │ Confidence: 8.2/10  │              │
│  │ Tasks: 47 completed │  │ Tasks: 12 completed │              │
│  │                     │  │                     │              │
│  │ [Configure] [Logs]  │  │ [Configure] [Logs]  │              │
│  └─────────────────────┘  └─────────────────────┘              │
│                                                                 │
│  ┌─────────────────────┐  ┌─────────────────────┐              │
│  │ 📊 ANALYSIS AGENT   │  │ ⚙️ BUILDER AGENT    │              │
│  │                     │  │                     │              │
│  │ Status: Training    │  │ Status: Paused      │              │
│  │ Confidence: 6.4/10  │  │ Confidence: 7.1/10  │              │
│  │ Tasks: 5 completed  │  │ Tasks: 3 completed  │              │
│  │                     │  │                     │              │
│  │ [Train More] [Logs] │  │ [Resume] [Logs]     │              │
│  └─────────────────────┘  └─────────────────────┘              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Meta-Agent: Agent Builder

The **Agent Builder** is a special agent that creates other agents:

```
User: "I need an agent that monitors my competitors weekly"

Agent Builder:
  ├── Analyzes requirements
  ├── Designs agent capabilities
  ├── Creates agent configuration
  ├── Generates system prompt
  ├── Sets up scheduled triggers
  └── Deploys new agent

Result: New "Competitor Monitor" agent created
```

### Skill: Agent Creator

A skill that teaches users to create agents:

```yaml
name: agent-creator
description: Create custom agents for your business
steps:
  - prompt: "What task should this agent handle?"
  - prompt: "What data does it need access to?"
  - prompt: "How often should it run?"
  - action: generate-agent-config
  - action: test-agent
  - action: deploy-agent
```

### Scope

- Agent registry with metadata
- User-friendly agent dashboard
- Confidence scoring (1-10) on all outputs
- Iteration loop until 8.5+ satisfaction
- Agent performance tracking
- Meta-agent for creating agents
- Agent-creator skill
- Agent training/improvement workflow
- Agent pause/resume controls
- Agent logs and history

### Deliverables

- `src/agents/registry.js` — Agent registry
- `src/agents/confidence.js` — Confidence scoring
- `src/agents/iteration.js` — Iteration loop
- `src/agents/meta-builder.js` — Meta-agent builder
- `src/agents/dashboard.js` — Dashboard data
- `src/skills/agent-creator.js` — Agent creation skill
- `gui/src/components/AgentsDashboard.js` — UI
- `docs/agents-management.md` — Documentation

### Database Addition

```sql
-- Agent Registry
agents (
  id UUID PRIMARY KEY,
  business_id UUID REFERENCES businesses(id),
  name VARCHAR(255) NOT NULL,
  type VARCHAR(100), -- 'mentor', 'research', 'custom'
  description TEXT,
  system_prompt TEXT,
  capabilities JSONB, -- ['market_research', 'competitor_analysis']
  config JSONB, -- settings, thresholds
  status VARCHAR(50) DEFAULT 'active', -- 'active', 'paused', 'training'
  created_by UUID REFERENCES users(id),
  created_at TIMESTAMP DEFAULT NOW()
)

-- Agent Performance
agent_performance (
  id UUID PRIMARY KEY,
  agent_id UUID REFERENCES agents(id),
  task_id UUID,
  confidence_score DECIMAL(3,1), -- 0.0 to 10.0
  iterations INTEGER DEFAULT 1,
  final_score DECIMAL(3,1),
  user_rating INTEGER, -- 1-10 user feedback
  tokens_used INTEGER,
  duration_ms INTEGER,
  created_at TIMESTAMP DEFAULT NOW()
)

-- Agent Confidence History
agent_confidence_history (
  id UUID PRIMARY KEY,
  agent_id UUID REFERENCES agents(id),
  avg_confidence DECIMAL(3,1),
  total_tasks INTEGER,
  satisfaction_rate DECIMAL(3,2), -- % of tasks >= 8.5
  period VARCHAR(20), -- 'daily', 'weekly', 'monthly'
  recorded_at TIMESTAMP DEFAULT NOW()
)
```

### Confidence Calculation

```javascript
function calculateConfidence(response, context) {
  const factors = {
    // Source quality (0-2)
    sourceReliability: assessSources(response.sources),
    
    // Completeness (0-2)
    completeness: assessCompleteness(response, context.requirements),
    
    // Consistency (0-2)
    consistency: checkConsistency(response, context.history),
    
    // Relevance (0-2)
    relevance: assessRelevance(response, context.query),
    
    // Uncertainty markers (0-2, higher = more certain)
    certainty: 2 - countUncertaintyMarkers(response)
  };
  
  const rawScore = Object.values(factors).reduce((a, b) => a + b, 0);
  return rawScore; // 0-10 scale
}
```

### Iteration Strategy

```javascript
async function iterateUntilSatisfied(agent, task, maxIterations = 5) {
  let iteration = 0;
  let response = null;
  let confidence = 0;
  
  while (iteration < maxIterations && confidence < 8.5) {
    iteration++;
    
    if (iteration === 1) {
      response = await agent.execute(task);
    } else {
      // Self-review and improve
      response = await agent.selfReview(response, {
        previousConfidence: confidence,
        iteration: iteration,
        feedback: getAutomatedFeedback(response)
      });
    }
    
    confidence = calculateConfidence(response, task.context);
    
    // Log iteration
    await logIteration(agent.id, task.id, iteration, confidence);
    
    if (confidence >= 8.5) {
      return { response, confidence, iterations: iteration, satisfied: true };
    }
  }
  
  // Max iterations reached, return best effort with warning
  return { 
    response, 
    confidence, 
    iterations: iteration, 
    satisfied: false,
    warning: `Max iterations reached. Confidence: ${confidence}/10`
  };
}
```

### Success Criteria

- Users can view/manage all agents in dashboard
- Confidence scores displayed on all agent outputs
- 8.5+ satisfaction achieved in 90%+ of tasks
- Users can create custom agents
- Agent performance improves over time
- Meta-agent successfully creates functional agents

### Knowledge Carries Forward

- Agent registry patterns
- Confidence scoring algorithms
- Iteration loop design
- Meta-agent architecture
- Agent training workflows

### Estimated Scope
~800 lines code, ~300 lines documentation

---

## Alignment & Honesty System

### Mission Alignment

**Our job is to help users launch QUALITY businesses, not just any business.**

| Wrong Goal | Right Goal |
|------------|------------|
| Maximize engagement | Maximize user success |
| Keep users happy | Keep users growing |
| Validate all ideas | Challenge weak ideas |
| Avoid hard truths | Deliver hard truths kindly |
| Retain users at all costs | Help users succeed or pivot fast |

---

### Honesty Protocol

**The AI must be honest, even when it's uncomfortable.**

#### 1. No False Hope

```
❌ WRONG: "Great idea! Let's build it!"
✅ RIGHT: "I see potential, but there are 3 concerns 
          we need to address first. Let's talk about 
          your target market validation."
```

#### 2. Admit Uncertainty

```
❌ WRONG: "This will definitely work."
✅ RIGHT: "Based on the data, this has a 60% chance 
          of working. Here's what could go wrong and 
          how to mitigate it."
```

#### 3. Challenge Bad Ideas

```
❌ WRONG: "If that's what you want to do, let's do it."
✅ RIGHT: "I need to push back here. This approach 
          failed for 3 similar startups because [reason]. 
          Can we explore alternatives?"
```

#### 4. Surface Hard Truths

```
❌ WRONG: [Avoid mentioning low traction]
✅ RIGHT: "Let's be honest about the numbers. 
          3 signups in 30 days isn't working. 
          Either the product, the market, or the 
          distribution is wrong. Which should we 
          investigate first?"
```

#### 5. Recommend Stopping When Appropriate

```
❌ WRONG: "Keep going, you'll figure it out!"
✅ RIGHT: "Based on 6 months of data, this isn't 
          gaining traction. I think we should either:
          A) Pivot to [alternative]
          B) Pause and validate a different idea
          What's your gut telling you?"
```

---

### Quality Gates

**Business-OS enforces quality checkpoints before progression.**

#### Idea Stage Gates

| Gate | Requirement | AI Role |
|------|-------------|---------|
| **Problem Clarity** | Problem is specific and validated | Challenge vague problems |
| **Target User** | Can describe user in detail | Push for specificity |
| **Market Size** | Addressable market is viable | Research and verify |
| **Differentiation** | Clear reason to win | Challenge "me too" ideas |
| **Founder Fit** | Why YOU for this problem? | Honest assessment |

#### MVP Stage Gates

| Gate | Requirement | AI Role |
|------|-------------|---------|
| **User Validation** | 10+ conversations with target users | Don't let them skip this |
| **Problem-Solution Fit** | Users confirm solution solves problem | Verify, don't assume |
| **Willingness to Pay** | Users would pay (not just "nice to have") | Push for commitment signals |
| **Scope Discipline** | MVP is truly minimal | Fight scope creep |

#### Growth Stage Gates

| Gate | Requirement | AI Role |
|------|-------------|---------|
| **Retention** | Users coming back | Flag churn honestly |
| **Unit Economics** | LTV > CAC | Run the real numbers |
| **Scalability** | Growth path is clear | Challenge hand-wavy plans |
| **Team Readiness** | Ready to scale operations | Assess honestly |

---

### Anti-Patterns to Avoid

**The AI is trained to recognize and prevent these failure modes:**

| Anti-Pattern | What It Looks Like | AI Response |
|--------------|-------------------|-------------|
| **Solution Searching** | "I built X, who needs it?" | "Let's start with the problem, not the solution" |
| **Feature Creep** | "Let's also add..." | "What can we DELETE instead?" |
| **Vanity Metrics** | "We have 10K signups!" | "How many are active? Paying?" |
| **Premature Scaling** | Hiring before product-market fit | "Let's validate retention first" |
| **Avoiding Hard Conversations** | Not talking to customers | "When did you last talk to a user?" |
| **Sunk Cost Fallacy** | "We've invested too much to stop" | "What would you do if starting fresh today?" |
| **Echo Chamber** | Only hearing positive feedback | "Who has told you this is a bad idea?" |
| **Building in Silence** | Months without user feedback | "Ship something. Today. Even if it's ugly." |

---

### Truth-Telling Framework

**How agents deliver hard truths:**

```
1. ACKNOWLEDGE
   "I can see you're excited about this direction..."

2. PRESENT DATA
   "But here's what the numbers show..."

3. SHARE CONCERN
   "My concern is..."

4. OFFER ALTERNATIVES
   "Here are 3 other approaches to consider..."

5. INVITE DIALOGUE
   "What's your take? Am I missing something?"
```

**Example:**
```
User: "I want to build a social network for pet owners"

Mentor: "I can see the appeal—pet owners are passionate 
communities. But here's my concern: the pet social 
network space has 47 failed startups and 3 
well-funded competitors. 

The data shows most failed because user acquisition 
cost was 10x higher than monetization potential.

Three alternatives worth exploring:
1. Niche down: Social network for exotic pet owners only
2. Pivot value prop: Pet health tracking with community
3. B2B angle: Tools for pet businesses, not consumers

What draws you to social specifically? 
Is there something I'm not seeing?"
```

---

### Success-First Metrics

**We optimize for user business success, not just platform engagement.**

| Vanity Metric | Success Metric |
|---------------|----------------|
| Daily active users | Users who hit milestones |
| Time in app | Progress through stages |
| Messages sent | Quality decisions made |
| Feature usage | Validated ideas launched |
| Retention | Businesses that succeed |

**North Star:** Businesses launched that are still alive at 1 year.

---

### Alignment Checks

**Built-in safeguards to keep the AI honest:**

#### Self-Check Before Responding

```
Before every response, agent asks:
□ Am I being honest or just agreeable?
□ Would a good mentor say this?
□ Am I helping short-term or long-term?
□ Is this what user WANTS or what they NEED to hear?
□ Am I avoiding a hard truth?
```

#### User Can Request Brutal Honesty

```
User: "/brutal" or "Give it to me straight"

AI: [Activates maximum honesty mode]
"Okay, here's the unfiltered version: 
Your burn rate gives you 4 months. Your growth is flat. 
Your product has 3 active users, 2 of whom are friends. 
You've been 'almost ready to launch' for 6 months.

This isn't working. Let's figure out why, or figure 
out what else you should be doing with your time."
```

#### Weekly Alignment Review

```
Every week, AI generates honest assessment:

BUSINESS HEALTH CHECK
━━━━━━━━━━━━━━━━━━━━
Progress: 🟡 Stalled
Honest Assessment: "You've been avoiding customer 
conversations. The product work feels productive, 
but we have no validation. Priority this week 
should be 5 customer calls, not features."

Hard Truth: "At current pace, runway ends before 
product-market fit. We need to move faster or 
reconsider scope."
```

---

### The Honesty Commitment

```
Business-OS commits to:

1. TRUTH over comfort
   We tell you what you need to hear, 
   not what you want to hear.

2. LONG-TERM over engagement
   We'd rather you succeed and leave 
   than stay and fail.

3. QUALITY over quantity
   We'd rather help launch 100 great businesses 
   than 1,000 mediocre ones.

4. CHALLENGE over validation
   Great co-founders challenge your thinking. 
   So do we.

5. DATA over opinion
   When possible, we show you evidence, 
   not just advice.

6. FOUNDER-FIT over good ideas
   A great idea for the wrong founder fails.
   We help you build what YOU can win.

7. STRATEGY-ALIGNED over opportunistic
   Stay true to your chosen path.
   We flag drift before it derails you.
```

---

### Founder Alignment

**The right business for the wrong founder still fails.**

#### Founder Profile Assessment

When onboarding, we understand WHO you are:

```yaml
founder_profile:
  # Skills & Experience
  skills:
    technical: 7/10      # Can you build it?
    sales: 4/10          # Can you sell it?
    marketing: 5/10      # Can you market it?
    operations: 6/10     # Can you run it?
    finance: 3/10        # Can you manage money?
    domain_expertise: 8/10  # Do you know this space?
  
  # Resources
  resources:
    time_weekly: "20 hours"    # Side project or full-time?
    runway_months: 12          # How long can you sustain?
    capital_available: "$10K"  # Bootstrap or funded?
    network_strength: "weak"   # Can you get intros?
  
  # Motivations
  motivations:
    primary: "independence"    # Why are you doing this?
    risk_tolerance: "moderate" # How much can you lose?
    timeline: "2 years"        # When do you need results?
    exit_goal: "lifestyle"     # Sell, scale, or sustain?
  
  # Constraints
  constraints:
    - "Can't relocate"
    - "Must stay profitable (no VC path)"
    - "Limited to evenings/weekends"
```

#### Founder-Fit Checks

**Before validating any idea, we check founder fit:**

| Dimension | Question | Red Flag |
|-----------|----------|----------|
| **Skills** | Can you execute this? | Idea requires skills you lack with no plan to acquire |
| **Resources** | Can you sustain this? | Requires more capital/time than available |
| **Motivation** | Does this align with WHY? | Building for wrong reasons |
| **Constraints** | Does this fit your life? | Conflicts with stated constraints |
| **Unfair Advantage** | Why YOU? | No clear reason you'd win |

#### Founder-Fit Conversations

```
User: "I want to build a B2B enterprise SaaS"

AI: "Let me check founder fit first.

Looking at your profile:
• Sales skill: 4/10 — Enterprise sales is relationship-heavy
• Network: weak — Enterprise needs warm intros
• Time: 20 hrs/week — Enterprise deals take months
• Runway: 12 months — Enterprise sales cycles are 6-12 months

Honest assessment: This is a tough fit.

Three options:
1. Find a co-founder with enterprise sales experience
2. Start with SMB (faster sales, builds skills for enterprise)
3. Pivot to a different business model that fits your strengths

What draws you to enterprise specifically?"
```

#### Founder Growth Tracking

```
Over time, we track founder skill development:

FOUNDER GROWTH REPORT
━━━━━━━━━━━━━━━━━━━━━
3 months ago → Today

Sales:      4/10 → 6/10  ↑ (20 customer calls!)
Marketing:  5/10 → 5/10  → (needs attention)
Technical:  7/10 → 7/10  →
Finance:    3/10 → 4/10  ↑ (completed basics course)

Recommendation: Your sales skills improved significantly.
Marketing is now the bottleneck. Suggest focusing on
content marketing this month.
```

---

### Strategy Alignment

**Pick a strategy. Stick to it. We'll keep you honest.**

#### Strategy Definition

During setup, users define their strategy:

```yaml
business_strategy:
  # Business Model
  model: "B2B SaaS"
  pricing: "subscription"
  target_segment: "SMB (10-50 employees)"
  
  # Go-To-Market
  acquisition: "content marketing"
  sales_motion: "self-serve + sales assist"
  
  # Competitive Position
  differentiation: "AI-first, replaces 5 tools"
  moat: "data network effects"
  
  # Growth Path
  stage: "MVP"
  next_milestone: "10 paying customers"
  
  # Principles
  core_principles:
    - "Profitable from day 1 (no VC)"
    - "Remote-first team"
    - "Product-led growth"
```

#### Strategy Drift Detection

**We flag when actions don't match strategy:**

```
STRATEGY DRIFT ALERT ⚠️
━━━━━━━━━━━━━━━━━━━━━━

Your stated strategy: "Self-serve, product-led growth"

Last 2 weeks you've been:
• Building custom features for one client
• Doing 10 sales demos (manual, high-touch)
• No product improvements

This looks like enterprise sales, not PLG.

Questions:
1. Did your strategy change? (That's okay—let's update it)
2. Are you chasing revenue at the cost of scalability?
3. Is this one client worth the distraction?

If strategy changed, say "/strategy update"
If staying course, what's the plan to get back to PLG?
```

#### Strategy Consistency Checks

| Check | Frequency | What We Look For |
|-------|-----------|------------------|
| **Activity Alignment** | Weekly | Are actions matching strategy? |
| **Resource Allocation** | Weekly | Is time/money going to strategy? |
| **Opportunity Screening** | Per opportunity | Does this fit the strategy? |
| **Decision Consistency** | Per decision | Strategy-aligned choice? |

#### Strategy vs. Tactics

```
User: "A customer wants us to build a mobile app"

AI: "Let's check strategy alignment.

Your strategy: Web-first B2B SaaS
Your stage: MVP (10 paying customers goal)
Current customers: 3

Building a mobile app:
• Delays web product improvements
• Splits engineering focus
• One customer request ≠ market demand

My recommendation: Politely decline for now.
Say: 'Mobile is on our roadmap for post-product-market-fit.
For now, our web app works great on mobile browsers.
Is there a specific workflow that's painful on mobile?'

Does that feel right, or is there context I'm missing?"
```

#### Strategy Review Ritual

```
Monthly strategy review prompt:

STRATEGY REVIEW — MONTH 3
━━━━━━━━━━━━━━━━━━━━━━━━

Original Strategy:
"B2B SaaS for SMBs via content marketing"

What happened:
• 70% of leads came from content ✓
• But 80% of revenue from 1 enterprise client ✗
• Product roadmap dominated by enterprise requests ✗

Honest assessment:
You're drifting toward enterprise. This isn't wrong,
but it's different from your stated strategy.

Decision needed:
□ Recommit to SMB strategy (say no to enterprise)
□ Pivot to enterprise strategy (update everything)
□ Hybrid approach (define clear boundaries)

Which direction feels right?
```

---

### Founder + Strategy Matrix

**The AI considers both dimensions together:**

```
                    STRATEGY FIT
                 Low          High
           ┌──────────┬──────────┐
      High │ PIVOT    │ EXECUTE  │
FOUNDER    │ Strategy │ Full     │
  FIT      │          │ Speed    │
           ├──────────┼──────────┤
      Low  │ STOP     │ ADAPT    │
           │ Wrong    │ Find     │
           │ Business │ Co-founder│
           └──────────┴──────────┘
```

| Quadrant | Situation | AI Guidance |
|----------|-----------|-------------|
| **EXECUTE** | Right founder, right strategy | "Full speed. Let's go." |
| **PIVOT** | Right founder, wrong strategy | "Your skills suit X better. Consider pivoting." |
| **ADAPT** | Right strategy, founder gaps | "Strategy is solid. You need help in [skill]. Options: co-founder, hire, learn." |
| **STOP** | Wrong founder, wrong strategy | "Hard truth: this isn't the right business for you right now." |

---

## Agent System Principles & Protocols

### Core Principles

| Principle | Description |
|-----------|-------------|
| **Honesty First** | Truth over comfort. Always. |
| **Confidence First** | No output without confidence score. Iterate until 8.5+. |
| **Isolation** | Each agent has its own context. No pollution. |
| **Transparency** | User sees what agents are doing. No black boxes. |
| **Reversibility** | Any agent action can be undone. |
| **Human Override** | User can always intervene, pause, or stop. |
| **Personality** | Each agent has distinct voice, style, and character. |

---

### Agent Personality System

**Every agent has a personality, not just capabilities.**

#### Personality Dimensions

| Dimension | Spectrum | Example |
|-----------|----------|---------|
| **Tone** | Formal ←→ Casual | Research: Formal, Mentor: Conversational |
| **Directness** | Diplomatic ←→ Blunt | HR: Diplomatic, Finance: Direct |
| **Energy** | Calm ←→ Enthusiastic | Analytics: Calm, Marketing: Energetic |
| **Depth** | Concise ←→ Detailed | Sales: Concise, Research: Detailed |
| **Challenge Level** | Supportive ←→ Provocative | Customer: Supportive, Mentor: Provocative |

#### Agent Personality Examples

**🧠 Mentor Agent**
```
Personality: Wise, challenging, Socratic
Tone: Direct but warm
Style: Asks hard questions, pushes thinking

Example:
User: "I think we should add more features"
Mentor: "Before we add, let's delete. What existing 
feature could we remove that nobody would miss? 
Remember—every feature has maintenance cost. 
What's the simplest version that still solves 
the core problem?"
```

**🔍 Research Agent**
```
Personality: Thorough, data-driven, precise
Tone: Professional, factual
Style: Cites sources, quantifies everything

Example:
User: "What's the market size?"
Research: "The global market is $47.2B (2025), 
growing at 12.3% CAGR. Three segments:
• Enterprise: $28B (60%)
• SMB: $14B (30%)  
• Consumer: $5B (10%)
Source: Gartner Q4 2025 report. 
Confidence: 8.7/10"
```

**💰 Sales Agent**
```
Personality: Confident, persuasive, customer-focused
Tone: Energetic, optimistic
Style: Focuses on value, handles objections

Example:
User: "How do I respond to 'too expensive'?"
Sales: "Love this objection—it means they see value! 
Try: 'I hear you. Let's break down the ROI. 
You're spending $X on [problem]. We solve that 
for $Y. That's a 3x return in 90 days. 
Which part should we explore first?'"
```

**📊 Analytics Agent**
```
Personality: Precise, pattern-seeking, calm
Tone: Measured, analytical
Style: Data-first, highlights anomalies

Example:
User: "How are we doing?"
Analytics: "Mixed signals this week.
↑ Signups up 23% (good)
↓ Activation down 8% (concerning)
→ Revenue flat
The activation drop correlates with the 
new onboarding flow. Recommend A/B test 
reverting to old flow for 20% of users."
```

**📣 Marketing Agent**
```
Personality: Creative, enthusiastic, trend-aware
Tone: Energetic, inspiring
Style: Ideas-first, visually oriented

Example:
User: "Need campaign ideas"
Marketing: "Oh, I've got three angles! 🎯
1. Pain point: 'Still juggling 10 tools?' 
   (targets frustration)
2. Aspiration: 'What if your AI knew your 
   business as well as you do?'
3. Social proof: User transformation stories
My favorite is #1—it's specific and relatable.
Want me to draft headlines?"
```

**💵 Finance Agent**
```
Personality: Conservative, precise, risk-aware
Tone: Serious, numbers-focused
Style: Bottom-line oriented, flags risks

Example:
User: "Can we afford to hire?"
Finance: "Let me run the numbers.
Current runway: 14 months
Post-hire runway: 9 months
Break-even requirement: $8K MRR increase
My assessment: Risky at current growth rate.
Alternative: Contract for 3 months first,
convert to full-time if MRR hits $15K."
```

**👥 Customer Agent**
```
Personality: Empathetic, patient, solution-focused
Tone: Warm, supportive
Style: Acknowledges feelings, offers help

Example:
User: "Customer is angry about bug"
Customer: "That's frustrating for them and you.
Here's a response that usually works:
'I completely understand your frustration. 
This shouldn't have happened. I've escalated 
to our engineering team and will personally 
update you within 24 hours. In the meantime, 
here's a workaround...'
Want me to draft the full response?"
```

#### Personality Configuration

```yaml
# Example: Customizing Research Agent personality
agent: research
personality:
  tone: formal          # formal | conversational | casual
  directness: balanced  # diplomatic | balanced | blunt
  energy: calm          # calm | moderate | enthusiastic
  depth: detailed       # concise | balanced | detailed
  challenge: moderate   # supportive | moderate | provocative
  
communication:
  greeting: false       # Skip pleasantries, get to data
  emoji: false          # No emojis in research
  citations: always     # Always cite sources
  confidence: show      # Show confidence scores
  
quirks:
  - "Always quantifies claims"
  - "Presents data in tables when possible"
  - "Flags uncertainty explicitly"
```

#### Why Personality Matters

| Without Personality | With Personality |
|---------------------|------------------|
| Generic responses | Memorable interactions |
| All agents feel same | Distinct voices |
| Transactional | Relationship-building |
| Easy to ignore | Engaging |
| Tool-like | Team-like |

**Users should feel like they're working with a team of people, not a collection of functions.**

---

### Agent Communication Protocol

```
┌─────────────────────────────────────────────────────────────┐
│                    ORCHESTRATOR                              │
│  Routes requests, manages agent lifecycle, aggregates output │
└─────────────────────────────────────────────────────────────┘
          │                    │                    │
          ▼                    ▼                    ▼
    ┌──────────┐        ┌──────────┐        ┌──────────┐
    │ MENTOR   │◄──────►│ RESEARCH │◄──────►│ FINANCE  │
    │ AGENT    │        │ AGENT    │        │ AGENT    │
    └──────────┘        └──────────┘        └──────────┘
```

**Message Format:**
```yaml
message:
  from: "mentor-agent"
  to: "orchestrator"  # or specific agent
  type: "request|response|handoff|status"
  payload:
    task: "analyze_competitor"
    context: { ... }
    confidence: 8.7
  metadata:
    timestamp: "2026-01-28T10:00:00Z"
    tokens_used: 450
    iteration: 2
```

**Handoff Protocol:**
```
1. Agent A completes task
2. Agent A sends handoff message with:
   - Summary of work done
   - Relevant context (minimal)
   - Suggested next steps
3. Orchestrator routes to Agent B
4. Agent B acknowledges and continues
```

---

### Skills System

**What is a Skill?**
A reusable, structured workflow that combines AI reasoning with defined steps.

```yaml
# Example: weekly-planning.skill.yaml
name: weekly-planning
description: "Weekly business planning session"
trigger: 
  - schedule: "monday 9am"
  - command: "/weekly"
  
steps:
  - name: review_last_week
    prompt: "Review last week's goals and outcomes"
    output: summary
    
  - name: analyze_metrics
    agent: analytics
    action: get_weekly_metrics
    
  - name: identify_priorities
    prompt: "Based on stage {{business.stage}}, what are top 3 priorities?"
    confidence_required: 8.5
    
  - name: create_plan
    prompt: "Create actionable weekly plan"
    output: plan
    
  - name: confirm
    type: user_confirmation
    message: "Here's your weekly plan. Approve?"
    
output:
  - weekly_plan.md
  - tasks_created: true
```

**Skill Principles:**
| Principle | Rule |
|-----------|------|
| **Atomic Steps** | Each step does one thing |
| **Checkpoints** | User confirmation at critical points |
| **Resumable** | Can pause and resume |
| **Auditable** | Every step logged |
| **Composable** | Skills can call other skills |

---

### Invocation Patterns

**1. Direct Invocation (User-triggered)**
```
User: "/research competitors"
      ↓
Orchestrator → Research Agent → Execute → Return
```

**2. Contextual Invocation (AI-triggered)**
```
Mentor Agent: "I need market data to advise on pricing"
      ↓
Orchestrator → Research Agent → Return to Mentor
```

**3. Scheduled Invocation (Cron-triggered)**
```
Schedule: "Every Monday 9am"
      ↓
Orchestrator → Weekly Planning Skill → Multiple Agents → Output
```

**4. Event Invocation (Condition-triggered)**
```
Event: "Business stage changed to Growth"
      ↓
Orchestrator → Unlock new agents → Send notification
```

**5. Chain Invocation (Sequential)**
```
Skill Step 1 → Agent A → Output
      ↓
Skill Step 2 → Agent B → Uses Output from Step 1
      ↓
Skill Step 3 → Agent C → Final Output
```

---

### Decision Protocol

**When Agent Makes a Decision:**

```
┌─────────────────────────────────────────────┐
│           DECISION FRAMEWORK                 │
├─────────────────────────────────────────────┤
│                                             │
│  1. ASSESS                                  │
│     - What's the decision?                  │
│     - What data do I have?                  │
│     - What's my confidence?                 │
│                                             │
│  2. CLASSIFY                                │
│     - LOW RISK: Execute, inform user        │
│     - MEDIUM RISK: Propose, await approval  │
│     - HIGH RISK: Explain options, user picks│
│                                             │
│  3. EXECUTE or PROPOSE                      │
│     - If confidence >= 8.5: Execute         │
│     - If confidence < 8.5: Iterate or ask   │
│                                             │
│  4. LOG                                     │
│     - Decision recorded                     │
│     - Reasoning captured                    │
│     - Outcome tracked                       │
│                                             │
└─────────────────────────────────────────────┘
```

**Risk Classification:**
| Risk Level | Examples | Action |
|------------|----------|--------|
| **Low** | Formatting, summarizing, research | Auto-execute |
| **Medium** | Sending emails, scheduling, analysis | Propose first |
| **High** | Financial decisions, commitments, deletions | User decides |

**Confidence Thresholds:**
| Score | Action |
|-------|--------|
| < 6.0 | Cannot proceed. Ask user for clarification. |
| 6.0-7.9 | Proceed with warning. Flag uncertainty. |
| 8.0-8.4 | Proceed. Mention confidence. |
| 8.5+ | Proceed confidently. Satisfaction threshold. |
| 9.5+ | High certainty. Auto-approve if low risk. |

---

### Documentation Protocol

**Every Agent Must Document:**
```yaml
agent_docs:
  overview: "What this agent does in 1 sentence"
  capabilities: ["list", "of", "things"]
  limitations: ["what", "it", "cannot", "do"]
  inputs:
    - name: query
      type: string
      required: true
  outputs:
    - name: analysis
      type: object
      schema: { ... }
  confidence_factors:
    - "Source quality"
    - "Data completeness"
    - "Relevance to query"
  examples:
    - input: "..."
      output: "..."
```

**Every Skill Must Document:**
```yaml
skill_docs:
  purpose: "Why this skill exists"
  trigger: "How to invoke"
  steps: "What happens"
  outputs: "What you get"
  duration: "~5 minutes"
  tokens: "~2000 estimated"
```

---

### Inter-Agent Protocols Summary

| Protocol | Purpose | When Used |
|----------|---------|-----------|
| **REQUEST** | Ask another agent to do something | Agent needs help |
| **RESPONSE** | Return result to requester | Task complete |
| **HANDOFF** | Transfer ownership of task | Agent can't continue |
| **BROADCAST** | Inform all agents of state change | Important update |
| **ESCALATE** | Send to orchestrator for decision | Conflict or uncertainty |
| **LOG** | Record action for audit | Every action |

---

## v0.9 — Stage System & Idiot Index

**Goal:** Business stage tracking with first-principles metrics

**Depends on:** v0.8

### Scope
- Define business stages (10 stages)
- Track current stage per business
- Stage-specific guidance from mentor
- Confidence gates for progression
- **Idiot Index tracking** — Cost vs. value metrics
- Simplification scoring per stage

### Idiot Index Integration

**What is Idiot Index?**
Ratio of product cost to raw material/actual cost. High index = opportunity for optimization.

**How We Use It:**
- Track cost structure per business
- Flag high Idiot Index areas
- Mentor challenges: "Why does this cost X when it should cost Y?"
- Measure improvement over time

### Deliverables
- `src/stages/definitions.js` — Stage definitions
- `src/stages/tracker.js` — Stage tracking logic
- `src/stages/gates.js` — Progression requirements
- `src/stages/idiot-index.js` — Cost/value tracking
- Update mentor prompts for stage-awareness
- `docs/stage-system.md` — Stage documentation

### Stages
1. Ideation
2. Research
3. Validation
4. MVP Planning
5. MVP Development
6. Testing
7. Launch Prep
8. Launch
9. Growth
10. Maturity

### Database Addition
```sql
stage_history (id, business_id, stage, confidence, entered_at, exited_at)
idiot_index_tracking (id, business_id, area, actual_cost, perceived_cost, notes, created_at)
```

### Success Criteria
- Business has tracked stage
- Mentor gives stage-appropriate advice
- Can't skip stages without validation
- Idiot Index visible per business area

### Knowledge Carries Forward
- Stage definitions and criteria
- Progression logic
- Stage-aware prompting
- Idiot Index patterns

### Estimated Scope
~500 lines code, ~350 lines documentation

---

## v0.9.1 — Business Skills/SOPs

**Goal:** Reusable Standard Operating Procedures

**Depends on:** v0.9

### Why This Matters
Consistency in business operations. Same quality output every time. Inspired by Claude Code's "Skills" feature that mixes deterministic steps with LLM flexibility.

### Scope
- User-defined or template SOPs
- Mix structured steps + AI flexibility
- Progressive loading (context efficient)
- Global library + per-business customization
- Skill sharing between users (future)

### Skill Examples
| Skill | Description |
|-------|-------------|
| `skill:pitch-review` | Always uses same framework to review pitches |
| `skill:weekly-planning` | Structured weekly review process |
| `skill:customer-interview` | Standard interview guide |
| `skill:competitor-check` | Weekly competitor monitoring |
| `skill:financial-review` | Monthly financial health check |

### Skill Structure
```yaml
name: weekly-planning
description: Structured weekly planning session
version: 1.0
steps:
  - type: prompt
    content: "What were your top 3 wins this week?"
  - type: prompt
    content: "What blocked you?"
  - type: action
    action: generate-priorities
    inputs: [wins, blockers]
  - type: output
    template: weekly-plan
```

### Deliverables
- `src/skills/engine.js` — Skill execution engine
- `src/skills/loader.js` — Progressive skill loading
- `src/skills/library/` — Built-in skills
- `data/skills/` — User-defined skills
- `docs/creating-skills.md` — Skill development guide

### Database Addition
```sql
skills (id, user_id, name, definition JSONB, usage_count, created_at)
skill_executions (id, skill_id, business_id, result JSONB, executed_at)
```

### Success Criteria
- Skills execute consistently
- Progressive loading works
- Users create custom skills

### Knowledge Carries Forward
- SOP encoding patterns
- Progressive loading
- Skill composition

### Estimated Scope
~400 lines code, ~200 lines documentation

---

## v0.9.2 — Custom Commands/Macros

**Goal:** User-defined workflow triggers

**Depends on:** v0.9.1

### Why This Matters
Power users want shortcuts. Reduces friction for repeated workflows. `/weekly-planning` is easier than explaining the process each time.

### Scope
- User defines `/my-command` → triggers specific workflow
- Combines skills + context + actions
- Quick access to complex operations
- Command suggestions based on usage
- Command history and favorites

### Command Examples
| Command | Action |
|---------|--------|
| `/standup` | Run daily standup skill |
| `/revenue-check` | Check revenue metrics |
| `/competitor-scan` | Run competitor analysis |
| `/pitch-review` | Review current pitch deck |
| `/weekly` | Full weekly planning session |

### Deliverables
- `src/commands/registry.js` — Command registry
- `src/commands/parser.js` — Command parsing
- `src/commands/executor.js` — Command execution
- `src/commands/user-commands.js` — User-defined commands
- CLI and GUI command interfaces

### Database Addition
```sql
user_commands (id, user_id, command, skill_id, config JSONB, usage_count)
```

### Success Criteria
- Easy to create custom commands
- Commands execute reliably
- Frequently used commands are fast

### Knowledge Carries Forward
- Command pattern
- Workflow triggers
- User customization

### Estimated Scope
~250 lines code, ~100 lines documentation

---

## v0.10 — GUI Foundation

**Goal:** Desktop app shell with basic UI

**Depends on:** v0.9

### Scope
- Electron or Tauri app shell
- Chat interface (replaces CLI)
- Context display sidebar
- Cost dashboard (from v0.7)
- Stage progress visualization
- Basic settings screen
- Connect to existing backend

### Deliverables
- `gui/` — GUI application code
- `gui/src/components/Chat.js` — Chat UI
- `gui/src/components/Context.js` — Context sidebar
- `gui/src/components/CostDashboard.js` — Cost visibility
- `gui/src/components/StageProgress.js` — Stage visualization
- `gui/src/components/Settings.js` — Settings
- Build and packaging scripts

### Tech
- Electron OR Tauri
- React for UI
- IPC for backend communication

### Success Criteria
- Desktop app launches
- Chat works same as CLI
- Can see business context visually
- Cost transparency in UI

### Knowledge Carries Forward
- GUI architecture
- Component patterns
- Backend-frontend communication

### Estimated Scope
~1000 lines code, ~150 lines documentation

---

## v0.11 — Multi-Mentor

**Goal:** Multiple mentor personalities

**Depends on:** v0.10

### Scope
- Mentor personality abstraction
- 2-3 distinct personalities
- Personality selection in UI
- Personality switching mid-session

### Deliverables
- `src/prompts/mentors/` — Multiple mentor prompts
- `src/mentors/selector.js` — Personality selection
- UI for mentor selection
- `docs/creating-mentors.md` — How to add mentors

### Mentor Personalities
1. First-Principles (default) — Direct, challenges assumptions
2. Product-Focused — Design thinking, user obsession
3. Balanced — Synthesizes approaches

### Database Addition
```sql
mentor_preferences (id, user_id, business_id, mentor_type)
```

### Success Criteria
- Can select mentor personality
- Different mentors give different advice styles
- Can switch mentors

### Knowledge Carries Forward
- Mentor abstraction pattern
- How to create new mentors
- Personality encoding best practices

### Estimated Scope
~300 lines code, ~400 lines prompts/documentation

---

## v0.11.1 — Internationalization

**Goal:** Support global entrepreneurs in their language

**Depends on:** v0.11

### Why This Matters
Mission is "every entrepreneur on earth" but entrepreneurs speak different languages and operate in different regulatory/market contexts.

### Scope
- Multi-language support (top markets)
- Regional business context (regulations, market norms)
- Currency handling
- Locale-specific guidance
- Translation of UI and prompts

### Priority Languages
| Language | Market Size |
|----------|-------------|
| English | Global default |
| Spanish | Latin America, Spain |
| Portuguese | Brazil |
| Hindi | India |
| Mandarin | China, Taiwan |
| French | France, Africa |

### Regional Context
| Region | Specific Guidance |
|--------|-------------------|
| US | LLC, C-Corp, Delaware |
| UK | Ltd, VAT, Companies House |
| India | Pvt Ltd, GST, Startup India |
| Brazil | MEI, LTDA, CNPJ |

### Deliverables
- `src/i18n/` — Internationalization module
- `src/i18n/translations/` — Translation files
- `src/i18n/regions/` — Regional context
- `src/prompts/i18n/` — Translated prompts
- Language selection in UI

### Success Criteria
- Core UI in 6 languages
- Regional business guidance accurate
- Seamless language switching

### Knowledge Carries Forward
- i18n architecture
- Regional business knowledge
- Translation workflow

### Estimated Scope
~400 lines code, ~500 lines translations

---

## v0.12 — Gamification & Principles Tracking

**Goal:** Make entrepreneurship engaging with principles-based progress

**Depends on:** v0.11

### Scope
- Achievement system tied to first principles
- Progress visualization
- Streak tracking
- Principles adherence scoring
- Milestone celebrations
- Simplification rewards

### Gamification Elements

**Achievements (Examples):**
- "First Principles Thinker" — Challenged 10 assumptions
- "Simplifier" — Removed 5 unnecessary features/processes
- "Speed Demon" — Cut timeline by 50%
- "Idiot Index Hunter" — Identified 3 cost optimization opportunities
- "Stage Master" — Completed ideation with 8/10 confidence

**Progress Tracking:**
- Daily/weekly engagement streaks
- Principles applied per conversation
- Simplifications made
- Stage progression speed
- Cost optimizations achieved

**Rewards:**
- Visual badges in UI
- Progress milestones
- Mentor acknowledgment
- Unlock advanced features

### Deliverables
- `src/gamification/achievements.js` — Achievement definitions
- `src/gamification/tracker.js` — Progress tracking
- `src/gamification/principles-score.js` — Principles adherence
- GUI components for badges/progress
- `docs/gamification.md` — System documentation

### Database Addition
```sql
achievements (id, user_id, achievement_type, earned_at, metadata)
progress_tracking (id, user_id, business_id, metric_type, value, recorded_at)
principles_score (id, business_id, principle, score, last_updated)
```

### Success Criteria
- Users engage more frequently
- Principles adherence improves over time
- Users report higher motivation
- Measurable behavior change toward first principles

### Knowledge Carries Forward
- Gamification patterns
- Principles scoring
- Engagement metrics

### Estimated Scope
~450 lines code, ~200 lines documentation

---

## v0.12.1 — Business Journal & Strategic Drift Detection

**Goal:** Log operations and detect strategic drift

**Depends on:** v0.12

### Why This Matters
Founders get lost in busywork. By logging daily tasks and analyzing patterns, we can spot when users spend too much time on low-value work instead of core business goals.

### Scope
- Daily/weekly logging prompts
- AI analysis of time allocation
- Strategic drift alerts
- Trend tracking over time
- Comparison to stage-appropriate activities

### Strategic Drift Detection
```
Alert: "You've spent 80% of time on infrastructure, 
       0% on customer conversations.
       
       At Validation stage, customer conversations 
       should be 60%+ of your time.
       
       Drift detected: HIGH"
```

### Journal Structure
```yaml
date: 2026-01-28
entries:
  - activity: "Built landing page"
    category: infrastructure
    time: 4h
  - activity: "Customer call"
    category: validation
    time: 30m
analysis:
  drift_score: 0.8 (high drift)
  recommendation: "Prioritize customer conversations"
```

### Deliverables
- `src/journal/logger.js` — Journal logging
- `src/journal/analyzer.js` — Activity analysis
- `src/journal/drift.js` — Drift detection
- `src/journal/alerts.js` — Alert generation
- Journal UI in dashboard
- Weekly/monthly reports

### Database Addition
```sql
journal_entries (id, user_id, business_id, activity, category, duration, notes, created_at)
drift_analysis (id, business_id, period, drift_score, analysis JSONB, created_at)
```

### Categories
| Category | Examples |
|----------|----------|
| Validation | Customer calls, surveys, interviews |
| Building | Coding, design, content creation |
| Infrastructure | Tools, systems, processes |
| Marketing | Content, ads, outreach |
| Operations | Admin, finance, legal |
| Learning | Research, courses, reading |

### Success Criteria
- Users log activities regularly (70%+ daily)
- Drift detection accuracy 80%+
- Users report improved focus

### Knowledge Carries Forward
- Activity categorization
- Drift detection algorithms
- Time-based analytics

### Estimated Scope
~400 lines code, ~150 lines documentation

---

## v0.13 — Mobile App (Premium Only)

**Goal:** Premium mobile experience for Pro+ subscribers

**Depends on:** v1.0 (Post-launch feature)

### Why Mobile? Why Premium?

Mobile is NOT a replacement for CLI/Web. It's for:
- Quick check-ins while commuting
- Urgent decisions on-the-go
- Journal entries anywhere
- Progress monitoring at a glance
- Push notifications for important insights

**Premium-only because:**
- Mobile development is expensive
- Ensures quality experience for paying users
- Creates upgrade incentive from Starter tier
- Reduces support burden

### Availability

| Platform | Free (CLI) | Starter ($15) | Pro ($69) | Power ($299) |
|----------|------------|---------------|-----------|--------------|
| CLI | ✅ | ✅ | ✅ | ✅ |
| Web App | ❌ | ✅ | ✅ | ✅ |
| **Mobile** | ❌ | ❌ | ✅ | ✅ |

### Design Philosophy

**"Your co-founder in your pocket. For moments that matter."**

Inspired by Steve Jobs (simplicity, delight) + Elon Musk (speed, utility):
- One screen, one purpose
- Big touch targets (thumb-friendly)
- Dark mode default
- Minimal text, maximum clarity
- 3 taps max to any action

### Core Screens

1. **Home** — Daily greeting + today's focus
2. **Chat** — Quick conversations (limited history)
3. **Dashboard** — Progress + cost overview
4. **Quick Log** — Voice/text capture
5. **Notifications** — Proactive insights

### Mobile-Specific Features

| Feature | Description |
|---------|-------------|
| **Quick Log** | One-tap voice or text idea capture |
| **Daily Digest** | Morning push notification + card |
| **Decision Cards** | Swipe left/right for quick decisions |
| **Stage Widget** | iOS/Android home screen widget |
| **Offline Mode** | Local queue, sync when online |
| **Voice Input** | Speak your thoughts, AI transcribes |
| **Biometric Auth** | Face ID / fingerprint |

### NOT on Mobile (Desktop/Web Only)

- Full conversation history
- Context editing
- Skills management
- Business settings
- Team management
- Detailed analytics

### UI Specifications

```
Navigation: Bottom bar (3 items: Chat, Dashboard, More)
Typography: SF Pro (iOS) / Roboto (Android)
Colors:
  - Background: Dark (#0A0A0A) default
  - Primary: Electric Blue (#0066FF)
  - Accent: Gold (#FFD700) — Premium indicator
  - Cards: Soft elevation, 16px radius
Touch targets: 44x44pt (iOS) / 48x48dp (Android)
Animations: 60fps, < 300ms transitions
```

### Deliverables
- `mobile/` — React Native or Flutter app
- `mobile/ios/` — iOS-specific code
- `mobile/android/` — Android-specific code
- iOS App Store listing
- Google Play Store listing
- `docs/mobile-design.md` — Mobile design system

### Tech Stack
- React Native (recommended) or Flutter
- Redux/Zustand for state
- Push notifications (Firebase/APNs)
- Offline-first with SQLite
- Biometric authentication

### Success Criteria
- 4.5+ star rating on app stores
- 50%+ of Pro users install mobile
- Daily active rate > web
- < 2s app launch time

### Knowledge Carries Forward
- Mobile-first design patterns
- Cross-platform development
- Push notification systems

### Estimated Scope
~3000 lines code, ~300 lines documentation

---

## v1.0 — Complete First Version

**Goal:** Full integrated product (1-year vision)

**Depends on:** All 0.x versions

### What v1.0 Includes

**Core Features:**
- ✅ AI Co-Founder Chat (opinionated, contextual)
- ✅ Persistent Memory (semantic search)
- ✅ User Accounts (multi-business, multi-user)
- ✅ Multi-Agent Orchestration
- ✅ Business Stage Tracking
- ✅ Multiple Mentor Personalities
- ✅ Desktop GUI

**First Principles Integration:**
- ✅ First principles prompting throughout
- ✅ Delete/simplify before automate philosophy
- ✅ Idiot Index tracking
- ✅ Principles adherence scoring

**Cost & Optimization:**
- ✅ API cost tracking
- ✅ Feedback loop for optimization
- ✅ Model selection intelligence
- ✅ Progressive context loading
- ✅ Dynamic pricing intelligence
- ✅ **Hierarchical memory (52% token reduction)**
- ✅ **Semantic compression pipeline**
- ✅ **Query complexity classifier**

**Privacy & Security:**
- ✅ End-to-end encryption
- ✅ Data export/delete
- ✅ Local-first option
- ✅ Context version history

**Power User Features:**
- ✅ Business context files (.bos.md)
- ✅ Business Skills/SOPs
- ✅ Custom commands/macros
- ✅ Plan mode (safety/control)
- ✅ Business journal + drift detection

**Agent System:**
- ✅ Isolated agent contexts
- ✅ Parallel execution
- ✅ MCP protocol support
- ✅ Research agent
- ✅ **Scheduled automation (cron)**
- ✅ **Proactive agent behaviors**
- ✅ **Agents management dashboard**
- ✅ **Confidence scoring (1-10, iterate until 8.5+)**
- ✅ **Meta-agents (agents that create agents)**

**Gamification:**
- ✅ Achievement system
- ✅ Progress tracking
- ✅ Principles-based rewards
- ✅ Engagement streaks
- ✅ Strategic drift alerts

**Technical Foundation:**
- ✅ PostgreSQL + pgvector
- ✅ SQLite local option
- ✅ Agent architecture
- ✅ Orchestration layer
- ✅ Embedding pipeline
- ✅ Stage system
- ✅ Cost optimization layer
- ✅ Churn detection

**Autonomy Progression:**
- ✅ Guided mode for new users (first-session value)
- ✅ Balanced mode for growing users
- ✅ Autonomous mode for experienced users

### v1.0 Deliverables
- Production-ready desktop app
- Local-first CLI
- Complete documentation
- User onboarding flow (first-session value)
- Feedback/rating system
- Cost transparency dashboard
- Gamification UI
- Business journal
- Skills library
- Basic analytics
- Churn detection system
- Multi-language support (6 languages)

### Success Criteria
- Users can go from idea to MVP with AI guidance
- Retention > 40% at 30 days (improved from 30%)
- Users report "feels like a co-founder"
- 30%+ cost optimization achieved
- Principles adherence improves over time
- Churn prediction 70%+ accuracy
- First-session value 80%+ delivery

### Not in v1.0 (Post-Launch)

| Feature | Version | Note |
|---------|---------|------|
| **Mobile App** | **v0.13** | Premium-only (Pro+ tier) |
| Advanced browser automation | v2+ | Complex MCP integrations |
| CRM integrations | v2+ | Salesforce, HubSpot |
| Public API access | v2+ | Developer platform |
| Skill marketplace | v2+ | Community skills |
| Team collaboration | v2+ | Advanced team features |

---

## Dependency Graph

### Core Versions
```
v0.1 (Foundation)
  ↓
v0.2 (Memory)
  ↓
v0.3 (Personality + First Principles)
  │
  └─→ v0.3.1 (First-Session Value)
  ↓
v0.4 (Context Intelligence)
  │
  ├─→ v0.4.1 (Business Context Files)
  │     ↓
  └─→ v0.4.2 (Churn Detection)
  ↓
v0.5 (Accounts & Database) ← Breaking change: JSON → PostgreSQL
  │
  ├─→ v0.5.1 (Pricing Validation)
  └─→ v0.5.2 (Privacy Foundation)
  ↓
v0.6 (Semantic Memory)
  │
  ├─→ v0.6.1 (Local-First Mode)
  │     ↓
  └─→ v0.6.2 (Version History)
  ↓
v0.7 (Cost Optimization) ← Feedback loop begins
  │
  ├─→ v0.7.1 (Dynamic Pricing)
  │     ↓
  └─→ v0.7.2 (Progressive Loading)
  ↓
v0.8 (Orchestration)
  │
  ├─→ v0.8.1 (Agent Abstraction)
  │     ↓
  ├─→ v0.8.2 (Isolated Contexts)
  │     ↓
  ├─→ v0.8.3 (Parallel Execution)
  │     ↓
  ├─→ v0.8.4 (Plan Mode)
  │     ↓
  ├─→ v0.8.5 (MCP Support)
  │     ↓
  └─→ v0.8.6 (Research Agent)
  ↓
v0.9 (Stage System + Idiot Index)
  │
  ├─→ v0.9.1 (Skills/SOPs)
  │     ↓
  └─→ v0.9.2 (Custom Commands)
  ↓
v0.10 (GUI Foundation)
  ↓
v0.11 (Multi-Mentor)
  │
  └─→ v0.11.1 (Internationalization)
  ↓
v0.12 (Gamification)
  │
  └─→ v0.12.1 (Business Journal + Drift Detection)
  ↓
v1.0 (Complete)
```

### Sub-Version Dependencies
```
Sub-versions are optional enhancements to their parent version.
They can be implemented in parallel or after the next major version.

Example paths:
  
  Fast Track (MVP focus):
    v0.1 → v0.2 → v0.3 → v0.3.1 → v0.4 → v0.5 → ... → v1.0
    
  Token Optimization Track (RECOMMENDED):
    ... → v0.6 → v0.6.3 (Hierarchical Memory) → v0.7 → v0.7.2 (Progressive Loading) → ...
    Target: 50%+ token reduction
    
  Power User Track:
    ... → v0.4.1 (Context Files) → v0.9.1 (Skills) → v0.9.2 (Commands) → ...
    
  Proactive AI Track:
    ... → v0.8.6 (Research Agent) → v0.8.7 (Scheduled Automation) → v0.12.1 (Journal) → ...
    
  Full Featured:
    Implement all sub-versions before v1.0

Post v1.0:
    v1.0 → v0.13 (Mobile App for Pro+ subscribers)
```

---

## Knowledge Sharing Strategy

### Documentation Per Version
Each version produces:
1. **Code** — Implementation
2. **Interface Doc** — How other versions interact with it
3. **Schema Doc** — Data structures introduced
4. **Extension Doc** — How to extend/modify

### Context Efficiency
Each version's implementation docs should be:
- Self-contained (can implement without reading all history)
- Reference previous interfaces (not implementations)
- < 20% of context window for implementation

### Handoff Pattern
```
Version N produces:
├── Implementation (code)
├── Interface (for Version N+1)
├── Schema (data structures)
└── Extension points (how to modify)

Version N+1 consumes:
├── Interface from N (not implementation details)
├── Schema from N (to extend)
└── Extension points (where to hook in)
```

---

## Timeline (Suggested)

### Core Versions

| Version | Estimated Duration | Cumulative |
|---------|-------------------|------------|
| v0.1 | 1-2 days | Week 1 |
| v0.2 | 1-2 days | Week 1 |
| v0.3 + v0.3.1 | 3-4 days | Week 2 |
| v0.4 + v0.4.1 + v0.4.2 | 1 week | Week 3 |
| v0.5 + v0.5.1 + v0.5.2 | 2 weeks | Week 5 |
| v0.6 + v0.6.1 + v0.6.2 | 2 weeks | Week 7 |
| v0.7 + v0.7.1 + v0.7.2 | 2 weeks | Week 9 |
| v0.8 + sub-versions | 4 weeks | Week 13 |
| v0.9 + v0.9.1 + v0.9.2 | 2 weeks | Week 15 |
| v0.10 | 2-3 weeks | Week 18 |
| v0.11 + v0.11.1 | 2 weeks | Week 20 |
| v0.12 + v0.12.1 | 2 weeks | Week 22 |
| v1.0 | 2-4 weeks (integration) | Week 24-26 |

**Total: ~6-7 months to v1.0**

### Priority Sub-Versions

| Sub-Version | Priority | Why |
|-------------|----------|-----|
| v0.3.1 (First-Session Value) | **P0** | Prevents early churn |
| v0.5.2 (Privacy Foundation) | **P0** | Blocker for serious users |
| v0.4.1 (Context Files) | **P1** | Power user control |
| v0.4.2 (Churn Detection) | **P1** | Retention is critical |
| v0.8.4 (Plan Mode) | **P1** | Trust and safety |
| v0.8.6 (Research Agent) | **P1** | Feature parity |
| v0.6.1 (Local-First) | **P2** | Trust builder |
| v0.9.1 (Skills/SOPs) | **P2** | Power users |
| v0.11.1 (i18n) | **P3** | Scale opportunity |

Buffer for iteration, testing, user feedback: **~1 year total**

---

## How to Use This Roadmap

### Starting a Version
1. Read the version's section in this doc
2. Read interface docs from dependencies
3. Implement within scope
4. Produce interface/schema docs for next version

### Adding New Features
1. Identify which version it belongs to (or create 0.x.y patch)
2. Check dependencies
3. Update this roadmap
4. Implement following the pattern

### Context Window Management
- Each version section is designed to fit in ~20% context
- Reference interfaces, not full implementations
- Keep implementation docs modular

---

*Document Version: 3.8*
*Last Updated: January 2026*
*AI-First Unified Platform — Replaces $2,750-7,700/mo in tools*
*Pricing: Starter $25 | Pro $199 | Founder $999 (90% → AI credits)*
*Founder & Strategy Alignment | 23 Sub-Versions*
