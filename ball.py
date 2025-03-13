from turtle import Turtle
from config import (
    GRID_SIZE,
    BALL_BASE_MOV_SPEED
)

class Ball:
    def __init__(self):
        """Initializes the Ball object"""
        self.ball = Turtle()
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.size = 20
        self.boundary_offset = 10
        self.initial_position = (0,0)

        self.x_move = BALL_BASE_MOV_SPEED
        self.y_move = BALL_BASE_MOV_SPEED

        # Make it a little smaller
        self.ball.shapesize(stretch_wid=0.7, stretch_len=0.7)

        # Define initial position and draw
        self.ball.goto(self.initial_position)

    def get_position(self):
        """Returns the Ball's current position.
        
        Returns: A tuple (x,y) with the current X and Y position of the paddle
        """
        return self.ball.xcor(), self.ball.ycor()

    def move(self):
        """Moves the ball"""
        new_x = self.ball.xcor() + self.x_move
        new_y = self.ball.ycor() + self.y_move
        self.ball.goto(new_x, new_y)

    def bounce_x(self):
        """Bounces the ball on the X axis"""
        self.x_move *= -1

    def bounce_y(self):
        """Bounces the ball on the Y axis"""
        self.y_move *= -1

    def reset_position(self):
        """Resets the ball position to the initial position"""
        self.ball.goto(self.initial_position)
        self.bounce_x()
    
    def collision_left(self):
        """Detects collision between the ball and the left wall
        Returns:
            bool: True if a collision is detected, False otherwise"""
        return self.ball.xcor() <= -GRID_SIZE + self.size
    
    def collision_right(self):
        """Detects collision between the ball and the right wall
        Returns:
            bool: True if a collision is detected, False otherwise"""
        return self.ball.xcor() >= GRID_SIZE - self.size

    def collision_top(self):
        """Detects collision between the ball and the top wall
        Returns:
            bool: True if a collision is detected, False otherwise"""
        return self.ball.ycor() >= GRID_SIZE - self.size

    def collision_down(self):
        """Detects collision between the ball and the bottom wall
        Returns:
            bool: True if a collision is detected, False otherwise"""
        return self.ball.ycor() <= -GRID_SIZE + self.size
    
    def check_paddle_collision(self, paddle):
        """Detects collision between the ball and a paddle
        Args:
            paddle (Paddle): The paddle to check collision with.
        Returns:
            bool: True if a collision is detected, False otherwise
        """
        return (
            abs(self.ball.xcor() - paddle.paddle.xcor()) < self.size and
            paddle.paddle.ycor() - paddle.length / 2 < self.ball.ycor() < paddle.paddle.ycor() + paddle.length / 2
        )
    
    def collision_paddle(self, left_paddle, right_paddle):
        """Checks collision with either paddle and bounces the ball if detected
        Args:
        left_paddle (Paddle): the left Paddle object
        right_paddle (Paddle): the right paddle object"""
        if self.check_paddle_collision(left_paddle) or self.check_paddle_collision(right_paddle):
            self.bounce_x()

    def handle_collisions(self, left_paddle, right_paddle):
        """Handles all possible collisions with the Ball"""
        if self.collision_left() or self.collision_right():
            self.bounce_x()

        if self.collision_top() or self.collision_down():
            self.bounce_y()

        self.collision_paddle(left_paddle, right_paddle)