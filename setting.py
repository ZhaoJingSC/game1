class Setting():
    def __init__(self):
        self.width=1200
        self.high=600
        self.bg_color=(0,255,255)
        self.ship_limit = 3
        self.ship_type = 1#默认飞船形状为1型
        #设置子弹属性

        self.bullet_allowed=9
        self.lvlup_speed=2
        self.score_lvlup_speed=2

        self.active_setting()
    def active_setting(self):
        self.enemy_flag=1
        self.ship_speed=1.5
        self.bullet_speed = 1
        self.enemy_speed = 1
        self.enemy_down_speed = 2
        self.enemy_score=5


    def lvlup(self):
        self.enemy_down_speed*=self.lvlup_speed
        self.enemy_speed*=self.lvlup_speed
        self.ship_speed*=self.lvlup_speed
        self.bullet_speed*=self.lvlup_speed
    def score_lvlup(self):
        self.enemy_score*=self.score_lvlup_speed