import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from paddle import Paddle
from ball import Ball
from config import (
    GRID_SIZE
)

class TestPaddle(unittest.TestCase):
    def setUp(self):
        """Set up the test environment"""
        self.paddle = Paddle(x_position = 0)
        self.ball = Ball()

    def test_move_up(self):
        """Test the Paddle UP movement"""
        initial_y = self.paddle.get_position()[1]
        self.paddle.move_up()
        self.assertEqual(self.paddle.get_position()[1], initial_y + self.paddle.paddle_speed, f"Paddle failed to move up correctly")

    def test_move_down(self):
        """Test the Paddle DOWN movement"""
        initial_y = self.paddle.get_position()[1]
        self.paddle.move_down()
        self.assertEqual(self.paddle.get_position()[1], initial_y - self.paddle.paddle_speed, f"Paddle failed to move down correctly")

    def test_upper_boundary(self):
        """Test the Paddle goes out of bounds on the UP boundary"""
        self.paddle.sety(GRID_SIZE)
        self.paddle.move_up()
        self.assertEqual(self.paddle.get_position()[1], GRID_SIZE, f"Paddle out of bounds on the upper boundary")

    def test_lower_boundary(self):
        """Test the Paddle goes out of bounds on the DOWN boundary"""
        self.paddle.sety(-GRID_SIZE)
        self.paddle.move_down()
        self.assertEqual(self.paddle.get_position()[1], -GRID_SIZE, f"Paddle out of bounds on the upper boundary")

    def test_initial_paddle_speed(self):
        """Test if paddle starts with the correct speed."""
        self.assertEqual(self.paddle.paddle_speed, self.ball.ball_speed, f"Incorrect starting speed")

    def test_paddle_speed_updates(self):
        """Test if paddle speed updates correctly to match ball speed."""
        self.ball.bounce_x()  # Increase ball speed
        self.paddle.update_speed(self.ball.ball_speed)
        self.assertEqual(self.paddle.paddle_speed, self.ball.ball_speed, f"Speed did not update correctly")

    def tearDown(self):
        """Tear down after each test"""
        pass

if __name__ == "__main__":
    unittest.main(verbosity=2)