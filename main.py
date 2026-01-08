import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


def main():
    # Print startup info to console
    print("Starting Asteroids with pygame version: 2.6.1")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize pygame and create main window and clock
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0  # Delta time between frames, in seconds

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    # Create the player ship at the center of the screen
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    # Main game loop - runs until user quits
    while True:
        log_state()  # Log current game state (for debugging / monitoring)

        # Handle input and window events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Clear the screen, update and draw the player, then show the new frame
        screen.fill("black")
        updatable.update(dt)
        for one in drawable:
            one.draw(screen)
        pygame.display.flip()

        # Limit game to 60 FPS and compute frame time
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
