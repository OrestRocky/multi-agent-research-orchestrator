# System Architecture

This project follows a modular multi-agent architecture designed for autonomous research execution.

## Overview Diagram

+------------------+
| Orchestrator |
+------------------+
|
+------------------+-------------------+
| | |
v v v
Collector Analyzer Report Writer
| | |
+--------------+-------------------+
|
Memory

## Components
- **Orchestrator**: Controls flow between agents.
- **Collector Agent**: Retrieves raw data.
- **Analyzer Agent**: Interprets and structures the data.
- **Report Agent**: Generates human-readable reports.
- **Memory**: Stores and retrieves intermediate or long-term data.

Designed for research automation, modularity, and explainability.
