import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from ball import Ball
from paddle import Paddle
from config import (
    GRID_SIZE,
    BALL_BASE_MOV_SPEED
)

class TestBall(unittest.TestCase):
    def setUp(self):
        """Set up the test environment"""
        self.ball = Ball()
        self.left_paddle = Paddle(-GRID_SIZE)
        self.right_paddle = Paddle(GRID_SIZE - self.left_paddle.width/2)

    def test_initial_position(self):
        """Test whether the ball starts at the correct initial position"""
        self.assertEqual(self.ball.ball.xcor(), self.ball.initial_position[0], f"The Ball's Initial position is incorrect on X axis")
        self.assertEqual(self.ball.ball.ycor(), self.ball.initial_position[1], f"The Ball's Initial position is incorrect on Y axis")

    def test_reset_position(self):
        """Test whether the ball resets correctly to the initial position"""
        self.ball.move()
        self.ball.reset_position()
        self.assertEqual(self.ball.ball.xcor(), self.ball.initial_position[0], f"The Ball's Initial position is incorrect on X axis")
        self.assertEqual(self.ball.ball.ycor(), self.ball.initial_position[1], f"The Ball's Initial position is incorrect on Y axis")

    def test_move(self):
        """Test the ball movement"""
        initial_x = self.ball.ball.xcor()
        initial_y = self.ball.ball.ycor()
        self.ball.move()
        self.assertEqual(self.ball.ball.xcor(), initial_x + BALL_BASE_MOV_SPEED, f"The Ball's movement is incorrect on X axis")
        self.assertEqual(self.ball.ball.ycor(), initial_y + BALL_BASE_MOV_SPEED, f"The Ball's movement is incorrect on Y axis")

    def test_bounce_y(self):
        """Test the ball's bouncing correctly on Y axis"""
        initial_y_move = self.ball.y_move
        self.ball.bounce_y()
        self.assertEqual(self.ball.y_move, -initial_y_move, f"The ball's bouncing is incorrect on Y axis")

    def test_bounce_x(self):
        """Test the ball's bouncing correctly on X axis"""
        initial_x_move = self.ball.x_move
        self.ball.bounce_x()
        self.assertEqual(self.ball.x_move, -initial_x_move, f"The ball's bouncing is incorrect on Y axis")

    def test_collision_left(self):
        """Test the ball collision on the left boundary"""
        self.ball.ball.setx(-GRID_SIZE)
        self.assertTrue(self.ball.collision_left(), f"Ball collision with left wall not detected")

    def test_collision_right(self):
        """Test the ball collision on the right boundary"""
        self.ball.ball.setx(GRID_SIZE)
        self.assertTrue(self.ball.collision_right(), f"Ball collision with right wall not detected")

    def test_collision_top(self):
        """Test the ball collision on the upper boundary"""
        self.ball.ball.sety(GRID_SIZE)
        self.assertTrue(self.ball.collision_top(), f"Ball collision with upper wall not detected")

    def test_collision_down(self):
        """Test the ball collision on the lower boundary"""
        self.ball.ball.sety(-GRID_SIZE)
        self.assertTrue(self.ball.collision_down(), f"Ball collision with lower wall not detected")

    def test_paddle_collision(self):
        """Test the ball collision with the paddles"""
        # Simulate collision with left paddle
        self.ball.ball.goto(self.left_paddle.paddle.xcor(), self.left_paddle.paddle.ycor())
        self.assertTrue(self.ball.check_paddle_collision(self.left_paddle), f"Ball collision with the left paddle not detected correctly.")

        # Simulate collision with right paddle
        self.ball.ball.goto(self.right_paddle.paddle.xcor(), self.right_paddle.paddle.ycor())
        self.assertTrue(self.ball.check_paddle_collision(self.right_paddle), f"Ball collision with the right paddle not detected correctly.")

    def test_ball_bounce_on_paddle(self):
        """Test if the ball correctly bounces after coliding with a paddle"""
        initial_x_move = self.ball.x_move

        # Simulate collision with left paddle
        self.ball.ball.goto(self.left_paddle.paddle.xcor(), self.left_paddle.paddle.ycor())
        self.ball.collision_paddle(self.left_paddle, self.right_paddle)
        self.assertEqual(self.ball.x_move, -initial_x_move, f"The ball did not bounce corectly after coliding with the left paddle")

        # Simulate collision with right paddle
        self.ball.ball.goto(self.right_paddle.paddle.xcor(), self.right_paddle.paddle.ycor())
        self.ball.collision_paddle(self.left_paddle, self.right_paddle)
        self.assertEqual(self.ball.x_move, initial_x_move, f"The ball did not bounce correctly after coliding with the right paddle")

    def tearDown(self):
        """Tear down after each test"""
        pass

if __name__ == "__main__":
    unittest.main(verbosity=2)







