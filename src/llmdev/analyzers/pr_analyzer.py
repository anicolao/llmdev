"""
Deep PR content analysis - extracts prompts, problems, solutions, and checklists.
"""

import re
import logging
from typing import Dict, List, Any, Optional
from datetime import datetime


logger = logging.getLogger(__name__)


class PRAnalyzer:
    """Analyzes PR content to extract development context and patterns."""
    
    # PR category keywords
    CATEGORY_KEYWORDS = {
        'vision': ['design', 'planning', 'architecture', 'vision', 'proposal', 'RFC'],
        'foundation': ['core', 'infrastructure', 'setup', 'initial', 'base', 'framework'],
        'feature': ['add', 'implement', 'create', 'new feature', 'introduce'],
        'fix': ['fix', 'bug', 'issue', 'broken', 'repair', 'resolve', 'correct'],
        'refine': ['improve', 'enhance', 'polish', 'refactor', 'optimize', 'better'],
        'docs': ['readme', 'documentation', 'guide', 'docs', 'comment', 'docstring'],
    }
    
    def analyze_pr(self, pr_data: Dict[str, Any], commits_data: Optional[List[Dict]] = None) -> Dict[str, Any]:
        """
        Perform deep analysis of a pull request.
        
        Args:
            pr_data: PR data dictionary with title, body, comments, etc.
            commits_data: Optional list of commits in this PR
            
        Returns:
            Dictionary with comprehensive PR analysis
        """
        body = pr_data.get('body', '')
        title = pr_data.get('title', '')
        created_at = pr_data.get('created_at')
        merged_at = pr_data.get('merged_at')
        updated_at = pr_data.get('updated_at')
        
        # Extract various components
        prompts = self.extract_prompts(body)
        problem = self.extract_problem_statement(body)
        solution = self.extract_solution_approach(body)
        checklist_items = self.extract_checklist(body)
        
        # Calculate metrics
        iteration_count = len(commits_data) if commits_data else 0
        time_to_merge = self._calculate_duration(created_at, merged_at or updated_at)
        
        # Categorize PR
        category = self.categorize_pr(title, body)
        
        # Assess complexity
        complexity = self._assess_complexity(
            iteration_count, 
            time_to_merge, 
            len(checklist_items),
            len(body) if body else 0
        )
        
        return {
            'number': pr_data.get('number'),
            'title': title,
            'category': category,
            'prompt_extraction': prompts,
            'problem_statement': problem,
            'solution_approach': solution,
            'checklist_items': checklist_items,
            'iteration_count': iteration_count,
            'time_to_merge_hours': time_to_merge,
            'complexity_score': complexity['score'],
            'complexity_indicators': complexity['indicators'],
            'created_at': created_at,
            'merged_at': merged_at,
        }
    
    def extract_prompts(self, text: str) -> List[Dict[str, str]]:
        """
        Extract prompt-like sections from PR body.
        
        Looks for sections like:
        - "## Problem"
        - "Task Request:"
        - Quoted sections that look like instructions
        
        Args:
            text: PR body text
            
        Returns:
            List of extracted prompts with type and content
        """
        if not text:
            return []
        
        prompts = []
        
        # Look for markdown headers that indicate prompts/problems/tasks
        patterns = [
            (r'##\s*(Problem|Issue|Task|Request|Objective|Goal)[:\s]*\n(.*?)(?=\n##|\Z)', 'problem'),
            (r'##\s*(Solution|Approach|Implementation)[:\s]*\n(.*?)(?=\n##|\Z)', 'solution'),
            (r'##\s*(Context|Background)[:\s]*\n(.*?)(?=\n##|\Z)', 'context'),
            (r'Task Request[:\s]*\n(.*?)(?=\n\n|\Z)', 'task_request'),
            (r'Prompt[:\s]*\n(.*?)(?=\n\n|\Z)', 'explicit_prompt'),
        ]
        
        for pattern, prompt_type in patterns:
            matches = re.finditer(pattern, text, re.IGNORECASE | re.DOTALL)
            for match in matches:
                content = match.group(2) if match.lastindex >= 2 else match.group(1)
                content = content.strip()
                if content and len(content) > 20:  # Meaningful content
                    prompts.append({
                        'type': prompt_type,
                        'content': content[:500],  # Limit length
                    })
        
        return prompts
    
    def extract_problem_statement(self, text: str) -> Optional[str]:
        """
        Extract the problem statement from PR body.
        
        Args:
            text: PR body text
            
        Returns:
            Problem statement if found, None otherwise
        """
        if not text:
            return None
        
        # Look for problem/issue sections
        patterns = [
            r'##\s*Problem[:\s]*\n(.*?)(?=\n##|\Z)',
            r'##\s*Issue[:\s]*\n(.*?)(?=\n##|\Z)',
            r'##\s*Description[:\s]*\n(.*?)(?=\n##|\Z)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
            if match:
                problem = match.group(1).strip()
                if problem and len(problem) > 20:
                    return problem[:500]  # Limit length
        
        # If no explicit section, use first substantial paragraph
        paragraphs = text.split('\n\n')
        for para in paragraphs[:3]:  # Check first 3 paragraphs
            para = para.strip()
            if para and len(para) > 50 and not para.startswith('#'):
                return para[:500]
        
        return None
    
    def extract_solution_approach(self, text: str) -> Optional[str]:
        """
        Extract the solution approach from PR body.
        
        Args:
            text: PR body text
            
        Returns:
            Solution approach if found, None otherwise
        """
        if not text:
            return None
        
        patterns = [
            r'##\s*Solution[:\s]*\n(.*?)(?=\n##|\Z)',
            r'##\s*Approach[:\s]*\n(.*?)(?=\n##|\Z)',
            r'##\s*Implementation[:\s]*\n(.*?)(?=\n##|\Z)',
            r'##\s*Changes[:\s]*\n(.*?)(?=\n##|\Z)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
            if match:
                solution = match.group(1).strip()
                if solution and len(solution) > 20:
                    return solution[:500]
        
        return None
    
    def extract_checklist(self, text: str) -> List[Dict[str, Any]]:
        """
        Extract checklist items from PR body.
        
        Args:
            text: PR body text
            
        Returns:
            List of checklist items with completion status
        """
        if not text:
            return []
        
        checklist_items = []
        
        # Match markdown checklist items: - [ ] or - [x]
        pattern = r'^\s*-\s*\[([xX\s])\]\s*(.+)$'
        
        for line in text.split('\n'):
            match = re.match(pattern, line)
            if match:
                checked = match.group(1).strip().lower() == 'x'
                item_text = match.group(2).strip()
                checklist_items.append({
                    'text': item_text,
                    'completed': checked,
                })
        
        return checklist_items
    
    def categorize_pr(self, title: str, body: str) -> str:
        """
        Categorize PR based on title and body content.
        
        Categories:
        - vision: Design, planning, architecture
        - foundation: Core infrastructure, setup
        - feature: New functionality
        - fix: Bug fixes, repairs
        - refine: Improvements, optimizations
        - docs: Documentation updates
        
        Args:
            title: PR title
            body: PR body text
            
        Returns:
            Category name
        """
        combined_text = f"{title} {body}".lower()
        
        # Count keyword matches for each category
        category_scores = {}
        for category, keywords in self.CATEGORY_KEYWORDS.items():
            score = sum(1 for keyword in keywords if keyword.lower() in combined_text)
            category_scores[category] = score
        
        # Return category with highest score, default to 'feature'
        if max(category_scores.values()) > 0:
            return max(category_scores.items(), key=lambda x: x[1])[0]
        
        return 'feature'
    
    def _calculate_duration(self, start_time: Any, end_time: Any) -> float:
        """
        Calculate duration between two timestamps in hours.
        
        Args:
            start_time: Start timestamp
            end_time: End timestamp
            
        Returns:
            Duration in hours, or 0 if times are invalid
        """
        if not start_time or not end_time:
            return 0.0
        
        try:
            if isinstance(start_time, str):
                start_time = datetime.fromisoformat(start_time.replace('Z', '+00:00'))
            if isinstance(end_time, str):
                end_time = datetime.fromisoformat(end_time.replace('Z', '+00:00'))
            
            delta = end_time - start_time
            return delta.total_seconds() / 3600.0
        except (ValueError, AttributeError, TypeError):
            return 0.0
    
    def _assess_complexity(
        self, 
        iteration_count: int, 
        time_to_merge: float,
        checklist_count: int,
        body_length: int
    ) -> Dict[str, Any]:
        """
        Assess PR complexity based on multiple indicators.
        
        Args:
            iteration_count: Number of commits
            time_to_merge: Hours to merge
            checklist_count: Number of checklist items
            body_length: Length of PR body
            
        Returns:
            Dictionary with complexity score and indicators
        """
        score = 0
        indicators = []
        
        # Iteration count scoring
        if iteration_count >= 6:
            score += 3
            indicators.append('high_iteration_count')
        elif iteration_count >= 3:
            score += 2
            indicators.append('moderate_iteration_count')
        elif iteration_count == 1:
            score += 0
            indicators.append('quick_win')
        else:
            score += 1
        
        # Time to merge scoring
        if time_to_merge > 72:  # > 3 days
            score += 3
            indicators.append('long_duration')
        elif time_to_merge > 24:  # > 1 day
            score += 2
            indicators.append('moderate_duration')
        elif time_to_merge < 8:  # < 8 hours
            score += 0
            indicators.append('fast_merge')
        else:
            score += 1
        
        # Checklist complexity
        if checklist_count > 20:
            score += 2
            indicators.append('extensive_checklist')
        elif checklist_count > 10:
            score += 1
            indicators.append('moderate_checklist')
        
        # Body length (detailed description)
        if body_length > 2000:
            score += 1
            indicators.append('detailed_description')
        
        # Classify overall complexity
        if score >= 6:
            complexity_level = 'high'
        elif score >= 3:
            complexity_level = 'moderate'
        else:
            complexity_level = 'low'
        
        return {
            'score': score,
            'level': complexity_level,
            'indicators': indicators,
        }
