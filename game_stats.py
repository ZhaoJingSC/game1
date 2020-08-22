class GameStats():
    def __init__(self,setting):
        self.setting=setting
        self.reset_stats()#为什么要这么写代码
        self.game_active=False
        self.choice_active=False
        self.high_score=0


    def reset_stats(self):
        self.ships_left=self.setting.ship_limit
        self.score = 0
        self.lvl=1