import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    

    update_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (update_group, drawable_group)
    Asteroid.containers = (asteroids, update_group, drawable_group)
    AsteroidField.containers = update_group

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    dt = 0 # delta time

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Exiting Asteroids, did you have fun?")
                return
        
        # player.update(dt)
        update_group.update(dt)
        screen.fill("black")
        
        # player.draw(screen)
        for drawable in drawable_group:
            drawable.draw(screen)
        
        pygame.display.flip()
        
        # resource management
        dt = clock.tick(60) / 1000
    


if __name__ == "__main__":
    main()
