# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
# import the constants variable from constants.py
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        # Check if players pressed the X in the corner. 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Run all update from everything in the updatable group.
        for object in updatable:
            object.update(dt)

        # Perform a collision check between every bullet and every asteroid. 
        for object in asteroids:
            for shot in shots:
                if (object.collision(shot)):
                    object.kill()
                    shot.kill()

        # Perform a collision check between the player and every asteroid. 
        for object in asteroids:
            if (object.collision(player)):
                print("Game over!")
                exit()
            

        screen.fill((0, 0, 0)) # RGB value for black.
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()

        # Limit the framerate to 60 FPS. 
        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()