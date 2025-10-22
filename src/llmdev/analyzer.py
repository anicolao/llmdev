"""
Repository analyzer that orchestrates data collection and analysis.
"""

import logging
from typing import Dict, List, Any
from datetime import datetime

from llmdev.config import Config
from llmdev.github_client import GitHubClient
from llmdev.detector import CopilotDetector, Detection


logger = logging.getLogger(__name__)


class RepositoryAnalyzer:
    """Analyzes GitHub repositories for LLM-generated code."""
    
    def __init__(self, config: Config):
        """
        Initialize the analyzer.
        
        Args:
            config: Configuration object
        """
        self.config = config
        self.github_client = GitHubClient(config)
        self.detector = CopilotDetector()
        
    def analyze(self, owner: str, repo: str) -> Dict[str, Any]:
        """
        Analyze a GitHub repository.
        
        Args:
            owner: Repository owner
            repo: Repository name
            
        Returns:
            Dictionary containing analysis results
        """
        logger.info(f"Starting analysis of {owner}/{repo}")
        
        # Get repository
        repository = self.github_client.get_repository(owner, repo)
        
        # Collect data
        logger.info("Collecting repository data...")
        commits_data = self._collect_commits(repository)
        prs_data = self._collect_prs(repository)
        issues_data = self._collect_issues(repository)
        
        # Run detection
        logger.info("Running Copilot detection...")
        all_detections = []
        
        # Detect in commits
        for commit_data in commits_data:
            detections = self.detector.detect_in_commit(commit_data)
            all_detections.extend(detections)
        
        # Detect in PRs
        for pr_data in prs_data:
            detections = self.detector.detect_in_pr(pr_data)
            all_detections.extend(detections)
        
        # Detect in issues
        for issue_data in issues_data:
            detections = self.detector.detect_in_issue(issue_data)
            all_detections.extend(detections)
        
        logger.info(f"Found {len(all_detections)} Copilot detections")
        
        # Generate summary
        summary = self.detector.get_summary(all_detections)
        
        # Compile results
        results = {
            'repository': {
                'owner': owner,
                'name': repo,
                'full_name': repository.full_name,
                'description': repository.description,
                'stars': repository.stargazers_count,
                'forks': repository.forks_count,
                'created_at': repository.created_at,
                'updated_at': repository.updated_at,
            },
            'analysis': {
                'timestamp': datetime.now(),
                'commits_analyzed': len(commits_data),
                'prs_analyzed': len(prs_data),
                'issues_analyzed': len(issues_data),
            },
            'commits': commits_data,
            'prs': prs_data,
            'issues': issues_data,
            'detections': all_detections,
            'summary': summary,
        }
        
        logger.info("Analysis complete")
        return results
    
    def _collect_commits(self, repository) -> List[Dict[str, Any]]:
        """Collect commit data from repository."""
        logger.info("Fetching commits...")
        commits = self.github_client.get_commits(repository)
        
        commits_data = []
        for commit in commits:
            try:
                commits_data.append({
                    'sha': commit.sha,
                    'message': commit.commit.message,
                    'author': commit.commit.author.name if commit.commit.author else 'unknown',
                    'author_email': commit.commit.author.email if commit.commit.author else '',
                    'date': commit.commit.author.date if commit.commit.author else None,
                    'url': commit.html_url,
                })
            except Exception as e:
                logger.warning(f"Error processing commit {commit.sha}: {e}")
                continue
        
        logger.info(f"Collected {len(commits_data)} commits")
        return commits_data
    
    def _collect_prs(self, repository) -> List[Dict[str, Any]]:
        """Collect PR data from repository."""
        logger.info("Fetching pull requests...")
        prs = self.github_client.get_pull_requests(repository)
        
        prs_data = []
        for pr in prs:
            try:
                # Get comments
                comments = self.github_client.get_pr_comments(pr)
                
                prs_data.append({
                    'number': pr.number,
                    'title': pr.title,
                    'body': pr.body or '',
                    'author': pr.user.login if pr.user else 'unknown',
                    'state': pr.state,
                    'created_at': pr.created_at,
                    'updated_at': pr.updated_at,
                    'merged': pr.merged,
                    'url': pr.html_url,
                    'comments': comments,
                })
            except Exception as e:
                logger.warning(f"Error processing PR #{pr.number}: {e}")
                continue
        
        logger.info(f"Collected {len(prs_data)} pull requests")
        return prs_data
    
    def _collect_issues(self, repository) -> List[Dict[str, Any]]:
        """Collect issue data from repository."""
        logger.info("Fetching issues...")
        issues = self.github_client.get_issues(repository)
        
        issues_data = []
        for issue in issues:
            try:
                # Get comments
                comments = self.github_client.get_issue_comments(issue)
                
                issues_data.append({
                    'number': issue.number,
                    'title': issue.title,
                    'body': issue.body or '',
                    'author': issue.user.login if issue.user else 'unknown',
                    'state': issue.state,
                    'created_at': issue.created_at,
                    'updated_at': issue.updated_at,
                    'url': issue.html_url,
                    'comments': comments,
                })
            except Exception as e:
                logger.warning(f"Error processing issue #{issue.number}: {e}")
                continue
        
        logger.info(f"Collected {len(issues_data)} issues")
        return issues_data
