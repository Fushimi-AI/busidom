# Week 1: Technical Specification

## Overview

This document defines the technical architecture for v0.1 (Foundation + Memory).

---

## System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                       CLI Layer                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │   index.js  │  │   cli.js    │  │  commands   │     │
│  │  (entry)    │→ │  (REPL)     │→ │  (/help,    │     │
│  │             │  │             │  │   /clear)   │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
└────────────────────────┬────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────┐
│                     Core Services                        │
│  ┌─────────────────────┐  ┌─────────────────────┐      │
│  │      api.js         │  │     memory.js       │      │
│  │  ┌───────────────┐  │  │  ┌───────────────┐  │      │
│  │  │ sendMessage() │  │  │  │ loadContext() │  │      │
│  │  │ handleError() │  │  │  │ saveMessage() │  │      │
│  │  └───────────────┘  │  │  │ clearContext()│  │      │
│  └──────────┬──────────┘  │  └───────┬───────┘  │      │
│             │             │          │          │      │
└─────────────┼─────────────┴──────────┼──────────┴──────┘
              │                        │
              ▼                        ▼
┌─────────────────────────┐  ┌─────────────────────────┐
│    External: LLM API    │  │   File System: JSON     │
│  (OpenAI / Kimi K2.5)   │  │   data/context.json     │
└─────────────────────────┘  └─────────────────────────┘
```

---

## Module Specifications

### 1. index.js (Entry Point)

**Purpose:** Bootstrap the application

```javascript
#!/usr/bin/env node

import { startCLI } from './cli.js';
import { validateConfig } from './config.js';

async function main() {
  try {
    validateConfig();
    await startCLI();
  } catch (error) {
    console.error('Failed to start:', error.message);
    process.exit(1);
  }
}

main();
```

**Exports:** None (entry point)

---

### 2. cli.js (CLI Interface)

**Purpose:** Handle user interaction and command routing

**Exports:**
```javascript
export async function startCLI();
export function parseCommand(input);
export function showHelp();
export function showWelcome();
```

**REPL Loop:**
```javascript
import inquirer from 'inquirer';
import chalk from 'chalk';
import ora from 'ora';
import { sendMessage } from './api.js';
import { loadContext, saveMessage, clearContext } from './memory.js';

export async function startCLI() {
  showWelcome();
  const context = await loadContext();
  
  while (true) {
    const { input } = await inquirer.prompt([{
      type: 'input',
      name: 'input',
      message: chalk.green('You:'),
      prefix: ''
    }]);
    
    // Handle commands
    if (input.startsWith('/')) {
      const handled = await handleCommand(input, context);
      if (handled === 'exit') break;
      continue;
    }
    
    // Handle chat
    await handleChat(input, context);
  }
}
```

**Commands:**
| Command | Action |
|---------|--------|
| `/help` | Show available commands |
| `/exit` | Quit the application |
| `/clear` | Clear conversation memory |
| `/history` | Show recent messages |
| `/history N` | Show last N messages |
| `/version` | Show version |

---

### 3. api.js (LLM API Wrapper)

**Purpose:** Abstract LLM API communication

**Exports:**
```javascript
export async function sendMessage(messages);
export function formatMessages(context);
export function estimateTokens(text);
```

**Implementation:**
```javascript
import OpenAI from 'openai';

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
  baseURL: process.env.OPENAI_BASE_URL || 'https://api.openai.com/v1'
});

export async function sendMessage(messages) {
  try {
    const response = await openai.chat.completions.create({
      model: process.env.OPENAI_MODEL || 'gpt-4o-mini',
      messages: messages,
      temperature: 0.7,
      max_tokens: parseInt(process.env.MAX_TOKENS) || 1000
    });
    
    return {
      content: response.choices[0].message.content,
      usage: response.usage
    };
  } catch (error) {
    throw new APIError(error);
  }
}
```

**Error Handling:**
```javascript
class APIError extends Error {
  constructor(originalError) {
    if (originalError.status === 401) {
      super('Invalid API key. Check your OPENAI_API_KEY.');
    } else if (originalError.status === 429) {
      super('Rate limited. Please wait and try again.');
    } else if (originalError.code === 'ENOTFOUND') {
      super('Network error. Check your internet connection.');
    } else {
      super(`API error: ${originalError.message}`);
    }
    this.name = 'APIError';
    this.original = originalError;
  }
}
```

---

### 4. memory.js (Persistence Layer)

**Purpose:** Manage conversation persistence

**Exports:**
```javascript
export async function loadContext();
export async function saveMessage(role, content);
export async function clearContext();
export async function getHistory(count);
export function truncateMessages(messages, maxTokens);
```

**Context Schema:**
```javascript
const CONTEXT_SCHEMA = {
  version: '0.1',
  created: null,      // ISO8601 timestamp
  updated: null,      // ISO8601 timestamp
  messages: [],       // Array of Message objects
  metadata: {
    totalMessages: 0,
    truncatedAt: null
  }
};

const MESSAGE_SCHEMA = {
  role: null,         // 'user' | 'assistant' | 'system'
  content: null,      // string
  timestamp: null     // ISO8601 timestamp
};
```

**Implementation:**
```javascript
import { promises as fs } from 'fs';
import path from 'path';

const DATA_DIR = path.join(process.cwd(), 'data');
const CONTEXT_PATH = path.join(DATA_DIR, 'context.json');

export async function loadContext() {
  try {
    await fs.mkdir(DATA_DIR, { recursive: true });
    const data = await fs.readFile(CONTEXT_PATH, 'utf-8');
    return JSON.parse(data);
  } catch (error) {
    if (error.code === 'ENOENT') {
      return createEmptyContext();
    }
    throw error;
  }
}

export async function saveMessage(role, content) {
  const context = await loadContext();
  
  context.messages.push({
    role,
    content,
    timestamp: new Date().toISOString()
  });
  
  context.updated = new Date().toISOString();
  context.metadata.totalMessages++;
  
  // Truncate if needed
  if (context.messages.length > MAX_MESSAGES) {
    context.messages = truncateMessages(context.messages, MAX_MESSAGES);
    context.metadata.truncatedAt = new Date().toISOString();
  }
  
  // Atomic write: write to temp, then rename
  const tempPath = `${CONTEXT_PATH}.tmp`;
  await fs.writeFile(tempPath, JSON.stringify(context, null, 2));
  await fs.rename(tempPath, CONTEXT_PATH);
  
  return context;
}

export async function clearContext() {
  const empty = createEmptyContext();
  await fs.writeFile(CONTEXT_PATH, JSON.stringify(empty, null, 2));
  return empty;
}

function createEmptyContext() {
  return {
    ...CONTEXT_SCHEMA,
    created: new Date().toISOString(),
    updated: new Date().toISOString(),
    messages: [],
    metadata: { totalMessages: 0, truncatedAt: null }
  };
}
```

**Truncation Strategy:**
```javascript
const MAX_MESSAGES = 50;  // Keep last 50 messages
const MAX_TOKENS = 4000;  // Approximate token limit

export function truncateMessages(messages, maxMessages) {
  if (messages.length <= maxMessages) {
    return messages;
  }
  
  // Keep first message (if system prompt) + last N messages
  const firstMessage = messages[0];
  const recentMessages = messages.slice(-maxMessages + 1);
  
  if (firstMessage.role === 'system') {
    return [firstMessage, ...recentMessages];
  }
  
  return recentMessages;
}
```

---

## Configuration

### Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `OPENAI_API_KEY` | Yes | - | API key for LLM |
| `OPENAI_BASE_URL` | No | `https://api.openai.com/v1` | API endpoint |
| `OPENAI_MODEL` | No | `gpt-4o-mini` | Model to use |
| `MAX_TOKENS` | No | `1000` | Max response tokens |
| `MAX_MESSAGES` | No | `50` | Max messages to keep |

### .env.example

```bash
# Required
OPENAI_API_KEY=sk-your-key-here

# Optional - for alternative APIs
OPENAI_BASE_URL=https://api.openai.com/v1
OPENAI_MODEL=gpt-4o-mini

# Optional - limits
MAX_TOKENS=1000
MAX_MESSAGES=50
```

---

## Error Handling Strategy

### Error Categories

| Category | Example | User Message | Log Level |
|----------|---------|--------------|-----------|
| Config | Missing API key | "Please set OPENAI_API_KEY" | Error |
| Network | Connection timeout | "Network error. Try again." | Warn |
| API | Rate limit | "Rate limited. Wait 60s." | Warn |
| API | Invalid key | "Invalid API key." | Error |
| File | JSON corrupt | "Memory corrupted. Resetting." | Error |

### Error Flow

```javascript
try {
  // Operation
} catch (error) {
  if (error instanceof APIError) {
    console.error(chalk.red(error.message));
    // Don't crash, continue REPL
  } else if (error instanceof FileError) {
    console.error(chalk.red('Memory error. Resetting...'));
    await clearContext();
  } else {
    console.error(chalk.red('Unexpected error:', error.message));
    process.exit(1);
  }
}
```

---

## Testing Strategy

### Unit Tests (if time permits)

```javascript
// memory.test.js
describe('memory', () => {
  test('loadContext returns empty on first run', async () => {
    const context = await loadContext();
    expect(context.messages).toEqual([]);
  });
  
  test('saveMessage persists messages', async () => {
    await saveMessage('user', 'Hello');
    const context = await loadContext();
    expect(context.messages).toHaveLength(1);
  });
  
  test('clearContext resets memory', async () => {
    await saveMessage('user', 'Hello');
    await clearContext();
    const context = await loadContext();
    expect(context.messages).toEqual([]);
  });
});
```

### Manual Testing Checklist

- [ ] Fresh start with no data/
- [ ] Multiple message exchanges
- [ ] Close and reopen (memory persists)
- [ ] /clear command
- [ ] /history command
- [ ] Invalid API key error
- [ ] Network timeout error
- [ ] Very long message handling

---

## Performance Considerations

### Token Usage

- Each conversation includes full history up to MAX_MESSAGES
- Estimate: ~4 tokens per word average
- 50 messages × 100 words average = 20,000 tokens context
- Cost consideration for long conversations

### Optimization Opportunities (Future)

1. **Summarization**: Summarize old messages instead of truncating
2. **Semantic chunking**: Only include relevant history
3. **Caching**: Cache common responses (v0.7)

---

## Security Considerations

### MVP Scope

- API key stored in .env (gitignored)
- No authentication (single user)
- No encryption (local files only)

### Future (v0.5+)

- Encrypt sensitive data at rest
- User authentication
- API key per user

---

## Dependencies

```json
{
  "name": "business-os",
  "version": "0.1.0",
  "type": "module",
  "bin": {
    "bos": "./src/index.js"
  },
  "dependencies": {
    "commander": "^12.1.0",
    "inquirer": "^9.2.0",
    "openai": "^4.52.0",
    "dotenv": "^16.4.0",
    "chalk": "^5.3.0",
    "ora": "^8.0.0"
  },
  "devDependencies": {
    "vitest": "^1.6.0"
  }
}
```

---

## Compatibility

### Tested Platforms
- macOS 14+ (primary)
- Ubuntu 22.04+
- Windows 11 (WSL2)

### Node.js Version
- Minimum: 18.0.0
- Recommended: 20.0.0+

### LLM APIs
- OpenAI (gpt-4o-mini, gpt-4o)
- **Kimi K2.5 (default, 10x cheaper)**
- Any OpenAI-compatible endpoint

---

## Coding Agent Integration (Post-MVP)

### Overview

Starting v0.5, Business-OS will integrate AI coding agents:

**Default:** Kimi Code (Parallel Agents)  
**Alternative:** Claude Code

### Why Kimi Code as Default

| Factor | Kimi Code | Claude Code |
|--------|-----------|-------------|
| **Cost** | ~10x cheaper | Premium |
| **Parallel Agents** | Up to 100 | Sequential |
| **Speed (Complex)** | 4.5x faster | Baseline |
| **Node.js SDK** | Native | CLI wrapper |

### Agent Swarm Architecture

Kimi K2.5 uses **Parallel-Agent Reinforcement Learning (PARL)**:

```
┌─────────────────────────────────────────────────────┐
│              KIMI CODE AGENT SWARM                   │
├─────────────────────────────────────────────────────┤
│                                                      │
│   ┌──────────────────────────────────────────┐      │
│   │          ORCHESTRATOR                    │      │
│   │   Decomposes task → Assigns sub-agents   │      │
│   └──────────────────────────────────────────┘      │
│                        │                            │
│        ┌───────────────┼───────────────┐            │
│        ▼               ▼               ▼            │
│   ┌─────────┐    ┌─────────┐    ┌─────────┐        │
│   │Sub-Agent│    │Sub-Agent│    │Sub-Agent│        │
│   │  File1  │    │  File2  │    │  Tests  │        │
│   └─────────┘    └─────────┘    └─────────┘        │
│        │               │               │            │
│        └───────────────┼───────────────┘            │
│                        ▼                            │
│                 ┌───────────┐                       │
│                 │  COMBINE  │                       │
│                 └───────────┘                       │
│                                                      │
│   Up to 100 agents | 1,500 tool calls | 4.5x faster │
└─────────────────────────────────────────────────────┘
```

### Integration via Kimi Agent SDK

```javascript
// src/agents/coding/kimi-code.js (v0.5+)
import { KimiAgent } from 'kimi-agent-sdk';

export class KimiCodeAgent {
  constructor(config) {
    this.agent = new KimiAgent({
      apiKey: process.env.KIMI_API_KEY,
      model: 'k2.5',
      agentSwarm: true,
      maxAgents: 50
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
}
```

### CLI Flag

```bash
# Default (Kimi Code with parallel agents)
bos refactor src/

# Alternative (Claude Code)
bos refactor src/ --agent=claude
```

### Implementation Timeline

| Version | Milestone |
|---------|-----------|
| v0.1-0.4 | MVP (no coding agents) |
| v0.5 | Add Kimi Agent SDK |
| v0.8 | Full Kimi Code integration |
| v0.8.1 | Claude Code alternative |

See [coding-agents.md](../../../ideation/tech-stack/coding-agents.md) for full strategy.
