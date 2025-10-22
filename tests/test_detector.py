"""
Tests for the Copilot detector.
"""

import pytest
from llmdev.detector import CopilotDetector, Detection


class TestCopilotDetector:
    """Test cases for CopilotDetector."""
    
    def test_detect_explicit_mention_in_text(self):
        """Test detection of explicit Copilot mentions."""
        detector = CopilotDetector()
        
        text = "This code was generated using GitHub Copilot"
        detections = detector.detect_in_text(text, 'commit', 'abc123')
        
        assert len(detections) > 0
        assert detections[0].detection_type == 'explicit_mention'
        assert detections[0].confidence > 0.9
        assert 'copilot' in detections[0].evidence.lower()
    
    def test_no_detection_in_clean_text(self):
        """Test that clean text produces no detections."""
        detector = CopilotDetector()
        
        text = "This is a regular commit message"
        detections = detector.detect_in_text(text, 'commit', 'abc123')
        
        assert len(detections) == 0
    
    def test_detect_in_commit(self):
        """Test Copilot detection in commit data."""
        detector = CopilotDetector()
        
        commit_data = {
            'sha': 'abc123',
            'message': 'Fix bug with copilot assistance',
            'author': 'developer'
        }
        
        detections = detector.detect_in_commit(commit_data)
        
        assert len(detections) > 0
        assert detections[0].source_type == 'commit'
        assert detections[0].source_id == 'abc123'
    
    def test_detect_in_pr(self):
        """Test Copilot detection in PR data."""
        detector = CopilotDetector()
        
        pr_data = {
            'number': 42,
            'title': 'Add new feature',
            'body': 'This PR was created with GitHub Copilot',
            'comments': []
        }
        
        detections = detector.detect_in_pr(pr_data)
        
        assert len(detections) > 0
        assert detections[0].source_type == 'pr'
        assert detections[0].source_id == '42'
    
    def test_detect_in_issue(self):
        """Test Copilot detection in issue data."""
        detector = CopilotDetector()
        
        issue_data = {
            'number': 10,
            'title': 'Bug in copilot-generated code',
            'body': 'Description here',
            'comments': []
        }
        
        detections = detector.detect_in_issue(issue_data)
        
        assert len(detections) > 0
        assert detections[0].source_type == 'issue'
        assert detections[0].source_id == '10'
    
    def test_case_insensitive_detection(self):
        """Test that detection is case-insensitive by default."""
        detector = CopilotDetector()
        
        # Different case variations
        texts = [
            'using COPILOT',
            'Using Copilot',
            'using copilot',
            'USING GITHUB COPILOT'
        ]
        
        for text in texts:
            detections = detector.detect_in_text(text, 'test', 'test1')
            assert len(detections) > 0, f"Failed to detect: {text}"
    
    def test_get_summary(self):
        """Test summary generation from detections."""
        detector = CopilotDetector()
        
        detections = [
            Detection('commit', '1', 'explicit_mention', 0.95, 'test1'),
            Detection('commit', '2', 'explicit_mention', 0.90, 'test2'),
            Detection('pr', '3', 'explicit_mention', 0.95, 'test3'),
            Detection('issue', '4', 'explicit_mention', 0.85, 'test4'),
        ]
        
        summary = detector.get_summary(detections)
        
        assert summary['total'] == 4
        assert summary['by_source']['commit'] == 2
        assert summary['by_source']['pr'] == 1
        assert summary['by_source']['issue'] == 1
        assert summary['by_type']['explicit_mention'] == 4
        assert 0 < summary['average_confidence'] <= 1.0
    
    def test_empty_summary(self):
        """Test summary with no detections."""
        detector = CopilotDetector()
        
        summary = detector.get_summary([])
        
        assert summary['total'] == 0
        assert summary['average_confidence'] == 0.0
