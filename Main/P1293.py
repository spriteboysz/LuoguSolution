#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-29 23:48:22
LastEditTime: 2022-01-02 17:29:01
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
        cost.append([info[i][2], info[i][1], c])
    city = list(min(cost, key=lambda el: (el[2], el[1])))
    print(city[0], city[2])


if __name__ == '__main__':
    func()
