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
