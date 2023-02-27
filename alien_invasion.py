import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    '''Overall class to manage assets and behavior'''

    '''Initialize the game, and create game resources'''
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        '''set background color'''
        self.bg_color = (230, 230, 230)


    '''Start the main loop for the game'''
    def run_game(self):
            while True:
                self._check_events()
                self._update_screen()

    def _check_event(self):
        '''respond to keypresses and mouse events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        '''update images on screen, flip to the new screen'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
        pygame.display.flip()

if __name__ == '__main__':
     '''Make a game instance, and run the game'''
     ai = AlienInvasion()
     ai.run_game()
    



