import unittest
from src.orchestrator import ResearchOrchestrator

class TestOrchestrator(unittest.TestCase):
    def test_run(self):
        orchestrator = ResearchOrchestrator()
        result = orchestrator.run("Quantum computing applications")
        self.assertIn("Report", result)

if __name__ == "__main__":
    unittest.main()
