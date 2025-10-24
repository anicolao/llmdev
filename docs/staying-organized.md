---
layout: default
title: How To Stay Organized
---

# How To Stay Organized

As projects grow beyond the initial MVP, organization becomes critical. The key is **design before code**—especially choosing between credible alternative implementation plans before committing to an approach.

## The Design Analysis Step

When facing a complex feature, pause to evaluate at least two different implementation approaches before coding.

### Why Alternative Analysis Matters

**Without alternatives:**
- You commit to the first idea that sounds reasonable
- Miss better approaches that become obvious later
- Waste time on rework when initial approach hits limits

**With alternatives:**
- Surface trade-offs explicitly
- Choose the right complexity level
- Avoid premature optimization
- Build confidence through comparison

**Evidence**: DikuMUD PR #162 explicitly stated "Focus on writing only the design doc... don't implement anything yet." This design-first approach prevented 3-4 refactor cycles that would have occurred with code-first.

## The Two-Alternative Minimum

Always generate at least two credible alternatives before implementing.

### What Makes an Alternative "Credible"?

Each option should:
- Actually solve the stated problem
- Have clear pros and cons
- Be implementable with available tools/skills
- Differ meaningfully from other options (not just minor variations)

### Example: dikuclient Color Support

**Context**: Need to handle ANSI color codes from server

**Alternative 1: Client-side parsing**
- Parse ANSI codes in client JavaScript
- Convert to HTML/CSS styling
- **Pro**: Full control, can add enhancements
- **Con**: Complex parser, potential bugs, maintenance burden

**Alternative 2: Terminal emulation library**
- Use existing `blessed` or `xterm.js` library
- **Pro**: Battle-tested, handles edge cases
- **Con**: Larger dependency, some features unused

**Alternative 3: Minimal regex replacement**
- Simple regex to convert basic colors only
- **Pro**: Tiny, easy to understand, sufficient for MVP
- **Con**: Doesn't handle all ANSI codes

**Decision**: Started with Alternative 3 in PR #2 (2 commits). Later enhanced incrementally. Right complexity for the phase.

## Design Document Template

Use this template for features requiring analysis:

```markdown
# Design: [Feature Name]

## Problem Statement
[What are we solving? Why does it matter?]

## Success Criteria
[How will we know this works?]
- [ ] Measurable criterion 1
- [ ] Measurable criterion 2

## Alternative 1: [Name]
**Approach**: [High-level description]

**Pros**:
- [Advantage 1]
- [Advantage 2]

**Cons**:
- [Limitation 1]
- [Limitation 2]

**Estimated Complexity**: [Small/Medium/Large]

## Alternative 2: [Name]
[Same structure as Alternative 1]

## Alternative 3: [Name] (if needed)
[Same structure]

## Recommendation
**Choose**: Alternative [N]

**Rationale**: [Why this one? What trade-offs are we accepting?]

**Implementation Plan**:
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Out of Scope** (for now):
- [What we're explicitly not doing]
- [Why we're deferring it]
```

## When to Use Design Analysis

Not every feature needs deep analysis. Use this decision tree:

### ⚡ Skip Design Doc (Quick Implementation)
- Adding simple CRUD endpoint
- Fixing obvious bug
- Minor UI tweak
- Updating documentation
- Adding test for existing code

**Action**: Write prompt and implement directly (1-2 commits expected)

### Light Design (Issue Description)
- New feature with one clear approach
- Moderate complexity
- Affects 2-3 files

**Action**: Write problem statement in issue, outline approach, implement (3-5 commits expected)

### 📐 Full Design Doc (Separate PR)
- Multiple viable approaches exist
- Affects architecture or key abstractions
- Impacts multiple components
- High cost if we choose wrong approach

**Action**: Design doc in separate PR/issue, get review, then implement (6+ commits expected)

## Design-First in Practice

### Example 1: morpheum Interface Design (PR #10)

**Situation**: Needed to integrate Copilot alongside existing OpenAI provider

**Process**:
1. Created design doc comparing 3 approaches
2. Chose interface-first architecture
3. Implemented in PR #10 (1 commit, 1h 18m)

**Result**: Later added Anthropic, DeepSeek, Ollama providers—each took 1-2 hours because interface was designed well.

**ROI**: 30 min design → 5x faster provider additions → saved 6-8 hours total

### Example 2: DikuMUD Zone Validation (PR #119)

**Situation**: 3D room layouts had consistency errors (35 found by human inspection)

**Process**:
1. Evaluated 3 alternatives:
   - Manual validation (not scalable)
   - Simple rule checker (misses spatial issues)
   - BFS-based graph validator (comprehensive)
2. Chose Alternative 3
3. Built validator tool in separate PR

**Result**: Found all 35 errors automatically, enabled incremental fixing with validation between each fix.

**Impact**: Prevented future geometry bugs entirely (validator runs in CI)

### Example 3: dikuclient Networking Layer (Issue #1 → PR #2)

**Situation**: Need client-server architecture

**Process**:
1. Issue #1 created comprehensive design doc
2. Evaluated WebSocket vs raw TCP, decided WebSocket
3. Laid out architecture: client ↔ proxy ↔ MUD server
4. PR #2 implemented the design

**Result**: All 63 subsequent PRs built on this architecture—no architectural rework needed.

## Prompts for Design Analysis

### Generate Alternatives Prompt

```markdown
I need to implement [feature] that [specific requirement].

Before implementing, please analyze at least 2 different 
approaches to solve this:

For each alternative:
1. Describe the approach
2. List pros and cons
3. Estimate complexity (small/medium/large)
4. Identify risks or unknowns

After analysis, recommend which approach and explain why.

Consider:
- Maintainability
- Performance  
- Complexity
- Time to implement
```

### Design Doc Review Prompt

```markdown
I've written a design doc for [feature] (see [file/issue]).

Please review and:
1. Identify any missed alternatives worth considering
2. Point out unstated assumptions
3. Highlight potential risks in recommended approach
4. Suggest improvements to the implementation plan

Don't implement anything yet—focus on design quality.
```

### Implementation from Design Prompt

```markdown
Following the design in [file/issue], please implement 
Alternative [N]: [name].

Implementation plan from design:
1. [Step 1]
2. [Step 2]
3. [Step 3]

Remember to:
- Follow the design exactly
- Add tests as specified in success criteria
- Mark anything deferred to future work with TODO
```

## Organization Patterns

### 1. Branch Naming for Transparency

Use consistent prefixes that show what AI contributed:

```bash
# AI-assisted branches
copilot/add-color-support
copilot/fix-connection-bug
copilot/refactor-parser

# Human design branches  
design/api-architecture
design/data-model
```

**Evidence**: dikuclient used `copilot/*` for all 63 PRs. Made it trivial to track AI contributions and learn from patterns.

### 2. Issue as Design Document

For medium complexity, use the issue description as the design doc:

```markdown
## Problem
[Specific issue]

## Analysis
I evaluated two approaches:
1. [Approach 1]: [pros/cons]
2. [Approach 2]: [pros/cons]

Recommending Approach 2 because [rationale].

## Implementation Plan
- [ ] Step 1
- [ ] Step 2  
- [ ] Step 3

## Success Criteria
- [ ] Passes test X
- [ ] Performance meets Y
```

### 3. Checkpoint PRs

Every 10-15 feature PRs, create a checkpoint PR:

```markdown
PR Title: "Checkpoint: Consolidate Phase [N] work"

Contents:
- Add tests for recent features
- Update documentation
- Fix flaky tests
- Validate everything still works
- Update VISION if direction shifted
```

**Evidence**: dikuclient PR #15 consolidated early work. DikuMUD PR #122 created comprehensive quest documentation. morpheum had multiple stabilization phases.

## Staying Organized Checklist

Use this checklist before starting complex work:

- [ ] **Problem is clear**: Can state it in 2 sentences
- [ ] **Success criteria defined**: Know what "done" looks like
- [ ] **Alternatives evaluated**: Considered at least 2 approaches
- [ ] **Trade-offs understood**: Know what we're giving up
- [ ] **Scope bounded**: Clear on what's in/out
- [ ] **Tests planned**: Know how to validate it works
- [ ] **Rollback plan**: Know how to undo if needed

## Success Metrics

You're organized if:

- Complex features take 1 design PR + 1-2 implementation PRs
- 80% of PRs have clear requirements (not discovered during implementation)
- Architectural changes happen through design first (not refactoring later)
- You can explain why you chose this approach over alternatives

**Evidence**: Projects with design-first approach averaged 3 commits/PR. Projects without averaged 6-8 commits/PR (double the iteration).

## Common Pitfalls

### Analysis Paralysis
Spending days on design docs for simple features.

**Fix**: Use decision tree above. Most features are "quick implementation."

### False Alternatives
"Alternative 1: Do it. Alternative 2: Don't do it."

**Fix**: Alternatives should be different implementation approaches, not whether to implement.

### Choosing Favorites
Already decided, then manufacturing alternatives to justify it.

**Fix**: Generate alternatives before deciding. You might be surprised which is actually best.

### Ignoring Design
"Let's just start coding and see what happens."

**Fix**: Code-first works for MVP, but design-first prevents rework for complex features.

## What's Next?

Now that you're organized:

- **[Leveling Up](leveling-up.html)**: Learn rapid iteration patterns
- **[Sharpen the Saw](sharpen-the-saw.html)**: Master consolidation and refinement
- **[Getting Started](getting-started.html)**: Review foundation practices

---

<small>**Evidence sources**: [DikuMUD](https://github.com/anicolao/DikuMUD) PR #162 (design-first), PR #119 (validation tool), [morpheum](https://github.com/anicolao/morpheum) PR #10 (interface design), [dikuclient](https://github.com/anicolao/dikuclient) Issue #1→PR #2 (architecture design), PR #15 (checkpoint consolidation).</small>
