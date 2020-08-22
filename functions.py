import pygame
import sys
from bullet import Bullet
from enemy import Enemy
from time import sleep
from ship import Ship
def check_events(ship,setting,screen,bullets,stats,button,enemies,sb):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                ship.right=True
            if event.key==pygame.K_LEFT:
                ship.left=True
            if event.key==pygame.K_SPACE and len(bullets)<setting.bullet_allowed and stats.game_active==True:
                if setting.ship_type==1:
                    new_bullet=Bullet(setting,ship,screen)
                    bullets.add(new_bullet)
                if setting.ship_type==2:
                    for i in range(3):
                        bullet=Bullet(setting,ship,screen)
                        bullet.rect.x=ship.rect.x+(i-1)*bullet.rect.width
                        bullets.add(bullet)
                if setting.ship_type==3:
                    for i in range(3):
                        bullet=Bullet(setting,ship,screen)
                        bullet.y=ship.rect.y-(i+1)*bullet.rect.height
                        bullet.rect.y=bullet.y
                        bullets.add(bullet)
            if event.key==pygame.K_ESCAPE:
                sys.exit()
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                ship.right=False
            if event.key==pygame.K_LEFT:
                ship.left=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            if button.rect.collidepoint(mouse_x,mouse_y) and stats.game_active==False:
                stats.choice_active=True
            if get_ship1_rect(screen,setting).collidepoint(mouse_x,mouse_y) and stats.game_active==False and stats.choice_active==True:
                setting.ship_type=1
                reset_stats(stats, sb, enemies, bullets, setting, screen, ship)
            if get_ship2_rect(screen, setting).collidepoint(mouse_x,mouse_y) and stats.game_active == False and stats.choice_active == True:
                setting.ship_type = 2
                reset_stats(stats, sb, enemies, bullets, setting, screen, ship)
            if get_ship3_rect(screen, setting).collidepoint(mouse_x,mouse_y) and stats.game_active == False and stats.choice_active == True:
                setting.ship_type = 3
                reset_stats(stats, sb, enemies, bullets, setting, screen, ship)



def update_screen(screen,setting,ship,bullets,enemies,stats,button,sb):
    screen.fill(setting.bg_color)
    if stats.game_active==True and stats.choice_active==False:
        ship.blitme()
        sb.blit_score()
        sb.blit_high_score()
        sb.blit_lvl()
        sb.blit_ship()
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        enemies.draw(screen)
    if stats.game_active==False and stats.choice_active==False:
        button.draw_button()
    if stats.game_active==False and stats.choice_active==True:
        ship.choice_ship_image()
    pygame.display.flip()

def delete_bullet(bullets):
    for bullet in bullets.copy():
        if bullet.rect.y<=0:
            bullets.remove(bullet)

def create_enemis(setting,screen,enemies):
    enemy=Enemy(screen,setting)
    enemy_width=enemy.rect.width
    n=(setting.width-4*enemy_width)/(enemy_width*2)
    for m in range(5):
        for i in range(int(n)):
            new_enemy=Enemy(screen,setting)
            new_enemy.x=enemy_width+i*2*enemy_width
            new_enemy.rect.x=new_enemy.x#十分关键的一行数据，不然会出现赋值错误
            new_enemy.rect.y=2*enemy.rect.height+m*2*enemy.rect.height
            enemies.add(new_enemy)

def update_enemies(enemies,stats,bullets,ship,setting,screen,sb):
    check_enemies_edge(enemies)
    enemies.update()
    for enemy in enemies.sprites():
        if enemy.rect.bottom>=enemy.screen_rect.bottom:
            ship_hit(stats, bullets, enemies, ship, setting, screen,sb)
            break


def check_enemies_edge(enemies):
    for enemy in enemies.sprites():
        if enemy.check_edge():
            for enemy in enemies.sprites():
                enemy.rect.y+=enemy.down_speed
            enemy.setting.enemy_flag *= -1
            break
def update_bulllets(bullets,enemies,setting,screen,stats,sb):
    bullets.update()
    collisions=pygame.sprite.groupcollide(bullets,enemies,True,True)
    if collisions:
        for enemy in collisions.values():
            stats.score+=setting.enemy_score*len(enemy)
        sb.prep_score()
    if stats.score>stats.high_score:
        stats.high_score=stats.score
        sb.prep_high_score()
    if len(enemies)==0:
        bullets.empty()
        setting.lvlup()
        setting.score_lvlup()
        create_enemis(setting, screen, enemies)
        stats.lvl+=1
        sb.prep_lvl()


def update_ship(ship,enemies,bullets,setting,screen,stats,sb):
    ship.update_ship()
    if pygame.sprite.spritecollideany(ship,enemies):
        ship_hit(stats,bullets,enemies,ship,setting,screen,sb)

def ship_hit(stats,bullets,enemies,ship,setting,screen,sb):
    if stats.ships_left>0:
        stats.ships_left -= 1
        sb.prep_ship()
        bullets.empty()
        enemies.empty()
        ship.center()
        sleep(1)
        create_enemis(setting, screen, enemies)
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)

def get_ship1_rect(screen,setting):
    ship1=Ship(screen,setting)
    ship1.image = pygame.image.load('image\ship1.bmp')
    ship1.rect.centery = ship1.screen_rect.centery
    ship1.rect.x = ship1.screen_rect.centerx - 10  * ship1.rect.width
    return ship1.rect

def get_ship2_rect(screen,setting):
    ship2=Ship(screen,setting)
    ship2.image = pygame.image.load('image\ship2.bmp')
    ship2.rect.centery = ship2.screen_rect.centery
    ship2.rect.x = ship2.screen_rect.centerx
    return ship2.rect

def get_ship3_rect(screen,setting):
    ship3=Ship(screen,setting)
    ship3.image = pygame.image.load('image\ship2.bmp')
    ship3.rect.centery = ship3.screen_rect.centery
    ship3.rect.x = ship3.screen_rect.centerx + 10  * ship3.rect.width
    return ship3.rect

def reset_stats(stats,sb,enemies,bullets,setting,screen,ship):
    pygame.mouse.set_visible(False)
    stats.reset_stats()
    sb.prep_score()
    sb.prep_lvl()
    sb.prep_ship()
    stats.game_active = True
    stats.choice_active = False
    enemies.empty()
    bullets.empty()
    setting.active_setting()
    create_enemis(setting, screen, enemies)
    ship.center()