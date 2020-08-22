import pygame
import sys
from bullet import Bullet
from enemy import Enemy
from time import sleep
from ship import Ship
def check_events(ship,setting,screen,bullets,stats,button,enemies,sb):
    '''检出事件的函数，包括键盘和鼠标'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #事件为退出则关闭窗口
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            #键盘按键按下的事件
            if event.key==pygame.K_RIGHT:
                #右键按下，飞船右移flag为True
                ship.right=True
            if event.key==pygame.K_LEFT:
                #左键按下，飞船左移flag为True
                ship.left=True
            if event.key==pygame.K_SPACE and len(bullets)<setting.bullet_allowed and stats.game_active==True:
                #空格建按下，并且游戏为活跃状态且当前子弹数不超过最大子弹数，则发射子弹
                if setting.ship_type==1:
                    #发射1型子弹
                    new_bullet=Bullet(setting,ship,screen)
                    bullets.add(new_bullet)
                if setting.ship_type==2:
                    # 发射2型子弹
                    for i in range(3):
                        bullet=Bullet(setting,ship,screen)
                        bullet.rect.x=ship.rect.x+(i-1)*bullet.rect.width
                        bullets.add(bullet)
                if setting.ship_type==3:
                    # 发射3型子弹
                    for i in range(3):
                        bullet=Bullet(setting,ship,screen)
                        bullet.y=ship.rect.y-(i+1)*bullet.rect.height
                        bullet.rect.y=bullet.y
                        bullets.add(bullet)
            if event.key==pygame.K_ESCAPE:
                #按ESC退出
                sys.exit()
        elif event.type==pygame.KEYUP:
            # 键盘按键松开的事件
            if event.key==pygame.K_RIGHT:
                #右键松开，飞船右移flag为False
                ship.right=False
            if event.key==pygame.K_LEFT:
                # 左键松开，飞船左移flag为False
                ship.left=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            # 鼠标点击的事件
            mouse_x,mouse_y=pygame.mouse.get_pos()#获取鼠标点击坐标
            if button.rect.collidepoint(mouse_x,mouse_y) and stats.game_active==False:
                #鼠标点击开始按钮，并且当前游戏活跃状态为False，游戏变为活跃状态
                stats.choice_active=True
            if get_ship1_rect(screen,setting).collidepoint(mouse_x,mouse_y) and stats.game_active==False and stats.choice_active==True:
                # 鼠标点击1型飞船，并且当前游戏活跃状态为False，游戏选择状态为True，选择1型飞船
                setting.ship_type=1
                reset_stats(stats, sb, enemies, bullets, setting, screen, ship)#重置游戏设置
            if get_ship2_rect(screen, setting).collidepoint(mouse_x,mouse_y) and stats.game_active == False and stats.choice_active == True:
                # 鼠标点击2型飞船，并且当前游戏活跃状态为False，游戏选择状态为True，选择2型飞船
                setting.ship_type = 2
                reset_stats(stats, sb, enemies, bullets, setting, screen, ship)#重置游戏设置
            if get_ship3_rect(screen, setting).collidepoint(mouse_x,mouse_y) and stats.game_active == False and stats.choice_active == True:
                # 鼠标点击3型飞船，并且当前游戏活跃状态为False，游戏选择状态为True，选择3型飞船
                setting.ship_type = 3
                reset_stats(stats, sb, enemies, bullets, setting, screen, ship)#重置游戏设置

def update_screen(screen,setting,ship,bullets,enemies,stats,button,sb):
    '''更新屏幕'''
    screen.fill(setting.bg_color)#填充背景色
    if stats.game_active==True and stats.choice_active==False:
        #游戏为活跃状态，且选择状态关闭
        ship.blitme()#画出飞船
        sb.blit_score()#画出得分
        sb.blit_high_score()#画出最高分
        sb.blit_lvl()#画出等级
        sb.blit_ship()#画出飞船

        #画出射出子弹
        for bullet in bullets.sprites():
            bullet.draw_bullet()

        enemies.draw(screen)#画出敌人
    if stats.game_active==False and stats.choice_active==False:
        #游戏为非活跃状态，选择状态也为非活状态时画出开始按钮
        button.draw_button()
    if stats.game_active==False and stats.choice_active==True:
        # 游戏为非活跃状态，选择状态也为活状态时画出选择飞船图像
        ship.choice_ship_image()
    pygame.display.flip()#让绘制的屏幕可见

def delete_bullet(bullets):
    '''如果子弹飞出边界，删除子弹'''
    for bullet in bullets.copy():
        if bullet.rect.y<=0:
            bullets.remove(bullet)

def create_enemies(setting,screen,enemies):
    '''创建敌人'''
    enemy=Enemy(screen,setting)
    enemy_width=enemy.rect.width
    n=(setting.width-4*enemy_width)/(enemy_width*2)#计算屏幕一行能容下敌人最大数量
    for m in range(5):
        for i in range(int(n)):
            new_enemy=Enemy(screen,setting)
            new_enemy.x=enemy_width+i*2*enemy_width
            new_enemy.rect.x=new_enemy.x#这里用x去表示敌人位置，再赋值给rect.x，不然会出现赋值错误
            new_enemy.rect.y=2*enemy.rect.height+m*2*enemy.rect.height
            enemies.add(new_enemy)

def update_enemies(enemies,stats,bullets,ship,setting,screen,sb):
    '''更新敌人位置'''
    check_enemies_edge(enemies)
    enemies.update()
    for enemy in enemies.sprites():
        if enemy.rect.bottom>=enemy.screen_rect.bottom:
            '''敌人到达屏幕底端，调用函数ship_hit,重置界面'''
            ship_hit(stats, bullets, enemies, ship, setting, screen,sb)
            break


def check_enemies_edge(enemies):
    '''检验敌人是否触碰屏幕左右边界，是的话，下移并且改变移动方向'''
    for enemy in enemies.sprites():
        if enemy.check_edge():
            for enemy in enemies.sprites():
                enemy.rect.y+=enemy.down_speed
            enemy.setting.enemy_flag *= -1
            break

def update_bulllets(bullets,enemies,setting,screen,stats,sb):
    '''更新子弹'''
    bullets.update()

    #检验子弹和敌人是否碰撞，是的话计算的分，删除该子弹和敌人
    collisions=pygame.sprite.groupcollide(bullets,enemies,True,True)
    if collisions:
        for enemy in collisions.values():
            stats.score+=setting.enemy_score*len(enemy)
        sb.prep_score()#重置得分图像
    if stats.score>stats.high_score:
        '''得分超过最高分，重置最高分图像'''
        stats.high_score=stats.score
        sb.prep_high_score()
    if len(enemies)==0:
        '''敌人消灭完，升级并且重新生成敌人'''
        bullets.empty()
        setting.lvlup()
        setting.score_lvlup()
        create_enemies(setting, screen, enemies)
        stats.lvl+=1
        sb.prep_lvl()


def update_ship(ship,enemies,bullets,setting,screen,stats,sb):
    '''更新飞船位置'''
    ship.update_ship()
    if pygame.sprite.spritecollideany(ship,enemies):
        '''检验飞船与敌人是否碰撞，是的话，调用函数ship_hit，重置界面'''
        ship_hit(stats,bullets,enemies,ship,setting,screen,sb)

def ship_hit(stats,bullets,enemies,ship,setting,screen,sb):
    '''飞船坠毁，命数减一，重新生成敌人，飞船居中'''
    if stats.ships_left>0:
        '''还有剩余命数，命数减一'''
        stats.ships_left -= 1
        sb.prep_ship()
        bullets.empty()#清空当前子弹
        enemies.empty()#清空当前敌人
        ship.center()#居中飞船
        sleep(1)#延时1se
        create_enemies(setting, screen, enemies)#创建新的敌人
    else:
        '''无剩余命数，游戏变为非活跃状态，显示鼠标'''
        stats.game_active=False
        pygame.mouse.set_visible(True)

def get_ship1_rect(screen,setting):
    '''获取ship1的图像信息'''
    ship1=Ship(screen,setting)
    ship1.image = pygame.image.load('image\ship1.bmp')
    ship1.rect.centery = ship1.screen_rect.centery
    ship1.rect.x = ship1.screen_rect.centerx - 10  * ship1.rect.width
    return ship1.rect

def get_ship2_rect(screen,setting):
    '''获取ship2的图像信息'''
    ship2=Ship(screen,setting)
    ship2.image = pygame.image.load('image\ship2.bmp')
    ship2.rect.centery = ship2.screen_rect.centery
    ship2.rect.x = ship2.screen_rect.centerx
    return ship2.rect

def get_ship3_rect(screen,setting):
    '''获取ship3的图像信息'''
    ship3=Ship(screen,setting)
    ship3.image = pygame.image.load('image\ship2.bmp')
    ship3.rect.centery = ship3.screen_rect.centery
    ship3.rect.x = ship3.screen_rect.centerx + 10  * ship3.rect.width
    return ship3.rect

def reset_stats(stats,sb,enemies,bullets,setting,screen,ship):
    '''重置游戏'''
    pygame.mouse.set_visible(False)#隐藏鼠标
    stats.reset_stats()#重置游戏记录
    sb.prep_score()#重置得分图像
    sb.prep_lvl()#重置等级图像
    sb.prep_ship()#重置飞船图像
    stats.game_active = True#游戏变为活跃状态
    stats.choice_active = False#选择状态非活跃
    enemies.empty()#清空敌人
    bullets.empty()#清空子弹
    setting.active_setting()#重置游戏动态设置
    create_enemies(setting, screen, enemies)#创建新的敌人
    ship.center()#飞船居中