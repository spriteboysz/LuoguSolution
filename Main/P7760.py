#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-14 23:59:09
LastEditTime: 2021-12-15 22:24:22
Description: Tuna
FilePath: P7760.py
'''


def func():
    n = int(input())
    x = int(input())
    cost = 0
    for _ in range(n):
        p1, p2 = map(int, input().strip().split())
        if abs(p1 - p2) <= x:
            cost += max(p1, p2)
        else:
            cost += int(input())
    print(cost)


if __name__ == '__main__':
    func()
