import unittest
from src.agents.report_writer import ReportWriterAgent

class TestReportWriterAgent(unittest.TestCase):
    def test_write(self):
        agent = ReportWriterAgent()
        report = agent.write("some insights")
        self.assertIn("Final Research Report", report)

if __name__ == "__main__":
    unittest.main()
