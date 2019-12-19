import sys
import pygame

def run_game():
    # Init a game and create screen object
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    bg_color = (230, 230, 230)

    # Main loop for the game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(bg_color)
        pygame.display.flip()


run_game()