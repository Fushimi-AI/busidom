# Onboarding System

## Overview

The onboarding process is **personalized** based on whether the user is starting a new venture or adding an existing one. This ensures relevant setup and appropriate guidance from the start.

---

## Onboarding Flow

### Step 1: Venture Selection

**Primary Question:** "Are you starting a new venture or adding an existing one?"

Two distinct paths:
- **New Venture** - Starting from scratch
- **Existing Venture** - Business already in progress

---

## Path A: New Venture Onboarding

**Context:** User is at the very beginning of their entrepreneurship journey

### Onboarding Steps

#### 1. Welcome & Explanation
- Brief intro to business-os
- Explain the stage-based approach
- Introduce mentor concept
- Set expectations for the journey

#### 2. Idea Exploration
**Questions to ask:**
- What problem are you trying to solve?
- Who has this problem?
- Why now? Why you?
- What's your initial solution idea?

**Purpose:** 
- Capture initial thinking
- Help user articulate the idea
- Set baseline for future reference

#### 3. Business Type Selection
- SaaS
- Physical products
- Service business
- Other

**Purpose:** Customize guidance and metrics for business type

#### 4. Set Initial Stage
**Default:** Ideation stage
- Explain what this stage entails
- Show stage checklist
- Set confidence level baseline (typically low at start)

#### 5. Mentor Selection
- Present mentor options
- Allow profile browsing
- Sample interactions
- User selects mentor
- Mentor introduces themselves

#### 6. Business Principles & Models
From user settings:
- Strategic frameworks (First Principles, Blue Ocean, etc.)
- Business model approach (Bootstrapped, VC-backed, etc.)
- Financial approach (Revenue-first, growth-first, etc.)

#### 7. Set Initial Goals
- What do you want to achieve?
- Timeline preferences (flexible)
- Success definition
- Work style preferences

#### 8. Begin Journey
- Mentor gives first guidance
- Present first tasks/actions
- Show dashboard
- Start ideation stage work

### New Venture Mentor Behavior

**Elon Mentor Approach:**
> "So you're starting from zero. Good. No baggage, no bad assumptions. Let's break down your idea to first principles. What's the fundamental problem you're solving?"

**Jobs Mentor Approach:**
> "Starting fresh means you can do this right. First question: is this problem worth solving? Would YOU pay for this solution? Be honest."

---

## Path B: Existing Venture Onboarding

**Context:** User has a business that's already operational or in development

### Onboarding Steps

#### 1. Welcome & Context Setting
- Brief intro to business-os
- Explain we'll assess current state
- Honest assessment helps provide better guidance
- This is confidential, be truthful

#### 2. Business Information Gathering

**Basic Information:**
- Business name
- Business type (SaaS, physical product, etc.)
- When did you start?
- Team size (just you? small team? larger?)
- Current status (idea, prototype, launched, scaling?)

#### 3. Current Stage Assessment

**Diagnostic Questions:**

**Ideation/Validation:**
- Have you validated the problem with real customers?
- Do you have evidence people will pay for this?
- What research have you done?

**Product/MVP:**
- Do you have a working product/prototype?
- Can customers use it today?
- Is it generating value?

**Launch/Traction:**
- Do you have customers/users?
- Are they paying customers?
- What's your retention rate?

**Growth/Scaling:**
- Monthly revenue?
- Growth rate?
- Team size and structure?
- What's working? What's not?

#### 4. Metrics Collection

**Financial:**
- Monthly revenue (if any)
- Expenses / burn rate
- Runway
- Funding raised (if any)

**Customer:**
- Number of customers/users
- Acquisition channels
- Retention/churn
- Growth trend

**Product:**
- Development status
- Key features shipped
- Technical debt level
- Quality issues

#### 5. Challenge & Gap Identification

**Mentor asks probing questions:**
- What's blocking your growth?
- What keeps you up at night?
- Where do you need help most?
- What have you been avoiding?

#### 6. Stage Placement & Assessment

**Mentor determines:**
- What stage is the business truly at?
- Confidence level for that stage
- Whether foundations are solid
- If earlier stage work needs revisiting

**Honest Assessment:**
> "You say you're ready to scale, but your retention is 40%. That's a product problem. We need to go back to Testing stage and fix core issues before scaling."

#### 7. Mentor Selection

Same as new venture:
- Present mentor options
- Allow profile browsing
- User selects mentor

#### 8. Business Principles & Configuration

- Set strategic frameworks
- Business model alignment
- Financial approach
- Configure what needs immediate focus

#### 9. Prioritization & Action Plan

**Mentor helps identify:**
- Top 3 priorities
- Quick wins available
- Critical issues to address
- What to focus on first

#### 10. Begin Guided Work

- Set up in appropriate stage
- Configure dashboard with relevant metrics
- Create initial tasks
- Start working with mentor guidance

### Existing Venture Mentor Behavior

**Elon Mentor Approach:**
> "Let's see where you really are. What's your monthly revenue? Burn rate? Growth rate? Don't sugarcoat it. I need real numbers to help you."

**Jobs Mentor Approach:**
> "Tell me about your product. But more importantly - are people using it? Do they love it? Because if they're not delighted, everything else is premature."

**On Finding Gaps:**

**Elon:**
> "You've been in 'launch prep' for 6 months. That's too long. You're overthinking it. We're moving you back to MVP stage with a 2-week deadline to ship something. Anything."

**Jobs:**
> "Your product has 50 features and none of them are great. We're going back to basics. Pick the ONE thing that matters most and make that wonderful. Cut everything else."

---

## Key Differences Between Paths

### New Venture
- ✅ Clean slate, no baggage
- ✅ Proper foundation from start
- ✅ Learn correct principles early
- ✅ Follow stages sequentially
- ⚠️ Less context to work with initially

### Existing Venture  
- ✅ Immediate value - help with current challenges
- ✅ Can assess real metrics and progress
- ✅ Identify blind spots
- ✅ Course-correct if needed
- ⚠️ May need to revisit earlier stages
- ⚠️ Possible bad habits to unlearn

---

## Personalization Elements

### Based on Venture Type
- **New:** Focus on validation and foundations
- **Existing:** Focus on gaps and acceleration

### Based on Business Type
- **SaaS:** Emphasize MRR, churn, LTV:CAC
- **Physical Products:** Emphasize unit economics, inventory, margins
- **Services:** Emphasize delivery, capacity, pricing

### Based on Stage
- **Early (Ideation/Research):** Validation focus
- **Mid (MVP/Testing):** Product and user focus
- **Late (Launch/Growth):** Scaling and efficiency focus

### Based on Mentor
- **Elon:** Technical depth, speed, first principles
- **Jobs:** Product quality, user experience, craft

### Based on Goals
- **Lifestyle Business:** Profitability and sustainability
- **High Growth:** Scaling and metrics
- **Social Impact:** Mission and contribution

---

## Onboarding Success Metrics

**New Venture:**
- User completes full onboarding
- Initial idea documented
- First stage tasks created
- User engages with mentor in first session

**Existing Venture:**
- Accurate stage placement
- Key metrics captured
- Priority issues identified
- User feels understood and helped

---

## Technical Implementation Notes

### Data Collection
- Store venture type (new vs. existing)
- Store all onboarding responses
- Create initial business profile
- Set stage and confidence level

### Mentor Integration
- Load selected mentor personality
- Initialize mentor context with user's situation
- Enable mentor to reference onboarding data
- Personalize communication style

### Stage Configuration
- If new: Start at Ideation
- If existing: Place at assessed stage
- Set confidence level appropriately
- Configure stage-specific checklists

### Dashboard Setup
- Show relevant metrics for business type
- Hide irrelevant sections for early stage
- Display immediate priorities
- Show next actions clearly

---

## Notes

The onboarding must:
- Be thorough but not overwhelming
- Gather enough context to provide value
- Set accurate expectations
- Create trust through honest assessment
- Get user to first value quickly

**For new ventures:** Get them excited and started right

**For existing ventures:** Provide immediate value and clarity on current state
