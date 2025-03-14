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

def setup_controls(screen, left_paddle, right_paddle):
    """Binds keyboard controls to the paddles
    Args:
        screen: An Scren object
        left_paddle: A Paddle object, to represent the left side paddle
        right_paddle: A Paddle object, to represent the right side paddle
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
    
    # Moving the ball and checking collision
    ball.move()
    ball.handle_collisions(left_paddle, right_paddle)

    # Update Paddles speed to match the ball's speed
    left_paddle.update_speed(ball.speed)
    right_paddle.update_speed(ball.speed)

    screen.update()

    # Schedule the next screen update.
    # For reference, 1000ms = 1 second
    screen.ontimer(lambda: game_loop(screen, left_paddle, right_paddle, ball), 100)

def main():
    # Setting up the Game window
    screen = setup_game_window()

    # Creating the paddles
    left_paddle = Paddle(-GRID_SIZE)
    # Right paddle must be adjusted so it is completely inside the screen
    right_paddle = Paddle(GRID_SIZE - left_paddle.width/2)

    left_paddle.get_regions()

    # Creating the ball
    ball = Ball()

    # Binding the keyboard controls
    setup_controls(screen, left_paddle, right_paddle)
    
    # Starting the game loop
    game_loop(screen, left_paddle, right_paddle, ball)
    screen.mainloop()

if __name__ == "__main__":
    main()