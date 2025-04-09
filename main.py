import pygame

from constants import *

def main():
    pygame.init()
    # Initialize a new GUI window or screen for display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Infinite while loop for the game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pygame.Surface.fill(screen,"black")
            # Refresh the screen
            pygame.display.flip()


if __name__ == "__main__":
    main()