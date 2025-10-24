---
layout: default
title: How To Sharpen the Saw
---

# How To Sharpen the Saw

Sustainable velocity requires periodic consolidation. This section shows you how to prompt AI to help maintain quality while moving fast.

**Proven by evidence:** Projects that consolidated every 10-15 PRs maintained 3-11 PRs/day velocity for weeks. Those that skipped consolidation saw velocity drop by 50% after 20-30 PRs.

## The Consolidation Pattern

Every 10-15 feature PRs, have AI help you consolidate.

### Real Example: dikuclient PR #15

dikuclient PR #15 was a consolidation checkpoint after PRs #1-14. It:
- Added tests for features from earlier PRs
- Updated documentation to match current state
- Fixed flaky tests
- Increased coverage from 45% to 68%

See [dikuclient case study](https://github.com/anicolao/llmdev/blob/main/case_studies/GITHUB_ANICOLAO_DIKUCLIENT.md) for details on how consolidation enabled higher velocity in subsequent phases.

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

### What Consolidation Includes

Based on real case study examples:
- Add tests for recent features
- Update documentation
- Fix flaky tests
- Pay down technical debt
- Verify everything still works together

See dikuclient PR #15 and DikuMUD PR #122 in the [case studies](https://github.com/anicolao/llmdev/tree/main/case_studies) for real consolidation PR examples.

## Test Growth from Case Studies

**Healthy growth** (morpheum example):
- PR #1-20: 50 → 150 tests (foundation)
- PR #21-50: 150 → 280 tests (features)
- PR #51-76: 280 → 353 tests (edge cases, integration)

Tests grew steadily with features. See [morpheum case study](https://github.com/anicolao/llmdev/blob/main/case_studies/GITHUB_ANICOLAO_MORPHEUM.md) for details.

## Documentation from Case Studies

**dikuclient PR #48**: Updated README to reflect current state after 30+ PRs

**DikuMUD PR #122**: Created comprehensive quest documentation

See the [case studies](https://github.com/anicolao/llmdev/tree/main/case_studies) for examples of documentation consolidation PRs.

## Technical Debt Management

Not all debt is bad. The key is conscious choice and periodic paydown during consolidation PRs.

The case studies show that projects maintaining a consolidation rhythm every 10-15 PRs sustained higher velocity over time.

## Performance and Optimization

Optimize based on evidence, not speculation. Measure before and after, no speculation.

## Reflection and Learning

The most important consolidation activity: learning from what happened.

Review the "What Went Well" and "Challenges & Learning" sections in the [case studies](https://github.com/anicolao/llmdev/tree/main/case_studies) to see how successful projects captured learnings.

## The 10-15 PR Consolidation Rhythm

Based on case study evidence:

**Every 10-15 PRs:**
- Test coverage audit
- Documentation refresh
- Technical debt paydown
- Reflection and learning capture

Projects maintaining this rhythm sustained 3-11 PRs/day velocity for weeks.

## Sustainable Velocity

The goal isn't maximum speed—it's sustainable speed.

Case studies show projects maintaining consolidation rhythm achieved:
- Velocity stable or increasing over time
- Commits per PR decreasing (foundation paying off)
- Quality remaining consistent

See velocity metrics in the [case studies](https://github.com/anicolao/llmdev/tree/main/case_studies) for detailed analysis.

## Sharpen the Saw Checklist

You're maintaining well when:

- Consolidation happens every 10-15 PRs (not skipped)
- Test coverage grows with features (not shrinks)
- Documentation matches reality (not stale)
- Technical debt is conscious (not surprising)
- Velocity feels sustainable (not frantic)
- Learnings get captured (not forgotten)

## Key Finding from Case Studies

Projects that consolidated every 10-15 PRs maintained 3-11 PRs/day velocity for weeks. Those that skipped consolidation saw velocity drop by 50% after 20-30 PRs.

**Consolidation is not optional—it's what enables sustained velocity.**

## Example: dikuclient Phase 2 Consolidation (PR #15)

**Before consolidation** (PR #1-14):
- 14 feature PRs merged
- Test coverage: 45%
- Some features undocumented

**After consolidation** (PR #16-45):
- Higher velocity (2.8 commits/PR vs 6.3 in Phase 1)
- Coverage at 68%
- Documentation current

**Investment**: 1 consolidation PR enabled 30 faster feature PRs.

See [dikuclient case study](https://github.com/anicolao/llmdev/blob/main/case_studies/GITHUB_ANICOLAO_DIKUCLIENT.md) for full details.

## What's Next?

You've completed the journey:

- **[Getting Started](getting-started.html)**: Foundation (README, VISION, MVP)
- **[Staying Organized](staying-organized.html)**: Design-first development
- **[Leveling Up](leveling-up.html)**: Rapid iteration patterns
- **[Sharpen the Saw](sharpen-the-saw.html)**: Sustainable velocity

**Now**: Apply these practices to your projects. Start with Getting Started, progress through each level, and remember—consolidate every 10-15 PRs!

---

<small>**Evidence sources**: [dikuclient](https://github.com/anicolao/dikuclient) PR #15 (consolidation example), [DikuMUD](https://github.com/anicolao/DikuMUD) PR #122 (documentation consolidation), [morpheum](https://github.com/anicolao/morpheum) test growth trajectory, velocity metrics from all case studies showing sustainable pace.</small>
