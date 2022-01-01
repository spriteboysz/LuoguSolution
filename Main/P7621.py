#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-14 23:00:54
LastEditTime: 2021-12-14 23:14:21
Description: 超市购物
FilePath: P7621.py
'''


def func():
    n = int(input())
    cost = 0
    for _ in range(n):
        price, num = map(float, input().strip().split())
        cost += price * num
    print("%.1f" % (cost * 0.85 * 10 // 1 / 10))


if __name__ == '__main__':
    func()
