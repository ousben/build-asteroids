from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import pygame

def main():
    # initialize the game engine
    pygame.init()
    print("Starting asteroids!")

    # Créer la fenêtre et le joueur à l'intérieur de main(
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        # Mettre à jour la logique du joueur
        for obj in updatable:
            obj.update(dt)

        # Remplir l'écran en noir
        screen.fill((0, 0, 0))
        
        # Dessiner le joueur avant le flip
        for obj in drawable:
            obj.draw(screen)
        
        updatable.update(dt)
        
        # Rafraîchir l'affichage en dernier
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

#print(f"Screen width: {SCREEN_WIDTH}")
#print(f"Screen height: {SCREEN_HEIGHT}")
