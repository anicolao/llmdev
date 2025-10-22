"""
Repository analyzer that orchestrates data collection and analysis.
"""

import logging
from typing import Dict, List, Any
from datetime import datetime

from llmdev.config import Config
from llmdev.github_client import GitHubClient
from llmdev.detector import CopilotDetector, Detection
from llmdev.analyzers import PRAnalyzer, IterationAnalyzer, PromptAnalyzer


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
        
        # Initialize deep analyzers if enabled
        if config.deep_analysis:
            self.pr_analyzer = PRAnalyzer()
            self.iteration_analyzer = IterationAnalyzer()
            self.prompt_analyzer = PromptAnalyzer()
        else:
            self.pr_analyzer = None
            self.iteration_analyzer = None
            self.prompt_analyzer = None
        
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
        
        # Add deep analysis if enabled
        if self.config.deep_analysis:
            logger.info("Running deep analysis...")
            deep_analysis = self._run_deep_analysis(prs_data, commits_data)
            results['deep_analysis'] = deep_analysis
        
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
    
    def _run_deep_analysis(
        self, 
        prs_data: List[Dict[str, Any]], 
        commits_data: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Run deep analysis on PRs using specialized analyzers.
        
        Args:
            prs_data: List of PR data
            commits_data: List of commit data
            
        Returns:
            Dictionary with deep analysis results
        """
        pr_analyses = []
        all_prompts = []
        
        for pr_data in prs_data:
            # Get commits for this PR if needed
            pr_commits = []
            if self.config.analyze_commits_per_pr:
                # In a real implementation, we'd fetch commits per PR
                # For now, use iteration count from PR metadata
                pass
            
            # Analyze PR content
            pr_analysis = self.pr_analyzer.analyze_pr(pr_data, pr_commits)
            
            # Analyze iterations
            iterations = self.iteration_analyzer.analyze_iterations(pr_data, pr_commits)
            pr_analysis['iterations'] = iterations
            
            # Analyze prompts
            prompts = pr_analysis.get('prompt_extraction', [])
            for prompt in prompts:
                prompt_analysis = self.prompt_analyzer.analyze_prompt(
                    prompt.get('content', ''),
                    outcome_data={
                        'iteration_count': pr_analysis.get('iteration_count', 0),
                        'complexity_score': pr_analysis.get('complexity_score', 0),
                        'merged': pr_data.get('merged', False),
                    }
                )
                prompt_analysis['pr_number'] = pr_data.get('number')
                all_prompts.append(prompt_analysis)
            
            pr_analyses.append(pr_analysis)
        
        # Generate aggregate summaries
        iteration_summary = self.iteration_analyzer.get_iteration_summary(pr_analyses)
        prompt_patterns = self.prompt_analyzer.extract_prompt_patterns(all_prompts)
        
        # Categorize PRs
        category_distribution = {}
        for pr_analysis in pr_analyses:
            category = pr_analysis.get('category', 'unknown')
            category_distribution[category] = category_distribution.get(category, 0) + 1
        
        return {
            'pr_analyses': pr_analyses,
            'iteration_summary': iteration_summary,
            'prompt_patterns': prompt_patterns,
            'category_distribution': category_distribution,
            'total_prompts_found': len(all_prompts),
        }
