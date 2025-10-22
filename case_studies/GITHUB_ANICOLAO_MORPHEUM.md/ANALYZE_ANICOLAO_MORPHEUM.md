# Analysis Instructions for anicolao/morpheum

This document provides structured instructions for analyzing the **anicolao/morpheum** repository using tools with Model Context Protocol (MCP) access to GitHub. Following these instructions will help you create a comprehensive case study without hitting API rate limits.

## Background

The llmdev project studies how LLMs like GitHub Copilot are used to build real software systems. This analysis should extract:
- Development story arc (how the project evolved from vision to current state)
- Prompt patterns (what requests drove development)
- Iteration patterns (which changes required more/fewer iterations)
- Success and challenge patterns

## Prerequisites

**Required Tool Access:**
- MCP-enabled tool with GitHub server access (e.g., GitHub Copilot with MCP support)
- Read access to the anicolao/morpheum repository

**Reference Materials:**
Review the case study format by examining:
- `case_studies/GITHUB_ANICOLAO_DIKUCLIENT.md` - Comprehensive case study example
- `case_studies/GITHUB_ANICOLAO_DIKU.md` - Shorter project example
- `.github/copilot-instructions.md` - Project guidelines

## Analysis Steps

### Phase 1: Repository Overview (10-15 minutes)

**Goal:** Understand the repository's purpose, scale, and history.

**Tasks:**
1. Use MCP to fetch repository metadata:
   - Description, language, creation date
   - Star count, fork count
   - README content

2. Get high-level statistics:
   - Total number of commits (approximate)
   - Total number of PRs (open and closed)
   - Total number of issues (open and closed)
   - Number of contributors

3. Identify the primary development period:
   - Date of first commit
   - Date of most recent commit
   - Any obvious gaps in activity

**Output:** Write a brief repository overview section.

### Phase 2: Detect LLM Usage Patterns (15-20 minutes)

**Goal:** Identify where and how LLMs (especially Copilot) were used.

**Tasks:**
1. Search for Copilot mentions in:
   - Issue titles and descriptions (search: "copilot" OR "co-pilot" OR "github copilot")
   - PR titles and descriptions
   - Commit messages

2. Look for bot-authored commits:
   - Commits by "Copilot" user
   - Commits by "copilot-swe-agent"
   - Branch names starting with "copilot/"

3. Identify transparent practices:
   - Branches named "copilot/*"
   - PR descriptions with [WIP] or checkboxes
   - Issues explicitly requesting Copilot work

**Output:** Create a "LLM Usage Detection" section with statistics.

### Phase 3: Extract Development Story Arc (30-45 minutes)

**Goal:** Trace the project's evolution from inception to current state.

**Tasks:**
1. Find the origin story:
   - Look at Issue #1 or the earliest issues
   - Read the initial PR descriptions
   - Identify the original vision/goal

2. Map development phases:
   - Group issues/PRs by theme or time period
   - Identify major milestones (e.g., "MVP complete", "feature X added")
   - Look for design documents or planning issues

3. For each phase, note:
   - Time period
   - Main features/changes
   - Key PRs (reference by number)
   - Velocity (PRs/day or issues/week)

4. Extract 5-10 representative PRs that tell the story:
   - Include PR number, title, and brief description
   - Note commit count (iteration indicator)
   - Note time to merge

**Output:** Write "Development Story Arc" section with chronological phases.

### Phase 4: Analyze Prompts and Requests (30-45 minutes)

**Goal:** Understand what requests/prompts drove development.

**Tasks:**
1. For each major PR/issue, extract the original prompt:
   - Look for sections like "Task Request:", "## Problem", "## Goal"
   - Copy the original text (don't paraphrase)
   - Note the PR/issue number

2. Categorize prompts by type:
   - Vision/Planning: "Design a system that..."
   - Feature: "Add support for X"
   - Bug Fix: "Fix issue where..."
   - Refinement: "Improve the..."
   - Documentation: "Document how to..."

3. Analyze prompt characteristics:
   - Specificity: Vague vs detailed
   - Context: Background information provided?
   - Constraints: Explicit requirements or limitations?
   - Examples: Concrete examples given?

4. Identify effective prompt patterns:
   - What structure do successful prompts use?
   - Do they follow Problem-Context-Solution format?
   - Are verification criteria specified?

**Output:** Write "Prompt Analysis" section with examples and patterns.

### Phase 5: Iteration Pattern Analysis (20-30 minutes)

**Goal:** Understand which work required more/fewer iterations and why.

**Tasks:**
1. For 15-20 representative PRs, collect:
   - PR number and title
   - Number of commits
   - Time between creation and merge
   - Complexity indicators (lines changed, files changed)

2. Classify PRs into patterns:
   - **Quick Win** (1-2 commits, same day): Why was this fast?
   - **Normal** (3-5 commits, 1-2 days): Standard complexity
   - **Complex** (6+ commits or >3 days): What made this hard?

3. Look for correlation with:
   - Prompt specificity
   - Novel vs familiar features
   - Foundation vs feature work

4. Extract lessons:
   - What predicts quick success?
   - What causes extra iterations?
   - How does project maturity affect iteration?

**Output:** Write "Iteration Patterns" section with classification and insights.

### Phase 6: Identify Development Patterns (20-30 minutes)

**Goal:** Extract reusable patterns and practices.

**Tasks:**
1. Look for successful patterns:
   - Design-first approach (design docs before code)
   - Checkpoint PRs (consolidation/refactoring)
   - Progressive enhancement (MVP → features → polish)
   - Explicit verification criteria in PRs
   - Use of [WIP] for transparency

2. Look for challenges:
   - Where did the project struggle?
   - Were there abandoned PRs or issues?
   - Any major pivots or redesigns?

3. Identify domain-specific patterns:
   - Are there patterns unique to this project's domain?
   - How does the tech stack influence development?

**Output:** Write "Development Patterns" section with 5-7 patterns.

### Phase 7: Best Practices and Recommendations (15-20 minutes)

**Goal:** Distill actionable guidance for readers.

**Tasks:**
1. Based on observations, create:
   - **Best Practices**: What worked well (with PR examples)
   - **Anti-Patterns**: What to avoid
   - **Prompt Templates**: Reusable prompt structures
   - **Decision Framework**: When to use which approach

2. Tailor recommendations for:
   - Developers using LLM tools
   - Teams adopting AI-assisted development
   - Similar projects in this domain

3. Include specific, measurable advice:
   - "Use Problem-Context-Solution format for prompts"
   - "Aim for 3-5 commits per PR for optimal iteration"
   - "Create design docs before implementation for complex features"

**Output:** Write "Best Practices" and "Recommendations" sections.

### Phase 8: Final Synthesis (15-20 minutes)

**Goal:** Create executive summary and key takeaways.

**Tasks:**
1. Write Executive Summary (3-5 paragraphs):
   - Project overview
   - Key statistics
   - Main insights
   - Unique aspects

2. Create Key Takeaways (5-7 bullet points):
   - Most important lessons
   - Surprising findings
   - Universal vs domain-specific insights

3. Add Methodology section:
   - Explain how analysis was performed
   - Note any limitations
   - Acknowledge what couldn't be analyzed

4. Add Conclusion:
   - Summarize value of this case study
   - Point to patterns others can replicate

**Output:** Complete the case study document.

## Output Format

Save your analysis as: `case_studies/GITHUB_ANICOLAO_MORPHEUM.md`

Use this structure:

```markdown
# Case Study: anicolao/morpheum

## Executive Summary

[3-5 paragraphs summarizing the project and key findings]

## Development Story Arc

### Phase 1: [Name] ([Dates])
- Key activities
- Major PRs: #X, #Y
- Velocity: N PRs/day

[Continue for each phase...]

## Prompt Analysis

### Effective Prompt Patterns
- Pattern 1: [Name and example]
- Pattern 2: [Name and example]

### Prompt Examples
**PR #X: [Title]**
```
[Original prompt text]
```
Result: [Commits, time, success]

## Iteration Patterns

### Quick Wins (1-2 commits)
- PR #X: [Title] - Why fast: [reason]

### Complex Work (6+ commits)
- PR #Y: [Title] - Why complex: [reason]

## Development Patterns

1. **[Pattern Name]**: Description with PR examples
2. **[Pattern Name]**: Description with PR examples

## What Went Well

- Success 1 (PR #X)
- Success 2 (PR #Y)

## Challenges & Learnings

- Challenge 1 (PR #Z) - How it was addressed
- Challenge 2 (Issue #N) - Lessons learned

## Best Practices

### For Developers
1. Practice 1 - Why it works
2. Practice 2 - Why it works

### For Teams
1. Practice 1
2. Practice 2

## Key Takeaways

1. Takeaway 1
2. Takeaway 2

## Technical Insights

[Domain or tech-specific observations]

## Conclusion

[Wrap up the case study]

## Appendix: Methodology

**Analysis Performed:** [Date]
**Tool Used:** MCP-enabled analysis tool
**Scope:** [Number of PRs/issues analyzed]
**Limitations:** [Any gaps in the analysis]
```

## Tips for Success

1. **Be Evidence-Based**: Every claim should reference specific PRs, issues, or commits
2. **Quote Original Text**: Don't paraphrase prompts - quote them exactly
3. **Show Your Work**: Include PR numbers so readers can verify
4. **Be Balanced**: Document both successes and challenges
5. **Make It Actionable**: Readers should know what to do differently
6. **Compare When Possible**: Reference other case studies for context

## Rate Limit Management

**Advantages of MCP Approach:**
- MCP server handles rate limiting internally
- Can fetch more data per request
- Built-in caching and optimization
- No need to track API quota manually

**Best Practices:**
- Fetch data in bulk when possible (all PRs, then analyze)
- Don't fetch the same data twice
- Use search with specific queries rather than listing everything

## Questions or Issues?

If you encounter problems or need clarification:
1. Check existing case studies for examples
2. Review `.github/copilot-instructions.md` for project guidelines
3. Ask for guidance from the llmdev maintainers

---

**Estimated Time:** 2-3 hours for comprehensive analysis
**Output:** 30-50 page case study document
**Value:** Actionable insights for LLM-assisted development community
