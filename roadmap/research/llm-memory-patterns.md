# LLM Memory & Context Management Research

**Source:** OpenAI Documentation, Developer Community, Production Best Practices  
**Research Date:** January 2026

---

## Key Findings

### 1. OpenAI Conversation State Options

**Three Approaches:**

| Approach | Best For | Complexity |
|----------|----------|------------|
| **Chat Completions API** | Manual control, custom logic | Medium |
| **Assistants API + Threads** | Built-in state management | Low |
| **Responses API** | Conversation support | Low |

**Recommendation for MVP:** Chat Completions API with manual JSON storage
- Full control over context
- No vendor lock-in
- Easy to migrate to database later

---

### 2. Context Management Strategies

#### 2.1 Rolling Window
Keep last N messages. Simple but loses old context.

```javascript
const MAX_MESSAGES = 50;
const context = messages.slice(-MAX_MESSAGES);
```

**Pros:** Simple, predictable token usage  
**Cons:** Loses early important context

#### 2.2 Summarization
Summarize old messages, keep recent detailed.

```javascript
const context = [
  { role: 'system', content: systemPrompt },
  { role: 'system', content: `Summary of past: ${summary}` },
  ...recentMessages.slice(-20)
];
```

**Pros:** Preserves context semantically  
**Cons:** Requires summarization calls (cost)

#### 2.3 Semantic Retrieval (RAG)
Store messages in vector DB, retrieve relevant ones.

**Pros:** Optimal context selection  
**Cons:** Complex, requires v0.6+ (vector DB)

**Recommendation for MVP:** Rolling window with optional summarization
- Implement rolling window in v0.1
- Add summarization in v0.7 (cost optimization)
- Add semantic retrieval in v0.6 (vector DB)

---

### 3. Token Management

#### Token Estimation
- ~4 tokens per word (English average)
- ~1.3 tokens per character (code)

```javascript
function estimateTokens(text) {
  return Math.ceil(text.split(/\s+/).length * 1.3);
}
```

#### Budget Allocation

| Component | Token Budget |
|-----------|--------------|
| System prompt | 500-1000 |
| Business context | 500-1000 |
| Conversation history | 2000-4000 |
| User message | Variable |
| **Total target** | **< 6000** |

---

### 4. Production Best Practices

**From OpenAI:**

1. **Retry with exponential backoff** for rate limits
2. **Set reasonable max_tokens** to control costs
3. **Use streaming** for better UX on long responses
4. **Log token usage** for cost tracking
5. **Handle API errors gracefully**

**Implementation:**

```javascript
import OpenAI from 'openai';

const openai = new OpenAI();

async function sendMessage(messages, retries = 3) {
  for (let i = 0; i < retries; i++) {
    try {
      const response = await openai.chat.completions.create({
        model: process.env.OPENAI_MODEL || 'gpt-4o-mini',
        messages,
        max_tokens: 1000,
        temperature: 0.7
      });
      
      return {
        content: response.choices[0].message.content,
        usage: response.usage
      };
    } catch (error) {
      if (error.status === 429 && i < retries - 1) {
        const waitTime = Math.pow(2, i) * 1000;
        await new Promise(r => setTimeout(r, waitTime));
        continue;
      }
      throw error;
    }
  }
}
```

---

### 5. Memory Architecture for Business-OS

#### MVP (v0.1-v0.4)
```
┌─────────────────────────────────────────┐
│              JSON Files                  │
│  ┌─────────────┐  ┌─────────────┐       │
│  │ context.json│  │business.json│       │
│  │ (messages)  │  │ (context)   │       │
│  └─────────────┘  └─────────────┘       │
└─────────────────────────────────────────┘
```

#### v0.5+ (Database)
```
┌─────────────────────────────────────────┐
│              PostgreSQL                  │
│  ┌─────────────┐  ┌─────────────┐       │
│  │ messages    │  │ businesses  │       │
│  │ table       │  │ table       │       │
│  └─────────────┘  └─────────────┘       │
└─────────────────────────────────────────┘
```

#### v0.6+ (Vector DB)
```
┌─────────────────────────────────────────┐
│           PostgreSQL + pgvector         │
│  ┌─────────────┐  ┌─────────────┐       │
│  │ Structured  │  │ Embeddings  │       │
│  │ data        │  │ (vectors)   │       │
│  └─────────────┘  └─────────────┘       │
│                  │                       │
│                  ▼                       │
│         Semantic Search                  │
└─────────────────────────────────────────┘
```

---

### 6. External Storage Considerations

**Options for session persistence:**
- **JSON files** — MVP, single user (v0.1-v0.4)
- **SQLite** — Local-first, offline (v0.6.1)
- **PostgreSQL** — Multi-user, production (v0.5+)
- **Supabase/Firebase** — Managed, quick setup

**Recommendation:** 
- Start with JSON (v0.1)
- Migrate to PostgreSQL (v0.5)
- Add pgvector (v0.6)

---

## Application to Business-OS

### v0.1 Implementation

1. **JSON file storage** for messages
2. **Rolling window** (last 50 messages)
3. **System prompt** always first
4. **Token estimation** for budget awareness
5. **Retry logic** with exponential backoff

### Future Enhancements

| Version | Enhancement |
|---------|-------------|
| v0.5 | PostgreSQL migration |
| v0.6 | pgvector semantic search |
| v0.7 | Summarization for token reduction |
| v0.8 | Per-agent context isolation |

---

## References

1. [OpenAI Conversation State Guide](https://platform.openai.com/docs/guides/conversation-state)
2. [OpenAI Production Best Practices](https://platform.openai.com/docs/guides/production-best-practices)
3. [OpenAI Agents Guide](https://platform.openai.com/docs/guides/agents)
