import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    '''Overall class to manage assets and behavior'''

    '''Initialize the game, and create game resources'''
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        '''set background color'''
        self.bg_color = (230, 230, 230)


    '''Start the main loop for the game'''
    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

            print(len(self.bullets))
            
    def _update_bullets(self):
        '''Update position of bullets and get rid of old bullets'''
        #Update bullet positions
        self.bullets.update()

        #Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _check_events(self):
        '''respond to keypresses and mouse events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                #move the ship to the right
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                #move the ship to the left
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        '''Respond to keypresses'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
                
    def _check_keyup_events(self, event):
        '''respond to key releases'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False  
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        '''create a new bullet and add it to the bullets group'''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

                
    def _update_screen(self):
        '''update images on screen, flip to the new screen'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        pygame.display.flip()

if __name__ == '__main__':
     '''Make a game instance, and run the game'''
     ai = AlienInvasion()
     ai.run_game()
    



