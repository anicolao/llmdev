# Copilot Instructions for llmdev Project

## Project Mission

The llmdev project systematically studies how LLMs are used to build real software systems, distilling actionable insights for the development community. Our work focuses on **evidence-based analysis** of real-world repositories to understand patterns of success and failure in LLM-assisted development.

## Core Work Categories

Every task in this project falls into one of four categories. **Always identify which category applies before beginning work:**

### (A) Creating New Case Studies

**Objective:** Analyze repositories to extract development stories, prompts, iteration patterns, and actionable learnings

**When This Applies:**
- Analyzing a new repository (e.g., "analyze anicolao/somerepo")
- Creating case study documentation
- Extracting patterns from PR history

**Process:**
1. **Identify the Story Arc**
   - Find the original vision/objective (usually Issue #1 or early PRs)
   - Trace development phases from inception to current state
   - Document major milestones and pivots

2. **Extract and Analyze Prompts**
   - Locate prompts in PR descriptions, issue comments, commit messages
   - Categorize by type (vision, feature request, bug fix, refinement)
   - Identify what made effective prompts work
   - Note patterns in prompt structure (Problem-Context-Solution, etc.)

3. **Analyze Iteration Patterns**
   - Count commits per PR as iteration indicator
   - Identify fast wins (1-2 commits, same day) vs complex work (6+ commits)
   - Extract WHY certain features took more/fewer iterations
   - Document feedback loops and correction patterns

4. **Document Development Patterns**
   - Design-first approaches
   - Checkpoint/consolidation PRs
   - WIP transparency practices
   - Branch naming conventions
   - Testing patterns

5. **Structure the Case Study**
   ```markdown
   # Case Study: [owner/repo]
   ## Executive Summary
   ## Development Story Arc
      - Phase 1: Vision & Planning
      - Phase 2: Foundation
      - Phase 3: Core Features
      - Phase 4: Polish & Refinement
      - [Additional phases as needed]
   ## Prompt Analysis
   ## Iteration Deep Dive
   ## Development Patterns
   ## What Went Well
   ## Challenges & Learning
   ## Best Practices
   ## Key Takeaways
   ## Technical Insights
   ## Conclusion
   ## Appendix: Methodology
   ```

6. **Make It Actionable**
   - Include specific PR examples (PR #N with context)
   - Provide templates and formulas others can use
   - Show anti-patterns to avoid
   - Include metrics for measuring success

**Quality Checklist:**
- [ ] Complete story arc from first commit to latest
- [ ] All major PRs analyzed for patterns
- [ ] Prompts extracted and evaluated
- [ ] Iteration counts explained with reasoning
- [ ] Specific, replicable recommendations provided
- [ ] Evidence-based claims (every assertion backed by PR reference)
- [ ] Actionable templates and patterns included

**Learnings from dikuclient Case Study:**
- Don't just count detections—tell the development story
- Extract the actual prompts from PR descriptions
- Explain WHY things took many vs few iterations
- Focus on what others can replicate
- Include specific PR numbers as evidence
- Create prompt templates that worked
- Document anti-patterns observed
- Provide metrics for measuring success

### (B) Improving the Tooling

**Objective:** Enhance llmdev analysis tools to make case study creation more efficient and insightful

**When This Applies:**
- Adding new detection methods
- Improving report generation
- Enhancing data collection
- Fixing bugs in analysis tools

**Process:**
1. **Review Current Limitations**
   - Check MVP2.md for documented enhancement needs
   - Identify pain points from recent case study work
   - Consider rate limits, API efficiency, data extraction gaps

2. **Design the Enhancement**
   - Write clear specification of what to add/change
   - Consider impact on existing case studies
   - Plan for backward compatibility

3. **Implement Incrementally**
   - Make small, focused changes
   - Test with real repository data
   - Validate against existing case studies
   - Ensure tests pass

4. **Document the Change**
   - Update relevant .md files (MVP.md, MVP2.md, README.md)
   - Add examples of new capabilities
   - Update command-line help if applicable

**Priority Areas (from MVP2.md):**
1. Deep PR content analysis (extract prompts, problems, solutions)
2. Iteration pattern detection (commit sequences, refinement tracking)
3. Prompt repository and effectiveness scoring
4. Timeline and progression visualization
5. Smart categorization (vision/foundation/feature/fix/refine/docs)
6. Caching and rate limit management
7. Enhanced report generation with story arcs

**Quality Checklist:**
- [ ] Tests pass (run `pytest`)
- [ ] Backward compatible or migration path provided
- [ ] Documentation updated
- [ ] Performance acceptable
- [ ] Works with both small and large repositories

### (C) Summarizing Content

**Objective:** Distill large amounts of case study content into digestible, actionable formats

**When This Applies:**
- Creating overview documents
- Generating best practices guides
- Extracting common patterns across multiple case studies
- Creating quick reference materials

**Process:**
1. **Identify the Audience**
   - Developers using LLM tools?
   - Organizations adopting AI?
   - Researchers studying patterns?
   - Tool creators improving products?

2. **Extract Key Patterns**
   - What patterns appear across multiple case studies?
   - What practices consistently lead to success?
   - What anti-patterns are commonly observed?
   - What metrics matter most?

3. **Organize by Actionability**
   - Start with "Quick Wins" (easy to apply)
   - Progress to "Advanced Techniques"
   - Include decision frameworks
   - Provide templates and checklists

4. **Create Different Formats**
   - Quick reference (1-2 pages)
   - Detailed guide (10-20 pages)
   - Presentation slides
   - Interactive examples

**Output Examples:**
- "Top 10 Patterns for LLM-Assisted Development"
- "Prompt Templates That Work"
- "Anti-Patterns to Avoid"
- "Measuring Success: Key Metrics"
- "Quick Start Guide for AI-Assisted Coding"

**Quality Checklist:**
- [ ] Evidence-based (references specific case studies)
- [ ] Actionable (readers know what to do next)
- [ ] Concise (respects reader's time)
- [ ] Well-organized (easy to scan and find information)
- [ ] Credible (includes success metrics and examples)

### (D) Publishing Content

**Objective:** Make learnings accessible through GitHub Pages or other public channels

**When This Applies:**
- Setting up GitHub Pages site
- Creating navigation structure
- Formatting for web consumption
- Adding search and discovery features

**Process:**
1. **Plan the Site Structure**
   ```
   / (Home)
   /case-studies/
   /best-practices/
   /guides/
   /about/
   ```

2. **Convert Content to Web Format**
   - Ensure markdown renders properly
   - Add navigation elements
   - Create index pages
   - Add metadata (dates, tags, categories)

3. **Enhance Discoverability**
   - Add search functionality
   - Create category pages
   - Include related content links
   - Add RSS feed for updates

4. **Optimize for Reading**
   - Add table of contents
   - Use appropriate heading levels
   - Include code syntax highlighting
   - Ensure mobile-friendly

**GitHub Pages Setup:**
- Use Jekyll for static site generation
- Create `_config.yml` for site configuration
- Organize content in appropriate directories
- Add navigation in `_includes/`
- Style with `_layouts/` and CSS

**Quality Checklist:**
- [ ] All links work (no 404s)
- [ ] Mobile-responsive design
- [ ] Fast load times
- [ ] Accessible (WCAG guidelines)
- [ ] SEO-friendly (titles, descriptions, headers)
- [ ] Easy navigation
- [ ] Search functionality works

## General Guidelines for All Work

### Before Starting Any Task

1. **Categorize the Work**
   - Is this (A) case study, (B) tooling, (C) summarization, or (D) publishing?
   - Review the relevant section above for that category

2. **Understand the Context**
   - Read VISION.md for project goals
   - Review MVP.md and MVP2.md for current state
   - Check existing case studies for patterns
   - Look at recent commits to understand trajectory

3. **Plan the Approach**
   - Break work into small, verifiable steps
   - Identify what success looks like
   - Consider what could go wrong
   - Plan for testing and validation

### During the Work

1. **Make Small, Incremental Changes**
   - Commit frequently with clear messages
   - Test after each significant change
   - Use `report_progress` to push and update PR
   - Review what was committed (use `git diff`)

2. **Stay Evidence-Based**
   - Every claim needs a specific example
   - Reference actual PRs, commits, or files
   - Avoid speculation—stick to observable data
   - When uncertain, note limitations

3. **Be Actionable**
   - Readers should know what to do next
   - Provide templates, checklists, formulas
   - Include both "what" and "why"
   - Show examples of applying the advice

### After Completing the Task

1. **Validate Quality**
   - Run tests (`pytest`)
   - Check markdown rendering
   - Verify all links work
   - Ensure consistent formatting

2. **Document and Reflect**
   - Update relevant .md files
   - Note any challenges encountered
   - Suggest improvements for next time
   - Update these instructions if new patterns emerge

3. **Provide Recommendations**
   - What could make this task easier next time?
   - What tooling enhancements would help?
   - What patterns should be reused?
   - What anti-patterns should be avoided?

## Effective Practices from dikuclient Case Study

### What Worked Well

1. **Complete Story Arc**
   - Traced development from Issue #1 through PR #63
   - Showed how prompts evolved over time
   - Documented all 6 development phases
   - Made the journey clear and followable

2. **Specific PR References**
   - "PR #3 took 15+ commits because..." (with reasoning)
   - "PR #45 took 1 commit because..." (contrast)
   - Every pattern backed by specific examples
   - Readers can verify claims

3. **Actionable Templates**
   - Problem-Context-Solution prompt template
   - Checklist patterns for complex work
   - [WIP] usage guidelines
   - Metrics for measuring success

4. **Honest Analysis**
   - Included challenges, not just successes
   - Documented anti-patterns
   - Showed what didn't work well
   - Built credibility through balance

### What to Replicate

1. **Extract Actual Prompts**
   - Look in PR descriptions, issue comments
   - Show what the human asked for
   - Analyze why certain prompts worked
   - Create reusable templates

2. **Explain Iteration Counts**
   - 1-2 commits = quick win (why?)
   - 3-5 commits = normal complexity (why?)
   - 6+ commits = struggled (what caused it?)
   - Teach pattern recognition

3. **Provide Evidence Tables**
   - Velocity breakdown by phase
   - Success metrics with numbers
   - Pattern frequency analysis
   - Before/after comparisons

4. **Create Reusable Artifacts**
   - Prompt templates
   - Checklist patterns
   - Decision frameworks
   - Metric definitions

## Handling Common Scenarios

### Rate Limits Hit

1. Use reduced scope (analyze fewer PRs initially)
2. Implement caching (see MVP2.md recommendations)
3. Focus on quality over quantity
4. Resume work after rate limit resets

### Unclear Requirements

1. Ask clarifying questions in comment reply
2. Propose 2-3 interpretation options
3. Show examples of what each would look like
4. Wait for confirmation before proceeding

### Large Scope Task

1. Break into phases (report in PR description)
2. Commit after each phase with `report_progress`
3. Get feedback early and often
4. Be willing to adjust based on feedback

### Disagreement with Feedback

1. Understand the concern fully
2. Consider the user's perspective
3. Propose alternative approaches
4. Remember: human has final decision

## Documentation Standards

### Markdown Formatting

- Use `#` for title, `##` for major sections, `###` for subsections
- Include code blocks with language specification: ```python
- Use `**bold**` for emphasis, `*italics*` sparingly
- Create tables for structured data
- Add horizontal rules `---` between major sections

### Evidence Standards

- Always cite specific PRs: "PR #42"
- Include dates for timeline context
- Show before/after for changes
- Link to actual commits/PRs when possible
- Quote actual prompts, commit messages, PR text

### Writing Style

- **Active voice**: "Copilot generated..." not "was generated by..."
- **Specific**: "3.5 PRs/day" not "very fast"
- **Clear**: Short sentences, avoid jargon
- **Actionable**: "Do X by..." not "X is important"
- **Honest**: Include limitations and challenges

## Version Control

- Create feature branches for work
- Use descriptive commit messages
- Commit frequently (every meaningful unit)
- Use `report_progress` to push and update PR
- Review what was committed before finalizing

## Testing Requirements

- Run `pytest` before committing
- Validate markdown renders correctly
- Check all internal links work
- Ensure code examples are correct
- Test with real repository data when possible

## Continuous Improvement

These instructions will evolve based on:
- Patterns discovered in new case studies
- Feedback from PR reviews
- Tool enhancements that change workflows
- New best practices that emerge

**After each major task, consider:**
- What would make this easier next time?
- Should these instructions be updated?
- What new patterns emerged?
- What should be added to MVP2.md?

---

*These instructions guide Copilot work on the llmdev project. They will be updated as we learn and the project evolves.*

*Last updated: October 2025 (after dikuclient case study)*
