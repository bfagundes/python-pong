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

    def test_collision_left(self):
        """Test the ball collision on the left boundary"""
        self.ball.ball.sety(-GRID_SIZE)
        self.assertTrue(self.ball.collision_left(), f"Ball collision with left wall not detected")

    def test_collision_right(self):
        """Test the ball collision on the right boundary"""
        self.ball.ball.sety(GRID_SIZE)
        self.assertTrue(self.ball.collision_right(), f"Ball collision with right wall not detected")

    def test_collision_top(self):
        """Test the ball collision on the upper boundary"""
        self.ball.ball.setx(GRID_SIZE)
        self.assertTrue(self.ball.collision_top(), f"Ball collision with upper wall not detected")

    def test_collision_down(self):
        """Test the ball collision on the lower boundary"""
        self.ball.ball.setx(-GRID_SIZE)
        self.assertTrue(self.ball.collision_down(), f"Ball collision with lower wall not detected")

    def tearDown(self):
        """Tear down after each test"""
        pass

if __name__ == "__main__":
    unittest.main(verbosity=2)