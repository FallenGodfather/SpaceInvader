# Create a more natural alien.py
human_alien_content = '''import pygame
from settings import *

class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y, row):
        super().__init__()
        self.row = row
        self.direction = 1  # 1 for right, -1 for left
        
        # Try to load custom alien image
        try:
            self.image = pygame.image.load('alien.png')
            self.image = pygame.transform.scale(self.image, (SHIP_SIZE, SHIP_SIZE))
        except:
            try:
                # Fallback to jpg
                self.image = pygame.image.load('NicePng_space-invader-png_1926059.jpg')
                self.image = pygame.transform.scale(self.image, (SHIP_SIZE, SHIP_SIZE))
            except:
                # Create colored rectangle based on row
                self.image = pygame.Surface((SHIP_SIZE, SHIP_SIZE))
                colors = [RED, PURPLE, CYAN]
                self.image.fill(colors[row % len(colors)])
                # Add a border for visibility
                pygame.draw.rect(self.image, WHITE, self.image.get_rect(), 2)
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def move_sideways(self):
        """Move alien left or right"""
        self.rect.x += self.direction * 15
    
    def move_down(self):
        """Move alien down when hitting edge"""
        self.rect.y += 30
'''

# Save the alien file  
with open('alien.py', 'w') as f:
    f.write(human_alien_content)

print("✅ Created alien.py - much cleaner and more natural")