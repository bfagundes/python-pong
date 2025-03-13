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
        """Returns the Paddle current position.
        
        Returns: A tuple (x,y) with the current X and Y position of the paddle
        """
        return self.ball.xcor(), self.ball.ycor()
    
    # def move_up(self):
    #     """Moves the Ball UP"""
    #     if self.ball.ycor() < GRID_SIZE:
    #         self.ball.sety(self.ball.ycor() + BALL_BASE_MOV_SPEED)

    # def move_down(self):
    #     """Moves the Ball DOWN"""
    #     if self.ball.ycor() > -GRID_SIZE:
    #         self.ball.sety(self.ball.ycor() - BALL_BASE_MOV_SPEED)

    # def move_left(self):
    #     """Moves the Ball LEFT"""
    #     if self.ball.xcor() > -GRID_SIZE:
    #         self.ball.setx(self.ball.xcor() - BALL_BASE_MOV_SPEED)

    # def move_right(self):
    #     """Moves the Ball RIGHT"""
    #     if self.ball.xcor() < GRID_SIZE:
    #         self.ball.setx(self.ball.xcor() + BALL_BASE_MOV_SPEED)

    def move(self):
        new_x = self.ball.xcor() + BALL_BASE_MOV_SPEED
        new_y = self.ball.ycor() + BALL_BASE_MOV_SPEED
        self.ball.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def reset_position(self):
        self.ball.goto(self.initial_position)
        self.bounce_x()
    
    def collision_left(self):
        return self.ball.xcor() >= -GRID_SIZE
    
    def collision_right(self):
        return self.ball.xcor() <= GRID_SIZE

    def collision_top(self):
        return self.ball.ycor() <= GRID_SIZE

    def collision_down(self):
        return self.ball.ycor() >= - GRID_SIZE