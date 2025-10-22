"""
Configuration management for llmdev.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class Config:
    """Configuration for llmdev analysis."""
    
    github_token: Optional[str] = None
    output_dir: Path = Path("output")
    max_commits: int = 100
    max_prs: int = 50
    max_issues: int = 50
    verbose: bool = False
    
    # GitHub API rate limiting
    api_retry_attempts: int = 3
    api_retry_delay: int = 2  # seconds
    
    # Caching and rate limiting (MVP2 features)
    enable_cache: bool = True
    cache_ttl: int = 3600  # seconds (1 hour)
    enable_rate_limiting: bool = True
    
    # Deep analysis features (MVP2)
    deep_analysis: bool = False
    analyze_commits_per_pr: bool = False
    
    def __post_init__(self):
        """Ensure output_dir is a Path object."""
        if not isinstance(self.output_dir, Path):
            self.output_dir = Path(self.output_dir)
