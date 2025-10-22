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

### Basic Usage

Analyze a GitHub repository:

```bash
llmdev analyze owner/repo
```

For example:

```bash
llmdev analyze microsoft/vscode
```

### GitHub Token Authentication

For better API rate limits and access to private repositories, provide a GitHub personal access token:

```bash
# Using environment variable (recommended)
export GITHUB_TOKEN=your_token_here
llmdev analyze owner/repo

# Or using command-line option
llmdev analyze owner/repo --token your_token_here
```

To create a GitHub token:
1. Go to https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Select scopes: `repo` (for private repos) or `public_repo` (for public repos only)
4. Copy the generated token

### Advanced Options

```bash
# Specify output directory
llmdev analyze owner/repo --output ./reports

# Limit analysis scope
llmdev analyze owner/repo --max-commits 50 --max-prs 25 --max-issues 25

# Enable verbose logging
llmdev analyze owner/repo --verbose

# Enable deep analysis (MVP2 feature)
llmdev analyze owner/repo --deep-analysis

# Disable caching
llmdev analyze owner/repo --no-cache
```

### Deep Analysis Mode (MVP2)

The `--deep-analysis` flag enables advanced analysis features:

**Features:**
- **PR Content Analysis**: Extracts prompts, problem statements, solutions, and checklists from PR descriptions
- **Iteration Patterns**: Tracks commit sequences and identifies refinement patterns (quick wins vs complex work)
- **Prompt Analysis**: Measures prompt specificity, context, constraints, and effectiveness
- **Smart Categorization**: Classifies PRs by type (vision/foundation/feature/fix/refine/docs)
- **Enhanced Reports**: Generates insights about development patterns, prompt effectiveness, and iteration statistics

**Example:**
```bash
llmdev analyze anicolao/dikuclient --deep-analysis
```

**Deep Analysis Report Sections:**
- PR Category Distribution
- Iteration Patterns (average commits per PR, pattern distribution)
- Prompt Analysis (specificity scores, characteristics)
- Most Complex PRs (with complexity indicators)
- Quick Wins (1-2 commit PRs)

### Command Help

```bash
# General help
llmdev --help

# Command-specific help
llmdev analyze --help
```

## Output

The tool generates a markdown report in the output directory with:

### Standard Analysis
- Repository overview and statistics
- Analysis scope (commits, PRs, issues analyzed)
- Copilot detection summary
- Detailed findings with links to specific commits, PRs, and issues
- Breakdown by source type and detection method

### Deep Analysis (--deep-analysis flag)
Additional sections when deep analysis is enabled:
- **PR Category Distribution**: Shows how PRs are categorized (vision, foundation, feature, fix, refine, docs)
- **Iteration Patterns**: Average commits per PR, refinement counts, and pattern distribution
- **Prompt Analysis**: Statistics on prompt characteristics (specificity, context, constraints, examples)
- **Most Complex PRs**: Top 5 complex PRs with indicators explaining complexity
- **Quick Wins**: List of PRs that merged with 1-2 commits

## Detection Methods

The MVP focuses on detecting explicit Copilot mentions and patterns:

1. **Explicit Mentions**: Searches for keywords like "copilot", "github copilot", "co-pilot" in:
   - Commit messages
   - PR titles and descriptions
   - PR comments and reviews
   - Issue titles and descriptions
   - Issue comments

2. **Bot Attribution**: Identifies commits or contributions from Copilot-related bot accounts

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

### MVP 1.0 (Complete)
Basic detection and reporting capabilities. See [MVP.md](MVP.md) for details.

### MVP 2.0 (Current)
Enhanced analysis capabilities for case study generation:
- ✅ Deep PR content analysis (prompts, problems, solutions)
- ✅ Iteration pattern detection and classification
- ✅ Prompt effectiveness analysis
- ✅ Smart PR categorization
- ✅ API response caching and rate limiting
- ✅ Enhanced report generation

See [MVP2.md](MVP2.md) for the complete feature specification and [VISION.md](VISION.md) for long-term goals.

### Key Features Added in MVP 2.0

**Analyzers Module**:
- `PRAnalyzer`: Extracts structured content from PR descriptions
- `IterationAnalyzer`: Classifies development patterns (quick wins, normal, complex)
- `PromptAnalyzer`: Measures prompt quality and effectiveness

**Caching Infrastructure**:
- `DiskCache`: TTL-based caching for API responses
- `RateLimiter`: Intelligent rate limit management with exponential backoff

**Usage Example**:
```bash
# Basic analysis (MVP 1.0)
llmdev analyze owner/repo

# Deep analysis with caching (MVP 2.0)
llmdev analyze owner/repo --deep-analysis
```

## Contributing

We welcome contributions! As we develop the tools and methodologies, we'll be looking for:

- Ideas for detection and analysis approaches
- Case studies from real projects
- Feedback on the tools and frameworks we develop

## License

[LICENSE](LICENSE) CC0

## Related Resources

- [GitHub Copilot](https://github.com/features/copilot)
- [AI-Assisted Development Research](https://github.com/topics/ai-assisted-development)
