# LLM Dev

A toolkit for analyzing and understanding how Large Language Models (LLMs) like GitHub Copilot are used to build real-world systems.

## Overview

The `llmdev` project provides tools to inspect GitHub repositories and identify code written with the assistance of LLMs, particularly GitHub Copilot. By analyzing these codebases, we can:

- Understand what patterns and practices work well when using LLMs for development
- Identify common pitfalls and challenges in LLM-assisted coding
- Distill learnings from successful and unsuccessful attempts
- Build a knowledge base of best practices for LLM-augmented development

## Purpose

As LLMs become increasingly integrated into software development workflows, it's crucial to understand their impact on code quality, development velocity, and long-term maintainability. This project aims to:

1. **Analyze LLM-generated code**: Develop tools to identify and extract code written or modified by LLMs in GitHub repositories
2. **Evaluate outcomes**: Assess the quality, maintainability, and effectiveness of LLM-assisted development
3. **Extract insights**: Summarize patterns of success and failure to guide future development practices
4. **Share knowledge**: Create a repository of findings that can help developers and teams use LLMs more effectively

## Goals

- Build tools to detect LLM-generated code in repositories
- Create metrics and analysis frameworks for evaluating LLM-assisted development
- Document case studies of successful and unsuccessful LLM usage
- Develop best practices and guidelines for effective LLM-augmented development

## Installation

### From Source

```bash
# Clone the repository
git clone https://github.com/anicolao/llmdev.git
cd llmdev

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the package
pip install -e .

# Install development dependencies (optional)
pip install -e ".[dev]"
```

## Usage

llmdev provides a phased instruction approach for analyzing repositories:

### Recommended Approach: Phased Analysis with MCP Tools

**Best for:** All repository sizes, comprehensive case studies, avoiding API rate limits

Generate phase-by-phase instructions that guide MCP-enabled tools (like GitHub Copilot) through repository analysis:

```bash
# Start with the introduction phase
llmdev generate-instructions owner/repo --phase intro

# Progress through each phase sequentially:
# intro → overview → detection → story → prompts → 
# iteration → patterns → recommendations → synthesis
```

This creates focused instruction documents for each analysis phase, guiding you through:
- Repository overview and statistics
- LLM usage pattern detection
- Development story arc extraction
- Prompt and iteration analysis
- Best practices identification

**Advantages:**
- ✅ No API rate limits (uses MCP GitHub server)
- ✅ Works with repositories of any size (tested on 900+ commits, 180+ PRs)
- ✅ Proven approach (used to create all case studies)
- ✅ Takes 2-3 hours for comprehensive 30-50 page case study
- ✅ Produces professional, actionable output

**Example workflow:**
```bash
# Phase 1: Introduction and setup
llmdev generate-instructions anicolao/dikuclient --phase intro
# Follow instructions in generated file with your MCP tool

# Phase 2: Repository overview
llmdev generate-instructions anicolao/dikuclient --phase overview
# Continue following instructions

# Repeat for all phases until synthesis (final phase)
```

### Legacy Direct Analysis (Deprecated)

**⚠️ Not recommended:** The direct Python analysis approach hits API rate limits on most real repositories.

```bash
llmdev analyze owner/repo
```

This command directly calls GitHub APIs and will likely fail on repositories with more than a few dozen PRs due to rate limits. It remains available for:
- Very small repositories (<20 PRs)
- Testing and development
- Specific edge cases

**For all other use cases, use the phased instruction approach above.**

### Command Help

```bash
# General help
llmdev --help

# Command-specific help
llmdev generate-instructions --help
```

## Output

The phased instruction approach generates comprehensive case studies with:

### Standard Sections
- **Executive Summary**: Key findings at a glance
- **Repository Overview**: Basic statistics and context
- **Development Story Arc**: How the project evolved over time
- **LLM Usage Patterns**: Copilot mentions and usage evidence
- **Prompt Analysis**: Effective prompts and patterns
- **Iteration Patterns**: Quick wins vs complex work
- **Development Patterns**: Successful practices and anti-patterns
- **Best Practices**: Actionable recommendations
- **Technical Insights**: Technology-specific observations

### Example Output

See existing case studies in the `case_studies/` directory:
- `GITHUB_ANICOLAO_DIKUCLIENT.md` - 60+ page comprehensive analysis
- `GITHUB_ANICOLAO_DIKUMUD.md` - 40+ page detailed case study
- `GITHUB_ANICOLAO_DIKU.md` - Complete analysis of 30 issues

Each demonstrates the depth and quality achievable with the phased instruction approach.

## Testing

Run the test suite:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=llmdev --cov-report=html
```

## Development Status

This project is in active development. Current status:

### MVP (Complete)
Phased instruction generation for comprehensive repository analysis. See [MVP.md](MVP.md) for details.

**Key Features:**
- ✅ Phase-by-phase instruction generation
- ✅ MCP tool integration guidance
- ✅ Comprehensive case study format
- ✅ Works on repositories of any size
- ✅ No API rate limit issues

### Enhanced Analysis (MVP 2.0)

Additional analysis capabilities available but primarily for reference:
- Deep PR content analysis (prompts, problems, solutions)
- Iteration pattern detection and classification
- Prompt effectiveness analysis
- Smart PR categorization

See [MVP2.md](MVP2.md) for enhancement specifications and [VISION.md](VISION.md) for long-term goals.

## Contributing

We welcome contributions! The llmdev project focuses on understanding how LLMs are used in real software development.

**Ways to contribute:**
- Create new case studies using the phased instruction approach
- Improve instruction templates and guidance
- Enhance phase instructions with additional examples
- Share insights from your repository analyses
- Suggest improvements to the case study format

See the `.github/copilot-instructions.md` file for detailed guidance on working with this project.

## License

[LICENSE](LICENSE) CC0

## Related Resources

- [GitHub Copilot](https://github.com/features/copilot)
- [AI-Assisted Development Research](https://github.com/topics/ai-assisted-development)
