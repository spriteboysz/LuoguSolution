#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-16 23:23:06
LastEditTime: 2021-11-16 23:24:43
Description: Three Piles of Candies
FilePath: CF1196A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().strip().split())
        print((a + b + c) // 2)


if __name__ == '__main__':
    func()
