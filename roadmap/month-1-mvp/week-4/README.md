# Week 4: MVP Launch (v0.4)

**Version:** 0.4 (MVP)  
**Ship by:** End of Week 4  
**Lines of Code:** ~100 (bug fixes, polish)  
**Depends on:** v0.3 ✅

---

## Goal

**SHIP IT.**

No new features. Only:
1. Bug fixes
2. Polish
3. 5 real users
4. Public launch

---

## Why This Matters

> "If you're not embarrassed by the first version of your product, you've launched too late." — Reid Hoffman

Week 4 is not about building. It's about:
- **Validating** with real humans
- **Learning** what actually matters
- **Deciding** if we continue

---

## Daily Breakdown

### Days 1-2: Internal Testing + Bug Fixes

**Day 1 Tasks:**
- [ ] Fresh install on clean machine
- [ ] Test full user journey (first session to snapshot)
- [ ] Document all bugs found
- [ ] Prioritize: critical → high → medium → low
- [ ] Fix critical bugs

**Day 2 Tasks:**
- [ ] Fix high-priority bugs
- [ ] Test edge cases
- [ ] Improve error messages
- [ ] Final code review
- [ ] Prepare for beta

**Bug Severity Guide:**
| Severity | Definition | Action |
|----------|------------|--------|
| Critical | App crashes, data loss | Fix immediately |
| High | Feature doesn't work | Fix before beta |
| Medium | Annoying but works | Fix if time |
| Low | Nice to have | Log for later |

---

### Days 3-4: Beta Testing with 5 Users

**Preparation:**
- [ ] Identify 5 target users (founders you know)
- [ ] Prepare setup instructions
- [ ] Create feedback form
- [ ] Schedule 30-minute sessions

**Beta User Criteria:**
- Real entrepreneurs (not just friends)
- Building something currently
- Willing to give honest feedback
- Available for 30-minute session

**Beta Session Structure:**
1. **Setup (5 min):** Help them install
2. **First Session (15 min):** Let them use it naturally
3. **Feedback (10 min):** Structured questions

**Feedback Questions:**
1. What was your first impression?
2. Did you get value from the first session?
3. Would you use this again? Why/why not?
4. What was confusing?
5. What's missing?
6. Would you recommend this to a friend?

**What to Watch:**
- Where do they hesitate?
- What questions do they ask?
- When do they smile/frown?
- Do they want to continue?

---

### Days 5-6: Iterate on Feedback

**Day 5 Tasks:**
- [ ] Synthesize feedback from all 5 users
- [ ] Identify common themes
- [ ] Prioritize fixes/changes
- [ ] Implement top 3 improvements
- [ ] Update documentation

**Day 6 Tasks:**
- [ ] Final bug fixes
- [ ] Polish README
- [ ] Prepare launch materials
- [ ] Final internal test
- [ ] Prepare launch post

**Feedback Synthesis Template:**
```
## User Feedback Summary

### What Worked
- [Common positive feedback]

### What Didn't Work
- [Common issues]

### Requests
- [Common feature requests - LOG, don't build]

### Surprises
- [Unexpected observations]

### Validation Status
- Did they return? Y/N
- Would they recommend? Y/N
- NPS (0-10): X
```

---

### Day 7: LAUNCH

**Launch Checklist:**
- [ ] All critical bugs fixed
- [ ] README complete and clear
- [ ] Setup works in < 5 minutes
- [ ] At least 1 beta user willing to return
- [ ] Public repository ready
- [ ] Launch announcement prepared

**Launch Activities:**
- [ ] Push to public GitHub
- [ ] Post on Twitter/X
- [ ] Post on relevant communities (Indie Hackers, etc.)
- [ ] Notify waitlist (if any)
- [ ] Monitor for issues

**Launch Announcement Template:**
```
🚀 Launched: Business-OS v0.4 (MVP)

Your AI co-founder for entrepreneurs.

Unlike generic AI:
✅ Opinionated - challenges weak ideas
✅ Persistent - remembers your business
✅ Action-oriented - delivers insights, not just advice

Try it: [link]

Built in public. Feedback welcome.
```

---

## Validation Criteria

### Must Have (Ship Blocker)
- [ ] 5 users complete first session
- [ ] Zero critical bugs
- [ ] Setup takes < 5 minutes
- [ ] README explains what it does

### Should Have
- [ ] At least 1 user returns voluntarily
- [ ] Positive feedback on personality
- [ ] Users understand the value prop

### Nice to Have
- [ ] Users share with others
- [ ] Feature requests (signal of interest)
- [ ] Offer to pay (strongest signal)

---

## Decision Framework

**At end of Week 4, decide:**

| Signal | Count | Decision |
|--------|-------|----------|
| Users who returned | 0 | **Kill or major pivot** |
| Users who returned | 1-2 | **Investigate + iterate** |
| Users who returned | 3+ | **Continue to v0.5** |

### If Killing
- Document learnings
- Thank users for feedback
- Move to next idea or pivot

### If Pivoting
- Identify what didn't work
- Propose 3 alternative approaches
- Validate before building

### If Continuing
- Plan v0.5 (database + accounts)
- Set up development infrastructure
- Start building momentum

---

## Success Metrics

| Metric | Target | Actual |
|--------|--------|--------|
| Beta users tested | 5 | ⬜ |
| Users who returned | ≥1 | ⬜ |
| Critical bugs at launch | 0 | ⬜ |
| Setup time | < 5 min | ⬜ |
| First-session completion | > 80% | ⬜ |

---

## What NOT to Do

❌ **Don't add new features**
- Week 4 is for validation, not building

❌ **Don't ignore negative feedback**
- If users don't like it, understand why

❌ **Don't skip the decision**
- Make a clear continue/pivot/kill decision

❌ **Don't launch without users**
- At least 5 real tests before public launch

❌ **Don't optimize prematurely**
- Ship, learn, then optimize

---

## MVP Definition

> A CLI tool where entrepreneurs get opinionated, context-aware guidance from an AI co-founder that remembers everything and challenges weak thinking.

### Features
- ✅ CLI chat interface
- ✅ Conversation memory (persists across sessions)
- ✅ Opinionated mentor personality
- ✅ First-principles thinking
- ✅ Auto-extract business context
- ✅ First-session value (< 5 minutes)
- ✅ Business snapshot generation

### Commands
- `/help` - Show commands
- `/clear` - Clear conversation
- `/history` - Show recent messages
- `/snapshot` - Show business snapshot
- `/context` - Show extracted context
- `/exit` - Quit

---

## Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Can't find 5 beta users | Start reaching out Day 1 |
| Critical bug found Day 6 | Don't launch, fix first |
| No users return | Have pivot options ready |
| Negative reception | Learn and iterate, don't give up |

---

## After Launch

### Week 5 and Beyond (if validated)

1. **Set up analytics** - Track usage patterns
2. **Create feedback loop** - Regular user check-ins
3. **Plan v0.5** - Database + user accounts
4. **Build in public** - Share progress, build audience

### Ongoing Metrics to Track

- Daily active users
- Session completion rate
- Return rate (% who use twice+)
- Feature requests
- Bug reports

---

## Quick Links

- [Detailed Tasks →](./TASKS.md)
- [Launch Checklist →](./LAUNCH_CHECKLIST.md)
- [Feedback Template →](./FEEDBACK_TEMPLATE.md)
- [Back to Month 1 →](../README.md)
