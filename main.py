import sys
import pygame
from alien_invasion.settings import Settings
from alien_invasion.ship import Ship
import alien_invasion.game_functions as gf
from pygame.sprite import Group
from alien_invasion.alien import Alien
from alien_invasion.game_stats import GameStats
from alien_invasion.scoreboard import Scoreboard
from alien_invasion.button import Button


def run_game():
    # Init a game and create screen object
    pygame.init()
    pygame.display.set_caption("Alien Invasion")
    ai_settings = Settings()  # ai_settings means Alien Invasion Settings
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    play_button = Button(ai_settings, screen, "Play")
    aliens = Group()
    ship = Ship(ai_settings, screen)
    bullets = Group()
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    gf.create_fleet(ai_settings, screen, ship, aliens)
    # Main loop for the game
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, sb, stats, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, sb, stats, ship, aliens, bullets, play_button)


run_game()
