# Create a simple and natural bullet.py
human_bullet_content = '''import pygame
from settings import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.speed = speed
        
        # Try to load custom bullet image
        try:
            self.image = pygame.image.load('bullet.png')
            self.image = pygame.transform.scale(self.image, (BULLET_WIDTH, BULLET_HEIGHT))
        except:
            try:
                # Fallback to jpg
                self.image = pygame.image.load('NicePng_bullet-clipart-png_4297561.jpg')
                self.image = pygame.transform.scale(self.image, (BULLET_WIDTH, BULLET_HEIGHT))
            except:
                # Create colored rectangle
                self.image = pygame.Surface((BULLET_WIDTH, BULLET_HEIGHT))
                if speed < 0:  # Player bullet (going up)
                    self.image.fill(WHITE)
                else:  # Enemy bullet (going down)
                    self.image.fill(YELLOW)
        
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
    
    def update(self):
        """Move bullet up or down"""
        self.rect.y += self.speed
        
        # Remove if off screen
        if self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT:
            self.kill()
'''

# Save the bullet file
with open('bullet.py', 'w') as f:
    f.write(human_bullet_content)

print("✅ Created bullet.py - simple and straightforward")