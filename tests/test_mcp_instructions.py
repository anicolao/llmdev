"""
Tests for MCP instructions generator.
"""

import pytest
from pathlib import Path
import tempfile
import os

from llmdev.mcp_instructions import MCPInstructionsGenerator


class TestMCPInstructionsGenerator:
    """Test MCP instructions generation."""

    def test_generate_instructions(self):
        """Test generating instructions for a repository."""
        with tempfile.TemporaryDirectory() as tmpdir:
            generator = MCPInstructionsGenerator(Path(tmpdir))
            
            output_path = generator.generate("test-owner", "test-repo")
            
            # Verify file was created
            assert output_path.exists()
            assert output_path.name == "ANALYZE_TEST-OWNER_TEST-REPO.md"
            
            # Verify content
            content = output_path.read_text()
            assert "test-owner/test-repo" in content
            assert "Analysis Instructions" in content
            assert "Phase 1:" in content
            assert "Phase 2:" in content
            assert "Repository Overview" in content
            assert "LLM Usage Patterns" in content
            assert "Development Story Arc" in content
            assert "Prompt Analysis" in content

    def test_generate_batch_instructions(self):
        """Test generating instructions for multiple repositories."""
        with tempfile.TemporaryDirectory() as tmpdir:
            generator = MCPInstructionsGenerator(Path(tmpdir))
            
            repositories = [
                ("owner1", "repo1"),
                ("owner2", "repo2"),
            ]
            
            results = generator.generate_batch_instructions(repositories)
            
            assert len(results) == 2
            assert "owner1/repo1" in results
            assert "owner2/repo2" in results
            
            # Verify both files exist
            for path in results.values():
                assert path.exists()

    def test_output_directory_creation(self):
        """Test that output directory is created if it doesn't exist."""
        with tempfile.TemporaryDirectory() as tmpdir:
            nested_dir = Path(tmpdir) / "nested" / "output"
            generator = MCPInstructionsGenerator(nested_dir)
            
            output_path = generator.generate("test-owner", "test-repo")
            
            assert nested_dir.exists()
            assert output_path.exists()

    def test_instructions_content_structure(self):
        """Test that generated instructions have expected structure."""
        with tempfile.TemporaryDirectory() as tmpdir:
            generator = MCPInstructionsGenerator(Path(tmpdir))
            output_path = generator.generate("example-owner", "example-repo")
            
            content = output_path.read_text()
            
            # Check for major sections
            required_sections = [
                "# Analysis Instructions for example-owner/example-repo",
                "## Background",
                "## Prerequisites",
                "## Analysis Steps",
                "### Phase 1: Repository Overview",
                "### Phase 2: Detect LLM Usage Patterns",
                "### Phase 3: Extract Development Story Arc",
                "### Phase 4: Analyze Prompts and Requests",
                "### Phase 5: Iteration Pattern Analysis",
                "### Phase 6: Identify Development Patterns",
                "### Phase 7: Best Practices and Recommendations",
                "### Phase 8: Final Synthesis",
                "## Output Format",
                "## Tips for Success",
                "## Rate Limit Management",
            ]
            
            for section in required_sections:
                assert section in content, f"Missing section: {section}"

    def test_instructions_include_examples(self):
        """Test that instructions include helpful examples and templates."""
        with tempfile.TemporaryDirectory() as tmpdir:
            generator = MCPInstructionsGenerator(Path(tmpdir))
            output_path = generator.generate("test-owner", "test-repo")
            
            content = output_path.read_text()
            
            # Check for example content
            assert "case_studies/GITHUB_ANICOLAO_DIKUCLIENT.md" in content
            assert "Problem-Context-Solution" in content
            assert "Quick Win" in content
            assert "## Executive Summary" in content
            assert "**Output:**" in content  # Task outputs are specified

    def test_instructions_mention_mcp_benefits(self):
        """Test that instructions explain MCP advantages."""
        with tempfile.TemporaryDirectory() as tmpdir:
            generator = MCPInstructionsGenerator(Path(tmpdir))
            output_path = generator.generate("test-owner", "test-repo")
            
            content = output_path.read_text()
            
            # Check for MCP-related content
            assert "MCP" in content or "Model Context Protocol" in content
            assert "rate limit" in content.lower()
            assert "GitHub server" in content or "github server" in content.lower()
