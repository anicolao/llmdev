"""
Command-line interface for llmdev.
"""

import click
import logging
import sys
from pathlib import Path
from typing import Optional

from llmdev.analyzer import RepositoryAnalyzer
from llmdev.reporter import ReportGenerator
from llmdev.config import Config
from llmdev.mcp_instructions import MCPInstructionsGenerator


def setup_logging(verbose: bool) -> None:
    """Configure logging based on verbosity level."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


@click.group()
@click.version_option(version="0.1.0")
def cli():
    """llmdev - Analyze LLM-generated code in GitHub repositories."""
    pass


@cli.command(hidden=True)  # Hidden from help - use generate-instructions instead
@click.argument("repository")
@click.option(
    "--token", envvar="GITHUB_TOKEN", help="GitHub API token (can also use GITHUB_TOKEN env var)"
)
@click.option(
    "--output",
    "-o",
    default="output",
    type=click.Path(),
    help="Output directory for reports (default: output/)",
)
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose logging")
@click.option(
    "--max-commits",
    type=int,
    default=100,
    help="Maximum number of commits to analyze (default: 100)",
)
@click.option(
    "--max-prs", type=int, default=50, help="Maximum number of PRs to analyze (default: 50)"
)
@click.option(
    "--max-issues", type=int, default=50, help="Maximum number of issues to analyze (default: 50)"
)
@click.option(
    "--deep-analysis",
    is_flag=True,
    help="Enable deep analysis with prompt extraction, iteration patterns, and categorization",
)
@click.option("--no-cache", is_flag=True, help="Disable caching of API responses")
def analyze(
    repository: str,
    token: Optional[str],
    output: str,
    verbose: bool,
    max_commits: int,
    max_prs: int,
    max_issues: int,
    deep_analysis: bool,
    no_cache: bool,
):
    """
    [DEPRECATED] Analyze a GitHub repository for LLM-generated code using REST API.
    
    ⚠️  WARNING: This command is deprecated due to GitHub API rate limits.
    
    For repositories with more than a few PRs, this will likely fail with rate limit errors.
    
    🚀 RECOMMENDED: Use 'generate-instructions' command instead:
       llmdev generate-instructions owner/repo --phase intro
    
    The generate-instructions approach uses MCP GitHub server which avoids rate limits
    and produces better, more comprehensive case studies.

    REPOSITORY should be in the format 'owner/repo' (e.g., 'microsoft/vscode')
    """
    setup_logging(verbose)
    logger = logging.getLogger(__name__)
    
    # Show deprecation warning
    click.echo("=" * 70, err=True)
    click.echo("⚠️  DEPRECATION WARNING", err=True)
    click.echo("=" * 70, err=True)
    click.echo("This command is deprecated and likely to fail on real repositories.", err=True)
    click.echo("", err=True)
    click.echo("GitHub API rate limits:", err=True)
    click.echo("  - Unauthenticated: 60 requests/hour", err=True)
    click.echo("  - Authenticated: 5,000 requests/hour", err=True)
    click.echo("", err=True)
    click.echo("A typical repository analysis requires hundreds or thousands of API calls.", err=True)
    click.echo("", err=True)
    click.echo("🚀 RECOMMENDED APPROACH:", err=True)
    click.echo(f"   llmdev generate-instructions {repository} --phase intro", err=True)
    click.echo("", err=True)
    click.echo("This creates phase-by-phase instructions for MCP-enabled tools", err=True)
    click.echo("that avoid rate limits entirely.", err=True)
    click.echo("=" * 70, err=True)
    click.echo("", err=True)
    
    # Ask for confirmation to continue
    if not click.confirm("Do you want to continue with the deprecated analyze command?"):
        click.echo("Aborted. Use 'generate-instructions' instead.")
        sys.exit(0)

    logger.info(f"Starting analysis of repository: {repository}")

    # Validate repository format
    if "/" not in repository:
        click.echo("Error: Repository must be in format 'owner/repo'", err=True)
        sys.exit(1)

    owner, repo = repository.split("/", 1)

    # Check for GitHub token
    if not token:
        click.echo(
            "Warning: No GitHub token provided. API rate limits will be restrictive.\n"
            "Set GITHUB_TOKEN environment variable or use --token option.",
            err=True,
        )

    # Create output directory
    output_path = Path(output)
    output_path.mkdir(parents=True, exist_ok=True)

    # Create configuration
    config = Config(
        github_token=token,
        output_dir=output_path,
        max_commits=max_commits,
        max_prs=max_prs,
        max_issues=max_issues,
        verbose=verbose,
        deep_analysis=deep_analysis,
        enable_cache=not no_cache,
    )

    try:
        # Initialize analyzer
        logger.info("Initializing repository analyzer...")
        if deep_analysis:
            logger.info("Deep analysis mode enabled - extracting prompts, patterns, and iterations")
        analyzer = RepositoryAnalyzer(config)

        # Run analysis
        logger.info("Fetching repository data...")
        results = analyzer.analyze(owner, repo)

        # Generate report
        logger.info("Generating report...")
        report_generator = ReportGenerator(config)
        report_path = report_generator.generate(results)

        click.echo(f"\n✓ Analysis complete!")
        click.echo(f"✓ Report saved to: {report_path}")

    except Exception as e:
        logger.exception("Analysis failed")
        click.echo(f"Error: {str(e)}", err=True)
        sys.exit(1)


@cli.command()
@click.argument("repository")
@click.option(
    "--output",
    "-o",
    default="output",
    type=click.Path(),
    help="Output directory for instructions (default: output/)",
)
@click.option(
    "--phase",
    "-p",
    type=click.Choice([
        "intro", "overview", "detection", "story", "prompts",
        "iteration", "patterns", "recommendations", "synthesis"
    ], case_sensitive=False),
    help="Generate instructions for a specific phase (intro, overview, detection, story, prompts, iteration, patterns, recommendations, synthesis)",
)
def generate_instructions(repository: str, output: str, phase: Optional[str]):
    """
    Generate MCP-compatible analysis instructions for a repository.

    This command creates structured instruction documents that guide
    MCP-enabled tools (like GitHub Copilot) through analyzing a repository
    to create a case study. This approach avoids API rate limits by using
    the MCP GitHub server directly.

    Instructions are broken into phases to avoid overwhelming context windows:
    
    - intro: Introduction and setup
    - overview: Repository metadata and statistics  
    - detection: LLM usage pattern detection
    - story: Development story arc extraction
    - prompts: Prompt and request analysis
    - iteration: Iteration pattern analysis
    - patterns: Development pattern identification
    - recommendations: Best practices synthesis
    - synthesis: Executive summary and completion

    REPOSITORY should be in the format 'owner/repo' (e.g., 'microsoft/vscode')

    Examples:
        # Start analysis - get introduction and workflow
        llmdev generate-instructions owner/repo --phase intro
        
        # Get next phase instructions
        llmdev generate-instructions owner/repo --phase overview
        
        # Generate full instructions (legacy mode, not recommended for large analysis)
        llmdev generate-instructions owner/repo
    """
    logger = logging.getLogger(__name__)
    
    # Validate repository format
    if "/" not in repository:
        click.echo("Error: Repository must be in format 'owner/repo'", err=True)
        sys.exit(1)

    owner, repo = repository.split("/", 1)
    
    # Create output directory
    output_path = Path(output)
    output_path.mkdir(parents=True, exist_ok=True)
    
    try:
        generator = MCPInstructionsGenerator(output_path)
        instructions_path = generator.generate(owner, repo, phase=phase)
        
        click.echo(f"\n✓ Instructions generated successfully!")
        click.echo(f"✓ File saved to: {instructions_path}")
        
        if phase:
            click.echo(f"\n📋 Phase: {phase}")
            click.echo(f"Follow the instructions in the file, then run:")
            
            # Suggest next phase
            phases = MCPInstructionsGenerator.PHASES
            if phase in phases:
                current_idx = phases.index(phase)
                if current_idx < len(phases) - 1:
                    next_phase = phases[current_idx + 1]
                    click.echo(f"  llmdev generate-instructions {owner}/{repo} --phase {next_phase}")
                else:
                    click.echo(f"\n🎉 This is the final phase. Your case study should now be complete!")
                    click.echo(f"📄 Save to: case_studies/GITHUB_{owner.upper()}_{repo.upper()}.md")
        else:
            click.echo(f"\n⚠️  Note: Full instructions mode generates a large document.")
            click.echo(f"   Consider using --phase flag for step-by-step analysis:")
            click.echo(f"   llmdev generate-instructions {owner}/{repo} --phase intro")
        
    except Exception as e:
        logger.exception("Failed to generate instructions")
        click.echo(f"Error: {str(e)}", err=True)
        sys.exit(1)


def main():
    """Main entry point for the CLI."""
    cli()


if __name__ == "__main__":
    main()
