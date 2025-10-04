# Simplify and humanize the settings.py
human_settings_content = '''# Game settings and constants
# Author: Hassan Ali (FallenGodfather)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
NAV_HEIGHT = 50

# Sprite sizes
SHIP_SIZE = 40
BULLET_WIDTH = 6
BULLET_HEIGHT = 12

# Game speeds
SHIP_SPEED = 5
BULLET_SPEED = 8
ALIEN_MOVE_DELAY = 25  # frames between alien movements

# Colors (RGB values)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)

# Game configuration  
ALIEN_ROWS = 3
ALIEN_COLS = 8
PLAYER_LIVES = 3
RESPAWN_TIME = 3000  # milliseconds
'''

# Save humanized settings
with open('settings.py', 'w') as f:
    f.write(human_settings_content)

print("✅ Humanized settings.py - cleaner constants")