# Create a more natural player.py (renamed from ship.py)
human_player_content = '''import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.lives = PLAYER_LIVES
        
        # Try to load custom spaceship image
        try:
            self.image = pygame.image.load('spaceship.png')
            self.image = pygame.transform.scale(self.image, (SHIP_SIZE, SHIP_SIZE))
        except:
            try:
                # Fallback to jpg
                self.image = pygame.image.load('NicePng_spaceship-png_138961.jpg')  
                self.image = pygame.transform.scale(self.image, (SHIP_SIZE, SHIP_SIZE))
            except:
                # Create colored rectangle if no image found
                self.image = pygame.Surface((SHIP_SIZE, SHIP_SIZE))
                self.image.fill(GREEN)
        
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
    
    def update(self, keys):
        """Update player position based on key input"""
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.rect.left > 0:
                self.rect.x -= SHIP_SPEED
        
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.rect.right < SCREEN_WIDTH:
                self.rect.x += SHIP_SPEED
        
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if self.rect.top > 0:
                self.rect.y -= SHIP_SPEED
        
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if self.rect.bottom < SCREEN_HEIGHT:
                self.rect.y += SHIP_SPEED
    
    def take_damage(self):
        """Player takes damage"""
        self.lives -= 1
        if self.lives <= 0:
            self.kill()
'''

# Save the player file
with open('player.py', 'w') as f:
    f.write(human_player_content)

print("✅ Created player.py - simpler and more human-like")