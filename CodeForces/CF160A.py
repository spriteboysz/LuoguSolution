#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-03 22:30:09
LastEditTime: 2021-12-03 22:48:56
Description: Twins
FilePath: CF160A.py
'''


def func():
    n = int(input())
    coins = list(sorted(map(int, input().strip().split())))
    total = sum(coins)
    for i in range(n):
        current = sum(coins[:(i+1)])
        if current > total - current:
            print(i + 1)
            break
    else:
        print(-1)


if __name__ == '__main__':
    func()
