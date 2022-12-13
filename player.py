class player:
    def __init__(self, info: list) -> None:
        self.info = info
        pass

    def name(self) -> str:
        '''
        球员名字
        '''
        return self.info[0]

    def rating(self) -> int:
        '''
        球员能力值
        '''
        return self.info[1]

    def number(self) -> int:
        '''
        球衣号码
        '''
        return int(self.info[2][1:])

    def team(self) -> str:
        '''
        球队名字
        '''
        return self.info[3]

    def position(self) -> str:
        '''
        球员位置
        '''
        return self.info[4]

    def game_version(self) -> str:
        '''
        游戏版本
        '''
        return self.info[-1]
    pass
