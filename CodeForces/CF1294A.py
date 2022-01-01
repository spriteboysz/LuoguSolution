#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-11 23:15:28
LastEditTime: 2021-11-11 23:17:58
Description: Collecting Coins
FilePath: CF1294A.py
'''


def func():
    n = int(input())
    for _ in range(n):
        a, b, c, n = map(int, input().strip().split())
        if (a + b + c + n) % 3 == 0 and (a + b + c + n) // 3 >= max(a, b, c):
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    func()
