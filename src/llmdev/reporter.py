"""
Report generation for analysis results.
"""

import logging
from typing import Dict, Any, List
from pathlib import Path
from datetime import datetime

from llmdev.config import Config
from llmdev.detector import Detection


logger = logging.getLogger(__name__)


class ReportGenerator:
    """Generates markdown reports from analysis results."""
    
    def __init__(self, config: Config):
        """
        Initialize the report generator.
        
        Args:
            config: Configuration object
        """
        self.config = config
        
    def generate(self, results: Dict[str, Any]) -> Path:
        """
        Generate a markdown report from analysis results.
        
        Args:
            results: Analysis results dictionary
            
        Returns:
            Path to the generated report file
        """
        logger.info("Generating report...")
        
        # Create report filename
        repo_name = results['repository']['name']
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_filename = f"{repo_name}_analysis_{timestamp}.md"
        report_path = self.config.output_dir / report_filename
        
        # Generate report content
        content = self._generate_markdown(results)
        
        # Write report
        report_path.write_text(content)
        logger.info(f"Report saved to {report_path}")
        
        return report_path
    
    def _generate_markdown(self, results: Dict[str, Any]) -> str:
        """Generate markdown content for the report."""
        repo = results['repository']
        analysis = results['analysis']
        summary = results['summary']
        detections = results['detections']
        
        lines = []
        
        # Header
        lines.append(f"# LLM Development Analysis Report")
        lines.append(f"")
        lines.append(f"**Repository:** [{repo['full_name']}](https://github.com/{repo['full_name']})")
        lines.append(f"**Analysis Date:** {analysis['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append(f"")
        
        # Repository Overview
        lines.append(f"## Repository Overview")
        lines.append(f"")
        if repo.get('description'):
            lines.append(f"**Description:** {repo['description']}")
            lines.append(f"")
        lines.append(f"- **Stars:** {repo['stars']:,}")
        lines.append(f"- **Forks:** {repo['forks']:,}")
        lines.append(f"- **Created:** {repo['created_at'].strftime('%Y-%m-%d')}")
        lines.append(f"- **Last Updated:** {repo['updated_at'].strftime('%Y-%m-%d')}")
        lines.append(f"")
        
        # Analysis Scope
        lines.append(f"## Analysis Scope")
        lines.append(f"")
        lines.append(f"- **Commits Analyzed:** {analysis['commits_analyzed']}")
        lines.append(f"- **Pull Requests Analyzed:** {analysis['prs_analyzed']}")
        lines.append(f"- **Issues Analyzed:** {analysis['issues_analyzed']}")
        lines.append(f"")
        
        # Add deep analysis sections if available
        if 'deep_analysis' in results:
            deep_lines = self._generate_deep_analysis_sections(results['deep_analysis'])
            lines.extend(deep_lines)
        
        # Detection Summary
        lines.append(f"## Detection Summary")
        lines.append(f"")
        lines.append(f"**Total Copilot Detections:** {summary['total']}")
        lines.append(f"")
        
        if summary['total'] > 0:
            lines.append(f"**Average Confidence:** {summary['average_confidence']:.2%}")
            lines.append(f"")
            
            # Breakdown by source
            lines.append(f"### Detections by Source")
            lines.append(f"")
            for source_type, count in summary['by_source'].items():
                percentage = (count / summary['total'] * 100) if summary['total'] > 0 else 0
                lines.append(f"- **{source_type.capitalize()}:** {count} ({percentage:.1f}%)")
            lines.append(f"")
            
            # Breakdown by detection type
            lines.append(f"### Detections by Type")
            lines.append(f"")
            for detection_type, count in summary['by_type'].items():
                percentage = (count / summary['total'] * 100) if summary['total'] > 0 else 0
                type_name = detection_type.replace('_', ' ').title()
                lines.append(f"- **{type_name}:** {count} ({percentage:.1f}%)")
            lines.append(f"")
        else:
            lines.append(f"*No Copilot usage detected in the analyzed content.*")
            lines.append(f"")
        
        # Detailed Findings
        if detections:
            lines.append(f"## Detailed Findings")
            lines.append(f"")
            
            # Group detections by source type
            detections_by_source = {}
            for detection in detections:
                source_type = detection.source_type
                if source_type not in detections_by_source:
                    detections_by_source[source_type] = []
                detections_by_source[source_type].append(detection)
            
            # Commits
            if 'commit' in detections_by_source:
                lines.append(f"### Commits with Copilot Detection")
                lines.append(f"")
                commit_detections = detections_by_source['commit'][:10]  # Top 10
                for detection in commit_detections:
                    lines.append(f"- **Commit:** `{detection.source_id[:8]}`")
                    lines.append(f"  - **Type:** {detection.detection_type.replace('_', ' ').title()}")
                    lines.append(f"  - **Confidence:** {detection.confidence:.0%}")
                    lines.append(f"  - **Evidence:** \"{detection.evidence}\"")
                    # Find commit URL
                    for commit_data in results['commits']:
                        if commit_data['sha'] == detection.source_id:
                            lines.append(f"  - **Link:** {commit_data['url']}")
                            break
                    lines.append(f"")
                
                if len(detections_by_source['commit']) > 10:
                    lines.append(f"*... and {len(detections_by_source['commit']) - 10} more commit detections*")
                    lines.append(f"")
            
            # Pull Requests
            if 'pr' in detections_by_source:
                lines.append(f"### Pull Requests with Copilot Mentions")
                lines.append(f"")
                pr_detections = detections_by_source['pr'][:10]  # Top 10
                for detection in pr_detections:
                    lines.append(f"- **PR #{detection.source_id}**")
                    lines.append(f"  - **Type:** {detection.detection_type.replace('_', ' ').title()}")
                    lines.append(f"  - **Confidence:** {detection.confidence:.0%}")
                    lines.append(f"  - **Evidence:** \"{detection.evidence}\"")
                    # Find PR URL
                    for pr_data in results['prs']:
                        if str(pr_data['number']) == detection.source_id:
                            lines.append(f"  - **Link:** {pr_data['url']}")
                            break
                    lines.append(f"")
                
                if len(detections_by_source['pr']) > 10:
                    lines.append(f"*... and {len(detections_by_source['pr']) - 10} more PR detections*")
                    lines.append(f"")
            
            # Issues
            if 'issue' in detections_by_source:
                lines.append(f"### Issues with Copilot Mentions")
                lines.append(f"")
                issue_detections = detections_by_source['issue'][:10]  # Top 10
                for detection in issue_detections:
                    lines.append(f"- **Issue #{detection.source_id}**")
                    lines.append(f"  - **Type:** {detection.detection_type.replace('_', ' ').title()}")
                    lines.append(f"  - **Confidence:** {detection.confidence:.0%}")
                    lines.append(f"  - **Evidence:** \"{detection.evidence}\"")
                    # Find issue URL
                    for issue_data in results['issues']:
                        if str(issue_data['number']) == detection.source_id:
                            lines.append(f"  - **Link:** {issue_data['url']}")
                            break
                    lines.append(f"")
                
                if len(detections_by_source['issue']) > 10:
                    lines.append(f"*... and {len(detections_by_source['issue']) - 10} more issue detections*")
                    lines.append(f"")
        
        # Footer
        lines.append(f"---")
        lines.append(f"")
        lines.append(f"*Report generated by llmdev v0.1.0*")
        
        return '\n'.join(lines)
    
    def _generate_deep_analysis_sections(self, deep_analysis: Dict[str, Any]) -> List[str]:
        """
        Generate markdown sections for deep analysis results.
        
        Args:
            deep_analysis: Deep analysis results
            
        Returns:
            List of markdown lines
        """
        lines = []
        
        # PR Category Distribution
        lines.append("## PR Category Distribution")
        lines.append("")
        category_dist = deep_analysis.get('category_distribution', {})
        if category_dist:
            for category, count in sorted(category_dist.items(), key=lambda x: x[1], reverse=True):
                lines.append(f"- **{category.title()}:** {count} PRs")
            lines.append("")
        
        # Iteration Patterns
        lines.append("## Iteration Patterns")
        lines.append("")
        iteration_summary = deep_analysis.get('iteration_summary', {})
        if iteration_summary:
            lines.append(f"**Average Commits per PR:** {iteration_summary.get('average_commits', 0):.1f}")
            lines.append(f"**Average Refinements per PR:** {iteration_summary.get('average_refinements', 0):.1f}")
            lines.append("")
            
            pattern_dist = iteration_summary.get('pattern_distribution', {})
            if pattern_dist:
                lines.append("### Pattern Distribution")
                lines.append("")
                for pattern, count in sorted(pattern_dist.items(), key=lambda x: x[1], reverse=True):
                    pattern_name = pattern.replace('_', ' ').title()
                    lines.append(f"- **{pattern_name}:** {count} PRs")
                lines.append("")
        
        # Prompt Analysis
        lines.append("## Prompt Analysis")
        lines.append("")
        prompt_patterns = deep_analysis.get('prompt_patterns', {})
        if prompt_patterns and prompt_patterns.get('total_prompts', 0) > 0:
            lines.append(f"**Total Prompts Analyzed:** {prompt_patterns['total_prompts']}")
            lines.append(f"**Average Specificity Score:** {prompt_patterns.get('average_specificity', 0):.2f}")
            lines.append("")
            lines.append("### Prompt Characteristics")
            lines.append("")
            lines.append(f"- **With Context:** {prompt_patterns.get('context_percentage', 0):.1f}%")
            lines.append(f"- **With Constraints:** {prompt_patterns.get('constraints_percentage', 0):.1f}%")
            lines.append(f"- **With Examples:** {prompt_patterns.get('examples_percentage', 0):.1f}%")
            lines.append("")
        else:
            lines.append("*No structured prompts found in PR descriptions.*")
            lines.append("")
        
        # Top Complex PRs
        pr_analyses = deep_analysis.get('pr_analyses', [])
        if pr_analyses:
            # Sort by complexity
            complex_prs = sorted(
                [pr for pr in pr_analyses if pr.get('complexity_score', 0) >= 6],
                key=lambda x: x.get('complexity_score', 0),
                reverse=True
            )[:5]
            
            if complex_prs:
                lines.append("## Most Complex PRs")
                lines.append("")
                for pr in complex_prs:
                    lines.append(f"### PR #{pr.get('number')}: {pr.get('title', 'N/A')}")
                    lines.append("")
                    lines.append(f"- **Category:** {pr.get('category', 'unknown').title()}")
                    lines.append(f"- **Complexity Score:** {pr.get('complexity_score', 0)}")
                    lines.append(f"- **Iterations:** {pr.get('iteration_count', 0)} commits")
                    if pr.get('time_to_merge_hours', 0) > 0:
                        hours = pr['time_to_merge_hours']
                        if hours > 24:
                            lines.append(f"- **Time to Merge:** {hours/24:.1f} days")
                        else:
                            lines.append(f"- **Time to Merge:** {hours:.1f} hours")
                    
                    indicators = pr.get('complexity_indicators', [])
                    if indicators:
                        lines.append(f"- **Complexity Indicators:** {', '.join(indicators)}")
                    
                    # Show problem/solution if available
                    problem = pr.get('problem_statement')
                    if problem:
                        lines.append(f"- **Problem:** {problem[:200]}...")
                    
                    lines.append("")
            
            # Quick wins
            quick_wins = [
                pr for pr in pr_analyses 
                if pr.get('iterations', {}).get('pattern_type') == 'quick_win'
            ][:5]
            
            if quick_wins:
                lines.append("## Quick Wins (1-2 commits)")
                lines.append("")
                for pr in quick_wins:
                    lines.append(f"- **PR #{pr.get('number')}:** {pr.get('title', 'N/A')} ({pr.get('category', 'unknown')})")
                lines.append("")
        
        return lines
