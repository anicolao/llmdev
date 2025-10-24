# LLM Development Documentation Site

This directory contains the GitHub Pages site for LLM Development—a collection of evidence-based practices for building software with AI assistance.

## Structure

```
docs/
├── _config.yml              # Jekyll configuration
├── index.md                 # Home page
├── getting-started.md       # How To Get Started
├── staying-organized.md     # How To Stay Organized
├── leveling-up.md          # How To Level Up
├── sharpen-the-saw.md      # How To Sharpen the Saw
├── about.md                # About the site and methodology
└── assets/
    └── main.scss           # Custom styling (minima theme override)
```

## Local Development

To preview the site locally:

```bash
# Install Jekyll (if not already installed)
gem install bundler jekyll

# Create a Gemfile in the docs directory
cat > docs/Gemfile << EOF
source "https://rubygems.org"
gem "github-pages", group: :jekyll_plugins
gem "webrick"
EOF

# Install dependencies
cd docs
bundle install

# Serve locally
bundle exec jekyll serve

# Open http://localhost:4000/ in your browser
# Note: For custom domain setup, baseurl is "" (empty)
# For GitHub Pages default URL, it would be http://localhost:4000/llmdev/
```

## Deployment

GitHub Pages automatically builds and deploys this site when changes are pushed to the main branch.

**This site uses a custom domain:** `https://llmdev.morpheum.dev`

**Configuration in GitHub repository settings:**
1. Go to Settings → Pages
2. Set Source to "Deploy from a branch"
3. Select branch: main
4. Select folder: /docs
5. Custom domain: llmdev.morpheum.dev
6. Enforce HTTPS: enabled

For setup without custom domain, the site would be available at: `https://anicolao.github.io/llmdev/`
See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed configuration instructions.

## Content Guidelines

All content on this site follows these principles:

### Evidence-Based
- Every claim backed by specific PR references
- Metrics from real projects (velocity, iteration counts, etc.)
- Examples from production codebases

### Actionable
- Templates and checklists readers can use
- Specific prompts that worked
- Step-by-step processes

### Concise
- Focus on "How To" rather than theory
- Short sections with clear headings
- Scannable content with checklists

### Examples
- Reference real PRs from case studies
- Show before/after comparisons
- Include both successes and failures

## How This Site Was Built

This site demonstrates its own methodology:

**Foundation** (Getting Started):
- Started with clear VISION.md and README.md
- Built tiny MVP (instruction generator)
- Iterated from working kernel

**Organization** (Staying Organized):
- Evaluated multiple approaches (API vs instructions)
- Chose phased approach after design analysis
- Documented alternatives in DESIGN_OPTIONS.md

**Iteration** (Leveling Up):
- Created 4 comprehensive case studies
- Refined templates through use
- Test-driven development (51 tests)

**Consolidation** (Sharpen the Saw):
- Distilled insights into SUMMARY.md
- Created this documentation site
- Captured patterns in copilot-instructions.md

See [about.md](about.md) for complete details.

## Editing Content

### Adding a New Page

1. Create a new `.md` file in the `docs/` directory
2. Add front matter:
   ```yaml
   ---
   layout: default
   title: Your Page Title
   ---
   ```
3. Add to `_config.yml` under `header_pages` if it should be in navigation
4. Write content in Markdown
5. Test locally before committing

### Updating Existing Pages

1. Edit the relevant `.md` file
2. Follow the existing structure and style
3. Include evidence sources at the bottom
4. Test locally to verify formatting

### Style Guidelines

**Headings:**
- `#` for page title
- `##` for major sections
- `###` for subsections

**Code blocks:**
```markdown
\`\`\`bash
command here
\`\`\`
```

**Checklists:**
```markdown
- [ ] Incomplete item
- [x] Completed item
```

**Evidence sources:**
```markdown
<small>**Evidence sources**: [project](url) PR #X (description).</small>
```

## Maintenance

Regular maintenance tasks:

- **Monthly**: Review all examples still work with latest case studies
- **Quarterly**: Update metrics if new case studies completed
- **As needed**: Fix broken links, update deprecated information

## Questions or Issues?

Open an issue in the [llmdev repository](https://github.com/anicolao/llmdev/issues).
