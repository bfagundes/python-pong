import time, random
from turtle import Turtle
from config import GRID_SIZE, ANGLES, MAX_SCORE

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