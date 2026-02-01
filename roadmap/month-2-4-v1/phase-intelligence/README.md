# Phase: Intelligence (Weeks 9-11)

**Goal:** Multi-agent system with business stage awareness

---

## Overview

| Version | Focus | Duration |
|---------|-------|----------|
| **v0.8** | Multi-Agent Orchestration | 2 weeks |
| **v0.9** | Business Stages + Quality Gates | 1 week |

---

## v0.8 — Multi-Agent Orchestration

### Why Multi-Agent?

Single AI = one perspective, one capability

Multi-Agent = specialized expertise, better results

| Agent | Specialty | When Active |
|-------|-----------|-------------|
| **Mentor** | Strategic guidance, first principles | Default, always available |
| **Research** | Market analysis, competitor research | When user needs data |
| **Analytics** | Metrics, KPIs, financial modeling | When discussing numbers |
| **Sales** | Customer conversations, objection handling | When discussing sales |
| **Marketing** | Positioning, messaging, channels | When discussing growth |

### Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      USER REQUEST                            │
└────────────────────────────┬────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────┐
│                     ORCHESTRATOR                             │
│  • Classify request                                          │
│  • Select appropriate agent(s)                               │
│  • Manage context                                            │
│  • Aggregate responses                                       │
│  • Ensure confidence ≥ 8.5                                   │
└────────────────────────────┬────────────────────────────────┘
                             │
         ┌───────────────────┼───────────────────┐
         │                   │                   │
         ▼                   ▼                   ▼
┌─────────────┐      ┌─────────────┐      ┌─────────────┐
│   MENTOR    │      │  RESEARCH   │      │  ANALYTICS  │
│   AGENT     │      │   AGENT     │      │   AGENT     │
│             │      │             │      │             │
│ First       │      │ Market data │      │ Metrics     │
│ principles  │      │ Competitors │      │ Financials  │
│ Strategy    │      │ Trends      │      │ Forecasts   │
└─────────────┘      └─────────────┘      └─────────────┘
```

### Agent Definition Schema

```javascript
const AgentSchema = {
  id: 'research',
  name: 'Research Agent',
  description: 'Market intelligence and data analysis',
  
  // When to activate
  triggers: [
    'market size', 'competitors', 'research',
    'industry', 'trends', 'data'
  ],
  
  // System prompt
  systemPrompt: `You are a research specialist...`,
  
  // Tools this agent can use
  tools: ['web_search', 'data_analysis'],
  
  // Model preference
  preferredModel: 'gpt-4o',
  
  // Confidence threshold
  minConfidence: 8.5,
  
  // Max iterations to reach confidence
  maxIterations: 3
};
```

### Confidence Scoring

Every agent output must have confidence ≥ 8.5:

```javascript
async function executeAgent(agent, request) {
  let response = null;
  let confidence = 0;
  let iterations = 0;
  
  while (confidence < 8.5 && iterations < agent.maxIterations) {
    response = await agent.execute(request, {
      previousResponse: response,
      feedback: confidence < 8.5 ? 'Improve confidence' : null
    });
    
    confidence = await evaluateConfidence(response, request);
    iterations++;
  }
  
  return { response, confidence, iterations };
}
```

### Deliverables (v0.8)

- [ ] Agent abstraction layer
- [ ] Orchestrator routing logic
- [ ] 3 initial agents (Mentor, Research, Analytics)
- [ ] Confidence scoring system
- [ ] Agent handoff protocol
- [ ] Per-agent context isolation

---

## v0.9 — Business Stages + Quality Gates

### Business Stages

| Stage | Definition | Key Questions |
|-------|------------|---------------|
| **Idea** | Concept only, no product | Is this problem worth solving? |
| **MVP** | Building or launched MVP | Does anyone want this? |
| **Growth** | Has customers, growing | How do we scale this? |
| **Scale** | Established, optimizing | How do we maximize efficiency? |

### Quality Gates

Users cannot progress stages without passing gates:

```javascript
const QualityGates = {
  idea_to_mvp: {
    required: [
      'problem_validated',      // Talked to 10+ potential customers
      'solution_hypothesis',    // Clear hypothesis to test
      'founder_fit_assessed',   // Skills match the challenge
      'differentiation_clear'   // Know what makes this unique
    ],
    blocking: [
      'no_target_customer',     // Can't describe ideal customer
      'solution_searching'      // Solution looking for problem
    ]
  },
  
  mvp_to_growth: {
    required: [
      'users_acquired',         // Has paying/active users
      'retention_signal',       // Users coming back
      'unit_economics_known',   // Understand cost per user
      'growth_channel_tested'   // Know one channel that works
    ],
    blocking: [
      'premature_scaling',      // Scaling without retention
      'vanity_metrics_only'     // Only tracking DAU, not value
    ]
  },
  
  growth_to_scale: {
    required: [
      'repeatable_acquisition', // Can predictably get customers
      'positive_unit_economics',// Making money per customer
      'team_in_place',          // Not solo anymore
      'systems_documented'      // Processes written down
    ],
    blocking: [
      'founder_bottleneck',     // Everything requires founder
      'manual_processes'        // Can't scale with people
    ]
  }
};
```

### Stage-Aware Prompting

```javascript
function getStagePrompt(stage) {
  const prompts = {
    idea: `The user is in IDEA stage. Focus on:
      - Problem validation
      - Customer discovery
      - First principles thinking
      - Challenging assumptions
      DO NOT discuss: scaling, hiring, funding rounds`,
    
    mvp: `The user is in MVP stage. Focus on:
      - Building minimum viable product
      - Getting first users
      - Measuring retention
      - Iterating based on feedback
      DO NOT discuss: optimization, multiple products`,
    
    growth: `The user is in GROWTH stage. Focus on:
      - Scaling acquisition channels
      - Improving unit economics
      - Building team
      - Process documentation
      DO NOT discuss: premature optimization`,
    
    scale: `The user is in SCALE stage. Focus on:
      - Operational efficiency
      - Team scaling
      - Market expansion
      - Competitive moats`
  };
  
  return prompts[stage];
}
```

### Idiot Index Integration

Track cost vs. value for business decisions:

```javascript
async function calculateIdiotIndex(business) {
  // Gather cost data
  const monthlyCosts = await getCosts(business.id);
  
  // Estimate value delivered
  const valueMetrics = await getValueMetrics(business.id);
  
  // Calculate Idiot Index (cost/value ratio)
  const idiotIndex = monthlyCosts / valueMetrics.mrr;
  
  // Ideal: < 0.3 (costs less than 30% of revenue)
  // Warning: 0.3-0.5
  // Critical: > 0.5
  
  return {
    idiotIndex,
    status: idiotIndex < 0.3 ? 'healthy' : idiotIndex < 0.5 ? 'warning' : 'critical',
    recommendations: generateRecommendations(idiotIndex, monthlyCosts)
  };
}
```

### Deliverables (v0.9)

- [ ] Stage detection/assessment
- [ ] Quality gate implementation
- [ ] Stage-appropriate prompting
- [ ] Idiot Index calculator
- [ ] Stage progression recommendations
- [ ] Anti-pattern detection

---

## Success Criteria

### v0.8
- [ ] Orchestrator routes to correct agent 90%+
- [ ] All agent outputs have confidence ≥ 8.5
- [ ] Agents can hand off to each other
- [ ] Context isolation working

### v0.9
- [ ] Stage detection accuracy > 85%
- [ ] Quality gates block premature progression
- [ ] Stage-appropriate guidance delivered
- [ ] Idiot Index calculated and displayed

---

## Timeline

| Week | Focus |
|------|-------|
| 9 | v0.8 Days 1-5: Orchestrator + Agent abstraction |
| 10 | v0.8 Days 6-10: Confidence scoring + 3 agents |
| 11 | v0.9: Stages + Quality gates |

---

## Quick Links

- [v0.8 Detailed Plan](./v0.8-agents.md)
- [v0.9 Detailed Plan](./v0.9-stages.md)
- [Back to Months 2-4](../README.md)
