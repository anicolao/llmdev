"""
Tests for the new analyzers in MVP2.
"""

import pytest
from datetime import datetime
from llmdev.analyzers import PRAnalyzer, IterationAnalyzer, PromptAnalyzer


class TestPRAnalyzer:
    """Test cases for PRAnalyzer."""

    def test_extract_prompts_with_problem_section(self):
        """Test extraction of problem section from PR body."""
        analyzer = PRAnalyzer()

        body = """
## Problem
We need to add authentication to the API endpoint.

## Solution
Implement JWT-based authentication.
"""

        prompts = analyzer.extract_prompts(body)

        assert len(prompts) > 0
        assert any(p["type"] == "problem" for p in prompts)
        assert any("authentication" in p["content"].lower() for p in prompts)

    def test_extract_checklist(self):
        """Test checklist extraction from PR body."""
        analyzer = PRAnalyzer()

        body = """
- [x] Implement authentication
- [ ] Add tests
- [x] Update documentation
"""

        items = analyzer.extract_checklist(body)

        assert len(items) == 3
        assert items[0]["completed"] is True
        assert items[1]["completed"] is False
        assert "authentication" in items[0]["text"].lower()

    def test_categorize_pr_as_feature(self):
        """Test PR categorization as feature."""
        analyzer = PRAnalyzer()

        title = "Add new user authentication"
        body = "This PR implements a new feature for user authentication"

        category = analyzer.categorize_pr(title, body)

        assert category == "feature"

    def test_categorize_pr_as_fix(self):
        """Test PR categorization as fix."""
        analyzer = PRAnalyzer()

        title = "Fix broken login bug"
        body = "This PR fixes an issue with the login system"

        category = analyzer.categorize_pr(title, body)

        assert category == "fix"

    def test_categorize_pr_as_docs(self):
        """Test PR categorization as docs."""
        analyzer = PRAnalyzer()

        title = "Update README"
        body = "This PR updates the documentation"

        category = analyzer.categorize_pr(title, body)

        assert category == "docs"

    def test_analyze_pr_complete(self):
        """Test complete PR analysis."""
        analyzer = PRAnalyzer()

        pr_data = {
            "number": 42,
            "title": "Add new feature",
            "body": "## Problem\nWe need this feature.\n\n- [x] Implement\n- [ ] Test",
            "created_at": datetime(2024, 1, 1, 10, 0),
            "merged_at": datetime(2024, 1, 1, 14, 0),
            "merged": True,
        }

        commits = [
            {
                "sha": "abc123",
                "message": "Initial implementation",
                "date": datetime(2024, 1, 1, 10, 30),
            },
            {"sha": "def456", "message": "Fix bug", "date": datetime(2024, 1, 1, 12, 0)},
        ]

        result = analyzer.analyze_pr(pr_data, commits)

        assert result["number"] == 42
        assert result["category"] == "feature"
        assert result["iteration_count"] == 2
        assert result["time_to_merge_hours"] == 4.0
        assert len(result["checklist_items"]) == 2
        assert result["complexity_score"] > 0


class TestIterationAnalyzer:
    """Test cases for IterationAnalyzer."""

    def test_classify_quick_win(self):
        """Test classification of quick win pattern."""
        analyzer = IterationAnalyzer()

        pr_data = {"number": 1, "merged": True}
        commits = [{"sha": "abc", "message": "Implement feature", "date": datetime.now()}]

        result = analyzer.analyze_iterations(pr_data, commits)

        assert result["pattern_type"] == "quick_win"
        assert result["commit_count"] == 1

    def test_classify_complex(self):
        """Test classification of complex pattern."""
        analyzer = IterationAnalyzer()

        pr_data = {"number": 1, "merged": True}
        commits = [
            {"sha": "a", "message": "Initial", "date": datetime.now()},
            {"sha": "b", "message": "Fix", "date": datetime.now()},
            {"sha": "c", "message": "Fix again", "date": datetime.now()},
            {"sha": "d", "message": "Another fix", "date": datetime.now()},
            {"sha": "e", "message": "Yet another fix", "date": datetime.now()},
            {"sha": "f", "message": "Final fix", "date": datetime.now()},
        ]

        result = analyzer.analyze_iterations(pr_data, commits)

        assert result["pattern_type"] in ["complex", "complex_with_corrections"]
        assert result["commit_count"] == 6

    def test_classify_commit_message_types(self):
        """Test commit message classification."""
        analyzer = IterationAnalyzer()

        assert analyzer._classify_commit_message("initial implementation") == "initial"
        assert analyzer._classify_commit_message("fix bug") == "fix"
        assert analyzer._classify_commit_message("improve performance") == "refine"
        assert analyzer._classify_commit_message("add tests") == "test"
        assert analyzer._classify_commit_message("update readme") == "docs"
        assert analyzer._classify_commit_message("merge branch") == "merge"

    def test_iteration_summary(self):
        """Test iteration summary generation."""
        analyzer = IterationAnalyzer()

        pr_analyses = [
            {"iterations": {"pattern_type": "quick_win", "commit_count": 1, "refinement_count": 0}},
            {"iterations": {"pattern_type": "normal", "commit_count": 3, "refinement_count": 1}},
            {"iterations": {"pattern_type": "complex", "commit_count": 6, "refinement_count": 3}},
        ]

        summary = analyzer.get_iteration_summary(pr_analyses)

        assert summary["total_prs"] == 3
        assert summary["average_commits"] == (1 + 3 + 6) / 3
        assert summary["average_refinements"] == (0 + 1 + 3) / 3
        assert "quick_win" in summary["pattern_distribution"]


class TestPromptAnalyzer:
    """Test cases for PromptAnalyzer."""

    def test_measure_specificity_high(self):
        """Test specificity measurement for detailed prompt."""
        analyzer = PromptAnalyzer()

        prompt = """
Implement a function called `authenticate_user` that takes username and password 
parameters and returns a JWT token. The function should:
1. Validate credentials against the database
2. Generate a token with 24-hour expiration
3. Include user_id and role in the token payload
"""

        score = analyzer._measure_specificity(prompt)

        assert score > 0.5  # Should be considered specific

    def test_measure_specificity_low(self):
        """Test specificity measurement for vague prompt."""
        analyzer = PromptAnalyzer()

        prompt = "Make it better"

        score = analyzer._measure_specificity(prompt)

        assert score < 0.3  # Should be considered vague

    def test_check_for_context(self):
        """Test context detection."""
        analyzer = PromptAnalyzer()

        with_context = "The current system has a bug because the validation is missing"
        without_context = "Add validation"

        assert analyzer._check_for_context(with_context) is True
        assert analyzer._check_for_context(without_context) is False

    def test_check_for_constraints(self):
        """Test constraint detection."""
        analyzer = PromptAnalyzer()

        with_constraints = "Must complete within 100ms and should not use more than 10MB memory"
        without_constraints = "Make it faster"

        assert analyzer._check_for_constraints(with_constraints) is True
        assert analyzer._check_for_constraints(without_constraints) is False

    def test_check_for_examples(self):
        """Test example detection."""
        analyzer = PromptAnalyzer()

        with_examples = "For example: `authenticate('user', 'pass')` should return a token"
        without_examples = "Add authentication"

        assert analyzer._check_for_examples(with_examples) is True
        assert analyzer._check_for_examples(without_examples) is False

    def test_analyze_tone(self):
        """Test tone analysis."""
        analyzer = PromptAnalyzer()

        imperative = "Implement the feature. Add tests. Fix the bug."
        collaborative = "We could add a feature here. Perhaps we should consider testing?"

        assert analyzer._analyze_tone(imperative) == "imperative"
        assert analyzer._analyze_tone(collaborative) == "collaborative"

    def test_analyze_prompt_complete(self):
        """Test complete prompt analysis."""
        analyzer = PromptAnalyzer()

        prompt = """
## Problem
The authentication system is broken because tokens expire too quickly.

## Solution
We need to implement a refresh token mechanism. The implementation should:
1. Generate both access and refresh tokens
2. Access tokens expire in 15 minutes
3. Refresh tokens expire in 7 days

Example usage:
```python
tokens = generate_tokens(user_id)
# Returns: {"access": "...", "refresh": "..."}
```
"""

        outcome = {
            "iteration_count": 2,
            "complexity_score": 3,
            "merged": True,
        }

        result = analyzer.analyze_prompt(prompt, outcome)

        assert result["specificity_score"] > 0.5
        assert result["has_context"] is True
        assert result["has_constraints"] is True
        assert result["has_examples"] is True
        assert result["word_count"] > 0
        assert result["effectiveness"] in ["highly_effective", "effective"]

    def test_extract_prompt_patterns(self):
        """Test pattern extraction from multiple prompts."""
        analyzer = PromptAnalyzer()

        prompts = [
            {
                "specificity_score": 0.8,
                "has_context": True,
                "has_constraints": True,
                "has_examples": True,
            },
            {
                "specificity_score": 0.6,
                "has_context": True,
                "has_constraints": False,
                "has_examples": False,
            },
            {
                "specificity_score": 0.4,
                "has_context": False,
                "has_constraints": False,
                "has_examples": False,
            },
        ]

        patterns = analyzer.extract_prompt_patterns(prompts)

        assert patterns["total_prompts"] == 3
        assert patterns["average_specificity"] == pytest.approx(0.6, rel=0.1)
        assert patterns["context_percentage"] == pytest.approx(66.67, rel=0.1)
        assert patterns["constraints_percentage"] == pytest.approx(33.33, rel=0.1)
