#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-20 14:16:01
LastEditTime: 2021-11-20 14:18:26
Description: Equalize Prices Again
FilePath: CF1234A.py
'''


from math import ceil


def func():
    q = int(input())
    for _ in range(q):
        n = int(input())
        price = sum(map(int, input().strip().split()))
        print(ceil(price / n))


if __name__ == '__main__':
    func()
