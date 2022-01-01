#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-07 23:11:12
LastEditTime: 2021-12-07 23:25:13
Description: 旗鼓相当的对手 - 加强版
FilePath: P5741.py
'''


def func():
    n = int(input())
    info = []
    for _ in range(n):
        name, *point = input().strip().split()
        point = list(map(int, point))
        point.append(sum(point))
        info.append([name, point])

    for i in range(n - 1):
        for j in range(i + 1, n):
            if abs(info[i][1][0] - info[j][1][0]) <= 5 and abs(info[i][1][1] - info[j][1][1]) <= 5 and abs(info[i][1][2] - info[j][1][2]) <= 5 and abs(info[i][1][3] - info[j][1][3]) <= 10:
                print(info[i][0], info[j][0])


if __name__ == '__main__':
    func()
