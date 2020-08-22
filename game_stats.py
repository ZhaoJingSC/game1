class GameStats():
    '''创建一个GameStats类,表示游戏的各种记录，比如得分，玩家剩余命数等'''
    def __init__(self,setting):
        self.setting=setting
        self.reset_stats()#重置游戏记录的设置
        self.game_active=False#游戏活跃状态默认为False
        self.choice_active=False#游戏选择状态默认为Fasle
        self.high_score=0#游戏最高分默认为0


    def reset_stats(self):
        '''游戏开始需要重置的游戏记录'''
        self.ships_left=self.setting.ship_limit#飞船剩余命数
        self.score = 0#游戏得分默认为0
        self.lvl=1#游戏等级默认为1