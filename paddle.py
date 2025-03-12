from turtle import Turtle
from config import (
    GRID_SIZE,
    PADDLE_BASE_MOV_SPEED
) 

class Paddle:
    def __init__(self, x_position):
        """Initializes a new Paddle object.
        
        Args:
           x_position: The initial X position for the paddle
        """
        self.width = 20
        self.length = 100

        self.paddle = Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid = self.length/20, stretch_len = self.width/20)
        self.paddle.penup()
        self.paddle.goto(x_position, 0)

    def move_up(self):
        """Moves the Paddle UP"""
        if self.paddle.ycor() < GRID_SIZE:
            self.paddle.sety(self.paddle.ycor() + PADDLE_BASE_MOV_SPEED)

    def move_down(self):
        """Moves the Paddle DOWN"""
        if self.paddle.ycor() > -GRID_SIZE:
            self.paddle.sety(self.paddle.ycor() - PADDLE_BASE_MOV_SPEED)

    def get_position(self):
        """Returns the Paddle current position.
        
        Returns: A tuple (x,y) with the current X and Y position of the paddle
        """
        return self.paddle.xcor(), self.paddle.ycor()

if __name__ == "__main__":
    pass