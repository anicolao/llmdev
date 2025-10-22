"""
Prompt extraction and analysis - studies prompt effectiveness.
"""

import re
import logging
from typing import Dict, List, Any, Optional


logger = logging.getLogger(__name__)


class PromptAnalyzer:
    """Analyzes prompts to understand effectiveness patterns."""
    
    def analyze_prompt(self, prompt_text: str, outcome_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Analyze a prompt for characteristics and effectiveness.
        
        Args:
            prompt_text: The prompt text to analyze
            outcome_data: Optional outcome information (iterations, success, etc.)
            
        Returns:
            Dictionary with prompt analysis
        """
        if not prompt_text:
            return {
                'specificity_score': 0,
                'has_context': False,
                'has_constraints': False,
                'has_examples': False,
                'word_count': 0,
            }
        
        specificity = self._measure_specificity(prompt_text)
        has_context = self._check_for_context(prompt_text)
        has_constraints = self._check_for_constraints(prompt_text)
        has_examples = self._check_for_examples(prompt_text)
        word_count = len(prompt_text.split())
        tone = self._analyze_tone(prompt_text)
        
        analysis = {
            'specificity_score': specificity,
            'has_context': has_context,
            'has_constraints': has_constraints,
            'has_examples': has_examples,
            'word_count': word_count,
            'tone': tone,
        }
        
        # Add effectiveness correlation if outcome data provided
        if outcome_data:
            analysis['effectiveness'] = self._correlate_with_outcome(analysis, outcome_data)
        
        return analysis
    
    def _measure_specificity(self, text: str) -> float:
        """
        Measure how specific/detailed a prompt is.
        
        Factors:
        - Presence of technical terms
        - Specific numbers/values
        - File/path references
        - Concrete examples
        
        Args:
            text: Prompt text
            
        Returns:
            Specificity score from 0.0 to 1.0
        """
        score = 0.0
        text_lower = text.lower()
        
        # Technical indicators
        tech_patterns = [
            r'\b(function|class|method|variable|parameter|return|type)\b',
            r'\b(implement|create|add|update|modify|refactor)\b',
            r'\b(bug|error|issue|fix|resolve)\b',
            r'\bfile\s+\w+\.\w+\b',  # File references
            r'\bpath[:\s]+[/\w]+',  # Path references
        ]
        
        for pattern in tech_patterns:
            if re.search(pattern, text_lower):
                score += 0.15
        
        # Specific numbers or values
        if re.search(r'\b\d+\b', text):
            score += 0.1
        
        # Code blocks
        if '```' in text or '`' in text:
            score += 0.2
        
        # Lists or bullet points (structured)
        if re.search(r'^\s*[-*]\s+', text, re.MULTILINE) or re.search(r'^\s*\d+\.\s+', text, re.MULTILINE):
            score += 0.15
        
        # Detailed description (length)
        if len(text) > 200:
            score += 0.1
        if len(text) > 500:
            score += 0.1
        
        return min(score, 1.0)
    
    def _check_for_context(self, text: str) -> bool:
        """
        Check if prompt provides context or background.
        
        Args:
            text: Prompt text
            
        Returns:
            True if context is present
        """
        context_indicators = [
            r'\b(context|background|currently|existing|previous)\b',
            r'\b(because|since|due to|reason)\b',
            r'\b(problem|issue|challenge)\b',
            r'##\s*(context|background)',
        ]
        
        text_lower = text.lower()
        return any(re.search(pattern, text_lower) for pattern in context_indicators)
    
    def _check_for_constraints(self, text: str) -> bool:
        """
        Check if prompt specifies constraints or requirements.
        
        Args:
            text: Prompt text
            
        Returns:
            True if constraints are present
        """
        constraint_indicators = [
            r'\b(must|should|need|require|constraint|requirement)\b',
            r'\b(without|avoid|don\'t|cannot)\b',
            r'\b(within|under|less than|more than|at least)\b',
            r'##\s*(requirements|constraints)',
        ]
        
        text_lower = text.lower()
        return any(re.search(pattern, text_lower) for pattern in constraint_indicators)
    
    def _check_for_examples(self, text: str) -> bool:
        """
        Check if prompt includes examples.
        
        Args:
            text: Prompt text
            
        Returns:
            True if examples are present
        """
        example_indicators = [
            r'\b(example|e\.g\.|for instance|such as|like)\b',
            r'```',  # Code blocks
            r'##\s*example',
        ]
        
        text_lower = text.lower()
        return any(re.search(pattern, text_lower) for pattern in example_indicators)
    
    def _analyze_tone(self, text: str) -> str:
        """
        Analyze the tone of the prompt.
        
        Tones:
        - imperative: Direct commands
        - collaborative: Suggestions and questions
        - descriptive: Explaining what's needed
        
        Args:
            text: Prompt text
            
        Returns:
            Tone classification
        """
        text_lower = text.lower()
        
        # Count imperative indicators
        imperative_count = len(re.findall(
            r'\b(implement|create|add|fix|update|change|make|do)\b', 
            text_lower
        ))
        
        # Count collaborative indicators
        collaborative_count = len(re.findall(
            r'\b(should|could|would|might|perhaps|consider|suggest)\b', 
            text_lower
        ))
        
        # Count question marks
        question_count = text.count('?')
        
        if imperative_count > collaborative_count + question_count:
            return 'imperative'
        elif collaborative_count > 0 or question_count > 0:
            return 'collaborative'
        else:
            return 'descriptive'
    
    def _correlate_with_outcome(
        self, 
        prompt_analysis: Dict[str, Any], 
        outcome_data: Dict[str, Any]
    ) -> str:
        """
        Correlate prompt characteristics with outcome success.
        
        Args:
            prompt_analysis: Analysis of the prompt
            outcome_data: Outcome information (iterations, time, success)
            
        Returns:
            Effectiveness rating
        """
        # Extract outcome metrics
        iterations = outcome_data.get('iteration_count', 0)
        complexity = outcome_data.get('complexity_score', 0)
        merged = outcome_data.get('merged', False)
        
        # Good outcome: few iterations, merged successfully
        is_good_outcome = iterations <= 3 and merged
        
        # Bad outcome: many iterations or not merged
        is_bad_outcome = iterations >= 6 or not merged
        
        # Effective prompts tend to be specific with context
        is_detailed_prompt = (
            prompt_analysis['specificity_score'] > 0.5 and
            prompt_analysis['has_context']
        )
        
        if is_good_outcome and is_detailed_prompt:
            return 'highly_effective'
        elif is_good_outcome:
            return 'effective'
        elif is_bad_outcome and not is_detailed_prompt:
            return 'ineffective'
        elif is_bad_outcome:
            return 'challenging_problem'
        else:
            return 'moderate'
    
    def extract_prompt_patterns(self, all_prompts: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Extract common patterns from a collection of prompts.
        
        Args:
            all_prompts: List of prompt analyses
            
        Returns:
            Dictionary with pattern statistics
        """
        if not all_prompts:
            return {
                'total_prompts': 0,
                'average_specificity': 0,
                'context_percentage': 0,
                'constraints_percentage': 0,
                'examples_percentage': 0,
            }
        
        total = len(all_prompts)
        total_specificity = sum(p.get('specificity_score', 0) for p in all_prompts)
        context_count = sum(1 for p in all_prompts if p.get('has_context', False))
        constraints_count = sum(1 for p in all_prompts if p.get('has_constraints', False))
        examples_count = sum(1 for p in all_prompts if p.get('has_examples', False))
        
        return {
            'total_prompts': total,
            'average_specificity': total_specificity / total if total > 0 else 0,
            'context_percentage': (context_count / total * 100) if total > 0 else 0,
            'constraints_percentage': (constraints_count / total * 100) if total > 0 else 0,
            'examples_percentage': (examples_count / total * 100) if total > 0 else 0,
        }
