import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group
class Ship(Sprite):
    def __init__(self,screen,setting):
        super().__init__()
        self.screen=screen
        self.setting=setting
        self.image=pygame.image.load('image\ship'+str(setting.ship_type)+'.bmp')
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
        self.image=pygame.image.load('image\ship'+str(self.setting.ship_type)+'.bmp')#重置图像
        self.screen.blit(self.image,self.rect)

    def center(self):
        self.x=self.screen_rect.centerx
        self.rect.x=self.x

    def choice_ship_image(self):
        self.ships_image=Group()
        for i in range(3):
            ship=Ship(self.screen,self.setting)
            ship.image = pygame.image.load('image\ship' + str(i+1) + '.bmp')
            ship.rect.centery=self.screen_rect.centery
            ship.rect.x=self.screen_rect.centerx-10*(1-int(i))*self.rect.width
            self.ships_image.add(ship)
        self.ships_image.draw(self.screen)