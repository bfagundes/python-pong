from turtle import Turtle
from config import (
    GRID_SIZE,
    DIFFICULTY,
    DIFFICULTY_SETTINGS
)

class Ball:
    def __init__(self):
        """Initializes the Ball object"""
        self.ball = Turtle()
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.size = 20
        self.initial_position = (0,0)

        self.base_speed = DIFFICULTY_SETTINGS[DIFFICULTY]["ball_speed"]
        self.max_speed = DIFFICULTY_SETTINGS[DIFFICULTY]["max_speed"]
        self.speed_increment = DIFFICULTY_SETTINGS[DIFFICULTY]["speed_increment"]
        self.angle = DIFFICULTY_SETTINGS[DIFFICULTY]["start_angle"]
        self.speed = self.base_speed

        self.x_move = self.speed
        self.y_move = self.angle

        # Make it a little smaller
        self.ball.shapesize(stretch_wid=0.7, stretch_len=0.7)

        # Define initial position and draw
        self.ball.goto(self.initial_position)

    def get_position(self):
        """Returns the Ball's current position.
        
        :returns: A tuple (x,y) with the current X and Y position of the paddle
        :rtype: tuple[float, float]
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

    def increase_speed(self):
        """Increases the ball speed"""
        if self.speed < self.max_speed:
            self.speed += self.speed_increment
    
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
        """Detects collision between the ball and a paddle.

        Args:
            paddle (Paddle): The paddle to check collision with.
        Returns:
            bool: True if a collision is detected, False otherwise.
        """
        ball_x = self.ball.xcor()
        ball_y = self.ball.ycor()
        
        paddle_x = paddle.paddle.xcor()
        paddle_y = paddle.paddle.ycor()
        paddle_half_length = paddle.length / 2
        paddle_half_width = paddle.width / 2
        paddle_top = paddle_y + paddle_half_length
        paddle_bottom = paddle_y - paddle_half_length

        if paddle_x == -GRID_SIZE:
            # Left Paddle
            return (
                ball_x <= -GRID_SIZE + self.size + paddle_half_width and
                ball_y <= paddle_top and
                ball_y >= paddle_bottom
            )
        else:
            # Right Paddle
            return (
                ball_x >= GRID_SIZE - self.size - paddle_half_width and
                ball_y <= paddle_top and
                ball_y >= paddle_bottom
            )
    
    def collision_paddle(self, left_paddle, right_paddle):
        """Checks collision with either paddle and bounces the ball if detected
        Args:
            left_paddle (Paddle): the left Paddle object
            right_paddle (Paddle): the right paddle object"""
        
        if self.check_paddle_collision(left_paddle):
            print(f"L Paddle Collision")
        if self.check_paddle_collision(right_paddle):
            print(f"R Paddle Collision")
        if self.collision_left():
            print(f"L Wall collision")
        if self.collision_right():
            print(f"R Wall collision")

        if self.check_paddle_collision(left_paddle) or self.check_paddle_collision(right_paddle):
            self.bounce_x()
            self.increase_speed()

    def handle_collisions(self, left_paddle, right_paddle):
        """Handles all possible collisions with the Ball"""

        self.collision_paddle(left_paddle, right_paddle)

        if self.collision_left() or self.collision_right():
            self.bounce_x() # remove this
            pass # increase score and do other applicable actions

        if self.collision_top() or self.collision_down():
            self.bounce_y()