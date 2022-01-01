#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-01 16:19:11
LastEditTime: 2022-01-01 22:34:53
Description: 过河卒
FilePath: P1002.py
'''


def func():
    horse = [[0, 0], [-2, 1], [-1, 2], [1, 2],
             [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]
    n, m, x, y = map(lambda el: int(el) + 2, input().strip().split())
    chess = [[0] * (m + 3) for _ in range(n + 3)]
    chess[2][2] = 1
    for item in horse:
        chess[x + item[0]][y + item[1]] = "h"

    for i in range(2, n + 1):
        for j in range(2, m + 1):
            if chess[i][j] != "h" and chess[i][j] != 1:
                if chess[i - 1][j] == "h":
                    chess[i][j] = chess[i][j - 1]
                elif chess[i][j - 1] == "h":
                    chess[i][j] = chess[i - 1][j]
                else:
                    chess[i][j] = chess[i - 1][j] + chess[i][j - 1]

    print(chess[n][m])


if __name__ == '__main__':
    func()
