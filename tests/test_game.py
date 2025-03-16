import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from game import Game
from ball import Ball
from paddle import Paddle
from config import GRID_SIZE

class TestGame(unittest.TestCase):
    def setUp(self):
        """Set up the test environment"""
        self.game = Game()
        self.ball = Ball()
        self.left_paddle = Paddle(-GRID_SIZE)
        self.right_paddle = Paddle(GRID_SIZE - self.left_paddle.width / 2)
    
    def test_initial_score(self):
        """Test that the initial score is 0-0."""
        self.assertEqual(self.game.playera_score, 0, f"PlayerA initial score is not zero")
        self.assertEqual(self.game.playerb_score, 0, f"PlayerB initial score is not zero")
    
    def test_score_point_left(self):
        """Test that the left player scores a point when the ball passes the right paddle."""
        # Simulate ball going past right paddle
        self.ball.ball.setx(GRID_SIZE + 10)  
        self.game.check_score(self.ball)
        self.assertEqual(self.game.playera_score, 1, f"Incorrect score after PlayerB scored")
    
    def test_score_point_right(self):
        """Test that the right player scores a point when the ball passes the left paddle."""
        # Simulate ball going past left paddle
        self.ball.ball.setx(-GRID_SIZE - 10)  
        self.game.check_score(self.ball)
        self.assertEqual(self.game.playerb_score, 1, f"Incorrect score after PlayerA scored")
    
    def test_ball_resets_on_score(self):
        """Test that the ball resets to the center after a score."""
        self.ball.ball.setx(GRID_SIZE + 10)
        self.game.check_score(self.ball)
        self.assertEqual(self.ball.get_position(), (0, 0), f"The ball did not reset correctly after a goal")
    
    def test_ball_moves_toward_loser(self):
        """Test that the ball moves toward the player who lost the point."""
        self.ball.ball.setx(GRID_SIZE + 10)
        self.game.check_score(self.ball)
        self.assertLess(self.ball.x_move, 0, f"The ball is not moving towards the point loser after a goal")

    def tearDown(self):
        """Tear down after each test"""
        pass

if __name__ == "__main__":
    unittest.main(verbosity=2)