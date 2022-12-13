'''
title: Analysis of nba players data in nba2k
author: Kang Jingyang
date: 2022-12-13
lastmod: 2022-12-13
description: This project is part of my essay for 概率论与数理统计
'''

import numpy as np
import csv
import unary_linear_regression as Ulr
from player import player


if __name__ == '__main__':
    # 从 CSV 中读取输入，存到 all_players : np.ndarray<player> 中
    all_players = []
    with open('nba2k-full.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            all_players.append(player(row))
            pass
        pass
    all_players = np.array(all_players)
    for guy in all_players:
        if guy.name() == 'Russell Westbrook':
            print(guy.name())
        pass
    pass
