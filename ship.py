import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group
class Ship(Sprite):
    '''创建一个Sprite的子类Ship，表示玩家飞船'''
    def __init__(self,screen,setting):
        super().__init__()
        self.screen=screen
        self.setting=setting

        #加载飞船的图像放入变量image中，共有三种不同的飞船形状，图像名字为ship1.bmp，ship2.bmp，ship3.bmp用setting中的ship_type属性区分开
        self.image=pygame.image.load('image\ship'+str(setting.ship_type)+'.bmp')
        self.rect=self.image.get_rect()#获取飞船图像image的rect（矩形）属性，
        self.screen_rect=self.screen.get_rect()#获取屏幕screen的rect(矩形）属性
        self.rect.centerx=self.screen_rect.centerx#居中飞船
        self.rect.bottom=self.screen_rect.bottom#使飞船位于屏幕底部
        self.x=float(self.rect.x)#x为浮点数型的rect.x,rect.x表示图像左上角
        self.right=False#right为False，代表飞船停止向右移动，为True代表飞船开始向右移动
        self.left=False#left为False，代表飞船停止向左移动，为True代表飞船开始向左移动为

    def update_ship(self):
        '''更新飞船的位置'''
        if self.right==True and self.rect.right<=self.screen_rect.right:
            '''在飞船右移为True和飞船不会移动屏幕右侧外时移动'''
            self.x+=self.setting.ship_speed#通过加上飞船速度来实现右移
        if self.left==True and self.rect.left>=0:
            '''在飞船左移为True和飞船不会移动屏幕左侧外时移动'''
            self.x-=self.setting.ship_speed#通过加上飞船速度来实现左移
        self.rect.x=self.x#因为rect.x只能是整数型，所以这里通过改变x，最后把x的赋给rect.x实现非整数速度的移动

    def blitme(self):
        '''在屏幕上画出飞船'''
        self.image=pygame.image.load('image\ship'+str(self.setting.ship_type)+'.bmp')#重置飞船图像
        self.screen.blit(self.image,self.rect)#画出飞船

    def center(self):
        '''是飞船居中'''
        self.x=self.screen_rect.centerx
        self.rect.x=self.x

    def choice_ship_image(self):
        '''显示选择飞船类型的界面'''
        self.ships_image=Group()#创建一个包含不同飞船形状的Group实例
        for i in range(3):
            '''在屏幕不同位置显示三种飞船形状'''
            ship=Ship(self.screen,self.setting)#创建一个Ship实例
            ship.image = pygame.image.load('image\ship' + str(i+1) + '.bmp')
            ship.rect.centery=self.screen_rect.centery#y位于屏幕中心
            ship.rect.x=self.screen_rect.centerx-10*(1-int(i))*self.rect.width#间隔10个飞船宽度
            self.ships_image.add(ship)#将Ship实例添加到Group中
        self.ships_image.draw(self.screen)#画出所有的飞船