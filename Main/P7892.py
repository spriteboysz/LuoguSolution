#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-16 23:22:35
LastEditTime: 2021-12-16 23:33:33
Description: R.I.P
FilePath: P7892.py
'''


def func():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().strip().split())
        for i in range(int(n ** 0.5) + 1, 0, -1):
            if n % i == 0:
                break
        if (n // i + i + 2) * 2 <= m:
            print("Good")
        else:
            print("Miss")


if __name__ == '__main__':
    func()
