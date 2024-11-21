from constants import *
import pygame
# this allows us to use code from
# the open-source pygame library
# throughout this file

def main():
    # initialize the game engine
    pygame.init()
    print("Starting asteroids!")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        # Remplir l'écran en noir
        screen.fill((0, 0, 0))
        # Rafraîchir l'affichage
        pygame.display.flip()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

if __name__ == "__main__":
    main()

#print(f"Screen width: {SCREEN_WIDTH}")
#print(f"Screen height: {SCREEN_HEIGHT}")
