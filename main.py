import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0 # delta time

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Exiting Asteroids, did you have fun?")
                return
        
        player.update(dt)
        screen.fill("black")
        
        player.draw(screen)
        pygame.display.flip()
        
        # resource management
        dt = clock.tick(60) / 1000
    


if __name__ == "__main__":
    main()
