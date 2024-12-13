# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
# import the constants variable from constants.py
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        # Check if players pressed the X in the corner. 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0)) # RGB value for black.
        pygame.display.flip()

        dt = clock.tick(60) / 1000
        print(dt)

if __name__ == "__main__":
    main()