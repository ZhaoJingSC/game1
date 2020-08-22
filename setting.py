class Setting():
    '''创建一个Setting类，包含游戏的各种设置'''
    def __init__(self):
        self.width=1200#屏幕宽
        self.high=600#屏幕高
        self.bg_color=(0,255,255)#屏幕背景色
        self.ship_limit = 3#玩家开始拥有的命数
        self.ship_type = 1#默认飞船形状为1型

        #设置子弹属性
        self.bullet_allowed=9#允许最大子弹数
        self.lvlup_speed=2#升级后子弹加快的速度

        self.score_lvlup_speed=2#升级后得分增加的速度

        self.active_setting()#游戏动态设置

    def active_setting(self):
        '''游戏的动态设置'''
        self.enemy_flag=1#敌人移动的方向flag
        self.ship_speed=1.5#飞船速度
        self.bullet_speed = 1#子弹速度
        self.enemy_speed = 1#敌人左右移动速度
        self.enemy_down_speed = 2#敌人下移速度
        self.enemy_score=5#每个敌人得分

    def lvlup(self):
        '''升级后的速度变化'''
        self.enemy_down_speed*=self.lvlup_speed#敌人下一东渡增加
        self.enemy_speed*=self.lvlup_speed#敌人左右移动速度增加
        self.ship_speed*=self.lvlup_speed#飞船速度增加
        self.bullet_speed*=self.lvlup_speed#子弹速度增加

    def score_lvlup(self):
        '''升级后得分变化'''
        self.enemy_score*=self.score_lvlup_speed