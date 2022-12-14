'''
title: Analysis of Kobe Bryant's performance in the play-off against ORL
author: Kang Jingyang
date: 2022-12-13
lastmod: 2022-12-13
description: This project is part of my essay for 概率论与数理统计
'''

import numpy as np
import csv
import unary_linear_regression as Ulr
from attempt import attempt


if __name__ == '__main__':
    # 从 CSV 中读取输入
    all_attempts = []
    with open('kobe_basket.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if row[0] == 'vs':
                continue
            all_attempts.append(attempt(row))
            pass
        pass
    all_attempts = np.array(all_attempts)
    # ============================================ Finish input and Parsing
    # get percentages of 3 types of attempts:
    #     un_known, close, mid_range, three_point
    attempt_in_a_game = np.empty(5)               # 总出手数
    attempt_in_a_game.fill(0)
    percentage_in_a_game = np.empty(5)            # 总命中率
    percentage_in_a_game.fill(0)
    three_point_in_a_game = np.empty(5)           # 三分球出手数
    three_point_in_a_game.fill(0)
    three_point_made_in_a_game = np.empty(5)      # 三分球命中数
    three_point_made_in_a_game.fill(0)
    three_point_percentage = np.empty(5)          # 三分球命中率
    three_point_percentage.fill(0)
    mid_range_in_a_game = np.empty(5)             # 中距离出手数
    mid_range_in_a_game.fill(0)
    mid_range_made_in_a_game = np.empty(5)        # 中距离命中数
    mid_range_made_in_a_game.fill(0)
    mid_range_percentage = np.empty(5)            # 中距离命中率
    mid_range_percentage.fill(0)
    close_in_a_game = np.empty(5)                 # 近距离出售数
    close_in_a_game.fill(0)
    close_made_in_a_game = np.empty(5)            # 近距离命中数
    close_made_in_a_game.fill(0)
    close_percentage = np.empty(5)                # 近距离命中率
    close_percentage.fill(0)
    for att in all_attempts:
        attempt_in_a_game[att.game-1] += 1
        if att.type == 'close':
            close_in_a_game[att.game-1] += 1
            if att.made is True:
                close_made_in_a_game[att.game-1] += 1
        elif att.type == 'mid_range':
            mid_range_in_a_game[att.game-1] += 1
            if att.made is True:
                mid_range_made_in_a_game[att.game-1] += 1
        elif att.type == 'three_point':
            three_point_in_a_game[att.game-1] += 1
            if att.made is True:
                three_point_made_in_a_game[att.game-1] += 1
        else:
            print('something wrong')
            exit()
        pass
    for i in range(5):
        three_point_percentage[i] = three_point_made_in_a_game[i] / \
            three_point_in_a_game[i]
        mid_range_percentage[i] = mid_range_made_in_a_game[i] / \
            mid_range_in_a_game[i]
        close_percentage[i] = close_made_in_a_game[i] / \
            close_in_a_game[i]
        percentage_in_a_game[i] = (
            three_point_made_in_a_game[i] +
            mid_range_made_in_a_game[i] +
            close_made_in_a_game[i]
        ) / attempt_in_a_game[i]
        pass
    print("percentage_in_a_game")
    print(percentage_in_a_game)
    print("three_point_percentage")
    print(three_point_percentage)
    print("mid_range_percentage")
    print(mid_range_percentage)
    print("close_percentage")
    print(close_percentage)
    pass
