# Business-OS Test Plan

> Comprehensive testing strategy covering unit, integration, and end-to-end tests

## Testing Strategy

### Test Pyramid

```
        /\
       /E2E\        ← 10 critical user flows
      /──────\
     /  INT   \     ← 30 integration tests
    /──────────\
   /   UNIT     \   ← 200+ unit tests
  /──────────────\
```

### Coverage Targets
- **Unit Tests**: 80%+ coverage
- **Integration Tests**: Critical paths covered
- **E2E Tests**: 10 key user journeys
- **Performance Tests**: Key operations benchmarked

---

## Phase 0: Foundation

### Unit Tests

**0.1 Project Setup**
```typescript
describe('Package Configuration', () => {
  test('npm install succeeds')
  test('typescript compiles without errors')
  test('eslint runs without errors')
  test('all dependencies resolve')
})
```

**0.2 CI/CD Pipeline**
```typescript
describe('GitHub Actions', () => {
  test('lint job passes on valid code')
  test('lint job fails on invalid code')
  test('test job runs all tests')
  test('build job creates dist/')
})
```

**0.3 Core Architecture**
```typescript
describe('Result Pattern', () => {
  test('success result has data')
  test('error result has error object')
  test('result helpers work correctly')
})

describe('Error Classes', () => {
  test('AppError has correct properties')
  test('ValidationError extends AppError')
  test('error codes are unique')
})

describe('DI Container', () => {
  test('registers and resolves services')
  test('throws on unregistered service')
  test('singleton pattern works')
})
```

**0.4 Basic CLI**
```typescript
describe('REPL', () => {
  test('starts and accepts input')
  test('/help shows commands')
  test('/quit exits gracefully')
  test('handles Ctrl+C')
  test('input history works')
})
```

**0.5 Configuration**
```typescript
describe('Config Loading', () => {
  test('loads from .env')
  test('loads from config file')
  test('env overrides file')
  test('validates required fields')
  test('throws on invalid config')
  test('defaults applied correctly')
})
```

### Integration Tests

**Phase 0 Integration**
```typescript
describe('Foundation Integration', () => {
  test('CLI starts with valid config', async () => {
    const cli = new REPL(config);
    await cli.start();
    expect(cli.isRunning()).toBe(true);
  })

  test('CLI fails fast on invalid config', async () => {
    expect(() => new REPL({})).toThrow(ConfigError);
  })
})
```

---

## Phase 1: MVP Core

### Unit Tests

**1.1 Chat Interface**
```typescript
describe('ChatService', () => {
  test('send message adds to history')
  test('stream yields chunks')
  test('history returns all messages')
  test('clear history empties array')
  test('handles LLM errors gracefully')
})

describe('StreamHandler', () => {
  test('displays streamed chunks')
  test('returns full response')
  test('handles stream errors')
})
```

**1.2 LLM Integration**
```typescript
describe('OpenAIProvider', () => {
  test('chat returns message')
  test('stream yields chunks')
  test('handles 429 rate limit')
  test('handles 401 auth error')
  test('handles timeout')
  test('no API key in error messages')
})

describe('LLM Factory', () => {
  test('creates OpenAI provider')
  test('creates Kimi provider')
  test('creates Anthropic provider')
  test('throws on unknown provider')
})

describe('Retry Logic', () => {
  test('retries on 429')
  test('retries on 500+')
  test('does not retry on 400')
  test('exponential backoff works')
  test('max retries enforced')
})
```

**1.3 Mentor Personality**
```typescript
describe('MentorService', () => {
  test('uses mentor system prompt')
  test('challenges weak ideas')
  test('asks probing questions')
  test('gives specific actions')
  test('adapts to stage')
})
```

**1.4 Context Extraction**
```typescript
describe('ContextExtractor', () => {
  test('extracts business name')
  test('detects stage correctly')
  test('identifies challenges')
  test('identifies goals')
  test('returns confidence score')
  test('handles ambiguous input')
})

describe('ContextService', () => {
  test('updates from messages')
  test('merges with existing context')
  test('saves to storage')
  test('loads from storage')
})
```

**1.5 Session Memory**
```typescript
describe('JSONStorageService', () => {
  test('saves conversation')
  test('loads conversation')
  test('lists conversations')
  test('handles corrupted JSON')
  test('creates directory if missing')
})

describe('MemoryService', () => {
  test('adds message')
  test('starts new conversation')
  test('loads conversation')
  test('auto-saves')
  test('generates title')
})
```

### Integration Tests

**Phase 1 Integration**
```typescript
describe('MVP Core Integration', () => {
  test('end-to-end chat flow', async () => {
    const user = await createTestUser();
    const chat = new ChatService(llm, mentorPrompt);

    const response = await chat.send("I have an idea for an app");

    expect(response.success).toBe(true);
    expect(response.data.role).toBe('assistant');
    expect(response.data.content.length).toBeGreaterThan(0);
  })

  test('context extraction from conversation', async () => {
    const messages = [
      { role: 'user', content: 'I want to build a CRM for dentists' },
      { role: 'assistant', content: 'Tell me more about the problem' },
      { role: 'user', content: 'Dentists struggle with patient scheduling' },
    ];

    const context = await contextExtractor.extract(messages);

    expect(context.industry).toContain('dental');
    expect(context.stage).toBe('idea');
    expect(context.problemStatement).toBeTruthy();
  })

  test('conversation persists across sessions', async () => {
    const memory1 = new MemoryService(storage);
    await memory1.init();
    await memory1.addMessage({ role: 'user', content: 'Hello' });
    await memory1.save();

    const memory2 = new MemoryService(storage);
    await memory2.init();
    const messages = memory2.getMessages();

    expect(messages.length).toBe(1);
    expect(messages[0].content).toBe('Hello');
  })
})
```

---

## Phase 2: Persistence

### Unit Tests

**2.1 PostgreSQL Setup**
```typescript
describe('DatabaseClient', () => {
  test('connects to database')
  test('query returns rows')
  test('queryOne returns single row')
  test('transaction commits')
  test('transaction rolls back on error')
  test('health check returns true')
})

describe('Migrator', () => {
  test('runs pending migrations')
  test('skips applied migrations')
  test('creates migration table')
  test('handles migration failure')
})
```

**2.2 User Auth**
```typescript
describe('AuthService', () => {
  test('register creates user')
  test('register rejects duplicate email')
  test('register validates password length')
  test('login returns tokens')
  test('login fails on wrong password')
  test('verifyToken validates JWT')
  test('refreshToken generates new tokens')
})

describe('UserRepository', () => {
  test('creates user')
  test('finds user by email')
  test('finds user by ID')
  test('password hash not exposed')
})
```

**2.3-2.5 Other Persistence**
```typescript
// Similar patterns for conversation, business, export
describe('ConversationRepository', () => {
  test('creates conversation')
  test('finds by business ID')
  test('updates message count')
  test('pagination works')
})

describe('ExportService', () => {
  test('exports all data')
  test('exports to JSON')
  test('exports to Markdown')
})

describe('ImportService', () => {
  test('imports from file')
  test('validates data')
  test('handles errors gracefully')
})
```

### Integration Tests

**Phase 2 Integration**
```typescript
describe('Persistence Integration', () => {
  test('user registration → login → conversation flow', async () => {
    // Register
    const user = await authService.register({
      email: 'test@example.com',
      password: 'password123'
    });
    expect(user.id).toBeTruthy();

    // Login
    const tokens = await authService.login({
      email: 'test@example.com',
      password: 'password123'
    });
    expect(tokens.accessToken).toBeTruthy();

    // Create business
    const business = await businessService.create(user.id, {
      name: 'Test Business'
    });

    // Create conversation
    const conv = await conversationRepo.create({
      businessId: business.id
    });

    // Add messages
    await messageRepo.create({
      conversationId: conv.id,
      role: 'user',
      content: 'Hello'
    });

    // Verify
    const messages = await messageRepo.findByConversationId(conv.id);
    expect(messages.length).toBe(1);
  })

  test('export → import round-trip', async () => {
    const user = await createTestUser();
    const business = await createTestBusiness(user.id);

    const exported = await exportService.exportAll(user.id);
    expect(exported.businesses.length).toBe(1);

    const result = await importService.importData(exported, user.id);
    expect(result.businessesImported).toBe(1);
  })
})
```

---

## Phase 3: Intelligence

### Unit Tests

**3.1 pgvector**
```typescript
describe('EmbeddingRepository', () => {
  test('inserts embedding')
  test('searches similar vectors')
  test('filters by source type')
  test('pagination works')
  test('deletes by source ID')
})
```

**3.2-3.5 Intelligence Features**
```typescript
describe('EmbeddingService', () => {
  test('embeds single text')
  test('embeds batch')
  test('caches results')
  test('handles API errors')
})

describe('MemoryRetriever', () => {
  test('retrieves similar memories')
  test('filters by threshold')
  test('deduplicates results')
  test('respects token limit')
})

describe('RelevanceScorer', () => {
  test('scores by similarity')
  test('applies recency decay')
  test('weights source types')
  test('topic alignment bonus')
})
```

### Integration Tests

**Phase 3 Integration**
```typescript
describe('Intelligence Integration', () => {
  test('message → embed → retrieve flow', async () => {
    // Add messages
    const messages = [
      'Our target customer is small business owners',
      'We focus on restaurants specifically',
      'They need better inventory management'
    ];

    for (const content of messages) {
      const message = await createMessage(content);
      const embedding = await embeddingService.embed(content);
      await vectorService.store('message', message.id, content, embedding);
    }

    // Search
    const query = "Who are our customers?";
    const results = await memoryRetriever.retrieve(query);

    expect(results.length).toBeGreaterThan(0);
    expect(results[0].content).toContain('small business');
  })

  test('progressive disclosure reduces tokens', async () => {
    const context = createLargeContext();

    const fullTokens = estimateTokens(JSON.stringify(context));

    const { content, tokensSaved } = await progressiveLoader.loadContext(
      businessId,
      context,
      "What's my business?",
      0.5  // Low relevance
    );

    expect(tokensSaved).toBeGreaterThan(fullTokens * 0.3);  // 30%+ savings
  })
})
```

---

## Phase 4: Multi-Agent

### Unit Tests

**4.1-4.5 Agent System**
```typescript
describe('BaseAgent', () => {
  test('executes task')
  test('calls tools')
  test('max iterations enforced')
  test('output validated')
})

describe('MentorAgent', () => {
  test('provides guidance')
  test('challenges assumptions')
  test('delegates to specialists')
})

describe('AgentOrchestrator', () => {
  test('routes to correct agent')
  test('parallel execution')
  test('synthesizes results')
  test('handles failures')
})

describe('ConfidenceScorer', () => {
  test('scores output')
  test('iterates on low scores')
  test('meets threshold')
  test('explains factors')
})
```

### Integration Tests

**Phase 4 Integration**
```typescript
describe('Multi-Agent Integration', () => {
  test('mentor delegates to research agent', async () => {
    const input = "Who are my main competitors?";

    const result = await mentorAgent.chat(input);

    // Verify research agent was called
    expect(mockResearchAgent.execute).toHaveBeenCalled();
    expect(result.output).toContain('competitor');
  })

  test('confidence iteration improves output', async () => {
    const agent = new TestAgent();

    const result = await agent.executeWithConfidence("vague question");

    expect(result.confidence.score).toBeGreaterThanOrEqual(8.5);
    expect(result.confidence.iterations).toBeGreaterThan(1);
  })
})
```

---

## Phase 4.5: Automation & Workflows

### Unit Tests

**4.5.1-4.5.5 Workflows**
```typescript
describe('WorkflowEngine', () => {
  test('starts workflow')
  test('executes steps sequentially')
  test('handles decision branches')
  test('pauses and resumes')
  test('tracks progress')
})

describe('AutomationScheduler', () => {
  test('schedules cron jobs')
  test('checks conditions')
  test('executes automation')
  test('handles failures')
})

describe('EventBus', () => {
  test('publishes events')
  test('triggers actions')
  test('at-least-once delivery')
  test('idempotent execution')
})
```

### Integration Tests

**Phase 4.5 Integration**
```typescript
describe('Workflow Integration', () => {
  test('stage change triggers workflow', async () => {
    await businessService.updateStage(businessId, 'mvp');

    // Wait for event processing
    await delay(100);

    const workflows = await workflowEngine.getActiveWorkflows(businessId);
    expect(workflows.some(w => w.workflowId === 'mvp_scoping_workflow')).toBe(true);
  })

  test('scheduled automation runs', async () => {
    jest.useFakeTimers();

    const automation = {
      id: 'daily_brief',
      schedule: '0 8 * * *',
      tasks: [{ type: 'prompt', message: 'Good morning!' }]
    };

    await scheduler.scheduleAutomation(automation);

    // Advance to 8 AM next day
    jest.advanceTimersByTime(24 * 60 * 60 * 1000);

    expect(mockNotificationService.send).toHaveBeenCalled();
  })
})
```

---

## End-to-End Tests

### Critical User Journeys

**E2E-1: New User Onboarding**
```typescript
test('new user onboarding flow', async () => {
  // 1. Launch app
  await app.launch();

  // 2. Create account
  await app.register('test@example.com', 'password123');

  // 3. Create business
  await app.createBusiness('My Startup');

  // 4. First conversation
  await app.sendMessage("I want to build a CRM");
  const response = await app.waitForResponse();

  expect(response).toContain('problem');

  // 5. Context extracted
  const context = await app.getContext();
  expect(context.businessName).toBe('My Startup');
  expect(context.stage).toBe('idea');
})
```

**E2E-2: Idea Validation Workflow**
```typescript
test('idea validation end-to-end', async () => {
  const user = await setupUser();

  // Start workflow
  await app.startWorkflow('problem_validation');

  // Complete steps
  await app.completeWorkflowStep({
    problem: 'Dentists struggle with scheduling'
  });

  await app.completeWorkflowStep({
    customers: ['Dr. Smith', 'Dr. Jones', /* ... */]
  });

  // Agent research
  await app.waitForAgent('research');

  // Final decision
  await app.makeDecision('yes');

  const status = await app.getWorkflowStatus();
  expect(status).toBe('completed');
})
```

**E2E-3: Multi-Device Sync**
```typescript
test('conversation syncs across devices', async () => {
  // Device 1
  const device1 = await createSession('test@example.com');
  await device1.sendMessage("Hello");

  // Device 2
  const device2 = await createSession('test@example.com');
  const messages = await device2.getMessages();

  expect(messages).toContainEqual(expect.objectContaining({
    content: "Hello"
  }));
})
```

---

## Performance Tests

### Benchmarks

```typescript
describe('Performance Benchmarks', () => {
  test('first message < 500ms', async () => {
    const start = Date.now();
    await chat.send("Hello");
    const duration = Date.now() - start;

    expect(duration).toBeLessThan(500);
  })

  test('vector search < 100ms', async () => {
    await seedDatabase(10000);  // 10K vectors

    const start = Date.now();
    await vectorService.search(queryEmbedding, { limit: 10 });
    const duration = Date.now() - start;

    expect(duration).toBeLessThan(100);
  })

  test('workflow execution < 30s', async () => {
    const start = Date.now();
    await workflowEngine.startWorkflow('test_workflow', businessId);
    const duration = Date.now() - start;

    expect(duration).toBeLessThan(30000);
  })
})
```

---

## Test Execution Plan

### Phase-by-Phase Testing

| Phase | Unit Tests | Integration Tests | Coverage Target |
|-------|------------|-------------------|-----------------|
| 0 | 25 | 2 | 85% |
| 1 | 40 | 3 | 80% |
| 2 | 35 | 4 | 80% |
| 3 | 30 | 2 | 75% |
| 4 | 25 | 3 | 75% |
| 4.5 | 30 | 3 | 75% |
| 5 | 35 | 2 | 70% |
| 6 | 20 | 1 | 80% |
| 7 | 10 | 2 | 70% |

### CI/CD Integration

```yaml
# .github/workflows/test.yml
name: Tests

on: [push, pull_request]

jobs:
  unit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm test -- --coverage
      - uses: codecov/codecov-action@v3

  integration:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: ankane/pgvector
      redis:
        image: redis
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm run test:integration

  e2e:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm run test:e2e
```

---

## Testing Tools

- **Unit**: Vitest
- **Integration**: Vitest + Test Containers
- **E2E**: Playwright
- **Performance**: k6 or Artillery
- **Coverage**: c8 or Istanbul
- **Mocking**: Vitest mocks
- **Fixtures**: Factory Bot pattern

