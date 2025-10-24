---
layout: default
title: How To Get Started
---

# How To Get Started

When starting a new project with AI assistance, three elements set you up for success: a clear README, a compelling VISION, and a tiny MVP. This foundation enables rapid iteration while maintaining direction.

**Proven by evidence:** All 4 analyzed case studies (334+ PRs) used this pattern to achieve 3-11 PRs/day sustained velocity.

## 1. Have AI Create a Clear README

Your README is the contract between you and the AI. Use AI to create it, following this proven structure.

### How to Prompt AI for Your README

The key is **what you tell the AI about your project**, not what sections to create (AI handles structure automatically).

**What makes an effective prompt:**
- **The problem** you're solving
- **Key features** (2-3 specific capabilities)
- **Target users** or use cases
- **Technology choices** (if you have preferences)

**Example prompt from dikuclient case study:**
```markdown
Create a README for an efficient, modern DikuMUD client. 

It should have two modes:
(1) TUI directly in terminal
(2) TUI in web browser using websocket->socket proxy

Key features: ANSI color support, command history, triggers and aliases.
Target: MUD players who want a modern client experience.
```

**What AI generated from this:**
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

### Prompt Writing Tips

**Good prompts include:**
- Specific problem or need ("MUD client for DikuMUD")
- 2-3 key features or modes
- Target user or use case
- Technical preferences (optional)

**Avoid:**
- ❌ "Create a README for my project" (too vague)
- ❌ Long detailed specifications (AI gets confused)
- ❌ Telling AI what sections to include (it knows this)

**Pattern**: Brief (2-4 sentences) + Specific (features/modes) + Focused (one clear purpose)

**Evidence**: Projects with focused initial prompts needed 1-3 commits. Vague prompts needed 6+ commits of back-and-forth.

## 2. Have AI Create a Compelling VISION

Your VISION document captures the "why" and guides long-term direction. Use AI to create it following this proven template.

### How to Prompt AI for Your VISION

Focus on **why your project matters** and **what guides your decisions**. AI will handle the structure.

**What makes an effective prompt:**
- **The problem** in the world today
- **Your solution approach** (mission)
- **2-4 principles** that guide decisions
- **How you'll know** you're succeeding

**Example prompt from llmdev:**
```markdown
Create a VISION for a project that systematically studies how LLMs are used to build real software.

The problem: We're learning how to use AI tools effectively, but lack systematic analysis of what works.

Mission: Analyze real LLM-assisted projects to distill actionable insights for developers.

Principles: Evidence-based (real data), balanced (strengths and limitations), knowledge sharing (open findings).

Success: Developers make better decisions, tools improve, quality increases measurably.
```

**What AI generated from this:**

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

### How to Prompt AI for Your MVP

Focus on **one core feature** that proves the concept. Specify constraints to keep it tiny.

**What makes an effective MVP prompt:**
- Reference README/VISION (gives context)
- **ONE specific feature** to implement
- Explicit constraints ("minimal", "2-4 hours")
- **Technology choice** (language/framework)

**Example prompt from morpheum:**
```markdown
Based on the README and VISION: Create a TypeScript project that integrates with OpenAI API.

Implement ONLY: Send a prompt to OpenAI and get a response.

Constraints:
- Use TypeScript + Node.js
- One test that validates it works
- Working in 2-4 hours, not days
- Everything else comes later

This is the kernel—we'll build on it incrementally.
```

**What this produced:**

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

Focus on **what to tell AI** about your project, not how to structure the output.

### Step 1: README Prompt (5 minutes to write, AI creates in seconds)

```markdown
"Create a README for [type of project] that [core purpose].

Key features: [2-3 specific capabilities]
Target users: [who will use this]
Tech: [language/framework if you have preference]"
```

**Example**: "Create a README for a MUD client with terminal and web browser modes. Key features: ANSI colors, command history, triggers. Target: MUD players. Tech: Go or Rust."

### Step 2: VISION Prompt (5 minutes to write, AI creates in seconds)

```markdown
"Create a VISION for [project] that [mission].

Problem: [what's wrong today]
Solution: [your approach]
Principles: [2-4 decision guides]
Success: [how you'll measure it]"
```

**Example**: "Create a VISION for analyzing LLM-assisted development. Problem: lack systematic understanding. Solution: analyze real projects. Principles: evidence-based, balanced, open. Success: developers improve, tools improve."

### Step 3: MVP Prompt (10 minutes to write, AI builds in 2-4 hours)

```markdown
"Using README and VISION: Create [tech stack] project.

Implement ONLY: [one specific feature]
Constraints: minimal, 2-4 hours, one test
Everything else later"
```

**Example**: "Using README and VISION: Create TypeScript+Node project. Implement ONLY: connect to server and echo messages. Constraints: minimal, 2-4 hours, one test."

### Step 4: Iteration (ongoing)

```markdown
"Add [specific feature]. Keep changes minimal. Reference README/VISION."
```

## What Makes Prompts Effective

Learn from patterns in successful case studies.

### Anatomy of a Good Initial Prompt

**dikuclient's winning formula:**
1. **Clear objective**: "efficient, modern DikuMUD client"
2. **Specific modes**: "TUI in terminal OR web browser via websocket"
3. **Key constraints**: "Go or Rust" (gave options, required justification)
4. **Scope control**: "Write design doc only, no code"

**Why it worked:** Specific enough to guide AI, flexible enough to get good suggestions.

### Anatomy of a Good Feature Prompt

**Pattern from morpheum (PR #10):**
```markdown
"Integrate Copilot provider alongside OpenAI.

Requirements:
- Same LLMClient interface
- Support streaming responses
- Handle authentication

Constraints: minimal changes, reuse existing patterns"
```

**Why it worked:** 
- Referenced existing code (LLMClient interface)
- Specific requirements (not "make it better")
- Clear constraints (minimal changes)
- Result: 1 commit, 1h 18m

### Prompt Writing Principles

**Do:**
- ✅ Be specific about the problem/feature
- ✅ Give 2-3 concrete requirements
- ✅ State explicit constraints ("minimal", "2-4 hours")
- ✅ Reference existing docs (README/VISION)

**Don't:**
- ❌ Tell AI what sections/structure to create (it knows)
- ❌ Write long detailed specs (AI gets confused)
- ❌ Be vague ("make it better", "add features")
- ❌ Ask for everything at once

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
