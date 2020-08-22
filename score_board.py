import pygame
from pygame.sprite import Group
from ship import Ship
class ScoreBoard():
    def __init__(self,setting,screen,stats):
        self.setting=setting
        self.stats=stats
        self.font=pygame.font.SysFont(None,48)
        self.text_color=(30,30,30)
        self.screen=screen
        self.screen_rect=self.screen.get_rect()#
        self.prep_score()#注意代码顺序，上面两行一定在这个属性上面，不然这个函数中的一些属性找不到
        self.prep_high_score()
        self.prep_lvl()
        self.prep_ship()

    def prep_score(self):
        score=int(round(self.stats.score,-1))
        score_str="{:,}".format(score)
        self.score_image=self.font.render("Score:"+score_str,True,self.text_color,self.setting.bg_color)
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right
        self.score_rect.top = self.score_rect.top

    def prep_high_score(self):
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render("High Score:"+high_score_str, True, self.text_color, self.setting.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_lvl(self):
        lvl= str(self.stats.lvl)
        self.lvl_image=self.font.render("lvl:"+lvl,True,self.text_color,self.setting.bg_color)
        self.lvl_rect=self.lvl_image.get_rect()
        self.lvl_rect.right=self.screen_rect.right
        self.lvl_rect.top=self.score_rect.bottom+10

    def prep_ship(self):
        self.ships = Group()
        for n in range(self.stats.ships_left):
            ship=Ship(self.screen,self.setting)
            ship.rect.x = n*ship.rect.width
            ship.rect.y = self.screen_rect.top
            self.ships.add(ship)

    def blit_score(self):
        self.screen.blit(self.score_image,self.score_rect)

    def blit_high_score(self):
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def blit_lvl(self):
        self.screen.blit(self.lvl_image,self.lvl_rect)

    def blit_ship(self):
        self.ships.draw(self.screen)