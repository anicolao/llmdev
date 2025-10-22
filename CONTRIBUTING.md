# Contributing to llmdev

Thank you for your interest in contributing to llmdev! This document provides guidelines and information for contributors.

## Development Setup

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR-USERNAME/llmdev.git
cd llmdev
```

### 2. Set Up Development Environment

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode with dev dependencies
pip install -e ".[dev]"
```

### 3. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

## Development Workflow

### Running Tests

Always run tests before committing:

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=llmdev --cov-report=html

# Run specific test file
pytest tests/test_detector.py

# Run with verbose output
pytest -v
```

### Code Style

We use standard Python tools for code quality:

```bash
# Format code with black
black src/ tests/

# Check code style with flake8
flake8 src/ tests/

# Type checking with mypy (optional but recommended)
mypy src/
```

### Testing Your Changes

1. **Unit Tests**: Test individual components in isolation
2. **Integration Tests**: Test end-to-end workflows
3. **Manual Testing**: Run the CLI on real repositories

Example manual test:
```bash
llmdev analyze anicolao/llmdev --max-commits 10 --verbose
```

## Code Organization

```
llmdev/
├── src/llmdev/
│   ├── __init__.py       # Package initialization
│   ├── cli.py            # Command-line interface
│   ├── config.py         # Configuration management
│   ├── github_client.py  # GitHub API client
│   ├── analyzer.py       # Main analysis orchestration
│   ├── detector.py       # Copilot detection logic
│   └── reporter.py       # Report generation
└── tests/
    ├── test_detector.py      # Detector unit tests
    └── test_integration.py   # Integration tests
```

## Areas for Contribution

### 1. Detection Improvements

Help improve Copilot detection accuracy:

- Add new detection heuristics
- Improve existing pattern matching
- Reduce false positives
- Add support for other LLM tools (ChatGPT, Claude, etc.)

### 2. Features

Implement new features from the roadmap:

- Enhanced reporting (HTML, charts, visualizations)
- Performance optimizations
- Better error handling
- Additional GitHub API integrations

### 3. Testing

Expand test coverage:

- Add more unit tests
- Create integration tests for real repositories
- Add edge case tests
- Performance benchmarking

### 4. Documentation

Improve documentation:

- Add code examples
- Create tutorials
- Document detection heuristics
- Add FAQ section

### 5. Bug Fixes

Help fix issues:

- Check the issue tracker for bugs
- Reproduce and fix reported issues
- Add regression tests

## Pull Request Process

### 1. Before You Submit

- [ ] Run all tests and ensure they pass
- [ ] Add tests for new functionality
- [ ] Update documentation if needed
- [ ] Follow code style guidelines
- [ ] Write clear commit messages

### 2. Commit Messages

Use clear, descriptive commit messages:

```
Add support for detecting ChatGPT mentions

- Extend detector to recognize ChatGPT keywords
- Add tests for ChatGPT detection
- Update documentation with new capability
```

### 3. Pull Request Description

Include in your PR description:

- **What**: Brief description of changes
- **Why**: Motivation and context
- **How**: Implementation approach
- **Testing**: How you tested the changes
- **Screenshots**: For UI/output changes

### 4. Review Process

- Maintainers will review your PR
- Address any feedback or requested changes
- Once approved, your PR will be merged

## Development Tips

### Testing with Mock Data

For faster iteration, use mock data in tests:

```python
from llmdev.detector import CopilotDetector

detector = CopilotDetector()
commit_data = {
    'sha': 'abc123',
    'message': 'Add feature with Copilot',
    'author': 'developer'
}
detections = detector.detect_in_commit(commit_data)
```

### Testing with Real APIs

For testing API integration, use small repositories:

```bash
# Test with this repository (small and controlled)
llmdev analyze anicolao/llmdev --max-commits 5
```

### Debugging

Enable verbose logging for debugging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

Or use the CLI flag:
```bash
llmdev analyze owner/repo --verbose
```

## Questions?

- Open an issue for bugs or feature requests
- Start a discussion for questions or ideas
- Review existing issues and PRs for context

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on the code, not the person
- Help create a welcoming community

Thank you for contributing to llmdev! 🎉
