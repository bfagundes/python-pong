SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640
GRID_SIZE = SCREEN_WIDTH // 2

PADDLE_BASE_MOV_SPEED = 20
BALL_BASE_MOV_SPEED = 4

MAX_SCORE = 7

SINGLE_PLAYER = True

ANGLES = [-3, -2, -1, 0, 1, 2, 3]

DIFFICULTY = "medium"
DIFFICULTY_SETTINGS = {
    "easy": {
        "ball_speed": 4,
        "max_speed": 8,
        "speed_increment": 1,
        "start_angle": 1,
        "ai_reaction": 0.7,
        "ai_speed": 0.5
    },

    "medium": {
        "ball_speed": 8,
        "max_speed": 16,
        "speed_increment": 1,
        "start_angle": 2,
        "ai_reaction": 0.8,
        "ai_speed": 0.7
    },

    "hard": {
        "ball_speed": 16,
        "max_speed": 24,
        "speed_increment": 1,
        "start_angle": 3,
        "ai_reaction": 0.9,
        "ai_speed": 0.9
    }
}