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
from attempt import attempt


if __name__ == '__main__':
    # 从 CSV 中读取输入，存到 all_players : np.ndarray<player> 中
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
    for att in all_attempts:
        print(att.type)
        pass
    # ============================================ Finish input and Parsing
    # get percentages of 3 types of attempts:
    #     un_known, close, mid_range, three_point
    attempt_in_a_game = np.array([0, 0, 0, 0, 0])
    pass
