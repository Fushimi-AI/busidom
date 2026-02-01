# Development Framework: AI-Assisted Feature Development

> Framework for breaking down roadmap into AI-friendly dev tickets using GitHub

---

## Core Principles

1. **Small chunks** — Each ticket fits in one AI context window (~8K tokens of context)
2. **Self-contained** — Ticket has all info needed; no external dependencies to understand
3. **Testable** — Clear acceptance criteria; AI can verify completion
4. **Sequential** — Dependencies explicit; build order clear
5. **GitHub-native** — Issues, Projects, Milestones, PRs as single source of truth

---

## Hierarchy Structure

```
ROADMAP
└── Phase (GitHub Milestone)
    └── Epic (GitHub Issue with label:epic)
        └── Feature (GitHub Issue with label:feature)
            └── Task (GitHub Issue with label:task)
                └── Sub-task (Checklist in Issue body)
```

| Level | Size | AI Context | GitHub Entity |
|-------|------|------------|---------------|
| Phase | 2-4 weeks | N/A | Milestone |
| Epic | 3-7 days | N/A | Issue + `epic` label |
| Feature | 1-2 days | ~50K tokens | Issue + `feature` label |
| Task | 1-4 hours | ~8K tokens | Issue + `task` label |
| Sub-task | 15-60 min | ~2K tokens | Checkbox in task |

---

## Phase Breakdown (Business-OS)

### Phase 0: Foundation (Week 1-2)
- [ ] Project setup, tooling, CI/CD
- [ ] Core architecture scaffolding
- [ ] Basic CLI interface

### Phase 1: MVP Core (Week 3-4)
- [ ] Chat interface with memory
- [ ] Mentor personality system
- [ ] Context extraction

### Phase 2: Persistence (Week 5-6)
- [ ] PostgreSQL integration
- [ ] User accounts + auth
- [ ] Conversation storage

### Phase 3: Intelligence (Week 7-8)
- [ ] Vector DB (pgvector)
- [ ] Semantic memory retrieval
- [ ] Context relevance scoring

### Phase 4: Multi-Agent (Week 9-10)
- [ ] Agent orchestration framework
- [ ] Mentor agent
- [ ] Research agent

### Phase 5: Experience (Week 11-12)
- [ ] Desktop GUI (Electron/Tauri)
- [ ] Settings management
- [ ] Stage visualization

### Phase 6: Polish (Week 13-14)
- [ ] Token optimization
- [ ] Error handling
- [ ] Performance tuning

### Phase 7: Launch (Week 15-16)
- [ ] Documentation
- [ ] Onboarding flow
- [ ] v1.0 release

---

## GitHub Setup Checklist

### Labels (Create These)
```
type:epic        — Multi-feature initiative (blue)
type:feature     — User-facing capability (green)
type:task        — Single implementation unit (yellow)
type:bug         — Defect fix (red)
type:chore       — Maintenance/tooling (gray)

priority:critical — Blocks release
priority:high     — This sprint
priority:medium   — Next sprint
priority:low      — Backlog

status:ready      — Spec complete, ready for dev
status:blocked    — Waiting on dependency
status:review     — PR open, needs review

ai:claude         — For Claude Code
ai:cursor         — For Cursor
ai:manual         — Needs human
```

### Milestones (Create Per Phase)
```
Phase 0: Foundation     — Due: [date]
Phase 1: MVP Core       — Due: [date]
Phase 2: Persistence    — Due: [date]
...
```

### Project Board (Columns)
```
Backlog → Ready → In Progress → Review → Done
```

---

## Ticket Templates

### Epic Template
```markdown
## Epic: [Name]

**Goal:** One sentence describing the outcome

**Success Metrics:**
- [ ] Metric 1
- [ ] Metric 2

**Features in this Epic:**
- [ ] #issue-number Feature 1
- [ ] #issue-number Feature 2
- [ ] #issue-number Feature 3

**Dependencies:** None | #issue-numbers

**Phase:** [Milestone name]
```

### Feature Template
```markdown
## Feature: [Name]

**User Story:** As a [user], I want [capability] so that [benefit]

**Context:**
Brief background (2-3 sentences max)

**Acceptance Criteria:**
- [ ] Criteria 1
- [ ] Criteria 2
- [ ] Criteria 3

**Tasks:**
- [ ] #issue-number Task 1
- [ ] #issue-number Task 2

**Out of Scope:**
- Thing we're NOT doing
- Another thing we're NOT doing

**Dependencies:** None | #issue-numbers

**Labels:** `type:feature`, `priority:X`, `ai:claude`
```

### Task Template (AI-Optimized)
```markdown
## Task: [Verb] + [Object]

**Objective:** One sentence

**Context Files:**
- `src/path/to/file1.js` — Why relevant
- `src/path/to/file2.js` — Why relevant

**Requirements:**
1. Specific requirement 1
2. Specific requirement 2
3. Specific requirement 3

**Acceptance Criteria:**
- [ ] Testable outcome 1
- [ ] Testable outcome 2

**Technical Notes:**
- Use [specific pattern/library]
- Follow existing pattern in `src/example.js`
- Do NOT change [specific thing]

**Sub-tasks:**
- [ ] Sub-task 1 (15 min)
- [ ] Sub-task 2 (30 min)
- [ ] Sub-task 3 (15 min)

**Test Command:** `npm test -- --grep "feature name"`

**Labels:** `type:task`, `status:ready`, `ai:claude`
```

---

## AI Prompt Formula

When handing a task to AI, use this structure:

```
## Context
[Paste relevant file contents or summaries]

## Task
[Copy from GitHub issue]

## Constraints
- Don't modify files outside of [X]
- Follow existing patterns in codebase
- Keep changes minimal

## Output
- Files to create/modify
- Tests to add
- PR description
```

---

## Workflow

### 1. Planning (Human)
```
Roadmap → Break into Phases (Milestones)
       → Break into Epics (Issues)
       → Break into Features (Issues)
       → Break into Tasks (Issues)
       → Add to Project Board
```

### 2. Preparation (Human)
```
For each Task:
  → Write clear spec using template
  → List context files
  → Add acceptance criteria
  → Set labels: status:ready, ai:claude
  → Link dependencies
```

### 3. Execution (AI)
```
Pick task from "Ready" column
  → Read context files
  → Implement per requirements
  → Run tests
  → Create PR linking issue
  → Move to "Review"
```

### 4. Review (Human/AI)
```
Review PR
  → Check acceptance criteria
  → Run full test suite
  → Merge or request changes
  → Close issue
  → Move to "Done"
```

---

## Size Guidelines

### Too Big (Split It)
- More than 3 files to modify
- More than 200 lines of code
- More than 4 hours estimated
- Requires understanding 5+ context files
- Has multiple independent outcomes

### Right Size
- 1-3 files modified
- 50-150 lines of code
- 1-4 hours estimated
- 2-4 context files needed
- Single clear outcome

### Too Small (Combine It)
- Less than 15 min
- Trivial change
- No logic involved
- Pure formatting/rename

---

## Context Window Management

### For Each Task, Include:
1. **Task spec** (~500 tokens)
2. **Relevant source files** (~2-4K tokens)
3. **Test file if exists** (~1K tokens)
4. **Type definitions** (~500 tokens)
5. **Example patterns** (~1K tokens)

**Total: ~5-8K tokens** — Leaves room for AI reasoning

### Context Preparation Script
```bash
# Create context bundle for a task
echo "## Task Spec" > context.md
cat .github/ISSUE_TEMPLATE/task.md >> context.md

echo "## Relevant Files" >> context.md
cat src/relevant-file.js >> context.md

echo "## Test File" >> context.md
cat tests/relevant.test.js >> context.md
```

---

## Quality Gates

### Before Moving to "Ready"
- [ ] Task has clear objective (one sentence)
- [ ] Acceptance criteria are testable
- [ ] Context files are listed
- [ ] Dependencies are linked
- [ ] Estimate is under 4 hours
- [ ] Labels are set

### Before Merging PR
- [ ] All acceptance criteria checked
- [ ] Tests pass
- [ ] No linting errors
- [ ] PR links to issue
- [ ] Code follows existing patterns

### Before Closing Milestone
- [ ] All issues closed
- [ ] All PRs merged
- [ ] Integration tests pass
- [ ] Demo recorded/documented
- [ ] Retro notes captured

---

## Example: Breaking Down "Chat with Memory"

### Epic
```
Epic: Persistent Chat Memory
Goal: User conversations persist across sessions
```

### Features
```
Feature 1: Conversation Storage
Feature 2: Conversation Loading
Feature 3: Memory Context Injection
Feature 4: Memory Search
```

### Tasks (Feature 1: Conversation Storage)
```
Task 1.1: Create conversation data model
Task 1.2: Implement save conversation function
Task 1.3: Add auto-save on each message
Task 1.4: Write unit tests for storage
```

### Sub-tasks (Task 1.1: Create conversation data model)
```
- [ ] Define Conversation interface
- [ ] Define Message interface
- [ ] Create TypeScript types file
- [ ] Add JSDoc comments
```

---

## GitHub CLI Commands

```bash
# Create milestone
gh api repos/:owner/:repo/milestones -f title="Phase 1: MVP Core" -f due_on="2024-02-15"

# Create epic
gh issue create --title "Epic: Chat Memory System" --label "type:epic" --milestone "Phase 1: MVP Core"

# Create task from template
gh issue create --title "Task: Implement conversation save" --label "type:task,status:ready,ai:claude" --body-file .github/ISSUE_TEMPLATE/task.md

# List ready tasks
gh issue list --label "status:ready" --json number,title

# Create PR linking issue
gh pr create --title "feat: implement conversation save" --body "Closes #123"
```

---

## Checklist: Setting Up This Framework

### One-Time Setup
- [ ] Create GitHub repository (if not exists)
- [ ] Create all labels (copy from above)
- [ ] Create issue templates in `.github/ISSUE_TEMPLATE/`
- [ ] Create milestones for each phase
- [ ] Create GitHub Project board
- [ ] Configure Project board columns

### Per-Phase Setup
- [ ] Create epic issues for the phase
- [ ] Break epics into feature issues
- [ ] Break features into task issues
- [ ] Link all dependencies
- [ ] Set all priorities
- [ ] Add to project board

### Per-Task Prep
- [ ] Fill out task template completely
- [ ] Identify and list context files
- [ ] Write testable acceptance criteria
- [ ] Estimate time (if >4hr, split)
- [ ] Set `status:ready` label

### Per-Sprint
- [ ] Move ready tasks to "In Progress"
- [ ] Run AI on tasks
- [ ] Review PRs
- [ ] Update project board
- [ ] Close completed issues

---

## File: `.github/ISSUE_TEMPLATE/task.md`

```markdown
---
name: Task
about: Single implementation unit for AI development
labels: type:task
---

## Task: [Verb] + [Object]

**Objective:**

**Context Files:**
- `path/to/file.js` —

**Requirements:**
1.
2.
3.

**Acceptance Criteria:**
- [ ]
- [ ]

**Technical Notes:**
-

**Sub-tasks:**
- [ ]
- [ ]

**Test Command:**

**Estimate:** X hours
```

---

## Next Steps

1. [ ] Initialize GitHub repo with this structure
2. [ ] Create Phase 0 milestone and issues
3. [ ] Set up project board
4. [ ] Create first 5-10 tasks with full specs
5. [ ] Start executing with AI

