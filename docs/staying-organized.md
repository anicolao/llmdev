---
layout: default
title: How To Stay Organized
---

# How To Stay Organized

As projects grow beyond the initial MVP, organization becomes critical. The key is **design before code**—have AI evaluate alternatives before implementing.

**Proven by evidence:** DikuMUD's design-first approach (PR #162) prevented 3-4 refactor cycles, reducing work from 6+ commits to 1-3 commits per feature.

## Have AI Analyze Design Alternatives

When facing a complex feature, prompt AI to evaluate at least two different implementation approaches before coding.

### How to Prompt for Design Analysis

Focus on **describing the problem clearly**, not telling AI how to structure analysis (it knows how).

**What to include in your prompt:**
- **The problem**: What needs to be solved
- **Constraints**: What limits your options
- **Context**: Why this matters
- **Request**: "analyze alternatives and recommend"

**Example from dikuclient:**
```markdown
"We need to handle ANSI color codes from the MUD server.

Context: Terminal output with escape sequences
Constraint: Keep it simple for MVP, we can enhance later
Request: Analyze 2-3 approaches and recommend one"
```

**What AI does automatically** (you don't need to specify):
- Generates alternative approaches
- Lists pros/cons for each
- Estimates complexity
- Recommends best option
- Explains rationale

### Why This Pattern Works

**Without alternatives:**
- AI commits to first idea that sounds reasonable
- You miss better approaches that become obvious later
- More rework when initial approach hits limits

**With alternatives:**
- AI surfaces trade-offs explicitly
- You choose the right complexity level
- Avoid premature optimization
- Build confidence through comparison

## Example: AI-Generated Design Alternatives

**Context from dikuclient:** Need to handle ANSI color codes from server

**Prompt to AI:**
```markdown
We need to handle ANSI color codes from the MUD server.
Analyze 2-3 different approaches and recommend one.
```

**AI's Analysis:**

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

**Decision from case study**: Started with Alternative 3 in PR #2 (2 commits). Right complexity for MVP phase. Later enhanced incrementally as needed.

## When to Use Design Analysis

Not every feature needs deep analysis. Use AI to help decide:

### Quick Decision Prompt

```markdown
For implementing [feature], should I:
A) Implement directly (straightforward, one clear approach)
B) Do design analysis first (multiple viable approaches, affects architecture)

What's your recommendation and why?
```

### AI-Assisted Decision Tree

**⚡ Implement Directly** (prompt AI to code immediately):
- Simple CRUD endpoint
- Obvious bug fix
- Minor UI tweak
- Documentation update
- Test for existing code

**Prompt**: `"Implement [feature]. Make changes as small as possible."`

### 📝 Light Design** (have AI outline approach in issue):
- New feature with one clear approach
- Moderate complexity
- Affects 2-3 files

**Prompt**: `"Describe how to implement [feature], then implement it."`

### 📐 Full Design Analysis** (separate design-then-implement):
- Multiple viable approaches exist
- Affects architecture or key abstractions
- High cost if wrong approach chosen

**Prompt**: Use the design analysis template above, then implement separately.

## Design Document Template

When AI recommends full design analysis, use this template:

```markdown
# Design: [Feature Name]

## Problem Statement
[What are we solving? Why does it matter?]

## Success Criteria
- [ ] Measurable criterion 1
- [ ] Measurable criterion 2

## Alternative 1: [Name]
**Approach**: [High-level description]
**Pros**: [Advantages]
**Cons**: [Limitations]
**Complexity**: [Small/Medium/Large]

## Alternative 2: [Name]
[Same structure]

## Recommendation
**Choose**: Alternative [N]
**Rationale**: [Why? What trade-offs?]

## Implementation Plan
1. [Step 1]
2. [Step 2]
3. [Step 3]
```

Give this template to AI and have it fill it out before coding.

## Real-World Prompt Patterns

### Pattern 1: Problem Description

From DikuMUD PR #119 (zone validation):
```markdown
"3D room layouts have consistency errors - 35 found manually.

Problem: Manual validation doesn't scale
Context: Spatial relationships in MUD zones
Need: Automated validation that catches all errors

Analyze approaches and recommend one"
```

**Why it worked:** Clear problem, specific context, focused request. AI proposed BFS-based graph validator.

### Pattern 2: Integration Challenge

From morpheum PR #10 (Copilot integration):
```markdown
"Need to integrate Copilot provider alongside OpenAI.

Context: We have LLMClient interface from PR #2
Requirement: Same interface, add streaming support
Constraint: Minimal changes to existing code

Analyze how to add this cleanly"
```

**Why it worked:** Referenced existing code, stated constraints. Result: 1 commit, 1h 18m.

### Pattern 3: Implementation from Design

Once design is chosen:
```markdown
"Implement the BFS-based validator from the design analysis.

Focus on: Finding all connectivity errors
Test: Should catch the 35 known errors

Keep it simple for now - enhancements later"
```

**Key**: Focus on WHAT (problem, context, constraints) not HOW (AI handles analysis structure).

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
