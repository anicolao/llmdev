# Quick Start Guide

Get started with `llmdev` in just a few minutes!

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Access to an MCP-enabled tool (like GitHub Copilot)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/anicolao/llmdev.git
cd llmdev
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install llmdev

```bash
pip install -e .
```

## Your First Analysis

llmdev uses a phased instruction approach to guide you through repository analysis:

### Step 1: Generate Introduction Instructions

```bash
llmdev generate-instructions owner/repo --phase intro
```

This creates an instruction file (e.g., `ANALYZE_OWNER_REPO_PHASE_INTRO.md`) with:
- Background on the llmdev project
- Overview of the analysis process
- Guidance for getting started

### Step 2: Follow the Instructions

Open the generated file and follow the instructions using your MCP-enabled tool (like GitHub Copilot). Each phase provides:
- Clear objectives
- Specific tasks to complete
- Expected outputs
- Time estimates

### Step 3: Progress Through Each Phase

```bash
# After completing intro, move to overview
llmdev generate-instructions owner/repo --phase overview

# Then detection
llmdev generate-instructions owner/repo --phase detection

# Continue through: story → prompts → iteration → patterns → 
#   recommendations → synthesis
```

### Step 4: Complete Your Case Study

After completing all phases (typically 2-3 hours), you'll have a comprehensive 30-50 page case study documenting:
- Development story arc
- Prompt patterns and effectiveness
- Iteration strategies
- Best practices and recommendations

Save your completed analysis to:
```
case_studies/GITHUB_OWNER_REPO.md
```

## Example: Analyzing a Real Repository

Let's analyze the dikuclient repository as an example:

```bash
# Phase 1: Introduction
llmdev generate-instructions anicolao/dikuclient --phase intro
# Follow instructions to understand the project and workflow

# Phase 2: Repository Overview
llmdev generate-instructions anicolao/dikuclient --phase overview
# Gather basic statistics and metadata

# Phase 3: LLM Detection
llmdev generate-instructions anicolao/dikuclient --phase detection
# Find Copilot mentions and usage patterns

# Phase 4: Story Arc
llmdev generate-instructions anicolao/dikuclient --phase story
# Extract development phases and milestones

# Phase 5: Prompts
llmdev generate-instructions anicolao/dikuclient --phase prompts
# Analyze prompt effectiveness

# Phase 6: Iteration
llmdev generate-instructions anicolao/dikuclient --phase iteration
# Study iteration patterns

# Phase 7: Patterns
llmdev generate-instructions anicolao/dikuclient --phase patterns
# Identify development patterns

# Phase 8: Recommendations
llmdev generate-instructions anicolao/dikuclient --phase recommendations
# Create best practices

# Phase 9: Synthesis
llmdev generate-instructions anicolao/dikuclient --phase synthesis
# Finalize executive summary
```

Result: A comprehensive case study saved to `case_studies/GITHUB_ANICOLAO_DIKUCLIENT.md`

## Understanding the Phases

Each phase focuses on a specific aspect of analysis:

| Phase | Duration | Focus |
|-------|----------|-------|
| **intro** | 5 min | Project background and workflow |
| **overview** | 10-15 min | Repository statistics and metadata |
| **detection** | 15-20 min | LLM usage patterns |
| **story** | 20-30 min | Development timeline and phases |
| **prompts** | 20-30 min | Prompt analysis and effectiveness |
| **iteration** | 15-20 min | Iteration patterns and complexity |
| **patterns** | 20-30 min | Development practices |
| **recommendations** | 15-20 min | Best practices synthesis |
| **synthesis** | 10-15 min | Executive summary and finalization |

**Total time:** 2-3 hours for a comprehensive case study

## Tips for Success

1. **Complete phases in order** - Each phase builds on previous work
2. **Save your progress** - Document findings as you go
3. **Use examples** - Reference existing case studies for format guidance
4. **Be thorough** - The more detail you capture, the more valuable the case study
5. **Focus on insights** - Go beyond statistics to understand "why"

## Common Questions

### Do I need a GitHub token?

No! The phased instruction approach uses MCP tools that access GitHub directly, avoiding the need for personal access tokens and rate limits.

### How long does analysis take?

- Small repositories (<50 PRs): 1-2 hours
- Medium repositories (50-100 PRs): 2-3 hours  
- Large repositories (100+ PRs): 3-4 hours

### What if I need to pause?

You can stop at any phase boundary and resume later. Just continue with the next phase when ready.

### Can I skip phases?

It's not recommended - each phase contributes important insights. However, you can focus more time on phases most relevant to your goals.

## What's Next?

- Read the full [README.md](README.md) for more details
- Check out [MVP.md](MVP.md) to understand the approach
- Review existing [case studies](case_studies/) for examples
- Review [VISION.md](VISION.md) for the project's long-term goals
- Contribute by analyzing interesting repositories and sharing findings!

## Getting Help

If you encounter issues:
1. Check existing case studies for examples
2. Review the instruction files for guidance
3. Use the `--help` flag for command options
4. Open an issue on GitHub with details about your problem

Happy analyzing! 🚀
