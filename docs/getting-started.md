---
layout: default
title: How To Get Started
---

# How To Get Started

When starting a new project with AI assistance, three elements set you up for success: a clear README, a compelling VISION, and a tiny MVP. This foundation enables rapid iteration while maintaining direction.

**Proven by evidence:** All 4 analyzed case studies (334+ PRs) used this pattern to achieve 3-11 PRs/day sustained velocity.

## 1. Have AI Create a Clear README

Your README is the contract between you and the AI. Use AI to create it, following this proven structure.

### Prompt AI to Create Your README

**Prompt template:**
```markdown
Create a README.md for a [project type] that [brief description].

Include these sections:
- Overview: What this project does (2-3 sentences)
- Purpose: Why it exists and what problem it solves
- Installation: Exact commands to get started
- Usage: Concrete examples with actual commands
- Testing: How to validate it works

Keep it concise and specific. Use [dikuclient example below] as a style guide.
```

**Example README structure (from dikuclient case study):**
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

## 2. Have AI Create a Compelling VISION

Your VISION document captures the "why" and guides long-term direction. Use AI to create it following this proven template.

### Prompt AI to Create Your VISION

**Prompt template:**
```markdown
Create a VISION.md for [project name] that [mission statement].

Use this structure:
- The Challenge: What problem exists today
- Our Mission: What we're building and why
- Core Principles: 3-4 guiding principles for decisions
- Success Criteria: 3-5 measurable outcomes
- Open Questions: What we're still figuring out

Style it like the llmdev VISION.md example below.
```

**Example VISION structure (from llmdev case study):**

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

## 3. Have AI Build a Tiny MVP

Don't aim for perfection—prompt AI to build the smallest thing that works and can serve as the kernel for growth.

### Prompt AI to Create Your MVP

**Prompt template:**
```markdown
I've created README.md and VISION.md (see attached files).

Please create a tiny MVP that:
- Sets up [language/framework] project structure  
- Implements ONLY [one core feature from README]
- Has one test that validates it works
- Can build and run successfully

Make this as minimal as possible—we'll add features incrementally.
Target: Working in 2-4 hours, not days.
```

### MVP Checklist

AI should create an MVP that:
- [ ] **Builds successfully** (even if it does almost nothing)
- [ ] **Has one test** that validates core functionality
- [ ] **Is runnable** (can execute and see output)
- [ ] **Documents its limitations** (what it intentionally doesn't do yet)

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

**Evidence from case studies:**
- **dikuclient**: 3-hour MVP became foundation for 63 PRs
- **morpheum**: 3-hour MVP (3 PRs) enabled 73 more PRs
- **Pattern**: Tiny kernel → rapid iteration

**Why this pattern works:**
- **AI cognitive load**: Works better with small, focused tasks
- **Fast feedback**: See results immediately, adjust quickly
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

Use AI to create all three elements following these proven patterns:

```bash
# Step 1: Have AI Create Foundation (1 hour)
"Create a README.md for [project] that [description]"
# Review and refine

"Create a VISION.md for [project] with mission: [statement]"  
# Review and refine

# Step 2: Have AI Build MVP (2-4 hours)
"Using the README and VISION, create a tiny MVP that [one feature]"
# Verify it works

# Step 3: Verify Success (30 minutes)
- Build succeeds
- Tests pass
- Can run and see output

# Step 4: Start Iterating (Day 2+)
"Looking at README.md and VISION.md, add [next feature]"
# One feature at a time
# Reference README/VISION in each prompt
```

## Effective Prompts for AI

### Initial Setup Prompt

Use this pattern (from successful case studies):

```markdown
I want to create a [project type] that [specific purpose].

Please create:
1. README.md with overview, purpose, installation, usage
2. VISION.md with mission, principles, success criteria
3. A tiny MVP in [language/framework] that:
   - Implements just [ONE core feature]
   - Has one test
   - Builds and runs

Make everything as minimal as possible - we'll iterate.
Style: professional, concise, actionable.
```

### Feature Addition Prompt

Once you have the foundation:

```markdown
Looking at our README.md and VISION.md, I want to add [feature].

Requirements:
- [Specific requirement 1 with example]
- [Specific requirement 2 with example]

Constraints:
- Make changes as small as possible
- Maintain backward compatibility
- Stay aligned with our vision

Success criteria:
- [ ] [Testable outcome]
- [ ] All existing tests pass
```

## Success Metrics (from Case Studies)

You're on track if:

- AI creates README in one prompt (with minor refinement)
- AI creates VISION in one prompt (with minor refinement)
- AI creates working MVP in 2-4 hours (1-3 prompts)
- First 3 PRs complete in one day
- You can demo working software on day 1

**Evidence**: All analyzed projects that used this pattern achieved 3-11 PRs/day sustained velocity with 1-3 commits per PR.

## Common Pitfalls (from Case Studies)

### Starting Without Documentation
**Anti-pattern**: "I'll just start coding and document later"

**Result**: AI makes wrong assumptions, inconsistent direction, 3-5x more iteration

**Fix**: Use AI to create README + VISION first (1 hour total), then build

### Asking AI for Too Much at Once
**Anti-pattern**: "Build a complete system with X, Y, and Z"

**Result**: Analysis paralysis, overwhelming scope, weeks before first working code

**Fix**: Follow morpheum's 3-hour MVP pattern—one core feature, then iterate

### Vague Prompts to AI
**Anti-pattern**: "Build a good project" or "Make it better"

**Result**: AI optimizes for wrong goals, requires many iterations

**Fix**: Use specific prompts with examples, constraints, and success criteria

## What's Next?

Once you have README + VISION + tiny MVP:

1. **[Staying Organized](staying-organized.html)**: Learn design-first development for complex features
2. **[Leveling Up](leveling-up.html)**: Discover patterns for rapid iteration
3. **[Sharpen the Saw](sharpen-the-saw.html)**: Master consolidation and refinement

---

<small>**Evidence sources**: [dikuclient](https://github.com/anicolao/dikuclient) Issue #1→PR #3 (foundation), [morpheum](https://github.com/anicolao/morpheum) PR #1-3 (3-hour MVP), [DikuMUD](https://github.com/anicolao/DikuMUD) PR #162 (design-first pattern), [llmdev](https://github.com/anicolao/llmdev) VISION.md creation and use.</small>
