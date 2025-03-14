SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640
GRID_SIZE = SCREEN_WIDTH // 2

PADDLE_BASE_MOV_SPEED = 20
BALL_BASE_MOV_SPEED = 4

DIFFICULTY = "medium"
DIFFICULTY_SETTINGS = {
    "easy": {
        "ball_speed": 4,
        "max_speed": 8,
        "speed_increment": 1
    },

    "medium": {
        "ball_speed": 8,
        "max_speed": 16,
        "speed_increment": 1
    },

    "hard": {
        "ball_speed": 16,
        "max_speed": 24,
        "speed_increment": 1
    }
}