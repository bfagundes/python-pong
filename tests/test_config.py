import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from config import (
    DIFFICULTY_SETTINGS
)

class TestConfig(unittest.TestCase):
    def setUp(self):
        """Set up the test environment"""
        pass

    def test_difficulty_settings(self):
        """Ensure difficulty settings contain correct values."""
        for level, settings in DIFFICULTY_SETTINGS.items():
            with self.subTest(level=level):
                self.assertIn("ball_speed", settings)
                self.assertIn("max_speed", settings)
                self.assertGreater(settings["ball_speed"], 0)
                self.assertGreater(settings["max_speed"], settings["ball_speed"])

    def tearDown(self):
        """Tear down after each test"""
        pass

if __name__ == "__main__":
    unittest.main(verbosity=2)







