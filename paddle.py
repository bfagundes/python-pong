from turtle import Turtle
from config import (
    GRID_SIZE,
    DIFFICULTY,
    DIFFICULTY_SETTINGS
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
        self.boundary_offset = self.length / 2

        self.paddle = Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid = self.length/self.base_size, stretch_len = self.width/self.base_size)
        self.paddle.penup()
        self.paddle.goto(x_position, 0)

        self.speed = DIFFICULTY_SETTINGS[DIFFICULTY]["ball_speed"]

    def move_up(self):
        """Moves the Paddle UP"""
        if self.paddle.ycor() < GRID_SIZE - self.boundary_offset:
            self.paddle.sety(min(self.paddle.ycor() + self.speed, GRID_SIZE - self.boundary_offset))
    
    def move_down(self):
        """Moves the Paddle DOWN"""
        if self.paddle.ycor() > -GRID_SIZE + self.boundary_offset:
            self.paddle.sety(max(self.paddle.ycor() - self.speed, -GRID_SIZE + self.boundary_offset))

    def get_position(self):
        """Returns the Paddle current position.
        
        Returns: A tuple (x,y) with the current X and Y position of the paddle
        """
        return self.paddle.xcor(), self.paddle.ycor()
    
    def update_speed(self, new_speed):
        """Updates the Paddle speed"""
        self.speed = new_speed

if __name__ == "__main__":
    pass