import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, NAV_HEIGHT, BLACK
from game import Game

def main():
    # Initialize pygame
    pygame.init()

    # Create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + NAV_HEIGHT))
    pygame.display.set_caption("Space Invaders - Hassan Ali")

    # Game clock for consistent frame rate
    clock = pygame.time.Clock()

    # Create game instance
    game = Game(screen)

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    game.handle_spacebar()

        # Update game state
        game.update()

        # Draw everything
        screen.fill(BLACK)
        game.draw()

        pygame.display.flip()
        clock.tick(60)  # 60 FPS

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
