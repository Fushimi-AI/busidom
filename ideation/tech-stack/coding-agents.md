# Coding Agents Strategy

**Default:** Kimi Code (Parallel Agents)  
**Alternative:** Claude Code  
**Decision Date:** Jan 29, 2026

---

## Overview

Business-OS uses AI coding agents for development tasks. This document defines the strategy for selecting and integrating coding sub-agents.

**Key Decision:** Kimi Code is the **default** coding sub-agent due to its parallel agents feature (Agent Swarm), with Claude Code available as an alternative.

---

## Why Parallel Agents Matter

Traditional AI coding assistants process tasks sequentially. Kimi K2.5's Agent Swarm changes this:

```
Traditional (Claude Code):
┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐
│File1│ → │File2│ → │File3│ → │Tests│ = 9 minutes
└─────┘    └─────┘    └─────┘    └─────┘

Kimi Code (Parallel):
┌─────┐
│File1│─┐
└─────┘ │
┌─────┐ │
│File2│─┼─→ ┌───────┐ = 2 minutes
└─────┘ │   │Combine│
┌─────┐ │   └───────┘
│File3│─┤
└─────┘ │
┌─────┐ │
│Tests│─┘
└─────┘
```

**Result:** 4.5x faster for complex, parallelizable tasks.

---

## Comparison Matrix

| Factor | Kimi Code | Claude Code |
|--------|-----------|-------------|
| **Default** | ✅ Yes | No |
| **Cost (Jan 2026)** | $0.60/$3.00 per M tokens | $5/$25 per M tokens |
| **Cost Ratio** | **~8x cheaper** | Premium |
| **Free Tier** | 3 agentic tasks/week | None |
| **Parallel Agents** | Up to 100 agents | Sequential only |
| **Tools per Agent** | 1,500+ | Limited |
| **Max Tool Calls** | 1,500 parallel | Sequential |
| **Speed (Complex)** | 4.5x faster | Baseline |
| **Speed (Simple)** | ~34 tok/sec | ~91 tok/sec |
| **Context Window** | 256K tokens | 200K tokens |
| **Node.js SDK** | Native | CLI wrapper |
| **License** | Apache 2.0 | Proprietary |
| **IDE Integration** | VSCode, Cursor, Zed | VSCode, Cursor |
| **Video Input** | ✅ Video-to-code | Image only |
| **Production Use** | Moonshot internal | **80-100% of Anthropic code** |

---

## When to Use Each Agent

### Use Kimi Code (Default) When:

- ✅ Multi-file refactoring
- ✅ Codebase-wide analysis
- ✅ Test suite generation
- ✅ Documentation generation
- ✅ Code migration tasks
- ✅ Bulk file operations
- ✅ Cost-sensitive operations
- ✅ **Video-to-code conversion** (screen recordings → working sites)
- ✅ **Website cloning** from visual examples

### Use Claude Code (Alternative) When:

- ⚡ Time-critical single-file fixes
- 🧠 Complex debugging requiring deep reasoning
- 🎯 Accuracy-critical code generation
- 💬 Interactive coding sessions with fast feedback

### Decision Tree

```
Is the task parallelizable?
├── Yes → Multi-file? → Kimi Code
├── Yes → Test generation? → Kimi Code  
├── Yes → Codebase analysis? → Kimi Code
├── No → Time-critical? → Claude Code
├── No → Deep debugging? → Claude Code
└── Uncertain → Default to Kimi Code (cheaper)
```

---

## Unique Kimi Code Capabilities

### Video-to-Code (Novel Feature)

Unlike traditional AI models that only convert images to code, Kimi K2.5 can process **video inputs**:

```
Screen Recording → Frame Analysis → Context Understanding → Code Generation
```

**Real-World Example:**
- **Input:** 2-minute screen recording of Anthropic's website
- **Output:** Fully functional website replica
- **Time:** 25 minutes
- **Prompts:** 1 ("Create an exact replica of this website")

**How It Works:**
1. Analyzes each frame in the video
2. Understands pixel-level details across temporal sequences
3. Infers user interactions, animations, and transitions
4. Generates complete front-end code (HTML, CSS, JavaScript)
5. Maintains design fidelity across components

**Why This Matters:**
- **More intuitive** than describing requirements in text
- **Faster iteration** - show instead of tell
- **Perfect for prototyping** from existing examples
- **Ideal for front-end work** where visual fidelity matters

**Business-OS Use Cases:**
- Clone competitor interfaces for analysis
- Recreate design mockups from Figma recordings
- Generate UI from user testing videos
- Build prototypes from whiteboard sessions (video recorded)

### Real-World Validation

**Anthropic's Production Use (Jan 2026):**
- **80-100% of Anthropic's production code** is now built using Claude Code
- Multiple agent instances working in parallel
- Validates that parallel coding agents are production-ready
- Not experimental - actively replacing human developers for routine tasks

**This proves:**
- Multi-agent coding is mature technology
- Cost-effective for production workloads
- Quality meets professional standards
- Kimi Code's parallel approach is the future

---

## Integration Architecture

### System Design

```
┌─────────────────────────────────────────────────────────────┐
│                    BUSINESS-OS CLI                          │
│                    bos [command] --agent=<kimi|claude>      │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    CODING AGENT ROUTER                      │
│                                                              │
│   function selectAgent(task, userPreference) {              │
│     if (userPreference) return userPreference;              │
│     if (task.isParallelizable) return 'kimi-code';          │
│     if (task.isTimeCritical) return 'claude-code';          │
│     return 'kimi-code'; // Default                          │
│   }                                                          │
└─────────────────────────────────────────────────────────────┘
                              │
              ┌───────────────┴───────────────┐
              ▼                               ▼
┌─────────────────────────┐     ┌─────────────────────────┐
│      KIMI CODE          │     │     CLAUDE CODE         │
│                         │     │                         │
│  ┌───────────────────┐  │     │  ┌───────────────────┐  │
│  │ Kimi Agent SDK    │  │     │  │ Claude CLI        │  │
│  │ (Node.js native)  │  │     │  │ (Shell wrapper)   │  │
│  └───────────────────┘  │     │  └───────────────────┘  │
│           │             │     │           │             │
│           ▼             │     │           ▼             │
│  ┌───────────────────┐  │     │  ┌───────────────────┐  │
│  │ Agent Swarm       │  │     │  │ Sequential        │  │
│  │ Orchestrator      │  │     │  │ Execution         │  │
│  └───────────────────┘  │     │  └───────────────────┘  │
│           │             │     │           │             │
│     ┌─────┼─────┐       │     │           │             │
│     ▼     ▼     ▼       │     │           ▼             │
│  ┌─────┬─────┬─────┐    │     │     ┌─────────┐        │
│  │Sub 1│Sub 2│Sub N│    │     │     │ Claude  │        │
│  │Agent│Agent│Agent│    │     │     │ Sonnet  │        │
│  └─────┴─────┴─────┘    │     │     └─────────┘        │
│                         │     │                         │
└─────────────────────────┘     └─────────────────────────┘
```

### Kimi Code Integration

**Via Kimi Agent SDK (Node.js):**

```javascript
// src/agents/coding/kimi-code.js
import { KimiAgent } from 'kimi-agent-sdk';

export class KimiCodeAgent {
  constructor(config) {
    this.agent = new KimiAgent({
      apiKey: config.apiKey || process.env.KIMI_API_KEY,
      model: 'k2.5',
      agentSwarm: true,
      maxAgents: config.maxAgents || 50
    });
  }

  async refactor(files, instructions) {
    return this.agent.execute({
      task: 'refactor',
      files,
      instructions,
      parallelism: 'auto'
    });
  }

  async generateTests(files) {
    return this.agent.execute({
      task: 'test-generation',
      files,
      parallelism: 'max'  // Tests can be fully parallel
    });
  }

  async analyze(directory) {
    return this.agent.execute({
      task: 'codebase-analysis',
      directory,
      parallelism: 'auto'
    });
  }
}
```

**Via CLI (ACP Protocol):**

```bash
# Start Kimi as ACP server
kimi --acp --thinking

# IDE connects automatically via ACP
# Supports: VSCode, Cursor, Zed, JetBrains
```

### Claude Code Integration

**Via CLI wrapper:**

```javascript
// src/agents/coding/claude-code.js
import { spawn } from 'child_process';

export class ClaudeCodeAgent {
  async execute(task, files, instructions) {
    return new Promise((resolve, reject) => {
      const process = spawn('claude', [
        'code',
        '--task', task,
        '--files', files.join(','),
        '--instructions', instructions
      ]);
      
      let output = '';
      process.stdout.on('data', (data) => output += data);
      process.on('close', (code) => {
        if (code === 0) resolve(output);
        else reject(new Error(`Claude Code exited with ${code}`));
      });
    });
  }
}
```

---

## Configuration

### Environment Variables

```bash
# Kimi Code (Default)
KIMI_API_KEY=your-kimi-key
KIMI_MAX_AGENTS=50          # Max parallel agents (default: 50)

# Claude Code (Alternative)
ANTHROPIC_API_KEY=your-claude-key

# Agent Selection
BOS_DEFAULT_CODING_AGENT=kimi  # 'kimi' or 'claude'
```

### CLI Flags

```bash
# Use default (Kimi Code)
bos refactor src/

# Explicitly use Kimi Code
bos refactor src/ --agent=kimi

# Use Claude Code
bos refactor src/ --agent=claude

# Force parallel mode (Kimi only)
bos refactor src/ --parallel=max

# Limit parallel agents
bos refactor src/ --max-agents=20
```

### Config File

```javascript
// bos.config.js
export default {
  coding: {
    default: 'kimi',
    
    kimi: {
      enabled: true,
      maxAgents: 50,
      parallelism: 'auto',  // 'auto' | 'max' | 'none'
    },
    
    claude: {
      enabled: true,
      // Used when --agent=claude or when kimi fails
    },
    
    // Task-specific overrides
    taskDefaults: {
      'refactor': { agent: 'kimi', parallelism: 'auto' },
      'debug': { agent: 'claude' },
      'test-gen': { agent: 'kimi', parallelism: 'max' },
      'single-file': { agent: 'kimi', parallelism: 'none' },
    }
  }
};
```

---

## Cost Analysis

### Per-Task Cost Comparison

| Task | Files | Kimi Code Cost | Claude Code Cost | Savings |
|------|-------|----------------|------------------|---------|
| Small refactor | 1 | $0.05 | $0.45 | 90% |
| Medium refactor | 5 | $0.15 | $1.50 | 90% |
| Large refactor | 20 | $0.50 | $5.00 | 90% |
| Test suite gen | 10 | $0.30 | $3.00 | 90% |
| Codebase analysis | 50 | $0.80 | $8.00 | 90% |

### Monthly Projection (Active Developer)

| Usage Level | Kimi Code | Claude Code | Savings |
|-------------|-----------|-------------|---------|
| Light (100 tasks) | $15 | $150 | $135/mo |
| Medium (500 tasks) | $75 | $750 | $675/mo |
| Heavy (1000 tasks) | $150 | $1,500 | $1,350/mo |

**Kimi Code default saves ~90% on coding agent costs.**

---

## Implementation Roadmap

| Version | Milestone | Status |
|---------|-----------|--------|
| v0.1-0.4 | MVP (no coding agents) | 🔄 Current |
| v0.5 | Add Kimi Agent SDK dependency | ⏳ Planned |
| v0.5.1 | Basic `--agent` flag support | ⏳ Planned |
| v0.8 | Full Kimi Code integration | ⏳ Planned |
| v0.8.1 | Claude Code as alternative | ⏳ Planned |
| v0.8.2 | Task-based auto-selection | ⏳ Planned |
| v0.9 | Agent performance metrics | ⏳ Planned |

---

## Risks & Mitigations

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Kimi API downtime | Medium | High | Claude Code fallback |
| Parallel agents complexity | Low | Medium | Start with simple tasks |
| Quality variance | Low | Medium | Test extensively, allow override |
| SDK breaking changes | Medium | Medium | Pin versions, monitor releases |
| Cost increases | Low | Low | BYOK model, can switch defaults |

---

## Testing Strategy

### Integration Tests

```javascript
describe('Coding Agent Selection', () => {
  test('defaults to Kimi Code', async () => {
    const agent = selectAgent({ task: 'refactor' });
    expect(agent.name).toBe('kimi-code');
  });

  test('respects --agent=claude flag', async () => {
    const agent = selectAgent({ task: 'refactor' }, { agent: 'claude' });
    expect(agent.name).toBe('claude-code');
  });

  test('Kimi Code uses parallel agents for multi-file', async () => {
    const result = await kimiAgent.refactor(['a.js', 'b.js', 'c.js'], 'add types');
    expect(result.parallelAgentsUsed).toBeGreaterThan(1);
  });
});
```

### Performance Benchmarks

```javascript
describe('Parallel Agent Performance', () => {
  test('multi-file refactor is faster with Kimi', async () => {
    const files = ['src/a.js', 'src/b.js', 'src/c.js', 'src/d.js', 'src/e.js'];
    
    const kimiStart = Date.now();
    await kimiAgent.refactor(files, 'add error handling');
    const kimiTime = Date.now() - kimiStart;
    
    const claudeStart = Date.now();
    await claudeAgent.refactor(files, 'add error handling');
    const claudeTime = Date.now() - claudeStart;
    
    expect(kimiTime).toBeLessThan(claudeTime * 0.5); // At least 2x faster
  });
});
```

---

## Summary

**Kimi Code as default = 90% cost savings + 4.5x faster parallel execution**

- Default: `--agent=kimi` (or omit flag)
- Alternative: `--agent=claude`
- Auto-selection: Based on task type when implemented (v0.8.2)

This strategy maximizes cost efficiency while maintaining quality through intelligent fallback.

---

See also:
- [kimi-research.md](./kimi-research.md) — Full Kimi K2.5 research
- [architecture.md](./architecture.md) — System architecture
