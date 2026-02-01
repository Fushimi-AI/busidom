# Week 1: Detailed Task List

## Day 1: Project Setup + Basic CLI

### Hour 1-2: Project Initialization
- [ ] Create project directory structure
- [ ] Run `npm init -y`
- [ ] Install core dependencies:
  ```bash
  npm install commander inquirer openai dotenv chalk ora
  ```
- [ ] Create `.gitignore` (node_modules, .env, data/)
- [ ] Create `.env.example`

### Hour 2-3: CLI Foundation
- [ ] Create `src/index.js` as entry point
- [ ] Create `src/cli.js` with Commander setup
- [ ] Add program name, version, description
- [ ] Implement basic REPL loop:
  ```javascript
  // Pseudocode
  while (true) {
    const input = await prompt("You: ");
    if (input === "/exit") break;
    console.log("AI: [placeholder]");
  }
  ```

### Hour 3-4: Basic Commands
- [ ] Implement `/help` - show available commands
- [ ] Implement `/exit` - quit gracefully
- [ ] Implement `/version` - show version
- [ ] Add command parsing logic
- [ ] Test all commands work

**End of Day 1 Checkpoint:**
- [ ] `npm start` launches CLI
- [ ] Can type messages
- [ ] Commands recognized
- [ ] Clean exit on `/exit`

---

## Day 2: LLM API Integration

### Hour 1-2: API Module Setup
- [ ] Create `src/api.js`
- [ ] Load environment variables
- [ ] Initialize OpenAI client:
  ```javascript
  import OpenAI from 'openai';
  
  const openai = new OpenAI({
    apiKey: process.env.OPENAI_API_KEY,
    baseURL: process.env.OPENAI_BASE_URL
  });
  ```

### Hour 2-3: Send Message Function
- [ ] Create `sendMessage(messages)` function
- [ ] Implement chat completion call:
  ```javascript
  const response = await openai.chat.completions.create({
    model: process.env.OPENAI_MODEL || 'gpt-4o-mini',
    messages: messages,
    temperature: 0.7,
    max_tokens: 1000
  });
  ```
- [ ] Extract and return assistant message

### Hour 3-4: Error Handling + UX
- [ ] Handle API errors (rate limit, auth, network)
- [ ] Add loading spinner while waiting (ora):
  ```javascript
  const spinner = ora('Thinking...').start();
  // ... API call
  spinner.stop();
  ```
- [ ] Format response with colors (chalk)
- [ ] Test with real API calls

### Hour 4-5: Integration + Testing
- [ ] Connect API to CLI loop
- [ ] Test full flow: input → API → output
- [ ] Test error scenarios:
  - Invalid API key
  - Network timeout
  - Empty input

**End of Day 2 Checkpoint:**
- [ ] User types → AI responds
- [ ] Loading indicator shows
- [ ] Errors handled gracefully
- [ ] Works with valid API key

---

## Day 3: Memory System (Part 1)

### Hour 1-2: Schema Design
- [ ] Design conversation message schema
- [ ] Design context file schema
- [ ] Create `data/` directory
- [ ] Create `src/memory.js`

### Hour 2-3: Save Function
- [ ] Implement `saveMessage(message)`:
  ```javascript
  export async function saveMessage(role, content) {
    const context = await loadContext();
    context.messages.push({
      role,
      content,
      timestamp: new Date().toISOString()
    });
    context.updated = new Date().toISOString();
    await fs.writeFile(CONTEXT_PATH, JSON.stringify(context, null, 2));
  }
  ```
- [ ] Handle file creation if doesn't exist
- [ ] Add atomic write (write to temp, then rename)

### Hour 3-4: Load Function
- [ ] Implement `loadContext()`:
  ```javascript
  export async function loadContext() {
    try {
      const data = await fs.readFile(CONTEXT_PATH, 'utf-8');
      return JSON.parse(data);
    } catch (e) {
      return createEmptyContext();
    }
  }
  ```
- [ ] Create default empty context structure
- [ ] Handle JSON parse errors

### Hour 4-5: Integration
- [ ] Integrate memory with CLI loop
- [ ] Save user messages automatically
- [ ] Save assistant messages automatically
- [ ] Load history on startup
- [ ] Pass history to API calls

**End of Day 3 Checkpoint:**
- [ ] Messages saved to `data/context.json`
- [ ] History loads on startup
- [ ] AI has context from previous messages
- [ ] Close → Reopen → Remembers

---

## Day 4: Memory System (Part 2) + Commands

### Hour 1-2: Clear Command
- [ ] Implement `/clear` command:
  ```javascript
  if (input === '/clear') {
    await clearContext();
    console.log('Memory cleared.');
    continue;
  }
  ```
- [ ] Create `clearContext()` function
- [ ] Confirm before clearing (optional)
- [ ] Test clear works

### Hour 2-3: History Command
- [ ] Implement `/history` command
- [ ] Show last N messages (default 10)
- [ ] Format nicely with timestamps
- [ ] Add `/history N` for custom count

### Hour 3-4: Context Management
- [ ] Implement message truncation for long conversations
- [ ] Keep system prompt + last N messages
- [ ] Add summary of older messages (optional)
- [ ] Track token count (approximate)

### Hour 4-5: Edge Cases
- [ ] Test with very long conversations
- [ ] Test concurrent access (unlikely but handle)
- [ ] Test file corruption recovery
- [ ] Add backup before overwrite

**End of Day 4 Checkpoint:**
- [ ] `/clear` resets memory
- [ ] `/history` shows messages
- [ ] Long conversations truncated
- [ ] No crashes on edge cases

---

## Day 5: Polish + Alternative APIs

### Hour 1-2: Kimi K2.5 Support
- [ ] Test with Kimi K2.5 API endpoint
- [ ] Verify message format compatibility
- [ ] Handle any API differences
- [ ] Document in README

### Hour 2-3: Configuration
- [ ] Add configurable API endpoint
- [ ] Add configurable model selection
- [ ] Add configurable max tokens
- [ ] Validate environment variables on startup

### Hour 3-4: Error Messages + UX
- [ ] Improve error messages (actionable)
- [ ] Add graceful shutdown (Ctrl+C)
- [ ] Add welcome message on start
- [ ] Show memory status on start

### Hour 4-5: Documentation
- [ ] Write README with:
  - Quick start
  - Environment setup
  - Available commands
  - Troubleshooting
- [ ] Add inline code comments
- [ ] Create CHANGELOG.md

**End of Day 5 Checkpoint:**
- [ ] Works with OpenAI
- [ ] Works with Kimi K2.5
- [ ] README complete
- [ ] v0.1 DONE

---

## Days 6-7: Buffer + Testing

### Testing Checklist
- [ ] Fresh install on Mac
- [ ] Fresh install on Linux (if available)
- [ ] Fresh install on Windows (if available)
- [ ] Works without .env (helpful error)
- [ ] Works with invalid API key (clear error)
- [ ] Memory persists after crash
- [ ] Commands work correctly
- [ ] No memory leaks in long sessions

### Bug Fixes
- [ ] Fix any bugs found during testing
- [ ] Refactor messy code
- [ ] Optimize if needed

### Preparation for Week 2
- [ ] Review Week 2 requirements
- [ ] Identify any blockers
- [ ] Document lessons learned

---

## Code Quality Checklist

- [ ] No console.log in production code (use proper logging)
- [ ] All async functions have error handling
- [ ] No hardcoded values (use config/env)
- [ ] Functions are small and single-purpose
- [ ] Code is readable without excessive comments

---

## Definition of Done

v0.1 is DONE when:
1. ✅ All success criteria met
2. ✅ README complete
3. ✅ Works on fresh machine
4. ✅ No known critical bugs
5. ✅ Code pushed to repository
