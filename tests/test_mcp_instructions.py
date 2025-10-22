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

    def test_generate_phase_instructions(self):
        """Test generating phase-specific instructions."""
        with tempfile.TemporaryDirectory() as tmpdir:
            generator = MCPInstructionsGenerator(Path(tmpdir))
            
            # Test intro phase
            output_path = generator.generate("test-owner", "test-repo", phase="intro")
            
            # Verify file naming
            assert output_path.name == "ANALYZE_TEST-OWNER_TEST-REPO_PHASE_INTRO.md"
            assert output_path.exists()
            
            # Verify content is phase-specific
            content = output_path.read_text()
            assert "Introduction" in content
            assert "Analysis Workflow" in content
            assert "intro" in content.lower()
            # Should guide to next phase
            assert "overview" in content.lower()

    def test_all_phases_generate_correctly(self):
        """Test that all defined phases can be generated."""
        with tempfile.TemporaryDirectory() as tmpdir:
            generator = MCPInstructionsGenerator(Path(tmpdir))
            
            phases = MCPInstructionsGenerator.PHASES
            
            for phase in phases:
                output_path = generator.generate("test-owner", "test-repo", phase=phase)
                
                # Verify file exists
                assert output_path.exists()
                
                # Verify file naming
                expected_name = f"ANALYZE_TEST-OWNER_TEST-REPO_PHASE_{phase.upper()}.md"
                assert output_path.name == expected_name
                
                # Verify content has reasonable length (phase-specific, not full doc)
                content = output_path.read_text()
                assert len(content) > 100  # Not empty
                assert len(content) < 15000  # Not the full multi-phase document
                
                # Verify phase-specific title
                assert phase in content.lower() or phase.title() in content

    def test_invalid_phase_raises_error(self):
        """Test that invalid phase name raises ValueError."""
        with tempfile.TemporaryDirectory() as tmpdir:
            generator = MCPInstructionsGenerator(Path(tmpdir))
            
            with pytest.raises(ValueError) as exc_info:
                generator.generate("test-owner", "test-repo", phase="invalid-phase")
            
            assert "Invalid phase" in str(exc_info.value)
            assert "invalid-phase" in str(exc_info.value)

    def test_phase_instructions_are_shorter_than_full(self):
        """Test that phase instructions are significantly shorter than full instructions."""
        with tempfile.TemporaryDirectory() as tmpdir:
            generator = MCPInstructionsGenerator(Path(tmpdir))
            
            # Generate full instructions
            full_path = generator.generate("test-owner", "test-repo")
            full_content = full_path.read_text()
            full_length = len(full_content)
            
            # Generate phase instruction
            phase_path = generator.generate("test-owner", "test-repo", phase="overview")
            phase_content = phase_path.read_text()
            phase_length = len(phase_content)
            
            # Phase should be shorter than full (less than 40%)
            assert phase_length < full_length * 0.4
            assert phase_length > 500  # But still substantial

    def test_phase_progression_guidance(self):
        """Test that each phase guides to the next phase."""
        with tempfile.TemporaryDirectory() as tmpdir:
            generator = MCPInstructionsGenerator(Path(tmpdir))
            
            phases = MCPInstructionsGenerator.PHASES
            
            for i, phase in enumerate(phases[:-1]):  # All except last
                output_path = generator.generate("test-owner", "test-repo", phase=phase)
                content = output_path.read_text()
                
                # Should mention the next phase
                next_phase = phases[i + 1]
                assert next_phase in content.lower()
                assert "next" in content.lower() or "proceed" in content.lower()

    def test_final_phase_indicates_completion(self):
        """Test that the final phase indicates completion."""
        with tempfile.TemporaryDirectory() as tmpdir:
            generator = MCPInstructionsGenerator(Path(tmpdir))
            
            # Generate final phase (synthesis)
            final_phase = MCPInstructionsGenerator.PHASES[-1]
            output_path = generator.generate("test-owner", "test-repo", phase=final_phase)
            content = output_path.read_text()
            
            # Should indicate completion
            assert "final" in content.lower() or "complete" in content.lower()
            assert "case study" in content.lower()
