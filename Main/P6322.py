#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-30 23:30:22
LastEditTime: 2021-12-30 23:45:03
Description: PRSTENI
FilePath: P6322.py
'''


from math import gcd


def func():
    n = int(input())
    radius = list(map(int, input().strip().split()))
    turn = []
    for i in range(1, n):
        g = gcd(radius[i], radius[0])
        turn.append(str(radius[0]//g) + "/" + str(radius[i]//g))
    print("\n".join(turn))


if __name__ == '__main__':
    func()
