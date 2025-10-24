---
layout: default
title: About
---

# About LLM Development

## The Methodology

LLM Development is a proven methodology for building software with AI assistance. This site teaches you **how to work effectively with AI tools** using patterns distilled from analyzing 334+ PRs across successful real-world projects.

### What You'll Learn

**Foundation Patterns:**
- How to prompt AI to create effective README and VISION documents
- How to get AI to build a tiny MVP in hours
- How to maintain direction while iterating rapidly

**Development Patterns:**
- Design-first prompting for complex features
- Specific prompt structures that reduce iteration
- Testing patterns that work with AI
- Consolidation practices for sustainable velocity

**Proven Results:**
- 3-11 PRs/day sustained velocity
- 1-3 commits for 80% of features
- Production-ready in 2-5 weeks

### Evidence Base

All practices are validated by comprehensive case study analysis:

- **[dikuclient](https://github.com/anicolao/dikuclient)**: 63 PRs in 18 days, 3.5 PRs/day
- **[DikuMUD](https://github.com/anicolao/DikuMUD)**: 165 PRs in 15 days, 11 PRs/day
- **[morpheum](https://github.com/anicolao/morpheum)**: 76 PRs in 37 days
- **[diku](https://github.com/anicolao/diku)**: 30 issues in 5 days

These represent 334+ PRs and 900+ commits of real development work analyzed systematically.

Full case studies (30-75 pages each) available in the [llmdev repository](https://github.com/anicolao/llmdev/tree/main/case_studies) for those interested in the detailed analysis.

### Analysis Methodology

Each case study follows a rigorous phased approach:

1. **Repository Overview**: Gather statistics, timeline, key metrics
2. **LLM Usage Detection**: Identify Copilot mentions, patterns, explicit attribution
3. **Development Story Arc**: Extract phases, milestones, evolution
4. **Prompt Analysis**: Study what prompts worked, identify patterns
5. **Iteration Patterns**: Analyze commit counts, complexity, refinement cycles
6. **Development Patterns**: Extract practices, anti-patterns, success factors
7. **Best Practices**: Synthesize actionable recommendations
8. **Technical Insights**: Document technology-specific learnings

### What Makes This Different

Most AI coding advice is speculation or marketing. This methodology is:

- **Evidence-based**: Every practice validated by analyzing 334+ real PRs
- **Metric-driven**: Velocity, iteration counts, success rates from production work
- **Actionable**: Specific prompts, templates, and checklists you can use immediately
- **Proven**: 3-11 PRs/day sustained velocity achieved by following these patterns

## Want to Analyze Projects Yourself?

The [llmdev tool](https://github.com/anicolao/llmdev) lets you analyze any repository to extract patterns:

```bash
git clone https://github.com/anicolao/llmdev.git
cd llmdev && pip install -e .

# Analyze any repository
llmdev generate-instructions owner/repo --phase intro
```

This is how we created the case studies that informed this site's methodology. You can use it to:
- Study how specific projects work
- Extract patterns from codebases you admire
- Validate that your projects follow good patterns
- Create your own case studies

Takes 2-3 hours to complete a comprehensive analysis.

## How This Site Was Built

This site was created using its own methodology—a practical demonstration of the practices we teach.

### Phase 1: Foundation (Getting Started)

**Clear README**
- The llmdev project started with comprehensive README.md
- Documented installation, usage, and examples
- Provided clear context for AI assistance

**Compelling VISION**
- Created VISION.md defining mission and principles
- Established success criteria
- Identified open questions and long-term goals

**Tiny MVP**
- Built minimal instruction generator (Phase 1)
- Got it working and tested in hours
- Iterated from that kernel

### Phase 2: Organization (Staying Organized)

**Design Analysis**
- Evaluated multiple approaches:
  1. Direct API analysis (tried first, hit rate limits)
  2. Phased instruction generation (chosen approach)
  3. Hybrid caching system (considered but deferred)

**Alternative Selection**
- Chose phased instructions based on evidence:
  - Pro: No rate limits
  - Pro: Works on any repository size
  - Pro: Proven with real case studies
  - Con: Requires MCP tools (acceptable trade-off)

**Design Documents**
- Created DESIGN_OPTIONS.md for architectural decisions
- Documented MVP.md with approach and rationale
- Planned MVP2.md for future enhancements

### Phase 3: Iteration (Leveling Up)

**Rapid Iteration**
- Created case studies through phased analysis
- Refined instruction templates based on usage
- Improved guidance incrementally

**Specific Prompts**
- Problem-Context-Solution structure for features
- Clear constraints in prompts
- Success criteria for each phase

**Test-First Development**
- 51 tests covering core functionality
- Tests guided development
- 62% code coverage maintained

### Phase 4: Consolidation (Sharpen the Saw)

**Periodic Consolidation**
- Consolidated learnings into SUMMARY.md
- Created this documentation site (consolidation of insights)
- Captured patterns in copilot-instructions.md

**Documentation Updates**
- Kept README current with approach evolution
- Updated QUICKSTART.md based on user feedback
- Created comprehensive case studies

**Reflection**
- Learned that direct API approach failed (documented in MVP.md)
- Identified successful phased approach through iteration
- Captured best practices from case study creation

## Timeline: Building This Site

**Foundation Phase** (Original llmdev development):
- Day 1-2: README + VISION + basic structure
- Day 3-7: MVP instruction generator
- Week 2-4: First case studies created

**Enhancement Phase**:
- Analyzed 4 comprehensive repositories
- Distilled insights into SUMMARY.md
- Created reusable patterns and templates

**Documentation Phase** (This site):
- Day 1: Planned site structure and content
- Day 2: Created How To guides from case study insights
- Day 3: Set up GitHub Pages with Jekyll
- Day 4: Polish and publish

**Total**: Weeks of analysis → Hours of site creation (because foundation was solid)

## Success Metrics

The llmdev project demonstrates the practices it teaches:

**Velocity:**
- Sustained development over weeks
- Multiple comprehensive case studies completed
- Rapid iteration on instruction templates

**Quality:**
- 51 tests passing
- Clear documentation
- Actionable outputs (case studies)

**Learning:**
- Failed approaches documented (MVP.md)
- Successful patterns captured (SUMMARY.md)
- Continuous improvement (MVP2.md planning)

## Contributing

We welcome contributions to both the site and the llmdev tool:

**Ways to contribute:**
- Analyze additional repositories using llmdev
- Share insights from your LLM-assisted projects
- Improve How To guides with additional examples
- Report issues or suggest improvements
- Create case studies of interesting projects

See [CONTRIBUTING.md](https://github.com/anicolao/llmdev/blob/main/CONTRIBUTING.md) in the llmdev repository.

## License

This site and the llmdev project are released under CC0 (public domain). Use freely, adapt, share, and build upon these insights.

## Contact

- **GitHub**: [llmdev project](https://github.com/anicolao/llmdev)
- **Issues**: [Report issues or suggestions](https://github.com/anicolao/llmdev/issues)
- **Discussions**: [Join discussions](https://github.com/anicolao/llmdev/discussions)

---

<small>Last updated: October 2025 | Built with evidence, maintained with care.</small>
