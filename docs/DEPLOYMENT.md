# Deploying LLM Development Site

This site is designed to be deployed on GitHub Pages.

## GitHub Pages Setup

To enable GitHub Pages for this repository:

1. **Go to Repository Settings**
   - Navigate to https://github.com/anicolao/llmdev/settings/pages

2. **Configure Source**
   - Under "Build and deployment" → "Source"
   - Select: **Deploy from a branch**
   - Branch: `main` (or your default branch)
   - Folder: `/docs`
   - Click **Save**

3. **Wait for Deployment**
   - GitHub will automatically build and deploy the site
   - First deployment takes 1-2 minutes
   - Subsequent deployments are faster

4. **Access the Site**
   - Site will be available at: `https://anicolao.github.io/llmdev/`
   - Custom domains can be configured in the same settings page

## How GitHub Pages Works

GitHub Pages automatically:
- Detects the `docs/_config.yml` Jekyll configuration
- Builds the site using Jekyll
- Serves the static HTML at the configured URL
- Rebuilds on every push to the main branch

## Verification

After deployment, verify:

- ✅ Home page loads: `https://anicolao.github.io/llmdev/`
- ✅ Navigation works (check all links in header)
- ✅ Internal links work (test links between pages)
- ✅ Styling applied (CSS loaded correctly)
- ✅ Code blocks formatted properly
- ✅ No 404 errors in browser console

## Troubleshooting

### Site Not Building

Check the **Actions** tab for build errors:
- Go to https://github.com/anicolao/llmdev/actions
- Look for "pages build and deployment" workflow
- Click to see error details

Common issues:
- Invalid YAML in `_config.yml`
- Missing front matter in `.md` files
- Broken links or references

### Styling Not Applied

If pages load but look unstyled:
- If using custom domain: Verify `baseurl: ""` and `url` matches custom domain in `_config.yml`
- If using GitHub Pages default URL: Verify `baseurl: "/llmdev"` matches repository name in `_config.yml`
- Check `assets/main.scss` exists and has proper front matter (`---` at top)
- Check browser console for CSS 404 errors

### 404 on Navigation Links

If links show 404 errors:
- Verify all files listed in `header_pages` exist in `docs/`
- Check file extensions match (`.md` not `.html`)
- GitHub Pages converts `.md` to `.html` automatically

## Local Development

To test the site locally before deploying:

```bash
# Install dependencies
cd docs
bundle install

# Serve locally
bundle exec jekyll serve

# Open http://localhost:4000/llmdev/
```

Note: Local development requires Ruby and Jekyll installed.

## Continuous Deployment

GitHub Pages automatically deploys on every push to main branch.

**Workflow:**
1. Make changes to files in `docs/` directory
2. Commit and push to main branch
3. GitHub Actions automatically rebuilds site
4. Changes appear at `https://anicolao.github.io/llmdev/` within 1-2 minutes

## Custom Domain

This site is currently configured to use a custom domain: `llmdev.morpheum.dev`

The custom domain is configured with:
1. `CNAME` file in `docs/` directory containing: `llmdev.morpheum.dev`
2. DNS CNAME record: `llmdev` → `anicolao.github.io`
3. Updated `_config.yml`:
   ```yaml
   url: "https://llmdev.morpheum.dev"
   baseurl: ""
   ```

### To Use a Different Custom Domain:

1. Update `CNAME` file to `docs/` directory:
   ```
   llmdev.example.com
   ```

2. Configure DNS at your domain provider:
   - Add CNAME record: `llmdev` → `anicolao.github.io`
   - Or A records pointing to GitHub's IPs

3. Update `_config.yml`:
   ```yaml
   url: "https://llmdev.example.com"
   baseurl: ""
   ```

4. Enable HTTPS in GitHub settings

### To Revert to GitHub Pages Default URL:

Update `_config.yml`:
```yaml
url: "https://anicolao.github.io"
baseurl: "/llmdev"
```

And remove the `CNAME` file.

See [GitHub Pages custom domain docs](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site) for details.

## Monitoring

**Health checks:**
- Monitor site availability at https://anicolao.github.io/llmdev/
- Check GitHub Actions for build failures
- Review visitor analytics (if GitHub Pages analytics enabled)

**Content updates:**
- Review and update content quarterly
- Keep examples current with latest case studies
- Fix broken links as repositories evolve

## Support

For issues with:
- **Site content**: Open issue in llmdev repository
- **GitHub Pages**: Check [GitHub Pages documentation](https://docs.github.com/en/pages)
- **Jekyll**: Check [Jekyll documentation](https://jekyllrb.com/docs/)
