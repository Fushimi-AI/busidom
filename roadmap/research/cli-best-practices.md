# CLI Best Practices Research

**Source:** Node.js CLI Apps Best Practices, OpenJS Foundation, WebbyLab  
**Research Date:** January 2026

---

## Key Findings

### 1. Command Parameter Handling

**Best Tools:**
- **Commander.js** — Industry standard, 3.5M weekly downloads
- **Docopt** — Universal interface, auto-generates docs
- **Yargs** — Feature-rich, popular alternative

**Recommendation:** Use Commander.js for Business-OS (proven, documented, maintainable)

---

### 2. Interactive User Experience

**Best Tools:**
- **Inquirer.js** — Questions, selections, confirmations
- **Prompts** — Lighter alternative
- **Readline** — Built-in Node.js (basic)

**Recommendation:** Use Inquirer.js for onboarding flows, readline for simple REPL

---

### 3. Core Focus Areas

1. **Distribution & Accessibility**
   - Publish to npm for easy install
   - Support global install (`npm install -g`)
   - Clear first-run experience

2. **Cross-Platform Compatibility**
   - Test on macOS, Linux, Windows
   - Use path.join() not hardcoded paths
   - Handle different shells (bash, zsh, PowerShell)

3. **Error Handling**
   - Provide actionable error messages
   - Distinguish user errors from system errors
   - Never show raw stack traces to users

4. **User Experience Design**
   - Show progress for long operations (spinners)
   - Use colors sparingly but meaningfully
   - Support --help for all commands
   - Exit codes: 0 for success, non-zero for failure

---

### 4. Best Practices Checklist

**From nodejs-cli-apps-best-practices (3.9k stars):**

- [ ] Respect POSIX arguments syntax
- [ ] Use spinner for async operations
- [ ] Support --version and --help
- [ ] Support NO_COLOR environment variable
- [ ] Allow piping (stdin/stdout)
- [ ] Test on fresh install
- [ ] Handle Ctrl+C gracefully

---

### 5. Recommended Dependencies

```json
{
  "commander": "^12.0.0",      // Command parsing
  "inquirer": "^9.0.0",        // Interactive prompts
  "chalk": "^5.0.0",           // Terminal colors
  "ora": "^8.0.0",             // Spinners
  "dotenv": "^16.0.0",         // Environment variables
  "conf": "^12.0.0"            // Config persistence (optional)
}
```

---

## Application to Business-OS

### Week 1 Implementation

1. **Use Commander.js** for command structure
2. **Use Inquirer.js** for interactive prompts
3. **Use Ora** for loading states
4. **Use Chalk** for colored output (minimal)
5. **Graceful shutdown** on Ctrl+C
6. **Clear error messages** for API/config issues

### Example Structure

```javascript
#!/usr/bin/env node
import { program } from 'commander';
import inquirer from 'inquirer';
import chalk from 'chalk';
import ora from 'ora';

program
  .name('bos')
  .description('Your AI co-founder')
  .version('0.1.0');

program
  .command('chat')
  .description('Start a conversation')
  .action(startChat);

program
  .command('clear')
  .description('Clear conversation history')
  .action(clearHistory);

program.parse();
```

---

## References

1. [Node.js CLI Apps Best Practices](https://github.com/lirantal/nodejs-cli-apps-best-practices)
2. [OpenJS Foundation CLI Guide](https://openjsf.org/blog/node-js-command-line-interface-applications-best-practices-a-guide)
3. [WebbyLab CLI Best Practices](https://webbylab.com/blog/best-practices-for-building-cli-and-publishing-it-to-npm/)
