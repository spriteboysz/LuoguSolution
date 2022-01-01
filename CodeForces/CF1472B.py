#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-25 22:55:24
LastEditTime: 2021-11-25 23:00:55
Description: Fair Division
FilePath: CF1472B.py
'''


def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        candies = list(map(int, input().strip().split()))
        a, b = candies.count(1), candies.count(2)
        if b % 2 == 0:
            if a % 2 == 0:
                print("YES")
            else:
                print("NO")
        else:
            if a >= 2 and a % 2 == 0:
                print("YES")
            else:
                print("NO")


if __name__ == '__main__':
    func()
