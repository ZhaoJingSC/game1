import pygame#导入pygame包
from setting import Setting#导入Setting类
from ship import Ship#导入Ship类
from game_stats import GameStats#导入GameStats类
from button import Button#导入Button类
import functions as f#导入functions模块记为f
from pygame.sprite import Group#导入Group类
from score_board import ScoreBoard#导入ScoreBoard类
def run_game():
    '''主函数，包含初始化屏幕，刷新屏幕的循环功能'''
    pygame.init()#初始化
    setting=Setting()#创建一个Setting实例，储存在setting变量中
    screen=pygame.display.set_mode((setting.width,setting.high))#创建一个屏幕，放在变量screen中，屏幕的宽为setting变量的width属性，高为high属性
    pygame.display.set_caption("game1")#命名屏幕的名字为“game1”
    button=Button(screen,'Start')#创建一个Button（开始按钮）实例放在button变量中
    ship=Ship(screen,setting)#创建一个Ship（玩家飞船）实例放在ship变量中
    bullets=Group()#创建一个Group（子弹）实例，放在bullets中
    enemies=Group()#创建一个Group（敌人）实例，放在enemies中
    stats=GameStats(setting)#创建一个GameStats（游戏记录）实例，放在stats中
    f.create_enemies(setting, screen, enemies)#调用f模块中的create_enemies函数，创建一群敌人
    sb=ScoreBoard(setting,screen,stats)#创建一个ScoreBoard(计分板)实例放在sb变量中
    while True:
        '''游戏主循环'''
        f.check_events(ship,setting,screen,bullets,stats,button,enemies,sb)#调用f模块中的check_event（检验事件）函数
        if stats.game_active:
            '''判断游戏是否为活跃状态，然后执行以下程序'''
            f.update_ship(ship,enemies,bullets,setting,screen,stats,sb)#调用f模块中的update_ship（更新飞船）函数
            f.update_bulllets(bullets,enemies,setting,screen,stats,sb)#调用f模块中的update_bullets（更新子弹）函数
            f.update_enemies(enemies,stats,bullets,ship,setting,screen,sb)#调用f模块中的update_enemies（更新敌人）函数
            f.delete_bullet(bullets)##调用f模块中的delete_bullet（删除子弹）函数
        f.update_screen(screen,setting,ship,bullets,enemies,stats,button,sb)#调用f模块中的update_screen（更新屏幕）函数，不止在游戏活跃状态下更新屏幕
run_game()#运行主函数