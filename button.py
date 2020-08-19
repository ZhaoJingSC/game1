import pygame
class Button():
    def __init__(self,screen,msg):
        self.screen=screen
        self.screen_rect=self.screen.get_rect()
        self.button_color=(0,255,0)
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,50)
        self.rect=pygame.Rect(0,0,200,100)
        self.rect.center=self.screen_rect.center
        self.prep_msg(msg)#又是一个函数

    def prep_msg(self,msg):
        self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.screen_rect.center

    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
