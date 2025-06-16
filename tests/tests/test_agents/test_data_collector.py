import unittest
from src.agents.data_collector import DataCollectorAgent

class TestDataCollectorAgent(unittest.TestCase):
    def test_collect(self):
        agent = DataCollectorAgent()
        data = agent.collect("AI in education")
        self.assertIn("AI", data)

if __name__ == "__main__":
    unittest.main()
