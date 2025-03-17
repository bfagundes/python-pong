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
    
    @property
    def paddle_top(self):
        """Dynamically calculates the paddle's top Y-coordinate."""
        return self.paddle.ycor() + self.length / 2
    
    @property
    def paddle_bottom(self):
        """Dynamically calculates the paddle's bottom Y-coordinate."""
        return self.paddle.ycor() - self.length / 2
    
    def get_regions(self):
        """Returns the Paddle regions

        :returns: A list of tuples with all the paddle regions. (Min value, Max value)
        :rtype: List[tuple]:
        """

        # Breakpoint percentages
        percentages = [0,10,30,45,55,70,90,100]

        # Calculating the breakpoints dinamically (in case paddle length changes)
        breakpoints = []
        for p in percentages:
            breakpoints.append(int(self.length * p / 100))
        print(f"Breakpoints: {breakpoints}")

        adjusted_breakpoints = []
        adjusted_breakpoints.append(breakpoints[0])
        for b in breakpoints[1:-1]:
            adjusted_breakpoints.append(breakpoints[b]+breakpoints[b+1])
        print(f"Breakpoints: {adjusted_breakpoints}")

        regions = []
        for i in range(len(adjusted_breakpoints) -1):
            regions.append((adjusted_breakpoints[i], adjusted_breakpoints[i+1]))
        print(f"Regions: {regions}")

    def update_speed(self, new_speed):
        """Updates the Paddle speed
        
        Args:
            new_speed (int): The new speed for the Paddle"""
        self.speed = new_speed

if __name__ == "__main__":
    pass