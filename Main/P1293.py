#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-29 23:48:22
LastEditTime: 2021-12-30 22:41:07
Description: 班级聚会
FilePath: P1293.py
'''


def func():
    info, cost = [], []
    while True:
        n, distance, city = input().strip().split()
        info.append([int(n), int(distance), city])
        if city == "Moscow":
            break

    for i in range(len(info)):
        c = 0
        for j in range(len(info)):
            c += abs(info[j][1] - info[i][1]) * info[j][0]
        cost.append([info[i][2], c])
    print(" ".join(map(str, min(cost, key=lambda el: (el[1], el[0])))))


if __name__ == '__main__':
    func()
