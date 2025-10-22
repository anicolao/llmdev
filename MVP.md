# Minimum Viable Product (MVP)

## Overview

The MVP for `llmdev` implements a **monolithic pipeline approach** - a single, unified pipeline that handles the complete workflow from repository ingestion through analysis and reporting. This approach prioritizes getting a working end-to-end system running quickly, allowing us to validate our assumptions and gather real insights before potentially modularizing later.

**Focus**: The MVP specifically targets **GitHub Copilot-generated code** detection, analyzing commits, pull requests, and issues to identify Copilot usage patterns.

## Monolithic Pipeline Architecture

The MVP pipeline will be a single, linear workflow:

```
GitHub Repository → GitHub API Data Collection → Analyze Commits/PRs/Issues → Detect Copilot Code → Generate Report
```

All components will be implemented in a single codebase with a unified command-line interface, making it easy to run, debug, and iterate on.

## Core Objectives

1. **Repository Ingestion**: Use GitHub API to access repository metadata, commits, PRs, and issues
2. **Multi-Source Analysis**: Parse git history, PR conversations, and issue discussions
3. **Copilot Detection**: Identify code likely written with GitHub Copilot assistance using heuristics
4. **Basic Reporting**: Generate a simple report of findings across all analyzed sources

## Success Criteria

The MVP is considered successful when it can:

- ✅ Access a public GitHub repository via the GitHub API
- ✅ Parse git commit history, PR conversations, and issue discussions
- ✅ Identify at least one type of Copilot-generated code pattern
- ✅ Detect Copilot mentions in PRs and issues
- ✅ Generate a basic markdown report with findings from all sources
- ✅ Run end-to-end on at least 3 real-world repositories
- ✅ Complete analysis of a small repository (< 100 commits, 50 PRs/issues) in under 5 minutes

## Initial Development Tasks

### Phase 1: Project Setup (Week 1)

#### Task 1.1: Repository Structure
- [ ] Create basic Python project structure
- [ ] Set up `pyproject.toml` or `setup.py` for dependencies
- [ ] Create `.gitignore` for Python projects
- [ ] Set up virtual environment

**Dependencies to include:**
- PyGithub or ghapi (for GitHub API access)
- GitPython (for repository operations)
- Click or argparse (for CLI)
- pytest (for testing)
- requests (for API calls)

#### Task 1.2: CLI Framework
- [ ] Create main entry point (`llmdev.py` or `main.py`)
- [ ] Implement basic command structure: `llmdev analyze <owner/repo>`
- [ ] Add `--help` documentation
- [ ] Add verbose logging option
- [ ] Add GitHub token authentication support

#### Task 1.3: Configuration
- [ ] Create configuration system for pipeline settings
- [ ] Define output directory structure
- [ ] Set up logging configuration
- [ ] Configure GitHub API rate limiting handling

**Deliverable:** A runnable CLI that accepts a repository identifier and prints "Analysis started"

---

### Phase 2: GitHub API Integration (Week 1-2)

#### Task 2.1: GitHub API Setup
- [ ] Implement GitHub API client initialization
- [ ] Handle authentication (tokens, rate limiting)
- [ ] Create error handling for API failures
- [ ] Add retry logic for transient failures

#### Task 2.2: Repository Data Collection
- [ ] Fetch repository metadata via API
- [ ] Retrieve commit history (limited to recent or paginated)
- [ ] Clone repository for code analysis (optional, as needed)
- [ ] Handle private vs public repository access

#### Task 2.3: Pull Request Data Collection
- [ ] Fetch all PRs (or recent N PRs) from repository
- [ ] Extract PR metadata (title, description, author, dates)
- [ ] Retrieve PR comments and review comments
- [ ] Parse PR conversation threads

#### Task 2.4: Issue Data Collection
- [ ] Fetch all issues (or recent N issues) from repository
- [ ] Extract issue metadata (title, description, author, dates)
- [ ] Retrieve issue comments
- [ ] Parse issue conversation threads

**Deliverable:** Successfully fetch and store commits, PRs, and issues from 3 different repositories

---

### Phase 3: Multi-Source Analysis (Week 2-3)

#### Task 3.1: Commit Analysis
- [ ] Parse commit history from API or git
- [ ] Extract commit metadata (hash, author, date, message)
- [ ] Parse commit diffs for code changes
- [ ] Handle merge commits appropriately

#### Task 3.2: PR Conversation Analysis
- [ ] Parse PR descriptions for Copilot mentions
- [ ] Analyze PR comments for Copilot references
- [ ] Extract code snippets from PR discussions
- [ ] Track PR review comments

#### Task 3.3: Issue Discussion Analysis
- [ ] Parse issue descriptions for Copilot mentions
- [ ] Analyze issue comments for Copilot references
- [ ] Identify code snippets in issues
- [ ] Track issue resolution patterns

#### Task 3.4: Data Aggregation
- [ ] Create unified data structure for all sources
- [ ] Link PRs to commits
- [ ] Cross-reference issues with PRs/commits
- [ ] Prepare aggregated data for detection phase

**Deliverable:** Parse and aggregate data from commits, PRs, and issues for a repository

---

### Phase 4: Copilot Detection (Week 3-4)

#### Task 4.1: Explicit Copilot Mentions
Implement detection for direct Copilot references:

- [ ] **Commit Message Detection**: Look for keywords like "copilot", "github copilot", "co-pilot"
- [ ] **PR/Issue Detection**: Search descriptions and comments for Copilot mentions
- [ ] **Author Attribution**: Identify commits/PRs authored by copilot bots or with Copilot tags

#### Task 4.2: Copilot Code Pattern Analysis
- [ ] Detect common Copilot code signatures in commits:
  - Characteristic comment styles (e.g., detailed inline explanations)
  - Common placeholder patterns
  - Typical function/variable naming conventions
- [ ] Analyze code changes in PRs for Copilot patterns
- [ ] Calculate confidence scores (0-1) for each detection

#### Task 4.3: Conversation Pattern Analysis
- [ ] Identify discussions about Copilot usage in PRs
- [ ] Track issue reports related to Copilot-generated code
- [ ] Analyze feedback patterns on Copilot contributions
- [ ] Correlate code patterns with conversation mentions

#### Task 4.4: Author and Contributor Analysis
- [ ] Track commits per author with Copilot indicators
- [ ] Identify authors who explicitly mention using Copilot
- [ ] Correlate detection patterns with specific contributors
- [ ] Build author profiles for Copilot usage

**Deliverable:** Run detection on 3 repositories and identify Copilot usage across commits, PRs, and issues

---

### Phase 5: Report Generation (Week 4)

#### Task 5.1: Basic Statistics
Generate a markdown report including:
- [ ] Repository overview (name, commits/PRs/issues analyzed, date range)
- [ ] Total Copilot-detected instances across all sources (count and percentage)
- [ ] Breakdown by detection source (commits, PRs, issues)
- [ ] Breakdown by detection heuristic
- [ ] Top files with Copilot-detected changes

#### Task 5.2: Detailed Findings
- [ ] List top 10 Copilot-detected commits with evidence
- [ ] Highlight significant PRs mentioning Copilot
- [ ] Show issues discussing Copilot-generated code
- [ ] Show code snippets for high-confidence detections
- [ ] Include links to commits, PRs, and issues on GitHub

#### Task 5.3: Cross-Source Analysis
- [ ] Correlate Copilot usage across commits and PRs
- [ ] Identify patterns in issue reports about Copilot code
- [ ] Show timeline of Copilot adoption in the repository
- [ ] Create simple ASCII/text charts showing:
  - Timeline of Copilot usage across sources
  - Distribution by source type (commits, PRs, issues)
  - Author distribution

**Deliverable:** Generate complete HTML/Markdown report with multi-source analysis for test repositories

---

### Phase 6: Testing & Validation (Week 4-5)

#### Task 6.1: Unit Tests
- [ ] Test GitHub API client with various inputs
- [ ] Test commit parsing edge cases
- [ ] Test PR and issue data extraction
- [ ] Test Copilot detection heuristics with known examples
- [ ] Test report generation

#### Task 6.2: Integration Tests
- [ ] Run end-to-end on 5 diverse repositories
- [ ] Validate output quality manually
- [ ] Test error handling (API failures, rate limits, missing data)
- [ ] Performance testing (time and memory)
- [ ] Test with repositories of varying sizes

#### Task 6.3: Documentation
- [ ] Update README with installation instructions
- [ ] Add usage examples with GitHub token setup
- [ ] Document Copilot detection heuristics and rationale
- [ ] Document GitHub API usage and rate limits
- [ ] Create troubleshooting guide

**Deliverable:** 80%+ test coverage, successful analysis of 5 repositories with multi-source data

---

## MVP Scope Boundaries

### In Scope ✅
- Public GitHub repositories only
- GitHub API for accessing commits, PRs, and issues
- Copilot-specific detection using heuristics
- Multi-source analysis (commits, PR conversations, issue discussions)
- Command-line interface
- Single-machine execution
- Markdown/HTML reports

### Out of Scope ❌
- Private repository support without tokens
- General LLM detection (focus is Copilot-specific)
- Machine learning-based detection (too complex for MVP)
- Database storage (use file-based storage)
- Web UI (CLI only)
- Real-time analysis
- Multi-repository comparison
- Deep code analysis beyond pattern matching

## Technical Decisions

### Why Monolithic?
1. **Faster Development**: Single codebase is easier to set up and modify
2. **Simpler Debugging**: All code runs in one process
3. **Easier Testing**: No need for inter-service testing
4. **Rapid Iteration**: Changes don't require coordinating multiple components
5. **Validation First**: Proves the concept before architectural complexity
6. **Unified API Access**: Single GitHub API client handles all data sources

### Why Focus on Copilot?
1. **Clear Scope**: Starting with one specific LLM tool reduces complexity
2. **Easier Detection**: Copilot has distinctive patterns and explicit mentions
3. **GitHub Integration**: Natural fit with GitHub API and repository data
4. **Validation Data**: Can verify detection against known Copilot usage
5. **Extensible**: Learnings can be applied to other LLM tools later

### Future Migration Path
Once MVP is validated, we can:
- Extract detection logic into pluggable modules
- Add support for other LLM tools (ChatGPT, Claude, etc.)
- Separate storage layer for larger datasets
- Add API layer for programmatic access
- Introduce parallel processing for large repositories
- Enhance with machine learning-based detection

## Development Timeline

**Total Duration**: 5 weeks

| Week | Phase | Key Deliverable |
|------|-------|----------------|
| 1 | Setup + GitHub API | Working CLI with API access |
| 2 | API Integration + Analysis | Fetch commits, PRs, and issues |
| 3 | Multi-Source Analysis + Detection | Parse and analyze all sources |
| 4 | Detection + Reporting | Generate multi-source reports |
| 5 | Testing + Documentation | Production-ready MVP |

## Getting Started

To begin MVP development:

1. **Fork/Clone** this repository
2. **Create feature branch**: `git checkout -b feature/mvp-pipeline`
3. **Start with Phase 1, Task 1.1**: Set up project structure
4. **Work sequentially** through tasks, checking off completed items
5. **Test continuously** as you build
6. **Update this document** with learnings and adjustments

## Success Metrics

By the end of MVP development, we should have:

- ✅ Working CLI tool that can be installed via pip
- ✅ GitHub API integration for commits, PRs, and issues
- ✅ Analysis of at least 5 real-world repositories
- ✅ Reports identifying Copilot usage patterns across multiple sources
- ✅ Documentation for users to run the tool themselves (including GitHub token setup)
- ✅ Test suite with 80%+ coverage
- ✅ Clear insights on what works and what needs improvement

## Next Steps After MVP

Once the MVP is complete and validated:

1. Gather feedback from initial users
2. Evaluate accuracy of detection heuristics
3. Identify bottlenecks and performance issues
4. Decide on modularization strategy
5. Plan for Phase 2 (as per VISION.md)

---

*This MVP document is a living document. Update it as you learn and adjust the plan based on what you discover during development.*
