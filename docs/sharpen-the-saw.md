---
layout: default
title: How To Sharpen the Saw
---

# How To Sharpen the Saw

Sustainable velocity requires periodic consolidation. This section shows you how to prompt AI to help maintain quality while moving fast.

**Proven by evidence:** Projects that consolidated every 10-15 PRs maintained 3-11 PRs/day velocity for weeks. Those that skipped consolidation saw velocity drop by 50% after 20-30 PRs.

## The Consolidation Pattern

Every 10-15 feature PRs, have AI help you consolidate.

### How to Prompt for Consolidation

Focus on **what needs attention**, not how to organize the work (AI handles that).

**What to include in your prompt:**
- **Which PRs** to review
- **Specific gaps** you've noticed (missing tests, outdated docs)
- **Known issues** (flaky tests, duplicated code)
- **Quality goals** (coverage target, performance)

**Example from dikuclient PR #15:**
```markdown
"Consolidation checkpoint after PRs #1-14.

Gaps noticed:
- PRs #8, #11, #13 lack tests
- README outdated (missing new commands)
- One flaky connection test
- Color codes feature undocumented

Goals:
- Coverage from 45% to 68%
- All features documented
- No flaky tests

Focus on quality, not new features"
```

**Why it worked:** Specific gaps, clear goals, explicit scope (no new features).

Every 10-15 feature PRs, pause to consolidate. This isn't "slowing down"—it's maintaining the capacity to move fast.

### What is a Consolidation PR?

A checkpoint that:
- Adds tests for recent features
- Updates documentation
- Fixes flaky tests
- Pays down technical debt
- Creates validation tools
- Verifies everything still works together

**Not**: New features, architectural changes, or scope expansion.

### The 10-15 PR Rhythm

**Why this frequency?**
- Short enough: Debt doesn't compound exponentially
- Long enough: Batch related improvements efficiently
- Predictable: Team knows consolidation is coming

**Evidence from projects:**
- dikuclient PR #15: "Verify and document barebones implementation"
- DikuMUD PR #122: Comprehensive quest summary documentation
- morpheum: Multiple testing/stabilization phases between feature pushes

### Consolidation PR Template

```markdown
# PR: Consolidate Phase [N] Work

## Testing
- [ ] Add tests for features from PR #X-Y
- [ ] Fix flaky test in [module]
- [ ] Increase coverage from [X]% to [Y]%
- [ ] Add integration test for [workflow]

## Documentation  
- [ ] Update README with new features
- [ ] Document [complex feature] in detail
- [ ] Add examples for [API]
- [ ] Update VISION if direction shifted

## Technical Debt
- [ ] Refactor [duplicated code]
- [ ] Improve error messages in [module]
- [ ] Remove deprecated [feature]
- [ ] Optimize [slow operation]

## Validation
- [ ] Run full test suite
- [ ] Check all examples still work
- [ ] Verify performance benchmarks
- [ ] Test on fresh install

## Reflection
What worked well in last 10-15 PRs?
What should we do differently?
What patterns emerged that we should codify?
```

## Testing Consolidation

Tests should grow with features, but occasionally need focused attention.

### Test Debt Indicators

You have test debt when:
- Coverage is decreasing
- Tests are flaky (pass/fail inconsistently)
- Tests take too long to run
- Tests don't catch real bugs
- Tests are brittle (break on unrelated changes)

### Test Consolidation Checklist

**Coverage gaps:**
```bash
# Find untested code
pytest --cov=src --cov-report=html
# Open htmlcov/index.html
# Add tests for red sections
```

**Flaky tests:**
```bash
# Run test 10 times
for i in {1..10}; do pytest tests/test_flaky.py || break; done

# If fails sometimes:
# 1. Identify timing/race conditions
# 2. Add explicit waits or mocks
# 3. Make deterministic
```

**Slow tests:**
```bash
# Profile test time
pytest --durations=10

# Speed up by:
# - Using fixtures more effectively
# - Mocking expensive operations
# - Parallelizing with pytest-xdist
```

### Test Growth Pattern

**Healthy growth** (morpheum example):
- PR #1-20: 50 → 150 tests (foundation)
- PR #21-50: 150 → 280 tests (features)
- PR #51-76: 280 → 353 tests (edge cases, integration)

Tests grew steadily with features.

## Documentation Consolidation

Documentation rots fast. Periodic refresh keeps it accurate.

### Documentation Checklist

**README accuracy:**
- [ ] Installation steps work on fresh system
- [ ] Usage examples are current
- [ ] Dependencies are up to date
- [ ] Screenshots/output match current version

**API documentation:**
- [ ] All public functions documented
- [ ] Examples show actual usage
- [ ] Error conditions explained
- [ ] Breaking changes highlighted

**Vision alignment:**
- [ ] VISION still reflects actual direction
- [ ] Success criteria updated based on learnings
- [ ] New principles added if emerged

### Documentation Prompt

```markdown
Review and update documentation after recent changes:

PRs since last update: #X through #Y

Please:
1. Check README examples still work
2. Update any outdated screenshots/output
3. Document new features added in [PR list]
4. Fix any broken links
5. Ensure installation steps are current

Test each example by actually running it.
```

## Technical Debt Management

Not all debt is bad. The key is conscious choice and periodic paydown.

### Conscious Debt vs Unconscious Debt

**Conscious debt** (acceptable):
```python
# TODO(PR #47): Optimize this algorithm
# Current O(n²) implementation works for n < 100
# Will need O(n log n) when we add feature X
def slow_but_working(data):
    # Simple implementation
    pass
```

You know:
- What the debt is
- Why you took it on
- What triggers paydown
- How to fix it

**Unconscious debt** (dangerous):
- Code that's confusing but "works"
- Workarounds nobody understands
- Copy-pasted code with subtle variations
- Dependencies on deprecated features

### Debt Paydown Priority

**High priority** (fix in consolidation PR):
- Security vulnerabilities
- Data corruption risks
- Flaky tests affecting CI
- Confusing code in critical paths
- Duplicated logic (3+ copies)

**Medium priority** (plan for next phase):
- Performance optimizations (if measurable impact)
- API inconsistencies (if causing confusion)
- Missing error handling (if users hit it)
- Code smells (if slowing development)

**Low priority** (note for future):
- Premature optimizations
- Aesthetic preferences
- "Nice to have" refactorings
- Speculative improvements

### Debt Paydown Prompt

```markdown
Technical debt review for consolidation:

Focus areas:
1. [Module X] has duplicated logic in 3 places
2. [Function Y] is confusing (see TODO comment)
3. [Test Z] is flaky (passes 70% of time)

For each:
1. Explain why it's debt (what's wrong)
2. Propose minimal fix
3. Estimate impact if we don't fix
4. Recommend priority (high/medium/low)

Don't implement yet—just analyze and recommend.
```

## Performance and Optimization

Optimize based on evidence, not speculation.

### When to Optimize

**Don't optimize when:**
- No users complaining
- No metrics showing problem
- "Feels like it could be faster"
- Pre-optimizing for scale you don't have

**Do optimize when:**
- Users report slow operations
- Benchmarks show regression
- Operations exceed time budgets
- Profiling identifies hotspots

### Optimization Process

```bash
# 1. Measure first
$ time npm run operation
# 3.2 seconds

# 2. Profile
$ npm run profile-operation
# Identified: Database query in loop (N+1 problem)

# 3. Optimize
# Move query outside loop

# 4. Measure again  
$ time npm run operation
# 0.8 seconds (4x improvement)

# 5. Add benchmark test
def test_operation_performance():
    start = time.time()
    run_operation()
    duration = time.time() - start
    assert duration < 1.0, f"Too slow: {duration}s"
```

**Key**: Measure before and after. No speculation.

## Reflection and Learning

The most important consolidation activity: learning from what happened.

### Reflection Questions

**After each consolidation:**

**What worked well?**
- Which prompts led to quick, quality results?
- What patterns emerged naturally?
- Which practices should we continue?

**What was challenging?**
- Where did we iterate more than expected?
- What caused confusion or rework?
- What should we do differently?

**What did we learn?**
- Any new patterns worth codifying?
- Changes to VISION or principles?
- Tools or techniques to adopt?

### Capture Learnings

**Update copilot-instructions.md:**
```markdown
## Learnings from Phase 2 (PR #16-30)

### What Worked
- Test-first for API endpoints (1-2 commits consistently)
- Design docs for complex features (prevented 2 refactors)

### What Didn't Work
- Starting features without clear success criteria (led to scope creep)

### New Patterns
- Always include example usage in PR description
- Run integration tests before marking PR ready

### Adjustments
- Updated prompt template to require success criteria
- Added integration test step to checklist
```

### Learning Prompt

```markdown
Reflection on PRs #X-Y:

Analyze these PRs for patterns:
1. Which completed in 1-3 commits? What made them smooth?
2. Which took 6+ commits? What caused extra iteration?
3. Did any prompts work particularly well? Extract patterns.
4. Any anti-patterns emerged? What to avoid?

Format findings as:
- Patterns to continue
- Patterns to avoid  
- Lessons learned
- Recommended adjustments
```

## Maintenance Rituals

Build these into your rhythm:

### Daily
- Run tests before starting new work
- Check CI status (address failures quickly)
- Review yesterday's PRs (any follow-up needed?)

### Weekly
- Dependency updates (security patches)
- Check issue backlog (anything urgent?)
- Review metrics (velocity, test coverage, build time)

### Every 10-15 PRs (Consolidation)
- Test coverage audit
- Documentation refresh
- Technical debt paydown
- Reflection and learning capture

### Monthly
- VISION alignment check (still on track?)
- Success criteria review (achieved any? need updates?)
- Major dependency upgrades (if needed)
- Performance benchmarking

## Sustainable Velocity

The goal isn't maximum speed—it's sustainable speed.

### Signs of Unsustainable Pace

**Burnout indicators:**
- Every PR feels like a struggle
- Tests breaking frequently
- Documentation falling behind
- Technical debt growing

**Quality degradation:**
- Bugs in recent features
- Flaky tests increasing
- Regressions in old features
- Customer complaints up

**Process breakdown:**
- Skipping tests "just this once"
- Merging without review
- Taking shortcuts on documentation
- Deferring consolidation

### Signs of Sustainable Pace

**Healthy rhythm:**
- PRs feel productive, not frantic
- Tests provide confidence
- Documentation stays current
- Quality is consistent

**Improving over time:**
- Velocity stable or increasing
- Commits per PR decreasing
- Technical debt stable or decreasing
- Team confidence high

**Process working:**
- Consolidation happens on schedule
- Tests catch issues early
- Documentation helps onboarding
- Learnings get captured

## Sharpen the Saw Checklist

You're maintaining well when:

- Consolidation happens every 10-15 PRs (not skipped)
- Test coverage grows with features (not shrinks)
- Documentation matches reality (not stale)
- Technical debt is conscious (not surprising)
- Velocity feels sustainable (not frantic)
- Learnings get captured (not forgotten)

## Common Pitfalls

### Skipping Consolidation
"We're on a roll, let's keep going!"

**Result**: Technical debt compounds, velocity drops, quality suffers.

**Fix**: Treat consolidation as mandatory, not optional.

### Premature Optimization
"This could be faster, let's refactor!"

**Result**: Time spent on non-problems, real issues ignored.

**Fix**: Optimize based on evidence (metrics, profiling, user reports).

### Perfect Code Obsession
"This needs complete rewrite before we can continue."

**Result**: Endless refactoring, no forward progress.

**Fix**: Pay down debt incrementally during consolidation.

### Documentation Debt
"We'll document it when we're done."

**Result**: Documentation never happens, or is wrong.

**Fix**: Small doc updates in consolidation PRs.

## Example Consolidation Timeline

**dikuclient Phase 2 Consolidation (PR #15):**

**Before consolidation** (PR #1-14):
- 14 feature PRs merged
- Test coverage: 45%
- Some features undocumented
- One flaky test
- README outdated

**Consolidation PR #15:**
1. Added tests for PRs #8, #11, #13 (coverage → 68%)
2. Fixed flaky connection test
3. Updated README with new commands
4. Documented color codes feature
5. Removed deprecated websocket option
6. Ran full test suite on fresh install

**Result**: Solid foundation for Phase 3 development

**After consolidation** (PR #16-45):
- Higher velocity (2.8 commits/PR vs 6.3 in Phase 1)
- Fewer bugs
- Documentation current
- Tests reliable

**Investment**: 1 consolidation PR enabled 30 faster feature PRs.

## What's Next?

You've completed the journey:

- **[Getting Started](getting-started.html)**: Foundation (README, VISION, MVP)
- **[Staying Organized](staying-organized.html)**: Design-first development
- **[Leveling Up](leveling-up.html)**: Rapid iteration patterns
- **[Sharpen the Saw](sharpen-the-saw.html)**: Sustainable velocity

**Now**: Apply these practices to your projects. Start with Getting Started, progress through each level, and remember—consolidate every 10-15 PRs!

---

<small>**Evidence sources**: [dikuclient](https://github.com/anicolao/dikuclient) PR #15 (consolidation example), [DikuMUD](https://github.com/anicolao/DikuMUD) PR #122 (documentation consolidation), [morpheum](https://github.com/anicolao/morpheum) test growth trajectory, velocity metrics from all case studies showing sustainable pace.</small>
