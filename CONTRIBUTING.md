# Contributing to llmdev

Thank you for your interest in contributing to llmdev! This document provides guidelines for contributors.

## Project Mission

The llmdev project studies how LLMs like GitHub Copilot are used to build real software systems. Our approach is evidence-based analysis through comprehensive case studies.

See `.github/copilot-instructions.md` for detailed project guidance and best practices.

## Ways to Contribute

### 1. Create Case Studies

The most valuable contribution is analyzing repositories and creating case studies:

**Process:**
1. Choose an interesting repository (preferably with visible LLM usage)
2. Use `llmdev generate-instructions` to start phased analysis
3. Follow instructions through all 9 phases
4. Create comprehensive case study following existing format
5. Save to `case_studies/GITHUB_OWNER_REPO.md`
6. Submit pull request

**What makes a good case study:**
- Thorough analysis (30-50 pages)
- Clear development story arc
- Actual prompts extracted and analyzed
- Iteration patterns explained
- Actionable best practices
- Evidence-based insights

See existing case studies in `case_studies/` for examples.

### 2. Improve Instructions

Help enhance the phased instruction templates:

**Areas for improvement:**
- Clarify phase objectives
- Add more examples and guidance
- Improve task descriptions
- Enhance output templates
- Update based on user feedback

**Files to edit:**
- `src/llmdev/mcp_instructions.py` - Instruction generator
- Instruction templates within the generator

### 3. Enhance Documentation

Improve project documentation:

- Update README with clearer examples
- Enhance QUICKSTART guide
- Add FAQ sections
- Create video tutorials or walkthroughs
- Document edge cases and tips

### 4. Code Improvements

For developers familiar with the codebase:

**Legacy components** (deprecated but maintained):
- `analyzer.py` - Direct API analysis
- `github_client.py` - REST API client
- `detector.py` - Pattern detection
- `reporter.py` - Automated reports

These components are retained for edge cases but not primary workflow.

**Active components:**
- `cli.py` - Command-line interface
- `mcp_instructions.py` - Instruction generation
- `analyzers/` - Analysis helpers (for future automation)
- `cache/` - Caching infrastructure

## Development Setup (For Code Contributions)

### 1. Fork and Clone

```bash
git clone https://github.com/YOUR-USERNAME/llmdev.git
cd llmdev
```

### 2. Set Up Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -e ".[dev]"
```

### 3. Create Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### 4. Run Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=llmdev

# Run specific tests
pytest tests/test_mcp_instructions.py -v
```

## Pull Request Process

### For Case Studies

1. Ensure case study follows the standard format
2. Include all required sections
3. Provide evidence-based insights
4. Follow naming convention: `GITHUB_OWNER_REPO.md`
5. Place in `case_studies/` directory

### For Code/Documentation Changes

1. Run tests and ensure they pass
2. Update documentation if needed
3. Write clear commit messages
4. Keep changes focused and minimal

### Commit Messages

Use clear, descriptive commit messages:

```
Add case study for microsoft/calculator

- Complete 9-phase analysis
- Extract 15 prompt examples
- Identify 3 key development patterns
- Document lessons learned
```

## Case Study Guidelines

### Required Sections

1. **Executive Summary** - Key findings overview
2. **Repository Overview** - Basic statistics
3. **Development Story Arc** - Project evolution
4. **LLM Usage Patterns** - Evidence of LLM assistance
5. **Prompt Analysis** - Effective prompts and patterns
6. **Iteration Patterns** - Quick wins vs complex work
7. **Development Patterns** - Practices observed
8. **Best Practices** - Actionable recommendations
9. **Technical Insights** - Technology-specific notes
10. **Conclusion** - Summary and takeaways
11. **Appendix: Methodology** - How analysis was performed

### Quality Standards

- **Evidence-based**: Every claim backed by specific examples
- **Actionable**: Clear recommendations others can apply
- **Comprehensive**: Cover all aspects of development
- **Well-structured**: Easy to navigate and reference
- **Professional**: Polished writing and formatting

## Questions?

- Review existing case studies for examples
- Check `.github/copilot-instructions.md` for detailed project guidance
- Open an issue for questions or discussions
- Review closed PRs for context on past decisions

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on improving the project
- Help create a welcoming community

## Getting Started

The best way to start contributing:

1. **Read existing case studies** - Understand the format and depth
2. **Pick a repository** - Choose something interesting to analyze
3. **Follow the phased approach** - Use `generate-instructions` for each phase
4. **Document thoroughly** - Capture insights as you analyze
5. **Submit your case study** - Share what you learned

Thank you for contributing to llmdev! 🎉
