# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
# import the constants variable from constants.py
from constants import *
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        # Check if players pressed the X in the corner. 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0)) # RGB value for black.
        player.draw(screen)
        pygame.display.flip()

        # Limit the framerate to 60 FPS. 
        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()