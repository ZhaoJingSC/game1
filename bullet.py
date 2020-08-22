import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,setting,ship,screen):
        super().__init__()
        self.setting=setting
        self.ship=ship
        self.screen=screen
        self.image=pygame.image.load("image\ship"+str(setting.ship_type)+'.bmp')
        self.rect=self.image.get_rect()
        self.rect.centerx=self.ship.rect.centerx
        self.rect.top=self.ship.rect.top
        self.y=float(self.rect.y)
        self.speed=self.setting.bullet_speed

    def update(self):
        self.y-=self.speed
        self.rect.y=self.y

    def draw_bullet(self):
        self.screen.blit(self.image,self.rect)