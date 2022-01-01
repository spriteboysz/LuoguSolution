#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-13 23:16:13
LastEditTime: 2021-12-13 23:29:16
Description: 混合牛奶 Mixing Milk
FilePath: P1208.py
'''


def func():
    n, m = map(int, input().strip().split())
    farmers = []
    for _ in range(m):
        farmers.append(tuple(map(int, input().strip().split())))

    farmers = sorted(farmers, key=lambda el: el[0])
    milk, cost = 0, 0
    for el in farmers:
        if milk + el[1] <= n:
            milk += el[1]
            cost += el[0] * el[1]
        else:
            cost += el[0] * (n - milk)
            break
    print(cost)


if __name__ == '__main__':
    func()
