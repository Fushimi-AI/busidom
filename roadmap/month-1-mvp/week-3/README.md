# Week 3: Intelligence (v0.3)

**Version:** 0.3  
**Ship by:** End of Week 3  
**Lines of Code:** ~400  
**Depends on:** v0.2 ✅

---

## Goal

Make the AI intelligent about your business:
1. Auto-extract business info from conversation
2. Build structured business context
3. Guarantee first-session value
4. Deliver actionable insight in 5 minutes

---

## Why This Matters

Research shows:
- **75% of users churn in first week** without value
- **24 hours** to create "aha moment"
- **First 5 minutes** determine if they come back

We must:
- Understand the business WITHOUT asking 20 questions
- Deliver value FAST
- Create a tangible artifact (business snapshot)

---

## Two Sub-Goals

### 1. Context Extraction (Auto-learn)
Extract business information automatically from conversation:
- Business name
- Industry/type
- Stage (idea/mvp/growth/scale)
- Current challenges
- Goals
- Founder background

### 2. First-Session Value (Guarantee impact)
Every first session must deliver:
- One challenged assumption
- One actionable insight
- One business snapshot document

---

## Daily Breakdown

### Day 1: Context Schema + Extractor Design

**Tasks:**
- [ ] Design business context schema
- [ ] Create extractor module structure
- [ ] Implement extraction prompts
- [ ] Test extraction accuracy

**Deliverables:**
- `src/context/extractor.js`
- `data/business.json` schema
- Extraction prompt templates

**Time:** 4-5 hours

---

### Day 2: Auto-Extraction Implementation

**Tasks:**
- [ ] Implement real-time extraction during chat
- [ ] Add confidence scoring for extractions
- [ ] Handle conflicting information
- [ ] Update business.json automatically

**Deliverables:**
- Working auto-extraction
- Confidence-based updates
- Business context persisted

**Time:** 5-6 hours

---

### Day 3: First-Session Flow Design

**Tasks:**
- [ ] Design first-session conversation flow
- [ ] Create guided onboarding prompts
- [ ] Implement session state tracking
- [ ] Build quick assessment (3 questions)

**Deliverables:**
- `src/onboarding/first-session.js`
- First-session state machine
- Assessment question set

**Time:** 5-6 hours

---

### Day 4: Business Snapshot Generator

**Tasks:**
- [ ] Design snapshot template
- [ ] Implement snapshot generation
- [ ] Add `/snapshot` command
- [ ] Test end-to-end first session

**Deliverables:**
- `src/templates/business-snapshot.md`
- Snapshot generation logic
- Working `/snapshot` command

**Time:** 4-5 hours

---

### Day 5: Integration + Value Delivery

**Tasks:**
- [ ] Integrate all components
- [ ] Ensure value delivery in < 5 minutes
- [ ] Add first-session completion tracking
- [ ] Polish user experience

**Deliverables:**
- Fully integrated v0.3
- < 5 minute time to value
- Completion tracking

**Time:** 4-5 hours

---

### Days 6-7: Testing + Refinement

- [ ] Test with mock users
- [ ] Refine extraction accuracy
- [ ] Improve first-session flow
- [ ] Fix bugs

---

## Business Context Schema

```javascript
// data/business.json

{
  "version": "0.3",
  "created": "2024-01-15T10:30:00Z",
  "updated": "2024-01-15T14:20:00Z",
  
  "business": {
    "name": "TechStartup",
    "industry": "B2B SaaS",
    "stage": "idea",  // idea | mvp | growth | scale
    "description": "AI-powered analytics for SMBs",
    "confidence": 0.85
  },
  
  "founder": {
    "background": "technical",  // technical | business | mixed
    "experience": "first-time",  // first-time | serial | experienced
    "skills": ["coding", "product"],
    "gaps": ["sales", "marketing"],
    "confidence": 0.7
  },
  
  "challenges": [
    {
      "description": "Finding first customers",
      "severity": "high",
      "extractedAt": "2024-01-15T10:35:00Z"
    }
  ],
  
  "goals": [
    {
      "description": "Launch MVP in 3 months",
      "timeframe": "3 months",
      "extractedAt": "2024-01-15T10:40:00Z"
    }
  ],
  
  "assumptions": [
    {
      "statement": "SMBs will pay $50/month for analytics",
      "challenged": false,
      "extractedAt": "2024-01-15T10:45:00Z"
    }
  ],
  
  "insights": [
    {
      "content": "Focus on one vertical before going broad",
      "deliveredAt": "2024-01-15T11:00:00Z",
      "acknowledged": true
    }
  ],
  
  "sessions": {
    "first": {
      "completedAt": "2024-01-15T11:30:00Z",
      "valueDelivered": true,
      "snapshotGenerated": true
    },
    "count": 1,
    "lastAt": "2024-01-15T11:30:00Z"
  }
}
```

---

## Context Extraction Logic

```javascript
// src/context/extractor.js

const EXTRACTION_PROMPTS = {
  businessName: `Based on this conversation, what is the business name? 
    Return JSON: {"name": "...", "confidence": 0.0-1.0} or null if not mentioned.`,
  
  industry: `Based on this conversation, what industry/type of business is this?
    Return JSON: {"industry": "...", "confidence": 0.0-1.0} or null if unclear.`,
  
  stage: `Based on this conversation, what stage is this business?
    Options: idea (just an idea), mvp (building/launched MVP), growth (has customers, growing), scale (established, scaling)
    Return JSON: {"stage": "...", "confidence": 0.0-1.0}`,
  
  challenges: `Based on this conversation, what challenges is the founder facing?
    Return JSON: {"challenges": [{"description": "...", "severity": "high|medium|low"}]}`,
  
  assumptions: `Based on this conversation, what assumptions is the founder making that should be challenged?
    Return JSON: {"assumptions": [{"statement": "..."}]}`
};

export async function extractContext(messages, existingContext) {
  const recentMessages = messages.slice(-10);  // Focus on recent
  
  const extractions = await Promise.all([
    extractField('businessName', recentMessages),
    extractField('industry', recentMessages),
    extractField('stage', recentMessages),
    extractField('challenges', recentMessages),
    extractField('assumptions', recentMessages)
  ]);
  
  return mergeExtractions(existingContext, extractions);
}

function mergeExtractions(existing, extractions) {
  // Only update if new extraction has higher confidence
  // or fills a gap
  for (const extraction of extractions) {
    if (!extraction) continue;
    
    if (!existing[extraction.field] || 
        extraction.confidence > existing[extraction.field].confidence) {
      existing[extraction.field] = extraction.value;
    }
  }
  
  return existing;
}
```

---

## First-Session Flow

```javascript
// src/onboarding/first-session.js

const FIRST_SESSION_FLOW = {
  stages: ['greeting', 'assessment', 'challenge', 'insight', 'snapshot'],
  
  greeting: {
    message: `Welcome to Business-OS! I'm your AI co-founder.
    
Unlike generic AI, I'm here to challenge your thinking, not just agree with you.

Let me learn about your business with 3 quick questions. Then I'll give you one actionable insight and a snapshot of what I understand.

Ready?`,
    next: 'assessment'
  },
  
  assessment: {
    questions: [
      "In one sentence, what are you building and for whom?",
      "What's the one problem you're trying to solve right now?",
      "If this succeeds wildly, what does that look like in 6 months?"
    ],
    next: 'challenge'
  },
  
  challenge: {
    // AI challenges one assumption based on answers
    prompt: `Based on the user's answers, identify ONE assumption they're making and challenge it constructively.`,
    next: 'insight'
  },
  
  insight: {
    // AI provides one actionable insight
    prompt: `Based on everything so far, provide ONE specific, actionable insight. Not generic advice—something they can do today.`,
    next: 'snapshot'
  },
  
  snapshot: {
    // Generate and save business snapshot
    action: 'generateSnapshot',
    message: `Here's what I've learned about your business. I've saved this to your business snapshot.
    
Type /snapshot anytime to see or update it.

Now, what would you like to work on?`
  }
};
```

---

## Business Snapshot Template

```markdown
# Business Snapshot
Generated: {date}

## Your Business
**Name:** {business.name}
**Industry:** {business.industry}
**Stage:** {business.stage}

## Your Focus
**Main Challenge:** {challenges[0].description}
**6-Month Goal:** {goals[0].description}

## Key Assumption to Test
> {assumptions[0].statement}

**Why this matters:** This assumption underlies your strategy. If wrong, the whole plan changes.

## First Insight
{insights[0].content}

## Recommended Next Steps
1. {nextStep1}
2. {nextStep2}
3. {nextStep3}

---
*Updated by Business-OS on {date}*
```

---

## Success Criteria

| Criteria | Status |
|----------|--------|
| Auto-extracts business name from conversation | ⬜ |
| Auto-extracts industry/stage | ⬜ |
| Auto-extracts challenges | ⬜ |
| First session completes in < 5 minutes | ⬜ |
| Delivers one challenged assumption | ⬜ |
| Delivers one actionable insight | ⬜ |
| Generates business snapshot | ⬜ |
| User wants to come back | ⬜ |

---

## Commands Added

| Command | Action |
|---------|--------|
| `/snapshot` | Show current business snapshot |
| `/context` | Show extracted business context |
| `/reset-context` | Clear business context (keep chat) |

---

## Test Scenarios

### Scenario 1: Complete First Session
1. Start fresh (no context)
2. Answer 3 assessment questions
3. Receive challenged assumption
4. Receive actionable insight
5. Snapshot generated

**Expected time:** < 5 minutes

### Scenario 2: Context Persistence
1. Mention business name in conversation
2. Close app
3. Reopen
4. AI remembers business name

### Scenario 3: Gradual Extraction
1. Don't answer all questions upfront
2. Chat naturally about business
3. Context fills in over time

---

## Dependencies on v0.2

- ✅ Mentor personality working
- ✅ First principles embedded
- ✅ Challenges weak thinking
- Intelligence adds context awareness

---

## Files Changed/Added

```
src/
├── context/
│   └── extractor.js       ← NEW
├── onboarding/
│   └── first-session.js   ← NEW
├── templates/
│   └── business-snapshot.md ← NEW
├── prompts/
│   ├── mentor.js          ← UPDATE (context-aware)
│   └── principles.js      ← Same
├── cli.js                 ← UPDATE (new commands)
└── memory.js              ← UPDATE (business context)

data/
├── context.json           ← Same (chat history)
└── business.json          ← NEW (business context)
```

---

## Metrics to Track

| Metric | Target |
|--------|--------|
| Time to first insight | < 5 minutes |
| Context extraction accuracy | > 80% |
| First-session completion rate | > 90% |
| Snapshot generation success | 100% |

---

## Quick Links

- [Detailed Tasks →](./TASKS.md)
- [Technical Specification →](./TECH_SPEC.md)
- [Onboarding Research →](../../research/onboarding-research.md)
- [Back to Month 1 →](../README.md)
