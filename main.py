from turtle import Screen
from config import (
    SCREEN_WIDTH, 
    SCREEN_HEIGHT, 
    GRID_SIZE
)

def setup_game_window():
    screen = Screen()
    screen.title("Classic Pont")
    screen.setup(width = SCREEN_WIDTH, height = SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.tracer(0)

    # Establish a grid-based coordinate system
    screen.setworldcoordinates(-GRID_SIZE, -GRID_SIZE, GRID_SIZE, GRID_SIZE)

    return screen

def main():
    screen = setup_game_window()
    
    screen.mainloop()

if __name__ == "__main__":
    main()