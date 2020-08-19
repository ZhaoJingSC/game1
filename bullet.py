import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,setting,ship,screen):
        super().__init__()
        self.setting=setting
        self.ship=ship
        self.screen=screen
        self.rect=pygame.Rect(0,0,self.setting.bullet_width,self.setting.bullet_high)
        self.rect.centerx=self.ship.rect.centerx
        self.rect.top=self.ship.rect.top
        self.y=float(self.rect.y)
        self.color=self.setting.bullet_color
        self.speed=self.setting.bullet_speed

    def update(self):
        self.y-=self.speed
        self.rect.y=self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)