# Usage Instructions

## Quick Start

Run the orchestrator with a query:
```bash
python src/orchestrator.py --query "Example research topic"
Agent Behavior

Each agent is responsible for one stage of research:

DataCollectorAgent: Finds raw information.
AnalyzerAgent: Performs processing and insight extraction.
ReportWriterAgent: Formats results into a final document.
Memory

Use VectorMemory to store and retrieve research fragments dynamically.

Coming Soon

Integration with external APIs.
LLM plugins for deeper semantic processing.
