# Quick Start Guide

Get started with `llmdev` in just a few minutes!

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- A GitHub account (for API token)

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

## Get a GitHub Token

To avoid rate limits and access repositories effectively, you'll need a GitHub Personal Access Token:

1. Go to https://github.com/settings/tokens
2. Click **"Generate new token (classic)"**
3. Give it a descriptive name (e.g., "llmdev analysis")
4. Select scopes:
   - For **public repositories only**: Select `public_repo`
   - For **private repositories**: Select `repo`
5. Click **"Generate token"**
6. **Copy the token immediately** (you won't see it again!)

## Choose Your Analysis Approach

llmdev offers two ways to analyze repositories:

### Option 1: MCP Instructions (Recommended for Comprehensive Analysis)

**Best for:** Creating detailed case studies, large repositories (100+ PRs), avoiding API rate limits

Generate analysis instructions that guide you through comprehensive repository analysis:

```bash
llmdev generate-instructions owner/repo
```

This creates a structured instruction document that you can follow using MCP-enabled tools (like GitHub Copilot). No API token needed! Takes 2-3 hours but produces a comprehensive 30-50 page case study.

**Example:**
```bash
llmdev generate-instructions anicolao/dikuclient --output ./instructions
# Opens: instructions/ANALYZE_ANICOLAO_DIKUCLIENT.md
# Follow the 8-phase analysis process with your MCP-enabled tool
```

### Option 2: Direct Python Analysis (Legacy)

**Best for:** Quick statistics, small repositories (<50 PRs)

#### Set Your GitHub Token

```bash
export GITHUB_TOKEN=your_token_here
```

Or on Windows (PowerShell):
```powershell
$env:GITHUB_TOKEN="your_token_here"
```

#### Analyze a Repository

Start with a small repository to test:

```bash
llmdev analyze anicolao/llmdev --max-commits 20 --max-prs 10 --max-issues 10
```

This will:
- Fetch up to 20 commits, 10 PRs, and 10 issues
- Detect Copilot usage patterns
- Generate a markdown report in the `output/` directory

**Note:** This approach may hit API rate limits on larger repositories. For comprehensive analysis, use the MCP instructions approach instead.

### View the Report

```bash
# Find the generated report
ls -lt output/

# View it with your favorite markdown viewer or text editor
cat output/llmdev_analysis_*.md
```

## Example Repositories to Analyze

Try analyzing these repositories (start with smaller limits):

```bash
# A small project
llmdev analyze microsoft/calculator --max-commits 50

# A medium project (be patient, this takes a few minutes)
llmdev analyze facebook/react --max-commits 100 --max-prs 50

# Use verbose mode to see what's happening
llmdev analyze your-org/your-repo --verbose
```

## Common Options

```bash
# Specify output directory
llmdev analyze owner/repo --output ./my-reports

# Adjust analysis scope
llmdev analyze owner/repo --max-commits 200 --max-prs 100 --max-issues 50

# Get help
llmdev --help
llmdev analyze --help
```

## Troubleshooting

### "403 Forbidden" Error
- Make sure your GitHub token is set correctly
- Check that your token has the right permissions
- Verify you're not hitting rate limits (wait a few minutes and try again)

### "No module named 'llmdev'" Error
- Make sure you've activated your virtual environment
- Run `pip install -e .` again

### Analysis is Very Slow
- Reduce the number of items to analyze with `--max-commits`, `--max-prs`, `--max-issues`
- Large repositories with many PRs/issues can take several minutes
- Use `--verbose` to see progress

## What's Next?

- Read the full [README.md](README.md) for more details
- Check out [MVP.md](MVP.md) to see the development roadmap
- Review [VISION.md](VISION.md) for the project's long-term goals
- Contribute by analyzing interesting repositories and sharing findings!

## Running Tests

To verify your installation:

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run with coverage
pytest --cov=llmdev
```

## Getting Help

If you encounter issues:
1. Check this guide's troubleshooting section
2. Look at the example commands above
3. Use the `--help` flag for command options
4. Open an issue on GitHub with details about your problem

Happy analyzing! 🚀
