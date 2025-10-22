# Minimum Viable Product (MVP)

## Overview

The MVP for `llmdev` implements a **monolithic pipeline approach** - a single, unified pipeline that handles the complete workflow from repository ingestion through analysis and reporting. This approach prioritizes getting a working end-to-end system running quickly, allowing us to validate our assumptions and gather real insights before potentially modularizing later.

## Monolithic Pipeline Architecture

The MVP pipeline will be a single, linear workflow:

```
GitHub Repository → Clone → Analyze Commits → Detect LLM Code → Generate Report
```

All components will be implemented in a single codebase with a unified command-line interface, making it easy to run, debug, and iterate on.

## Core Objectives

1. **Repository Ingestion**: Clone and prepare a GitHub repository for analysis
2. **Commit Analysis**: Parse git history to identify commits and changes
3. **LLM Detection**: Identify code likely written with LLM assistance using heuristics
4. **Basic Reporting**: Generate a simple report of findings

## Success Criteria

The MVP is considered successful when it can:

- ✅ Clone a public GitHub repository
- ✅ Parse the git commit history
- ✅ Identify at least one type of LLM-generated code pattern
- ✅ Generate a basic markdown report with findings
- ✅ Run end-to-end on at least 3 real-world repositories
- ✅ Complete analysis of a small repository (< 100 commits) in under 5 minutes

## Initial Development Tasks

### Phase 1: Project Setup (Week 1)

#### Task 1.1: Repository Structure
- [ ] Create basic Python project structure
- [ ] Set up `pyproject.toml` or `setup.py` for dependencies
- [ ] Create `.gitignore` for Python projects
- [ ] Set up virtual environment

**Dependencies to include:**
- GitPython (for repository operations)
- Click or argparse (for CLI)
- pytest (for testing)

#### Task 1.2: CLI Framework
- [ ] Create main entry point (`llmdev.py` or `main.py`)
- [ ] Implement basic command structure: `llmdev analyze <repo-url>`
- [ ] Add `--help` documentation
- [ ] Add verbose logging option

#### Task 1.3: Configuration
- [ ] Create configuration system for pipeline settings
- [ ] Define output directory structure
- [ ] Set up logging configuration

**Deliverable:** A runnable CLI that accepts a repository URL and prints "Analysis started"

---

### Phase 2: Repository Ingestion (Week 1-2)

#### Task 2.1: Repository Cloning
- [ ] Implement safe repository cloning
- [ ] Handle authentication (public repos first, tokens later)
- [ ] Create temporary workspace management
- [ ] Add cleanup on exit/error

#### Task 2.2: Repository Validation
- [ ] Verify repository is valid git repository
- [ ] Check repository size limits (start with < 1GB)
- [ ] Validate repository has accessible history
- [ ] Handle edge cases (empty repos, no commits)

#### Task 2.3: Metadata Extraction
- [ ] Extract repository basic info (name, URL, default branch)
- [ ] Count total commits
- [ ] Identify primary programming languages
- [ ] Record analysis start time/date

**Deliverable:** Successfully clone and validate 3 different repositories

---

### Phase 3: Commit Analysis (Week 2-3)

#### Task 3.1: Commit History Parsing
- [ ] Iterate through all commits in repository
- [ ] Extract commit metadata (hash, author, date, message)
- [ ] Parse commit diffs
- [ ] Handle merge commits appropriately

#### Task 3.2: Change Detection
- [ ] Identify files added, modified, deleted in each commit
- [ ] Extract line-level changes (additions/deletions)
- [ ] Track file types and extensions
- [ ] Calculate commit size metrics

#### Task 3.3: Pattern Storage
- [ ] Create in-memory data structure for commit data
- [ ] Design simple schema for analysis results
- [ ] Prepare for detection phase

**Deliverable:** Parse full history of a repository and print commit statistics

---

### Phase 4: LLM Detection (Week 3-4)

#### Task 4.1: Initial Heuristics
Implement basic detection heuristics (start with 2-3):

- [ ] **Commit Message Detection**: Look for keywords like "copilot", "chatgpt", "AI generated", "AI assisted"
- [ ] **Large Boilerplate Commits**: Detect commits with > 100 lines added with high repetition patterns
- [ ] **Rapid Commits**: Identify unusually fast commit sequences (multiple commits within minutes)

#### Task 4.2: Code Pattern Analysis
- [ ] Detect common LLM code signatures:
  - Excessive comments explaining obvious code
  - Generic variable names (e.g., `result`, `data`, `temp`)
  - Placeholder comments (e.g., "TODO: implement this")
- [ ] Calculate confidence scores (0-1) for each detection

#### Task 4.3: Author Analysis
- [ ] Track commits per author
- [ ] Identify authors with high LLM-likelihood scores
- [ ] Correlate detection patterns with authors

**Deliverable:** Run detection on 3 repositories and identify at least 5 likely LLM-assisted commits

---

### Phase 5: Report Generation (Week 4)

#### Task 5.1: Basic Statistics
Generate a markdown report including:
- [ ] Repository overview (name, commits analyzed, date range)
- [ ] Total LLM-detected commits (count and percentage)
- [ ] Breakdown by detection heuristic
- [ ] Top files with LLM-detected changes

#### Task 5.2: Detailed Findings
- [ ] List top 10 LLM-detected commits with evidence
- [ ] Show code snippets for high-confidence detections
- [ ] Include commit links to GitHub

#### Task 5.3: Visualization
- [ ] Create simple ASCII/text charts showing:
  - Timeline of LLM usage
  - Distribution by file type
  - Author distribution

**Deliverable:** Generate complete HTML/Markdown report for test repositories

---

### Phase 6: Testing & Validation (Week 4-5)

#### Task 6.1: Unit Tests
- [ ] Test repository cloning with various inputs
- [ ] Test commit parsing edge cases
- [ ] Test detection heuristics with known examples
- [ ] Test report generation

#### Task 6.2: Integration Tests
- [ ] Run end-to-end on 5 diverse repositories
- [ ] Validate output quality manually
- [ ] Test error handling and edge cases
- [ ] Performance testing (time and memory)

#### Task 6.3: Documentation
- [ ] Update README with installation instructions
- [ ] Add usage examples
- [ ] Document detection heuristics and rationale
- [ ] Create troubleshooting guide

**Deliverable:** 80%+ test coverage, successful analysis of 5 repositories

---

## MVP Scope Boundaries

### In Scope ✅
- Public GitHub repositories only
- Basic LLM detection using heuristics
- Command-line interface
- Single-machine execution
- Markdown/HTML reports

### Out of Scope ❌
- Private repository support (requires authentication)
- Machine learning-based detection (too complex for MVP)
- Database storage (use file-based storage)
- Web UI (CLI only)
- Real-time analysis
- Multi-repository comparison
- GitHub API integration beyond cloning

## Technical Decisions

### Why Monolithic?
1. **Faster Development**: Single codebase is easier to set up and modify
2. **Simpler Debugging**: All code runs in one process
3. **Easier Testing**: No need for inter-service testing
4. **Rapid Iteration**: Changes don't require coordinating multiple components
5. **Validation First**: Proves the concept before architectural complexity

### Future Migration Path
Once MVP is validated, we can:
- Extract detection logic into pluggable modules
- Separate storage layer for larger datasets
- Add API layer for programmatic access
- Introduce parallel processing for large repositories

## Development Timeline

**Total Duration**: 5 weeks

| Week | Phase | Key Deliverable |
|------|-------|----------------|
| 1 | Setup + Ingestion | Clonable, runnable CLI |
| 2 | Ingestion + Analysis | Parse commit history |
| 3 | Analysis + Detection | Identify LLM patterns |
| 4 | Detection + Reporting | Generate reports |
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
- ✅ Analysis of at least 5 real-world repositories
- ✅ Reports identifying LLM usage patterns
- ✅ Documentation for users to run the tool themselves
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
