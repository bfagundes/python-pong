import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from paddle import Paddle
from config import GRID_SIZE

class TestPaddle(unittest.TestCase):
    def setUp(self):
        """Set up the test environment"""
        self.paddle = Paddle(x_position = 0)

    def test_move_up(self):
        """Test the Paddle UP movement"""
        initial_y = self.paddle.get_position()[1]
        self.paddle.move_up()
        self.assertEqual(self.paddle.get_position()[1], initial_y + 20, f"Paddle failed to move up correctly")

    def test_move_down(self):
        """Test the Paddle DOWN movement"""
        initial_y = self.paddle.get_position()[1]
        self.paddle.move_down()
        self.assertEqual(self.paddle.get_position()[1], initial_y - 20, f"Paddle failed to move down correctly")

    def test_upper_boundary(self):
        """Test the Paddle goes out of bounds on the UP boundary"""
        self.paddle.paddle.sety(GRID_SIZE)
        self.paddle.move_up()
        self.assertEqual(self.paddle.get_position()[1], GRID_SIZE, f"Paddle out of bounds on the upper boundary")

    def test_lower_boundary(self):
        """Test the Paddle goes out of bounds on the DOWN boundary"""
        self.paddle.paddle.sety(-GRID_SIZE)
        self.paddle.move_down()
        self.assertEqual(self.paddle.get_position()[1], -GRID_SIZE, f"Paddle out of bounds on the upper boundary")

    def tearDown(self):
        """Tear down after each test"""
        pass

if __name__ == "__main__":
    unittest.main(verbosity=2)