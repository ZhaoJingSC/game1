from pygame.sprite import Sprite
import pygame
class Enemy(Sprite):
    def __init__(self,screen,setting):
        super().__init__()
        self.screen=screen
        self.setting=setting
        self.screen_rect=self.screen.get_rect()
        self.image=pygame.image.load('image\enemy2.bmp')
        self.rect=self.image.get_rect()
        self.x=float(self.rect.x)
        self.speed=self.setting.enemy_speed
        self.down_speed=self.setting.enemy_down_speed

    def update(self):
        self.x+=self.setting.enemy_flag*self.speed
        self.rect.x=self.x

    def check_edge(self):
        if self.rect.right>=self.screen_rect.right or self.rect.left<=0:
            return True