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
        self.base_size = 20
        self.width = 20
        self.length = 100
        self.boundary_offset = (self.length / 2) + self.base_size

        self.paddle = Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid = self.length/self.base_size, stretch_len = self.width/self.base_size)
        self.paddle.penup()
        self.paddle.goto(x_position, 0)

    def move_up(self):
        """Moves the Paddle UP"""
        if self.paddle.ycor() < GRID_SIZE - self.boundary_offset:
            self.paddle.sety(self.paddle.ycor() + PADDLE_BASE_MOV_SPEED)

    def move_down(self):
        """Moves the Paddle DOWN"""
        if self.paddle.ycor() > -GRID_SIZE + self.boundary_offset:
            self.paddle.sety(self.paddle.ycor() - PADDLE_BASE_MOV_SPEED)

    def get_position(self):
        """Returns the Paddle current position.
        
        Returns: A tuple (x,y) with the current X and Y position of the paddle
        """
        return self.paddle.xcor(), self.paddle.ycor()

if __name__ == "__main__":
    pass