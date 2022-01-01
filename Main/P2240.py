#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-06 23:23:19
LastEditTime: 2021-12-06 23:33:46
Description: 部分背包问题
FilePath: P2240.py
'''


def func():
    n, t = map(int, input().strip().split())
    coins = []
    for _ in range(n):
        m, v = map(int, input().strip().split())
        coins.append([m, v])
    coins = sorted(coins, key=lambda el: el[1]/el[0], reverse=True)
    weight, value = 0, 0
    for el in coins:
        if weight + el[0] <= t:
            weight += el[0]
            value += el[1]
        else:
            value += el[1] * (t - weight) / el[0]
            break
    print("%.2f" % value)


if __name__ == '__main__':
    func()
