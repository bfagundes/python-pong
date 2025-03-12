import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from ball import Ball
from config import (
    GRID_SIZE,
    BALL_BASE_MOV_SPEED
)

class TestBall(unittest.TestCase):
    def setUp(self):
        """Set up the test environment"""
        self.ball = Ball()

    def test_collision_left_goal(self):
        """Test the ball collision on the left goal"""
        self.ball.ball.sety(-GRID_SIZE)
        self.assertTrue(self.ball.is_goal_left(), f"Ball collision with left wall not detected")

    def tearDown(self):
        """Tear down after each test"""
        pass

if __name__ == "__main__":
    unittest.main(verbosity=2)