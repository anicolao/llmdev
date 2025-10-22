"""
Iteration pattern detection - analyzes commit sequences and refinement patterns.
"""

import logging
from typing import Dict, List, Any, Optional
from datetime import datetime


logger = logging.getLogger(__name__)


class IterationAnalyzer:
    """Analyzes iteration patterns in PR development."""
    
    # Iteration patterns
    QUICK_WIN_THRESHOLD = 2  # commits
    MODERATE_THRESHOLD = 5   # commits
    
    def analyze_iterations(
        self, 
        pr_data: Dict[str, Any], 
        commits_data: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Analyze iteration patterns for a PR.
        
        Args:
            pr_data: PR data dictionary
            commits_data: List of commits in this PR
            
        Returns:
            Dictionary with iteration analysis
        """
        if not commits_data:
            return {
                'pattern_type': 'unknown',
                'commit_count': 0,
                'refinement_count': 0,
                'commit_sequence': [],
            }
        
        commit_count = len(commits_data)
        commit_sequence = self._extract_commit_sequence(commits_data)
        pattern_type = self._classify_iteration_pattern(commit_count, commit_sequence)
        refinement_count = self._count_refinements(commit_sequence)
        success_factors = self._analyze_success_factors(pr_data, commits_data)
        
        return {
            'pattern_type': pattern_type,
            'commit_count': commit_count,
            'refinement_count': refinement_count,
            'commit_sequence': commit_sequence,
            'success_factors': success_factors,
        }
    
    def _extract_commit_sequence(self, commits_data: List[Dict[str, Any]]) -> List[Dict[str, str]]:
        """
        Extract a simplified commit sequence with classifications.
        
        Args:
            commits_data: List of commit dictionaries
            
        Returns:
            List of commits with type classification
        """
        sequence = []
        
        for commit in commits_data:
            message = commit.get('message', '').lower()
            commit_type = self._classify_commit_message(message)
            
            sequence.append({
                'sha': commit.get('sha', '')[:8],
                'message': commit.get('message', '')[:100],  # Truncate
                'type': commit_type,
                'date': commit.get('date'),
            })
        
        return sequence
    
    def _classify_commit_message(self, message: str) -> str:
        """
        Classify a commit message by type.
        
        Types:
        - initial: Initial implementation or plan
        - fix: Bug fixes or corrections
        - refine: Improvements or refinements
        - test: Test-related changes
        - docs: Documentation changes
        - merge: Merge commits
        
        Args:
            message: Commit message text (lowercase)
            
        Returns:
            Commit type
        """
        # Check for merge commits
        if message.startswith('merge'):
            return 'merge'
        
        # Check for test commits (before initial, as "add tests" could match both)
        test_keywords = ['test', 'testing', 'spec']
        if any(keyword in message for keyword in test_keywords):
            return 'test'
        
        # Check for docs commits
        doc_keywords = ['doc', 'readme', 'comment']
        if any(keyword in message for keyword in doc_keywords):
            return 'docs'
        
        # Check for initial/plan commits
        initial_keywords = ['initial', 'add', 'create', 'implement', 'start', 'begin', 'wip']
        if any(keyword in message for keyword in initial_keywords):
            return 'initial'
        
        # Check for fix commits
        fix_keywords = ['fix', 'bug', 'error', 'issue', 'correct', 'repair', 'resolve']
        if any(keyword in message for keyword in fix_keywords):
            return 'fix'
        
        # Check for refinement commits
        refine_keywords = ['improve', 'enhance', 'refactor', 'optimize', 'update', 'polish']
        if any(keyword in message for keyword in refine_keywords):
            return 'refine'
        
        return 'other'
    
    def _classify_iteration_pattern(
        self, 
        commit_count: int, 
        commit_sequence: List[Dict[str, str]]
    ) -> str:
        """
        Classify the overall iteration pattern.
        
        Patterns:
        - quick_win: 1-2 commits, merged quickly
        - normal: 3-5 commits, standard refinement
        - complex: 6+ commits, significant iteration
        - plan_implement_fix: Clear sequence of plan -> implement -> fix
        
        Args:
            commit_count: Total number of commits
            commit_sequence: Sequence of commits with types
            
        Returns:
            Pattern type name
        """
        if commit_count <= self.QUICK_WIN_THRESHOLD:
            return 'quick_win'
        elif commit_count <= self.MODERATE_THRESHOLD:
            # Check for plan -> implement -> fix pattern
            if len(commit_sequence) >= 3:
                types = [c['type'] for c in commit_sequence[:3]]
                if 'initial' in types and 'fix' in types:
                    return 'plan_implement_fix'
            return 'normal'
        else:
            # Check if there are many fixes (struggling)
            fix_count = sum(1 for c in commit_sequence if c['type'] == 'fix')
            if fix_count >= commit_count // 2:
                return 'complex_with_corrections'
            return 'complex'
    
    def _count_refinements(self, commit_sequence: List[Dict[str, str]]) -> int:
        """
        Count the number of refinement-type commits.
        
        Args:
            commit_sequence: Sequence of commits
            
        Returns:
            Number of refinement commits
        """
        refine_types = {'fix', 'refine'}
        return sum(1 for c in commit_sequence if c['type'] in refine_types)
    
    def _analyze_success_factors(
        self, 
        pr_data: Dict[str, Any], 
        commits_data: List[Dict[str, Any]]
    ) -> List[str]:
        """
        Identify factors that contributed to success or difficulty.
        
        Args:
            pr_data: PR data
            commits_data: List of commits
            
        Returns:
            List of success/difficulty factors
        """
        factors = []
        
        # Check if PR has a detailed description
        body = pr_data.get('body', '')
        if body and len(body) > 500:
            factors.append('detailed_description')
        
        # Check if PR was merged
        if pr_data.get('merged'):
            factors.append('successfully_merged')
        
        # Check commit velocity
        if commits_data and len(commits_data) > 1:
            dates = [c.get('date') for c in commits_data if c.get('date')]
            if dates and len(dates) > 1:
                try:
                    # Parse dates if they're strings
                    parsed_dates = []
                    for d in dates:
                        if isinstance(d, str):
                            parsed_dates.append(datetime.fromisoformat(d.replace('Z', '+00:00')))
                        else:
                            parsed_dates.append(d)
                    
                    if len(parsed_dates) > 1:
                        time_span = (max(parsed_dates) - min(parsed_dates)).total_seconds() / 3600.0
                        commits_per_day = len(commits_data) / max((time_span / 24.0), 0.1)
                        
                        if commits_per_day > 5:
                            factors.append('rapid_iteration')
                        elif commits_per_day < 1:
                            factors.append('slow_iteration')
                except (ValueError, AttributeError, TypeError):
                    pass
        
        # Check for single commit (well-planned)
        if len(commits_data) == 1:
            factors.append('well_planned')
        
        return factors
    
    def get_iteration_summary(self, all_prs_analysis: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Generate summary statistics across all PRs.
        
        Args:
            all_prs_analysis: List of PR analysis results
            
        Returns:
            Summary dictionary with aggregate statistics
        """
        if not all_prs_analysis:
            return {
                'total_prs': 0,
                'pattern_distribution': {},
                'average_commits': 0,
                'average_refinements': 0,
            }
        
        pattern_counts = {}
        total_commits = 0
        total_refinements = 0
        
        for pr_analysis in all_prs_analysis:
            iterations = pr_analysis.get('iterations', {})
            pattern = iterations.get('pattern_type', 'unknown')
            pattern_counts[pattern] = pattern_counts.get(pattern, 0) + 1
            total_commits += iterations.get('commit_count', 0)
            total_refinements += iterations.get('refinement_count', 0)
        
        total_prs = len(all_prs_analysis)
        
        return {
            'total_prs': total_prs,
            'pattern_distribution': pattern_counts,
            'average_commits': total_commits / total_prs if total_prs > 0 else 0,
            'average_refinements': total_refinements / total_prs if total_prs > 0 else 0,
        }
