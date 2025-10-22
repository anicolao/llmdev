"""
Generate analysis instructions for MCP-enabled tools.

This module creates structured analysis instructions that can be used with
Model Context Protocol (MCP) enabled tools like GitHub Copilot to analyze
repositories without hitting API rate limits.
"""

import logging
from typing import Dict, Any, Optional
from pathlib import Path


logger = logging.getLogger(__name__)


class MCPInstructionsGenerator:
    """Generate MCP-compatible analysis instructions for repositories."""
    
    # Define all available phases
    PHASES = [
        "intro",
        "overview",
        "detection",
        "story",
        "prompts",
        "iteration",
        "patterns",
        "recommendations",
        "synthesis",
    ]

    def __init__(self, output_dir: Path):
        """
        Initialize the instructions generator.

        Args:
            output_dir: Directory where instructions will be saved
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate(self, owner: str, repo: str, phase: Optional[str] = None) -> Path:
        """
        Generate analysis instructions for a repository.

        Args:
            owner: Repository owner
            repo: Repository name
            phase: Optional phase name to generate instructions for a specific phase.
                   If None, generates full instructions (legacy mode).
                   Valid phases: intro, overview, detection, story, prompts, 
                                iteration, patterns, recommendations, synthesis

        Returns:
            Path to the generated instructions file
        """
        if phase and phase not in self.PHASES:
            raise ValueError(
                f"Invalid phase '{phase}'. Valid phases: {', '.join(self.PHASES)}"
            )
        
        if phase:
            logger.info(f"Generating phase '{phase}' instructions for {owner}/{repo}")
            instructions = self._build_phase_instructions(owner, repo, phase)
            output_path = self.output_dir / f"ANALYZE_{owner.upper()}_{repo.upper()}_PHASE_{phase.upper()}.md"
        else:
            logger.info(f"Generating full MCP analysis instructions for {owner}/{repo}")
            instructions = self._build_instructions(owner, repo)
            output_path = self.output_dir / f"ANALYZE_{owner.upper()}_{repo.upper()}.md"

        with open(output_path, "w") as f:
            f.write(instructions)

        logger.info(f"Instructions saved to: {output_path}")
        return output_path

    def _build_instructions(self, owner: str, repo: str) -> str:
        """
        Build the structured analysis instructions.

        Args:
            owner: Repository owner
            repo: Repository name

        Returns:
            Markdown formatted instructions
        """
        return f"""# Analysis Instructions for {owner}/{repo}

This document provides structured instructions for analyzing the **{owner}/{repo}** repository using tools with Model Context Protocol (MCP) access to GitHub. Following these instructions will help you create a comprehensive case study without hitting API rate limits.

## Background

The llmdev project studies how LLMs like GitHub Copilot are used to build real software systems. This analysis should extract:
- Development story arc (how the project evolved from vision to current state)
- Prompt patterns (what requests drove development)
- Iteration patterns (which changes required more/fewer iterations)
- Success and challenge patterns

## Prerequisites

**Required Tool Access:**
- MCP-enabled tool with GitHub server access (e.g., GitHub Copilot with MCP support)
- Read access to the {owner}/{repo} repository

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

Save your analysis as: `case_studies/GITHUB_{owner.upper()}_{repo.upper()}.md`

Use this structure:

```markdown
# Case Study: {owner}/{repo}

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
"""

    def _build_phase_instructions(self, owner: str, repo: str, phase: str) -> str:
        """
        Build instructions for a specific phase.
        
        Args:
            owner: Repository owner
            repo: Repository name
            phase: Phase name
            
        Returns:
            Markdown formatted instructions for the specified phase
        """
        phase_builders = {
            "intro": self._phase_intro,
            "overview": self._phase_overview,
            "detection": self._phase_detection,
            "story": self._phase_story,
            "prompts": self._phase_prompts,
            "iteration": self._phase_iteration,
            "patterns": self._phase_patterns,
            "recommendations": self._phase_recommendations,
            "synthesis": self._phase_synthesis,
        }
        
        return phase_builders[phase](owner, repo)
    
    def _phase_intro(self, owner: str, repo: str) -> str:
        """Introduction and context for the analysis."""
        return f"""# Analysis Instructions for {owner}/{repo} - Introduction

## Background

The llmdev project studies how LLMs like GitHub Copilot are used to build real software systems. This analysis will extract:
- Development story arc (how the project evolved from vision to current state)
- Prompt patterns (what requests drove development)
- Iteration patterns (which changes required more/fewer iterations)
- Success and challenge patterns

## Prerequisites

**Required Tool Access:**
- MCP-enabled tool with GitHub server access (e.g., GitHub Copilot with MCP support)
- Read access to the {owner}/{repo} repository

**Reference Materials:**
Review the case study format by examining:
- `case_studies/GITHUB_ANICOLAO_DIKUCLIENT.md` - Comprehensive case study example
- `case_studies/GITHUB_ANICOLAO_DIKU.md` - Shorter project example
- `.github/copilot-instructions.md` - Project guidelines

## Analysis Workflow

This analysis is broken into phases to avoid overwhelming context windows:

1. **intro** - This introduction (you are here)
2. **overview** - Repository metadata and statistics
3. **detection** - LLM usage pattern detection
4. **story** - Development story arc extraction
5. **prompts** - Prompt and request analysis
6. **iteration** - Iteration pattern analysis
7. **patterns** - Development pattern identification
8. **recommendations** - Best practices synthesis
9. **synthesis** - Executive summary and key takeaways

**To proceed:** Generate the next phase instructions using:
```
llmdev generate-instructions {owner}/{repo} --phase overview
```

## Output Structure

You will build the case study incrementally in:
`case_studies/GITHUB_{owner.upper()}_{repo.upper()}.md`

Start with this template structure:

```markdown
# Case Study: {owner}/{repo}

## Executive Summary
[To be completed in synthesis phase]

## Development Story Arc
[To be completed in story phase]

## Prompt Analysis
[To be completed in prompts phase]

## Iteration Patterns
[To be completed in iteration phase]

## Development Patterns
[To be completed in patterns phase]

## What Went Well
[To be completed in recommendations phase]

## Challenges & Learnings
[To be completed in recommendations phase]

## Best Practices
[To be completed in recommendations phase]

## Key Takeaways
[To be completed in synthesis phase]

## Technical Insights
[To be completed throughout]

## Conclusion
[To be completed in synthesis phase]

## Appendix: Methodology
[To be completed in synthesis phase]
```

---

**Next Step:** Run `llmdev generate-instructions {owner}/{repo} --phase overview` to begin Phase 1.
"""

    def _phase_overview(self, owner: str, repo: str) -> str:
        """Repository overview phase."""
        return f"""# Phase 1: Repository Overview - {owner}/{repo}

**Time Estimate:** 10-15 minutes
**Goal:** Understand the repository's purpose, scale, and history.

## Tasks

1. **Fetch repository metadata using MCP:**
   - Use `github-mcp-server-get_file_contents` to read README.md
   - Look at repository description and primary language
   - Note creation date and last update

2. **Get high-level statistics:**
   - Total number of commits (use `github-mcp-server-list_commits` with pagination)
   - Total number of PRs (use `github-mcp-server-list_pull_requests`)
   - Total number of issues (use `github-mcp-server-list_issues`)
   - Number of contributors (check commit authors)
   - Repository size indicators (files, lines of code if visible)

3. **Identify the primary development period:**
   - Date of first commit
   - Date of most recent commit
   - Any obvious gaps in activity (look at commit timeline)

4. **Read the README:**
   - What is the project's purpose?
   - What technologies does it use?
   - Is there documentation about architecture or design?

## Output

Add to your case study document (`case_studies/GITHUB_{owner.upper()}_{repo.upper()}.md`):

### Section: Project Overview (add after Executive Summary placeholder)

```markdown
## Project Overview

**Repository:** {owner}/{repo}
**Purpose:** [Brief description from README]
**Primary Language:** [Language]
**Tech Stack:** [Key technologies]

**Development Statistics:**
- **Period:** [First commit date] to [Last commit date]
- **Total Commits:** ~[number]
- **Total PRs:** [number] ([X] open, [Y] closed)
- **Total Issues:** [number] ([X] open, [Y] closed)
- **Contributors:** [number]
- **Activity:** [e.g., "Active development" or "Completed project"]

**Project Type:** [e.g., "CLI tool", "Web application", "Library", etc.]
**Domain:** [e.g., "Gaming", "Productivity", "Developer Tools"]
```

## Reflection

Before proceeding:
- Do you understand what this project does?
- Is this a active or historical project?
- What scale is this project (toy, personal tool, production app)?

## Next Step

Run `llmdev generate-instructions {owner}/{repo} --phase detection` for Phase 2.
"""

    def _phase_detection(self, owner: str, repo: str) -> str:
        """LLM usage detection phase."""
        return f"""# Phase 2: Detect LLM Usage Patterns - {owner}/{repo}

**Time Estimate:** 15-20 minutes
**Goal:** Identify where and how LLMs (especially Copilot) were used.

## Tasks

1. **Search for Copilot mentions in issues:**
   - Use `github-mcp-server-search_issues` with query: "copilot OR co-pilot OR github copilot repo:{owner}/{repo}"
   - Count total mentions
   - Note which issues explicitly request Copilot work
   - Look for patterns in how Copilot is referenced

2. **Search for Copilot mentions in PRs:**
   - Use `github-mcp-server-search_pull_requests` with query: "copilot repo:{owner}/{repo}"
   - Count PR titles and descriptions mentioning Copilot
   - Look for patterns: [WIP], checklists, explicit task requests

3. **Examine branch names:**
   - Use `github-mcp-server-list_branches` to get all branches
   - Count branches starting with "copilot/"
   - This indicates transparent labeling of AI-generated work

4. **Check for bot-authored commits:**
   - Look for commits by usernames like "copilot", "copilot-swe-agent"
   - Use `github-mcp-server-search_code` to find references to copilot in commit messages

5. **Identify transparency practices:**
   - Do PR descriptions clearly state they're Copilot-generated?
   - Are there patterns like "[WIP]" or structured checklists?
   - Is there evidence of human oversight and iteration?

## Output

Add to your case study document:

### Section: LLM Usage Detection

```markdown
## LLM Usage Detection

**Copilot Detection Summary:**
- **Total Detections:** [number]
- **Issues mentioning Copilot:** [number]
- **PRs mentioning Copilot:** [number]
- **Copilot-prefixed branches:** [number]
- **Bot-authored commits:** [number if any]

**Confidence:** [High/Medium/Low - based on explicit vs implicit evidence]

**Transparency Indicators:**
- ✅/❌ Branches explicitly labeled (copilot/*)
- ✅/❌ PR descriptions declare Copilot usage
- ✅/❌ [WIP] tags used during development
- ✅/❌ Checklists showing iteration process
- ✅/❌ Explicit task requests in issues/PRs

**Detection by Source:**
| Source | Count | Percentage |
|--------|-------|------------|
| Issues | [X] | [Y]% |
| PRs | [X] | [Y]% |
| Branches | [X] | [Y]% |
| Commits | [X] | [Y]% |

**Example References:**
- Issue #[N]: [Brief description of how Copilot was mentioned]
- PR #[N]: [Brief description]
```

## Reflection

- Is this clearly a Copilot-assisted project?
- How transparent is the development process?
- Are there interesting patterns in how Copilot is used?

## Next Step

Run `llmdev generate-instructions {owner}/{repo} --phase story` for Phase 3.
"""

    def _phase_story(self, owner: str, repo: str) -> str:
        """Development story arc phase."""
        return f"""# Phase 3: Extract Development Story Arc - {owner}/{repo}

**Time Estimate:** 30-45 minutes
**Goal:** Trace the project's evolution from inception to current state.

## Tasks

1. **Find the origin story:**
   - Use `github-mcp-server-get_issue` to read Issue #1 (if it exists)
   - Read the earliest few PRs using `github-mcp-server-list_pull_requests` sorted by created
   - Look for design documents or planning issues
   - Identify: What was the original vision/goal?

2. **Map development chronologically:**
   - Get all PRs in chronological order
   - Group them by time periods or themes
   - Identify major milestones (look for PRs like "MVP", "v1.0", etc.)
   - Note velocity changes (fast initial development vs later refinement)

3. **Identify development phases:**
   Create 4-6 phases that tell the story. Common patterns:
   - Phase 1: Vision & Planning (design docs, architecture decisions)
   - Phase 2: Foundation (core infrastructure, basic functionality)
   - Phase 3: Core Features (main functionality implemented)
   - Phase 4: Enhancement (additional features, UX improvements)
   - Phase 5: Refinement (bug fixes, polish, optimization)
   - Phase 6: Maintenance (ongoing updates, if applicable)

4. **For each phase, document:**
   - Time period (dates)
   - Main focus/goal
   - Key PRs (5-10 most significant, with PR numbers)
   - Velocity (PRs per day/week)
   - Notable achievements or challenges

5. **Extract representative PRs:**
   For 10-15 significant PRs across all phases:
   - Use `github-mcp-server-pull_request_read` with method="get" to get details
   - Note: PR number, title, description summary
   - Note: Number of commits (iteration indicator)
   - Note: Time to merge (created_at to merged_at)
   - Note: Size indicators (if visible: files changed, lines changed)

## Output

Add to your case study document:

### Section: Development Story Arc

```markdown
## Development Story Arc

### Phase 1: [Phase Name] ([Start Date] - [End Date])

**Focus:** [Main goal or theme of this phase]

**Key Activities:**
- [Activity 1]
- [Activity 2]

**Major PRs:**
- **PR #[N]**: [Title] ([X] commits, merged in [Y] days)
  - [Brief description of what this accomplished]
- **PR #[N]**: [Title] ([X] commits, merged in [Y] days)
  - [Brief description]

**Velocity:** [X] PRs over [Y] days = [Z] PRs/day

**Achievements:**
- [What was accomplished in this phase]

**Challenges:**
- [Any obstacles encountered]

[Repeat for each phase...]

### Timeline Visualization

```
Week 1-2: Vision & Planning
├─ Issue #1: Original vision
└─ PR #2: Design document

Week 3-4: Foundation
├─ PR #3: Core infrastructure
├─ PR #5: Basic functionality
└─ PR #7: First working version

[Continue timeline...]
```

### Development Velocity Analysis

| Phase | Duration | PRs | Velocity | Characteristics |
|-------|----------|-----|----------|-----------------|
| 1. Vision | [X days] | [Y] | [Z/day] | [Planning-heavy] |
| 2. Foundation | [X days] | [Y] | [Z/day] | [High iteration] |
[...]
```

## Reflection

- Does the story arc make sense chronologically?
- Can you identify clear inflection points or milestones?
- How did the project's focus evolve over time?

## Next Step

Run `llmdev generate-instructions {owner}/{repo} --phase prompts` for Phase 4.
"""

    def _phase_prompts(self, owner: str, repo: str) -> str:
        """Prompt analysis phase."""
        return f"""# Phase 4: Analyze Prompts and Requests - {owner}/{repo}

**Time Estimate:** 30-45 minutes
**Goal:** Understand what requests/prompts drove development.

## Tasks

1. **Extract original prompts:**
   For the 10-15 representative PRs identified in Phase 3:
   - Use `github-mcp-server-pull_request_read` with method="get"
   - Look for structured sections in PR bodies:
     * "Task Request:"
     * "## Problem"
     * "## Goal"
     * "## Requirements"
     * Issue references (may need to fetch those issues too)
   - **Copy the exact text** - don't paraphrase
   - Note the PR/issue number for each prompt

2. **Categorize prompts by type:**
   - **Vision/Planning**: "Design a system that..."
   - **Feature**: "Add support for X"
   - **Bug Fix**: "Fix issue where..."
   - **Refinement**: "Improve the..."
   - **Documentation**: "Document how to..."

3. **Analyze prompt characteristics:**
   For each prompt, rate:
   - **Specificity**: Vague (1) to Very Detailed (5)
   - **Context**: None (1) to Comprehensive (5)
   - **Constraints**: None (1) to Many Explicit (5)
   - **Examples**: No examples (0) to Multiple examples (5)

4. **Correlate with outcomes:**
   - How many commits did this PR take?
   - How long to merge?
   - Was the work completed successfully?
   - Did it require rework or follow-up PRs?

5. **Identify effective patterns:**
   - Do successful prompts share common structure?
   - Problem-Context-Solution format?
   - Checklists with verification criteria?
   - References to similar work?

## Output

Add to your case study document:

### Section: Prompt Analysis

```markdown
## Prompt Analysis

### Prompt Extraction

#### PR #[N]: [Title] ([Category])

**Original Prompt:**
```
[Exact text from PR description or linked issue]
```

**Characteristics:**
- Specificity: [1-5] - [Brief justification]
- Context: [1-5] - [Brief justification]
- Constraints: [1-5] - [Count of explicit requirements]
- Examples: [0-5] - [Were examples provided?]

**Outcome:**
- Commits: [X]
- Time to merge: [Y] days/hours
- Success: [Yes/No/Partial]
- Follow-up required: [Yes/No]

[Repeat for 8-12 representative PRs...]

### Effective Prompt Patterns

#### Pattern 1: Problem-Context-Solution
**Structure:**
1. Clear problem statement
2. Background context
3. Suggested approach or constraints
4. Verification criteria

**Example:** PR #[N]
**Success Rate:** [X]% of PRs using this pattern completed in 1-3 commits

#### Pattern 2: [Another pattern you identify]
[Description and example]

### Prompt Effectiveness Correlation

| Prompt Type | Avg Commits | Avg Time | Success Rate |
|-------------|-------------|----------|--------------|
| Vague | [X] | [Y] days | [Z]% |
| Moderate | [X] | [Y] days | [Z]% |
| Detailed | [X] | [Y] days | [Z]% |
| With Examples | [X] | [Y] days | [Z]% |

### Anti-Patterns

**Anti-Pattern 1: [Name]**
- Description: [What makes this ineffective]
- Example: PR #[N]
- Impact: [How it caused problems]

[List 2-3 anti-patterns if identified]
```

## Reflection

- What makes a prompt effective for this project?
- Are there domain-specific prompt patterns?
- How does prompt quality correlate with iteration count?

## Next Step

Run `llmdev generate-instructions {owner}/{repo} --phase iteration` for Phase 5.
"""

    def _phase_iteration(self, owner: str, repo: str) -> str:
        """Iteration pattern analysis phase."""
        return f"""# Phase 5: Iteration Pattern Analysis - {owner}/{repo}

**Time Estimate:** 20-30 minutes
**Goal:** Understand which work required more/fewer iterations and why.

## Tasks

1. **Classify PRs by iteration count:**
   Using the PRs from Phase 3, categorize:
   - **Quick Win** (1-2 commits, merged same day)
   - **Normal** (3-5 commits, 1-2 days)
   - **Complex** (6-10 commits, 2-5 days)
   - **Very Complex** (11+ commits or >5 days)

2. **Analyze Quick Wins:**
   - What characteristics do they share?
   - Clear requirements? Building on existing patterns? Small scope?
   - Extract 3-5 examples

3. **Analyze Complex Work:**
   - What made these PRs difficult?
   - Ambiguous requirements? Novel features? Integration challenges?
   - Look at commit messages for clues (fix, update, adjust, etc.)
   - Extract 3-5 examples

4. **Look for patterns:**
   - Do certain types of work always take more iterations?
   - Does project maturity affect iteration count?
   - How does prompt specificity correlate?
   - Are there "reset and retry" patterns (many commits, then new PR)?

5. **Extract lessons:**
   - What predicts quick success?
   - What causes extra iterations?
   - How does the project show learning over time?

## Output

Add to your case study document:

### Section: Iteration Patterns

```markdown
## Iteration Patterns

### Classification Summary

| Pattern | Count | % of Total | Avg Commits | Avg Time |
|---------|-------|-----------|-------------|----------|
| Quick Win | [X] | [Y]% | [Z] | [Hours] |
| Normal | [X] | [Y]% | [Z] | [1-2 days] |
| Complex | [X] | [Y]% | [Z] | [3-5 days] |
| Very Complex | [X] | [Y]% | [Z] | [>5 days] |

### Quick Wins (1-2 commits, same day)

**Characteristics:**
- Well-defined requirements with clear acceptance criteria
- Building on established patterns or existing code
- Small, focused scope
- Usually done after project has stable foundation

**Examples:**

**PR #[N]: [Title]**
- Commits: 1
- Time: [X] hours
- Why Fast: [Specific reason - e.g., "Clear requirement, followed existing pattern for similar feature"]

[Repeat for 2-4 more examples]

### Normal Complexity (3-5 commits)

**Characteristics:**
- Standard complexity requiring plan → implement → fix cycle
- Some edge cases discovered during implementation
- Integration with existing components needs adjustment

**Examples:**

**PR #[N]: [Title]**
- Commits: [X]
- Time: [Y] days
- Iteration Pattern: [e.g., "Initial implementation, bug fix, refinement based on testing"]

[Repeat for 2-3 examples]

### Complex Work (6+ commits)

**Characteristics:**
- Novel features without existing patterns to follow
- Ambiguous requirements requiring clarification
- Technical challenges or limitations discovered
- Multiple integration points

**Examples:**

**PR #[N]: [Title]**
- Commits: [X]
- Time: [Y] days
- Why Complex: [Detailed explanation of what made this hard]
- Iteration Pattern: [e.g., "Multiple approaches tried, significant rework after initial implementation"]

[Repeat for 2-3 examples]

### Iteration Trends Over Time

**Early Project (First [X] PRs):**
- Average: [Y] commits/PR
- Characteristics: [More experimentation, foundation building]

**Mid Project (PR [X]-[Y]):**
- Average: [Z] commits/PR
- Characteristics: [Building on established patterns]

**Late Project (PR [Y]+):**
- Average: [W] commits/PR
- Characteristics: [Refinement, fewer surprises]

### Factors Affecting Iteration Count

**Factors Associated with Quick Success:**
1. [Factor 1 - e.g., "Detailed prompt with examples"]
2. [Factor 2 - e.g., "Similar feature already exists"]
3. [Factor 3]

**Factors Associated with More Iteration:**
1. [Factor 1 - e.g., "Vague requirements"]
2. [Factor 2 - e.g., "Novel technical approach"]
3. [Factor 3]

### Key Insights

- [Insight 1 about iteration patterns]
- [Insight 2]
- [Insight 3]
```

## Reflection

- Do you see learning/improvement over time?
- Are iteration patterns predictable based on work type?
- What advice would you give to reduce iterations?

## Next Step

Run `llmdev generate-instructions {owner}/{repo} --phase patterns` for Phase 6.
"""

    def _phase_patterns(self, owner: str, repo: str) -> str:
        """Development patterns phase."""
        return f"""# Phase 6: Identify Development Patterns - {owner}/{repo}

**Time Estimate:** 20-30 minutes
**Goal:** Extract reusable patterns and practices.

## Tasks

1. **Look for successful patterns:**
   Review PRs and issues for evidence of:
   - **Design-first approach**: Design docs before implementation
   - **Checkpoint PRs**: Consolidation/refactoring between features
   - **Progressive enhancement**: MVP → features → polish
   - **Explicit verification**: Test criteria in PR descriptions
   - **Transparency markers**: [WIP], checklists, clear status
   - **Iterative refinement**: Small PRs building toward goal
   - **Template usage**: Consistent PR description format

2. **Look for challenges:**
   - Where did the project struggle?
   - Were there abandoned PRs or issues?
   - Any major pivots or redesigns?
   - False starts that were restarted?

3. **Identify domain-specific patterns:**
   - Are there patterns unique to this project's domain?
   - How does the tech stack influence development?
   - Language-specific patterns (e.g., Go vs Python vs JavaScript)?

4. **Look for collaboration patterns:**
   - How are reviews handled?
   - Are there pair programming indicators?
   - How is feedback incorporated?

5. **Extract the "why" behind patterns:**
   - Why did certain approaches work well?
   - What made challenges challenging?
   - How did the team adapt over time?

## Output

Add to your case study document:

### Section: Development Patterns

```markdown
## Development Patterns

### Pattern 1: [Pattern Name]

**Description:** [What the pattern is]

**Evidence:**
- PR #[N]: [How this PR exemplifies the pattern]
- PR #[M]: [Another example]

**Why It Works:** [Explanation of effectiveness]

**When to Apply:** [Guidance on when this pattern is appropriate]

[Repeat for 5-7 patterns...]

### Pattern Examples from This Project

#### Pattern: [Specific Pattern Name]

**Example: PR #[N] - [Title]**

Context: [What was being attempted]

Approach: [How the pattern was applied]

Result: [What happened - commits, time, success]

Lesson: [What we learn from this]

[Repeat for 3-5 concrete examples]

### Challenges and How They Were Addressed

#### Challenge 1: [Description]

**Where it occurred:** PR #[N], Issue #[M]

**Root cause:** [Why this was difficult]

**How addressed:** [What was done to resolve it]

**Lesson learned:** [Takeaway for future work]

[Repeat for 3-4 major challenges]

### Abandoned or Pivoted Work

**PR/Issue #[N]: [Title]**
- Original goal: [What was attempted]
- Why abandoned/pivoted: [Reason]
- What happened instead: [Alternative approach]
- Lesson: [What this teaches us]

[If any exist - this shows honest learning]

### Domain-Specific Patterns

**Pattern: [Name specific to this domain]**
- Description: [How this relates to the project's domain]
- Example: [Specific instance]
- Applicability: [When others in this domain should use it]

### Technology Stack Influence

**How [Language/Framework] Shaped Development:**
- [Observation 1 about tech stack impact]
- [Observation 2]

**Examples:**
- PR #[N]: [How tech stack enabled quick development]
- PR #[M]: [Or created challenges]

### Development Philosophy

Based on observed patterns, this project follows:
- [Philosophy point 1 - e.g., "Design before code"]
- [Philosophy point 2 - e.g., "Transparency in process"]
- [Philosophy point 3 - e.g., "Iterative refinement over big-bang releases"]
```

## Reflection

- Which patterns are universally applicable?
- Which are specific to this project/domain/tech stack?
- What surprised you about how development proceeded?

## Next Step

Run `llmdev generate-instructions {owner}/{repo} --phase recommendations` for Phase 7.
"""

    def _phase_recommendations(self, owner: str, repo: str) -> str:
        """Best practices and recommendations phase."""
        return f"""# Phase 7: Best Practices and Recommendations - {owner}/{repo}

**Time Estimate:** 15-20 minutes
**Goal:** Distill actionable guidance for readers.

## Tasks

1. **Synthesize best practices:**
   Review all previous phases and extract:
   - What consistently led to success?
   - What patterns should be replicated?
   - What anti-patterns should be avoided?
   - What prompt templates worked well?

2. **Categorize recommendations:**
   - For developers using LLM tools
   - For teams adopting AI-assisted development
   - For similar projects in this domain
   - For specific technical stacks

3. **Make recommendations specific and measurable:**
   - Bad: "Write good prompts"
   - Good: "Use Problem-Context-Solution format with 2-3 examples (see PR #X)"
   - Bad: "Iterate appropriately"
   - Good: "Aim for 3-5 commits per PR; 6+ often indicates unclear requirements"

4. **Provide templates and formulas:**
   - Prompt template that worked
   - PR description template used
   - Checklist approach
   - Decision framework

5. **Back everything with evidence:**
   - Each recommendation should reference specific PRs
   - Show before/after or good/bad examples
   - Provide metrics where possible

## Output

Add to your case study document:

### Section: Best Practices

```markdown
## Best Practices

### For Developers Using LLM Tools

#### 1. [Practice Name]

**What to do:** [Specific, actionable guidance]

**Why it works:** [Explanation based on observations]

**Evidence:** PR #[N] achieved [result] using this approach

**Example:**
```
[Show the actual prompt, code, or approach used]
```

**Anti-pattern to avoid:** [What NOT to do, with example]

[Repeat for 5-7 practices for developers]

### For Teams Adopting AI-Assisted Development

#### 1. [Team Practice]

**Practice:** [What teams should do]

**Implementation:** [How to actually do it]

**Benefits:** [What teams gain]

**Example from {owner}/{repo}:** [Specific evidence]

[Repeat for 3-5 team practices]

### Domain-Specific Recommendations

**For [Domain Type] Projects:**

1. [Specific recommendation for this domain]
   - Why: [Reason]
   - Example: PR #[N]

[Provide 3-4 domain-specific recommendations]

### Prompt Templates

#### Template 1: Problem-Context-Solution

```markdown
## Problem
[Clear statement of what needs to be solved/built]

## Context
[Background information, why this matters, related work]

## Proposed Solution
[Suggested approach, constraints, requirements]

## Verification Criteria
- [ ] [Specific testable criterion 1]
- [ ] [Specific testable criterion 2]
```

**When to use:** [Guidance]
**Success rate in {owner}/{repo}:** [X]% completed in [Y] commits
**Examples:** PRs #[N], #[M]

[Provide 2-3 other templates that worked]

### Decision Framework

**When deciding [common decision in this domain]:**

```
IF [condition 1]:
  → Approach A (see PR #[N])
ELIF [condition 2]:
  → Approach B (see PR #[M])
ELSE:
  → Approach C (see PR #[K])
```

**Example decision frameworks:**
- When to create a design doc first
- When to split work into multiple PRs
- When to ask for more clarification

## What Went Well

- ✅ **[Success 1]**: [Description] (PR #[N])
  - Why successful: [Reason]
  - Replication: [How others can achieve this]

- ✅ **[Success 2]**: [Description] (PR #[M])
  - Why successful: [Reason]
  - Replication: [How others can achieve this]

[List 5-7 major successes]

## Challenges & Learnings

### Challenge 1: [Description]

**Context:** [Where/when this occurred]

**Impact:** [How it affected the project]

**How addressed:** [What was done]

**Lesson:** [What we learn]

**Recommendation:** [How others can avoid this]

**Evidence:** PR #[N], Issue #[M]

[Repeat for 3-5 major challenges]

### General Learnings

1. **[Learning 1]**: [Insight from this project]
   - Supporting evidence: [PRs/issues]
   - Applicability: [Who should care about this]

[List 5-7 key learnings]

## Anti-Patterns Observed

### Anti-Pattern 1: [Name]

**Description:** [What this looks like]

**Why problematic:** [Issues it causes]

**Example:** PR #[N] took [X] commits because [reason]

**Better approach:** [Alternative, with example]

[List 3-4 anti-patterns if observed]

## Metrics for Success

Based on this analysis, measure success by:

1. **[Metric 1]**: [What to measure and why]
   - Target: [Specific target based on observations]
   - How to measure: [Method]

2. **[Metric 2]**: [What to measure and why]
   - Target: [Specific target]
   - How to measure: [Method]

[Provide 4-5 measurable success criteria]
```

## Reflection

- Are your recommendations specific enough to act on?
- Have you provided templates/examples for each?
- Is everything backed by evidence from the PRs?

## Next Step

Run `llmdev generate-instructions {owner}/{repo} --phase synthesis` for Phase 8 (final phase).
"""

    def _phase_synthesis(self, owner: str, repo: str) -> str:
        """Final synthesis phase."""
        return f"""# Phase 8: Final Synthesis - {owner}/{repo}

**Time Estimate:** 15-20 minutes
**Goal:** Create executive summary and key takeaways; finalize the case study.

## Tasks

1. **Write Executive Summary (3-5 paragraphs):**
   - Paragraph 1: What is this project? (scope, purpose, tech)
   - Paragraph 2: Key statistics (PRs, timeline, velocity)
   - Paragraph 3: Main insights and findings
   - Paragraph 4: Unique aspects or notable patterns
   - Paragraph 5: Value to readers

2. **Create Key Takeaways (5-7 bullet points):**
   - Most important lessons from this case study
   - Surprising findings
   - Universal insights (applicable to any project)
   - Domain-specific insights
   - Avoid duplicating content from Best Practices - focus on big picture

3. **Write Conclusion:**
   - Summarize the development journey
   - Highlight the value of this case study
   - Point to patterns others can replicate
   - End with inspiring or thought-provoking statement

4. **Add Methodology section:**
   - When was analysis performed
   - What tools were used
   - What was the scope (how many PRs/issues analyzed)
   - What limitations or gaps exist
   - Acknowledge areas not covered

5. **Add Technical Insights (if applicable):**
   - Technology-specific observations
   - Architecture decisions and their impact
   - Performance or scalability considerations
   - Tool-specific patterns (e.g., using specific libraries/frameworks)

6. **Final review and polish:**
   - Check all PR references are correct
   - Ensure markdown formatting is correct
   - Verify tables are complete
   - Check for spelling/grammar
   - Ensure consistent voice throughout

## Output

Complete these final sections in your case study document:

### Section: Executive Summary (at the top)

```markdown
## Executive Summary

[3-5 paragraphs covering:]

- Project overview: what, why, how
- Scale and timeline of development
- Key findings and insights
- Notable patterns or approaches
- Value to readers/community
```

### Section: Key Takeaways (near end, before Conclusion)

```markdown
## Key Takeaways

1. **[Takeaway 1]**: [2-3 sentence insight]

2. **[Takeaway 2]**: [2-3 sentence insight]

3. **[Takeaway 3]**: [2-3 sentence insight]

[Continue for 5-7 total takeaways]
```

### Section: Technical Insights (if applicable)

```markdown
## Technical Insights

### [Technology/Framework] Impact

[Observations about how tech choices affected development]

**Example:** PR #[N] demonstrates [specific technical pattern]

### Architecture Decisions

**Decision 1:** [What was decided]
- Rationale: [Why]
- Impact: [How it affected development]
- Evidence: PR #[N]

[Repeat for major technical decisions]

### Performance and Scalability Observations

[If relevant to the project]
```

### Section: Conclusion

```markdown
## Conclusion

[3-4 paragraphs wrapping up the case study]

- Summarize the development journey
- Highlight key successes and learnings
- Connect to broader LLM-assisted development trends
- Inspire readers with actionable insights
```

### Section: Appendix - Methodology

```markdown
## Appendix: Methodology

**Analysis Date:** [Current date]

**Tool Used:** MCP-enabled analysis tool (GitHub Copilot with MCP GitHub server)

**Analysis Scope:**
- Issues analyzed: [N] of [Total]
- PRs analyzed: [N] of [Total]
- Commits reviewed: [Approximate number]
- Time period: [First commit] to [Last commit]

**Data Sources:**
- GitHub repository: {owner}/{repo}
- Issue descriptions and comments
- PR descriptions, comments, and reviews
- Commit messages and history
- Repository documentation

**Analysis Approach:**
- Phase-based structured analysis
- Focus on observable patterns and evidence
- Extraction of prompts and iteration patterns
- Classification of development phases
- Identification of best practices and anti-patterns

**Limitations:**
- [Limitation 1 - e.g., "Private discussions not visible"]
- [Limitation 2 - e.g., "Some early history may be incomplete"]
- [Limitation 3 - e.g., "Analysis focused on Copilot usage, may have missed other tools"]

**Acknowledgments:**
[If applicable, credit the repository authors or contributors]
```

## Final Review Checklist

Before considering the case study complete, verify:

- [ ] Executive summary is compelling and accurate
- [ ] All sections are complete (no [TODO] markers)
- [ ] All PR references are correct and verifiable
- [ ] Tables are complete with accurate data
- [ ] Code blocks and quotes use proper markdown
- [ ] Key takeaways are distinct from best practices
- [ ] Conclusion ties everything together
- [ ] Methodology explains limitations
- [ ] Document is 30-50 pages (comprehensive)
- [ ] Voice is consistent: evidence-based, actionable, balanced

## Saving the Case Study

Save your completed case study to:
`case_studies/GITHUB_{owner.upper()}_{repo.upper()}.md`

## Post-Analysis Steps

1. **Review against examples:**
   - Compare to `case_studies/GITHUB_ANICOLAO_DIKUCLIENT.md`
   - Ensure similar depth and quality

2. **Get feedback:**
   - If working on llmdev repo, create PR for review
   - Ask maintainers to review

3. **Share learnings:**
   - Consider writing a blog post summarizing key insights
   - Share on social media or dev communities

---

**🎉 Congratulations!** You've completed a comprehensive case study analysis of **{owner}/{repo}**.

This document should now provide actionable insights for developers using LLM tools, teams adopting AI-assisted development, and the broader software development community.
"""

    def generate_batch_instructions(self, repositories: list[tuple[str, str]]) -> Dict[str, Path]:
        """
        Generate instructions for multiple repositories.

        Args:
            repositories: List of (owner, repo) tuples

        Returns:
            Dictionary mapping "owner/repo" to instruction file path
        """
        results = {}
        for owner, repo in repositories:
            path = self.generate(owner, repo)
            results[f"{owner}/{repo}"] = path
        return results
