# Minimum Viable Product (MVP)

## Overview

The MVP for `llmdev` implements a **phased instruction approach** - generating structured analysis instructions that guide MCP-enabled tools (like GitHub Copilot) through comprehensive repository analysis. This approach completely avoids GitHub API rate limits while producing high-quality case studies.

**Focus**: The MVP specifically targets analyzing **GitHub Copilot-generated code** in repositories, extracting development stories, prompts, iteration patterns, and actionable insights.

## ⚠️ Historical Note: Original Approach Failed

**What was tried:** A REST API-based monolithic pipeline that directly called GitHub APIs to fetch and analyze repository data.

**Why it failed:** GitHub API rate limits (60 requests/hour unauthenticated, 5000/hour authenticated) are insufficient for analyzing real repositories. Even small repositories with 30-50 PRs would immediately hit rate limits.

**Evidence:** Attempts to analyze the diku repository (30 issues) failed immediately with rate limit errors, requiring manual analysis.

**Lesson learned:** Direct API consumption doesn't scale for comprehensive repository analysis. A different approach was needed.

## Current Approach: Phased Instruction Generation

The current MVP generates phase-by-phase instructions that work with MCP-enabled tools:

```
llmdev generate-instructions → Phase Instructions → MCP Tool Analysis → Case Study Document
```

This approach uses the MCP GitHub server, which has different rate limit characteristics and enables comprehensive analysis of repositories of any size.

## Core Objectives

1. **Instruction Generation**: Create phase-by-phase analysis instructions for MCP tools
2. **Multi-Source Analysis**: Guide analysis of commits, PRs, and issues through structured phases
3. **Pattern Extraction**: Help identify development patterns, prompts, and iteration strategies
4. **Case Study Creation**: Enable creation of comprehensive case studies through guided analysis

## Success Criteria

The MVP is considered successful when it can:

- ✅ Generate structured analysis instructions for any public GitHub repository
- ✅ Break analysis into manageable phases to avoid overwhelming context windows
- ✅ Guide MCP tools through comprehensive repository analysis
- ✅ Extract development story arcs, prompts, and iteration patterns
- ✅ Enable creation of 30-50 page case studies in 2-3 hours
- ✅ Work without hitting API rate limits (proven on repositories with 900+ commits, 180+ PRs)
- ✅ Produce consistent, high-quality output following case study format

## Phased Analysis Process

The MVP breaks analysis into 8 phases:

### Phase 1: Introduction and Setup
- Project background and goals
- Case study format overview
- Workflow guidance

### Phase 2: Repository Overview
- Basic repository statistics
- Star/fork counts, creation dates
- Language and technology stack
- Initial impressions

### Phase 3: LLM Usage Detection
- Identify Copilot mentions in commits, PRs, issues
- Look for bot accounts and automated commits
- Gather evidence of LLM-assisted development

### Phase 4: Development Story Arc
- Trace project evolution from first commit to latest
- Identify major phases and milestones
- Document how prompts drove development

### Phase 5: Prompt Analysis
- Extract actual prompts from PR descriptions and issues
- Categorize prompt types (vision, feature, fix, refine)
- Identify what makes effective prompts

### Phase 6: Iteration Pattern Analysis
- Count commits per PR as iteration indicator
- Classify: quick wins (1-2 commits) vs complex work (6+ commits)
- Understand what caused high/low iteration counts

### Phase 7: Development Pattern Identification
- Document development practices observed
- Identify successful patterns to replicate
- Note anti-patterns to avoid

### Phase 8: Synthesis and Recommendations
- Create executive summary
- Provide actionable recommendations
- Finalize case study document

## Implementation Details

### Command-Line Interface

The MVP provides a simple CLI:

```bash
# Generate instructions for a specific phase
llmdev generate-instructions owner/repo --phase intro

# Phases progress through: intro → overview → detection → story → 
#   prompts → iteration → patterns → recommendations → synthesis
```

### Instruction Generation

Each phase generates a focused instruction document containing:
- **Context**: Background on what this phase accomplishes
- **Tasks**: Specific steps to perform
- **Expected Output**: What to document and where
- **Time Estimate**: How long the phase typically takes
- **Next Steps**: How to proceed to the next phase

### Example Usage

```bash
# Start analysis
llmdev generate-instructions anicolao/dikuclient --phase intro
# Follow instructions in generated file

# Continue to next phase
llmdev generate-instructions anicolao/dikuclient --phase overview
# Follow instructions, then continue

# Repeat for each phase until synthesis (final phase)
```

## MVP Scope

### In Scope ✅
- Public GitHub repositories
- Phased instruction generation for MCP-enabled tools
- Copilot-specific analysis patterns
- Multi-source analysis (commits, PR conversations, issue discussions)
- Case study format documentation
- Development pattern extraction

### Out of Scope ❌
- Private repository direct analysis (use MCP tools with appropriate access)
- General LLM detection beyond Copilot
- Machine learning-based detection
- Direct GitHub API consumption for large-scale analysis
- Web UI
- Real-time analysis
- Automated report generation (human analyst follows instructions)

## Why This Approach Works

### Advantages Over Direct API Approach

1. **No Rate Limits**: MCP GitHub server has different access patterns
2. **Scalable**: Works on repositories with hundreds of PRs/issues
3. **High Quality**: Human analyst provides context and insight
4. **Proven**: Successfully used to create comprehensive case studies (dikuclient, DikuMUD)
5. **Time Efficient**: 2-3 hours produces 30-50 page case study

### Why Phased Instructions?

1. **Manageable Context**: Each phase fits within LLM context windows
2. **Structured Output**: Ensures comprehensive, consistent analysis
3. **Iterative Progress**: Can pause and resume at phase boundaries
4. **Quality Control**: Review each phase before proceeding
5. **Reusable Patterns**: Instructions codify best practices

## Technical Architecture

### Components

1. **Instruction Generator** (`mcp_instructions.py`)
   - Creates phase-specific instruction documents
   - Templates for each analysis phase
   - Guidance on next steps

2. **CLI** (`cli.py`)
   - Command-line interface for generating instructions
   - Phase progression management
   - Help and documentation

3. **Case Study Format**
   - Standardized template structure
   - Consistent sections across case studies
   - Actionable recommendations format

### Data Flow

```
User → llmdev generate-instructions → Instruction File → 
MCP Tool reads instructions → Analyzes GitHub repo → 
Creates case study content → User saves to case_studies/
```

### Legacy Components (Deprecated)

The following components exist but are deprecated due to API rate limit issues:
- `analyzer.py` - Direct GitHub API analysis (hits rate limits)
- `github_client.py` - REST API client (insufficient for large repos)
- `detector.py` - Copilot detection (now done via MCP tool)
- `reporter.py` - Automated report generation (manual process preferred)

These components may be useful for small repositories or specific use cases but are not recommended for primary workflow.

### Why Focus on Copilot?
1. **Clear Scope**: Starting with one specific LLM tool reduces complexity
2. **Easier Detection**: Copilot has distinctive patterns and explicit mentions
3. **GitHub Integration**: Natural fit with GitHub repositories
4. **Validation Data**: Can verify analysis against known Copilot usage
5. **Extensible**: Learnings can be applied to other LLM tools later

## Current Status and Examples

### Proven Case Studies

The phased instruction approach has successfully created:

1. **dikuclient** (63 PRs): Comprehensive 60+ page case study
2. **DikuMUD** (167 PRs): Detailed 40+ page case study  
3. **diku** (30 issues): Complete analysis

All created using the phased instruction methodology without hitting rate limits.

### Time Requirements

- **Small repository** (< 30 PRs): 1-2 hours
- **Medium repository** (50-100 PRs): 2-3 hours
- **Large repository** (100+ PRs): 3-4 hours

Each phase takes 15-30 minutes depending on repository size.

## Getting Started

To begin using the MVP:

1. **Install llmdev**
   ```bash
   git clone https://github.com/anicolao/llmdev.git
   cd llmdev
   pip install -e .
   ```

2. **Start your first analysis**
   ```bash
   llmdev generate-instructions owner/repo --phase intro
   ```

3. **Follow the instructions**
   - Open the generated instruction file
   - Use an MCP-enabled tool (like GitHub Copilot) 
   - Complete each phase sequentially

4. **Progress through phases**
   ```bash
   llmdev generate-instructions owner/repo --phase overview
   llmdev generate-instructions owner/repo --phase detection
   # ... continue through all phases
   ```

5. **Save your case study**
   - Save completed analysis to `case_studies/GITHUB_OWNER_REPO.md`
   - Follow the format from existing case studies

## Success Metrics

The MVP is successful when:

- ✅ Can generate instructions for any public repository
- ✅ Instructions are clear and actionable
- ✅ Produces high-quality case studies (30-50 pages)
- ✅ Works without API rate limit issues
- ✅ Completed in reasonable time (2-3 hours)
- ✅ Output follows consistent format
- ✅ Results are actionable and insightful

## Future Enhancements

Potential improvements to the phased instruction approach:

1. **More detailed phase instructions** with additional examples
2. **Customizable templates** for different repository types
3. **Automated metrics collection** during phase execution
4. **Integration with additional MCP tools** beyond GitHub
5. **Batch processing** for analyzing multiple repositories
6. **Enhanced output formats** (interactive HTML, visualizations)

---

*This MVP document reflects the current working approach. The original REST API-based approach described in earlier versions failed due to rate limits and has been replaced with this proven phased instruction methodology.*
