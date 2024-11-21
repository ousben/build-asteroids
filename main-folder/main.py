from constants import *
from player import Player
import pygame

def main():
    # initialize the game engine
    pygame.init()
    print("Starting asteroids!")

    # Créer la fenêtre et le joueur à l'intérieur de main(
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    clock = pygame.time.Clock() 
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        # Mettre à jour la logique du joueur
        player.update(dt)

        # Remplir l'écran en noir
        screen.fill((0, 0, 0))
        
        # Dessiner le joueur avant le flip
        player.draw(screen)
        
        # Rafraîchir l'affichage en dernier
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

#print(f"Screen width: {SCREEN_WIDTH}")
#print(f"Screen height: {SCREEN_HEIGHT}")
