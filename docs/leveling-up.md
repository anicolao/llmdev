---
layout: default
title: How To Level Up
---

# How To Level Up

Once you've mastered the basics, advanced prompting patterns unlock extraordinary productivity. These techniques come from analyzing projects that sustained 3-11 PRs/day for weeks.

**Proven by evidence:** Projects using these advanced patterns achieved 80% of PRs in 1-3 commits, compared to 6+ commits without them.

## Advanced Prompting for Rapid Iteration

The key is crafting prompts that give AI exactly the right constraints and context.

### Target the 1-3 Commit Sweet Spot

**Goal**: Have AI complete 80% of features in 1-3 commits

**How to achieve this:**
- Clear requirements in your prompts
- Appropriate scope (one feature at a time)
- Fast feedback loop

**Evidence from case studies:**
- dikuclient: 3.5 PRs/day, average 2.8 commits/PR in feature phase
- DikuMUD: 11 PRs/day, average 2.1 commits/PR in polish phase
- morpheum: 10 PRs in 17 hours, most 1 commit each

### When to Expect More Iterations

Some features naturally take 6-15 commits with AI. This is normal for:

- **Learning new domains**: First time AI tackles a pattern
- **Foundation work**: Core abstractions everything builds on
- **Complex algorithms**: Spatial validation, graph traversal
- **Integration points**: Connecting multiple systems

**Example**: dikuclient PR #3 took 15 commits building networking foundation. Every subsequent networking feature took 1-3 commits because AI had the foundation to work from.

**Pattern**: High iteration on foundations → Low iteration on features

## Proven Patterns from Case Studies

### dikuclient: Foundation → Features

PR #3 took 15 commits building networking foundation. Every subsequent networking feature took 1-3 commits because AI had the foundation to work from.

**Pattern**: High iteration on foundations → Low iteration on features

### morpheum PR #10: Interface-Based Design

morpheum added Copilot provider integration in 1 commit (1h 18m) because it built on the LLMClient interface established in PR #2.

**Key insight**: When interfaces are well-designed, adding implementations is fast.

See [morpheum case study](https://github.com/anicolao/llmdev/blob/main/case_studies/GITHUB_ANICOLAO_MORPHEUM.md) and [dikuclient case study](https://github.com/anicolao/llmdev/blob/main/case_studies/GITHUB_ANICOLAO_DIKUCLIENT.md) for detailed analysis.

### What the Case Studies Show

Successful prompts are:
1. **Specific** about what needs to be done
2. **Constrained** (minimal changes, specific scope)
3. **Contextual** (reference existing code/interfaces)

Review the prompt analysis sections in the [case studies](https://github.com/anicolao/llmdev/tree/main/case_studies) to see real examples of effective prompts.

## Test Growth from Case Studies

**Healthy pattern**: Tests grow alongside features

- morpheum: 50 → 353 tests over 76 PRs
- dikuclient: PR #15 consolidated with test additions
- DikuMUD: 100+ integration tests validate all changes

See the [case studies](https://github.com/anicolao/llmdev/tree/main/case_studies) for detailed test growth patterns and coverage metrics.

## Plan for Refinement Cycles

Major features need follow-up PRs. Budget for them upfront.

### Real Example: dikuclient networking

- PR #3: Foundation (15 commits - complex)
- Subsequent networking features: 1-3 commits each

**Pattern**: Initial foundation work is complex, but subsequent features building on that foundation are fast.

See [dikuclient case study](https://github.com/anicolao/llmdev/blob/main/case_studies/GITHUB_ANICOLAO_DIKUCLIENT.md) for analysis of iteration patterns.

## Advanced Patterns from Case Studies

### Interface-First Architecture (morpheum)

morpheum added 4 providers in 1-2 hours each because the LLMClient interface was designed first. See [morpheum case study](https://github.com/anicolao/llmdev/blob/main/case_studies/GITHUB_ANICOLAO_MORPHEUM.md) for details.

**Result**: 76 PRs with zero breaking changes.

### Validation Tools (DikuMUD)

DikuMUD PR #119 built a BFS-based graph validator that automatically found 35 geometry errors in 3D room layouts. See [DikuMUD case study](https://github.com/anicolao/llmdev/blob/main/case_studies/GITHUB_ANICOLAO_DIKUMUD.md) for analysis.

### Git Bisect for Debugging (DikuMUD)

DikuMUD PR #132 used git bisect to identify that PR #129 caused a quest giver visibility bug. See case study for details.

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

## Key Insights

Velocity is the outcome of good practices, not a goal itself. The case studies show:

- 80% of PRs in 1-3 commits when foundation is solid
- Test coverage growing with features, not shrinking
- Complex features decomposed into clear phases

See the [case studies](https://github.com/anicolao/llmdev/tree/main/case_studies) for detailed velocity analysis.

## What's Next?

- **[Sharpen the Saw](sharpen-the-saw.html)**: Master consolidation and sustainable pace
- **[Getting Started](getting-started.html)**: Review foundation practices
- **[Staying Organized](staying-organized.html)**: Revisit design-first development

---

<small>**Evidence sources**: [dikuclient](https://github.com/anicolao/dikuclient) 63 PRs (3.5/day, phases), [DikuMUD](https://github.com/anicolao/DikuMUD) 165 PRs (11/day, validation tools, git bisect), [morpheum](https://github.com/anicolao/morpheum) 76 PRs (interface-first, progressive enhancement), velocity metrics from all case studies.</small>
