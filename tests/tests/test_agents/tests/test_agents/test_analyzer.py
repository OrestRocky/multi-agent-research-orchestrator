import unittest
from src.agents.analyzer import AnalyzerAgent

class TestAnalyzerAgent(unittest.TestCase):
    def test_analyze(self):
        agent = AnalyzerAgent()
        result = agent.analyze("some raw data")
        self.assertIn("insights", result.lower())

if __name__ == "__main__":
    unittest.main()
    
def test_empty_input(self):
    agent = AnalyzerAgent()
    result = agent.analyze("")
    self.assertIsInstance(result, str)
