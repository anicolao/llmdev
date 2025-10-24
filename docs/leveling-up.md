---
layout: default
title: How To Level Up
---

# How To Level Up

Once you've mastered the basics, advanced patterns unlock extraordinary productivity. These techniques come from analyzing projects that sustained 3-11 PRs/day for weeks while maintaining quality.

## Rapid Iteration Culture

Accept "good enough to iterate" over "perfect before merging." Speed comes from tight feedback loops, not from getting it right the first time.

### The 1-3 Commit Sweet Spot

**Target**: 80% of PRs complete in 1-3 commits

**What this means:**
- Requirements are clear enough that AI hits target quickly
- You've scoped work appropriately
- Fast feedback validates you're on track

**Evidence**: Projects achieving this velocity:
- dikuclient: 3.5 PRs/day for 18 days (63 PRs total)
- DikuMUD: 11 PRs/day for 15 days (165 PRs total)
- morpheum: 10 PRs in 17 hours

### When High Iteration is Good

Some PRs naturally take 6-15 commits. This is expected when:

- **Learning new domain**: First websocket integration, first API design
- **Foundation work**: Core abstractions that everything else builds on
- **Complex algorithms**: Spatial validation, graph traversal
- **Integration points**: Connecting multiple systems

**Example**: dikuclient PR #3 took 15 commits building the networking foundation. Every subsequent networking feature took 1-3 commits because foundation was solid.

**Key**: High iteration on foundations → Low iteration on features built on those foundations.

## Specific, Constrained Prompts

Vague prompts get vague results. Specific prompts with constraints get surgical changes.

### The Problem-Context-Solution Structure

```markdown
## Problem
[One specific issue, with example]

The connection drops when [exact scenario].
Example error: [actual error message]

## Context  
[Why it matters, what it affects]

This affects users who [specific use case].
It's related to [relevant code/architecture].

## Solution
[What to do, with constraints]

Fix by [approach], making changes as small as possible.

Constraints:
- Change at most [N] files
- Don't modify [existing functionality]
- Maintain backward compatibility

## Success Criteria
[How to verify it works]

- [ ] Error no longer occurs when [scenario]
- [ ] Existing tests still pass
- [ ] Add test that reproduces original issue
```

### Real Examples

**dikuclient PR #54** (3 commits, <8 hours):
```markdown
Problem: Color codes display as garbage
Context: ANSI escape sequences not being parsed
Solution: Add regex-based color parser
Constraints: As simple as possible, handle basic colors only
```

**DikuMUD** (multiple PRs):
```markdown
Problem: [Specific bug]
Context: [Affected area]
Solution: Make this fix as small as possible
```

Result: Surgical changes, minimal disruption, fast review.

### Constraint Patterns That Work

**Size constraints:**
- "as small as possible"
- "at most 3 files"
- "under 50 lines changed"

**Scope constraints:**
- "only affect [specific module]"
- "don't change existing behavior"
- "maintain current API"

**Quality constraints:**
- "add test that fails first"
- "include example usage"
- "update documentation"

**Verification constraints:**
- "`git grep [pattern]` should find nothing"
- "all tests must pass"
- "benchmark must stay under [X]ms"

## Test-First Development

Don't just add tests—use them to drive development.

### The Test → Implement → Validate Cycle

```bash
# 1. Write the test (shows what you want)
def test_connection_handles_timeout():
    client = Client(timeout=1)
    with pytest.raises(TimeoutError):
        client.connect("slow.server.example.com")
        
# 2. Run it (should fail)
$ pytest tests/test_client.py::test_connection_handles_timeout
# FAILED - TimeoutError not raised

# 3. Implement minimal fix
# (AI implements timeout handling)

# 4. Run again (should pass)
$ pytest tests/test_client.py::test_connection_handles_timeout  
# PASSED

# 5. Run all tests (ensure no regression)
$ pytest
# 51 passed
```

### Test Growth Patterns

**Healthy pattern**: Tests grow alongside features

- morpheum: 50 → 353 tests over 76 PRs
- dikuclient: PR #15 consolidated with test additions
- DikuMUD: 100+ integration tests validate all changes

**Anti-pattern**: Test debt accumulation

- Features added without tests
- "I'll add tests later" (never happens)
- Flaky tests ignored
- Coverage drops over time

### Test Prompt Formula

```markdown
Please add [feature] with test-first approach:

1. First, write a test that demonstrates [desired behavior]
2. Run the test to verify it fails with [expected error]
3. Implement the feature to make the test pass
4. Run all tests to ensure no regressions

The test should validate:
- [ ] Happy path: [scenario]
- [ ] Error case: [scenario]  
- [ ] Edge case: [scenario]
```

## Plan for Refinement Cycles

Major features need follow-up PRs. Budget for them upfront.

### The 1 + 2-3 Pattern

**Initial PR**: Core functionality, "good enough to iterate"
**Follow-up PRs**: Edge cases, polish, integration

**Example: dikuclient networking**
- PR #3: Foundation (15 commits - complex)
- PR #6: Handle disconnection edge case (2 commits)
- PR #7: Add reconnection logic (3 commits)
- PR #8: Improve error messages (1 commit)

**Example: morpheum WebSocket**
- PR #128: Basic WebSocket support (complex)
- Multiple follow-up PRs: Stability, error handling, edge cases

### How to Budget Refinement

When planning a major feature:

```markdown
Phase 1 (PR #N): Core implementation
- [ ] Basic happy path works
- [ ] Key test passes
- [ ] Documented in README

Phase 2 (PR #N+1): Edge cases  
- [ ] Handle error condition X
- [ ] Handle error condition Y
- [ ] Add integration test

Phase 3 (PR #N+2): Polish
- [ ] Improve error messages
- [ ] Add examples
- [ ] Performance optimization
```

**Key insight**: Declaring refinement phases upfront prevents the feeling of "this feature keeps having problems." It's not problems—it's planned iteration.

## Advanced Patterns

### 1. Interface-First Architecture

**Pattern**: Design interfaces before implementations

```typescript
// Step 1: Define interface (PR #1)
interface LLMClient {
  send(prompt: string): Promise<string>;
}

// Step 2: First implementation (PR #2)  
class OpenAIClient implements LLMClient {
  async send(prompt: string) {
    // Implementation
  }
}

// Step 3: Add providers easily (PR #7, #15, #23)
class AnthropicClient implements LLMClient { ... }
class OllamaClient implements LLMClient { ... }
```

**Impact**: morpheum added 4 providers in 1-2 hours each because interface was designed first.

**When to use**: Multiple implementations expected, variation points identified early.

### 2. Progressive Enhancement

**Pattern**: Extend interfaces without breaking existing code

```typescript
// V1: Basic functionality
interface Service {
  process(data: string): Promise<Result>;
}

// V2: Add optional enhancement
interface Service {
  process(data: string): Promise<Result>;
  processStreaming?(data: string, callback: (chunk: string) => void): Promise<Result>;
}
```

**Impact**: morpheum had 76 PRs with zero breaking changes.

**When to use**: Extending existing functionality, maintaining backward compatibility critical.

### 3. Validation Tools for Domain Problems

**Pattern**: Build tools to check consistency automatically

**Example: DikuMUD Zone Validator (PR #119)**
- Problem: 3D room layouts had 35 geometry errors
- Solution: BFS-based graph validator
- Result: Found all errors automatically, enabled incremental fixing

**When to use**: 
- Spatial reasoning required
- Complex state validation
- Multi-file consistency checks
- Domain rules hard to keep in head

**Template**:
```python
def validate_domain_rules(data):
    """Run all validation checks"""
    errors = []
    errors.extend(check_consistency(data))
    errors.extend(check_completeness(data))
    errors.extend(check_references(data))
    return errors

# Use in tests
def test_domain_validation():
    data = load_production_data()
    errors = validate_domain_rules(data)
    assert len(errors) == 0, f"Found {len(errors)} errors: {errors}"
```

### 4. Git Bisect for Regressions

**Pattern**: Automate finding which commit broke something

```bash
# Something broke, but not sure when
git bisect start

# Current version is broken  
git bisect bad

# Version from 2 weeks ago worked
git bisect good HEAD~50

# Git will checkout middle commit, you test
npm test
git bisect good  # if tests pass
# or
git bisect bad   # if tests fail

# Repeat until git identifies exact commit
# Usually takes log2(N) steps
```

**Example**: DikuMUD PR #132 used bisect to find that PR #129 caused quest giver visibility bug.

**Impact**: Fast root cause identification even across many commits.

### 5. Incremental Validation Pattern

**Pattern**: Fix-validate-fix cycles with explicit checking

```markdown
Prompt: Fix errors one by one, validating after each fix

Process:
1. Run validator → 34 errors
2. Fix error #1
3. Run validator → 32 errors (validate #1 actually fixed)
4. Fix error #2  
5. Run validator → 30 errors
...
N. Run validator → 0 errors
```

**Impact**: DikuMUD PR #120 went from 34→32→30→9→0 errors systematically. Tracks progress objectively, prevents regression.

### 6. Checklist-Driven Work

**Pattern**: Include task checklists in PR descriptions

```markdown
PR Description:

Complex feature with multiple steps:

- [x] Explore repository structure
- [x] Run existing tests to understand baseline
- [x] Implement core functionality
- [x] Add unit tests for core
- [ ] Add integration tests
- [ ] Update documentation  
- [ ] Add example usage
```

**Benefits**:
- Shows progress
- Enables resume after interruptions
- Helps AI stay organized
- Makes PR reviews easier

## Velocity Metrics

Track these to measure improvement:

### PR-Level Metrics

**Target ranges** (from successful projects):
- **Commits per PR**: 1-3 for 80% of PRs
- **Time to merge**: Same day for simple features
- **PRs per day**: 3-11 sustained over weeks
- **Test coverage**: Growing, not shrinking

### Phase Metrics

**Foundation phase** (first 10-15 PRs):
- Higher commits per PR (learning)
- Establishing architecture
- Building tooling

**Feature phase** (next 30-50 PRs):
- Lower commits per PR (foundation paying off)
- High velocity
- Rapid iteration

**Polish phase** (final 10-20 PRs):
- Variable commits (some complex edge cases)
- Consolidation PRs (testing, docs)
- Quality improvements

### What Good Looks Like

**dikuclient trajectory**:
- Phase 1 (PR 1-15): Foundation, 6.3 commits/PR avg
- Phase 2 (PR 16-45): Features, 2.8 commits/PR avg
- Phase 3 (PR 46-63): Polish, 2.1 commits/PR avg

Velocity increased as foundation solidified.

## Leveling Up Checklist

You've leveled up when:

- 80% of PRs complete in 1-3 commits
- You write specific, constrained prompts naturally
- Tests drive development, not follow it
- You budget for refinement cycles upfront
- Complex features decompose into clear phases
- Velocity feels sustainable (not frantic)

## Common Advanced Pitfalls

### Optimizing Too Early
Building interfaces for flexibility you don't need yet.

**Fix**: Add abstraction when you have 2-3 concrete examples, not speculatively.

### Skipping Refinement Budget
Assuming features are "done" after initial PR.

**Fix**: Explicitly plan for 2-3 follow-up PRs on complex features.

### Chasing Velocity Metrics
Doing 10 trivial PRs to hit "10 PRs/day" target.

**Fix**: Velocity is outcome of good practices, not the goal itself.

### Test Debt Accumulation
Moving fast by skipping tests.

**Fix**: Speed comes from fast feedback, which requires tests.

## What's Next?

- **[Sharpen the Saw](sharpen-the-saw.html)**: Master consolidation and sustainable pace
- **[Getting Started](getting-started.html)**: Review foundation practices
- **[Staying Organized](staying-organized.html)**: Revisit design-first development

---

<small>**Evidence sources**: [dikuclient](https://github.com/anicolao/dikuclient) 63 PRs (3.5/day, phases), [DikuMUD](https://github.com/anicolao/DikuMUD) 165 PRs (11/day, validation tools, git bisect), [morpheum](https://github.com/anicolao/morpheum) 76 PRs (interface-first, progressive enhancement), velocity metrics from all case studies.</small>
