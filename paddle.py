from turtle import Turtle
from config import (
    GRID_SIZE,
    PADDLE_BASE_MOV_SPEED
) 

class Paddle:
    def __init__(self, x_position):
        self.paddle = Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(x_position, 0)

    def move_up(self):
        if self.paddle.ycor() < GRID_SIZE:
            self.paddle.sety(self.paddle.ycor() + PADDLE_BASE_MOV_SPEED)

    def move_down(self):
        if self.paddle.ycor() > -GRID_SIZE:
            self.paddle.sety(self.paddle.ycor() - PADDLE_BASE_MOV_SPEED)

    def get_position(self):
        return self.paddle.xcor(), self.paddle.ycor()

if __name__ == "__main__":
    pass