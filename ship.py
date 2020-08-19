import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self,screen,setting):
        super().__init__()
        self.screen=screen
        self.setting=setting
        self.image=pygame.image.load('image\ship2.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()

        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.x=float(self.rect.x)
        self.right=False
        self.left=False

    def update_ship(self):
        if self.right==True and self.rect.right<=self.screen_rect.right:
            self.x+=self.setting.ship_speed
        if self.left==True and self.rect.left>=0:
            self.x-=self.setting.ship_speed
        self.rect.x=self.x

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def center(self):
        self.x=self.screen_rect.centerx
        self.rect.x=self.x