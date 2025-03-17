from turtle import Turtle
from config import (
    GRID_SIZE,
    DIFFICULTY,
    DIFFICULTY_SETTINGS
) 

class Paddle(Turtle):
    def __init__(self, x_position):
        """Initializes a new Paddle object.
        
        Args:
           x_position: The initial X position for the paddle
        """
        super().__init__()
        self.base_size = 20
        self.width = 20
        self.length = 100
        self.boundary_offset = self.length / 2

        self.speed(0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid = self.length/self.base_size, stretch_len = self.width/self.base_size)
        self.penup()
        self.goto(x_position, 0)

        self.paddle_speed = DIFFICULTY_SETTINGS[DIFFICULTY]["ball_speed"]

    def move_up(self):
        """Moves the Paddle UP"""
        if self.ycor() < GRID_SIZE - self.boundary_offset:
            self.sety(min(self.ycor() + self.paddle_speed, GRID_SIZE - self.boundary_offset))
    
    def move_down(self):
        """Moves the Paddle DOWN"""
        if self.ycor() > -GRID_SIZE + self.boundary_offset:
            self.sety(max(self.ycor() - self.paddle_speed, -GRID_SIZE + self.boundary_offset))

    def get_position(self):
        """Returns the Paddle current position.
        
        Returns: A tuple (x,y) with the current X and Y position of the paddle
        """
        return self.xcor(), self.ycor()
    
    @property
    def paddle_top(self):
        """Dynamically calculates the paddle's top Y-coordinate."""
        return self.ycor() + self.length / 2
    
    @property
    def paddle_bottom(self):
        """Dynamically calculates the paddle's bottom Y-coordinate."""
        return self.ycor() - self.length / 2
    
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
        self.paddle_speed = new_speed

if __name__ == "__main__":
    pass