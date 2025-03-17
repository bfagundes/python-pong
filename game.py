import time, random
from turtle import Turtle
from config import (
    GRID_SIZE, ANGLES, MAX_SCORE,
    DIFFICULTY, DIFFICULTY_SETTINGS
)

class Game: 
    def __init__(self):
        """Initializes the game, with score tracking"""
        self.playera_score = 0
        self.playerb_score = 0
        self.score_display = Turtle()
        self.score_display.color("white")
        self.score_display.penup()
        self.score_display.hideturtle()
        self.update_score_display()

    def check_score(self, ball):
        """Checks if a player scores a point. Resets the ball and updates the score.
        
        Args:
            ball (Ball): The game's Ball object
        """

        if ball.collision_left():
            self.playerb_score += 1
            self.reset_ball(ball, direction=1)
        elif ball.collision_right():
            self.playera_score += 1
            self.reset_ball(ball, direction=-1)
        
        self.update_score_display()

    def reset_ball(self, ball, direction):
        """Resets the ball to the center and sets its movement direction.
        
        Args:
            ball (Ball): The game's Ball object
            direction (int): The new direction of the ball (1=right, -1=left)
        """

        ball.reset_position()
        # Pause before resuming
        time.sleep(2)  

        # Set movement towards the loser
        ball.x_move = abs(ball.base_speed) * direction  

        # Update vertical angle to a random one
        new_angle = random.choice(ANGLES)
        ball.y_move = new_angle
    
    def update_score_display(self):
        """Updates the score display on the screen."""
        self.score_display.clear()
        self.score_display.goto(0, GRID_SIZE - 50)
        self.score_display.write(f"{self.playera_score} - {self.playerb_score}", align="center", font=("Courier", 24, "bold"))
    
    def get_score(self):
        """Returns the current score as a tuple.
        
        Returns
            (int,int): The score as a tuple (PlayerA, PlayerB)"""
        return self.playera_score, self.playerb_score
    
    def is_game_over(self):
        """Checks if a player has won the game and displays the game-over message."""
        if self.playera_score >= MAX_SCORE:
            self.display_game_over("Player A won!")
            return True
        elif self.playerb_score >= MAX_SCORE:
            self.display_game_over("Player B won!")
            return True
        return False
    
    def display_game_over(self, winner):
        """Displays the game-over message below the score."""
        self.score_display.goto(0, GRID_SIZE - 100)
        self.score_display.write(f"Game Over. {winner}", align="center", font=("Courier", 20, "bold"))

    def ai_move_paddle(self, paddle, ball):
        """Moves the AI paddle based on difficulty settings.
        
        Args:
            paddle (Paddle): The paddle to be controlled by AI
            ball (Ball): The game's Ball object
        """

        ai_speed = DIFFICULTY_SETTINGS[DIFFICULTY]["ball_speed"] * DIFFICULTY_SETTINGS[DIFFICULTY]["ai_speed"]
        reaction_chance = DIFFICULTY_SETTINGS[DIFFICULTY]["ai_reaction"]

        # Moves when the ball is 10 px away from the Paddle Y position
        if abs(ball.ycor() - paddle.paddle.ycor()) > 10:

            # If the ball is above the Paddle, move up
            if ball.ycor() > paddle.paddle.ycor():
                paddle.paddle.sety(paddle.paddle.ycor() + ai_speed * 2)

            # If the ball is below the Paddle, move down
            else:
                paddle.paddle.sety(paddle.paddle.ycor() - ai_speed * 2)

        # Introduce AI Mistakes
        # Random.random() generates a random number between 0 and 1
        # If this number is greather than the raction_chance, the AI makes a mistake
        # Mistake = The AI moves the Paddle to the opposite direction it should
        if random.random() > reaction_chance:

            # If the ball is above the Paddle, move DOWN
            if ball.ycor() > paddle.paddle.ycor():
                paddle.paddle.sety(paddle.paddle.ycor() - ai_speed)

            # If the ball is below the Paddle, move UP
            else:
                paddle.paddle.sety(paddle.paddle.ycor() + ai_speed)