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


def setup_logging(verbose: bool) -> None:
    """Configure logging based on verbosity level."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )


@click.group()
@click.version_option(version="0.1.0")
def cli():
    """llmdev - Analyze LLM-generated code in GitHub repositories."""
    pass


@cli.command()
@click.argument('repository')
@click.option(
    '--token',
    envvar='GITHUB_TOKEN',
    help='GitHub API token (can also use GITHUB_TOKEN env var)'
)
@click.option(
    '--output',
    '-o',
    default='output',
    type=click.Path(),
    help='Output directory for reports (default: output/)'
)
@click.option(
    '--verbose',
    '-v',
    is_flag=True,
    help='Enable verbose logging'
)
@click.option(
    '--max-commits',
    type=int,
    default=100,
    help='Maximum number of commits to analyze (default: 100)'
)
@click.option(
    '--max-prs',
    type=int,
    default=50,
    help='Maximum number of PRs to analyze (default: 50)'
)
@click.option(
    '--max-issues',
    type=int,
    default=50,
    help='Maximum number of issues to analyze (default: 50)'
)
def analyze(
    repository: str,
    token: Optional[str],
    output: str,
    verbose: bool,
    max_commits: int,
    max_prs: int,
    max_issues: int
):
    """
    Analyze a GitHub repository for LLM-generated code.
    
    REPOSITORY should be in the format 'owner/repo' (e.g., 'microsoft/vscode')
    
    Example:
        llmdev analyze microsoft/vscode --token YOUR_TOKEN
    """
    setup_logging(verbose)
    logger = logging.getLogger(__name__)
    
    logger.info(f"Starting analysis of repository: {repository}")
    
    # Validate repository format
    if '/' not in repository:
        click.echo("Error: Repository must be in format 'owner/repo'", err=True)
        sys.exit(1)
    
    owner, repo = repository.split('/', 1)
    
    # Check for GitHub token
    if not token:
        click.echo(
            "Warning: No GitHub token provided. API rate limits will be restrictive.\n"
            "Set GITHUB_TOKEN environment variable or use --token option.",
            err=True
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
        verbose=verbose
    )
    
    try:
        # Initialize analyzer
        logger.info("Initializing repository analyzer...")
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


def main():
    """Main entry point for the CLI."""
    cli()


if __name__ == '__main__':
    main()
