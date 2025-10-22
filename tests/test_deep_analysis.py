"""
Integration test for deep analysis mode.
"""

import pytest
from unittest.mock import Mock, MagicMock
from datetime import datetime
from llmdev.config import Config
from llmdev.analyzer import RepositoryAnalyzer


class TestDeepAnalysis:
    """Test deep analysis integration."""
    
    def test_deep_analysis_enabled(self):
        """Test that deep analysis creates the required analyzers."""
        config = Config(deep_analysis=True)
        analyzer = RepositoryAnalyzer(config)
        
        assert analyzer.pr_analyzer is not None
        assert analyzer.iteration_analyzer is not None
        assert analyzer.prompt_analyzer is not None
    
    def test_deep_analysis_disabled(self):
        """Test that analyzers are not created when deep analysis is disabled."""
        config = Config(deep_analysis=False)
        analyzer = RepositoryAnalyzer(config)
        
        assert analyzer.pr_analyzer is None
        assert analyzer.iteration_analyzer is None
        assert analyzer.prompt_analyzer is None
    
    def test_run_deep_analysis(self):
        """Test the deep analysis execution."""
        config = Config(deep_analysis=True)
        analyzer = RepositoryAnalyzer(config)
        
        # Mock PR data
        prs_data = [
            {
                'number': 1,
                'title': 'Add new feature',
                'body': '## Problem\nNeed authentication\n\n- [x] Implement\n- [ ] Test',
                'created_at': datetime(2024, 1, 1),
                'merged_at': datetime(2024, 1, 2),
                'merged': True,
                'comments': [],
            },
            {
                'number': 2,
                'title': 'Fix bug',
                'body': 'Fixed the login bug',
                'created_at': datetime(2024, 1, 3),
                'merged_at': datetime(2024, 1, 3),
                'merged': True,
                'comments': [],
            }
        ]
        
        commits_data = []
        
        result = analyzer._run_deep_analysis(prs_data, commits_data)
        
        assert 'pr_analyses' in result
        assert 'iteration_summary' in result
        assert 'prompt_patterns' in result
        assert 'category_distribution' in result
        
        assert len(result['pr_analyses']) == 2
        assert result['category_distribution']['feature'] >= 1
        assert result['category_distribution']['fix'] >= 1
