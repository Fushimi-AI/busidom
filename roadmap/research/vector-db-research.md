# Vector Database & Semantic Search Research

**Source:** pgvector documentation, Timescale, Red Gate  
**Research Date:** January 2026

---

## Overview

**pgvector** is an open-source PostgreSQL extension for vector similarity search.

| Metric | Value |
|--------|-------|
| GitHub Stars | 19.5k |
| Version (2025) | 0.8.1 |
| Optimal Scale | 1M - 50M vectors |
| Language SDKs | Python, Node.js, Go, .NET, C++, Elixir |

---

## Why pgvector for Business-OS

### Advantages

1. **Single Database** — No separate vector DB to manage
2. **SQL Integration** — Combine vector + structured queries
3. **Cost Effective** — No additional service costs
4. **Proven** — Used by major companies
5. **Node.js SDK** — Easy integration

### When NOT to Use

- Billions of vectors with millisecond latency
- No existing PostgreSQL infrastructure
- Need specialized vector-only features

**For Business-OS:** pgvector is ideal (< 50M vectors expected)

---

## Core Capabilities

### 1. Vector Storage

Store embeddings directly in PostgreSQL:

```sql
CREATE TABLE documents (
  id SERIAL PRIMARY KEY,
  content TEXT,
  embedding VECTOR(1536)  -- OpenAI embedding dimension
);
```

### 2. Similarity Search

Find semantically similar content:

```sql
SELECT content, 
       embedding <-> query_embedding AS distance
FROM documents
ORDER BY embedding <-> query_embedding
LIMIT 5;
```

### 3. Distance Metrics

| Operator | Metric | Use Case |
|----------|--------|----------|
| `<->` | L2 (Euclidean) | Default, most common |
| `<#>` | Inner product | Normalized vectors |
| `<=>` | Cosine distance | Text similarity |

**Recommendation:** Use cosine distance (`<=>`) for text embeddings

---

## Implementation Architecture

### v0.6 Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    APPLICATION                           │
│  ┌─────────────────────────────────────────────────┐    │
│  │           Node.js + OpenAI SDK                   │    │
│  │  ┌─────────────┐  ┌─────────────┐               │    │
│  │  │ Chat Logic  │  │ Embedding   │               │    │
│  │  │             │  │ Generator   │               │    │
│  │  └─────────────┘  └─────────────┘               │    │
│  └─────────────────────────────────────────────────┘    │
└────────────────────────┬────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────┐
│                  PostgreSQL + pgvector                   │
│  ┌─────────────────────┐  ┌─────────────────────┐      │
│  │   STRUCTURED        │  │   VECTOR            │      │
│  │   ───────────       │  │   ──────            │      │
│  │   users             │  │   message_embeddings │      │
│  │   businesses        │  │   context_vectors    │      │
│  │   messages          │  │   knowledge_base     │      │
│  │   sessions          │  │                     │      │
│  └─────────────────────┘  └─────────────────────┘      │
│                                                          │
│         UNIFIED QUERY LAYER                              │
│         ────────────────────                             │
│         "Find messages about pricing that I discussed    │
│          in the last week" (semantic + time filter)      │
└─────────────────────────────────────────────────────────┘
```

---

## Embedding Strategy

### What to Embed

| Content Type | Embed? | Why |
|--------------|--------|-----|
| User messages | ✅ Yes | Semantic search over history |
| AI responses | ✅ Yes | Find relevant past advice |
| Business context | ✅ Yes | Retrieve relevant business info |
| System prompts | ❌ No | Static, not searched |

### Embedding Model

**Recommendation:** `text-embedding-3-small` (OpenAI)
- 1536 dimensions
- Good quality/cost balance
- $0.02 / 1M tokens

```javascript
const response = await openai.embeddings.create({
  model: 'text-embedding-3-small',
  input: text
});
const embedding = response.data[0].embedding;
```

---

## Database Schema

### Messages Table (Structured)

```sql
CREATE TABLE messages (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id),
  business_id INTEGER REFERENCES businesses(id),
  role VARCHAR(20) NOT NULL,  -- 'user', 'assistant', 'system'
  content TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);
```

### Message Embeddings Table (Vector)

```sql
CREATE TABLE message_embeddings (
  id SERIAL PRIMARY KEY,
  message_id INTEGER REFERENCES messages(id) UNIQUE,
  embedding VECTOR(1536) NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Index for fast similarity search
CREATE INDEX ON message_embeddings 
USING ivfflat (embedding vector_cosine_ops)
WITH (lists = 100);
```

---

## Query Patterns

### 1. Semantic Search

```javascript
async function findSimilarMessages(queryText, limit = 5) {
  // Generate query embedding
  const queryEmbedding = await generateEmbedding(queryText);
  
  // Search by similarity
  const result = await db.query(`
    SELECT m.content, m.role, m.created_at,
           me.embedding <=> $1 AS distance
    FROM messages m
    JOIN message_embeddings me ON m.id = me.message_id
    WHERE m.user_id = $2
    ORDER BY me.embedding <=> $1
    LIMIT $3
  `, [queryEmbedding, userId, limit]);
  
  return result.rows;
}
```

### 2. Hybrid Search (Semantic + Structured)

```javascript
async function findRelevantContext(query, filters) {
  const embedding = await generateEmbedding(query);
  
  const result = await db.query(`
    SELECT m.content, m.role, m.created_at,
           me.embedding <=> $1 AS distance
    FROM messages m
    JOIN message_embeddings me ON m.id = me.message_id
    WHERE m.user_id = $2
      AND m.business_id = $3
      AND m.created_at > $4  -- Time filter
    ORDER BY me.embedding <=> $1
    LIMIT $5
  `, [embedding, filters.userId, filters.businessId, filters.since, filters.limit]);
  
  return result.rows;
}
```

---

## Performance Considerations

### Indexing Options

| Index Type | Best For | Trade-off |
|------------|----------|-----------|
| **ivfflat** | 1K-1M vectors | Good accuracy, fast |
| **hnsw** | 1M+ vectors | Better accuracy, more memory |

**Recommendation for MVP:** Start with ivfflat, upgrade to hnsw if needed

### Index Parameters

```sql
-- ivfflat: lists = sqrt(num_vectors)
-- For 100K vectors: lists = 316, use 100 for simplicity
CREATE INDEX ON message_embeddings 
USING ivfflat (embedding vector_cosine_ops)
WITH (lists = 100);

-- For queries, set probes (higher = more accurate, slower)
SET ivfflat.probes = 10;
```

---

## Node.js Integration

### Using pgvector with node-postgres

```javascript
import pg from 'pg';
import pgvector from 'pgvector/pg';

// Register vector type
await pgvector.registerType(client);

// Insert embedding
await client.query(
  'INSERT INTO message_embeddings (message_id, embedding) VALUES ($1, $2)',
  [messageId, pgvector.toSql(embedding)]
);

// Query by similarity
const result = await client.query(
  `SELECT * FROM message_embeddings 
   ORDER BY embedding <=> $1 
   LIMIT 5`,
  [pgvector.toSql(queryEmbedding)]
);
```

---

## Cost Analysis

### Embedding Costs (OpenAI)

| Model | Price | Dimensions |
|-------|-------|------------|
| text-embedding-3-small | $0.02/1M tokens | 1536 |
| text-embedding-3-large | $0.13/1M tokens | 3072 |
| text-embedding-ada-002 | $0.10/1M tokens | 1536 |

**Recommendation:** Use `text-embedding-3-small`

### Example Cost Calculation

- 1000 users
- 50 messages/user/day
- 100 tokens/message average
- Monthly: 1000 × 50 × 30 × 100 = 150M tokens
- Cost: 150M × $0.02/1M = **$3/month**

---

## Application to Business-OS

### v0.6 Implementation Plan

1. **Add pgvector extension** to PostgreSQL
2. **Create embedding tables** for messages
3. **Generate embeddings** on message save
4. **Implement semantic search** for context retrieval
5. **Hybrid queries** for relevant history

### Context Building

```javascript
async function buildContext(userMessage, businessId) {
  // 1. Get recent messages (structured query)
  const recent = await getRecentMessages(businessId, 10);
  
  // 2. Get semantically relevant messages (vector query)
  const relevant = await findSimilarMessages(userMessage, 5);
  
  // 3. Combine, deduplicate, order by relevance
  const context = combineAndDedupe(recent, relevant);
  
  return context;
}
```

---

## Migration Path

### v0.5 → v0.6

1. **Add pgvector extension**
   ```sql
   CREATE EXTENSION vector;
   ```

2. **Create embedding tables**

3. **Backfill embeddings** for existing messages

4. **Update context retrieval** to use semantic search

---

## References

1. [pgvector GitHub](https://github.com/pgvector/pgvector)
2. [PostgreSQL Vector Database Guide](https://dbadataverse.com/tech/postgresql/2025/12/pgvector-postgresql-vector-database-guide)
3. [Building AI-Powered Semantic Search](https://www.red-gate.com/simple-talk/databases/postgresql/how-to-build-an-ai-powered-semantic-search-in-postgresql-with-pgvector/)
4. [Semantic Search with Filters](https://www.timescale.com/blog/what-is-semantic-search-with-filters-and-how-to-implement-it-with-pgvector-and-python)
