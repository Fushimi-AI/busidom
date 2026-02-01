# Technical Architecture

## Overview

Business-OS is an **AI-first operating system** for SMEs and entrepreneurs. One platform that replaces Notion, Jira, Slack, and a dozen other tools.

This document describes the technical architecture, organized by version progression from v0.1 to v1.0.

---

## Core Design Principle: AI-First

Not AI added to legacy software. Intelligence built from the ground up.

| Old Approach | Business-OS Approach |
|--------------|---------------------|
| Tools + AI bolted on | AI-first architecture |
| Data scattered across apps | Unified data layer |
| Manual integrations | Native intelligence |
| 10+ subscriptions | One platform |

---

## Dual-Database Architecture

**The foundation of AI-first is AI-native data.**

```
┌─────────────────────────────────────────────────────────────┐
│                    DATA LAYER                                │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌─────────────────────┐    ┌─────────────────────┐         │
│  │   POSTGRESQL        │    │   PGVECTOR          │         │
│  │   (Structured)      │◄──►│   (Semantic)        │         │
│  │                     │    │                     │         │
│  │ • Users             │    │ • Memory embeddings │         │
│  │ • Businesses        │    │ • Context vectors   │         │
│  │ • Tasks             │    │ • Document chunks   │         │
│  │ • Relationships     │    │ • Similarity search │         │
│  │ • Permissions       │    │ • Agent knowledge   │         │
│  │ • Analytics         │    │                     │         │
│  └─────────────────────┘    └─────────────────────┘         │
│              │                        │                      │
│              └───────────┬────────────┘                      │
│                          │                                   │
│                          ▼                                   │
│              ┌─────────────────────┐                         │
│              │   UNIFIED QUERY     │                         │
│              │   (Precise + Relevant)                        │
│              └─────────────────────┘                         │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Why Both Databases?

| Query Type | Structured DB | Vector DB | Combined |
|------------|---------------|-----------|----------|
| "Tasks from last week" | ✅ Precise | ❌ | Precise |
| "Pricing discussions" | ❌ | ✅ Relevant | Relevant |
| "Pricing from last month" | ✅ Time filter | ✅ Semantic | **Precise + Relevant** |

### Data Flow

```
User Query: "What did we decide about pricing?"
    │
    ├──► Structured: Find recent conversations
    │
    ├──► Vector: Semantic search "pricing decisions"
    │
    └──► Combined: Ranked results with context
```

### What Each Powers

**Structured DB (PostgreSQL):**
- User accounts, authentication
- Business entities, relationships
- Task tracking, milestones
- Stage progression
- Metrics, analytics history
- Permissions, multi-user

**Vector DB (pgvector):**
- Semantic memory retrieval
- Context relevance scoring
- Progressive disclosure levels
- Agent-to-query matching
- Similar conversation finding
- Knowledge clustering

---

## Architecture by Version

### MVP Architecture (v0.1 — v0.4)

```
┌─────────────────────────────────────┐
│              CLI (v0.1)             │
│         User Input/Output           │
└─────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────┐
│          API Wrapper (v0.1)         │
│      OpenAI/Kimi Compatible         │
└─────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────┐
│      Mentor Prompt (v0.3)           │
│    System Prompt + Personality      │
└─────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────┐
│     Context Layer (v0.2 + v0.4)     │
│  JSON Storage + Auto-Extraction     │
└─────────────────────────────────────┘
```

**Tech Stack:**
- Node.js
- OpenAI-compatible API
- JSON file storage
- readline for CLI

---

### Foundation Architecture (v0.5 — v0.6)

```
┌─────────────────────────────────────┐
│              CLI (v0.1)             │
└─────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────┐
│         Auth Layer (v0.5)           │
│     User Registration/Login         │
└─────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────┐
│          API Wrapper                │
│      + Embedding Pipeline (v0.6)    │
└─────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────┐
│          Mentor Prompt              │
└─────────────────────────────────────┘
                  │
          ┌──────┴──────┐
          ▼             ▼
┌──────────────┐ ┌──────────────┐
│  PostgreSQL  │ │  Vector DB   │
│    (v0.5)    │ │   (v0.6)     │
│  Structured  │ │  Embeddings  │
└──────────────┘ └──────────────┘
```

**Tech Stack:**
- PostgreSQL (users, businesses, conversations)
- pgvector OR Pinecone (embeddings)
- bcrypt (auth)
- OpenAI embeddings API

---

### Intelligence Architecture (v0.7 — v0.8)

```
┌─────────────────────────────────────┐
│              CLI                    │
└─────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────┐
│         Auth Layer                  │
└─────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────┐
│    Cost Optimizer (v0.7)            │
│   API Tracking + Feedback Loop      │
└─────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────┐
│      Orchestrator (v0.8)            │
│   Intent Detection + Routing        │
└─────────────────────────────────────┘
                  │
     ┌────────────┼────────────┐
     ▼            ▼            ▼
┌─────────┐ ┌─────────┐ ┌─────────┐
│ Mentor  │ │Research │ │ Other   │
│ Agent   │ │ Agent   │ │ Agents  │
│ (v0.8)  │ │(future) │ │(future) │
└─────────┘ └─────────┘ └─────────┘
     │            │            │
     └────────────┼────────────┘
                  ▼
┌─────────────────────────────────────┐
│   Stage System + Idiot Index (v0.9) │
│   Tracking + Progression Gates      │
└─────────────────────────────────────┘
                  │
          ┌──────┴──────┐
          ▼             ▼
┌──────────────┐ ┌──────────────┐
│  PostgreSQL  │ │  Vector DB   │
└──────────────┘ └──────────────┘
```

**New Components:**
- Cost optimizer (API tracking, feedback loop)
- Orchestrator (agent routing)
- Agent abstraction layer
- Stage tracker + Idiot Index
- Progression gates

---

### Complete Architecture (v1.0)

```
┌─────────────────────────────────────────────────────────────┐
│                    USER INTERFACE                            │
│              CLI (v0.1) ──── GUI (v0.10)                    │
│           Custom Commands (v0.9.2), Plan Mode (v0.8.4)      │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      AUTH LAYER (v0.5)                       │
│        User Management, Sessions, Subscriptions, Multi-User  │
│              Privacy & Security (v0.5.2)                     │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                  COST OPTIMIZER (v0.7)                       │
│         API Tracking, Feedback Loop, Model Selection         │
│      Dynamic Pricing (v0.7.1), Progressive Loading (v0.7.2)  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   ORCHESTRATOR (v0.8)                        │
│         Intent Detection, Agent Routing, State Machine       │
│    Isolated Contexts (v0.8.2), Parallel Execution (v0.8.3)  │
│              Plan Mode (v0.8.4), MCP Support (v0.8.5)        │
└─────────────────────────────────────────────────────────────┘
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│  MENTOR AGENT   │ │ RESEARCH AGENT  │ │  MCP AGENTS     │
│  (v0.8+v0.11)   │ │   (v0.8.6)      │ │  (v0.8.5)       │
│ Multi-Persona   │ │ Market/Compete  │ │ Playwright,etc  │
└─────────────────┘ └─────────────────┘ └─────────────────┘
              │               │               │
              └───────────────┼───────────────┘
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   SKILLS ENGINE (v0.9.1)                     │
│        Reusable SOPs, Progressive Loading, Execution         │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   STAGE SYSTEM (v0.9)                        │
│      Stage Tracking, Idiot Index, Progression Gates          │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                 ALIGNMENT LAYER                              │
│         Founder Profile, Strategy Fit, Drift Detection       │
│    Honesty Protocol, Quality Gates, Anti-Pattern Detection   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                 GAMIFICATION (v0.12)                         │
│        Achievements, Principles Tracking, Streaks            │
│           Business Journal (v0.12.1), Drift Detection        │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   CONTEXT LAYER (v0.2-0.6)                   │
│     Memory Management, Semantic Search, Context Building     │
│   Context Files (v0.4.1), Version History (v0.6.2)          │
│       Churn Detection (v0.4.2), First-Session (v0.3.1)      │
└─────────────────────────────────────────────────────────────┘
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│   PostgreSQL    │ │   Vector DB     │ │  Local Storage  │
│   (v0.5)        │ │    (v0.6)       │ │   (v0.6.1)      │
│ Users, Business │ │  Embeddings     │ │ SQLite, Offline │
│  Subscriptions  │ │ Semantic Index  │ │  .bos.md Files  │
└─────────────────┘ └─────────────────┘ └─────────────────┘
```

### New Components (Sub-Versions)

| Component | Version | Function |
|-----------|---------|----------|
| First-Session Value | v0.3.1 | Guided onboarding, immediate deliverable |
| Context Files | v0.4.1 | User-editable .bos.md hierarchy |
| Churn Detection | v0.4.2 | Pre-churn signal monitoring |
| Privacy Foundation | v0.5.2 | Encryption, export, compliance |
| Local Storage | v0.6.1 | SQLite, offline mode |
| Version History | v0.6.2 | Context time machine |
| **Hierarchical Memory** | **v0.6.3** | **Temporal consolidation (52% token reduction)** |
| Dynamic Pricing | v0.7.1 | Value-based cost optimization |
| Progressive Loading | v0.7.2 | On-demand context, semantic compression |
| Agent Abstraction | v0.8.1 | Single-purpose interfaces |
| Isolated Contexts | v0.8.2 | Per-agent context windows |
| Parallel Execution | v0.8.3 | Concurrent agent/tool calls |
| Plan Mode | v0.8.4 | Approve before execute |
| MCP Support | v0.8.5 | Model Context Protocol |
| Research Agent | v0.8.6 | Market/competitor analysis |
| **Scheduled Automation** | **v0.8.7** | **Cron jobs, proactive agents** |
| **Agents Management** | **v0.8.8** | **Registry, confidence scoring, meta-agents** |
| Skills Engine | v0.9.1 | Reusable SOPs |
| Custom Commands | v0.9.2 | User-defined workflows |
| i18n | v0.11.1 | Multi-language support |
| Business Journal | v0.12.1 | Logging, drift detection |
| **Mobile App** | **v0.13** | **Premium-only (Pro+) mobile experience** |

### Alignment Components (Cross-Cutting)

| Component | Function |
|-----------|----------|
| **Founder Profile** | Skills, resources, motivations, constraints assessment |
| **Strategy Tracker** | Defined strategy, weekly drift detection |
| **Honesty Protocol** | No false hope, challenge bad ideas, admit uncertainty |
| **Quality Gates** | Must validate before stage progression |
| **Anti-Pattern Detection** | Solution searching, feature creep, vanity metrics |
| **Agent Personalities** | Distinct voice/style per agent |

---

## Database Schema (v0.5+)

### PostgreSQL Tables

```sql
-- Users (v0.5)
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Subscriptions (v0.5)
CREATE TABLE subscriptions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    tier VARCHAR(50) NOT NULL, -- 'free', 'starter', 'pro', 'power'
    business_limit INTEGER NOT NULL, -- 1, 3, 10
    credits_remaining INTEGER DEFAULT 0,
    started_at TIMESTAMP DEFAULT NOW(),
    expires_at TIMESTAMP,
    status VARCHAR(50) DEFAULT 'active'
);

-- Businesses (v0.5)
CREATE TABLE businesses (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    owner_id UUID REFERENCES users(id),
    name VARCHAR(255),
    type VARCHAR(100),
    stage VARCHAR(50) DEFAULT 'ideation',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Business Members (v0.5) - Multi-user support
CREATE TABLE business_members (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    business_id UUID REFERENCES businesses(id),
    user_id UUID REFERENCES users(id),
    role VARCHAR(50) NOT NULL, -- 'owner', 'cofounder', 'advisor', 'team', 'viewer'
    onboarded_at TIMESTAMP,
    invited_at TIMESTAMP DEFAULT NOW(),
    UNIQUE(business_id, user_id)
);

-- Conversations (v0.5)
CREATE TABLE conversations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    business_id UUID REFERENCES businesses(id),
    messages JSONB NOT NULL DEFAULT '[]',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Context (v0.5)
CREATE TABLE context (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    business_id UUID REFERENCES businesses(id) UNIQUE,
    data JSONB NOT NULL DEFAULT '{}',
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Embeddings (v0.6)
CREATE TABLE embeddings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    business_id UUID REFERENCES businesses(id),
    content TEXT NOT NULL,
    embedding VECTOR(1536),  -- pgvector
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMP DEFAULT NOW()
);

-- API Usage (v0.7) - Cost Optimization
CREATE TABLE api_usage (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    business_id UUID REFERENCES businesses(id),
    model VARCHAR(100) NOT NULL,
    tokens_in INTEGER,
    tokens_out INTEGER,
    cost DECIMAL(10,6),
    quality_rating INTEGER,  -- User feedback 1-5
    created_at TIMESTAMP DEFAULT NOW()
);

-- Prompt Performance (v0.7) - Feedback Loop
CREATE TABLE prompt_performance (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    prompt_hash VARCHAR(64),
    avg_quality DECIMAL(3,2),
    avg_cost DECIMAL(10,6),
    usage_count INTEGER DEFAULT 1,
    last_used TIMESTAMP DEFAULT NOW()
);

-- Stage History (v0.9)
CREATE TABLE stage_history (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    business_id UUID REFERENCES businesses(id),
    stage VARCHAR(50) NOT NULL,
    confidence INTEGER,
    entered_at TIMESTAMP DEFAULT NOW(),
    exited_at TIMESTAMP
);

-- Idiot Index Tracking (v0.9)
CREATE TABLE idiot_index_tracking (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    business_id UUID REFERENCES businesses(id),
    area VARCHAR(255) NOT NULL,  -- What area of business
    actual_cost DECIMAL(12,2),
    perceived_cost DECIMAL(12,2),
    notes TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Mentor Preferences (v0.11)
CREATE TABLE mentor_preferences (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    business_id UUID REFERENCES businesses(id),
    mentor_type VARCHAR(50) DEFAULT 'first-principles',
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Achievements (v0.12) - Gamification
CREATE TABLE achievements (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    achievement_type VARCHAR(100) NOT NULL,
    earned_at TIMESTAMP DEFAULT NOW(),
    metadata JSONB DEFAULT '{}'
);

-- Progress Tracking (v0.12) - Gamification
CREATE TABLE progress_tracking (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    business_id UUID REFERENCES businesses(id),
    metric_type VARCHAR(100) NOT NULL,  -- 'streak', 'principles_applied', etc.
    value INTEGER,
    recorded_at TIMESTAMP DEFAULT NOW()
);

-- Principles Score (v0.12) - Gamification
CREATE TABLE principles_score (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    business_id UUID REFERENCES businesses(id),
    principle VARCHAR(100) NOT NULL,  -- 'first_principles', 'simplify', 'idiot_index'
    score INTEGER,
    last_updated TIMESTAMP DEFAULT NOW()
);

-- Founder Profile (Alignment)
CREATE TABLE founder_profiles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    skills JSONB DEFAULT '{}',  -- {technical: 7, sales: 4, ...}
    resources JSONB DEFAULT '{}',  -- {time_weekly: "20 hours", runway: 12, ...}
    motivations JSONB DEFAULT '{}',  -- {primary: "independence", risk_tolerance: "moderate"}
    constraints TEXT[],
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Business Strategy (Alignment)
CREATE TABLE business_strategies (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    business_id UUID REFERENCES businesses(id),
    model VARCHAR(100),  -- 'B2B SaaS', 'E-commerce', etc.
    target_segment VARCHAR(100),
    acquisition_channel VARCHAR(100),
    differentiation TEXT,
    core_principles TEXT[],
    defined_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Strategy Drift Log (Alignment)
CREATE TABLE strategy_drift_log (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    business_id UUID REFERENCES businesses(id),
    drift_type VARCHAR(100),  -- 'activity', 'resource', 'opportunity'
    description TEXT,
    severity VARCHAR(50),  -- 'low', 'medium', 'high'
    resolved BOOLEAN DEFAULT FALSE,
    detected_at TIMESTAMP DEFAULT NOW()
);

-- Quality Gate Checks (Alignment)
CREATE TABLE quality_gate_checks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    business_id UUID REFERENCES businesses(id),
    gate_name VARCHAR(100),  -- 'problem_clarity', 'target_user', 'willingness_to_pay'
    stage VARCHAR(50),  -- 'idea', 'mvp', 'growth', 'scale'
    passed BOOLEAN,
    evidence TEXT,
    checked_at TIMESTAMP DEFAULT NOW()
);
```

---

## Component Details

### CLI (v0.1)

**Files:**
- `src/cli.js` — Input/output handling
- `src/api.js` — LLM API wrapper

**Interface:**
```javascript
// Input
readline.question('You: ', (input) => ...)

// Output
console.log('AI: ', response)
```

---

### Memory (v0.2)

**Files:**
- `src/memory.js` — Save/load functions
- `data/context.json` — Storage

**Interface:**
```javascript
function loadContext() → Context
function saveContext(context) → void
function clearContext() → void
function addToHistory(context, role, content) → Context
```

**Context Schema:**
```javascript
{
  business_name: string | null,
  stage: string,
  challenge: string | null,
  history: [{ role: string, content: string, timestamp: string }]
}
```

---

### Mentor Prompt (v0.3)

**Files:**
- `src/prompts/mentor.js` — System prompt

**Interface:**
```javascript
const MENTOR_SYSTEM_PROMPT = `...`
const CONTEXT_TEMPLATE = `...`

function buildPrompt(userMessage, context) → messages[]
```

---

### Extractor (v0.4)

**Files:**
- `src/extractor.js` — Info extraction

**Interface:**
```javascript
function extractBusinessInfo(userMessage, aiResponse, context) → Context
```

---

### Auth (v0.5)

**Files:**
- `src/auth/register.js`
- `src/auth/login.js`
- `src/auth/session.js`

**Interface:**
```javascript
function register(email, password) → User
function login(email, password) → Session
function validateSession(token) → User | null
```

---

### Vector Search (v0.6)

**Files:**
- `src/embeddings/generate.js`
- `src/vector/client.js`
- `src/vector/search.js`

**Interface:**
```javascript
function generateEmbedding(text) → vector
function storeEmbedding(businessId, content, embedding) → void
function searchSimilar(businessId, query, limit) → results[]
```

---

### Orchestrator (v0.7)

**Files:**
- `src/orchestrator/router.js`
- `src/orchestrator/state.js`

**Interface:**
```javascript
function routeRequest(input, context) → { agent: string, params: object }
function handleResponse(agentResponse, context) → Context
```

---

### Agent Base (v0.7)

**Files:**
- `src/agents/base.js`
- `src/agents/mentor.js`
- `src/agents/registry.js`

**Interface:**
```javascript
class Agent {
  constructor(config)
  async process(input, context) → response
  getName() → string
}

function registerAgent(name, agent) → void
function getAgent(name) → Agent
```

---

### Stage System (v0.8)

**Files:**
- `src/stages/definitions.js`
- `src/stages/tracker.js`
- `src/stages/gates.js`

**Interface:**
```javascript
const STAGES = ['ideation', 'research', ...]

function getCurrentStage(businessId) → Stage
function checkProgression(businessId) → { canProgress: boolean, confidence: number }
function advanceStage(businessId) → Stage
```

---

## Business Model: Open Core

### Open Source (CLI) — Free

- Core brain/engine
- BYOK (Bring Your Own Key)
- CLI interface
- Full functionality
- User controls costs and data
- Builds community and trust

### Subscription (GUI + Credits)

| Tier | Price | Users | Businesses | Value vs. |
|------|-------|-------|------------|-----------|
| **Starter** | $25/mo | 1 | 1 | < 1 business book |
| **Pro** | $199/mo | 1 | 1-3 | < 1 hr consultant |
| **Founder** | $999/mo | 1 | Up to 10 | < 1 day fractional exec |

### ROI Perspective

**What you're replacing:**
- Part-time consultant: $2,000-5,000/mo
- Market research tools: $200-500/mo
- Business coach: $500-2,000/mo
- Notion + Jira + Slack: $50-200/mo
- **Total: $2,750-7,700/mo**

### Economics

- **10% profit margin** — We keep 10%
- **90% to credits** — Passes through to AI usage
- Transparent, value-aligned pricing

### Multi-User Support

All tiers support adding human stakeholders:
- Co-founders
- Advisors
- Team members
- Investors (view-only)

**Short onboarding** for added users — Quick context download so they contribute immediately. The AI co-founder serves the whole team.

---

## Tech Stack Summary

| Component | MVP (v0.1-0.4) | Production (v0.5+) |
|-----------|----------------|-------------------|
| Runtime | Node.js | Node.js |
| Database | JSON file | PostgreSQL |
| Vector DB | — | pgvector / Pinecone |
| Auth | — | bcrypt + JWT |
| LLM | OpenAI API | Multi-provider |
| UI | CLI | CLI + Electron/Tauri |

---

## AI Model Integration

### Supported Models
- OpenAI (GPT-4, GPT-4 Turbo)
- **Kimi K2.5 (default, cost-effective)**
- Claude (Opus, Sonnet)
- Future: Gemini, DeepSeek

### Model Routing (v0.7+)
- Simple tasks → Lighter models
- Complex analysis → Heavier models
- Coding → Specialized coding agents (see below)

---

## Coding Agent Integration

### Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    CODING AGENT LAYER                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   ┌─────────────────────┐    ┌─────────────────────┐        │
│   │    KIMI CODE        │    │    CLAUDE CODE      │        │
│   │    (Default)        │    │    (Alternative)    │        │
│   │                     │    │                     │        │
│   │  • Agent Swarm      │    │  • Sequential       │        │
│   │  • 100 parallel     │    │  • Deep reasoning   │        │
│   │  • 1,500 tool calls │    │  • Faster tokens    │        │
│   │  • 4.5x faster      │    │                     │        │
│   │  • 10x cheaper      │    │                     │        │
│   │                     │    │                     │        │
│   │  Via: Kimi Agent    │    │  Via: CLI wrapper   │        │
│   │  SDK (Node.js)      │    │                     │        │
│   └─────────────────────┘    └─────────────────────┘        │
│                                                              │
│   CLI: bos [command] --agent=kimi (default) | --agent=claude│
└─────────────────────────────────────────────────────────────┘
```

### Default: Kimi Code (Parallel Agents)

**Why Kimi Code as Default:**
- **10x cheaper** than Claude Code ($2.50 vs $15/M output tokens)
- **4.5x faster** for complex tasks via parallel agent execution
- **Native Node.js SDK** for seamless integration
- **100 sub-agents** working simultaneously
- **1,500 tool calls** in parallel
- **Open source** (Apache 2.0)

**Parallel-Agent Reinforcement Learning (PARL):**
- Orchestrator decomposes tasks into parallelizable subtasks
- Specialized sub-agents (code generator, test writer, debugger)
- Dynamic agent creation without predefined workflows

### Alternative: Claude Code

**When to Use:**
- Time-critical single-file fixes (faster token generation)
- Complex debugging requiring deep reasoning
- User preference via `--agent=claude`

### Agent Selection

| Task Type | Default Agent | Rationale |
|-----------|---------------|-----------|
| Multi-file refactor | Kimi Code | Parallel agents excel |
| Codebase analysis | Kimi Code | Parallel scanning |
| Test generation | Kimi Code | Fully parallelizable |
| Single file edit | Kimi Code | Cost savings |
| Complex debugging | Claude Code | Deep reasoning |
| Time-critical fix | Claude Code | Faster tokens |

### Integration Points

**v0.5:** Add Kimi Agent SDK dependency
**v0.8:** Full coding agent integration
**v0.8.1:** Claude Code as alternative
**v0.8.2:** Task-based auto-selection

See [coding-agents.md](./coding-agents.md) for full strategy.

---

## Security Considerations

### MVP (v0.1-0.4)
- Local storage only
- User manages API keys
- No auth needed

### Production (v0.5+)
- Password hashing (bcrypt)
- Session tokens (JWT)
- Input validation
- Rate limiting
- Encrypted API key storage

---

## Deployment

### MVP
- Local only (`npm start`)
- No deployment needed

### Production
- CLI: npm package distribution
- GUI: Platform-specific installers
- Backend: Cloud hosting (if needed)

---

See [ROADMAP_DETAILED.md](../../ROADMAP_DETAILED.md) for implementation timeline.
