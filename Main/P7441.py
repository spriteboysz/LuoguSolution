#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-09 23:30:14
LastEditTime: 2022-01-09 23:58:30
Description: 「EZEC-7」Erinnerung
FilePath: P7441.py
'''


def func():
    t = int(input())
    for _ in range(t):
        x, y, k = map(int, input().strip().split())
        if x == 0 and y == 0:
            print(0)
        elif x == 0:
            print(0 if k % y else 1)
        elif y == 0:
            print(0 if k % x else 1)
        else:
            print(min(k // x, k // y))


if __name__ == '__main__':
    func()
