# Phase: Experience (Weeks 12-14)

**Goal:** Beautiful interface and personalized mentorship

---

## Overview

| Version | Focus | Duration |
|---------|-------|----------|
| **v0.10** | Desktop GUI | 2 weeks |
| **v0.11** | Multiple Mentors | 1 week |

---

## v0.10 — Desktop GUI

### Why Desktop First?

- Entrepreneurs work on laptops
- Need offline capability (flights, travel)
- Native performance
- Professional tool feel
- CLI is for power users, GUI for everyone

### Tech Stack Options

| Option | Pros | Cons | Recommendation |
|--------|------|------|----------------|
| **Tauri** | Small binary, Rust backend, fast | Newer ecosystem | ✅ Preferred |
| **Electron** | Mature, large ecosystem | Large binary, memory usage | Backup |
| **Web App** | No install, easy updates | Requires connection | v1.0+ |

**Decision:** Tauri with React/Svelte frontend

### Core Screens

#### 1. Chat Interface
```
┌─────────────────────────────────────────────────────────┐
│  Business-OS                               [−][□][×]    │
├─────────────────────────────────────────────────────────┤
│ ┌─────────────┐ ┌─────────────────────────────────────┐ │
│ │             │ │                                     │ │
│ │  SIDEBAR    │ │         CHAT AREA                   │ │
│ │             │ │                                     │ │
│ │  Businesses │ │  AI: Welcome back! Let's continue   │ │
│ │  > TechCo   │ │      working on your pricing...     │ │
│ │    StartupX │ │                                     │ │
│ │             │ │  You: I'm thinking $99/month...     │ │
│ │  ─────────  │ │                                     │ │
│ │  Settings   │ │  AI: Let's break that down. What's  │ │
│ │  Help       │ │      your cost to serve one...      │ │
│ │             │ │                                     │ │
│ └─────────────┘ │                                     │ │
│                 ├─────────────────────────────────────┤ │
│                 │ Type your message...          [Send] │ │
│                 └─────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
```

#### 2. Business Dashboard
```
┌─────────────────────────────────────────────────────────┐
│  TechCo Dashboard                                       │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Stage: MVP          Progress: ████████░░ 80%           │
│                                                         │
│  ┌──────────────────┐ ┌──────────────────┐             │
│  │  QUALITY GATES   │ │  IDIOT INDEX     │             │
│  │  ✅ Problem      │ │  Current: 0.35   │             │
│  │  ✅ Solution     │ │  Status: ⚠️       │             │
│  │  ⬜ First User   │ │  Target: < 0.30   │             │
│  │  ⬜ Retention    │ │                  │             │
│  └──────────────────┘ └──────────────────┘             │
│                                                         │
│  ┌──────────────────────────────────────────────┐      │
│  │  RECENT INSIGHTS                              │      │
│  │  • Focus on one vertical before going broad   │      │
│  │  • Your pricing assumes 1000 users at $99     │      │
│  │  • Challenge: How do you get first 10 users?  │      │
│  └──────────────────────────────────────────────┘      │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

#### 3. Cost Tracking
```
┌─────────────────────────────────────────────────────────┐
│  Token Usage & Costs                                    │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  This Month: $12.45 / $25.00 (Starter tier)            │
│  ███████████████░░░░░░░░░░░░░░░░ 50%                   │
│                                                         │
│  ┌─────────────────────────────────────────┐           │
│  │  Daily Usage                            │           │
│  │  $2 ─┤     ██                           │           │
│  │     ─┤  ██ ██ ██    ██                  │           │
│  │  $1 ─┤  ██ ██ ██ ██ ██ ██               │           │
│  │     ─┼──────────────────────────────    │           │
│  │       Mon Tue Wed Thu Fri Sat Sun       │           │
│  └─────────────────────────────────────────┘           │
│                                                         │
│  Token Efficiency: 52% savings from compression         │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Key Features

- [ ] Chat with full CLI parity
- [ ] Business switching
- [ ] Offline mode (SQLite cache)
- [ ] Native notifications
- [ ] Dark/light mode
- [ ] Keyboard shortcuts

### Deliverables (v0.10)

- [ ] Tauri + React/Svelte app
- [ ] Chat interface working
- [ ] Business dashboard
- [ ] Settings panel
- [ ] macOS, Windows, Linux builds

---

## v0.11 — Multiple Mentors

### Available Mentors

| Mentor | Style | Best For |
|--------|-------|----------|
| **Default** | Balanced, practical | Most users |
| **Elon** | First principles, urgency, brutal honesty | Technical founders |
| **Jobs** | Product obsession, simplicity, design | Product people |
| **Buffett** | Value investing, long-term thinking | Financial decisions |
| **Custom** | User-defined (Founder tier only) | Advanced users |

### Mentor Selection

```
┌─────────────────────────────────────────────────────────┐
│  Choose Your Mentor                                     │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐  │
│  │          │ │          │ │          │ │          │  │
│  │  DEFAULT │ │   ELON   │ │   JOBS   │ │ BUFFETT  │  │
│  │          │ │          │ │          │ │          │  │
│  │ Balanced │ │ Urgency  │ │ Product  │ │  Value   │  │
│  │ Practical│ │ 1st Prin.│ │ Simplify │ │ Long-term│  │
│  │          │ │          │ │          │ │          │  │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘  │
│       ✓                                                 │
│                                                         │
│  [Continue with Default]                                │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Mentor Personalities

```javascript
const MENTORS = {
  default: {
    name: 'Business Mentor',
    style: 'balanced',
    tone: 'supportive but challenging',
    traits: ['practical', 'clear', 'encouraging'],
    systemPrompt: `You are a balanced business mentor...`
  },
  
  elon: {
    name: 'Elon (First Principles)',
    style: 'intense',
    tone: 'direct, urgent, challenging',
    traits: ['first-principles', 'urgent', 'brutally honest'],
    phrases: [
      "If a timeline is long, it's wrong.",
      "The best part is no part.",
      "Why does it cost that much?"
    ],
    systemPrompt: `You embody Elon Musk's approach...`
  },
  
  jobs: {
    name: 'Steve (Product)',
    style: 'obsessive',
    tone: 'passionate, perfectionist',
    traits: ['simplicity', 'design-focused', 'user-obsessed'],
    phrases: [
      "Simple can be harder than complex.",
      "Design is how it works.",
      "Would you be proud of this?"
    ],
    systemPrompt: `You embody Steve Jobs' approach...`
  },
  
  buffett: {
    name: 'Warren (Value)',
    style: 'patient',
    tone: 'folksy, wise, long-term',
    traits: ['value-focused', 'patient', 'risk-aware'],
    phrases: [
      "Be fearful when others are greedy.",
      "Price is what you pay. Value is what you get.",
      "Risk comes from not knowing what you're doing."
    ],
    systemPrompt: `You embody Warren Buffett's approach...`
  }
};
```

### Custom Mentor (Founder Tier)

Founder tier users can create custom mentors:

```javascript
const customMentorSchema = {
  name: 'string',
  baseStyle: 'default|elon|jobs|buffett',
  
  // Custom traits
  traits: ['string'],
  
  // Custom phrases
  phrases: ['string'],
  
  // Custom system prompt additions
  customPrompt: 'string',
  
  // What to emphasize
  emphasis: {
    speed: 1-10,
    quality: 1-10,
    risk: 1-10,
    growth: 1-10
  }
};
```

### Deliverables (v0.11)

- [ ] 4 built-in mentors
- [ ] Mentor selection UI
- [ ] Mentor switching mid-conversation
- [ ] Custom mentor creation (Founder tier)
- [ ] Mentor-specific responses

---

## Success Criteria

### v0.10
- [ ] Desktop app runs on macOS, Windows, Linux
- [ ] Chat has CLI feature parity
- [ ] Offline mode works
- [ ] Native look and feel

### v0.11
- [ ] 4 mentors available
- [ ] Distinct personalities in responses
- [ ] Smooth mentor switching
- [ ] Custom mentors work (Founder tier)

---

## Timeline

| Week | Focus |
|------|-------|
| 12 | v0.10 Days 1-5: Tauri setup + Chat interface |
| 13 | v0.10 Days 6-10: Dashboard + Polish |
| 14 | v0.11: Multiple mentors |

---

## Quick Links

- [v0.10 Detailed Plan](./v0.10-gui.md)
- [v0.11 Detailed Plan](./v0.11-mentors.md)
- [Back to Months 2-4](../README.md)
