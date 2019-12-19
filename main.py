import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
    # Init a game and create screen object
    pygame.init()
    pygame.display.set_caption("Alien Invasion")
    ai_settings = Settings() # ai_settings means Alien Invasion Settings
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    
    ship = Ship(screen)

    # Main loop for the game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        pygame.display.flip()


run_game()