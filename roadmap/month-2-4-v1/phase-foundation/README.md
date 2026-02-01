# Phase: Foundation (Weeks 5-7)

**Goal:** Production-ready infrastructure

---

## Overview

| Version | Focus | Duration |
|---------|-------|----------|
| **v0.5** | Database + User Accounts | 2 weeks |
| **v0.6** | Vector DB + Semantic Memory | 1 week |

---

## v0.5 — Database + User Accounts

### Scope

1. **PostgreSQL Setup**
   - Database schema design
   - Connection pooling
   - Migrations framework

2. **User Authentication**
   - Registration/login
   - Password hashing (bcrypt)
   - Session management
   - Password reset

3. **Subscription Management**
   - Stripe integration
   - Tier management (Starter/Pro/Founder)
   - Usage tracking
   - Billing portal

4. **Multi-User Support**
   - Roles (owner, co-founder, advisor, team, viewer)
   - Permissions system
   - Business sharing

5. **Data Migration**
   - JSON to PostgreSQL migration
   - Zero data loss
   - Backward compatibility

### Database Schema

```sql
-- Users
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  name VARCHAR(255),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Subscriptions
CREATE TABLE subscriptions (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id),
  tier VARCHAR(50) NOT NULL,  -- starter, pro, founder
  stripe_subscription_id VARCHAR(255),
  status VARCHAR(50) NOT NULL,  -- active, canceled, past_due
  current_period_end TIMESTAMP,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Businesses
CREATE TABLE businesses (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  industry VARCHAR(255),
  stage VARCHAR(50),  -- idea, mvp, growth, scale
  owner_id INTEGER REFERENCES users(id),
  context JSONB,  -- Extracted business context
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Business Members
CREATE TABLE business_members (
  id SERIAL PRIMARY KEY,
  business_id INTEGER REFERENCES businesses(id),
  user_id INTEGER REFERENCES users(id),
  role VARCHAR(50) NOT NULL,  -- owner, co-founder, advisor, team, viewer
  created_at TIMESTAMP DEFAULT NOW(),
  UNIQUE(business_id, user_id)
);

-- Messages
CREATE TABLE messages (
  id SERIAL PRIMARY KEY,
  business_id INTEGER REFERENCES businesses(id),
  user_id INTEGER REFERENCES users(id),
  role VARCHAR(20) NOT NULL,  -- user, assistant, system
  content TEXT NOT NULL,
  tokens_used INTEGER,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Sessions
CREATE TABLE sessions (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id),
  business_id INTEGER REFERENCES businesses(id),
  started_at TIMESTAMP DEFAULT NOW(),
  ended_at TIMESTAMP,
  messages_count INTEGER DEFAULT 0,
  tokens_used INTEGER DEFAULT 0
);
```

### Tech Stack

| Component | Technology |
|-----------|------------|
| Database | PostgreSQL 16 |
| ORM | Drizzle or Prisma |
| Auth | Passport.js or Auth.js |
| Payments | Stripe |
| Hosting | Supabase, Railway, or self-hosted |

### Deliverables

- [ ] PostgreSQL database running
- [ ] User registration/login working
- [ ] Stripe subscription integration
- [ ] Multi-user roles working
- [ ] JSON data migrated
- [ ] CLI updated to use database

---

## v0.6 — Vector DB + Semantic Memory

### Scope

1. **pgvector Setup**
   - Extension installation
   - Vector columns
   - Indexing (ivfflat)

2. **Embedding Generation**
   - OpenAI embeddings API
   - Batch processing
   - Cost-efficient embedding

3. **Semantic Search**
   - Similarity queries
   - Hybrid queries (vector + structured)
   - Relevance scoring

4. **Context Retrieval**
   - Semantic context building
   - Relevant history selection
   - Deduplication

### Database Additions

```sql
-- Enable pgvector
CREATE EXTENSION vector;

-- Message Embeddings
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

### Embedding Strategy

```javascript
// Generate embedding for message
async function generateEmbedding(text) {
  const response = await openai.embeddings.create({
    model: 'text-embedding-3-small',
    input: text
  });
  return response.data[0].embedding;
}

// Store embedding on message save
async function saveMessage(message) {
  // Save message
  const savedMessage = await db.messages.create(message);
  
  // Generate and save embedding
  const embedding = await generateEmbedding(message.content);
  await db.messageEmbeddings.create({
    messageId: savedMessage.id,
    embedding
  });
  
  return savedMessage;
}
```

### Context Retrieval

```javascript
// Build context using semantic search
async function buildContext(query, businessId, limit = 10) {
  const queryEmbedding = await generateEmbedding(query);
  
  // Hybrid query: semantic + time-based
  const relevant = await db.query(`
    SELECT m.content, m.role, m.created_at,
           me.embedding <=> $1 AS distance
    FROM messages m
    JOIN message_embeddings me ON m.id = me.message_id
    WHERE m.business_id = $2
    ORDER BY 
      (me.embedding <=> $1) * 0.7 +  -- 70% semantic
      EXTRACT(EPOCH FROM NOW() - m.created_at) / 86400 * 0.3  -- 30% recency
    LIMIT $3
  `, [queryEmbedding, businessId, limit]);
  
  return relevant.rows;
}
```

### Deliverables

- [ ] pgvector extension installed
- [ ] Embedding generation working
- [ ] Semantic search functional
- [ ] Hybrid queries working
- [ ] Context retrieval improved

---

## Success Criteria

### v0.5
- [ ] New users can register and login
- [ ] Subscriptions work end-to-end
- [ ] Multi-user roles functional
- [ ] Zero data loss in migration

### v0.6
- [ ] Embeddings generated for all messages
- [ ] Semantic search returns relevant results
- [ ] Context retrieval 50%+ better than random

---

## Timeline

| Week | Focus |
|------|-------|
| 5 | v0.5 Days 1-5: Database + Auth |
| 6 | v0.5 Days 6-10: Subscriptions + Migration |
| 7 | v0.6: Vector DB + Semantic Search |

---

## Quick Links

- [v0.5 Detailed Plan](./v0.5-database.md)
- [v0.6 Detailed Plan](./v0.6-vector.md)
- [Back to Months 2-4](../README.md)
