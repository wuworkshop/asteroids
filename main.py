import pygame
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot

def main():
    pygame.init()
    # Initialize a new GUI window or screen for display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    # group for all objects that can be updated
    updatable = pygame.sprite.Group()
    # group for all the objects that can be drawn
    drawable = pygame.sprite.Group()
    # group for all asteroid objects
    asteroids = pygame.sprite.Group()
    # group for all shot objects
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()
    player = Player(x, y)
    # dt = "delta time"
    dt = 0

    # Infinite while loop for the game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pygame.Surface.fill(screen,"black")
            updatable.update(dt)
            for obj in drawable:
                obj.draw(screen)

            for asteroid in asteroids:
                for shot in shots:
                    # Check if an asteroid has collided with a shot
                    if asteroid.collide(shot):
                        asteroid.kill()
                        shot.kill()

                # Check if an asteroid has collided with the player
                if asteroid.collide(player):
                    print("Game over!")
                    exit()
            # Refresh the screen
            pygame.display.flip()
            # Set FPS (frames per second) to a maximum of 60 times per second.
            # .tick() method also returns the amount of time that has
            # passed since the last time it was called in milliseconds.
            dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()