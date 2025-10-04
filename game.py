import pygame
import random
from settings import *
from player import Player
from alien import Alien
from bullet import Bullet

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)

        # Game state
        self.state = "menu"  # menu, playing, paused, game_over
        self.score = 0
        self.level = 1

        # Sprites
        self.player = pygame.sprite.GroupSingle()
        self.aliens = pygame.sprite.Group()
        self.player_bullets = pygame.sprite.Group()
        self.alien_bullets = pygame.sprite.Group()

        # Timing
        self.alien_timer = 0
        self.last_alien_death = 0

        self.setup_game()

    def setup_game(self):
        """Initialize game objects"""
        # Create player
        player_x = SCREEN_WIDTH // 2
        player_y = SCREEN_HEIGHT - SHIP_SIZE - 10
        self.player.add(Player(player_x, player_y))

        # Create aliens
        self.spawn_aliens()

    def spawn_aliens(self):
        """Create a formation of aliens"""
        self.aliens.empty()

        start_x = 100
        start_y = 80
        spacing_x = 70
        spacing_y = 60

        for row in range(ALIEN_ROWS):
            for col in range(ALIEN_COLS):
                x = start_x + col * spacing_x
                y = start_y + row * spacing_y
                alien = Alien(x, y, row)
                self.aliens.add(alien)

    def handle_spacebar(self):
        """Handle spacebar press"""
        if self.state == "menu":
            self.state = "playing"
        elif self.state == "playing":
            self.shoot()
        elif self.state == "game_over":
            self.restart()

    def shoot(self):
        """Player shoots a bullet"""
        if self.player.sprite and len(self.player_bullets) < 3:  # Max 3 bullets
            x = self.player.sprite.rect.centerx
            y = self.player.sprite.rect.top
            bullet = Bullet(x, y, -BULLET_SPEED)
            self.player_bullets.add(bullet)

    def update(self):
        """Update game logic"""
        if self.state != "playing":
            return

        # Update player
        keys = pygame.key.get_pressed()
        if self.player.sprite:
            self.player.sprite.update(keys)

        # Update bullets
        self.player_bullets.update()
        self.alien_bullets.update()

        # Remove off-screen bullets
        for bullet in self.player_bullets:
            if bullet.rect.bottom < 0:
                bullet.kill()
        for bullet in self.alien_bullets:
            if bullet.rect.top > SCREEN_HEIGHT:
                bullet.kill()

        # Move aliens
        self.update_aliens()

        # Check collisions
        self.check_collisions()

        # Check win/lose conditions
        self.check_game_state()

    def update_aliens(self):
        """Move aliens with timing"""
        if len(self.aliens) == 0:
            # Respawn aliens after delay
            current_time = pygame.time.get_ticks()
            if current_time - self.last_alien_death > RESPAWN_TIME:
                self.spawn_aliens()
                self.level += 1
            return

        self.alien_timer += 1
        if self.alien_timer < ALIEN_MOVE_DELAY:
            return

        self.alien_timer = 0

        # Check if aliens hit screen edge
        move_down = False
        for alien in self.aliens:
            if alien.rect.left <= 0 or alien.rect.right >= SCREEN_WIDTH:
                move_down = True
                break

        # Move all aliens
        if move_down:
            for alien in self.aliens:
                alien.move_down()
                alien.direction *= -1
        else:
            for alien in self.aliens:
                alien.move_sideways()

        # Random alien shooting
        if random.random() < 0.01 and len(self.alien_bullets) < 5:
            shooting_aliens = [a for a in self.aliens if a.rect.bottom < SCREEN_HEIGHT - 100]
            if shooting_aliens:
                shooter = random.choice(shooting_aliens)
                bullet = Bullet(shooter.rect.centerx, shooter.rect.bottom, BULLET_SPEED)
                self.alien_bullets.add(bullet)

    def check_collisions(self):
        """Check for collisions between objects"""
        # Player bullets hit aliens
        hits = pygame.sprite.groupcollide(self.player_bullets, self.aliens, True, True)
        for hit in hits:
            self.score += 10
            if len(self.aliens) == 0:
                self.last_alien_death = pygame.time.get_ticks()

        # Alien bullets hit player
        if self.player.sprite:
            hits = pygame.sprite.spritecollide(self.player.sprite, self.alien_bullets, True)
            if hits:
                self.player.sprite.take_damage()

        # Aliens collide with player
        if self.player.sprite:
            hits = pygame.sprite.spritecollide(self.player.sprite, self.aliens, False)
            if hits:
                self.player.sprite.take_damage()

    def check_game_state(self):
        """Check if game is over"""
        # Player died
        if not self.player.sprite or self.player.sprite.lives <= 0:
            self.state = "game_over"
            return

        # Aliens reached bottom
        for alien in self.aliens:
            if alien.rect.bottom >= SCREEN_HEIGHT:
                self.state = "game_over"
                return

    def restart(self):
        """Restart the game"""
        self.state = "playing"
        self.score = 0
        self.level = 1
        self.alien_timer = 0

        # Clear sprites
        self.aliens.empty()
        self.player_bullets.empty()
        self.alien_bullets.empty()
        if self.player.sprite:
            self.player.sprite.kill()

        self.setup_game()

    def draw(self):
        """Draw everything on screen"""
        if self.state == "menu":
            self.draw_menu()
        elif self.state == "playing":
            self.draw_game()
        elif self.state == "game_over":
            self.draw_game_over()

    def draw_menu(self):
        """Draw the main menu"""
        title = self.font.render("SPACE INVADERS", True, WHITE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 60))
        self.screen.blit(title, title_rect)

        author = self.small_font.render("by Hassan Ali (FallenGodfather)", True, CYAN)
        author_rect = author.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 20))
        self.screen.blit(author, author_rect)

        start = self.small_font.render("Press SPACE to start", True, WHITE)
        start_rect = start.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 40))
        self.screen.blit(start, start_rect)

        controls = self.small_font.render("Arrow keys to move, SPACE to shoot", True, YELLOW)
        controls_rect = controls.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 80))
        self.screen.blit(controls, controls_rect)

    def draw_game(self):
        """Draw the game screen"""
        # Draw sprites
        self.player.draw(self.screen)
        self.aliens.draw(self.screen)
        self.player_bullets.draw(self.screen)
        self.alien_bullets.draw(self.screen)

        # Draw UI
        self.draw_ui()

    def draw_game_over(self):
        """Draw game over screen"""
        game_over = self.font.render("GAME OVER", True, RED)
        go_rect = game_over.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 40))
        self.screen.blit(game_over, go_rect)

        final_score = self.small_font.render(f"Final Score: {self.score}", True, WHITE)
        score_rect = final_score.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        self.screen.blit(final_score, score_rect)

        restart = self.small_font.render("Press SPACE to restart", True, WHITE)
        restart_rect = restart.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 40))
        self.screen.blit(restart, restart_rect)

    def draw_ui(self):
        """Draw the user interface"""
        # Score
        score_text = self.small_font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, SCREEN_HEIGHT + 10))

        # Level  
        level_text = self.small_font.render(f"Level: {self.level}", True, WHITE)
        self.screen.blit(level_text, (200, SCREEN_HEIGHT + 10))

        # Lives
        if self.player.sprite:
            lives_text = self.small_font.render(f"Lives: {self.player.sprite.lives}", True, WHITE)
            self.screen.blit(lives_text, (400, SCREEN_HEIGHT + 10))
