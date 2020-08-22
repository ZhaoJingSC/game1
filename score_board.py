import pygame
from pygame.sprite import Group
from ship import Ship
class ScoreBoard():
    '''创建一个ScoreBoard类，包含游戏各种记录的图像和显示函数'''
    def __init__(self,setting,screen,stats):
        self.setting=setting
        self.stats=stats
        self.font=pygame.font.SysFont(None,48)#设置字体
        self.text_color=(30,30,30)#文字的颜色
        self.screen=screen
        self.screen_rect=self.screen.get_rect()#
        self.prep_score()#初始化得分图像
        self.prep_high_score()#初始化最高分图像
        self.prep_lvl()#初始化等级图像
        self.prep_ship()#初始化剩余命数的图像

    def prep_score(self):
        '''初始化得分图像'''
        score=int(round(self.stats.score,-1))
        score_str="{:,}".format(score)#用"，"隔开的方式显示得分
        self.score_image=self.font.render("Score:"+score_str,True,self.text_color,self.setting.bg_color)#将文字转换为图像
        self.score_rect=self.score_image.get_rect()
        # 位于屏幕右上角
        self.score_rect.right = self.screen_rect.right
        self.score_rect.top = self.score_rect.top

    def prep_high_score(self):
        '''初始化最高分图像'''
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)#用"，"隔开的方式显示得分
        self.high_score_image = self.font.render("High Score:"+high_score_str, True, self.text_color, self.setting.bg_color)#将文字转换为图像
        self.high_score_rect = self.high_score_image.get_rect()
        #位于屏幕正上方
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_lvl(self):
        '''初始化等级图像'''
        lvl= str(self.stats.lvl)
        self.lvl_image=self.font.render("lvl:"+lvl,True,self.text_color,self.setting.bg_color)#将文字转换为图像
        self.lvl_rect=self.lvl_image.get_rect()
        #位于得分下方
        self.lvl_rect.right=self.screen_rect.right
        self.lvl_rect.top=self.score_rect.bottom+10

    def prep_ship(self):
        '''初始化玩家剩余命数图像,这里用飞船图像表示'''
        self.ships = Group()
        for n in range(self.stats.ships_left):
            ship=Ship(self.screen,self.setting)
            # 位于屏幕左上方
            ship.rect.x = n*ship.rect.width
            ship.rect.y = self.screen_rect.top
            self.ships.add(ship)

    def blit_score(self):
        '''画出得分'''
        self.screen.blit(self.score_image,self.score_rect)

    def blit_high_score(self):
        '''画出最高分'''
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def blit_lvl(self):
        '''画出等级'''
        self.screen.blit(self.lvl_image,self.lvl_rect)

    def blit_ship(self):
        ''''画出玩家剩余命数'''
        self.ships.draw(self.screen)