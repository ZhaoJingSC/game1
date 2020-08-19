import pygame
from setting import Setting
from ship import Ship
from game_stats import GameStats
from button import Button
import functions as f
from pygame.sprite import Group
from score_board import ScoreBoard
def run_game():
    pygame.init()
    setting=Setting()
    screen=pygame.display.set_mode((setting.width,setting.high))
    pygame.display.set_caption("game1")
    button=Button(screen,'Start')
    ship=Ship(screen,setting)
    bullets=Group()
    enemies=Group()
    stats=GameStats(setting)
    f.create_enemis(setting, screen, enemies)
    sb=ScoreBoard(setting,screen,stats)
    while True:
        f.check_events(ship,setting,screen,bullets,stats,button,enemies,sb)
        if stats.game_active:
            f.update_ship(ship,enemies,bullets,setting,screen,stats,sb)
            f.update_bulllets(bullets,enemies,setting,screen,stats,sb)
            f.update_enemies(enemies,stats,bullets,ship,setting,screen,sb)
            f.delete_bullet(bullets)
        f.update_screen(screen,setting,ship,bullets,enemies,stats,button,sb)#放在游戏活跃之外
run_game()
