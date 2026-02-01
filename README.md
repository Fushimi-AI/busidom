# Busidom

> **AI co-founder that tracks your startup commitments, holds you accountable, and automates workflows - local-first, open source.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0-blue)](https://www.typescriptlang.org/)
[![Node](https://img.shields.io/badge/Node-18+-green)](https://nodejs.org/)

## What is Busidom?

Busidom is an **ambient AI co-founder** specifically designed for startup founders. Unlike generic AI assistants, Busidom:

- 🎯 **Proactively holds you accountable** - Tracks what you said you'd do and follows up intelligently
- 🤖 **Works in the background** - Always-on monitoring for business signals (competitors, mentions, metrics)
- 🧠 **Remembers your business context** - Stage-aware advice (idea → validation → MVP → growth)
- ⚡ **Autonomous execution** - Dynamic skill generation, automated workflows

**The difference**: Most AI assistants wait for you to ask. Busidom anticipates your needs and keeps you on track.

## Core Philosophy: Ambient Computing

Busidom isn't a chat interface you visit - it's an AI that **lives with you**:

1. **Proactive, Not Reactive** - "You said you'd talk to 10 customers this week. How's that going?"
2. **Background, Not Foreground** - Monitors competitor pricing, customer mentions while you work
3. **Context-Aware** - Different advice for idea stage vs growth stage
4. **Autonomous** - Generates custom code on-the-fly, executes workflows without hand-holding

## Key Features (v1.0 - Open Source CLI)

### 🎯 Proactive Accountability
- Parses commitments from natural conversations
- Intelligent follow-up scheduling (early check, deadline, overdue)
- Contextual check-in messages (not robotic reminders)
- Learns optimal timing per user

### 🔍 Always-On Monitoring
- Task-based monitoring (< 50MB RAM, < 5% CPU)
- Tracks: competitor pricing, social mentions, market changes
- Semantic change detection (not just literal diffs)
- Intelligent alerts (only when actionable)

### 🛠️ Dynamic Agent Skills
- Generates custom code on-the-fly based on task needs
- No pre-built skill library needed - infinite extensibility
- Sandboxed execution with security validation
- Auto-caching for reuse

### 🤖 Multi-Agent System
- **Mentor Agent** - Opinionated guidance, tough love, specific playbooks
- **Research Agent** - Deep web research, competitive analysis
- **Orchestrator** - Delegates tasks to specialized agents

### 📋 Workflow Automation
- YAML-based workflow definitions
- State machine execution
- Integration with dynamic skills and agents
- Event-driven triggers

### 🗄️ Local-First Architecture
- SQLite for storage (zero config, portable)
- Local vector search (privacy, no API calls)
- Full functionality offline
- BYOK (Bring Your Own Keys)

## Installation

```bash
npm install -g busidom
```

## Quick Start

```bash
# Initialize
busidom init

# Start chatting
busidom chat

# View your commitments
busidom accountability list

# Add a monitoring task
busidom monitor add

# View scheduled workflows
busidom scheduler status
```

## Documentation

- 📖 [Product Strategy](./roadmap/PRODUCT_STRATEGY.md)
- 🗺️ [Complete Roadmap](./roadmap/MASTER_TRACKER_V2.md)
- 📋 [Roadmap Summary](./roadmap/ROADMAP_SUMMARY.md)
- 🧪 [Test Plan](./TEST_PLAN.md)

## Architecture

Busidom is built with:

- **Language**: TypeScript
- **Runtime**: Node.js 18+
- **Storage**: SQLite (better-sqlite3)
- **Vector Search**: sqlite-vec or ChromaDB (local)
- **LLM**: OpenAI, Anthropic, Kimi (pluggable)
- **Automation**: node-cron, state machines

### Project Structure

```
busidom/
├── src/
│   ├── core/              # Shared business logic
│   │   ├── agents/        # Multi-agent system
│   │   ├── accountability/ # Commitment tracking
│   │   ├── monitoring/    # Always-on monitoring
│   │   ├── workflows/     # Workflow engine
│   │   └── memory/        # Semantic memory
│   ├── cli/               # CLI interface
│   └── storage/           # SQLite layer
└── roadmap/               # Complete feature specs
```

## Roadmap

**Phase 0-1** (Week 1-4): Foundation + MVP Core
- ✅ Project setup
- ✅ Chat interface + mentor personality
- ✅ Session memory

**Phase 2-3** (Week 5-8): Storage + Intelligence
- ✅ SQLite setup
- ✅ Vector search
- ✅ Semantic memory

**Phase 4-5** (Week 9-12): Agents + Automation
- ✅ Multi-agent system
- ✅ Dynamic skills
- ✅ Proactive accountability
- ✅ Always-on monitoring
- ✅ Workflow engine

**Phase 6** (Week 13-14): Polish + Launch
- 🚀 CLI v1.0 Release

See [MASTER_TRACKER_V2.md](./roadmap/MASTER_TRACKER_V2.md) for detailed feature breakdown (62 features total).

## Contributing

We welcome contributions! Please see [DEVELOPMENT_FRAMEWORK.md](./DEVELOPMENT_FRAMEWORK.md) for guidelines.

### Development Setup

```bash
# Clone repository
git clone https://github.com/Fushimi-AI/busidom.git
cd busidom

# Install dependencies
npm install

# Run in development mode
npm run dev

# Run tests
npm test

# Build
npm run build
```

## Paid Version (Busidom Pro)

For non-technical founders who need web/mobile access:

- 🌐 **Web App** - Modern UI with real-time sync
- 📱 **Mobile Apps** - iOS + Android with push notifications
- ☁️ **Cloud Sync** - Multi-device support
- 👥 **Team Features** - Collaboration and shared context
- 🔐 **Managed Infrastructure** - We handle keys, hosting, scaling

**Pricing**: $25-999/mo (includes AI credits)

Repository: [busidom-pro](https://github.com/Fushimi-AI/busidom-pro) (private)

## Why Busidom vs Generic AI?

| Feature | ChatGPT/Claude | ClawdBot | **Busidom** |
|---------|---------------|----------|-------------|
| **Focus** | General | General | **Startup-specific** |
| **Advice** | Generic | Generic | **Stage-aware, opinionated** |
| **Accountability** | None | Generic reminders | **Business commitments** |
| **Monitoring** | None | Not core | **Task-based, business signals** |
| **Skills** | Fixed | Marketplace | **Dynamic generation** |
| **Deployment** | Cloud | Self-hosted | **Local-first + Cloud** |

## License

MIT License - see [LICENSE](./LICENSE) for details.

## Community

- **GitHub**: [Fushimi-AI/busidom](https://github.com/Fushimi-AI/busidom)
- **Discussions**: [GitHub Discussions](https://github.com/Fushimi-AI/busidom/discussions)
- **Issues**: [Bug Reports & Features](https://github.com/Fushimi-AI/busidom/issues)

## Acknowledgments

Built with inspiration from:
- ClawdBot - Proactive AI patterns
- AutoGPT - Autonomous agent architecture
- LangChain - Agent frameworks

---

**🤖 Generated with [Claude Code](https://claude.com/claude-code)**

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
