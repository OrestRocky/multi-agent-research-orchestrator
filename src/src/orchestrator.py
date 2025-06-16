from agents.data_collector import DataCollectorAgent
from agents.analyzer import AnalyzerAgent
from agents.report_writer import ReportWriterAgent

class ResearchOrchestrator:
    def __init__(self):
        self.collector = DataCollectorAgent()
        self.analyzer = AnalyzerAgent()
        self.writer = ReportWriterAgent()

    def run(self, query: str):
        print(f"[ORCHESTRATOR] Starting research for: {query}")
        data = self.collector.collect(query)
        insights = self.analyzer.analyze(data)
        report = self.writer.write(insights)
        print(f"[ORCHESTRATOR] Report completed.")
        return report
