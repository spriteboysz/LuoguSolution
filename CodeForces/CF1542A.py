#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-14 18:07:47
LastEditTime: 2021-11-14 22:04:08
Description: Odd Set
FilePath: CF1542A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        num = list(map(int, input().strip().split()))
        if len(list((filter(lambda el: el % 2 == 0, num)))) == n:
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    func()
