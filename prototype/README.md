# Business-OS Prototype

**Your AI co-founder in the terminal.**

Direct. Opinionated. Pushes you to build.

---

## Quick Start

```bash
# 1. Set your API key
export OPENAI_API_KEY=your-key-here

# OR for Kimi K2.5 (default, 10x cheaper):
export KIMI_API_KEY=your-key-here
export KIMI_API_BASE=https://api.moonshot.ai/v1
export BOS_MODEL=kimi-k2.5

# 2. Install and run
cd prototype
npm install
npm start
```

---

## Coding Agents (Post-MVP)

Business-OS uses AI coding agents for development tasks:

**Default: Kimi Code** (Parallel Agents)
- Up to 100 sub-agents working simultaneously
- 4.5x faster for complex tasks
- 10x cheaper than alternatives

**Alternative: Claude Code**
- Faster token generation
- Deep reasoning for complex debugging

```bash
# Refactor with Kimi Code (default)
bos refactor src/

# Refactor with Claude Code
bos refactor src/ --agent=claude
```

See [coding-agents.md](../ideation/tech-stack/coding-agents.md) for full strategy.

---

## What This Is

An AI co-founder that:
- **Challenges your thinking** — Not a yes-machine
- **Remembers your business** — Context persists across sessions
- **Pushes action** — Direct guidance, no fluff
- **Uses first-principles** — Breaks down problems to fundamentals
- **Asks "can we delete this?"** — Before optimizing anything
- **Simplifies before automating** — Complexity is the enemy

---

## What This Is NOT

- ❌ A finished product (this is MVP)
- ❌ A replacement for doing the work
- ❌ A feel-good chatbot that agrees with everything
- ❌ Generic AI advice

---

## Commands

```
bos              - Start conversation
bos --clear      - Clear history and start fresh
bos --help       - Show help

During chat:
/clear           - Clear history
/context         - Show current context
/quit            - Exit
```

---

## The Philosophy

> "Stop planning. Start building. Ship something. Learn. Iterate."

This tool exists to push you to take action—not to plan forever.

---

## Why This Exists

90% of startups fail because founders lack guidance, not because they lack effort. Access to great mentors and co-founders is gatekept.

This prototype tests one hypothesis: **Can an opinionated AI co-founder provide better guidance than generic AI chat?**

---

## Feedback

Using this? We want to hear from you.
- What worked?
- What didn't?
- What would make you come back?

---

## License

MIT
