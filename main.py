from turtle import Screen
from paddle import Paddle
from ball import Ball
from game import Game
from config import (
    SCREEN_WIDTH, 
    SCREEN_HEIGHT, 
    GRID_SIZE,
    SINGLE_PLAYER
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

    if not SINGLE_PLAYER:
        screen.onkey(lambda: right_paddle.move_up(), "Up")
        screen.onkey(lambda: right_paddle.move_down(), "Down")

def game_loop(screen, left_paddle, right_paddle, ball, game):
    """Handles the game loop and updates the screen
    Args:
        screen (Screen): An Scren object
        left_paddle (Paddle): A Paddle object, to represent the left side paddle
        right_paddle (Paddle): A Paddle object, to represent the right side paddle
        ball (Ball): A ball object
        game (Game): The game object
    """
    
    # Moving the ball and checking collision
    ball.move()
    ball.handle_collisions(left_paddle, right_paddle)

    # Ask AI to move the right Paddle for us
    if SINGLE_PLAYER:
        game.ai_move_paddle(right_paddle, ball)

    # Checks for score
    game.check_score(ball)

    if game.is_game_over():
        print(f"Game Over!")
        return

    # Update Paddles speed to match the ball's speed
    left_paddle.update_speed(ball.speed)
    right_paddle.update_speed(ball.speed)

    screen.update()

    # Schedule the next screen update.
    # For reference, 1000ms = 1 second
    screen.ontimer(lambda: game_loop(screen, left_paddle, right_paddle, ball, game), 100)

def main():
    # Setting up the Game window
    screen = setup_game_window()

    # Creating the paddles
    left_paddle = Paddle(-GRID_SIZE)
    # Right paddle must be adjusted so it is completely inside the screen
    right_paddle = Paddle(GRID_SIZE - left_paddle.width/2)

    # Creating the ball
    ball = Ball()

    # Initializes the game
    game = Game()

    # Binding the keyboard controls
    setup_controls(screen, left_paddle, right_paddle)
    
    # Starting the game loop
    game_loop(screen, left_paddle, right_paddle, ball, game)
    screen.mainloop()

if __name__ == "__main__":
    main()