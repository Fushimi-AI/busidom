# Phase: Optimization (Week 8)

**Goal:** Reduce API costs without losing quality

---

## v0.7 — Cost Optimization

### Why This Matters

Without optimization:
- Token usage grows linearly with conversation length
- All queries use most expensive model
- No visibility into costs
- Unsustainable for users and business

With optimization:
- **40-60% cost reduction**
- Smart model routing
- Transparent usage tracking
- Sustainable growth

---

## Optimization Strategies

### 1. Token Usage Tracking

Track every token spent:

```javascript
async function trackUsage(userId, businessId, usage) {
  await db.usage.create({
    userId,
    businessId,
    promptTokens: usage.prompt_tokens,
    completionTokens: usage.completion_tokens,
    totalTokens: usage.total_tokens,
    model: usage.model,
    cost: calculateCost(usage),
    timestamp: new Date()
  });
}

function calculateCost(usage) {
  const rates = {
    'gpt-4o': { input: 0.005, output: 0.015 },
    'gpt-4o-mini': { input: 0.00015, output: 0.0006 },
    'gpt-3.5-turbo': { input: 0.0005, output: 0.0015 }
  };
  
  const rate = rates[usage.model];
  return (
    (usage.prompt_tokens / 1000) * rate.input +
    (usage.completion_tokens / 1000) * rate.output
  );
}
```

### 2. Query Classification

Not all queries need GPT-4:

| Query Type | Example | Model | Cost |
|------------|---------|-------|------|
| Simple | "What's my business stage?" | gpt-4o-mini | $0.00015/1K |
| Medium | "Analyze my pricing strategy" | gpt-4o-mini | $0.00015/1K |
| Complex | "Create a go-to-market plan" | gpt-4o | $0.005/1K |

```javascript
async function classifyQuery(query) {
  // Simple heuristics first
  if (query.length < 50) return 'simple';
  if (query.includes('analyze') || query.includes('strategy')) return 'medium';
  if (query.includes('plan') || query.includes('comprehensive')) return 'complex';
  
  // LLM classification for ambiguous
  const classification = await classifyWithLLM(query);
  return classification;
}

function selectModel(classification) {
  const models = {
    simple: 'gpt-4o-mini',
    medium: 'gpt-4o-mini',
    complex: 'gpt-4o'
  };
  return models[classification];
}
```

**Expected Savings:** 40-60% (most queries are simple/medium)

### 3. Context Compression

Reduce context size before sending:

```javascript
async function compressContext(messages) {
  // 1. Summarize old messages
  const oldMessages = messages.slice(0, -10);
  const recentMessages = messages.slice(-10);
  
  if (oldMessages.length > 0) {
    const summary = await summarizeMessages(oldMessages);
    return [
      { role: 'system', content: `Summary of past: ${summary}` },
      ...recentMessages
    ];
  }
  
  return messages;
}

async function summarizeMessages(messages) {
  const response = await openai.chat.completions.create({
    model: 'gpt-4o-mini',  // Use cheap model for summarization
    messages: [
      { role: 'system', content: 'Summarize this conversation in 2-3 sentences.' },
      ...messages
    ],
    max_tokens: 200
  });
  
  return response.choices[0].message.content;
}
```

**Expected Savings:** 30-50% on long conversations

### 4. Semantic Deduplication

Don't include redundant context:

```javascript
async function deduplicateContext(messages, queryEmbedding) {
  // Embed all messages
  const embeddings = await Promise.all(
    messages.map(m => generateEmbedding(m.content))
  );
  
  // Find semantically unique messages
  const unique = [];
  const threshold = 0.85;  // Similarity threshold
  
  for (let i = 0; i < messages.length; i++) {
    const isDuplicate = unique.some(u => 
      cosineSimilarity(embeddings[i], embeddings[u.index]) > threshold
    );
    
    if (!isDuplicate) {
      unique.push({ ...messages[i], index: i });
    }
  }
  
  return unique;
}
```

**Expected Savings:** 10-20% on repetitive conversations

### 5. Caching

Cache common responses:

```javascript
const cache = new Map();

async function getCachedOrCompute(key, computeFn, ttl = 3600) {
  const cached = cache.get(key);
  
  if (cached && Date.now() - cached.timestamp < ttl * 1000) {
    return cached.value;
  }
  
  const value = await computeFn();
  cache.set(key, { value, timestamp: Date.now() });
  return value;
}

// Usage
const businessSummary = await getCachedOrCompute(
  `business-summary-${businessId}`,
  () => generateBusinessSummary(businessId),
  3600  // Cache for 1 hour
);
```

**Expected Savings:** 5-10% on repeated queries

---

## Cost Dashboard

### User-Facing Display

```
┌─────────────────────────────────────────────────────────┐
│  Token Usage & Costs                                    │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  This Month                                             │
│  ────────────                                           │
│  Used: $12.45 / $25.00 budget                          │
│  ███████████████░░░░░░░░░░░░░░░░ 50%                   │
│                                                         │
│  Savings This Month                                     │
│  ──────────────────                                     │
│  Model routing:    $8.20 saved (42%)                   │
│  Context compression: $4.10 saved (21%)                │
│  Total saved:      $12.30 (55%)                        │
│                                                         │
│  Without optimization: $24.75                          │
│  With optimization:    $12.45                          │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Database Schema

```sql
CREATE TABLE usage_logs (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id),
  business_id INTEGER REFERENCES businesses(id),
  
  -- Token tracking
  prompt_tokens INTEGER NOT NULL,
  completion_tokens INTEGER NOT NULL,
  total_tokens INTEGER NOT NULL,
  
  -- Cost tracking
  model VARCHAR(50) NOT NULL,
  cost_actual DECIMAL(10, 6) NOT NULL,
  cost_without_optimization DECIMAL(10, 6),
  
  -- Classification
  query_type VARCHAR(20),  -- simple, medium, complex
  compression_applied BOOLEAN DEFAULT false,
  cache_hit BOOLEAN DEFAULT false,
  
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE monthly_usage (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id),
  month DATE NOT NULL,
  total_tokens INTEGER DEFAULT 0,
  total_cost DECIMAL(10, 4) DEFAULT 0,
  total_saved DECIMAL(10, 4) DEFAULT 0,
  budget_limit DECIMAL(10, 4),
  UNIQUE(user_id, month)
);
```

---

## Budget Limits

### Per-Tier Limits

| Tier | Monthly Budget | Token Limit |
|------|----------------|-------------|
| Starter ($25) | $22.50 (90%) | ~150M tokens |
| Pro ($199) | $179.10 (90%) | ~1.2B tokens |
| Founder ($999) | $899.10 (90%) | ~6B tokens |

### Budget Enforcement

```javascript
async function checkBudget(userId) {
  const usage = await getMonthlyUsage(userId);
  const limit = await getBudgetLimit(userId);
  
  if (usage.totalCost >= limit) {
    throw new BudgetExceededError(
      `Monthly budget of $${limit} exceeded. ` +
      `Upgrade to Pro for more capacity.`
    );
  }
  
  if (usage.totalCost >= limit * 0.8) {
    // Warn at 80%
    notifyUser(userId, 'budget_warning', {
      used: usage.totalCost,
      limit: limit
    });
  }
  
  return { remaining: limit - usage.totalCost };
}
```

---

## Deliverables

- [ ] Token tracking on all API calls
- [ ] Query classification system
- [ ] Model routing logic
- [ ] Context compression
- [ ] Caching layer
- [ ] Cost dashboard (CLI + GUI)
- [ ] Budget limits and warnings
- [ ] Monthly usage reports

---

## Success Criteria

| Metric | Target |
|--------|--------|
| Cost reduction | ≥ 40% |
| Query classification accuracy | ≥ 85% |
| Cache hit rate | ≥ 10% |
| Budget warning accuracy | 100% |

---

## Timeline

| Day | Focus |
|-----|-------|
| 1 | Token tracking + database schema |
| 2 | Query classification + model routing |
| 3 | Context compression |
| 4 | Caching + deduplication |
| 5 | Cost dashboard + budget limits |
| 6-7 | Testing + optimization |

---

## Quick Links

- [v0.7 Detailed Plan](./v0.7-cost.md)
- [Back to Months 2-4](../README.md)
