# Week 1: Foundation + Memory (v0.1)

**Version:** 0.1  
**Ship by:** End of Week 1  
**Lines of Code:** ~350  

---

## Goal

Build a CLI chat tool that:
1. Accepts user input
2. Sends to LLM API
3. Displays response
4. **Remembers conversations across sessions**

---

## Why This Matters

This is the foundation everything builds on. If we can't:
- Talk to an LLM ✅
- Remember conversations ✅
- Provide a smooth CLI experience ✅

...nothing else matters.

---

## Daily Breakdown

### Day 1: Project Setup + Basic CLI

**Tasks:**
- [ ] Initialize Node.js project
- [ ] Install dependencies (commander, inquirer, openai, dotenv)
- [ ] Create basic CLI structure
- [ ] Add `/help` command
- [ ] Test basic input/output loop

**Deliverables:**
- `package.json` with dependencies
- `src/index.js` entry point
- `src/cli.js` with basic structure
- Working CLI that accepts input

**Time:** 3-4 hours

---

### Day 2: LLM API Integration

**Tasks:**
- [ ] Create API wrapper module
- [ ] Implement OpenAI chat completion call
- [ ] Handle API errors gracefully
- [ ] Add loading indicator while waiting
- [ ] Test with real API calls

**Deliverables:**
- `src/api.js` with `sendMessage()` function
- `.env.example` with API key template
- Error handling for common failures
- Working chat: user types → AI responds

**Time:** 3-4 hours

---

### Day 3: Memory System (Part 1)

**Tasks:**
- [ ] Design conversation schema
- [ ] Create memory module (save/load)
- [ ] Save messages to JSON after each exchange
- [ ] Load history on startup
- [ ] Include history in API context

**Deliverables:**
- `src/memory.js` with save/load functions
- `data/context.json` storage file
- Conversation persists across restarts

**Time:** 4-5 hours

---

### Day 4: Memory System (Part 2) + Commands

**Tasks:**
- [ ] Implement `/clear` command (reset memory)
- [ ] Implement `/history` command (show recent)
- [ ] Add conversation summary in context
- [ ] Handle large conversation truncation
- [ ] Test memory edge cases

**Deliverables:**
- Working `/clear` and `/history` commands
- Memory truncation for long conversations
- Tests passing for memory operations

**Time:** 4-5 hours

---

### Day 5: Polish + Alternative APIs

**Tasks:**
- [ ] Test with Kimi K2.5 API
- [ ] Add configurable API endpoint
- [ ] Improve error messages
- [ ] Add graceful shutdown
- [ ] Write README with setup instructions

**Deliverables:**
- Works with OpenAI and Kimi K2.5
- Clear setup documentation
- v0.1 complete and working

**Time:** 3-4 hours

---

### Days 6-7: Buffer + Testing

**Tasks:**
- [ ] Fix any bugs found
- [ ] Test on different machines
- [ ] Refactor if needed
- [ ] Prepare for Week 2

**Time:** As needed

---

## Success Criteria

| Criteria | Status |
|----------|--------|
| User types → AI responds | ⬜ |
| Close app → Reopen → AI remembers | ⬜ |
| `/clear` resets memory | ⬜ |
| `/history` shows recent messages | ⬜ |
| Works with OpenAI | ⬜ |
| Works with Kimi K2.5 | ⬜ |
| README with setup instructions | ⬜ |

---

## Technical Decisions

### Why Commander.js?
- 3.5M weekly downloads
- Industry standard for Node.js CLIs
- Excellent documentation
- Easy to extend

### Why JSON for Storage?
- No database setup required
- Human-readable for debugging
- Sufficient for MVP
- Easy to migrate later

### Why Not SQLite Yet?
- Adds complexity
- Not needed for single-user MVP
- PostgreSQL comes in v0.5

---

## API Schema

```javascript
// Conversation message format
{
  role: "user" | "assistant" | "system",
  content: string,
  timestamp: ISO8601
}

// Context file schema
{
  version: "0.1",
  created: ISO8601,
  updated: ISO8601,
  messages: [Message],
  summary: string | null
}
```

---

## Dependencies

```json
{
  "dependencies": {
    "commander": "^12.0.0",
    "inquirer": "^9.0.0",
    "openai": "^4.0.0",
    "dotenv": "^16.0.0",
    "chalk": "^5.0.0",
    "ora": "^8.0.0"
  }
}
```

---

## Environment Variables

```bash
# .env.example
OPENAI_API_KEY=sk-...
OPENAI_BASE_URL=https://api.openai.com/v1  # or Kimi endpoint
OPENAI_MODEL=gpt-4o-mini
```

---

## File Structure (End of Week 1)

```
src/
├── index.js          # Entry point
├── cli.js            # CLI commands and setup
├── api.js            # LLM API wrapper
└── memory.js         # JSON persistence

data/
└── context.json      # Conversation storage

.env.example
package.json
README.md
```

---

## Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| API rate limits | Medium | High | Add retry logic, backoff |
| Large context exceeds tokens | Medium | Medium | Truncate old messages |
| JSON corruption | Low | High | Backup before write |

---

## Testing Checklist

- [ ] Fresh install on new machine
- [ ] Works without .env (shows helpful error)
- [ ] Handles API timeout gracefully
- [ ] Memory persists after crash
- [ ] Commands work with typos (helpful suggestions)

---

## Quick Links

- [Detailed Tasks →](./TASKS.md)
- [Technical Specification →](./TECH_SPEC.md)
- [Back to Month 1 →](../README.md)
