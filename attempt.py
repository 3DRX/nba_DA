class attempt:
    def __init__(self, ipt: list) -> None:
        self.vs = ipt[0]
        self.game = int(ipt[1])
        if len(ipt[2]) == 1:
            self.quarter = int(ipt[2])
            pass
        else:
            self.quarter = 4+int(ipt[2][0])
        self.time = ipt[3]
        self.description: str = ipt[4]
        self.type = 'un_known'  # un_known, close, mid_range, three_point
        if ipt[5] == 'H':
            self.made = True
            pass
        else:
            self.made = False
            pass
        self.__parse_description()
        pass

    def __parse_description(self) -> None:
        if self.type != 'un_known':
            return
        desc: list[str] = []
        if self.game == 3:
            for word in self.description.split(' '):
                if word[0] == 'S':
                    break
                elif word[0] != 'B':
                    desc.append(word)
                    pass
                pass
            pass
        else:
            for word in self.description.split(' '):
                if word[0] != 'K' and word[0] != 'B' and word[0] != 'm':
                    desc.append(word)
                    pass
                pass
            pass
        for word in desc:
            word = word.lower()
            if word == 'layup' or word == 'dunk':
                self.type = 'close'
                return
            elif word == '3pt':
                self.type = 'three_point'
                return
            pass
        if self.type == 'un_known':
            self.type = 'mid_range'
            return
        pass
    pass
