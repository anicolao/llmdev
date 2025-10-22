"""
GitHub API client for fetching repository data.
"""

import logging
import time
from typing import List, Optional, Dict, Any
from github import Github, GithubException, RateLimitExceededException
from github.Repository import Repository
from github.Commit import Commit
from github.PullRequest import PullRequest
from github.Issue import Issue

from llmdev.config import Config
from llmdev.cache import DiskCache, RateLimiter


logger = logging.getLogger(__name__)


class GitHubClient:
    """Client for interacting with the GitHub API."""
    
    def __init__(self, config: Config):
        """
        Initialize GitHub client.
        
        Args:
            config: Configuration object with GitHub token
        """
        self.config = config
        self.github = Github(config.github_token) if config.github_token else Github()
        
        # Initialize caching if enabled
        self.cache = DiskCache() if config.enable_cache else None
        self.rate_limiter = RateLimiter() if config.enable_rate_limiting else None
        
    def get_repository(self, owner: str, repo: str) -> Repository:
        """
        Get a GitHub repository.
        
        Args:
            owner: Repository owner
            repo: Repository name
            
        Returns:
            GitHub Repository object
        """
        logger.info(f"Fetching repository: {owner}/{repo}")
        try:
            repository = self.github.get_repo(f"{owner}/{repo}")
            logger.info(f"Repository found: {repository.full_name}")
            return repository
        except GithubException as e:
            logger.error(f"Failed to fetch repository: {e}")
            raise
    
    def get_commits(self, repository: Repository, max_count: Optional[int] = None) -> List[Commit]:
        """
        Get commits from a repository.
        
        Args:
            repository: GitHub Repository object
            max_count: Maximum number of commits to fetch
            
        Returns:
            List of Commit objects
        """
        max_count = max_count or self.config.max_commits
        logger.info(f"Fetching up to {max_count} commits...")
        
        commits = []
        try:
            for i, commit in enumerate(repository.get_commits()):
                if i >= max_count:
                    break
                commits.append(commit)
                if (i + 1) % 10 == 0:
                    logger.debug(f"Fetched {i + 1} commits...")
                    
            logger.info(f"Fetched {len(commits)} commits")
            return commits
        except RateLimitExceededException:
            logger.warning("Rate limit exceeded while fetching commits")
            return commits
        except GithubException as e:
            logger.error(f"Error fetching commits: {e}")
            return commits
    
    def get_pull_requests(
        self, 
        repository: Repository, 
        max_count: Optional[int] = None,
        state: str = "all"
    ) -> List[PullRequest]:
        """
        Get pull requests from a repository.
        
        Args:
            repository: GitHub Repository object
            max_count: Maximum number of PRs to fetch
            state: PR state filter ('open', 'closed', 'all')
            
        Returns:
            List of PullRequest objects
        """
        max_count = max_count or self.config.max_prs
        logger.info(f"Fetching up to {max_count} pull requests (state: {state})...")
        
        prs = []
        try:
            for i, pr in enumerate(repository.get_pulls(state=state, sort='created', direction='desc')):
                if i >= max_count:
                    break
                prs.append(pr)
                if (i + 1) % 10 == 0:
                    logger.debug(f"Fetched {i + 1} PRs...")
                    
            logger.info(f"Fetched {len(prs)} pull requests")
            return prs
        except RateLimitExceededException:
            logger.warning("Rate limit exceeded while fetching PRs")
            return prs
        except GithubException as e:
            logger.error(f"Error fetching PRs: {e}")
            return prs
    
    def get_issues(
        self, 
        repository: Repository, 
        max_count: Optional[int] = None,
        state: str = "all"
    ) -> List[Issue]:
        """
        Get issues from a repository.
        
        Args:
            repository: GitHub Repository object
            max_count: Maximum number of issues to fetch
            state: Issue state filter ('open', 'closed', 'all')
            
        Returns:
            List of Issue objects
        """
        max_count = max_count or self.config.max_issues
        logger.info(f"Fetching up to {max_count} issues (state: {state})...")
        
        issues = []
        try:
            for i, issue in enumerate(repository.get_issues(state=state, sort='created', direction='desc')):
                # Skip pull requests (they show up in issues endpoint)
                if issue.pull_request:
                    continue
                if len(issues) >= max_count:
                    break
                issues.append(issue)
                if (len(issues)) % 10 == 0:
                    logger.debug(f"Fetched {len(issues)} issues...")
                    
            logger.info(f"Fetched {len(issues)} issues")
            return issues
        except RateLimitExceededException:
            logger.warning("Rate limit exceeded while fetching issues")
            return issues
        except GithubException as e:
            logger.error(f"Error fetching issues: {e}")
            return issues
    
    def get_pr_comments(self, pr: PullRequest) -> List[Dict[str, Any]]:
        """
        Get all comments from a pull request.
        
        Args:
            pr: PullRequest object
            
        Returns:
            List of comment dictionaries
        """
        comments = []
        try:
            # Get issue comments (conversation comments)
            for comment in pr.get_issue_comments():
                comments.append({
                    'type': 'issue_comment',
                    'body': comment.body,
                    'author': comment.user.login if comment.user else 'unknown',
                    'created_at': comment.created_at
                })
            
            # Get review comments (code review comments)
            for comment in pr.get_review_comments():
                comments.append({
                    'type': 'review_comment',
                    'body': comment.body,
                    'author': comment.user.login if comment.user else 'unknown',
                    'created_at': comment.created_at,
                    'path': comment.path
                })
        except GithubException as e:
            logger.warning(f"Error fetching PR comments: {e}")
            
        return comments
    
    def get_issue_comments(self, issue: Issue) -> List[Dict[str, Any]]:
        """
        Get all comments from an issue.
        
        Args:
            issue: Issue object
            
        Returns:
            List of comment dictionaries
        """
        comments = []
        try:
            for comment in issue.get_comments():
                comments.append({
                    'body': comment.body,
                    'author': comment.user.login if comment.user else 'unknown',
                    'created_at': comment.created_at
                })
        except GithubException as e:
            logger.warning(f"Error fetching issue comments: {e}")
            
        return comments
    
    def get_rate_limit(self) -> Dict[str, Any]:
        """
        Get current GitHub API rate limit status.
        
        Returns:
            Dictionary with rate limit information
        """
        rate_limit = self.github.get_rate_limit()
        return {
            'core': {
                'remaining': rate_limit.core.remaining,
                'limit': rate_limit.core.limit,
                'reset': rate_limit.core.reset
            }
        }
