import time
from turtle import Turtle
from config import GRID_SIZE

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
        time.sleep(2)  # Pause before resuming
        ball.x_move = abs(ball.base_speed) * direction  # Set movement towards the loser
        ball.y_move = ball.base_speed  # Reset vertical movement
        ball.speed = ball.base_speed  # Reset speed to default
    
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
    
    def is_game_over(self, max_score=7):
        """Checks if a player has won the game.
        
        Returns:
            bool: True if the game is over, False otherwise"""
        return self.playera_score >= max_score or self.playerb_score >= max_score