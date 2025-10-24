---
layout: default
title: How To Get Started
---

# How To Get Started

When starting a new project with AI assistance, the foundation is critical: prompt AI to create both README and VISION together. This enables rapid iteration while maintaining direction.

**Proven by evidence:** All 4 analyzed case studies (334+ PRs) used this pattern to achieve 3-11 PRs/day sustained velocity.

## 1. Prompt AI to Create README + VISION Together

The most effective pattern is to have AI create README and VISION in the same prompt. This helps the LLM naturally separate concerns: practical "how to use" content goes in README, while high-level objectives and principles go in VISION.

### The Real Example: dikuclient Issue #1

Here's the actual prompt that started the dikuclient project (from [dikuclient case study](https://github.com/anicolao/llmdev/blob/main/case_studies/GITHUB_ANICOLAO_DIKUCLIENT.md)):

**Actual Issue #1 text:**

> "Create an efficient, modern DikuMUD client written in go or rust. It is to have two ways of being used: (1) as a TUI directly in the user's terminal; or (2) as a TUI inside a web browser using a websocket->socket proxy to connect to the actual mud, or suggest another approach to easily reuse the TUI. In mode (2) the same binary should be the other side of the proxy. Write a design doc *only*, no code, that specifies the overall structure of such a client for approval before we begin implementing. Justify the language choice and outline the approach for the TUI, and explain how it will work inside the browser interface."

**Why this prompt worked:**
- Clear objective with specific requirements
- Constraints specified (Go or Rust, dual-mode operation)
- Asks for design doc first, not code
- Requires justification of choices
- Result: Led to 63 PRs over 18 days with 3.5 PRs/day sustained velocity

**What it produced:** See the [dikuclient repository](https://github.com/anicolao/dikuclient) for the actual README and design documents that resulted.

### Pattern: Ask for Both Foundation Documents

When starting a project, prompt AI to create both README and VISION. This works because:
- LLM understands the separation of concerns implied by the document names
- README naturally captures practical details
- VISION naturally captures mission and principles
- Having both gives AI better context for all future work

**Evidence**: DikuMUD's VISION.md was referenced in 23 of 165 PRs to validate design decisions stayed on track.

## 2. Have AI Build a Tiny MVP

Don't aim for perfection—prompt AI to build the smallest thing that works and can serve as the kernel for growth.

### Real MVP Examples from Case Studies

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

See full details in the [morpheum case study](https://github.com/anicolao/llmdev/blob/main/case_studies/GITHUB_ANICOLAO_MORPHEUM.md) and [dikuclient case study](https://github.com/anicolao/llmdev/blob/main/case_studies/GITHUB_ANICOLAO_DIKUCLIENT.md).

### Why Tiny Matters

**Evidence from case studies:**
- **dikuclient**: Foundation in 3 PRs became basis for 63 total PRs
- **morpheum**: 3-hour MVP (3 PRs) enabled 73 more PRs  
- **Pattern**: Tiny kernel → rapid iteration

**Why this pattern works:**
- AI works better with small, focused tasks
- Fast feedback: See results immediately, adjust quickly
- Early success maintains momentum
- Everything else builds on this kernel

## Quick Start Pattern

Based on the real dikuclient example:

### Step 1: Foundation (README + VISION + Design)

Start with a comprehensive prompt like dikuclient's Issue #1 (shown above). This single prompt should:
- Describe the project clearly
- Specify key requirements and modes
- Ask for design/planning documents first
- Require justification of technical choices

### Step 2: Build Tiny MVP

After design approval, prompt for minimal implementation:
- ONE core feature that proves the concept
- Must build and run
- One test to validate it works
- Reference the design documents

### Step 3: Iterate

Add features incrementally, referencing README/VISION in each prompt.

## What Makes Prompts Effective

### The dikuclient Formula

The actual Issue #1 that started dikuclient (shown above) demonstrates:
1. **Clear objective**: "efficient, modern DikuMUD client"
2. **Specific modes**: "TUI in terminal OR web browser via websocket"
3. **Key constraints**: "Go or Rust" (gave options, required justification)
4. **Scope control**: "Write design doc only, no code"

**Result:** 63 PRs over 18 days with 3.5 PRs/day sustained velocity.

See the [dikuclient case study](https://github.com/anicolao/llmdev/blob/main/case_studies/GITHUB_ANICOLAO_DIKUCLIENT.md) for full analysis of what made this prompt effective.

## Success Metrics (from Case Studies)

You're on track if:

- First 3 PRs complete in one day
- You can demo working software on day 1
- Foundation enables rapid iteration on subsequent features

**Evidence**: All analyzed projects achieved 3-11 PRs/day sustained velocity with 1-3 commits per PR after establishing foundation.

## What's Next?

Once you have README + VISION + tiny MVP:

1. **[Staying Organized](staying-organized.html)**: Learn design-first development for complex features
2. **[Leveling Up](leveling-up.html)**: Discover patterns for rapid iteration
3. **[Sharpen the Saw](sharpen-the-saw.html)**: Master consolidation and refinement

---

<small>**Evidence sources**: [dikuclient](https://github.com/anicolao/dikuclient) Issue #1→PR #3 (foundation), [morpheum](https://github.com/anicolao/morpheum) PR #1-3 (3-hour MVP), [DikuMUD](https://github.com/anicolao/DikuMUD) PR #162 (design-first pattern), [llmdev](https://github.com/anicolao/llmdev) VISION.md creation and use.</small>
