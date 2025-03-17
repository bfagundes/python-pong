from turtle import Turtle
from config import (
    GRID_SIZE,
    DIFFICULTY,
    DIFFICULTY_SETTINGS
)

class Ball(Turtle):
    def __init__(self):
        """Initializes the Ball object"""
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.size = 20
        self.initial_position = (0,0)

        self.base_speed = DIFFICULTY_SETTINGS[DIFFICULTY]["ball_speed"]
        self.max_speed = DIFFICULTY_SETTINGS[DIFFICULTY]["max_speed"]
        self.speed_increment = DIFFICULTY_SETTINGS[DIFFICULTY]["speed_increment"]
        self.angle = DIFFICULTY_SETTINGS[DIFFICULTY]["start_angle"]
        self.ball_speed = self.base_speed

        self.x_move = self.ball_speed
        self.y_move = self.angle

        # Make it a little smaller
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)

        # Define initial position and draw
        self.goto(self.initial_position)

    def get_position(self):
        """Returns the Ball's current position.
        
        :returns: A tuple (x,y) with the current X and Y position of the paddle
        :rtype: tuple[float, float]
        """
        return self.xcor(), self.ycor()

    def move(self):
        """Moves the ball"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        """Bounces the ball on the X axis"""
        self.x_move *= -1

    def bounce_y(self):
        """Bounces the ball on the Y axis"""
        self.y_move *= -1

    def reset_position(self):
        """Resets the ball position to the initial position"""
        self.goto(self.initial_position)

    def increase_speed(self):
        """Increases the ball speed"""
        if self.ball_speed < self.max_speed:
            self.ball_speed += self.speed_increment
    
    def collision_left(self):
        """Detects collision between the ball and the left wall

        Returns:
            bool: True if a collision is detected, False otherwise"""
        return self.xcor() <= -GRID_SIZE + self.size
    
    def collision_right(self):
        """Detects collision between the ball and the right wall

        Returns:
            bool: True if a collision is detected, False otherwise"""
        return self.xcor() >= GRID_SIZE - self.size

    def collision_top(self):
        """Detects collision between the ball and the top wall

        Returns:
            bool: True if a collision is detected, False otherwise"""
        return self.ycor() >= GRID_SIZE - self.size

    def collision_down(self):
        """Detects collision between the ball and the bottom wall

        Returns:
            bool: True if a collision is detected, False otherwise"""
        return self.ycor() <= -GRID_SIZE + self.size
    
    def adjust_angle(self, paddle):
        """Adjusts the ball angle (Y axis) after colliding with a Paddle
        Args:
            paddle (Paddle): The paddle that the Ball collided to
        """
        impact_position = ((self.ycor() - paddle.paddle_bottom) / paddle.length) * 100
        print(f"Impact position: {impact_position}")

        if impact_position <= 10:
            self.y_move = -3
        elif 10 < impact_position <= 30:
            self.y_move = -2
        elif 30 < impact_position <= 45:
            self.y_move = -1
        elif 45 < impact_position <= 55:
            self.y_move = 0
        elif 55 < impact_position <= 70:
            self.y_move = 1
        elif 70 < impact_position <= 90:
            self.y_move = 2
        else:
            self.y_move = 3
    
    def check_paddle_collision(self, paddle):
        """Detects collision between the ball and a paddle.

        Args:
            paddle (Paddle): The paddle to check collision with.
        Returns:
            bool: True if a collision is detected, False otherwise.
        """
        if paddle.paddle.xcor() == -GRID_SIZE:
            # Left Paddle
            return (
                self.xcor() <= -GRID_SIZE + self.size + paddle.width / 2 and
                paddle.paddle_bottom <= self.ycor() <= paddle.paddle_top
            )
        else:
            # Right Paddle
            return (
                self.xcor() >= GRID_SIZE - self.size - paddle.width / 2 and
                paddle.paddle_bottom <= self.ycor() <= paddle.paddle_top
            )

    def handle_collisions(self, left_paddle, right_paddle):
        """Handles all possible collisions with the Ball"""

        if self.check_paddle_collision(left_paddle):
            print(f"L Paddle Collision")
        if self.check_paddle_collision(right_paddle):
            print(f"R Paddle Collision")
        if self.collision_left():
            print(f"L Wall collision")
        if self.collision_right():
            print(f"R Wall collision")

        if self.check_paddle_collision(left_paddle):
            self.bounce_x()
            self.adjust_angle(left_paddle)
            self.increase_speed()

        elif self.check_paddle_collision(right_paddle):
            self.bounce_x()
            self.adjust_angle(right_paddle)
            self.increase_speed()

        elif self.collision_left() or self.collision_right():
            self.bounce_x()
            pass

        elif self.collision_top() or self.collision_down():
            self.bounce_y()