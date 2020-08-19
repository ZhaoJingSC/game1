class Setting():
    def __init__(self):
        self.width=1200
        self.high=600
        self.bg_color=(0,255,255)
        self.ship_limit = 3
        #设置子弹属性

        self.bullet_width=200
        self.bullet_high=50
        self.bullet_color=(255,0,0)
        self.bullet_allowed=5

        self.lvlup_speed=2
        self.score_lvlup_speed=2

        self.active_setting()
    def active_setting(self):
        self.enemy_flag=1
        self.ship_speed=1.5
        self.bullet_speed = 1
        self.enemy_speed = 10
        self.enemy_down_speed = 2
        self.enemy_score=5


    def lvlup(self):
        self.enemy_down_speed*=self.lvlup_speed
        self.enemy_speed*=self.lvlup_speed
        self.ship_speed*=self.lvlup_speed
        self.bullet_speed*=self.lvlup_speed
    def score_lvlup(self):
        self.enemy_score*=self.score_lvlup_speed