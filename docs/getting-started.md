---
layout: default
title: How To Get Started
---

# How To Get Started

When starting a new project with AI assistance, three elements set you up for success: a clear README, a compelling VISION, and a tiny MVP. This foundation enables rapid iteration while maintaining direction.

## 1. Start with a Clear README

Your README is the contract between you and the AI. Make it specific and actionable.

### What to Include

**Required sections:**
- **Overview**: What this project does (2-3 sentences)
- **Purpose**: Why it exists and what problem it solves
- **Installation**: Exact commands to get started
- **Usage**: Concrete examples of how to use it
- **Testing**: How to validate it works

**Example from dikuclient:**
```markdown
# Diku Client
A MUD client for Diku with modern features

## Purpose
Connect to and play DikuMUD with enhanced features:
- Color support
- Command history
- Triggers and aliases

## Installation
git clone https://github.com/anicolao/dikuclient.git
cd dikuclient
npm install

## Usage
npm start -- --host diku.mud.example.com --port 4000
```

### Why This Matters

A clear README gives the AI:
- **Context** about what you're building
- **Constraints** on how it should work
- **Success criteria** to validate against

**Evidence**: All 4 analyzed projects started with clear READMEs. Projects with vague READMEs needed more iteration (6+ commits vs 1-3 commits for clear specs).

## 2. Create a Compelling VISION

Your VISION document captures the "why" and long-term direction. This prevents the AI from optimizing for the wrong goals.

### Vision Template

```markdown
# Vision for [Project Name]

## The Challenge
[What problem exists today?]

## Our Mission
[What are you building and why?]

## Core Principles
1. [First principle - what guides decisions]
2. [Second principle]
3. [Third principle]

## Success Criteria
We'll know we're succeeding when:
- [Measurable outcome 1]
- [Measurable outcome 2]
- [Measurable outcome 3]

## Open Questions
- [What are you still figuring out?]
- [What trade-offs need consideration?]
```

### Real Example

From the llmdev project VISION.md:

```markdown
## Our Mission
Systematically study how LLMs are being used to build 
real software systems, distilling actionable insights 
for the entire development community.

## Core Principles
- Evidence-Based Analysis
- Balanced Perspective  
- Knowledge Sharing
- Continuous Learning

## Success Criteria
1. Developers make better decisions
2. Tools improve based on our analysis
3. Quality increases measurably
```

### Why This Matters

- **Keeps work aligned**: AI can check if proposals fit the vision
- **Prevents scope creep**: Clear boundaries on what's in/out of scope
- **Enables better prompts**: You can reference vision in requests

**Evidence**: DikuMUD's VISION.md was referenced in 23 of 165 PRs to validate design decisions stayed on track.

## 3. Build a Tiny MVP

Don't aim for perfection—build the smallest thing that works and can serve as the kernel for growth.

### MVP Checklist

Your MVP should:
- [ ] **Build successfully** (even if it does almost nothing)
- [ ] **Have one test** that validates core functionality
- [ ] **Be runnable** (can execute and see output)
- [ ] **Document its limitations** (what it intentionally doesn't do yet)

### Example MVP Progression

**dikuclient Phase 1 (PR #1-3):**
1. PR #1: Connect to server and echo input/output (23 commits - learning)
2. PR #2: Add basic ANSI color support (2 commits - focused)
3. PR #3: Implement command history (15 commits - foundation feature)

Result: Working client in 3 PRs. Everything after built on this kernel.

**morpheum Phase 1 (PR #1-3):**
1. PR #1: Project structure with TypeScript, tests (1 commit - 1h 16m)
2. PR #2: Basic OpenAI integration (1 commit - 1h 16m)  
3. PR #3: Test infrastructure (1 commit - 1h 18m)

Result: Working prototype in 3 hours. 73 more PRs refined and extended it.

### Why Tiny Matters

**Cognitive load**: AI works better with small, focused changes
**Fast feedback**: See results immediately, adjust quickly
**Confidence building**: Early success maintains momentum
**Foundation**: Everything else builds on this kernel

**Anti-pattern to avoid**: 
✗ Trying to build the complete system in PR #1
✗ "This needs X, Y, and Z before it can work"
✗ Multi-week initial development before first commit

**Proven pattern**:
✓ Build smallest possible working thing
✓ Get it running and tested
✓ Iterate from there

## Quick Start Formula

Combine all three elements:

```bash
# Day 1: Foundation
1. Write README.md (30 minutes)
   - What, why, how to install, how to use
   
2. Write VISION.md (30 minutes)
   - Mission, principles, success criteria
   
3. Create minimal project structure (1-2 hours)
   - Initialize project (npm init, poetry init, etc.)
   - Add basic build/test setup
   - Create single source file that runs
   - Write one test that passes
   
4. Verify it works (30 minutes)
   - Build succeeds
   - Tests pass
   - Can run and see output
   
# Day 2+: Iterate
5. Add one feature at a time
6. Test after each feature
7. Reference README/VISION in prompts
```

## Example Prompts

### Initial Setup Prompt
```markdown
I want to create a [project type] that [does what].

I've written a README.md with the overview and a VISION.md 
with our mission. Please help me create a tiny MVP that:

1. Sets up the project structure ([language/framework])
2. Implements just [one core feature]
3. Has one test that validates it works
4. Can build and run successfully

Make this as small as possible - we'll add features incrementally.
```

### Feature Addition Prompt
```markdown
Looking at our README.md and VISION.md, I want to add [feature].

This should:
- [Specific requirement 1]
- [Specific requirement 2]
- Stay aligned with our vision of [reference vision]

Please make minimal changes to implement this.
```

## Success Metrics

You're on track if:

- README takes 30 minutes to write (not days)
- VISION fits on one page (not a book)
- MVP works within 2-4 hours (not weeks)
- First 3 PRs complete in one day (not spread over weeks)
- You can show someone working software on day 1

**Evidence**: All analyzed projects that followed this pattern achieved 3-11 PRs/day sustained velocity.

## Common Pitfalls

### Starting Without Documentation
"I'll document it later" leads to:
- AI making wrong assumptions
- Inconsistent direction
- More iteration (3-5x more commits)

### Perfectionism in MVP
"It needs [long list] before it's ready" results in:
- Analysis paralysis
- Never shipping
- Lost momentum

### Vague Vision
"Build a good project" doesn't guide decisions.
AI will optimize for wrong goals.

## What's Next?

Once you have README + VISION + tiny MVP:

1. **[Staying Organized](staying-organized.html)**: Learn design-first development for complex features
2. **[Leveling Up](leveling-up.html)**: Discover patterns for rapid iteration
3. **[Sharpen the Saw](sharpen-the-saw.html)**: Master consolidation and refinement

---

<small>**Evidence sources**: [dikuclient](https://github.com/anicolao/dikuclient) Issue #1→PR #3 (foundation), [morpheum](https://github.com/anicolao/morpheum) PR #1-3 (3-hour MVP), [DikuMUD](https://github.com/anicolao/DikuMUD) PR #162 (design-first pattern), [llmdev](https://github.com/anicolao/llmdev) VISION.md creation and use.</small>
