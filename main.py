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
    screen.onkey(lambda: right_paddle.move_up(), "Up")
    screen.onkey(lambda: right_paddle.move_down(), "Down")

def game_loop(screen, left_paddle, right_paddle, ball):
    """Handles the game loop and updates the screen
        
    Args:
        screen: An Scren object
        left_paddle: A Paddle object, to represent the left side paddle
        right_paddle: A Paddle object, to represent the right side paddle
        ball: A ball object
    """
    ball.move()

    if ball.collision_left() or ball.collision_right():
        ball.bounce_x()
    
    if ball.collision_top() or ball.collision_down():
        ball.bounce_y()

    screen.update()

    # Schedule the next screen update.
    # For reference, 1000ms = 1 second
    screen.ontimer(lambda: game_loop(screen, left_paddle, right_paddle, ball), 200)

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