from turtle import Screen
from paddle import Paddle
from ball import Ball
from config import (
    SCREEN_WIDTH, 
    SCREEN_HEIGHT, 
    GRID_SIZE
)

def setup_game_window():
    """Setups the game window"""
    screen = Screen()
    screen.title("Classic Pong")
    screen.setup(width = SCREEN_WIDTH, height = SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.tracer(0)

    # Establish a grid-based coordinate system
    screen.setworldcoordinates(-GRID_SIZE, -GRID_SIZE, GRID_SIZE, GRID_SIZE)

    return screen

def setup_controls(screen, left_paddle, right_paddle, ball):
    """Binds keyboard controls to the paddles
    
    Args:
        screen: An Scren object
        left_paddle: A Paddle object, to represent the left side paddle
        right_paddle: A Paddle object, to represent the right side paddle
        ball: A ball object
    """
    screen.listen()
    screen.onkey(lambda: left_paddle.move_up(), "w")
    screen.onkey(lambda: left_paddle.move_down(), "s")
    #screen.onkey(lambda: right_paddle.move_up(), "Up")
    #screen.onkey(lambda: right_paddle.move_down(), "Down")

    #Temporary for testing ball movement
    screen.onkey(lambda: ball.move_up(), "Up")
    screen.onkey(lambda: ball.move_down(), "Down")
    screen.onkey(lambda: ball.move_left(), "Left")
    screen.onkey(lambda: ball.move_right(), "Right")

def game_loop(screen, left_paddle, right_paddle, ball):
    """Handles the game loop and updates the screen
        
    Args:
        screen: An Scren object
        left_paddle: A Paddle object, to represent the left side paddle
        right_paddle: A Paddle object, to represent the right side paddle
        ball: A ball object
    """

    print(ball.get_position())

    screen.update()

    # Schedule the next screen update.
    # For reference, 1000ms = 1 second
    screen.ontimer(lambda: game_loop(screen, left_paddle, right_paddle, ball), 125)

def main():
    # Setting up the Game window
    screen = setup_game_window()

    # Creating the paddles
    left_paddle = Paddle(-GRID_SIZE)
    # Right paddle must be adjusted so it is completely inside the screen
    right_paddle = Paddle(GRID_SIZE - left_paddle.width/2)

    # Creating the ball
    ball = Ball()

    # Binding the keyboard controls
    setup_controls(screen, left_paddle, right_paddle, ball)
    
    # Starting the game loop
    game_loop(screen, left_paddle, right_paddle, ball)
    screen.mainloop()

if __name__ == "__main__":
    main()