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

Focus on **describing the problem clearly**. The actual dikuclient Issue #1 demonstrates this:

> "Write a design doc *only*, no code, that specifies the overall structure of such a client for approval before we begin implementing. Justify the language choice and outline the approach for the TUI, and explain how it will work inside the browser interface."

This asks for design before implementation, with justification required for choices.

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

## Real Example from Case Studies

**dikuclient's design-first pattern:**

The project started with Issue #1 asking for a design document before any code. This established the architecture and made subsequent implementation smooth.

See PR #2 (ANSI color support, 2 commits) and other early PRs in the [dikuclient case study](https://github.com/anicolao/llmdev/blob/main/case_studies/GITHUB_ANICOLAO_DIKUCLIENT.md) for examples of features implemented efficiently after design was established.

**DikuMUD PR #162** used design-first approach for complex features, preventing 3-4 refactor cycles. See [DikuMUD case study](https://github.com/anicolao/llmdev/blob/main/case_studies/GITHUB_ANICOLAO_DIKUMUD.md) for details.

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

## Real Patterns from Case Studies

### DikuMUD PR #119: Zone Validation Tool

DikuMUD needed to validate 3D room layouts. The case study documents how a BFS-based graph validator was built to automatically catch geometry errors. See [DikuMUD case study](https://github.com/anicolao/llmdev/blob/main/case_studies/GITHUB_ANICOLAO_DIKUMUD.md) PR #119 for details.

### morpheum PR #10: Provider Integration  

morpheum added Copilot provider integration in 1 commit (1h 18m). The PR successfully reused existing LLMClient interface pattern. See [morpheum case study](https://github.com/anicolao/llmdev/blob/main/case_studies/GITHUB_ANICOLAO_MORPHEUM.md) for analysis of what made this efficient.

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

## Key Insight from Case Studies

Projects with design-first approach averaged 3 commits/PR. Projects without averaged 6-8 commits/PR (double the iteration).

**Evidence**: See velocity metrics in the [case studies](https://github.com/anicolao/llmdev/tree/main/case_studies) for detailed analysis.

## What's Next?

Now that you're organized:

- **[Leveling Up](leveling-up.html)**: Learn rapid iteration patterns
- **[Sharpen the Saw](sharpen-the-saw.html)**: Master consolidation and refinement
- **[Getting Started](getting-started.html)**: Review foundation practices

---

<small>**Evidence sources**: [DikuMUD](https://github.com/anicolao/DikuMUD) PR #162 (design-first), PR #119 (validation tool), [morpheum](https://github.com/anicolao/morpheum) PR #10 (interface design), [dikuclient](https://github.com/anicolao/dikuclient) Issue #1→PR #2 (architecture design), PR #15 (checkpoint consolidation).</small>
